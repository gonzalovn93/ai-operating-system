# WeeklyIdeation — Workflow Prompt

## Purpose
Scan 15+ content sources weekly, generate 12-20 ranked content ideas with quality scoring and risk flagging, then publish to Notion Content DB.

## Pipeline

```
Scan Sources → Generate Ideas → Filter & Rank → Publish to Notion → Summary
```

## Source Scanning

### Source Categories

| Category | Example Sources | Signal Type |
|----------|----------------|-------------|
| Industry newsletters | AI newsletters, PM newsletters | Trending topics, frameworks |
| Twitter/X thought leaders | AI researchers, PM leaders, founders | Hot takes, emerging discourse |
| Personal experience | Recent work, projects, decisions | Authentic stories, lessons |
| Podcast episodes | PM podcasts, startup podcasts | Deep frameworks, interviews |
| Competitor content | Other PM creators, similar voices | Gaps and opportunities |

### Theme-Specific Prompts (7 Themes)

| Theme | Language | Angle |
|-------|----------|-------|
| Tech & AI | English | Operating with AI, building AI products |
| PM & Growth | English | Product frameworks, growth strategies |
| Professional / Career | English | Career decisions, MBA lessons, networking |
| Productivity (ES) | Spanish | Systems, habits, intentional living |
| Entrepreneurship (ES) | Spanish | Startup lessons, founder journey |
| Identity & LatAm (ES) | Spanish | Cultural perspective, personal redefinition |
| Meta / Systems | English | Building systems, automation, tools |

## Idea Generation

Each idea includes:
- **Title:** Concise, specific (not clickbait)
- **Angle:** The specific perspective or hook
- **Key points:** 3-5 bullet points of what the post would cover
- **Source signal:** What triggered this idea
- **Tags:** Topic tags (determines language routing)
- **Quality score:** 1-10 based on originality, relevance, and voice fit
- **Risk flags:** Generic, too trendy, not lived experience, tip-list pattern

### Quality Scoring (1-10)

| Score | Criteria |
|-------|----------|
| 9-10 | Unique angle from lived experience, high voice fit, timely |
| 7-8 | Strong angle, good source signal, authentic connection |
| 5-6 | Decent topic but angle needs sharpening |
| 3-4 | Generic, could be written by anyone |
| 1-2 | Pure reaction content, no personal angle |

### Risk Flags
- **Generic:** Could be written by any PM on LinkedIn
- **Trendy:** Riding a wave without personal angle
- **Not lived:** No personal experience to ground it
- **Tip-list:** Sounds like "X things I learned"

## Notion Publishing

Ideas are published to the Content DB with:
- Title
- Status: "Backlog"
- Tags (determines English vs. Spanish)
- Date (required — views filter on it)
- Quality score
- Source notes

## Configuration

### `config/source_routing.yaml`
Maps themes to content sources — which newsletters, accounts, and feeds to scan for each theme.

### `config/quality_filters.yaml`
Defines quality thresholds and risk flag patterns.

### `config/writing_rules.yaml`
Tone, bilingual routing rules, and voice constraints.

## Usage

```bash
python main.py                    # Full weekly scan + generation
python main.py --theme="AI"      # Scan specific theme only
python main.py --dry-run          # Preview without publishing
```

## Output

```
WeeklyIdeation Complete

Generated: 16 ideas
Published: 14 to Notion (2 filtered for low quality)

By theme:
  Tech & AI: 4 ideas
  PM & Growth: 3 ideas
  Professional: 2 ideas
  Productivity (ES): 2 ideas
  Entrepreneurship (ES): 2 ideas
  Meta / Systems: 1 idea

Top ideas:
1. "Why I stopped automating my content workflow" (Score: 9)
2. "The Notion trap: when your system becomes the work" (Score: 8)
3. "Lo que nadie te dice sobre ser founder en EEUU" (Score: 8)

Tag distribution: AI (4), PM (3), Career (2), Productivity (2), ...
```

## File Structure

```
01_WeeklyIdeation/
├── main.py                    # Orchestrator
├── scan_sources.py            # Source fetching
├── generate_ideas.py          # Claude API idea generation
├── notion_publisher.py        # Publish to Content DB
├── linkedin_metrics.py        # Daily metrics fetch
├── config/
│   ├── source_routing.yaml
│   ├── quality_filters.yaml
│   └── writing_rules.yaml
└── prompts/                   # 7 theme-specific prompts
```

## Success Criteria

- Scans all configured sources
- Generates 12-20 ideas per week
- Quality score distribution: majority 7+
- Risk flags catch generic/tip-list patterns
- Published to Notion with correct tags and dates
- Language routing works (Spanish tags → Spanish content)
