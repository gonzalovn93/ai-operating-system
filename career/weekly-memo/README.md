# WeeklyMemo

**Type:** Automated Python Workflow  
**Skill Domain:** CareerOS  
**Command:** `python main.py memo`  

## What It Does

Generates a strategic pipeline report — analyzing the current state of my job search, identifying bottlenecks, prioritizing next actions, and surfacing risks. Treats the recruiting pipeline like a product funnel.

## How It Works

1. **Pipeline analysis:** Reads the Applications, Companies, and Network databases to build a current-state view
2. **Funnel metrics:** Calculates conversion rates across stages (discovered → applied → screening → interview → offer)
3. **Task generation:** Produces prioritized action items based on where the pipeline is weakest
4. **Strategic assessment:** Flags risks (stalled processes, over-concentration, timeline pressure) and opportunities
5. **Output:** A structured memo in Notion with sections for pipeline health, priorities, actions, and risks

## Design Decisions

- **Why a memo, not a dashboard?** Dashboards show data. Memos make recommendations. The weekly memo doesn't just say "you have 5 applications in screening" — it says "3 of those have been in screening for 2+ weeks with no update, consider following up or deprioritizing."
- **Why weekly?** Daily would be noise. Monthly would miss inflection points. Weekly matches the natural rhythm of recruiting — enough time to take action, short enough to course-correct.

## Architecture

```
weekly_memo/
├── memo_generator.py       # Main orchestrator and memo formatting
├── pipeline_analyzer.py    # Cross-database analysis and funnel metrics
└── task_generator.py       # Prioritized action item generation
```

## Prompt File

→ [`prompt.md`](./prompt.md)
