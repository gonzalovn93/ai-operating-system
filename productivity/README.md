# Productivity

Automated daily workflows for information intake, goal tracking, learning capture, and time management — a closed-loop personal operating system.

## Workflows

| Workflow | Trigger | What It Produces | Status |
|----------|---------|------------------|--------|
| [**DailyDigest**](./daily-digest/) | Daily, 8am (automated) | AI-curated briefing from 85+ sources → Notion journal | ✅ Active |
| [**LearningCapture**](./learning-capture/) | `"I learned X from Y"` | Structured insights with metadata → Notion | ✅ Active |
| [**WeeklyReview**](./weekly-review/) | `"Do my weekly review"` | OKR progress + calendar hours + blockers → Notion | ✅ Active |
| [**QuarterlyOKRDesign**](./quarterly-okr-design/) | `"Plan my Q2 OKRs"` | Identity-aligned OKRs with capacity validation → Notion | ✅ Active |
| [**TaskManagement**](./task-management/) | `"Schedule my week"` | Energy-based time blocks → Google Calendar | ✅ Active |
| [**HabitTracking**](./habit-tracking/) | `"Update my initiatives"` | Calendar sync + manual logging → Notion | ✅ Active |
| [**GranolaSync**](./granola-sync/) | `"Sync my Granola notes"` | AI-enhanced meeting notes → routed Notion pages | ✅ Active |
| [**TimeTracking**](./time-tracking/) | `"Time dashboard"` / weekly | Hours-by-category from Calendar → Notion journal | ✅ Active |

## Example

**DailyDigest (runs every morning at 8am):**

- Fetches from 85+ sources: Twitter lists, RSS feeds, YouTube channels, Hacker News, Gmail newsletters
- Scores each item 0-100 by relevance to 10 rotating domains (AI Strategy, PM & Growth, Startups, etc.)
- Clusters related items by topic (0.35 similarity threshold)
- Generates Claude AI summaries for top 15 items
- Publishes a formatted digest to today's Notion journal page

Total time: ~45 seconds. Replaces 30+ minutes of manual feed scanning.

**WeeklyReview (runs on command):**

- Pulls OKR progress from Notion (auto-resolves quarter via relation properties)
- Fetches Google Calendar events, categorizes by color-code → time allocation table
- Compares actual hours against initiative targets (GoPlai, recruiting, training, etc.)
- Auto-updates initiative progress in Notion from calendar data
- Asks for manual OKR inputs (user counts, interview counts, etc.)
- Publishes full analysis to Notion journal

## How They Connect

```
DailyDigest (daily)          LearningCapture (on-demand)
  85+ sources → journal        Any insight → Aprendizajes DB
        |                              |
  Information intake              Knowledge base
        |                              |
QuarterlyOKRDesign  <-------  WeeklyReview
  Identity-aligned OKRs          Progress vs pace
        |                              ^
TaskManagement                  HabitTracking
  Calendar time blocks    ->    Initiative progress sync
```

The core workflows form a closed loop: DailyDigest feeds learning, LearningCapture structures it, QuarterlyOKRDesign sets goals, TaskManagement schedules execution, HabitTracking tracks progress, and WeeklyReview identifies gaps. Two more feed the loop: **GranolaSync** captures meeting notes into Notion automatically, and **TimeTracking** measures where the week's hours actually went — the data WeeklyReview holds against targets.

## Stack

Python · Claude API · Notion API · Google Calendar API · Granola API · Twitter API v2 · YouTube Data API · Gmail OAuth · feedparser · Windows Task Scheduler
