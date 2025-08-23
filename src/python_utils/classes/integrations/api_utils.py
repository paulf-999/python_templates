#!/usr/bin/env python3
"""
Description: Generic API caller (env-driven base URL + optional Bearer token).
Usage:
    - python api_utils.py GET /v1/items
    - python api_utils.py POST /v1/items '{"name": "test"}'

Environment:
    - API_BASE_URL (e.g., https://api.example.com/)
    - API_TOKEN    (optional)
"""

__author__ = ""
__version__ = "1.0"
__date_created__ = ""

import json
import os
import sys
from urllib.parse import urljoin

import requests
from dotenv import load_dotenv

# Custom modules
from python_utils.classes.core.logging_utils import LoggingUtils

# Load .env file
load_dotenv()

# Set up logging using custom shared module
logging_utils = LoggingUtils()
logger = logging_utils.logger


def call_api(method, endpoint, payload=None):
    """Perform an HTTP request using env-based config."""
    base_url = os.getenv("API_BASE_URL")
    if not base_url:
        logger.error("API_BASE_URL must be set in .env")
        sys.exit(1)

    url = urljoin(base_url, endpoint.lstrip("/"))
    headers = {"Accept": "application/json"}
    token = os.getenv("API_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"

    try:
        resp = requests.request(method.upper(), url, json=payload, timeout=30, headers=headers)
        resp.raise_for_status()
    except requests.RequestException as e:
        logger.error(f"Request failed: {e}")
        sys.exit(1)

    try:
        return resp.json()
    except ValueError:
        return {"text": resp.text}


def main():
    """Main entry point of the script."""
    if len(sys.argv) < 3:
        logger.error("Usage: api_utils.py METHOD ENDPOINT [JSON_PAYLOAD]")
        sys.exit(1)

    method, endpoint = sys.argv[1], sys.argv[2]
    payload = None
    if len(sys.argv) > 3:
        raw = sys.argv[3]
        payload = json.load(open(raw[1:], "r", encoding="utf-8")) if raw.startswith("@") else json.loads(raw)

    result = call_api(method, endpoint, payload)
    logger.info(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
