#!/usr/bin/env python3
"""Read-only JSON CLI for the X API fallback."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from typing import Any

BASE_URL = "https://api.x.com/2"
TIMEOUT_SECONDS = 20


def fail(message: str) -> "None":
    print(message, file=sys.stderr)
    raise SystemExit(1)


def get(path: str, params: dict[str, Any]) -> dict[str, Any]:
    token = os.getenv("X_BEARER_TOKEN")
    if not token:
        fail("X_BEARER_TOKEN is required when X MCP is unavailable")
    try:
        import requests
    except ImportError:
        fail("install the fallback dependency with: python3 -m pip install requests")
    try:
        response = requests.get(
            f"{BASE_URL}{path}",
            headers={"Authorization": f"Bearer {token}"},
            params=params,
            timeout=TIMEOUT_SECONDS,
        )
        response.raise_for_status()
    except requests.RequestException as exc:
        fail(f"X API read failed: {exc}")
    return response.json()


def limit(value: str) -> int:
    parsed = int(value)
    if not 10 <= parsed <= 100:
        raise argparse.ArgumentTypeError("limit must be between 10 and 100")
    return parsed


def post_id(value: str) -> str:
    match = re.search(r"(?:status/)?(\d+)(?:\?.*)?$", value.rstrip("/"))
    if not match:
        raise argparse.ArgumentTypeError("provide an X post URL or numeric post ID")
    return match.group(1)


def main() -> None:
    parser = argparse.ArgumentParser(description="Read X data and print JSON; never writes to X.")
    commands = parser.add_subparsers(dest="command", required=True)
    search = commands.add_parser("search-posts", help="Search recent X posts.")
    search.add_argument("query")
    search.add_argument("--limit", type=limit, default=20)
    user = commands.add_parser("user-posts", help="Fetch a user's recent non-reply, non-repost posts.")
    user.add_argument("username")
    user.add_argument("--limit", type=limit, default=20)
    post = commands.add_parser("get-post", help="Fetch one post by URL or ID.")
    post.add_argument("post", type=post_id)
    args = parser.parse_args()

    fields = "created_at,public_metrics,conversation_id,author_id,note_tweet"
    if args.command == "search-posts":
        result = get("/tweets/search/recent", {"query": args.query, "max_results": args.limit, "tweet.fields": fields, "expansions": "author_id", "user.fields": "username,name"})
    elif args.command == "user-posts":
        account = get(f"/users/by/username/{args.username.lstrip('@')}", {"user.fields": "username,name"})
        account_id = (account.get("data") or {}).get("id")
        if not account_id:
            fail("X API returned no user for that username")
        result = get(f"/users/{account_id}/tweets", {"max_results": args.limit, "exclude": "retweets,replies", "tweet.fields": fields})
    else:
        result = get(f"/tweets/{args.post}", {"tweet.fields": fields, "expansions": "author_id", "user.fields": "username,name"})
    print(json.dumps(result, ensure_ascii=False))


if __name__ == "__main__":
    main()
