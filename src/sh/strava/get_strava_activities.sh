#!/usr/bin/env bash
set -euo pipefail

# ------------------------------------------------------------
# Load inputs from .env (same directory as this script)
# ------------------------------------------------------------
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ENV_FILE="${SCRIPT_DIR}/.env"

if [[ -f "${ENV_FILE}" ]]; then
  set -a
  # shellcheck disable=SC1090
  source "${ENV_FILE}"
  set +a
fi

# ------------------------------------------------------------
# Required inputs (from .env)
# ------------------------------------------------------------
: "${STRAVA_CLIENT_ID:?Set STRAVA_CLIENT_ID in .env}"
: "${STRAVA_CLIENT_SECRET:?Set STRAVA_CLIENT_SECRET in .env}"
: "${CODE:?Set CODE in .env}"

# Optional inputs (from .env, with defaults)
PER_PAGE="${PER_PAGE:-10}"
PAGE="${PAGE:-1}"

# ------------------------------------------------------------
# Output files
# ------------------------------------------------------------
OUT_DIR="tmp"
TOKEN_FILE="${OUT_DIR}/strava_token_response.json"
OUT_FILE="${OUT_DIR}/strava_activities.json"
OUT_PRETTY_FILE="${OUT_DIR}/strava_activities.pretty.json"

# ------------------------------------------------------------
# Helpers
# ------------------------------------------------------------
exchange_code_for_token() {
  curl -sS -X POST "https://www.strava.com/api/v3/oauth/token" \
    -d "client_id=${STRAVA_CLIENT_ID}" \
    -d "client_secret=${STRAVA_CLIENT_SECRET}" \
    -d "code=${CODE}" \
    -d "grant_type=authorization_code"
}

extract_access_token() {
  # Minimal extraction (no jq). Assumes the token JSON is on one line.
  sed -n 's/.*"access_token":"\([^"]*\)".*/\1/p'
}

list_activities() {
  local access_token="$1"
  curl -sS -X GET "https://www.strava.com/api/v3/athlete/activities?per_page=${PER_PAGE}&page=${PAGE}" \
    -H "Authorization: Bearer ${access_token}"
}

# ------------------------------------------------------------
# Main
# ------------------------------------------------------------
mkdir -p "${OUT_DIR}"

# 1) Get token JSON and save it (for debugging)
TOKEN_JSON="$(exchange_code_for_token)"
printf '%s\n' "${TOKEN_JSON}" > "${TOKEN_FILE}"

ACCESS_TOKEN="$(printf '%s' "${TOKEN_JSON}" | extract_access_token)"
if [[ -z "${ACCESS_TOKEN}" ]]; then
  echo "ERROR: Could not extract access_token. Token response saved to: ${TOKEN_FILE}" >&2
  echo "${TOKEN_JSON}" >&2
  exit 1
fi

# 2) Fetch activities and write directly as prettified JSON to strava_activities.json
list_activities "${ACCESS_TOKEN}" > "${OUT_FILE}.raw"
python3 -m json.tool "${OUT_FILE}.raw" > "${OUT_FILE}"
rm -f "${OUT_FILE}.raw"

echo "Wrote token response to: ${TOKEN_FILE}"
echo "Wrote prettified activities to: ${OUT_FILE}"
