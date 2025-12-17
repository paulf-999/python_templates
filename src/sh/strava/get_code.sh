#!/usr/bin/env bash
set -euo pipefail

# ------------------------------------------------------------
# Required inputs (fill these in)
# ------------------------------------------------------------
STRAVA_CLIENT_ID=""
STRAVA_CLIENT_SECRET=""
STRAVA_REFRESH_TOKEN=""
CODE=""

curl -sS -X POST "https://www.strava.com/api/v3/oauth/token" \
    -d "client_id=${STRAVA_CLIENT_ID}" \
    -d "client_secret=${STRAVA_CLIENT_SECRET}" \
    -d "code=${CODE}" \
    -d "grant_type=authorization_code" \
| python3 -m json.tool
