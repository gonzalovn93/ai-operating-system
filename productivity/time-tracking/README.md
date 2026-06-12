# TimeTracking

**Type:** Automated Python Workflow
**Skill Domain:** LearningProductivity
**Command:** `python time_dashboard.py` · `python calendar_tagger.py`

## What It Does

Turns Google Calendar into a time-accountability layer. It auto-classifies uncolored events into categories, then generates a weekly time-allocation dashboard — hours per category — and publishes it to the Notion journal. This is the data layer WeeklyReview compares actual hours against initiative targets.

## How It Works

1. **Tag:** `calendar_tagger` scans recent calendar events, classifies uncolored ones by keyword, and assigns a `colorId` so each event maps to a category (GoPlai, recruiting, training, etc.)
2. **Aggregate:** `time_dashboard` reads the now-color-coded week and sums hours by category
3. **Snapshot:** Saves a per-week JSON snapshot so time allocation is trackable over time
4. **Publish:** Writes a formatted weekly breakdown to the Notion journal page
5. **Alert:** Flags when a category drifts meaningfully from its target allocation

## Design Decisions

- **Why the calendar as source of truth?** The calendar is where time actually goes — it's a higher-fidelity record of effort than self-reported logs. Color-coding events turns a passive schedule into a measurable accountability signal.
- **Why auto-tagging?** Manually coloring every event never survives a busy week. Keyword classification handles the long tail automatically, so the dashboard reflects reality instead of only the events I remembered to label.
- **Why weekly JSON snapshots?** A point-in-time number isn't insight. Persisting weekly snapshots makes drift visible — am I trending away from the things I said matter? — which is exactly what the weekly review needs.

## Architecture

```
TimeTracking/
├── calendar_tagger.py     # Classifies uncolored events → category colorId
├── time_dashboard.py      # Weekly hours-by-category dashboard → Notion
├── config.py              # Category keywords + category ↔ color map + targets
└── data/time-tracking/    # Per-week JSON snapshots (2026-Wxx.json)
```

## Prompt File

→ [`prompt.md`](./prompt.md)
