8/22/26, 11:12 PM 

GTM Agent | Notion 

Youʼre almost there — sign up to start building in Notion today. 

Sign up or login 

# GTM A nt ge 

## — GTM A nt Des n Re irements ge ig qu 

A Codex CLI skill pack for founder-led GTM work. 

This is not a standalone app, CRM, backend service, or Python product. The product surface is Codex CLI + Codex skills + MCP servers/tools. Skills orchestrate research and drafting, write review-ready outputs to Notion, and stop. 

### Core Preference 

Use this order of operation: 

1. Codex skill for the workflow logic and hard rules. 

2. MCP server for external systems whenever one exists. 

3. Purpose-built tool/API adapter only when MCP is unavailable or unsuitable. 

4. No local app architecture unless a hard rule cannot be enforced by skills + MCP/tools. 

The design should stay close to the existing `design.md` direction: maximal MCP, skills calling MCP directly, and Python only for narrow tool gaps or deterministic helpers. 

### Product Goal 

Turn founder requests in Codex CLI into review-ready GTM artifacts in Notion. 

Artifacts: 

- Dripify-ready lead tables 

- market/company/person research reports 

https://app.notion.com/p/GTM-Agent-7aaeb9c5f59182d4b2cb8173d8cd3c23 

1/16 

8/22/26, 11:12 PM 

GTM Agent | Notion 

- X reply opportunity rows with suggested angles 

- polished X draft rows 

- research-artifact author lead tables with Dripify sequence drafts 

The founder reviews in Notion and manually uses Dripify or X outside the agent. 

### Hard Rules 

These rules are enforced by skills and should be repeated in the relevant `SKILL.md` files. 

#### Global 

- Never send messages. 

- Never publish or schedule posts. 

- Never operate a LinkedIn browser/session logged in as the founder. 

- Never choose outreach recipients silently; write rows for review. 

- Notion is the review/output surface. 

- Codex CLI is the interaction surface. 

- Prefer MCP over hand-written clients. 

- Use one focused query/request per run unless the founder explicitly asks for a batch. 

- If a result will be used for outreach, write source context or enough evidence for review. 

#### Statuses 

Default statuses are: 

```
New Reviewed Rejected
```

https://app.notion.com/p/GTM-Agent-7aaeb9c5f59182d4b2cb8173d8cd3c23 

2/16 

8/22/26, 11:12 PM 

GTM Agent | Notion 

Skills may create `New` rows and fill draft/research fields. The founder owns `Reviewed` and `Rejected` . 

#### LinkedIn / Dripify 

- LinkedIn is data-only inside this system. 

- Dripify owns LinkedIn sequencing and execution. 

- The agent prepares upload/copy fields only. 

- Primary dedupe key is `LinkedIn URL` . 

- Before creating new lead rows, check the target Notion table for existing `LinkedIn URL` values. 

- If a LinkedIn URL is missing, include the row only when the lead is still valuable enough for manual review. 

#### X 

- Use X API/MCP for X reads and recent founder posts. 

- For X-related drafting, fetch the founder's latest 10-30 posts through X API/MCP as the primary voice/taste reference. 

- For reply work, produce reply angles/aspects, not final replies. 

- No auto-like, auto-retweet, scheduling, posting queue, or `Posted` state. 

### Use Cases / Skills 

#### - 1. **`find-leads`** : Dripify Ready Lead Table 

Given a target description, find relevant leads, enrich them, draft a LinkedIn outreach sequence, and write rows to Notion for Dripify upload/copy. 

Example: 

https://app.notion.com/p/GTM-Agent-7aaeb9c5f59182d4b2cb8173d8cd3c23 

3/16 

8/22/26, 11:12 PM 

GTM Agent | Notion 

```
Find founders or VP product/GTM people at ITSM AI companies that
raised $50M+.
```

##### Tools: 

