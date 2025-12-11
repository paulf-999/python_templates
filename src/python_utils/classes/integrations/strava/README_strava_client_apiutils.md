# Strava Client (API Utils Variant)

This script (`strava_client_apiutils.py`) exports your Strava activities to JSON and CSV,
but uses the shared generic API client (`api_utils.py`) for the OAuth token request.

## Env Vars

```bash
API_BASE_URL=https://www.strava.com/api/v3
STRAVA_CLIENT_ID=your_client_id
STRAVA_CLIENT_SECRET=your_client_secret
STRAVA_REFRESH_TOKEN=your_refresh_token
````

> `API_TOKEN` is not used for Strava – the script fetches an access token using the
> refresh token on each run.

## What It Does

* Calls `/oauth/token` via `call_api(..., as_form=True)` from `api_utils.py`
* Gets an access token from Strava (logs if a new refresh token is issued)
* Fetches activities from `/athlete/activities` (last 2 years by default)
* Writes:

  * `strava_activities_<timestamp>.json`
  * `strava_activities_<timestamp>.csv`

## Usage

From the repo root (or any location with `python_utils` on `PYTHONPATH`):

```bash
python python_utils/classes/integrations/strava/strava_client_apiutils.py
```

Use this variant if you want Strava to follow the same patterns and logging as your
generic API integrations.
