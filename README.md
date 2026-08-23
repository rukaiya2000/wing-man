# Wing-Man

Wing-Man is a Codex CLI skill pack for founder-led go-to-market work. It
turns a focused request into a review-ready Notion artifact; it is not a CRM,
backend, worker, scheduler, or standalone application.

## Product boundaries

- Codex CLI is the interaction surface; Notion is the review/output surface.
- Skills own workflow logic and hard rules. MCP servers are the first choice
  for external systems. Local Python is limited to two read-only adapters for
  systems without a suitable configured MCP.
- The agent never sends messages, uses a founder's LinkedIn browser session,
  or silently selects outreach recipients.
- Rows use only `New`, `Reviewed`, and `Rejected`. Skills create `New`; the
  founder owns the review states.

## Codex skills

All project workflows live in [.codex/skills](.codex/skills) and are invoked
from Codex CLI.

| Skill | Outcome |
| --- | --- |
| `find-leads` | Evidence-backed people and outreach drafts in Notion |
| `deep-search` | Terminal-first market/company/people research; saves only on request |
| `artifact-outreach` | Artifact-author/contributor leads and review-ready outreach drafts |

Read [schemas/notion.md](schemas/notion.md) for allowed fields, natural
dedupe keys, and status ownership.

## Codex configuration

The project MCP servers are declared in [.codex/config.toml](.codex/config.toml):

- Notion MCP is the only write-capable integration, limited by the skills and
  schema to review tables.
- GitHub MCP is read-only for code, contributor, and release research.

No filled `.env` file is required or committed. The local adapters use no
credentials by default and never write to third-party systems. If you use one
for a system without a suitable configured MCP, copy
[.env.example](.env.example) to a local `.env` and set only the values you
need, or export them for that single command. See
[tools/README.md](tools/README.md) for details.

```bash
python3 tools/scholar.py --help
```

Run validation with:

```bash
python3 -m unittest discover -s tests
```

## Founder memory

`memory/` retains evidence about founder voice, topics, and preferences. The
direct-founder-note rule in [AGENTS.md](AGENTS.md) is always active. A skill
that reads or writes Notion runs
[.codex/memory-update-procedure.md](.codex/memory-update-procedure.md) as its
last step; it is a no-op unless the run provides new evidence.