|Need|Preferred tool|
|---|---|
|Notion output/review|NotionMCP|
|Web/company research|web search|
|Funding/company signals|web search / startup databases<br>where available|
|LinkedIn profile discovery|LinkedIn/professional dataAPIor<br>search tool; not browser<br>automation|
|Drafting|Codex skill using gathered<br>context|



##### Notion fields: 

https://app.notion.com/p/GTM-Agent-7aaeb9c5f59182d4b2cb8173d8cd3c23 

4/16 

8/22/26, 11:12 PM 

GTM Agent | Notion 

|Field|Notes|
|---|---|
|Name|Person name|
|Company|Company name|
|Role|Current role/title|
|LinkedIn URL|Primary dedupe andDripify key|
|ConnectNote|ShortLinkedIn connection note|
|FirstMessage|First post-connect message|
|Followup 1|First follow-up draft|
|Followup 2|Second follow-up draft|
|End ofSequence|Final close-the-loop draft|
|SourceQuery|Search/filter that found the lead|
|Status|New,Reviewed,Rejected|



##### Hard rules: 

- Check existing Notion rows by `LinkedIn URL` before creating new rows. 

- Draft the full Dripify sequence, not just one custom message. 

- Do not send or upload to Dripify. 

- Stop after Notion rows are ready. 

#### 2. **`deep-search`** : Market / Company / People Research 

Given one research question, produce a terminal-first analysis of a market, company set, or people landscape. 

Example: 

https://app.notion.com/p/GTM-Agent-7aaeb9c5f59182d4b2cb8173d8cd3c23 

5/16 

8/22/26, 11:12 PM 

GTM Agent | Notion 

```
Research ITSM AI companies that raised $50M+ and are building agent
workflows.
```

##### Tools: 

|Need|Preferred tool|
|---|---|
|News/company/product research|web search|
|Funding signals|web search / funding databases<br>where available|
|Professional/company signals|LinkedIn/professional data or<br>search|
|Technical artifacts|GitHub search/API|
|Existing founder context|NotionMCP|



##### Output: 

|Field|Notes|
|---|---|
|Company /Person|Entity being researched|
|What they do|One-line description|
|Why it matters|Relevance to theGTMhypothesis|
|Source(s)|Evidence links|
|Signal date|Funding, launch, article, or<br>observed recency|
|Relevance note|How this changes targeting or<br>prioritization|



##### Hard rules: 

https://app.notion.com/p/GTM-Agent-7aaeb9c5f59182d4b2cb8173d8cd3c23 

6/16 

8/22/26, 11:12 PM 

GTM Agent | Notion 

- One research question per run. 

- Ask one clarifying question only if scope is genuinely ambiguous. 

- Show analysis in terminal first. 

- Save to Notion or Markdown only if requested after showing the analysis. 

- Do not draft Dripify outreach in this use case. 

#### 3. **`x-reply-angles`** : Discover X Reply Opportunities 

Find relevant X posts, write them into the Response Calendar, suggest reply angles/aspects, and stop for founder review. 

Examples: 

```
Find posts to engage with and suggest reply angles.
```

```
Find recent posts about RL environments, agent benchmarks, and long-
horizon tool use.
```

##### Tools: 

|Need|Preferred tool|
|---|---|
|X post discovery/read|XAPI/MCP|
|Founder recent posts|XAPI/MCP|
|Linked source research|web search|
|Notion output|NotionMCP|



##### Notion fields: 

https://app.notion.com/p/GTM-Agent-7aaeb9c5f59182d4b2cb8173d8cd3c23 

7/16 

8/22/26, 11:12 PM 

GTM Agent | Notion 

|Field|Notes|
|---|---|
|Tweet URL|Original post|
|Author|X author|
|Tweet Text|Source post text|
|Angle 1|Suggested reply aspect|
|Angle 2|Suggested reply aspect|
|Angle 3|Suggested reply aspect|
|Grounding|Sources read or none needed|
|Status|New,Reviewed,Rejected|



