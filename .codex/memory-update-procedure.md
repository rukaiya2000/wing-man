# Memory update procedure

Every skill that accesses Notion runs this as its last step. It is silent when
the run produced no new evidence.

1. Read the relevant existing `memory/*.md` file and preserve its `## Founder
   notes (manual — preserved on regeneration)` section exactly.
2. Consider only evidence from the current run: founder comments, reviewed or
   rejected Notion artifacts, and the founder posts fetched from X MCP. A
   `New` row is not evidence of a preference.
3. Update only the generated observations that are supported by that evidence.
   Keep a source reference, confidence level, and a clear note where evidence
   is too thin to infer a rule. Never manufacture a style or topic preference.
4. Update `memory/MEMORY.md` only when a changed source file changes its
   confidence summary. Restore the manual-notes section verbatim.

This procedure never changes Notion statuses, sends messages, publishes,
schedules, or edits anything outside `memory/`.
