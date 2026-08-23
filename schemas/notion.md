# Notion review schemas

Notion MCP is the sole output path. Before creating a row, fetch the target
database and query existing rows by its natural key. Skills may create a row
with `Status = New` and fill the fields below; only the founder sets `Reviewed`
or `Rejected`.

## Dripify Leads

Natural key: `LinkedIn URL`.

| Field | Type / use |
| --- | --- |
| Name, Company, Role | text |
| LinkedIn URL | URL; primary dedupe key |
| ConnectNote, FirstMessage, Followup 1, Followup 2, End of Sequence | draft copy |
| SourceQuery | original target query |
| Evidence | source links and short relevance note |
| Status | `New`, `Reviewed`, or `Rejected` |

If a valuable person has no LinkedIn URL, include the row only with explicit
evidence and mark the missing URL in `Evidence`; it cannot be deduplicated
automatically.

## Research Reports

One page or row per entity when the founder asks to save a terminal report.

| Field | Type / use |
| --- | --- |
| Company / Person | title |
| What they do | one line |
| Why it matters | GTM relevance |
| Sources | URLs |
| Signal date | observed or source date |
| Relevance note | targeting implication |
| Status | `New`, `Reviewed`, or `Rejected` |

## X Reply Opportunities

Natural key: `Tweet URL`.

| Field | Type / use |
| --- | --- |
| Tweet URL, Author, Tweet Text | source context |
| Angle 1, Angle 2, Angle 3 | reply aspects, never finished reply copy |
| Grounding | linked sources read, or `No external source` |
| Status | `New`, `Reviewed`, or `Rejected` |

## X Drafts

| Field | Type / use |
| --- | --- |
| Final Text | polished human-review draft |
| Title | required only for articles |
| Post Type | `single tweet`, `thread`, or `article` |
| Notes | optional revision context |
| Status | `New`, `Reviewed`, or `Rejected` |

## Artifact Outreach Leads

Natural key: `LinkedIn URL`.

| Field | Type / use |
| --- | --- |
| Name, Organization, Role | person context |
| LinkedIn URL | primary dedupe key |
| ConnectNote, FirstMessage, Followup 1, Followup 2, End of Sequence | Dripify-ready draft copy |
| SourceArtifact | paper, repo, benchmark, or post URL |
| Evidence | authorship/contributor and relevance sources |
| Status | `New`, `Reviewed`, or `Rejected` |

Never add `Sent`, `Scheduled`, `Posted`, or any execution state to these
databases.
