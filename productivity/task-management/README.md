# TaskManagement

**Type:** Conversational Workflow (Claude Code + Google Calendar API)
**Skill Domain:** LearningProductivity
**Trigger:** Manual — "Schedule my week", "Block time for X"

## What It Does

Converts habits, goals, and priorities into scheduled time blocks in Google Calendar using energy patterns and pre-defined templates. Understands optimal block sizes per activity, respects existing commitments, and distributes work across the week.

## How It Works

```
User request  →  Parse activity  →  Apply energy rules  →  Check conflicts  →  Create events
  "12h GOPLAI"    Type, duration     Peak/low times         Existing calendar    Google Calendar
  "4 gym sessions" Block size         Optimal placement      MBA schedule         Color-coded
```

1. **Parse:** Extract activity type, time commitment, date range, and preferences
2. **Energy:** Apply energy pattern rules — deep work at peak times (9-11am), gym at consistent times (6pm), meetings during low energy (1-3pm)
3. **Distribute:** Calculate optimal block sizes (2h for deep work, 1h for gym) and spread across the week
4. **Conflict check:** Verify against existing calendar events, ensure buffers between sessions
5. **Schedule:** Create color-coded Google Calendar events with goals in descriptions

## Design Decisions

- **Why energy-based scheduling?** 2 hours of deep work at 9am produces more than 4 hours at 2pm. Scheduling around energy patterns maximizes output per hour.
- **Why block size limits?** Diminishing returns after 2 hours of deep work is well-documented. Enforcing this prevents "marathon" sessions that feel productive but aren't.
- **Why conflict checking?** Without it, the system would double-book over MBA classes and existing commitments.

## Architecture

```
TaskManagement (Conversational + API)
├── Request Parser      # Extract activity, time, constraints
├── Energy Optimizer    # Map activities to optimal time slots
├── Conflict Checker    # Verify against existing calendar
└── Calendar Integration
    └── calendar_client.py  # Google Calendar API
```

## Prompt File

> [`prompt.md`](./prompt.md)
