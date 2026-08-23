#!/usr/bin/env python3
"""Read-only JSON adapter for a configured Fresh LinkedIn Data API endpoint."""

from __future__ import annotations

import argparse
import json
import os
import sys
from typing import Any

TIMEOUT_SECONDS = 30


def fail(message: str) -> "None":
    print(message, file=sys.stderr)
    raise SystemExit(1)


def endpoint(operation: str) -> str:
    value = os.getenv(f"FRESH_LINKEDIN_{operation.upper()}_URL")
    if not value:
        fail(f"FRESH_LINKEDIN_{operation.upper()}_URL is required; copy it from the subscribed RapidAPI listing")
    return value


def request(operation: str, params: dict[str, str]) -> dict[str, Any]:
    key = os.getenv("FRESH_LINKEDIN_DATA_API_KEY")
    if not key:
        fail("FRESH_LINKEDIN_DATA_API_KEY is required")
    try:
        import requests
    except ImportError:
        fail("install the fallback dependency with: python3 -m pip install requests")
    headers = {"X-RapidAPI-Key": key}
    host = os.getenv("FRESH_LINKEDIN_DATA_API_HOST")
    if host:
        headers["X-RapidAPI-Host"] = host
    try:
        response = requests.get(endpoint(operation), headers=headers, params=params, timeout=TIMEOUT_SECONDS)
        response.raise_for_status()
    except requests.RequestException as exc:
        fail(f"Fresh LinkedIn Data API read failed: {exc}")
    payload = response.json()
    return normalize(payload)


def normalize(payload: Any) -> dict[str, Any]:
    """Keep the provider response while exposing common review fields when present."""
    row = payload.get("data", payload) if isinstance(payload, dict) else payload
    if isinstance(row, list):
        row = row[0] if row else {}
    if not isinstance(row, dict):
        return {"raw": payload}
    return {
        "name": row.get("name") or row.get("full_name") or row.get("fullName"),
        "company": row.get("company") or row.get("company_name") or row.get("current_company"),
        "role": row.get("headline") or row.get("title") or row.get("position"),
        "location": row.get("location"),
        "linkedin_url": row.get("linkedin_url") or row.get("linkedinUrl") or row.get("profile_url") or row.get("url"),
        "raw": payload,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Read professional data from RapidAPI and print JSON; never interacts with LinkedIn.")
    commands = parser.add_subparsers(dest="command", required=True)
    search = commands.add_parser("search", help="Search people or companies using the configured provider endpoint.")
    search.add_argument("query")
    search.add_argument("--company")
    search.add_argument("--limit", default="10")
    poll = commands.add_parser("poll", help="Poll a provider job ID.")
    poll.add_argument("job_id")
    profile = commands.add_parser("profile", help="Fetch an existing public profile URL.")
    profile.add_argument("linkedin_url")
    args = parser.parse_args()
    if args.command == "search":
        result = request("search", {"query": args.query, "company": args.company or "", "limit": args.limit})
    elif args.command == "poll":
        result = request("poll", {"job_id": args.job_id})
    else:
        result = request("profile", {"linkedin_url": args.linkedin_url})
    print(json.dumps(result, ensure_ascii=False))


if __name__ == "__main__":
    main()
