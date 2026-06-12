# RelationshipNurture

**Type:** Automated Python Workflow
**Skill Domain:** CareerOS
**Command:** `python main.py nurture`

## What It Does

Makes sure no warm relationship goes cold. Where NetworkingScout handles *new* outreach, RelationshipNurture handles *maintenance* — it reads the Notion Network database, applies a per-relationship cadence, and surfaces a daily report of *who needs attention, what to say, and why*. Maintaining 80+ relationships stops being a memory game.

## How It Works

1. **Read:** Pulls Strong / Warm / Cold contacts from the Notion Network DB (the "new outreach" set — *Haven't met* — is deliberately excluded; that's NetworkingScout's job)
2. **Apply cadence:** Each relationship stage has a follow-up rhythm; a manually-set "next touchpoint" date overrides the automatic one
3. **Detect overdue:** Anyone past their cadence (plus a grace period) surfaces as needing attention today; the next 7 days surface as "coming up"
4. **Cluster by company:** Contacts at the same company are grouped so insights compound across conversations
5. **Draft follow-ups:** Generates a context-aware message per overdue contact, pulled from the "Long Game" notes captured on their page (key insight, personal details, follow-up plan)
6. **Log touchpoints:** After a message is actually sent, one command writes the interaction date back to Notion and resets the cadence

## Cadence Model

| Stage | Cadence | Default follow-up |
|-------|---------|-------------------|
| Strong | every 2 weeks | Process update / ask / share a win |
| Warm | every 4 weeks | "Here's what's happened since we talked" |
| Cold | every 8 weeks | Lightweight touch (share an article, congrats) |
| Dormant | never auto | Reactivate only on a genuine reason |

## Design Decisions

- **Why split nurture from new outreach?** They're different motions with different goals — starting a relationship vs. compounding one. Partitioning by the `Relationship health` field keeps each workflow focused and prevents the two from stepping on each other.
- **Why `Last interaction` as the only cadence baseline?** A contact tagged Warm who was never actually spoken to should surface as a *data-hygiene nudge*, not as "wildly overdue." First-contact date is deliberately **not** a fallback — the cadence counts from real conversations only.
- **Why drafts, never auto-send?** The whole point is genuine connection. Every message is drafted from real context (a personal detail, a shared thread) for review — the system never sends on its own.
- **Why company clusters?** The high-leverage move isn't one coffee chat — it's a compounding point of view built from multiple insiders. Grouping contacts by company makes the gaps in that picture visible.

## Architecture

```
nurture/
├── nurture.py       # Orchestrator + CLI (daily, weekly, company, touch)
├── cadence.py       # Cadence rules + overdue / at-risk detection
├── notion_sync.py   # Reads contacts + "Long Game" page sections; logs touchpoints
├── drafts.py        # Context-aware follow-up drafting by relationship stage
└── report.py        # Daily report + Monday weekly summary rendering
```

## Prompt File

→ [`prompt.md`](./prompt.md)
