---
name: polish-x-drafts
description: Turn a rough note or existing X Drafts row into a polished review-only X draft in the founder's current voice. Never schedule or publish.
---

# Polish X drafts

Read the source note or X Drafts row, then read
[notion-map.md](../../../notion-map.md) for the confirmed destination and
[schemas/notion.md](../../../schemas/notion.md).

For every MCP call, retry once on failure. If the retry fails, stop and report
the error; do not substitute a local tool, direct API, or another source for
that failed operation.

1. Fetch the founder's latest 10–30 posts with X MCP as the primary voice and
   taste reference.
2. Preserve the founder's argument. Do not add claims that cannot be supported
   by the original note or provided context.
3. Choose the requested `Post Type`; when no type is provided, recommend a
   single tweet only if the argument survives intact in 280 characters. Otherwise
   recommend a thread. Every thread post must independently fit 280 characters.
4. For a Notion row, fetch comments before revising a rejected draft and address
   the feedback without changing the founder-owned `Status`. For a pasted note,
   create a new X Drafts row with `Status = New`.
5. Write `Final Text`, plus `Title` for an article and an optional short `Notes`
   explanation. Report the form chosen and any size constraint.

The outcome is draft copy for review, never a queue entry. Do not schedule,
publish, repost, or set `Reviewed` or `Rejected`.

After any Notion access, run `.codex/memory-update-procedure.md` as the last
step.
