import uuid

from tests.integration.http.conftest import RequestResponseLogger


def test_create_collection(client):
    """Test creating a new collection"""
    with RequestResponseLogger("Create Collection") as _:
        payload = {
            "name": "Test Collection Creation",
            "description": "Desc"
        }

        response = client.session.post(
            f"{client.base_url}/collections",
            headers=client.get_headers(),
            json=payload
        )
        assert response.status_code == 200

        data = response.json()
        coll_id = data["results"]["id"]
        assert coll_id is not None, "No collection_id returned"

        # Cleanup
        client.session.delete(
            f"{client.base_url}/collections/by-id/{coll_id}",
            headers=client.get_headers()
        )


def test_list_collections(client, test_collection):
    """Test listing collections"""
    with RequestResponseLogger("List Collections") as _:
        params = {
            "limit": 10,
            "offset": 0
        }

        response = client.session.get(
            f"{client.base_url}/collections",
            headers=client.get_headers(),
            params=params
        )
        assert response.status_code == 200

        data = response.json()
        results = data["results"]
        assert len(results) >= 1, "Expected at least one collection, none found"


def test_retrieve_collection(client, test_collection):
    """Test retrieving a specific collection"""
    with RequestResponseLogger("Retrieve Collection") as _:
        collection_id = test_collection["collection_id"]
        response = client.session.get(
            f"{client.base_url}/collections/by-id/{collection_id}",
            headers=client.get_headers()
        )
        assert response.status_code == 200

        data = response.json()
        retrieved = data["results"]
        assert retrieved["id"] == collection_id, "Retrieved wrong collection ID"


def test_update_collection(client, test_collection):
    """Test updating a collection"""
    with RequestResponseLogger("Update Collection") as _:
        collection_id = test_collection["collection_id"]
        payload = {
            "name": "Updated Test Collection",
            "description": "Updated description"
        }

        response = client.session.put(
            f"{client.base_url}/collections/by-id/{collection_id}",
            headers=client.get_headers(),
            json=payload
        )
        assert response.status_code == 200

        data = response.json()
        updated = data["results"]
        assert updated["name"] == payload["name"], "Collection name not updated"
        assert updated["description"] == payload["description"], "Collection description not updated"


def test_add_document_to_collection(client, test_collection, test_document_2):
    """Test adding a document to a collection"""
    with RequestResponseLogger("Add Document to Collection") as _:
        collection_id = test_collection["collection_id"]
        response = client.session.post(
            f"{client.base_url}/collections/by-id/{collection_id}/documents/{test_document_2}",
            headers=client.get_headers()
        )
        assert response.status_code == 200

        # Verify by listing documents
        docs_response = client.session.get(
            f"{client.base_url}/collections/by-id/{collection_id}/documents",
            headers=client.get_headers()
        )
        assert docs_response.status_code == 200

        docs_in_collection = docs_response.json()["results"]
        found = any(doc["id"] == test_document_2 for doc in docs_in_collection)
        assert found, "Added document not found in collection"


def test_list_documents_in_collection(client, test_collection, test_document):
    """Test listing documents in a collection"""
    with RequestResponseLogger("List Documents in Collection") as _:
        collection_id = test_collection["collection_id"]
        response = client.session.get(
            f"{client.base_url}/collections/by-id/{collection_id}/documents",
            headers=client.get_headers()
        )
        assert response.status_code == 200

        data = response.json()
        docs_in_collection = data["results"]
        found = any(doc["id"] == test_document for doc in docs_in_collection)
        assert found, "Expected document not found in collection"


def test_remove_document_from_collection(client, test_collection, test_document):
    """Test removing a document from a collection"""
    with RequestResponseLogger("Remove Document from Collection") as _:
        collection_id = test_collection["collection_id"]
        response = client.session.delete(
            f"{client.base_url}/collections/by-id/{collection_id}/documents/{test_document}",
            headers=client.get_headers()
        )
        assert response.status_code == 200

        # Verify removal
        docs_response = client.session.get(
            f"{client.base_url}/collections/by-id/{collection_id}/documents",
            headers=client.get_headers()
        )
        docs_in_collection = docs_response.json()["results"]
        found = any(doc["id"] == test_document for doc in docs_in_collection)
        assert not found, "Document still present in collection after removal"


def test_delete_collection(client):
    """Test deleting a collection"""
    with RequestResponseLogger("Delete Collection") as _:
        # First create a collection
        payload = {"name": "Delete Me",
                   "description": "Delete this collection"}

        create_response = client.session.post(
            f"{client.base_url}/collections",
            headers=client.get_headers(),
            json=payload
        )
        assert create_response.status_code == 200

        coll_id = create_response.json()["results"]["id"]

        # Delete the collection
        delete_response = client.session.delete(
            f"{client.base_url}/collections/by-id/{coll_id}",
            headers=client.get_headers()
        )
        assert delete_response.status_code == 200

        # Verify deletion
        get_response = client.session.get(
            f"{client.base_url}/collections/by-id/{coll_id}",
            headers=client.get_headers()
        )
        assert get_response.status_code == 404, "Collection still exists after deletion"


def test_create_collection_without_name(client):
    """Test creating a collection without a name"""
    with RequestResponseLogger("Create Collection Without Name") as _:
        payload = {
            "name": "",
            "description": "No name"
        }

        response = client.session.post(
            f"{client.base_url}/collections",
            headers=client.get_headers(),
            json=payload
        )
        assert response.status_code in [400, 409, 422], "Expected validation error for empty name"


def test_create_collection_with_invalid_data(client):
    """Test creating a collection with invalid data"""
    with RequestResponseLogger("Create Collection with Invalid Data") as _:
        payload = {
            "name": {"invalid": "type"},  # Invalid type for name field
            "description": 123  # Invalid type for description field
        }

        response = client.session.post(
            f"{client.base_url}/collections",
            headers=client.get_headers(),
            json=payload
        )
        assert response.status_code in [400, 422], "Expected validation error for invalid data types"


def test_filter_collections_by_non_existent_id(client):
    """Test filtering collections by a non-existent ID"""
    with RequestResponseLogger("Filter Collections by Non-existent ID") as _:
        random_id = str(uuid.uuid4())
        params = {"ids": [random_id]}

        response = client.session.get(
            f"{client.base_url}/collections",
            headers=client.get_headers(),
            params=params
        )
        assert response.status_code == 200
        results = response.json()["results"]
        assert len(results) == 0, "Expected no collections for a non-existent ID"


def test_list_documents_in_empty_collection(client):
    """Test listing documents in an empty collection"""
    with RequestResponseLogger("List Documents in Empty Collection") as _:
        # Create a new collection
        create_response = client.session.post(
            f"{client.base_url}/collections",
            headers=client.get_headers(),
            json={"name": "Empty Collection"}
        )
        assert create_response.status_code == 200
        empty_coll_id = create_response.json()["results"]["id"]

        # List documents
        docs_response = client.session.get(
            f"{client.base_url}/collections/by-id/{empty_coll_id}/documents",
            headers=client.get_headers()
        )
        assert docs_response.status_code == 200
        docs = docs_response.json()["results"]
        assert len(docs) == 0, "Expected no documents in a new empty collection"

        # Cleanup
        client.session.delete(
            f"{client.base_url}/collections/by-id/{empty_coll_id}",
            headers=client.get_headers()
        )
