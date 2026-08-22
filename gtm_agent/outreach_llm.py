"""Agent-backed writing help for research outreach.

Drafting runs through the Claude Agent SDK — the same agent already driving
this repo's skills — so there is no separate model API key to hold. It
authenticates the way Claude Code does; ``ANTHROPIC_API_KEY`` is honoured if
set but nothing here requires one.

The model only ever rephrases facts this app already fetched from OpenAlex or
Semantic Scholar. It is never asked to recall or guess who someone is, where
they work, or where their profiles live — that is exactly the kind of detail an
LLM invents confidently, and a wrong affiliation in a cold email is fatal.
"""

import asyncio
import json
import os
import time

from gtm_agent import trajectory

try:
    from claude_agent_sdk import (
        AssistantMessage,
        ClaudeAgentOptions,
        ResultMessage,
        TextBlock,
        ThinkingBlock,
        query,
    )
except ImportError:  # pragma: no cover - exercised only without the extra installed
    query = None

DEFAULT_MODEL = os.environ.get("OUTREACH_MODEL", "claude-opus-5")
TIMEOUT_SECONDS = 120

GROUNDING_RULE = (
    "Use only the facts in the JSON provided. Never add employers, titles, locations, "
    "personal details, or claims that are not present. If a fact is missing, leave it out "
    "rather than guessing. A name does not reveal anyone's gender, so never use he or she: "
    "use the person's name or they. Write plainly, with no marketing language and no em dashes."
)


class OutreachLLMError(RuntimeError):
    """Writing help was unavailable. Callers must keep the fetched facts usable."""


async def _run(system: str, user: str) -> tuple[str, str | None, dict, float | None]:
    """One single-turn, tool-less agent call. Returns (text, thinking, usage, cost)."""
    options = ClaudeAgentOptions(
        system_prompt=system,
        model=DEFAULT_MODEL,
        max_turns=1,
        # Pure text generation: no tool should ever fire, and the agent must not
        # inherit this repo's settings/skills — the prompt is the whole contract.
        allowed_tools=[],
        disallowed_tools=["Bash", "Edit", "Write", "NotebookEdit", "Read", "Glob", "Grep", "WebSearch", "WebFetch", "Agent"],
        setting_sources=[],
    )
    chunks: list[str] = []
    thinking: list[str] = []
    usage: dict = {}
    cost: float | None = None
    result_text: str | None = None

    async for message in query(prompt=user, options=options):
        if isinstance(message, AssistantMessage):
            for block in message.content:
                if isinstance(block, TextBlock):
                    chunks.append(block.text)
                elif isinstance(block, ThinkingBlock):
                    thinking.append(getattr(block, "thinking", "") or "")
        elif isinstance(message, ResultMessage):
            if message.is_error:
                raise OutreachLLMError(
                    f"The writing agent failed: {message.result or message.api_error_status or 'unknown error'}"
                )
            result_text = message.result
            cost = message.total_cost_usd
            raw_usage = message.usage
            usage = raw_usage if isinstance(raw_usage, dict) else (dict(raw_usage or {}) if raw_usage else {})

    text = (result_text or "".join(chunks)).strip()
    if not text:
        raise OutreachLLMError("The writing agent returned an empty draft.")
    return text, ("\n".join(t for t in thinking if t) or None), usage, cost


def _chat(system: str, user: str, max_tokens: int, purpose: str = "") -> str:
    """Draft one message.

    ``max_tokens`` is advisory here — the agent SDK takes no output cap, so the
    real length limits are the explicit word/character ceilings written into
    each caller's system prompt. It is still passed through to the trajectory
    so drafts stay comparable with runs made before the switch.
    """
    if query is None:
        trajectory.log_llm(DEFAULT_MODEL, system, user, purpose=purpose, error="claude-agent-sdk not installed")
        raise OutreachLLMError(
            "claude-agent-sdk is not installed, so drafting is off. Run `uv sync`. "
            "The scholarly facts above still apply."
        )
    try:
        asyncio.get_running_loop()
    except RuntimeError:
        pass
    else:
        trajectory.log_llm(DEFAULT_MODEL, system, user, purpose=purpose, error="called from a running event loop")
        raise OutreachLLMError("Drafting cannot run inside an active event loop. Call it from sync code.")

    started = time.monotonic()
    try:
        text, reasoning, usage, cost = asyncio.run(
            asyncio.wait_for(_run(system, user), timeout=TIMEOUT_SECONDS)
        )
    except OutreachLLMError as exc:
        trajectory.log_llm(DEFAULT_MODEL, system, user, purpose=purpose, error=str(exc),
                           latency_s=round(time.monotonic() - started, 3))
        raise
    except asyncio.TimeoutError as exc:
        trajectory.log_llm(DEFAULT_MODEL, system, user, purpose=purpose,
                           error=f"timed out after {TIMEOUT_SECONDS}s",
                           latency_s=round(time.monotonic() - started, 3))
        raise OutreachLLMError("The writing agent timed out. Please try again shortly.") from exc
    except Exception as exc:
        trajectory.log_llm(DEFAULT_MODEL, system, user, purpose=purpose, error=f"{type(exc).__name__}: {exc}",
                           latency_s=round(time.monotonic() - started, 3))
        raise OutreachLLMError("The writing agent is unavailable right now. Please try again shortly.") from exc

    trajectory.log_llm(
        DEFAULT_MODEL, system, user, response=text, reasoning=reasoning, purpose=purpose,
        usage=usage, latency_s=round(time.monotonic() - started, 3), cost_usd=cost,
        max_tokens_hint=max_tokens,
    )
    return text


