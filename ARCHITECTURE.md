# System Architecture

## Overview

The AI Operating System is structured as a 4-layer system, inspired by how product organizations separate strategy from execution. Each layer serves a different type of task, and choosing the right layer for a given problem is itself a design decision.

## The 4-Layer Model

```
┌─────────────────────────────────────────────────────┐
│  Layer 1: High-Context Agents (Claude Projects)     │
│  Strategy, judgment, iteration, critique             │
│  ↕ Persistent memory across sessions                │
├─────────────────────────────────────────────────────┤
│  Layer 2: Desktop Context Assistants                │
│  Real-time, interrupt-driven, screen-aware          │
│  ↕ Session-only context                             │
├─────────────────────────────────────────────────────┤
│  Layer 3: Document Assistants                       │
│  Fixed-corpus synthesis, hallucination-free          │
│  ↕ Document-bound context                           │
├─────────────────────────────────────────────────────┤
│  Layer 4: Static Prompts & Templates                │
│  Repeatable, generative, no memory needed           │
│  ↕ Stateless                                        │
└─────────────────────────────────────────────────────┘
```

### Layer 1 — High-Context Agents

**When to use:** Tasks requiring memory of past work, iterative reasoning, judgment, and critique.

These agents live as Claude Projects with persistent instructions. They know my background, goals, constraints, and operating style. They behave like senior PM teammates who have context on everything.

| Agent | Domain | Key Capability |
|-------|--------|---------------|
| Career Strategy Copilot | Career decisions | Parallel process management, negotiation, tradeoff analysis |
| Recruiting Strategist | Job pipeline | Company evaluation, sequencing, risk balancing |
| Personal Branding | Public presence | Website, LinkedIn, content as a coordinated system |
| Positioning Strategist | Narrative | Company-specific interview prep, story tailoring |
| PM Copilot | Product work | PRD review, strategy critique, tradeoff analysis |

**Design decision:** Each agent has an explicit *identity* (how it thinks), *operating style* (how it communicates), and *constraints* (what it should NOT do). This produces dramatically better output than a generic "you are a helpful assistant" prompt.

### Layer 2 — Desktop Context Assistants

**When to use:** Real-time, interrupt-driven tasks during meetings or active work.

These are lightweight, fast, and concise. They see what's on screen and respond in seconds.

Examples:
- "What should I ask next?" (during a networking call)
- "Rewrite this Slack message to sound more senior"
- "Interpret this dashboard — what's the story?"

**Design decision:** These don't need memory. They need speed and contextual awareness. Keeping them separate from Layer 1 agents prevents context pollution.

### Layer 3 — Document Assistants

**When to use:** Tasks involving a fixed corpus — transcripts, PRDs, research docs — where hallucination is unacceptable.

These assistants are grounded in specific documents and will not invent information outside them.

Examples:
- Synthesize 5 interview transcripts into themes
- Extract key decisions from a 30-page PRD
- Cross-reference two competitive analysis docs

**Design decision:** Explicitly restricting the context window to provided documents eliminates the most common failure mode of AI assistants — confidently stating things that aren't in the source material.

### Layer 4 — Static Prompts & Templates

**When to use:** Repeatable, generative tasks that don't require memory or judgment.

These are clean, structured, copy-paste-ready. They produce consistent output every time.

Examples:
- Write a PRD from a brief
- Generate OKRs for a quarter
- Draft a "Why this company?" answer
- Create user stories from requirements

**Design decision:** Not everything needs to be an agent. If the task is repeatable and doesn't benefit from memory, a well-crafted prompt template is simpler, faster, and more reliable.

---

## Choosing the Right Layer

The decision rule is simple:

```
Does this task need memory, judgment, or iteration?
├── Yes → Layer 1 (Agent)
│
├── No → Does it need real-time screen context?
│   ├── Yes → Layer 2 (Desktop)
│   └── No → Is it grounded in specific documents?
│       ├── Yes → Layer 3 (Document)
│       └── No → Layer 4 (Static Prompt)
```

**Common mistake:** Over-agentifying. Most people default to building agents when a static prompt would work better. Agents add complexity (memory management, identity drift, context window limits). Only use them when the task genuinely benefits from persistence and judgment.

---

## Skill Domain Architecture

