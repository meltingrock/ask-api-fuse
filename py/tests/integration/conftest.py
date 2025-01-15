import asyncio
import uuid
from typing import AsyncGenerator, Generator

import pytest

from fuse import FUSEAsyncClient, FUSEClient
from tests.integration.test_chunks import AsyncFUSETestClient  # Import the test client class


from dataclasses import dataclass

@dataclass
class TestConfig:
    base_url: str = "http://localhost:7272"
    api_base_url: str = f"{base_url}/api/v3/fuse"
    index_wait_time: float = 1.0
    chunk_creation_wait_time: float = 1.0
    superuser_email: str = "admin@example.com"
    superuser_password: str = "change_me_immediately"
    test_timeout: int = 30  # seconds

@pytest.fixture(scope="session")
def config() -> TestConfig:
    return TestConfig()


@pytest.fixture(scope="session")
def client(config: TestConfig) -> FUSEClient:
    """Create a shared client instance for the test session."""
    client = FUSEClient(config.api_base_url)
    client.users.login(config.superuser_email, config.superuser_password)
    return client


@pytest.fixture(scope="session")
def mutable_client(config: TestConfig) -> FUSEClient:
    """Create a shared client instance for the test session."""
    return FUSEClient(config.api_base_url)


@pytest.fixture
async def aclient(config: TestConfig) -> AsyncGenerator[FUSEAsyncClient, None]:
    """Create a shared async client instance."""
    client = FUSEAsyncClient(config.api_base_url)
    yield client
    # Add any cleanup if needed


@pytest.fixture
async def test_client():
    """Create an async test client instance."""
    return AsyncFUSETestClient()


@pytest.fixture
async def superuser_client(
    aclient: FUSEAsyncClient, config: TestConfig
) -> AsyncGenerator[FUSEAsyncClient, None]:
    """Creates a superuser client for tests requiring elevated privileges."""
    await aclient.users.login(config.superuser_email, config.superuser_password)
    yield aclient
    await aclient.users.logout()


@pytest.fixture
async def cleanup_documents():
    """Fixture for cleaning up documents after tests."""
    documents = []
    yield documents


@pytest.fixture(scope="session")
def test_document(client: FUSEClient) -> Generator[str, None, None]:
    """Create and yield a test document, then clean up."""
    random_suffix = str(uuid.uuid4())
    doc_resp = client.documents.create(
        raw_text=f"{random_suffix} Test doc for collections",
        run_with_orchestration=False,
    )

    doc_id = doc_resp["results"]["document_id"]
    yield doc_id
    try:
        client.documents.delete(id=doc_id)
    except Exception:
        pass


@pytest.fixture(scope="session")
def test_collection(client: FUSEClient, test_document: str) -> Generator[dict, None, None]:
    """Create a test collection with sample documents and clean up after tests."""
    collection_name = f"Test Collection {uuid.uuid4()}"
    collection_id = client.collections.create(name=collection_name)["results"]["id"]

    docs = [
        {
            "text": f"Aristotle was a Greek philosopher who studied under Plato {str(uuid.uuid4())}.",
            "metadata": {
                "rating": 5,
                "tags": ["philosophy", "greek"],
                "category": "ancient",
            },
        },
        {
            "text": f"Socrates is considered a founder of Western philosophy  {str(uuid.uuid4())}.",
            "metadata": {
                "rating": 3,
                "tags": ["philosophy", "classical"],
                "category": "ancient",
            },
        },
        {
            "text": f"Rene Descartes was a French philosopher. unique_philosopher  {str(uuid.uuid4())}",
            "metadata": {
                "rating": 8,
                "tags": ["rationalism", "french"],
                "category": "modern",
            },
        },
        {
            "text": f"Immanuel Kant, a German philosopher, influenced Enlightenment thought  {str(uuid.uuid4())}.",
            "metadata": {
                "rating": 7,
                "tags": ["enlightenment", "german"],
                "category": "modern",
            },
        },
    ]

    doc_ids = []
    for doc in docs:
        result = client.documents.create(
            raw_text=doc["text"],
            metadata=doc["metadata"],
            run_with_orchestration=False,
        )["results"]
        doc_id = result["document_id"]
        doc_ids.append(doc_id)
        client.collections.add_document(collection_id, doc_id)
    client.collections.add_document(collection_id, test_document)

    yield {"collection_id": collection_id, "document_ids": doc_ids}

    # Cleanup after tests
    try:
        for doc_id in doc_ids:
            try:
                client.documents.delete(id=doc_id)
            except Exception:
                pass
        try:
            client.collections.delete(collection_id)
        except Exception:
                pass
    except Exception as e:
        print(f"Error during test_collection cleanup: {e}")