TONE_INSTRUCTION = (
    "previously_sent_messages, if present, are messages the sender has actually sent before — match "
    "their tone, voice, and level of formality. Do not copy their content or claims, only the style."
)


def paper_blurb(paper: dict, notes: str = "", tone_examples: list[str] | None = None) -> str:
    """Short blurb about a paper — the shared context every outreach message
    to its authors builds on."""
    facts = {
        "title": paper.get("title"),
        "year": paper.get("year"),
        "abstract": paper.get("abstract"),
        "topics": paper.get("topics"),
        "your_notes_on_it": notes or None,
        "previously_sent_messages": tone_examples or None,
    }
    return _chat(
        system=(
            "Write a 2-4 sentence blurb about this paper for someone about to reach out to its "
            "authors. Center it on your_notes_on_it if present, since that is the reader's own take "
            "on what mattered — use the abstract only to fill in what the notes don't cover. "
            f"Plain, specific, no marketing language. {TONE_INSTRUCTION} " + GROUNDING_RULE
        ),
        user=json.dumps(facts, ensure_ascii=False),
        max_tokens=220,
        purpose="paper_blurb",
    )


CHANNEL_GUIDANCE = {
    "Email": "A cold email. Give it a subject line on the first line prefixed 'Subject: ', then the body. Keep the body under 130 words. Do not open with a greeting line — a salutation with the recipient's name is prepended separately.",
    "LinkedIn": "A LinkedIn connection-request note. Hard limit of 200 characters total (LinkedIn's own cap on connection notes) — this is not negotiable, stay under it. No subject line, no signature.",
    "X": "A direct message on X. Under 400 characters, conversational, no subject line.",
}


def outreach_message(
    *, paper_blurb_text: str, channel: str, sender: str | None = None, tone_examples: list[str] | None = None
) -> str:
    """Draft one outreach message for a paper, grounded in the shared blurb.
    Not personalized per recipient — the same message is reused for every
    selected author on a given channel."""
    facts = {
        "paper_blurb": paper_blurb_text,
        "about_the_sender": sender,
        "previously_sent_messages": tone_examples or None,
    }
    return _chat(
        system=(
            f"You write outreach to an academic paper's authors on behalf of the sender. "
            f"{CHANNEL_GUIDANCE.get(channel, CHANNEL_GUIDANCE['Email'])} "
            "Ground the message in paper_blurb. Write it generically enough to send to any of the "
            "paper's authors as-is — do not address a specific person by name. State genuine interest, "
            f"ask one low-friction question, and do not promise anything. Return the message only, with "
            f"no commentary. {TONE_INSTRUCTION} " + GROUNDING_RULE
        ),
        user=json.dumps(facts, ensure_ascii=False),
        max_tokens=400,
        purpose=f"outreach_message:{channel}",
    )


FOLLOWUP_CHANNEL_GUIDANCE = {
    "Email": "A short follow-up email replying in the same thread. No subject line, body only. Under 60 words.",
    "X": "A short follow-up direct message on X. Under 200 characters.",
    "LinkedIn": "A short LinkedIn connection-request follow-up note. Hard limit of 200 characters total "
    "(LinkedIn's own cap) — this is not negotiable, stay under it. No subject line, no signature.",
}


def followup_message(
    *, previous_message: str, channel: str, followup_number: int, tone_examples: list[str] | None = None
) -> str:
    """A brief nudge referencing a message that got no reply. Never restates
    the original pitch in full. `followup_number` 2 (the last one, per
    send_followups.py's two-follow-up cap) is written even shorter and gives
    the reader an easy out, since two silences is a stronger signal than one."""
    facts = {
        "previous_message_sent": previous_message,
        "which_followup": f"{followup_number} of 2",
        "previously_sent_messages": tone_examples or None,
    }
    tone_note = (
        "This is the final follow-up — keep it especially brief and give the reader an easy out, "
        "e.g. 'no worries if now isn't a good time'."
        if followup_number >= 2
        else "Keep it brief and low-pressure."
    )
    return _chat(
        system=(
            "You write a brief follow-up to a message that got no reply on behalf of the sender. "
            f"{FOLLOWUP_CHANNEL_GUIDANCE.get(channel, FOLLOWUP_CHANNEL_GUIDANCE['Email'])} "
            f"Reference previous_message_sent briefly rather than restating the full pitch. {tone_note} "
            f"Return the message only, with no commentary. {TONE_INSTRUCTION} " + GROUNDING_RULE
        ),
        user=json.dumps(facts, ensure_ascii=False),
        max_tokens=180,
        purpose=f"followup_{followup_number}:{channel}",
    )