Each of the 5 skill domains follows a consistent internal structure:

```
skill-name/
├── SKILL.md              # Chat routing — maps triggers to workflows
├── Workflows/            # Workflow definitions (markdown or Python)
├── Tools/                # Python utilities (API clients, helpers)
├── config/               # Configuration files
├── LEARNINGS.md          # Accumulated patterns from execution
└── execution_log.json    # Structured execution history
```

### SKILL.md — The Router

Every skill has a `SKILL.md` file that Claude Code reads at session start. It defines:
- What natural language triggers map to which workflow
- What context the skill needs to operate
- What databases it reads from and writes to
- What the expected output format is

This is the UX layer of the system. It's what makes Claude Code feel like a specialized tool rather than a general chatbot.

### LEARNINGS.md — The Memory

Each skill accumulates a `LEARNINGS.md` file — real patterns discovered through execution:
- API quirks and workarounds
- Prompt patterns that produce better output
- Edge cases and failure modes
- Performance benchmarks

This file is read by the skill on every execution, so the system genuinely improves over time.

### MEMORY.md — The Global Context

A single `MEMORY.md` file is auto-loaded into every Claude Code session. It contains:
- Master index of all skills and their locations
- Database IDs and property mappings
- Cross-skill conventions (naming, error handling, output formats)
- Global patterns that apply everywhere

This is the closest thing to institutional knowledge in a prompt-based system.

---

## Data Flow

```
User Command (natural language)
        │
        ▼
   SKILL.md Router
        │
        ├──→ Python Workflow (automated)
        │         │
        │         ├──→ External APIs (job boards, LinkedIn, RSS)
        │         ├──→ Claude API (analysis, generation)
        │         ├──→ Notion API (read/write databases)
        │         └──→ Google APIs (Drive, Calendar, Sheets)
        │
        └──→ Agent/Prompt (conversational)
                  │
                  ├──→ Claude API (reasoning, critique)
                  └──→ Notion API (context retrieval)
        │
        ▼
   Output (Notion page, PDF, Google Doc, terminal)
        │
        ▼
   LEARNINGS.md (patterns captured for next run)
```

---

## Integration Map

```
                    ┌──────────────┐
                    │  Claude Code │
                    │  (Runtime)   │
                    └──────┬───────┘
                           │
              ┌────────────┼────────────┐
              │            │            │
     ┌────────▼──┐  ┌─────▼─────┐  ┌──▼────────┐
     │  Claude   │  │  Notion   │  │  Google   │
     │  API      │  │  API      │  │  APIs     │
     │           │  │           │  │           │
     │ • Text    │  │ • 9 DBs   │  │ • Drive   │
     │ • Analysis│  │ • Pages   │  │ • Calendar│
     │ • Scoring │  │ • Journal │  │ • Sheets  │
     └───────────┘  └───────────┘  └───────────┘
                           │
                    ┌──────▼───────┐
                    │   Gemini     │
                    │  (Images)    │
                    └──────────────┘
```

---

## Why This Architecture?

### Why not just use ChatGPT / Claude chat?

Chat interfaces are stateless. Every conversation starts from zero. This system has persistent memory (`MEMORY.md`, `LEARNINGS.md`), structured dispatch (SKILL.md routing), and automated pipelines (scheduled Python workflows). The difference is the same as between using Google Sheets manually vs. building a data pipeline.

### Why Claude Code specifically?

Claude Code operates in a terminal environment with file system access, which means it can:
- Read and write local files (configs, outputs, logs)
- Execute Python scripts
- Interact with APIs
- Maintain persistent instruction files that load automatically

This makes it uniquely suited for building a system that bridges conversational AI and automated infrastructure.

### Why Notion as the database?

Notion's API is flexible enough to serve as a lightweight database for structured data (tasks, contacts, applications, content) while also being a UI I actually use daily. The same data that powers automated workflows is visible in my Notion workspace — no separate dashboard needed.

### Why separate skills instead of one mega-prompt?

Context window management. A single prompt with all 43+ workflows would be massive, slow, and fragile. Separate skills with their own SKILL.md routers mean Claude Code only loads the context relevant to the current task. This is the same principle behind microservices: bounded contexts, clear interfaces, independent scaling.
