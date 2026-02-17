# PM Toolkit — An AI-Native Operating System for Product Management

A modular system of Claude Code skills, Python workflows, and Notion integrations I designed to run my career, recruiting, content creation, and product work as a single operating system.

**43+ workflows · 5 skill domains · 9 Notion databases · 3 scheduled automations**

---

## Why This Exists

Most people use AI as a chatbot. I use it as infrastructure.

As a Product Manager recruiting for senior roles at top-tier tech companies, I needed a system that could:

- Hold context across weeks, not just single conversations
- Separate strategic thinking from execution tasks
- Automate the repetitive parts of job searching, networking, and content creation
- Scale my decision-making without losing quality

This toolkit is that system. It's built on [Claude Code](https://docs.anthropic.com/en/docs/claude-code), runs on Python, writes to Notion, and operates through natural language commands.

It's not a collection of prompts. It's an operating system.

---

## Architecture

The system is organized into **5 skill domains**, each with its own workflows, databases, and instruction files. A chat routing layer connects them so I can operate everything from a single Claude Code session.

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
│ OKRs     │ Ideation │ Hunt     │ PRDs     │  Scoring        │
│ Reviews  │ Posts    │ Scout    │ OKRs     │  Discovery      │
│ Habits   │ Carousels│ Blitz    │ Analysis │  Outreach       │
│ Digest   │ Metrics  │ Memo     │ Cases    │  Tracking       │
├──────────┴──────────┴──────────┴──────────┴─────────────────┤
│                     Notion Databases (9)                     │
│    Tasks · Learnings · Journal · Content · Applications     │
│           Companies · Network · Key Results · Habits        │
├─────────────────────────────────────────────────────────────┤
│                   Persistent Memory Layer                    │
│       MEMORY.md · LEARNINGS.md · execution_log.json         │
└─────────────────────────────────────────────────────────────┘
```

→ [Full architecture breakdown](./ARCHITECTURE.md)

---

## What's Inside

### Skill Domains

| Domain | Purpose | Workflows | Key Tech |
|--------|---------|-----------|----------|
| [**LearningProductivity**](./workflows/daily-digest/) | OKR tracking, weekly reviews, habit tracking, automated daily information digest | 6 | Notion API, Google Calendar, RSS/Twitter/YouTube fetchers |
| [**ContentVoice**](./workflows/content-package-generator/) | End-to-end LinkedIn content pipeline — ideation to carousel generation to metrics | 8 modules | Claude API, Gemini (images), Notion, LinkedIn CSV import |
| [**CareerOS**](./workflows/job-hunter/) | Automated job discovery, alumni-scored networking, tailored resume generation, pipeline analysis | 4 | httpx, reportlab (PDF), Notion API |
| [**PMToolkit**](./agents/pm-copilot/) | 38 PM workflows — PRDs, sizing, competitive analysis, case prep, and more | 38 | Claude API, Google Drive OAuth |
| [**Job Search Agent**](./workflows/) | Portable, configurable job search — swap the profile, run for anyone | 5 components | Scoring engine, Google Sheets API |

### Agents (Claude Projects)

High-context agents for tasks requiring memory, judgment, and iteration:

| Agent | What It Does |
|-------|-------------|
| [Career Strategy](./agents/career-strategy/) | Parallel process management, offer evaluation, decision framing |
| [Recruiting Strategist](./agents/recruiting-strategist/) | Company targeting, pipeline sequencing, risk-balanced strategy |
| [Personal Branding](./agents/personal-branding/) | Website, LinkedIn, and content strategy as a coordinated system |
| [Positioning Strategist](./agents/positioning-strategist/) | Interview narratives, company-specific story tailoring |
| [PM Copilot](./agents/pm-copilot/) | Product thinking partner — PRD review, tradeoff analysis, strategy critique |

### Workflows (Automated Pipelines)

Scheduled or on-demand Python workflows:

| Workflow | Trigger | What It Produces |
|----------|---------|-----------------|
| [JobHunter](./workflows/job-hunter/) | `python main.py hunt` | PM roles from target companies → Notion |
| [NetworkingScout](./workflows/networking-scout/) | `python main.py scout` | Scored networking contacts → Notion |
| [ApplicationBlitz](./workflows/application-blitz/) | `python main.py blitz` | Tailored resume PDF + cover letter |
| [WeeklyMemo](./workflows/weekly-memo/) | `python main.py memo` | Strategic pipeline report |
| [DailyDigest](./workflows/daily-digest/) | Scheduled, daily | AI-summarized news from 80+ sources → Notion journal |
| [ContentPackageGenerator](./workflows/content-package-generator/) | On-demand | LinkedIn post + 7-slide carousel + video script |
| [WeeklyIdeation](./workflows/weekly-ideation/) | On-demand | 12–20 content ideas from curated sources |
| [ContentRetro](./workflows/content-retro/) | Weekly | Performance analysis of published content |

### Templates

Reusable, copy-paste-ready frameworks:

| Template | Use Case |
|----------|----------|
| [PRD Template](./templates/prd-template.md) | Product Requirements Document |
| [OKR Template](./templates/okr-template.md) | Quarterly Objectives & Key Results |
| [Case Study Template](./templates/case-study-template.md) | Portfolio-ready project write-up |

---

## How I Actually Use This

A typical week looks like:

- **Monday morning:** DailyDigest has already run — I scan the Notion journal page over coffee to see what's relevant in AI, product, and tech
- **Monday:** `"Find PM jobs"` → JobHunter scrapes target companies, scores roles, and populates my Applications database
- **Tuesday:** `"Find people at Notion"` → NetworkingScout identifies contacts, scores them by relevance and alumni overlap, generates outreach context
- **Wednesday:** `"Generate materials for this role"` → ApplicationBlitz analyzes the JD and produces a tailored resume + cover letter
- **Thursday:** `"Write a PRD for X"` → PMToolkit generates a structured PRD from my input and pushes it to Google Drive
- **Friday:** `"Do my weekly review"` → WeeklyReview pulls OKR progress, completed tasks, and learnings into a structured reflection
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
git clone https://github.com/gonzalovn93/pm-toolkit.git

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

I'm **Gonzalo Vásquez** — Product Manager, founder, and builder. 6+ years of PM experience across consumer tech, ads, and fintech (Rappi, Intuit). Currently finishing my MBA at Berkeley Haas and building [GOPLAI](https://goplai.com), an AI-powered sports-tech platform.

This toolkit is how I operate.

→ [Website](https://gonzalovasquez.com) · [LinkedIn](https://linkedin.com/in/gonzalovasquezd)

---

## License

MIT
