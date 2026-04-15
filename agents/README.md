# Agents

High-context copilots with persistent memory, judgment, and defined operating styles — not generic prompts.

## What makes these different

Each agent is a Claude Project with an explicit *identity* (how it thinks), *operating style* (how it communicates), and *constraints* (what it should NOT do). They retain context across sessions and behave like senior teammates who know your background, goals, and constraints.

The key distinction: these agents *challenge* weak thinking. They're designed as collaborators, not typists.

## Agents

| Agent | Domain | What It Does | Type |
|-------|--------|-------------|------|
| [Career Strategy](./career-strategy/) | Career decisions | Parallel process management, offer evaluation, negotiation, tradeoff analysis | Claude Project |
| [Recruiting Strategist](./recruiting-strategist/) | Job pipeline | Company evaluation, pipeline sequencing, positioning, compensation analysis | Claude Project |
| [Personal Branding](./personal-branding/) | Public presence | Website, LinkedIn, content strategy as a coordinated system | Claude Project |
| [Positioning Strategist](./positioning-strategist/) | Narrative | Company-specific interview prep, story tailoring, narrative frameworks | Claude Project |
| [PM Copilot](./pm-copilot/) | Product work | PRD review, strategy critique, tradeoff analysis + 38 workflow templates | Claude Project |
| [Perplexity Intel Agent](./perplexity-intel-agent/) | Competitive intel | Weekly monitoring of Google AI, OpenAI, Microsoft Copilot, Anthropic | Python (production) |

## Example

**Input:**
```
"I have offers from Company A ($180K, Series B) and Company B ($155K, FAANG).
Company A wants an answer by Friday. What should I do?"
```

**Career Strategy Agent output:**
- Parallel process analysis: timeline pressure, leverage points, information gaps
- Framework: regret minimization, financial modeling, career trajectory comparison
- Recommended script for requesting a deadline extension from Company A
- Decision matrix with weighted criteria based on your stated goals

The agent knows your career history, risk tolerance, and long-term goals from prior sessions — it doesn't ask for context you've already given.

## How it works

- **Claude Projects** (5 agents): Persistent instruction files define identity, knowledge base, and constraints. Memory carries across sessions. Each agent has a `prompt.md` with the full system prompt.
- **Python agent** (Perplexity Intel Agent): Production script using Claude Sonnet + Tavily Search in a tool-use loop. Runs weekly via scheduler, outputs competitive intelligence reports.

## Files

Each agent folder contains:

| File | Purpose |
|------|---------|
| `README.md` | What the agent does and how to use it |
| `prompt.md` | Full system prompt — identity, operating style, constraints |
