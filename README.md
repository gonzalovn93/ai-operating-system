# AI Operating System

**I don't use AI as a chatbot. I use it as infrastructure.**

An operating system layer that turns natural language into structured workflows — across career, content, product, and productivity. Built on Claude Code, backed by Notion, scheduled with cron.

```
┌─────────────────────────────────────────────────────────────┐
│                    Chat Routing Layer                        │
│         Natural language → Skill dispatch (SKILL.md)        │
├──────────┬──────────┬──────────┬──────────┬─────────────────┤
│ Learning │ Content  │ Career   │    PM    │     Agents      │
│Productiv.│  Voice   │   OS     │ Toolkit  │  (High-Context) │
├──────────┼──────────┼──────────┼──────────┼─────────────────┤
│ 6 flows  │ 3 modules│ 4 flows  │38 flows  │  6 copilots     │
│ Digest   │ Ideation │ Hunt     │ PRDs     │  Career         │
│ Learning │ Posts    │ Scout    │ OKRs     │  Recruiting     │
│ Reviews  │ Retro   │ Blitz    │ Analysis │  Branding       │
│ OKRs     │          │ Memo     │ Cases    │  Positioning    │
│ Tasks    │          │          │          │  PM Copilot     │
│ Habits   │          │          │          │  Intel Agent    │
├──────────┴──────────┴──────────┴──────────┴─────────────────┤
│                     Notion Databases (9)                     │
│    Tasks · Learnings · Journal · Content · Applications     │
│           Companies · Network · Key Results · Habits        │
├─────────────────────────────────────────────────────────────┤
│                   Persistent Memory Layer                    │
│       MEMORY.md · LEARNINGS.md · execution_log.json         │
└─────────────────────────────────────────────────────────────┘
```

**48+ workflows · 9 Notion databases · 5 domains · 6 agents · 3 daily-use automations**

---

## Why This Exists

Most AI usage is stateless — every conversation starts from zero. This system has persistent memory, structured dispatch, and automated pipelines.

You describe *how you work* in plain text files. Your computer works that way from then on.

The result: an operating system layer on top of tools you already have (Notion, Google Calendar, LinkedIn) — not a new app to learn.

---

## Architecture

Five domains, each with its own workflows, databases, and instruction files. A chat routing layer connects them so everything runs from a single Claude Code session.

> [Full architecture deep dive →](./ARCHITECTURE.md)

---

## What's Inside

| Domain | What it covers | Key workflows | Count |
|--------|---------------|---------------|-------|
| [**Career**](./career) | Job scanning, networking, applications, pipeline strategy | JobHunter, NetworkingScout, ApplicationBlitz | 4 |
| [**Content**](./content) | Voice-driven posts, carousels, ideation, performance retro | ContentPackageGenerator, WeeklyIdeation | 3 |
| [**Product**](./product) | PRDs, OKRs, case studies, competitive analysis, board decks | 38 PM workflows via PMToolkit | 38 |
| [**Productivity**](./productivity) | Daily digests, learning capture, OKR tracking, weekly reviews | DailyDigest, WeeklyReview, HabitTracking | 6 |
| [**Agents**](./agents) | High-context copilots with persistent memory and judgment | Career Strategy, PM Copilot, Intel Agent | 6 |

### Agents

These aren't generic prompts — they're Claude Projects with persistent identity, operating style, and constraints. They behave like senior teammates who have context on everything.

| Agent | What It Does |
|-------|-------------|
| [Career Strategy](./agents/career-strategy/) | Parallel process management, offer evaluation, decision framing |
| [Recruiting Strategist](./agents/recruiting-strategist/) | Company targeting, pipeline sequencing, risk-balanced strategy |
| [Personal Branding](./agents/personal-branding/) | Website, LinkedIn, and content as a coordinated system |
| [Positioning Strategist](./agents/positioning-strategist/) | Interview narratives, company-specific story tailoring |
| [PM Copilot](./agents/pm-copilot/) | Product thinking partner — PRD review, tradeoff analysis, strategy critique |
| [Perplexity Intel Agent](./agents/perplexity-intel-agent/) | Weekly competitive intelligence — Google AI, OpenAI, Microsoft, Anthropic |

---

## How I Actually Use This

The three automations I run consistently:

- **Every morning:** DailyDigest aggregates 85+ sources (Twitter, RSS, YouTube, Hacker News, Gmail newsletters), scores and clusters them by relevance, generates AI summaries, and appends a curated digest to my Notion journal. I scan it over coffee instead of scrolling feeds.

- **Every week:** `"Find PM jobs"` — JobHunter scrapes 18 target companies across 6 ATS platforms, deduplicates against existing entries, scores for fit, and populates my Applications database in Notion.

