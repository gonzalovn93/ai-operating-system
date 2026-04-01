# AI Operating System

An AI-native operating system for product management, career, content, and productivity — built on Claude Code.

## Domains

| Domain | What it covers | Active Workflows |
|--------|---------------|-----------------|
| [**career**](./career) | Job scanning, networking, applications | 3 |
| [**content**](./content) | Voice-driven post + carousel generation | 1 |
| [**product**](./product) | PRD drafts, OKRs, case studies (38 via PM Toolkit) | 38 |
| [**productivity**](./productivity) | Daily digests, learning capture, OKR planning, weekly reviews, habit tracking, task automation | 6 |
| [**agents**](./agents) | High-context copilots for strategy, positioning, branding + production agents | 6 |

**48+ workflows · 9 Notion databases · 5 domains · 3 daily-use automations**

---

## Why This Exists

Most people use AI as a chatbot. I use it as infrastructure.

As a Product Manager recruiting for senior roles at top-tier tech companies, I needed a system that could:

- Hold context across weeks, not just single conversations
- Separate strategic thinking from execution tasks
- Automate the repetitive parts of job searching, networking, and content creation
- Scale my decision-making without losing quality

This is that system. It's built on [Claude Code](https://docs.anthropic.com/en/docs/claude-code), runs on Python, writes to Notion, and operates through natural language commands.

It's not a collection of prompts. It's an operating system.

---

## Architecture

The system is organized into **5 domains**, each with its own workflows, databases, and instruction files. A chat routing layer connects them so I can operate everything from a single Claude Code session.

```
┌─────────────────────────────────────────────────────────────┐
│                    Chat Routing Layer                        │
│         Natural language → Skill dispatch (SKILL.md)        │
├──────────┬──────────┬──────────┬──────────┬─────────────────┤
│ Learning │ Content  │ Career   │    PM    │   Job Search    │
│Productiv.│  Voice   │   OS     │ Toolkit  │     Agent       │
│          │          │          │          │   (Portable)    │
├──────────┼──────────┼──────────┼──────────┼─────────────────┤
│ 6 flows  │ 8 modules│ 4 flows  │38 flows  │  5 components   │
│ Digest   │ Ideation │ Hunt     │ PRDs     │  Scoring        │
│ Learning │ Posts    │ Scout    │ OKRs     │  Discovery      │
│ Reviews  │ Carousels│ Blitz    │ Analysis │  Outreach       │
│ OKRs     │ Metrics  │ Memo     │ Cases    │  Tracking       │
│ Tasks    │          │          │          │                 │
│ Habits   │          │          │          │                 │
├──────────┴──────────┴──────────┴──────────┴─────────────────┤
│                     Notion Databases (9)                     │
│    Tasks · Learnings · Journal · Content · Applications     │
│           Companies · Network · Key Results · Habits        │
├─────────────────────────────────────────────────────────────┤
│                   Persistent Memory Layer                    │
│       MEMORY.md · LEARNINGS.md · execution_log.json         │
└─────────────────────────────────────────────────────────────┘
```

> [Full architecture breakdown](./ARCHITECTURE.md)

---

## What's Inside

### Agents (Claude Projects)

High-context agents for tasks requiring memory, judgment, and iteration:

| Agent | What It Does |
|-------|-------------|
| [Career Strategy](./agents/career-strategy/) | Parallel process management, offer evaluation, decision framing |
| [Recruiting Strategist](./agents/recruiting-strategist/) | Company targeting, pipeline sequencing, risk-balanced strategy |
| [Personal Branding](./agents/personal-branding/) | Website, LinkedIn, and content strategy as a coordinated system |
| [Positioning Strategist](./agents/positioning-strategist/) | Interview narratives, company-specific story tailoring |
| [PM Copilot](./agents/pm-copilot/) | Product thinking partner — PRD review, tradeoff analysis, strategy critique |

### Career Workflows

