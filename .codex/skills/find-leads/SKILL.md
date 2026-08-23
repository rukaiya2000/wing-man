---
name: find-leads
description: Build a review-ready Dripify lead table in Notion from one target description. Use for founder, product, GTM, buyer, or company lead-finding requests; never execute outreach.
---

# Find leads

Turn one focused targeting request into evidence-backed rows in `Dripify Leads`.
Read [notion-map.md](../../../notion-map.md) for the destination hierarchy and
[schemas/notion.md](../../../schemas/notion.md) before any Notion write.

For every MCP call, retry once on failure. If the retry fails, stop and report
the error; do not substitute a local tool, direct API, or another source for
that failed operation.

1. Interpret one target query. If the founder asks for several distinct target
   groups, process only the explicitly requested batch; otherwise keep the run
   to one group. Ask one question only when role, company type, or geography is
   essential and genuinely ambiguous.
2. Research companies and people with web search. Verify current role and the
   signal that makes each lead relevant; retain the source URLs.
3. Use the configured professional-data MCP for discovery and enrichment.
   Never automate a founder's LinkedIn session or connection flow.
4. Follow the outreach-campaign routing in `notion-map.md`. Inspect the
   relevant existing campaign tables and deduplicate by `LinkedIn URL`. Do not
   create a duplicate. A person without a URL may be included only when their
   evidence makes manual review worthwhile.
5. For each new lead, draft a concise connection note, first message, two
   follow-ups, and a close-the-loop message. Ground personalization in the
   sources; do not invent familiarity, funding, or product claims.
6. Create a new campaign child page and its inline `Dripify Leads` table as
   specified in `notion-map.md`, then create the rows with `Status = New`, the
   original `SourceQuery`, and the review evidence. Report how many were
   created, deduplicated, and held for manual LinkedIn review.

Stop after the rows are review-ready. Never send, upload to Dripify, change a
review status, or choose recipients without writing them for founder review.

After any Notion access, run `.codex/memory-update-procedure.md` as the last
step.
