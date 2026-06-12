# RelationshipNurture — Workflow Prompt

## Purpose
Keep warm relationships warm. Surface who's overdue for a touchpoint, draft a genuine follow-up from real context, and log the interaction back to Notion once it's sent.

## Core Functionality

### Input
- Notion Network DB (Strong / Warm / Cold contacts)
- Per-contact fields: relationship stage, last interaction, optional next-touchpoint override, company
- Per-page "Long Game" notes: key insight, personal details, compounding POV, follow-up plan

### Processing
1. Load the nurture set (Strong / Warm / Cold; exclude *Haven't met*)
2. Compute each contact's due date from cadence, or a manual override if set
3. Bucket contacts: overdue (past cadence + grace), coming up (next 7 days), at risk (2× cadence with no touchpoint)
4. Cluster contacts by company and synthesize a compounding point of view
5. Draft a follow-up per overdue contact using the page's Long Game context
6. On `--touch`, write the interaction date to Notion and reset the cadence

### Output
- **Daily report:** overdue (with drafts), coming up, company clusters, stats
- **Weekly summary:** priority contacts, relationships at risk, company POV updates
- **Touchpoint log:** `Last interaction` / `Next touchpoint` updated in Notion (the only write)

## Triggers
- "Who do I need to follow up with?" / "Run my nurture report"
- "Weekly nurture summary"
- "Nurture status at [company]"
- "I just talked to [name]" / "Log a touchpoint with [name]"

## Design Notes
- **Never auto-sends** — drafts only, always reviewed before sending.
- **Cadence counts from real conversations** (`Last interaction`), not first-contact date.
- **Compounding over referrals** — the report optimizes for richer company-level POV, not just touchpoint volume.
