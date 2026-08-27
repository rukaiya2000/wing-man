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

1. Build a draft-specific voice set from the founder's own X profile with X MCP.
   - Resolve the founder's profile with `get_user`, then fetch recent posts with
     `get_user_posts`.
   - Extract the rough note's topic, named entities, post type, and argumentative
     shape. Use `search_posts` with several focused queries to find related posts
     authored by the founder. Restrict voice references to the founder's posts;
     never learn the founder's voice from other accounts.
   - Select 10–20 reference posts. Prefer posts related to the current draft in
     topic, format, or rhetorical shape, then fill gaps with recent posts. If no
     related posts exist, use the latest 10–30 posts as the fallback.
   - Infer recurring choices from the selected set, including opening style,
     sentence length, technical density, hedging, punctuation, paragraph breaks,
     and endings. Use those observations when drafting; do not copy phrases or
     clone a previous post.
2. Preserve the founder's argument. Do not add claims that cannot be supported
   by the original note or provided context.
   - Match the phrasing, rhythm, casing, punctuation, and degree of polish in
     the selected reference posts. Preserve the founder's direct, exploratory
     operator voice instead of rewriting it into generic polished social copy.
   - Never use em dashes. Use commas, periods, colons, or parentheses instead.
   - Do not open a final draft with "I think." State the claim directly, then use
     calibrated language later when genuine uncertainty matters.
   - Prefer a concrete number or example when it makes an abstraction easier to
     understand. Keep hypothetical examples clearly hypothetical and never imply
     that a specific model, benchmark, or result exists without support.
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
