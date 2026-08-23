# GTM Agent

GTM Agent is a Codex CLI skill pack for founder-led go-to-market work. It
turns a focused request into a review-ready Notion artifact; it is not a CRM,
backend, worker, scheduler, or standalone application.

## Product boundaries

- Codex CLI is the interaction surface; Notion is the review/output surface.
- Skills own workflow logic and hard rules. MCP servers are the first choice
  for external systems. Local Python is limited to three read-only fallbacks.
- The agent never sends messages, publishes or schedules X posts, uses a
  founder's LinkedIn browser session, or silently selects outreach recipients.
- Rows use only `New`, `Reviewed`, and `Rejected`. Skills create `New`; the
  founder owns the review states.

## Codex skills

All project workflows live in [.codex/skills](.codex/skills) and are invoked
from Codex CLI.

| Skill | Outcome |
| --- | --- |
| `find-leads` | Dripify-ready people and full draft sequences in Notion |
| `deep-search` | Terminal-first market/company/people research; saves only on request |
| `x-reply-angles` | X opportunities and three grounded response angles, not replies |
| `polish-x-drafts` | Voice-aware X drafts for human review |
| `artifact-outreach` | Artifact-author/contributor leads and review-ready Dripify sequences |

Read [schemas/notion.md](schemas/notion.md) for allowed fields, natural
dedupe keys, and status ownership.

## Codex configuration

The project MCP servers are declared in [.codex/config.toml](.codex/config.toml):

- Notion MCP is the only write-capable integration, limited by the skills and
  schema to review tables.
- X is read-only and uses the official `xurl` MCP bridge. Complete its OAuth
  flow when prompted.
- GitHub MCP is read-only for code, contributor, and release research.

No `.env` file is required. Fallback tools use no credentials by default and
never write to third-party systems. If a fallback is necessary, set only the
environment variables named in [tools/README.md](tools/README.md) for that
single command.

```bash
python3 tools/x_read.py --help
python3 tools/linkedin_fresh.py --help
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
