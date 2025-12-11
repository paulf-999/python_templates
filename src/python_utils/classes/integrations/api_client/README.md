# `api_utils.py` — Generic API Caller

A simple command-line tool for making API requests using environment variables and a shared helper module.
Supports JSON (default) and form-encoded payloads.

---

## Setup

Environment variables:

```
API_BASE_URL=https://api.example.com/
API_TOKEN=optional_bearer_token
```

Requires:

```
pip install requests python-dotenv
```

---

## Usage

### GET

```bash
python api_utils.py GET /v1/items
```

### POST (JSON body)

```bash
python api_utils.py POST /v1/items '{"name": "test"}'
```

### POST (JSON loaded from file)

```bash
python api_utils.py POST /v1/items @payload.json
```

### POST as form-encoded (e.g., OAuth token endpoints)

```bash
python api_utils.py POST /oauth/token --form '{"grant_type": "client_credentials"}'
```

---

## How it Works (very briefly)

* CLI parsing + payload loading handled by
  `python_utils/classes/integrations/api_client/_api_request_helpers.py`
* Request configuration built by `build_request_kwargs`
* `call_api()` sends the request and returns JSON or raw text
