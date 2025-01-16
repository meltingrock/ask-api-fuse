import asyncio
import uuid
import logging
import json
from datetime import datetime
from typing import AsyncGenerator, Generator, Optional, Any, Dict
import pytest
import httpx
import requests
from requests.auth import AuthBase
from requests.models import Response, PreparedRequest
from httpx import Response as HttpxResponse
from urllib.parse import urlparse, parse_qs

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("http_client")


class TestConfig:
    def __init__(self):
        self.base_url = "http://192.168.100.12:7272/api/fuse/v3"
        self.index_wait_time = 1.0
        self.chunk_creation_wait_time = 1.0
        self.superuser_email = "admin@example.com"
        self.superuser_password = "change_me_immediately"
        self.test_timeout = 30  # seconds


def log_request(request: PreparedRequest, prefix: str = "→") -> None:
    """Log request details"""
    logger.info(f"\n{prefix} Request: {request.method} {request.url}")
    logger.info(f"{prefix} Headers:")
    for key, value in request.headers.items():
        if key.lower() == "authorization":
            value = "Bearer [REDACTED]"
        logger.info(f"{prefix}   {key}: {value}")
    if request.body:
        try:
            body = json.loads(request.body.decode('utf-8'))
            logger.info(f"{prefix} Body:")
            logger.info(f"{prefix}   {json.dumps(body, indent=2)}")
        except (json.JSONDecodeError, AttributeError, UnicodeDecodeError):
            logger.info(f"{prefix} Body: <binary or invalid JSON>")


def log_response(response: Response, prefix: str = "←") -> None:
    """Log response details"""
    logger.info(f"\n{prefix} Response: {response.status_code} {response.reason}")
    logger.info(f"{prefix} Elapsed: {response.elapsed.total_seconds():.3f}s")
    logger.info(f"{prefix} Headers:")
    for key, value in response.headers.items():
        logger.info(f"{prefix}   {key}: {value}")
    try:
        json_response = response.json()
        logger.info(f"{prefix} Body:")
        logger.info(f"{prefix}   {json.dumps(json_response, indent=2)}")
    except json.JSONDecodeError:
        if response.text:
            logger.info(f"{prefix} Body (non-JSON):")
            logger.info(f"{prefix}   {response.text[:1000]}...")
        else:
            logger.info(f"{prefix} Body: <empty>")


async def log_httpx_request(request: httpx.Request, prefix: str = "→") -> None:
    """Log httpx request details"""
    logger.info(f"\n{prefix} Request: {request.method} {request.url}")
    logger.info(f"{prefix} Headers:")
    for key, value in request.headers.items():
        if key.lower() == "authorization":
            value = "Bearer [REDACTED]"
        logger.info(f"{prefix}   {key}: {value}")
    if request.content:
        try:
            body = json.loads(request.content.decode('utf-8'))
            logger.info(f"{prefix} Body:")
            logger.info(f"{prefix}   {json.dumps(body, indent=2)}")
        except (json.JSONDecodeError, AttributeError, UnicodeDecodeError):
            logger.info(f"{prefix} Body: <binary or invalid JSON>")


async def log_httpx_response(response: HttpxResponse, prefix: str = "←") -> None:
    """Log httpx response details"""
    logger.info(f"\n{prefix} Response: {response.status_code} {response.reason_phrase}")
    logger.info(f"{prefix} Headers:")
    for key, value in response.headers.items():
        logger.info(f"{prefix}   {key}: {value}")
    try:
        json_response = response.json()
        logger.info(f"{prefix} Body:")
        logger.info(f"{prefix}   {json.dumps(json_response, indent=2)}")
    except json.JSONDecodeError:
        if response.text:
            logger.info(f"{prefix} Body (non-JSON):")
            logger.info(f"{prefix}   {response.text[:1000]}...")
        else:
            logger.info(f"{prefix} Body: <empty>")


class RequestResponseLogger:
    """Context manager for logging HTTP requests and responses"""

    def __init__(self, operation_name: str):
        self.operation_name = operation_name
        self.start_time = None

    def __enter__(self):
        self.start_time = datetime.now()
        logger.info(f"\n=== Starting {self.operation_name} ===")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        end_time = datetime.now()
        duration = (end_time - self.start_time).total_seconds()
        logger.info(f"=== Completed {self.operation_name} in {duration:.3f}s ===\n")
        if exc_type:
            logger.error(f"Operation failed with error: {exc_val}")


class HTTPClient:
    """HTTP client wrapper to maintain session and authentication with logging"""

    def __init__(self, base_url: str):
        self.base_url = base_url
        self.session = requests.Session()
        self.auth_token = None

    def set_auth_token(self, token: str):
        self.auth_token = token
        self.session.headers.update({"Authorization": f"Bearer {token}"})

    def get_headers(self):
        headers = {
            "Content-Type": "application/json"
        }
        if self.auth_token:
            headers["Authorization"] = f"Bearer {self.auth_token}"
        return headers

    def login(self, email: str, password: str):
        with RequestResponseLogger("Login Operation") as _:
            request = requests.Request(
                'POST',
                f"{self.base_url}/v3/users/login",
                data={
                    "username": email,
                    "password": password
                }
            )
            prepared = self.session.prepare_request(request)
            log_request(prepared)

            response = self.session.send(prepared)
            log_response(response)

            response.raise_for_status()
            token = response.json().get("token")  # Adjust based on your API response
            if token:
                self.set_auth_token(token)
            return response.json()

    async def logout(self):
        if self.auth_token:
            try:
                response = self.session.post(f"{self.base_url}/auth/logout")
                response.raise_for_status()
            finally:
                self.auth_token = None
                self.session.headers.pop("Authorization", None)


