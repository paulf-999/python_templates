#!/usr/bin/env python3
"""
Standalone Strava client.

- Reads credentials and API base URL from .env (via python-dotenv)
- Talks directly to Strava's API using requests
- Exports activities to JSON and CSV
"""

import os
import sys
import time
import json
import csv
from datetime import datetime

import requests
from dotenv import load_dotenv

from python_utils.classes.core.logging_utils import LoggingUtils

# Load environment variables from .env (project root or current directory)
load_dotenv()

logger = LoggingUtils().logger

# API base URL from env (required)
API_BASE = os.getenv("API_BASE_URL")
if not API_BASE:
    logger.error("API_BASE_URL must be set in the environment or .env file (e.g. https://www.strava.com/api/v3).")
    sys.exit(1)

TOKEN_URL = f"{API_BASE}/oauth/token"


def get_access_token() -> str:
    """
    Exchange the Strava refresh token for an access token.

    Requires:
        STRAVA_CLIENT_ID
        STRAVA_CLIENT_SECRET
        STRAVA_REFRESH_TOKEN
    """
    client_id = os.getenv("STRAVA_CLIENT_ID")
    client_secret = os.getenv("STRAVA_CLIENT_SECRET")
    refresh_token = os.getenv("STRAVA_REFRESH_TOKEN")

    if not client_id or not client_secret or not refresh_token:
        logger.error(
            "STRAVA_CLIENT_ID, STRAVA_CLIENT_SECRET and STRAVA_REFRESH_TOKEN must all be set in the environment or .env file."  # noqa
        )
        sys.exit(1)

    resp = requests.post(
        TOKEN_URL,
        data={
            "client_id": int(client_id),
            "client_secret": client_secret,
            "grant_type": "refresh_token",
            "refresh_token": refresh_token,
        },
        timeout=30,
    )
    resp.raise_for_status()
    data = resp.json()

    new_refresh = data.get("refresh_token")
    if new_refresh and new_refresh != refresh_token:
        logger.warning("New Strava refresh_token issued: %s", new_refresh)

    try:
        return data["access_token"]
    except KeyError:
        logger.error("Strava token response missing 'access_token': %s", json.dumps(data))
        sys.exit(1)


def fetch_activities(
    access_token: str,
    per_page: int = 100,
    after: int | None = None,
    before: int | None = None,
) -> list[dict]:
    """Fetch activities with pagination and simple 429 backoff."""
    page = 1
    all_acts: list[dict] = []

    while True:
        params: dict[str, int] = {"page": page, "per_page": per_page}
        if after:
            params["after"] = after
        if before:
            params["before"] = before

        resp = requests.get(
            f"{API_BASE.rstrip('/')}/athlete/activities",
            headers={"Authorization": f"Bearer {access_token}"},
            params=params,
            timeout=30,
        )

        if resp.status_code == 429:
            logger.warning("Strava rate limit hit. Sleeping 60 seconds...")
            time.sleep(60)
            continue

        resp.raise_for_status()
        batch = resp.json()

        if not batch:
            break

        all_acts.extend(batch)
        page += 1
        time.sleep(0.25)  # gentle pacing

    return all_acts


def write_activities_csv(json_rows: list[dict], path: str) -> None:
    """Write a subset of activity fields to CSV."""
    if not json_rows:
        logger.info("No activities to write to CSV.")
        return

    fields = [
        "id",
        "name",
        "type",
        "sport_type",
        "distance",
        "moving_time",
        "elapsed_time",
        "total_elevation_gain",
        "start_date",
        "average_speed",
        "max_speed",
        "average_heartrate",
        "max_heartrate",
        "suffer_score",
        "commute",
        "private",
    ]

    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(fields)
        for a in json_rows:
            writer.writerow([a.get(k) for k in fields])


def main() -> None:
    """CLI entrypoint: export last 2 years of Strava activities to JSON + CSV."""
    access_token = get_access_token()

    two_years_ago = int(time.time()) - 60 * 60 * 24 * 365 * 2
    activities = fetch_activities(access_token, per_page=100, after=two_years_ago)

    ts = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
    json_path = f"strava_activities_{ts}.json"
    csv_path = f"strava_activities_{ts}.csv"

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(activities, f, ensure_ascii=False, indent=2)

    write_activities_csv(activities, csv_path)

    logger.info("Wrote %d activities", len(activities))
    logger.info("JSON: %s", json_path)
    logger.info("CSV : %s", csv_path)


if __name__ == "__main__":
    main()