##### Hard rules: 

- Produce reply ideas, not final reply copy. 

- The founder writes the final reply manually. 

- Research linked papers/repos/products/threads before suggesting angles. 

- Leave rows as `New` . 

- No scheduling, posting, auto-like, auto-retweet, or posting queue. 

#### 5. **`polish-x-drafts`** : Rough Note to X Draft 

Turn a rough note or Notion draft row into a polished X draft for human review. 

Examples: 

```
Turn this rough note into a tweet.
```

https://app.notion.com/p/GTM-Agent-7aaeb9c5f59182d4b2cb8173d8cd3c23 

8/16 

8/22/26, 11:12 PM 

GTM Agent | Notion 

```
Rewrite the rejected draft using the Notion comments.
```

##### Tools: 

|Need|Preferred tool|
|---|---|
|Notion draft rows/comments|NotionMCP|
|Founder recent posts|XAPI/MCP|
|Drafting|Codex skill|



##### Notion fields: 

|Field|Notes|
|---|---|
|Final Text|Polished draft|
|Title|Required for articles|
|Post Type|single tweet, thread, or article|
|Status|review-only lifecycle|
|Notes|Optional revision note|



##### Hard rules: 

- Preserve the founder's argument. 

- Do not add unsupported claims. 

- Single tweet must fit 280 characters. 

- Thread tweets must each fit 280 characters. 

- If one tweet would lose substance, recommend a thread. 

- No scheduling or posting. 

https://app.notion.com/p/GTM-Agent-7aaeb9c5f59182d4b2cb8173d8cd3c23 

9/16 

8/22/26, 11:12 PM 

GTM Agent | Notion 

#### 7. **`artifact-outreach`** : Research Artifact to Dripify Sequence 

#### Drafts 

Given a paper, benchmark, repo, blog post, or research artifact, identify relevant authors/contributors and prepare Dripify-ready outreach rows. 

##### Examples: 

```
Take this paper and find the authors worth reaching out to.
```

```
For this benchmark repo, identify the maintainers/researchers and
prepare LinkedIn-ready lead rows.
```

##### Tools: 

|Need|Preferred tool|
|---|---|
|Paper metadata/authors|Scholar/Semantic<br>Scholar/OpenAlex-style source<br>when available; otherwise web<br>search|
|Repo maintainers/contributors|GitHub search/API|
|Author profile enrichment|web search +<br>LinkedIn/professional data|
|Notion output|NotionMCP|
|Drafting|Codex skill using artifact context|



Notion fields: 

https://app.notion.com/p/GTM-Agent-7aaeb9c5f59182d4b2cb8173d8cd3c23 

10/16 

8/22/26, 11:12 PM 

GTM Agent | Notion 

|Field|Notes|
|---|---|
|Name|Person name|
|Organization|Lab, university, or company|
|Role|Current title or research role|
|LinkedIn URL|PrimaryDripify key|
|ConnectNote|Short connection note|
|FirstMessage|First post-connect message|
|Followup 1|First follow-up draft|
|Followup 2|Second follow-up draft|
|End ofSequence|Final close-the-loop draft|
|SourceArtifact|Paper/repo/benchmark that<br>surfaced them|
|Status|New,Reviewed,Rejected|



##### Hard rules: 

- Prioritize first/corresponding/senior authors, maintainers, and people at relevant labs/companies. 

- Check existing Notion rows by `LinkedIn URL` before creating new rows. 

- Draft the full Dripify sequence. 

- Do not send. 

- Stop at review. 

### Tooling Policy 

https://app.notion.com/p/GTM-Agent-7aaeb9c5f59182d4b2cb8173d8cd3c23 

11/16 

8/22/26, 11:12 PM 

GTM Agent | Notion 

