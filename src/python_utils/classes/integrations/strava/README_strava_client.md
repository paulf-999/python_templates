# Strava Client (Standalone)

This script (`strava_client.py`) is the original standalone Strava export tool.

It talks directly to the Strava API using `requests` and does not use `api_utils.py`.

## Env Vars

```bash
STRAVA_CLIENT_ID=your_client_id
STRAVA_CLIENT_SECRET=your_client_secret
STRAVA_REFRESH_TOKEN=your_refresh_token
````

## What It Does

* Calls Strava’s token endpoint to exchange the refresh token for an access token
* Fetches activities from `/athlete/activities` (e.g. last 2 years)
* Handles:

  * Pagination
  * Basic 429 rate limiting (sleep + retry)
* Writes:

  * `strava_activities_<timestamp>.json`
  * `strava_activities_<timestamp>.csv`

## Usage

```bash
python python_utils/classes/integrations/strava/strava_client.py
```

Use this version if you want a self-contained script without depending on the
shared API client.
