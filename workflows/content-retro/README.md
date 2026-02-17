# ContentRetro

**Type:** Weekly Automated Analysis  
**Skill Domain:** ContentVoice  
**Module:** 05  

## What It Does

Analyzes the performance of published LinkedIn content — identifying patterns in what works, what doesn't, and why. Produces actionable insights that feed back into the ideation and drafting process.

## How It Works

1. **Metrics pull:** Reads performance data from the Notion Content database (impressions, engagement, clicks)
2. **Pattern detection:** Identifies correlations between content attributes (theme, format, hook type, posting time) and performance
3. **Insight generation:** Produces a structured retrospective with top performers, underperformers, and hypotheses for why
4. **Recommendations:** Suggests adjustments to content strategy based on the data

## Design Decisions

- **Why a retrospective, not just a dashboard?** Dashboards show numbers. Retros generate insights. The difference is "Post X got 500 impressions" vs. "Posts with system-building themes consistently outperform career advice posts — consider shifting the mix."
- **Why weekly?** Matches the content creation cycle. Insights from this week's retro directly inform next week's ideation.
- **Feedback loop:** ContentRetro → WeeklyIdeation → ContentPackageGenerator → ContentRetro. The system is designed as a closed loop where performance data improves future content.

## Prompt File

→ [`prompt.md`](./prompt.md)
