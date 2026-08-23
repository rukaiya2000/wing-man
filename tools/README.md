# Narrow fallback tools

These JSON CLIs are used only when the corresponding MCP capability is
unavailable or unsuitable. They write one JSON value to stdout, write
diagnostics to stderr, exit non-zero on failure, and make no third-party
mutation.

| Tool | Commands | Required environment |
| --- | --- | --- |
| `linkedin_fresh.py` | `search`, `poll`, `profile` | `FRESH_LINKEDIN_DATA_API_KEY` and matching endpoint URL(s) |
| `x_read.py` | `search-posts`, `user-posts`, `get-post` | `X_BEARER_TOKEN` |
| `scholar.py` | `artifact`, `authors` | optional `OPENALEX_MAILTO`, `SEMANTIC_SCHOLAR_API_KEY` |

For Fresh LinkedIn Data API, set the operation-specific endpoint values supplied
by the RapidAPI listing: `FRESH_LINKEDIN_SEARCH_URL`,
`FRESH_LINKEDIN_POLL_URL`, and `FRESH_LINKEDIN_PROFILE_URL`. This avoids
hard-coding undocumented RapidAPI paths or credentials. The tool passes the
query parameters shown by `--help` and normalizes common profile fields.
