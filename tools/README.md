# Narrow local adapters

This free JSON CLI is used only for a system that has no suitable configured
MCP. It is never a fallback for a failed MCP call. It writes one JSON value to
stdout, writes diagnostics to stderr, exits non-zero on failure, and makes no
third-party mutation.

| Tool | Commands | Required environment |
| --- | --- | --- |
| `scholar.py` | `artifact`, `authors` | optional `SEMANTIC_SCHOLAR_API_KEY` |
