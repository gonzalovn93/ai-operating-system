# Productivity

Automated daily workflows and personal operating system for information intake, goal tracking, learning capture, and time management — all running through natural language commands in Claude Code.

## Workflows

| Workflow | Schedule / Trigger | What It Produces |
|----------|-------------------|-----------------|
| [**DailyDigest**](./daily-digest/) | Daily, 8am (automated) | AI-curated briefing from 85+ sources → Notion journal |
| [**LearningCapture**](./learning-capture/) | "I learned X from Y" | Structured insights with metadata → Notion Aprendizajes |
| [**WeeklyReview**](./weekly-review/) | "Do my weekly review" (Mondays) | OKR progress, calendar reality check, blocker analysis → Notion journal |
| [**QuarterlyOKRDesign**](./quarterly-okr-design/) | "Plan my Q2 OKRs" (end of quarter) | Identity-aligned OKRs with capacity validation → Notion |
| [**TaskManagement**](./task-management/) | "Schedule my week" | Energy-based time blocks → Google Calendar |
| [**HabitTracking**](./habit-tracking/) | "Update my initiatives" | Calendar sync + manual logging → Notion initiative progress |

## How They Connect

```
DailyDigest (daily)          LearningCapture (on-demand)
  85+ sources → journal        Any insight → Aprendizajes DB
        ↓                              ↓
  Information intake              Knowledge base
        ↓                              ↓
QuarterlyOKRDesign ← ── ── ── WeeklyReview
  Identity-aligned OKRs          Progress vs pace
        ↓                              ↑
TaskManagement                  HabitTracking
  Calendar time blocks    →     Initiative progress sync
```

The six workflows form a closed loop: DailyDigest feeds learning, LearningCapture structures it, QuarterlyOKRDesign sets goals, TaskManagement schedules execution, HabitTracking tracks progress, and WeeklyReview identifies gaps.

## Stack

Python · Claude API · Notion API · Google Calendar API · Twitter API v2 · YouTube Data API · Gmail OAuth · feedparser · Windows Task Scheduler