- **On demand:** `"Create the post for [title]"` — ContentPackageGenerator takes a content idea from my Notion backlog and produces a LinkedIn post, 7-slide editorial carousel with composited images, and a 45-second video script — all in my voice, for ~$0.87 per package.

The rest activates when needed:

- `"Find people at Anthropic"` — NetworkingScout scores contacts by Berkeley affinity and suggests outreach.
- `"Generate materials for [job]"` — ApplicationBlitz creates a tailored resume + cover letter.
- `"Write a PRD for X"` — PMToolkit generates any of 38 PM documents and saves to Google Drive.
- `"Do my weekly review"` — WeeklyReview pulls OKR progress from Notion, checks calendar hours against targets, identifies blockers, and publishes the analysis.

I don't open 5 different tools. I open Claude Code and speak in commands.

---

## Design Principles

1. **Skills have roles, not just prompts.** Each agent has a defined identity, operating style, failure modes, and constraints — not a generic "you are a helpful assistant."

2. **Context is architecture.** What an agent knows permanently (via `MEMORY.md`) vs. per-session changes how it reasons. Designing this boundary is a product decision.

3. **Systems over one-shots.** Every workflow runs repeatedly and improves over time through accumulated `LEARNINGS.md` files.

4. **Opinionated by default.** Agents challenge weak thinking rather than just execute. I want a collaborator, not a typist.

5. **Learnings are infrastructure.** Every skill logs patterns from execution — API quirks, prompt improvements, edge cases. The system gets smarter as it operates.

6. **Chat routing is UX.** Natural language maps to structured dispatch via `SKILL.md` files. This is the difference between using AI and operating an AI system.

---

## Technical Stack

| Component | Technology |
|-----------|-----------|
| AI Engine | Claude API (Anthropic) |
| Image Generation | Gemini |
| Runtime | Claude Code + Python 3.11+ |
| Database | Notion API (raw httpx — the SDK is incomplete) |
| Document Output | Google Drive (OAuth), reportlab (PDF) |
| Scheduling | System scheduler (cron / Windows Task Scheduler) |
| Content Tracking | LinkedIn CSV export + fuzzy matching import |

---

## Technical Learnings

Real patterns discovered through building and operating the system:

- **Notion SDK limitations:** The `notion-client` Python package lacks `databases.query()`. All skills use raw `httpx` requests instead. If you're building Notion integrations in Python, skip the SDK.
- **Notion property naming:** Title properties aren't always `Name`. Always verify the actual property name in the schema — this silently breaks queries.
- **Notion relation filters:** `Trimestre` (quarter) is a relation property, not a select. Filtering requires `relation: {contains: page_id}`, not `select: {equals: "Q2"}`.
- **Google Calendar re-auth:** OAuth tokens expire. The CalendarClient needs to handle token refresh and re-auth gracefully — delete the token file and re-run to trigger browser OAuth.
- **Scheduled tasks on laptops:** Windows Task Scheduler requires `DisallowStartIfOnBatteries=false` and `StartWhenAvailable=true`, or tasks silently fail on battery power.
- **URL-encoded OAuth tokens:** Some flows return encoded tokens. Always decode with `urllib.parse.unquote()`.
- **Calendar as source of truth:** Color-coded calendar events map to OKR categories. Weekly reviews pull actual hours from Google Calendar and compare against initiative targets — the calendar is the accountability layer.

---

## Setup

```bash
# Clone the repo
git clone https://github.com/gonzalovn93/ai-operating-system.git

# Install dependencies
pip install -r requirements.txt

# Configure environment variables (see .env.example)
cp .env.example .env
```

**Required API keys:** `ANTHROPIC_API_KEY`, `NOTION_API_KEY`, Google OAuth credentials (Calendar, Drive, Sheets).

**Optional:** `TWITTER_BEARER_TOKEN` (DailyDigest), `GEMINI_API_KEY` (ContentVoice).

> **Note:** This repo contains the system architecture, skill definitions, and workflow documentation. Some workflows reference private Notion databases and API configurations — you'll need to set up your own. The architecture and patterns are fully portable.

---

## About

I'm **Gonzalo Vasquez** — Product Manager, founder, and builder. 6+ years of PM experience across consumer tech, ads, and fintech (Rappi, Intuit). Currently finishing my MBA at Berkeley Haas and building [GOPLAI](https://letsgoplai.com), an AI-powered sports-tech platform.

This system is how I operate.

[Website](https://gonzalovasquez.com) · [LinkedIn](https://linkedin.com/in/gonzalovasquezd)

---

## License

MIT
