# WeeklyReview

**Type:** Automated Workflow (Python + Notion API + Google Calendar API)
**Skill Domain:** LearningProductivity
**Trigger:** Manual — "Do my weekly review", recommended Mondays

## What It Does

Automates the Monday weekly review by fetching OKR progress from Notion, checking Google Calendar for actual time spent, calculating progress vs targets, identifying blockers at critical/high/medium severity, and generating actionable insights. Publishes a full review to the Notion journal and updates the local tracking file.

## How It Works

```
Notion OKRs  →  Notion Initiatives  →  Calendar hours  →  Gap analysis  →  Blockers  →  Journal
  Progress        Time allocation       Actual vs plan     Expected pace    Severity     Notion +
  by pillar       by priority            per activity       calculations     rankings     CurrentState.md
```

1. **Fetch OKRs:** Query Notion for current quarter's Key Results with progress percentages
2. **Fetch Initiatives:** Get habit/initiative data with priority rankings
3. **Calendar Check:** Count actual hours spent on each activity via Google Calendar
4. **Calculate Gaps:** Compare actual progress vs expected pace based on week number
5. **Identify Blockers:** Flag critical (0% after week 3), high (below half pace), and medium (time deficit) issues
6. **Generate Insights:** What worked, what didn't, patterns, recommendations
7. **Publish:** Create journal entry in Notion + update local CurrentState.md

## Design Decisions

- **Why calendar reality check?** Notion tracks goals; Calendar tracks reality. Comparing them reveals the gap between intention and execution.
- **Why severity levels?** Not all blockers are equal. A 0% OKR in week 7 is critical; a slight time deficit is medium. Severity helps prioritize action.
- **Why mid-quarter detection?** Week 7 gets special treatment — it's the last chance to course-correct before the quarter ends.

## Architecture

```
WeeklyReview/
├── OKR Fetcher         # Notion API → progress data
├── Initiative Fetcher  # Notion API → habit data
├── Calendar Checker    # Google Calendar → actual hours
├── Gap Calculator      # Expected vs actual progress
├── Blocker Identifier  # Severity-ranked issues
├── Insight Generator   # Patterns + recommendations
└── Publishers
    ├── notion_client.py    # Journal entry
    └── CurrentState.md     # Local tracking file
```

## Prompt File

> [`prompt.md`](./prompt.md)
