---
name: artifact-outreach
description: Turn one paper, benchmark, repository, blog post, or research artifact into review-ready Dripify outreach rows in Notion. Never contact, export, or sequence anyone.
---

# Artifact outreach

Given one artifact, identify people worth reviewing and write `Artifact
Outreach Leads`. Read [notion-map.md](../../../notion-map.md) for the destination
hierarchy and [schemas/notion.md](../../../schemas/notion.md) before creating
rows.

For every MCP call, retry once on failure. If the retry fails, stop and report
the error; do not substitute a local tool, direct API, or another source for
that failed operation.

1. Resolve the artifact. Use GitHub MCP for repositories and contributors;
   use web research and `tools/scholar.py` for non-repository scholarly
   artifacts. Keep the canonical artifact URL and evidence. For papers,
   extract author order, affiliations, corresponding-author status, and any
   email, ORCID, lab, personal-site, or repository links that help resolve
   identity.
2. Prioritize first, corresponding, and senior authors; active maintainers;
   and contributors at clearly relevant labs or companies. Do not silently
   choose a recipient—every candidate belongs in a review row with rationale.
3. Resolve each priority author's identity with targeted web research before
   professional-data enrichment. Search the exact name with the paper title
   and affiliation to find Google Scholar, an institutional or personal page,
   ORCID, and a likely LinkedIn URL. Build a traceable identity chain such as
   `paper -> affiliation -> Scholar/personal page -> LinkedIn candidate`.
   Do not begin with a broad name-only professional-database search; common
   names create noisy, costly false matches.
4. Pass only likely LinkedIn URLs or other strongly supported identifiers to
   an allowlisted professional-data MCP, preferably in a batch. Pull current
   organization, role, employment history, education, and relevant profile
   signals, then cross-check them against the paper and web evidence. Treat a
   profile as verified only when at least two identity signals agree, such as
   current or previous affiliation, university, research area, personal site,
   GitHub identity, or publication history. Classify candidates as `Verified`,
   `Likely`, `Manual review`, or `Excluded`; retain the confidence and evidence
   in the review row. Never use an authenticated LinkedIn browser session.
5. Follow the outreach-campaign routing in `notion-map.md`. Inspect the
   relevant existing campaign tables and deduplicate by `LinkedIn URL` before
   creating anything. For candidates without URLs, create a manual-review row
   only when the evidence is strong enough to justify it.
6. Draft a connection note, first message, two follow-ups, and a close-the-loop
   note rooted in the artifact and person's contribution. Create a new campaign
   child page and its inline `Artifact Outreach Leads` table as specified in
   `notion-map.md`, then create rows with `Status = New`, `SourceArtifact`, and
   evidence links.

Stop once the Notion rows are ready. Never send, export to Dripify, change
review status, or run a LinkedIn session.

After any Notion access, run `.codex/memory-update-procedure.md` as the last
step.