|Tool /System|Policy|
|---|---|
|Codex skills|Own workflow instructions,<br>routing, hard rules, and output<br>shapes|
|NotionMCP|Primary read/write path for<br>review tables and docs|
|XAPI/MCP|Primary X read path and founder<br>voice source|
|Web search|Required for fresh<br>market/company/person/source<br>research|
|LinkedIn/professional data|Use only for<br>discovery/enrichment; no<br>browser-session automation|
|GitHub|Use for repos, maintainers, code<br>artifacts, and technical credibility|
|Scholar-style sources|Use for paper metadata and<br>author discovery where available|
|Dripify|External execution surface; agent<br>prepares fields only|
|Local scripts/adapters|Allowed only when noMCP/tool<br>exists or when deterministic<br>parsing/export is needed|



### Proposed New Project Structure 

https://app.notion.com/p/GTM-Agent-7aaeb9c5f59182d4b2cb8173d8cd3c23 

12/16 

8/22/26, 11:12 PM 

GTM Agent | Notion 

```
gtm-agent/ ├── README.md ├── AGENTS.md ├── design.md ├──
pyproject.toml ├── .env.example ├── .codex/ │ └── config.toml ├──
.agents/ │ └── skills/ │ ├── find-leads/ │ │ └── SKILL.md │ ├──
deep-search/ │ │ └── SKILL.md │ ├── x-reply-angles/ │ │ └── SKILL.md
│ ├── polish-x-drafts/ │ │ └── SKILL.md │ └── artifact-outreach/ │
└── SKILL.md ├── schemas/ │ └── notion.md ├── memory/ │ ├──
MEMORY.md │ ├── preferences.md │ ├── x-voice.md │ ├── x-topics.md │
├── outreach-voice.md │ └── outreach-topics.md ├── tools/ │ ├──
README.md │ ├── linkedin_fresh.py │ ├── x_read.py │ └── scholar.py
└── tests/ ├── test_tools.py └── canaries.md
```

#### Exact MCP Configuration 

> `.codex/config.toml` contains three project-scoped MCP servers: 

|Config name|Connection|Authentication|Allowed capabilities|
|---|---|---|---|
|`notion`|StreamableHTTP:<br>`https://mcp.notion.com/mcp`|OAuth|Search/fetch pages, query<br>databases, read comment<br>create rows, update draft|
|`x`|bridge<br>to<br>`npx @xdevplatform/xurl`<br>`https://api.x.com/mcp`|XOAuth 2.0PKCE|Search recent posts, fetch<br>post, fetch user/profile dat<br>fetch the founder's recent|
|`github`|OfficialGitHubMCP:<br>`https://api.githubcopilot.com/`<br>`mcp/`|OAuth orGitHub token|Repository/code search, fi<br>reads, contributor/maintai<br>metadata, releases and iss<br>research evidence|



Use each server's `enabled_tools` allowlist in `.codex/config.toml` . The X and GitHub servers must expose read operations only. Notion is the only MCP allowed to write, and only to the defined review databases/fields. 

#### Native Codex Tools 

https://app.notion.com/p/GTM-Agent-7aaeb9c5f59182d4b2cb8173d8cd3c23 

13/16 

8/22/26, 11:12 PM 

GTM Agent | Notion 

- Web search: primary tool for current market, company, funding, product, person, and news research. This is native Codex tooling, so there is no MCP entry or wrapper. 

- Shell: runs the three fallback CLIs and local validation only. 

- Filesystem: reads project memory and writes a Markdown research artifact only when explicitly requested. 

#### Local Fallback Tools 

These are narrow JSON CLIs, not an application layer. Each writes machinereadable JSON to stdout, diagnostics to stderr, exits non-zero on failure, and never sends, publishes, schedules, or changes third-party state. 

