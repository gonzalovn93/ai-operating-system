# DailyDigest

**Type:** Scheduled Python Pipeline  
**Skill Domain:** LearningProductivity  
**Schedule:** Daily, 8:00 AM  

## What It Does

A fully automated information pipeline that fetches content from 80+ sources across 10 topic domains, scores each item for relevance, applies diversity caps, generates AI summaries, and publishes a curated daily briefing to my Notion journal.

This is the most technically complex component in the system.

## How It Works

```
Sources (80+)  →  Fetchers  →  Scoring Engine  →  Diversity Caps  →  AI Summaries  →  Notion
   RSS              ↗             (0-100)          (per-domain         (Claude)         Journal
   Twitter/X     ↗                                  max to prevent                      Page
   YouTube     ↗                                    single-source
   Hacker News ↗                                    dominance)
   Gmail      ↗
```

1. **Fetch:** 5 specialized fetchers pull content from different source types
2. **Score:** Each item receives a relevance score (0–100) based on topic relevance, source quality, and recency
3. **Diversify:** Domain rotation across 10 topic areas ensures breadth — no single topic dominates
4. **Summarize:** Top items get AI-generated summaries via Claude API
5. **Publish:** A formatted daily journal page is created in Notion with categorized summaries

## Design Decisions

- **Why 5 separate fetchers?** Each source type has different APIs, rate limits, and content structures. Twitter needs bearer token auth. RSS needs XML parsing. YouTube needs the Data API. Separating them makes each one independently testable and replaceable.
- **Why scoring + diversity caps?** Without these, the digest would be dominated by whatever topic had the most content that day. Scoring ensures quality; caps ensure breadth. This mirrors how editorial teams curate — you don't just publish the top 10 by engagement.
- **Why domain rotation?** 10 topic areas rotate emphasis across days. Monday might lean heavier on AI research; Wednesday on product strategy. This prevents filter bubble effects and ensures coverage over a week.
- **Why Notion journal?** It appends to my daily journal page — the same page I use for reflections and notes. Information intake and personal reflection live in the same space.

## Architecture

```
DailyDigest/
├── main.py             # Pipeline orchestrator
├── config/
│   ├── sources.yaml    # Source definitions (URL, type, domain, priority)
│   └── credentials.json
├── fetchers/
│   ├── rss_fetcher.py
│   ├── twitter_fetcher.py
│   ├── youtube_fetcher.py
│   ├── hackernews_fetcher.py
│   └── gmail_fetcher.py
├── processors/
│   ├── scorer.py       # Relevance scoring (0-100)
│   ├── deduplicator.py
│   └── summarizer.py   # Claude API summarization
└── publishers/
    └── notion_publisher.py
```

## Prompt File

→ [`prompt.md`](./prompt.md)
