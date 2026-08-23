---
name: artifact-outreach
description: Turn one paper, benchmark, repository, blog post, or research artifact into review-ready outreach rows in Notion. Never contact, export, or sequence anyone.
---

# Artifact outreach

Given one artifact, identify people worth reviewing and write `Artifact
Outreach Leads`. Read [schemas/notion.md](../../../schemas/notion.md) before
creating rows.

For every MCP call, retry once on failure. If the retry fails, stop and report
the error; do not substitute a local tool, direct API, or another source for
that failed operation.

1. Resolve the artifact. Use GitHub MCP for repositories and contributors;
   use web research and `tools/scholar.py` for non-repository scholarly
   artifacts. Keep the canonical artifact URL and evidence.
2. Prioritize first, corresponding, and senior authors; active maintainers;
   and contributors at clearly relevant labs or companies. Do not silently
   choose a recipient—every candidate belongs in a review row with rationale.
3. Use public web evidence for current organization, role, and LinkedIn URL.
   Never use an authenticated LinkedIn browser session.
4. Query existing `Artifact Outreach Leads` by `LinkedIn URL` before creating
   anything. For candidates without URLs, create a manual-review row only when
   the evidence is strong enough to justify it.
5. Draft a connection note, first message, two follow-ups, and a close-the-loop
   note rooted in the artifact and person's contribution. Create the row with
   `Status = New`, `SourceArtifact`, and evidence links.

Stop once the Notion rows are ready. Never send, export to Dripify, change
review status, or run a LinkedIn session.

After any Notion access, run `.codex/memory-update-procedure.md` as the last
step.
