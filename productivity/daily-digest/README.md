# DailyDigest

**An automated information pipeline that reads 85+ sources, scores every item for relevance, and delivers a 15-item curated briefing to my Notion journal — every morning at 8am.**

---

## The Problem

Staying current across AI, product strategy, startups, and sports-tech means monitoring dozens of newsletters, RSS feeds, Twitter threads, YouTube channels, and Hacker News — every day. That's 100+ items competing for attention before the workday even starts.

The options are: spend 45 minutes scanning everything manually, miss things, or build a system that does it for you.

I built the system.

## How It Works

```
  85+ Sources          5 Fetchers         Scoring Engine        Output
 ─────────────      ──────────────      ────────────────     ──────────

  Twitter/X (15)  ─→  Twitter API  ─┐
  RSS feeds (55+) ─→  feedparser   ─┤
  YouTube (12)    ─→  YT Data API  ─┼→  Score (0-100)  →  Diversity  →  AI Summary  →  Notion
  Hacker News     ─→  HN API      ─┤   per item          Caps          (Claude)       Journal
  Gmail (curated) ─→  Gmail API   ─┘

                  100+ items fetched    →    scored    →   15 selected    →   summarized   →   published
```

The pipeline runs in **under 3 minutes**. By the time I open Notion with coffee, the briefing is already there.

## Scoring: How 100+ Items Become 15

Every item gets a relevance score from 0 to 100 based on four factors:

| Factor | Points | What It Rewards |
|--------|--------|----------------|
| Source tier | 10–40 | Tier 1 sources (Stratechery, Lenny's Newsletter) score highest |
| Domain weight | 5–28 | Topics "in focus" that day get boosted (rotates daily) |
| Recency | 0–15 | Published in last few hours > published yesterday |
| Engagement | 0–15 | HN points, tweet engagement — platform-adjusted and capped |

Then three diversity filters ensure the final 15 aren't all from the same place:

1. **Author cap** — max 1 item per author (no Paul Graham x5)
2. **Platform cap** — max 5 from any single platform (no Twitter domination)
3. **Domain rotation** — 4 of 10 topic domains are "in focus" each day, rotating across the week

This mirrors how editorial teams curate — you don't just rank by engagement and call it a day.

## 10 Topic Domains

Content rotates across these domains so the digest has breadth over any given week:

| Domain | Example Sources |
|--------|----------------|
| AI Strategy | Ethan Mollick, Anthropic Blog, Karpathy, SemiAnalysis |
| PM & Growth | Lenny Rachitsky, Shreyas Doshi, SVPG, Product Compass |
| Startups & Venture | Not Boring, Paul Graham, Acquired, Y Combinator |
| Psychology & Decisions | Farnam Street, Astral Codex Ten, Annie Duke |
| Life Design | Cal Newport, Derek Sivers, Sahil Bloom |
| Sports-Tech | Front Office Sports, StatsBomb, SportTechie |
| Culture & Film | The Marginalian, Critical Drinker, Every Frame a Painting |
| Fintech | Matt Levine, Fintech Takes, Net Interest |
| Tech Platforms | Platformer, Notion Blog, Nvidia Blog |
| Tech Industry | OpenAI Blog, Google AI Blog, Microsoft AI Blog |

Monday might lean AI + PM. Wednesday might lean Startups + Psychology. Over a week, everything gets covered.

## AI Summaries

Each of the 15 selected items gets a Claude-generated summary in a consistent format:

> **What happened** — one sentence on the core content.
> **Why it matters** — relevance to a PM / builder.
> **Takeaway** — one actionable question or insight.

This turns "I should read this article later" into "I already know the key point and whether it's worth a deeper dive."

## Newsletter Link Extraction

Curated newsletters like Techpresso bundle 10–20 links into a single email. Instead of treating the whole email as one item, the Gmail fetcher:

1. Extracts individual article links from the email body
2. Filters out tracking, unsubscribe, and image URLs
3. Fetches actual article titles via HTML meta tags
4. Scores each link independently

One email becomes 5 individually scored items competing on merit.

## Cross-Day Deduplication

Sources use a 48-hour lookback window to avoid missing content. Without dedup, the same article would appear two days in a row. The pipeline tracks every published URL and removes items that already appeared in a previous day's digest. The tracking file auto-prunes after 7 days.

## Architecture

```
DailyDigest/
├── main.py                          # Pipeline orchestrator
├── config/
│   ├── sources.json                 # 85+ source definitions
│   ├── rotation_schedule.json       # Domain rotation by day of week
│   └── published_urls.json          # Cross-day dedup tracking
├── fetchers/
│   ├── twitter_fetcher.py           # Bearer token auth, 15 accounts
│   ├── rss_fetcher.py               # 55+ feeds via feedparser
│   ├── youtube_fetcher.py           # 12 channels via YT Data API
│   ├── hackernews_fetcher.py        # Top stories by score
│   ├── gmail_fetcher.py             # Newsletter link extraction
│   └── enrichment.py                # Fetch article titles for extracted links
├── processors/
│   ├── priority_scorer.py           # 0-100 scoring algorithm
│   ├── topic_clusterer.py           # Group related items
│   └── ai_summarizer.py             # Claude API batch summarization
└── publishers/
    └── notion_publisher.py          # Append to daily journal page
```

## Output: What the Notion Page Looks Like

The digest appends to my daily journal page — the same page I use for reflections and notes. Information intake and personal reflection live in the same space.

Each day's digest includes:
- **Platform mix** — how many items came from each source type
- **Domain-grouped sections** — items organized by topic with emoji prefixes
- **Priority markers** — high-scoring items (80+) flagged for attention
- **Per-item format** — title, source, score, AI summary, direct link

## Usage

```bash
python main.py                    # Full run → publish to Notion
python main.py --dry-run          # Preview in terminal without publishing
python main.py --date 2026-03-08  # Run for a specific date
```

Scheduled daily at 8:00 AM via Windows Task Scheduler with `StartWhenAvailable=true` so it catches up if the machine was asleep.

## Design Decisions

**Why 5 separate fetchers?** Each source type has different APIs, auth methods, rate limits, and content structures. Separating them makes each independently testable and replaceable — I can swap the Twitter fetcher without touching RSS.

**Why scoring + diversity caps instead of just "top 15 by engagement"?** Without caps, the digest would be dominated by whatever had the most content that day. Scoring ensures quality; caps ensure breadth. Editorial curation requires both.

**Why domain rotation?** Prevents filter bubble effects. If I only boosted AI every day, I'd never see the Fintech or Sports-Tech content that often sparks the most unexpected connections.

**Why Notion journal?** The digest isn't a standalone feed — it's part of my daily reflection page. Reading what's happening in the world and writing about what I'm doing happen in the same context.

## Stack

Python 3.11+ · Claude API (summaries) · Notion API (publishing) · Twitter API v2 · YouTube Data API · Gmail OAuth · feedparser · Hacker News Firebase API

---

> Part of [AI Operating System](../../README.md) — an AI-native operating system for product management, career, content, and productivity.