class AsyncHTTPClient:
    """Async HTTP client wrapper"""

    def __init__(self, base_url: str):
        self.base_url = base_url
        self.client = httpx.AsyncClient()
        self.auth_token = None

    def get_headers(self):
        headers = {
            "Content-Type": "application/json"
        }
        if self.auth_token:
            headers["Authorization"] = f"Bearer {self.auth_token}"
        return headers

    async def login(self, email: str, password: str):
        with RequestResponseLogger("Async Login Operation") as _:
            request = self.client.build_request(
                'POST',
                f"{self.base_url}/users/login",
                data={"username": email, "password": password}
            )
            await log_httpx_request(request)

            response = await self.client.send(request)
            await log_httpx_response(response)

            response.raise_for_status()
            token = response.json().get("token")
            if token:
                self.auth_token = token
            return response.json()

    async def logout(self):
        if self.auth_token:
            try:
                response = await self.client.post(f"{self.base_url}/auth/logout")
                response.raise_for_status()
            finally:
                self.auth_token = None


@pytest.fixture(scope="session")
def config() -> TestConfig:
    return TestConfig()


@pytest.fixture(scope="session")
async def async_client(config) -> AsyncGenerator[AsyncHTTPClient, None]:
    """Create a shared async client instance for the test session."""
    client = AsyncHTTPClient(config.base_url)
    yield client
    await client.client.aclose()


@pytest.fixture(scope="session")
def client(config) -> HTTPClient:
    """Create a shared client instance for the test session."""
    client = HTTPClient(config.base_url)
    response = client.session.post(
        f"{config.base_url}/users/login",
        data={
            "username": config.superuser_email,
            "password": config.superuser_password
        }
    )
    response.raise_for_status()
    return client


@pytest.fixture(scope="session")
def test_document(client) -> Generator[str, None, None]:
    """Create and yield a test document, then clean up."""
    random_suffix = str(uuid.uuid4())
    response = client.session.post(
        f"{client.base_url}/documents",
        headers=client.get_headers(),
        json={
            "raw_text": f"{random_suffix} Test doc for collections",
            "run_with_orchestration": False
        }
    )
    response.raise_for_status()
    doc_id = response.json()["results"]["document_id"]

    yield doc_id

    # Cleanup
    try:
        client.session.delete(
            f"{client.base_url}/documents/{doc_id}",
            headers=client.get_headers()
        )
    except requests.exceptions.RequestException:
        pass


@pytest.fixture(scope="session")
def test_collection(client, test_document) -> Generator[dict, None, None]:
    """Create a test collection with sample documents and clean up after tests."""
    collection_name = f"Test Collection {uuid.uuid4()}"

    # Create collection
    response = client.session.post(
        f"{client.base_url}/collections",
        headers=client.get_headers(),
        json={"name": collection_name}
    )
    response.raise_for_status()
    collection_id = response.json()["results"]["id"]

    # Sample documents
    docs = [
        {
            "text": f"Aristotle was a Greek philosopher who studied under Plato {str(uuid.uuid4())}.",
            "metadata": {
                "rating": 5,
                "tags": ["philosophy", "greek"],
                "category": "ancient",
            },
        },
        # ... other docs ...
    ]

    doc_ids = []
    for doc in docs:
        # Create document
        doc_response = client.session.post(
            f"{client.base_url}/documents",
            headers=client.get_headers(),
            json={
                "raw_text": doc["text"],
                "metadata": doc["metadata"]
            }
        )
        doc_response.raise_for_status()
        doc_id = doc_response.json()["results"]["document_id"]
        doc_ids.append(doc_id)

        # Add document to collection
        add_response = client.session.post(
            f"{client.base_url}/collections/{collection_id}/documents/{doc_id}",
            headers=client.get_headers()
        )
        add_response.raise_for_status()

    # Add test_document to collection
    client.session.post(
        f"{client.base_url}/collections/{collection_id}/documents/{test_document}",
        headers=client.get_headers()
    )

    yield {"collection_id": collection_id, "document_ids": doc_ids}

    # Cleanup
    try:
        # Remove and delete all documents
        for doc_id in doc_ids:
            try:
                client.session.delete(
                    f"{client.base_url}/documents/{doc_id}",
                    headers=client.get_headers()
                )
            except requests.exceptions.RequestException:
                pass

        # Delete the collection
        try:
            client.session.delete(
                f"{client.base_url}/collections/{collection_id}",
                headers=client.get_headers()
            )
        except requests.exceptions.RequestException:
            pass
    except Exception as e:
        print(f"Error during test_collection cleanup: {e}")