|File|Used when|Concrete operations<br>Cre|
|---|---|---|
|`tools/linkedin_fresh.py`|Always forLinkedIn/professional<br>profile discovery because no<br>LinkedIn browser/sessionMCPis<br>allowed|,<br>, and<br>againstFreshLinkedInDataAPI<br>onRapidAPI; normalize name,<br>company, role, location, and<br>LinkedIn URL<br>`search`<br>`poll`<br>`profile`<br>`RA`|
|`tools/x_read.py`|Only when XMCPis unavailable|,<br>, and<br> through XAPI; read-<br>only endpoints only<br>`search-posts`<br>`user-posts`<br>`get-post`<br>`X_`|
|`tools/scholar.py`|For paper/benchmark author<br>metadata when web search is<br>insufficient|and<br>; query<br>OpenAlex first andSemantic<br>Scholar as fallback; return<br>canonical title, URL, authors,<br>affiliations, and authorIDs<br>`artifact`<br>`authors`<br>opt<br>sec<br>`SE`|



> `pyproject.toml` exists only to declare the Python runtime, HTTP client, and tests for these tools. There is no installable GTM application package. 

#### - - Skill to Tool Routing 

https://app.notion.com/p/GTM-Agent-7aaeb9c5f59182d4b2cb8173d8cd3c23 

14/16 

8/22/26, 11:12 PM 

GTM Agent | Notion 

|Skill|Primary path|Fallback|
|---|---|---|
|`find-leads`|Codex web search →<br> →Notion<br>MCP<br>`linkedin_fresh.py`|None forLinkedIn; fail clearly if<br>FreshLinkedInData is unavailable|
|`deep-search`|Codex web search +GitHubMCP<br>+<br>;Notion<br>MCPonly if founder asks to save<br>`linkedin_fresh.py`|CLIfor publicGitHub reads<br>`gh`|
|`x-reply-angles`|XMCP→Codex web search for<br>linked evidence →NotionMCP|`x_read.py`|
|`polish-x-drafts`|NotionMCP+ XMCPfor<br>founder's recent posts|`x_read.py`|
|`artifact-outreach`|•GitHubMCP+<br>Codex web search +<br> →Notion<br>MCP<br>`scholar.py`<br>`linkedin_fresh.py`|Web search for artifact/author<br>metadata;<br>CLIfor public<br>repository reads<br>`gh`|



#### No Integration 

- Dripify: no MCP, API client, upload, or browser automation. The project only writes Dripify-ready copy fields to Notion. 

- LinkedIn: no browser automation, authenticated founder session, sending, connection requests, or engagement actions. 

- Typefully, Gmail, email, calendars, and CRMs: absent. 

#### Ownership 

- `AGENTS.md` contains global hard rules and founder-memory capture. 

- Each `SKILL.md` owns its trigger, routing order, output contract, and stop condition. 

- `schemas/notion.md` defines allowed Notion databases, fields, natural dedupe 

- keys, and the only statuses: `New` , `Reviewed` , and `Rejected` . 

- `memory/` stores founder preferences and voice evidence. 

https://app.notion.com/p/GTM-Agent-7aaeb9c5f59182d4b2cb8173d8cd3c23 

15/16 

8/22/26, 11:12 PM 

GTM Agent | Notion 

- `tests/test_tools.py` uses recorded fixtures; no live API spend in tests. 

- `tests/canaries.md` defines manual review checks across all five skills. 

#### Deliberately Absent 

- No `src/` package, backend, service, local database, cache, worker, queue, scheduler, or cron job. 

- No publishing, sending, Dripify execution, or generic tool abstraction layer. 

### Notion Tables 

Minimum tables: 

- `Dripify Leads` 

- `Research Reports` or saved research pages 

- `X Reply Opportunities` 

- `X Drafts` 

- `Artifact Outreach Leads` 

No local store is required in the design. Dedupe should happen by querying Notion for existing natural keys before inserting rows. Add local state later only if repeated API cost or async paid searches make it necessary. 

### - Explicit Non Goals 

- Standalone backend app 

https://app.notion.com/p/GTM-Agent-7aaeb9c5f59182d4b2cb8173d8cd3c23 

16/16 

