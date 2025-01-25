#!/usr/bin/env python3
"""
Script to fetch documents from the Fuse API based on their extraction and ingestion status,
then trigger extraction for matching documents.

This script:
1. Fetches documents from the Fuse API
2. Filters for specific status criteria
3. Triggers extraction for matching documents
4. Provides comprehensive logging and error handling

Usage:
    python document_status_change.py

    For the object passed to the extraction function, the following attributes are required:
            {
            "run_type": "run",
            "settings": {
                "automatic_deduplication": true
            },
            "run_with_orchestration": true
            }

Environment Variables:
    FUSE_API_BASE_URL: Base URL for the Fuse API (default: http://192.168.100.12:7272)
    FUSE_API_BATCH_SIZE: Number of records to fetch per request (default: 100)
"""

import requests
import logging
import sys
import os
import json
from typing import List, Dict, Any, Optional
from urllib.parse import urljoin

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    stream=sys.stdout
)
logger = logging.getLogger(__name__)


class FuseAPIClient:
    """Client for interacting with the Fuse API."""

    def __init__(self, base_url: str = "http://192.168.100.12:7272", batch_size: int = 100):
        """
        Initialize the Fuse API client.

        Args:
            base_url: Base URL for the Fuse API
            batch_size: Number of records to fetch per request
        """
        self.base_url = base_url.rstrip('/')
        self.batch_size = batch_size
        self.session = requests.Session()
        self.session.headers.update({
            'accept': 'application/json',
            'Content-Type': 'application/json'
        })

    def get_documents(self, offset: int = 0) -> Dict[str, Any]:
        """
        Fetch a batch of documents from the API.

        Args:
            offset: Starting position for fetching documents

        Returns:
            Dict containing the API response

        Raises:
            requests.exceptions.RequestException: If the API request fails
        """
        url = urljoin(self.base_url, '/api/fuse/v3/documents')
        params = {
            'offset': offset,
            'limit': self.batch_size,
            'include_summary_embeddings': 0
        }

        try:
            response = self.session.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to fetch documents at offset {offset}: {str(e)}")
            raise

    def trigger_extraction(self, document_id: str) -> bool:
        """
        Trigger extraction for a specific document.

        Args:
            document_id: UUID of the document to process

        Returns:
            bool: True if extraction was successfully triggered, False otherwise
        """
        url = urljoin(self.base_url, f'/api/fuse/v3/documents/{document_id}/extract')

        payload = {
            "run_type": "run",
            "settings": {
                "automatic_deduplication": True
            },
            "run_with_orchestration": True
        }

        try:
            response = self.session.post(url, json=payload)
            response.raise_for_status()
            logger.info(f"Successfully triggered extraction for document {document_id}")
            return True
        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to trigger extraction for document {document_id}: {str(e)}")
            return False


def filter_documents(documents: List[Dict[str, Any]]) -> List[str]:
    """
    Filter documents based on extraction and ingestion status criteria.

    Args:
        documents: List of document objects from the API

    Returns:
        List of document IDs that match the criteria
    """
    return [
        doc['id'] for doc in documents
        if doc.get('extraction_status') == 'pending' and
           doc.get('ingestion_status') == 'enriched'
    ]


def main():
    """Main function to fetch documents and trigger extractions."""
    # Get configuration from environment or use defaults
    base_url = os.getenv('FUSE_API_BASE_URL', 'http://192.168.100.12:7272')
    batch_size = int(os.getenv('FUSE_API_BATCH_SIZE', '100'))

    client = FuseAPIClient(base_url, batch_size)
    matching_ids: List[str] = []
    offset = 0

    # Statistics for reporting
    total_processed = 0
    successful_extractions = 0
    failed_extractions = 0

    try:
        # Step 1: Fetch and filter documents
        while True:
            logger.info(f"Fetching documents with offset {offset}")
            response = client.get_documents(offset)

            current_batch = response.get('results', [])
            if not current_batch:
                break

            matching_ids.extend(filter_documents(current_batch))

            total_entries = response.get('total_entries', 0)
            if offset + batch_size >= total_entries:
                break

            offset += batch_size

        logger.info(f"Found {len(matching_ids)} documents requiring extraction")

        # Step 2: Trigger extraction for matching documents
        for doc_id in matching_ids:
            total_processed += 1
            if client.trigger_extraction(doc_id):
                successful_extractions += 1
            else:
                failed_extractions += 1

        # Step 3: Report final statistics
        logger.info("=== Extraction Process Complete ===")
        logger.info(f"Total documents processed: {total_processed}")
        logger.info(f"Successful extractions: {successful_extractions}")
        logger.info(f"Failed extractions: {failed_extractions}")

        # If there were any failures, exit with error code
        if failed_extractions > 0:
            logger.warning("Some extractions failed. Check the logs for details.")
            sys.exit(1)

    except Exception as e:
        logger.error(f"An error occurred during processing: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()