| Workflow | Trigger | What It Produces | Status |
|----------|---------|-----------------|--------|
| [JobHunter](./career/job-hunter/) | `python main.py hunt` | PM roles from 18 target companies → Notion | **Active** (weekly) |
| [NetworkingScout](./career/networking-scout/) | `python main.py scout` | Scored networking contacts → Notion | Available |
| [ApplicationBlitz](./career/application-blitz/) | `python main.py blitz` | Tailored resume PDF + cover letter | Available |

### Content Workflows

| Workflow | Trigger | What It Produces | Status |
|----------|---------|-----------------|--------|
| [ContentPackageGenerator](./content/content-package-generator/) | On-demand | LinkedIn post + 7-slide carousel + video script | **Active** |

### Productivity Workflows

| Workflow | Trigger | What It Produces | Status |
|----------|---------|-----------------|--------|
| [DailyDigest](./productivity/daily-digest/) | Daily | AI-summarized news from 85+ sources → Notion journal | **Active** (daily) |
| [LearningCapture](./productivity/learning-capture/) | "I learned X from Y" | Structured insights with metadata → Notion Aprendizajes | Available |
| [WeeklyReview](./productivity/weekly-review/) | "Do my weekly review" | OKR progress, calendar reality check, blocker analysis → Notion journal | Available |
| [QuarterlyOKRDesign](./productivity/quarterly-okr-design/) | "Plan my Q2 OKRs" | Identity-aligned OKRs with capacity validation → Notion | Available |
| [TaskManagement](./productivity/task-management/) | "Schedule my week" | Energy-based time blocks → Google Calendar | Available |
| [HabitTracking](./productivity/habit-tracking/) | "Update my initiatives" | Calendar sync + manual logging → Notion initiative progress | Available |

### Product Templates

| Template | Use Case |
|----------|----------|
| [PRD Template](./product/prd-template/) | Product Requirements Document |
| [OKR Template](./product/okr-template/) | Quarterly Objectives & Key Results |
| [Case Study Template](./product/case-study-template/) | Portfolio-ready project write-up |

---

## Folder Structure

```
ai-operating-system/
├── README.md
├── ARCHITECTURE.md
├── LICENSE
├── .env.example
├── .gitignore
│
├── career/
│   ├── README.md
│   ├── job-hunter/            # Active — weekly scans of 18 companies
│   ├── networking-scout/      # Available
│   └── application-blitz/     # Available
│
├── content/
│   ├── README.md
│   └── content-package-generator/  # Active — post + carousel + video script
│
├── product/
│   ├── README.md
│   ├── prd-template/
│   ├── okr-template/
│   └── case-study-template/
│
├── productivity/
│   ├── README.md
│   ├── daily-digest/
│   ├── learning-capture/
│   ├── weekly-review/
│   ├── quarterly-okr-design/
│   ├── task-management/
│   └── habit-tracking/
│
├── agents/
│   ├── career-strategy/
│   ├── recruiting-strategist/
│   ├── personal-branding/
│   ├── positioning-strategist/
│   ├── pm-copilot/
│   └── perplexity-intel-agent/  # Production — weekly competitor intelligence
│
└── images/
    └── architecture.mermaid
```

---

## How I Actually Use This

The three automations I run consistently:

- **Every morning:** DailyDigest aggregates 85+ sources (Twitter, RSS, YouTube, Hacker News, Gmail newsletters), scores and clusters them by relevance, generates AI summaries, and appends a curated digest to my Notion journal. I scan it over coffee instead of scrolling feeds.
- **Every week:** `"Find PM jobs"` → JobHunter scrapes 18 target companies across 6 ATS platforms, deduplicates against existing entries, scores for fit, and populates my Applications database in Notion.
- **On demand:** `"Create the post for [title]"` → ContentPackageGenerator takes a content idea from my Notion backlog and produces a LinkedIn post, 7-slide editorial carousel with composited images, and a 45-second video script — all in my voice, for ~$0.87 per package.

