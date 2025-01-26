#!/usr/bin/env python3
"""
Script to fetch and process documents from the Fuse API based on their failure status.

This script:
1. Fetches documents from the Fuse API
2. Filters documents based on configurable failure status criteria:
   - Both extraction and ingestion failed (all_failed)
   - Only ingestion failed (ingestion_failed)
   - Only extraction failed (extraction_failed)
3. Can trigger re-extraction for matching documents using required extraction parameters

Document Status Details:
- ingestion_status: Can be 'failed' among other states
- extraction_status: Can be 'failed' among other states
- A document can have failures in either or both processes

Extraction Process:
When triggering extraction, the following payload is required:
{
    "run_type": "run",
    "settings": {
        "automatic_deduplication": true
    },
    "run_with_orchestration": true
}

These parameters ensure:
- run_type="run": Executes a full extraction run
- automatic_deduplication=true: Enables automatic deduplication during processing
- run_with_orchestration=true: Ensures the extraction is managed by the orchestration system

Usage:
    python document_status_change.py [--filter-type {all_failed|ingestion_failed|extraction_failed}] [--trigger-extraction]

Environment Variables:
    FUSE_API_BASE_URL: Base URL for the Fuse API (default: http://192.168.100.12:7272)
    FUSE_API_BATCH_SIZE: Number of records to fetch per request (default: 100)

Examples:
    # Find documents where both extraction and ingestion failed
    python document_status_change.py --filter-type all_failed

    # Find and re-extract documents where extraction failed
    python document_status_change.py --filter-type extraction_failed --trigger-extraction

    # Find documents where only ingestion failed
    python document_status_change.py --filter-type ingestion_failed
"""

import requests
import logging
import sys
import os
import json
import argparse
from enum import Enum
from typing import List, Dict, Any, Optional, Set
from urllib.parse import urljoin

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    stream=sys.stdout
)
logger = logging.getLogger(__name__)


class FilterType(Enum):
    """Enumeration of available filter types"""
    ALL_FAILED = "all_failed"  # Both failed extraction and failed ingestion
    INGESTION_FAILED = "ingestion_failed"  # Only failed ingestion
    EXTRACTION_FAILED = "extraction_failed"  # Only failed extraction


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

        The extraction process requires specific parameters to be set:
        - run_type="run": Indicates this is a full extraction run
        - automatic_deduplication=true: Enables automatic deduplication
        - run_with_orchestration=true: Ensures orchestrated processing

        Args:
            document_id: UUID of the document to process

        Returns:
            bool: True if extraction was successfully triggered, False otherwise

        Example payload:
            {
                "run_type": "run",
                "settings": {
                    "automatic_deduplication": true
                },
                "run_with_orchestration": true
            }
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


def filter_documents(documents: List[Dict[str, Any]], filter_type: FilterType) -> List[Dict[str, Any]]:
    """
    Filter documents based on specified failure status criteria.

    Args:
        documents: List of document objects from the API
        filter_type: Type of filtering to apply:
            - ALL_FAILED: both extraction and ingestion failed
            - INGESTION_FAILED: only ingestion failed
            - EXTRACTION_FAILED: only extraction failed

    Returns:
        List of documents that match the failure criteria
    """
    filtered_docs = []

    for doc in documents:
        ingestion_failed = doc.get('ingestion_status') == 'failed'
        extraction_failed = doc.get('extraction_status') == 'failed'

        include_doc = False

        if filter_type == FilterType.ALL_FAILED:
            include_doc = ingestion_failed and extraction_failed
        elif filter_type == FilterType.INGESTION_FAILED:
            include_doc = ingestion_failed
        elif filter_type == FilterType.EXTRACTION_FAILED:
            include_doc = extraction_failed

        if include_doc:
            filtered_docs.append(doc)

    return filtered_docs


def process_documents(client: FuseAPIClient, filter_type: FilterType, trigger_extraction: bool = False) -> Dict[
    str, Any]:
    """
    Process documents according to filter criteria and optionally trigger extractions.

    Args:
        client: Initialized FuseAPIClient
        filter_type: Type of filtering to apply
        trigger_extraction: Whether to trigger extraction for matching documents

    Returns:
        Dict containing processing statistics
    """
    stats = {
        'total_processed': 0,
        'matching_documents': 0,
        'successful_extractions': 0,
        'failed_extractions': 0
    }

    matching_docs: List[Dict[str, Any]] = []
    offset = 0

    try:
        # Step 1: Fetch and filter documents
        while True:
            logger.info(f"Fetching documents with offset {offset}")
            response = client.get_documents(offset)

            current_batch = response.get('results', [])
            if not current_batch:
                break

            filtered_batch = filter_documents(current_batch, filter_type)
            matching_docs.extend(filtered_batch)

            total_entries = response.get('total_entries', 0)
            if offset + client.batch_size >= total_entries:
                break

            offset += client.batch_size

        stats['matching_documents'] = len(matching_docs)
        logger.info(f"Found {len(matching_docs)} matching documents")

        # Step 2: Process matching documents
        if trigger_extraction:
            for doc in matching_docs:
                stats['total_processed'] += 1
                if client.trigger_extraction(doc['id']):
                    stats['successful_extractions'] += 1
                else:
                    stats['failed_extractions'] += 1

        # Output matching document IDs and their status
        logger.info("\n=== Matching Documents ===")
        for doc in matching_docs:
            print(f"ID: {doc['id']}")
            print(f"  Title: {doc.get('title', 'N/A')}")
            print(f"  Ingestion Status: {doc.get('ingestion_status', 'N/A')}")
            print(f"  Extraction Status: {doc.get('extraction_status', 'N/A')}")
            print("---")

        return stats

    except Exception as e:
        logger.error(f"An error occurred during processing: {str(e)}")
        raise


def main():
    """Main function to run the document processing script."""
    parser = argparse.ArgumentParser(description='Process documents based on status criteria')
    parser.add_argument('--filter-type', type=str,
                        choices=['all_failed', 'ingestion_failed', 'extraction_failed'],
                        default='ingestion_failed',
                        help='Type of filtering to apply:\n' +
                             '  all_failed: documents where both extraction and ingestion failed\n' +
                             '  ingestion_failed: documents where only ingestion failed\n' +
                             '  extraction_failed: documents where only extraction failed')
    parser.add_argument('--trigger-extraction', action='store_true',
                        help='Trigger extraction for matching documents')
    args = parser.parse_args()

    # Get configuration from environment or use defaults
    base_url = os.getenv('FUSE_API_BASE_URL', 'http://192.168.100.12:7272')
    batch_size = int(os.getenv('FUSE_API_BATCH_SIZE', '100'))

    client = FuseAPIClient(base_url, batch_size)
    filter_type = FilterType(args.filter_type)

    try:
        stats = process_documents(client, filter_type, args.trigger_extraction)

        # Report final statistics
        logger.info("\n=== Processing Complete ===")
        logger.info(f"Total matching documents: {stats['matching_documents']}")
        if args.trigger_extraction:
            logger.info(f"Documents processed: {stats['total_processed']}")
            logger.info(f"Successful extractions: {stats['successful_extractions']}")
            logger.info(f"Failed extractions: {stats['failed_extractions']}")

        # Exit with error if any extractions failed
        if stats['failed_extractions'] > 0:
            logger.warning("Some extractions failed. Check the logs for details.")
            sys.exit(1)

    except Exception as e:
        logger.error(f"Script execution failed: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()