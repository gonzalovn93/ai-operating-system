# AI Operating System

An AI-native operating system for product management, career, content, and productivity — built on Claude Code.

## Domains

| Domain | What it covers | Workflows |
|--------|---------------|-----------|
| [**career**](./career) | Job scanning, networking, applications, weekly strategy | 4 |
| [**content**](./content) | Ideation, drafting, carousels, metrics retros | 3 |
| [**product**](./product) | PRD drafts, OKRs, case studies | 3 |
| [**productivity**](./productivity) | Daily digests, learning capture, OKR planning, weekly reviews, habit tracking, task automation | 6 |
| [**agents**](./agents) | High-context copilots for strategy, positioning, branding | 5 |

**48+ workflows · 9 Notion databases · 5 domains**

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

| Workflow | Trigger | What It Produces |
|----------|---------|-----------------|
| [JobHunter](./career/job-hunter/) | `python main.py hunt` | PM roles from target companies → Notion |
| [NetworkingScout](./career/networking-scout/) | `python main.py scout` | Scored networking contacts → Notion |
| [ApplicationBlitz](./career/application-blitz/) | `python main.py blitz` | Tailored resume PDF + cover letter |
| [WeeklyMemo](./career/weekly-memo/) | `python main.py memo` | Strategic pipeline report |

### Content Workflows

| Workflow | Trigger | What It Produces |
|----------|---------|-----------------|
| [ContentPackageGenerator](./content/content-package-generator/) | On-demand | LinkedIn post + 7-slide carousel + video script |
| [WeeklyIdeation](./content/weekly-ideation/) | On-demand | 12–20 content ideas from curated sources |
| [ContentRetro](./content/content-retro/) | Weekly | Performance analysis of published content |

### Productivity Workflows

| Workflow | Trigger | What It Produces |
|----------|---------|-----------------|
| [DailyDigest](./productivity/daily-digest/) | Scheduled, daily 8am | AI-summarized news from 85+ sources → Notion journal |
| [LearningCapture](./productivity/learning-capture/) | "I learned X from Y" | Structured insights with metadata → Notion Aprendizajes |
| [WeeklyReview](./productivity/weekly-review/) | "Do my weekly review" | OKR progress, calendar reality check, blocker analysis → Notion journal |
| [QuarterlyOKRDesign](./productivity/quarterly-okr-design/) | "Plan my Q2 OKRs" | Identity-aligned OKRs with capacity validation → Notion |
| [TaskManagement](./productivity/task-management/) | "Schedule my week" | Energy-based time blocks → Google Calendar |
| [HabitTracking](./productivity/habit-tracking/) | "Update my initiatives" | Calendar sync + manual logging → Notion initiative progress |

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
│   ├── job-hunter/
│   ├── networking-scout/
│   ├── application-blitz/
│   └── weekly-memo/
│
├── content/
│   ├── README.md
│   ├── content-package-generator/
│   ├── weekly-ideation/
│   └── content-retro/
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
│   └── pm-copilot/
│
└── images/
    └── architecture.mermaid
```

---

## How I Actually Use This

A typical week looks like:

- **Every morning:** DailyDigest has already run at 8am — I scan the Notion journal page over coffee to see what's relevant across AI, product, startups, and tech
- **Monday:** `"Do my weekly review"` → WeeklyReview pulls OKR progress from Notion, checks actual hours from Google Calendar, identifies blockers by severity, and generates a full analysis
- **Monday:** `"Find PM jobs"` → JobHunter scrapes target companies, scores roles, and populates my Applications database
- **Tuesday:** `"I learned X from the Lenny podcast"` → LearningCapture extracts insights, categorizes them, and stores them in the Aprendizajes database with application notes
- **Wednesday:** `"Schedule my week"` → TaskManagement creates energy-optimized time blocks in Google Calendar — deep work at 9am, gym at 6pm, no meetings before 11
- **Thursday:** `"Write a PRD for X"` → PMToolkit generates a structured PRD from my input and pushes it to Google Drive
- **End of quarter:** `"Plan my Q2 OKRs"` → QuarterlyOKRDesign reviews last quarter, validates identity alignment, designs OKRs with capacity math, and pushes to Notion
- **Ongoing:** `"Update my initiatives"` → HabitTracking syncs Google Calendar events to Notion initiative progress, showing before/after deltas
- **Ongoing:** ContentVoice generates post ideas, drafts, carousels, and tracks what performs — all feeding back into the next cycle

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
