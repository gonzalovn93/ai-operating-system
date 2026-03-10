# HabitTracking

**Type:** Hybrid Workflow (Automatic calendar sync + Manual input)
**Skill Domain:** LearningProductivity
**Trigger:** Manual — "Update my initiatives", "I did X hours of Y"

## What It Does

Bridges the gap between Google Calendar time blocks and Notion initiative tracking. Supports two modes: automatic calendar-based updates (bulk sync last week's events to initiative progress) and manual input (quick daily logging or corrections). Maps calendar event names to initiatives using a keyword dictionary.

## How It Works

```
Method A (Auto):                              Method B (Manual):
Calendar events  →  Keyword match  →  Update    User input  →  Parse  →  Update
  Last 7 days       Initiative map    Notion      "2h GOPLAI"   Amount    Notion
                                                                Initiative
```

1. **Calendar sync:** Read last week's events, match to initiatives by keyword (e.g., "GOPLAI Deep Work" → "Dedicar 10h a la semana GOPLAI")
2. **Manual input:** Parse natural language ("I did 2 hours of GOPLAI") to extract amount and initiative
3. **Corrections:** Detect correction language ("actually only 4x") and set absolute values instead of adding
4. **Update:** Push new progress to Notion Initiatives database
5. **Summary:** Show before/after progress with percentage changes

## Design Decisions

- **Why two methods?** Calendar sync is great for weekly bulk updates but misses ad-hoc work. Manual input catches everything else. Together they provide complete tracking.
- **Why keyword mapping?** Calendar events have inconsistent naming. A flexible keyword dictionary ("Gym", "Training", "Entrenar" all map to the same initiative) handles real-world messiness.
- **Why correction detection?** Users often say "actually I only did 4" — this needs to replace, not add. Detecting correction language prevents double-counting.

## Architecture

```
HabitTracking/
├── Calendar Sync       # Google Calendar → keyword matching
├── Manual Parser       # Natural language → initiative + amount
├── Correction Handler  # Detect "actually" / "only" → set vs add
├── Notion Updater      # Update initiative progress
└── Tools
    ├── calendar_client.py  # Google Calendar API
    └── notion_client.py    # Notion API
```

## Prompt File

> [`prompt.md`](./prompt.md)
