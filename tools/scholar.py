#!/usr/bin/env python3
"""Read paper and author metadata from OpenAlex, with Semantic Scholar fallback."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from typing import Any

OPENALEX = "https://api.openalex.org"
SEMANTIC_SCHOLAR = "https://api.semanticscholar.org/graph/v1"
TIMEOUT_SECONDS = 20
DOI = re.compile(r"10\.\d{4,9}/[^\s\"'<>]+", re.I)


def fail(message: str) -> "None":
    print(message, file=sys.stderr)
    raise SystemExit(1)


def get(url: str, params: dict[str, str] | None = None, headers: dict[str, str] | None = None) -> dict[str, Any]:
    query = dict(params or {})
    if url.startswith(OPENALEX) and os.getenv("OPENALEX_MAILTO"):
        query["mailto"] = os.environ["OPENALEX_MAILTO"]
    try:
        import requests
    except ImportError:
        fail("install the fallback dependency with: python3 -m pip install requests")
    try:
        response = requests.get(url, params=query, headers=headers, timeout=TIMEOUT_SECONDS)
        response.raise_for_status()
    except requests.RequestException as exc:
        fail(f"Scholarly metadata read failed: {exc}")
    return response.json()


def short_id(value: str | None) -> str | None:
    return value.rsplit("/", 1)[-1] if value else None


def author(authorship: dict[str, Any]) -> dict[str, Any]:
    person = authorship.get("author") or {}
    institutions = [item.get("display_name") for item in authorship.get("institutions") or []]
    raw = authorship.get("raw_affiliation_strings") or []
    identifier = short_id(person.get("id"))
    return {
        "author_id": f"openalex:{identifier}" if identifier else None,
        "name": person.get("display_name"),
        "organization": next((name for name in institutions if name), None) or (raw[0] if raw else None),
        "is_corresponding": bool(authorship.get("is_corresponding")),
    }


def normalize_work(work: dict[str, Any]) -> dict[str, Any]:
    location = work.get("primary_location") or {}
    doi = (work.get("doi") or "").replace("https://doi.org/", "") or None
    return {
        "source": "OpenAlex",
        "work_id": short_id(work.get("id")),
        "title": work.get("display_name"),
        "year": work.get("publication_year"),
        "doi": doi,
        "url": location.get("landing_page_url") or (f"https://doi.org/{doi}" if doi else work.get("id")),
        "authors": [author(item) for item in work.get("authorships") or []],
        "cited_by_count": work.get("cited_by_count"),
    }


def semantic_artifact(query: str) -> dict[str, Any]:
    """Use Semantic Scholar only when OpenAlex cannot identify a work."""
    headers = {"x-api-key": os.environ["SEMANTIC_SCHOLAR_API_KEY"]} if os.getenv("SEMANTIC_SCHOLAR_API_KEY") else None
    response = get(
        f"{SEMANTIC_SCHOLAR}/paper/search",
        {"query": query, "limit": "1", "fields": "title,year,externalIds,url,citationCount,authors.authorId,authors.name"},
        headers,
    )
    work = (response.get("data") or [None])[0]
    if not work:
        fail("No scholarly work matched the query")
    return {
        "source": "Semantic Scholar",
        "work_id": work.get("paperId"),
        "title": work.get("title"),
        "year": work.get("year"),
        "doi": (work.get("externalIds") or {}).get("DOI"),
        "url": work.get("url"),
        "authors": [
            {"author_id": f"semantic-scholar:{author.get('authorId')}" if author.get("authorId") else None, "name": author.get("name"), "organization": None, "is_corresponding": False}
            for author in work.get("authors") or []
        ],
        "cited_by_count": work.get("citationCount"),
    }


def artifact(query: str) -> dict[str, Any]:
    doi = DOI.search(query)
    if doi:
        work = get(f"{OPENALEX}/works/doi:{doi.group(0).rstrip('.')}")
    else:
        response = get(f"{OPENALEX}/works", {"search": query, "per-page": "5"})
        works = response.get("results") or []
        wanted = " ".join(query.lower().split())
        work = next((candidate for candidate in works if " ".join((candidate.get("display_name") or "").lower().split()) == wanted), None)
        work = work or (works[0] if works else None)
        if not work:
            return semantic_artifact(query)
    return normalize_work(work)


def authors(work_query: str) -> dict[str, Any]:
    return artifact(work_query)


def main() -> None:
    parser = argparse.ArgumentParser(description="Read scholarly metadata and print JSON; never writes to external systems.")
    commands = parser.add_subparsers(dest="command", required=True)
    for name, help_text in (("artifact", "Resolve a paper, DOI, or title."), ("authors", "Resolve an artifact and return authors.")):
        command = commands.add_parser(name, help=help_text)
        command.add_argument("query")
    args = parser.parse_args()
    print(json.dumps(artifact(args.query) if args.command == "artifact" else authors(args.query), ensure_ascii=False))


if __name__ == "__main__":
    main()
