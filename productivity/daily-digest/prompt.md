# DailyDigest — Workflow Prompt

## Purpose
Aggregate 85+ content sources daily, score and cluster by relevance, generate AI summaries, and log a curated 15-item reading list into the Notion "Estante" (Bookshelf) database — one entry per item — with an email and a WhatsApp nudge as secondary channels.

## Architecture

### Pipeline
```
Fetch (5 fetchers) → Score (0-100) → Diversity Caps → Domain Rotation → AI Summaries → Estante DB + Email + WhatsApp
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

## Notion Publishing — Estante (Bookshelf) database

### Output Format
Creates **one Estante entry per selected item** (top ~15). No combined page. Each entry maps to the Estante schema:

| Property | Type | Value |
|----------|------|-------|
| Title | title | Headline / key takeaway |
| Type | select | Reading · Video · Article (from source platform) |
| Format | select | X thread · Youtube video · Podcast · Article · LinkedIn post … |
| Domain | multi-select | Product · AI · Tech · Startups · Career … |
| Date | date | Today (drives the "Date = Today" reading view) |
| Link | url | Direct content URL |
| Author / Speaker | relation → Network | Linked ONLY if the author already exists in Network; publications / company posts skipped |
| Key insight | text | **Left empty** (reserved for manual promotion to Aprendizajes) |
| Rank | select | **Left empty** (reserved for manual promotion) |

Page body carries Summary / Source / "why this made the cut".

### Mapping rules
- **Type/Format** keyed off the source platform: twitter → Reading / X thread; youtube → Video / Youtube video; podcast → Video / Podcast; blog · newsletter · rss · HN → Article / Article.
- **Domain** maps the digest taxonomy → Estante options (e.g. `AI & Tech` → [AI, Tech], `PM & Growth` → [Product], `Startups & Venture` → [Startups, Entrepreneurship]).
- **Author** is best-effort: exact name lookup in the Network DB; never creates a Network row (no CRM pollution).

### Idempotency
- Queries Estante for entries already dated today and skips any item whose Link already exists.
- Combined with the cross-day `published_urls.json` tracker, running twice never double-logs.
- Rich text truncated to 2000 chars; max 100 blocks per API call.

### Secondary channels (unchanged)
After Estante is populated, the same digest is emailed (Gmail) and pushed to WhatsApp; both link back to the Estante "Date = Today" view.

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
    ├── notion_publisher.py             # One Estante entry per item
    ├── gmail_sender.py                 # Email digest
    └── whatsapp_sender.py              # WhatsApp nudge
```

## Success Criteria

- Fetches from all 5 platforms without errors
- Scores 80+ items, filters to 15 high-quality items
- No single author or platform dominates
- AI summaries are concise and actionable
- 15 entries created in the Estante DB (no duplicates) + email + WhatsApp sent, within 3 minutes
- Runs reliably on schedule (8am daily)
