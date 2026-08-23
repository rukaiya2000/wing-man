---
name: x-reply-angles
description: Find relevant X posts and add evidence-backed reply angles to Notion for founder review. Use for X engagement discovery; never create finished replies or interact with posts.
---

# X reply angles

Create review-ready rows in `X Reply Opportunities`; read
[schemas/notion.md](../../../schemas/notion.md) before writing.

For every MCP call, retry once on failure. If the retry fails, stop and report
the error; do not substitute a local tool, direct API, or another source for
that failed operation.

1. Use X MCP to fetch the founder's latest 10–30 posts as the primary current
   voice and topic reference, then search recent relevant posts for the given
   topic.
2. Read each candidate post and research any linked paper, repository, product,
   article, or thread before forming an angle. Keep source URLs in `Grounding`.
3. Fetch the target Notion database and deduplicate by `Tweet URL`.
4. For each net-new opportunity, write the source post plus three distinct
   aspects the founder could respond to: an observation, a useful tension, a
   question, a concrete implication, or a respectful counterpoint. They must
   be angles, not publish-ready reply text.
5. Create rows with `Status = New` and report the count plus any skipped
   duplicates or weakly grounded candidates.

Never like, repost, quote, reply, schedule, post, or change a review status.
After any Notion access, run `.codex/memory-update-procedure.md` as the last
step.
