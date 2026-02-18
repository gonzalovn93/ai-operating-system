# NetworkingScout

**Type:** Automated Python Workflow  
**Skill Domain:** CareerOS  
**Command:** `python main.py scout`  

## What It Does

Finds and scores relevant networking contacts at target companies, prioritizing alumni connections and role relevance. Produces a ranked outreach list — not a random one.

## How It Works

1. **Discovery:** Searches for contacts at a specified company using LinkedIn data
2. **Alumni detection:** Identifies Berkeley and other relevant alumni network overlaps
3. **Scoring:** Multi-factor scoring model weighing relevance, seniority, alumni connection, shared background, and reachability
4. **Message generation:** Produces contextual outreach suggestions based on the contact's profile
5. **Output:** Writes scored contacts to the Notion Network database

## Scoring Model

The scoring engine uses a weighted multi-factor model:

| Factor | What It Measures |
|--------|-----------------|
| Role relevance | How close is their role to PM / product leadership? |
| Seniority | Are they senior enough to influence hiring? |
| Alumni overlap | Shared school, program, or cohort? |
| Shared background | Common industries, companies, or interests? |
| Reachability | How likely are they to respond? (1st degree, 2nd degree, open to networking) |

Alumni connections receive a significant scoring boost — the shared context dramatically increases response rates.

## Design Decisions

- **Why scoring instead of just listing contacts?** Without scoring, every outreach list looks the same. Scoring forces prioritization — I spend time on the contacts most likely to convert to meaningful conversations, not just the most visible ones.
- **Why alumni detection as a separate module?** Alumni status is the single highest-leverage signal in networking. Isolating it as a detection module makes the scoring transparent and tunable.
- **Why generate message context?** Having a 2-line reason for reaching out ("you were PM at [company] and transitioned from fintech — I'm on a similar path") saves 10 minutes per outreach and produces better messages.

## Architecture

```
networking_scout/
├── networking_scout.py     # Main orchestrator
├── berkeley_detector.py    # Alumni network detection
├── scoring.py              # Multi-factor scoring engine
└── message_generator.py    # Contextual outreach suggestion generator
```

## Prompt File

→ [`prompt.md`](./prompt.md)
