# DailyDigest — Workflow Prompt

## Purpose
Aggregate 85+ content sources daily, score and cluster by relevance, generate AI summaries, and publish a curated digest to a Notion journal page.

## Architecture

### Pipeline
```
Fetch (5 fetchers) → Score (0-100) → Diversity Caps → Domain Rotation → AI Summaries → Notion Publish
```

### 5 Content Fetchers

| Fetcher | Sources | Method |
|---------|---------|--------|
| Twitter/X | 15 accounts (AI leaders, founders, company accounts) | Bearer token API |
| RSS | 55+ feeds (newsletters, blogs, podcasts) | feedparser |
| YouTube | 12 channels (tech, sports, culture) | YouTube Data API |
| Hacker News | Top 20 stories | HN API |
| Gmail | Curated newsletters (link extraction + enrichment) | Gmail OAuth API |

### 10 Rotating Domains

| Domain | Weight | Focus |
|--------|--------|-------|
| AI Strategy | 25 | AI product strategy, model releases, research |
| PM & Growth | 22 | Product management, growth frameworks |
| Startups & Venture | 20 | Fundraising, founder stories, VC |
| Psychology & Decisions | 15 | Behavioral science, decision-making |
| Life Design | 12 | Productivity, career, personal development |
| Sports-Tech | 18 | Sports analytics, fan tech, athlete tech |
| Culture & Film | 10 | Film criticism, cultural commentary |
| Fintech | 14 | Financial technology, crypto, payments |
| Tech Platforms | 16 | Platform strategy, developer tools |
| Tech Industry | 22 | Company releases, product launches |

Domains rotate by day of week — 4 domains are "in focus" each day with boosted weights.

## Priority Scoring (0-100)

```python
score = (
    source_tier_base       # Tier 1-4 sources (30-5 pts)
    + domain_weight        # Based on rotation schedule (10-25 pts)
    + recency_bonus        # Newer = higher (0-15 pts)
    + engagement_scaled    # Platform-specific scaling (0-8 pts)
    + platform_adjustment  # Twitter -10, newsletters +10
)
```

### Engagement Scaling (Platform-Specific)
- Twitter: Capped at 8 points (prevents viral tweets from dominating)
- RSS/Newsletters: Up to 15 points (rewards curated content)
- Hacker News: Based on points and comment count

## Diversity Enforcement

### Per-Author Cap
Maximum 1 item per author in the final digest. If an author has multiple items, keep the highest-scored one.

### Per-Platform Cap
Maximum 5 items from any single platform. Prevents Twitter or HN from dominating.

### Pipeline Order
Scoring → Author caps → Platform caps → Domain rotation → Final selection (15 items)

## Newsletter Link Extraction

Curated newsletters (like daily AI roundups) contain multiple article links. Instead of treating the whole email as 1 item:

1. Extract individual links from configured newsletters
2. Filter out tracking/unsubscribe URLs
3. Fetch actual article titles via HTML meta tags
4. Each link becomes a separate scored item

```python
NEWSLETTER_CONFIGS = {
    "newsletter@example.com": {
        "name": "Newsletter Name",
        "extract_links": True,
        "link_selectors": ["a[href]"],
        "exclude_patterns": ["unsubscribe", "tracking", "beehiiv", "mailchimp"]
    }
}
```

## AI Summarization

For each of the 15 final items, generate a 2-3 sentence summary using Claude:
- What happened / what was said
- Why it matters to a PM / builder
- One actionable takeaway or question

## Notion Publishing

### Output Format
Appends to today's journal page with:
- Platform mix stats (Twitter: X, RSS: X, HN: X, Gmail: X)
- Domain-grouped items with emoji prefixes
- High-priority items (score >= 80) marked with fire emoji
- Each item: title, source, score, AI summary, link

### Journal Integration
- Finds today's journal page by Entry Date property
- Creates page if it doesn't exist
- Appends digest as blocks (headings, paragraphs, dividers)
- Rich text truncated to 2000 chars (Notion API limit)
- Maximum 100 blocks per API call

## Configuration

### `config/sources.json`
All 85+ sources organized by domain, with tier assignments and platform metadata.

### `config/rotation_schedule.json`
Day-of-week → domain focus mapping (which 4 domains are boosted each day).

## Usage

```bash
python main.py                    # Standard run (today)
python main.py --dry-run          # Preview without publishing
python main.py --date 2026-02-15  # Run for specific date
```

## Scheduling

Runs daily at 8:00 AM via Windows Task Scheduler.

**Important scheduler settings:**
- `DisallowStartIfOnBatteries=false` (required for laptops)
- `StopIfGoingOnBatteries=false`
- `StartWhenAvailable=true` (catches up if machine was asleep)

## File Structure

```
DailyDigest/
├── main.py                          # Pipeline orchestrator
├── config/
│   ├── sources.json                 # 85+ source definitions
│   └── rotation_schedule.json       # Domain rotation by day
├── fetchers/
│   ├── twitter_fetcher.py
│   ├── rss_fetcher.py
│   ├── youtube_fetcher.py
│   ├── hackernews_fetcher.py
│   ├── gmail_fetcher.py
│   └── enrichment.py                # Newsletter link title fetching
├── processors/
│   ├── priority_scorer.py
│   ├── topic_clusterer.py
│   └── ai_summarizer.py
└── publishers/
    └── notion_publisher.py
```

## Success Criteria

- Fetches from all 5 platforms without errors
- Scores 80+ items, filters to 15 high-quality items
- No single author or platform dominates
- AI summaries are concise and actionable
- Published to Notion journal within 3 minutes
- Runs reliably on schedule (8am daily)
