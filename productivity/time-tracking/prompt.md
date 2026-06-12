# TimeTracking — Workflow Prompt

## Purpose
Make time visible. Auto-categorize calendar events, then report weekly hours-by-category to Notion so actual effort can be measured against goals.

## Core Functionality

### Input
- Google Calendar events (a week, or a retroactive range)
- A category configuration: keywords, category ↔ color map, target allocations

### Processing
1. Tag uncolored events by keyword → assign a category color
2. Read the color-coded week and aggregate hours per category
3. Save a weekly JSON snapshot
4. Publish a formatted breakdown to the Notion journal
5. Flag categories that drift from their target allocation

### Output
- Color-coded calendar (events moved out of "Default")
- A weekly time-allocation table in Notion
- Per-week JSON snapshots for trend tracking
- Drift alerts vs. targets

## Triggers
- "Tag my calendar" / "Categorize my week"
- "Time dashboard" / "How did I spend my week?"
- (Feeds "Do my weekly review")

## Design Notes
- **Calendar is the accountability layer** — color-coded events map to OKR categories.
- **Dry-run first** — preview tagging and the dashboard before any write.
- **Snapshots enable trends** — weekly JSON makes drift over time legible.
