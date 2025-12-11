"""
Internal helpers for API client scripts.
Not intended to be used directly by end users.
"""

import json
import os
import sys
from urllib.parse import urljoin

from dotenv import load_dotenv

from python_utils.classes.core.logging_utils import LoggingUtils

# Load env vars (safe to call multiple times across modules)
load_dotenv()

logging_utils = LoggingUtils()
logger = logging_utils.logger


def build_request_kwargs(method, endpoint, payload=None, *, as_form: bool = False):
    """
    Build the kwargs dict passed to requests.request().

    Handles:
    - Base URL + endpoint join
    - Headers (including optional Bearer token)
    - Payload wiring (JSON vs form-encoded)
    """
    base_url = os.getenv("API_BASE_URL")
    if not base_url:
        logger.error("API_BASE_URL must be set in .env")
        sys.exit(1)

    url = urljoin(base_url, endpoint.lstrip("/"))

    headers = {"Accept": "application/json"}

    token = os.getenv("API_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"

    kwargs = {
        "method": method.upper(),
        "url": url,
        "headers": headers,
        "timeout": 30,
    }

    if payload is not None:
        if as_form:
            headers.setdefault("Content-Type", "application/x-www-form-urlencoded")
            kwargs["data"] = payload
        else:
            headers.setdefault("Content-Type", "application/json")
            kwargs["json"] = payload

    return kwargs


def _load_payload(raw: str):
    """
    Parse the payload argument:

    - If it starts with '@', treat it as a JSON filename.
    - Otherwise, treat it as a JSON string.
    """
    if raw.startswith("@"):
        with open(raw[1:], "r", encoding="utf-8") as f:
            text = f.read()
    else:
        text = raw

    try:
        return json.loads(text)
    except json.JSONDecodeError as e:
        logger.error(f"Invalid JSON payload: {e}")
        sys.exit(1)


def parse_cli_args(argv):
    """
    Parse CLI arguments for a simple API client script.

    Expects:
        argv[0]  -> script name
        argv[1]  -> METHOD
        argv[2]  -> ENDPOINT
        argv[3]? -> JSON payload (string or @file)
        '--form' -> optional flag to send payload as form-encoded
    """
    if len(argv) < 3:
        logger.error(f"Usage: {argv[0]} METHOD ENDPOINT [JSON_PAYLOAD] [--form]")
        sys.exit(1)

    # Optional flag: if present, send body as form-encoded
    as_form = False
    if "--form" in argv:
        as_form = True
        argv.remove("--form")

    method, endpoint = argv[1], argv[2]

    # Payload is optional
    payload = None
    if len(argv) > 3:
        raw = argv[3]
        payload = _load_payload(raw)

    return method, endpoint, payload, as_form