The rest of the system activates when needed:

- **Career push:** `"Find people at Anthropic"` → NetworkingScout scores contacts by Berkeley affinity. `"Generate materials for [job]"` → ApplicationBlitz creates a tailored resume + cover letter via Claude.
- **Product work:** `"Write a PRD for X"` → PMToolkit generates any of 38 PM documents (PRDs, OKRs, competitive analysis, board decks) and saves to Google Drive.
- **Reflection:** `"Do my weekly review"` → WeeklyReview pulls OKR progress, checks calendar hours, identifies blockers.

I don't open 5 different tools. I open Claude Code and speak in commands.

---

## Design Principles

These emerged from building and iterating on the system over several months:

1. **Skills have roles, not just prompts.** Each agent has a defined identity, operating style, failure modes, and constraints. This produces dramatically better output than generic instructions.

2. **Context is architecture.** What an agent knows permanently (via `MEMORY.md`) vs. what it learns per-session changes how it reasons. Designing this boundary is a product decision.

3. **Systems over one-shots.** Every workflow is designed to be run repeatedly and improve over time. One-off prompts don't scale.

4. **Opinionated by default.** Agents challenge weak thinking rather than just execute instructions. This is a deliberate design choice — I want a collaborator, not a typist.

5. **Learnings are infrastructure.** Every skill accumulates a `LEARNINGS.md` file — patterns discovered through execution that improve future runs. The system gets smarter as it operates.

6. **Chat routing is UX.** The `SKILL.md` routing layer turns natural language into structured dispatch. This is the difference between "using AI" and "operating an AI system."

---

## Technical Stack

| Component | Technology |
|-----------|-----------|
| AI Engine | Claude API (Anthropic) |
| Image Generation | Gemini |
| Runtime | Claude Code + Python 3.11+ |
| Database | Notion API (via raw httpx) |
| Document Output | Google Drive (OAuth), reportlab (PDF) |
| Scheduling | System scheduler (cron / Windows Task Scheduler) |
| Content Tracking | LinkedIn CSV export + fuzzy matching import |

---

## Technical Learnings

Real patterns discovered through building and operating the system:

- **Notion SDK limitations:** The `notion-client` Python package lacks `databases.query()`. All skills use a custom wrapper with raw `httpx` instead. If you're building Notion integrations in Python, skip the SDK.
- **Notion property naming:** Title properties aren't always `Name`. Always verify the actual property name in the schema — this silently breaks queries.
- **Scheduled tasks on laptops:** Windows Task Scheduler requires `DisallowStartIfOnBatteries=false` and `StartWhenAvailable=true`, or tasks silently fail on battery power.
- **URL-encoded OAuth tokens:** Some flows return encoded tokens. Always decode with `urllib.parse.unquote()`.

---

## Setup

```bash
# Clone the repo
git clone https://github.com/gonzalovn93/ai-operating-system.git

# Install dependencies
pip install -r requirements.txt

# Configure environment variables (see .env.example)
cp .env.example .env

# Required API keys:
# - ANTHROPIC_API_KEY (Claude)
# - NOTION_API_KEY
# - Google OAuth credentials (Calendar, Drive, Sheets)
```

> **Note:** This repo contains the system architecture, skill definitions, and workflow documentation. Some workflows reference private Notion databases and API configurations that you'll need to set up for your own use.

---

## About

I'm **Gonzalo Vasquez** — Product Manager, founder, and builder. 6+ years of PM experience across consumer tech, ads, and fintech (Rappi, Intuit). Currently finishing my MBA at Berkeley Haas and building [GOPLAI](https://goplai.com), an AI-powered sports-tech platform.

This system is how I operate.

> [Website](https://gonzalovasquez.com) · [LinkedIn](https://linkedin.com/in/gonzalovasquezd)

---

## License

MIT
