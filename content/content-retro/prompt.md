# ContentRetro — Workflow Prompt

## Purpose
Analyze content performance over a specified period, generate actionable insights, and produce a retrospective with experiments to try.

## Pipeline

```
Fetch Metrics from Notion → Analyze Performance → Generate Recommendations → Publish Retro
```

## Metrics Analysis

### Data Sources
- Notion Content DB: Post titles, dates, tags, status
- LinkedIn metrics: Impressions, reactions, comments, shares, click-through rate
- Historical comparisons: Week-over-week and month-over-month trends

### Key Metrics Tracked

| Metric | What It Measures |
|--------|-----------------|
| Impressions | Reach / distribution |
| Reactions | Resonance |
| Comments | Engagement depth |
| Shares | Viral potential |
| CTR | Action-driving ability |
| Follower growth | Audience building |

### Performance Dimensions

**By Topic Tag:**
Which themes perform best? (AI, PM, Career, Spanish content, etc.)

**By Post Type:**
Text-only vs. carousel vs. video script. Which format drives engagement?

**By Language:**
English vs. Spanish performance comparison.

**By Day/Time:**
When do posts get the most traction?

**By Voice Adherence:**
Posts that follow the voice guide (no emojis, systems-over-tips, experience-first) vs. those that don't — which perform better?

## Recommendation Engine

### Analysis Categories

1. **What's working:** Top-performing themes, formats, and patterns
2. **What's not working:** Underperforming areas, declining metrics
3. **Experiments to try:** Specific tests based on the data
4. **Voice calibration:** Are the editorial rules helping or hurting?
5. **Content calendar suggestions:** What to write next week based on trends

### Experiment Format

```markdown
EXPERIMENT: [Name]
Hypothesis: [What you think will happen]
Test: [Specific action to take]
Metric: [How to measure success]
Duration: [How long to run]
```

## Notion Publishing

Creates a retro page in the Content DB with:
- Period covered (e.g., "Retro: Feb 3-16, 2026")
- Performance dashboard (metrics summary table)
- Top and bottom performers
- Trend analysis
- Recommendations and experiments
- Status: "Published"

## Usage

```bash
python main.py                    # Default: last 4 weeks
python main.py --weeks=2          # Custom period
python main.py --dry-run          # Preview without publishing
```

## Output Example

```
ContentRetro — Feb 3-16, 2026

Performance Summary:
  Posts published: 6
  Total impressions: 12,400 (+18% vs. prior period)
  Total reactions: 340 (+22%)
  Avg engagement rate: 4.2%

Top Performers:
  1. "Why I stopped automating my content" — 3,200 impressions, 89 reactions
  2. "The real cost of building in public" — 2,800 impressions, 72 reactions

Insights:
  ✓ Systems-thinking posts outperform tip-based content 2:1
  ✓ Spanish content has 40% higher engagement rate (smaller but loyal audience)
  ⚠ Carousel posts underperforming — may need visual refresh

Experiments:
  1. Test: Post at 7am PT instead of 9am PT (hypothesis: catch East Coast morning)
  2. Test: Add one "open question" ending per week (hypothesis: drives comments)

Retro published to Notion.
```

## File Structure

```
05_ContentRetro/
├── main.py                        # Orchestrator
├── performance_analyzer.py        # Metrics analysis
├── recommendation_engine.py       # Insight generation
├── notion_publisher.py            # Publish retro page
└── templates/
    └── retro_template.md
```

## Success Criteria

- Analyzes all posts in the specified period
- Identifies statistically meaningful patterns (not just anecdotes)
- Generates 2-3 specific, testable experiments
- Publishes clean retro page to Notion
- Total analysis time < 30 seconds
