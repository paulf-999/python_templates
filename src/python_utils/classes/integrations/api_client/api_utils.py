#!/usr/bin/env python3
"""
Description: Generic API caller (env-driven base URL + optional Bearer token).
Usage:
    - python api_utils.py GET /v1/items
    - python api_utils.py POST /v1/items '{"name": "test"}'
    - python api_utils.py POST /oauth/token --form '{"grant_type": "client_credentials", "client_id": "abc"}'

Environment:
    - API_BASE_URL (e.g., https://api.example.com/)
    - API_TOKEN    (optional)
"""

__author__ = "Paul Fry"
__version__ = "1.0"
__date_created__ = "11th December 2025"

import json
import sys

import requests
from dotenv import load_dotenv

# Custom modules
from python_utils.classes.core.logging_utils import LoggingUtils
from python_utils.classes.integrations.api_client._api_request_helpers import (
    build_request_kwargs,
    parse_cli_args,
)

# Load environment variables from .env (if present)
load_dotenv()

# Set up logging using custom shared module
logging_utils = LoggingUtils()
logger = logging_utils.logger


def call_api(method, endpoint, payload=None, *, as_form: bool = False):
    """Perform an HTTP request using env-based config.

    :param method: HTTP method (GET, POST, etc.)
    :param endpoint: Path relative to API_BASE_URL (e.g. /v1/items)
    :param payload: Python dict representing the request body (or None)
    :param as_form: If True, send payload as form-encoded; otherwise JSON
    """
    # Delegate URL/header/payload wiring to shared helper
    kwargs = build_request_kwargs(method, endpoint, payload, as_form=as_form)

    try:
        resp = requests.request(**kwargs)
        resp.raise_for_status()
    except requests.RequestException as e:
        logger.error(f"Request failed: {e}")
        sys.exit(1)

    # Try to decode JSON; if not JSON, return raw text under "text"
    try:
        return resp.json()
    except ValueError:
        return {"text": resp.text}


def main():
    """Simple CLI wrapper around call_api()."""
    method, endpoint, payload, as_form = parse_cli_args(sys.argv)

    result = call_api(method, endpoint, payload, as_form=as_form)
    # Pretty-print JSON/response to logs
    logger.info(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
