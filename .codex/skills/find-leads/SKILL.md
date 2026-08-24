---
name: find-leads
description: Find and qualify leads from one target description, reporting exploratory results or writing a review-ready Dripify table when requested. Use for founder, product, GTM, buyer, or company lead-finding requests; never execute outreach.
---

# Find leads

Turn one focused targeting request into an evidence-backed terminal report or
review rows in `Dripify Leads`. Read [notion-map.md](../../../notion-map.md) for
the destination hierarchy and [schemas/notion.md](../../../schemas/notion.md)
before any Notion write.

For every MCP call, retry once on failure. If the retry fails, stop and report
the error; do not substitute a local tool, direct API, or another source for
that failed operation.

1. Interpret one target query and determine the output mode. A request to
   test, compare, explore, or evaluate stops with a terminal report. Write to
   Notion only when the founder asks to add, save, or create leads. Process an
   explicitly requested batch; otherwise keep the run to one target group.
2. Resolve the exact company before searching for people. Verify its domain
   and LinkedIn company page, then resolve the provider's company identifier.
3. For a small or emerging company, or whenever its title taxonomy is unclear,
   use an allowlisted professional-data MCP to sample up to 25 employees with
   only the exact-employer constraint. This sample is not a lead list. Recheck
   each returned row's current employer and discard former employees,
   investors, advisors, and provider contamination before learning from it.
4. Derive a company-specific search strategy from the clean sample: observed
   titles and abbreviations (for example, `MTS`), adjacent titles, relevant
   headline or responsibility signals, and explicit exclusions. Distinguish
   cohort-discovery terms from qualification evidence; a generic title or a
   broad category such as `Engineering` cannot qualify a lead by itself.
5. Run one focused exact-employer query per provider using the observed title
   and profile signals. Limit each provider to one sampling query and one
   focused query unless the founder asks for a broader investigation.
6. Enrich only the focused shortlist. State or confirm paid enrichment when
   the provider requires it. Resolve canonical LinkedIn URLs and use public web
   sources to verify current employment and the relevance signal.
7. Classify every focused result as `Qualified`, `Held`, or `Excluded`.
   Qualification requires both verified current employment and evidence for
   the requested responsibility. A plausible title without evidence is held,
   not silently selected.
8. In exploratory mode, report the strategy, qualified and held candidates,
   exclusions, provider noise, likely false negatives, queries, and credits;
   then stop without accessing Notion.
9. In Notion-write mode, follow `notion-map.md`, inspect the relevant campaign
   tables, and deduplicate qualified candidates by `LinkedIn URL`. Draft the
   connection note and full follow-up sequence only for new qualified review
   rows, ground personalization in retained sources, and create the requested
   campaign child page and inline table with `Status = New` and the original
   `SourceQuery`. Report sampled, contaminated, qualified, held, excluded,
   deduplicated, and created counts, plus provider costs and limitations.

Stop after the rows are review-ready. Never send, upload to Dripify, change a
review status, automate a founder LinkedIn session, or invoke contact, list,
sequence, email, export, or other outbound tools.

After any Notion access, run `.codex/memory-update-procedure.md` as the last
step.
