# LearningCapture

**Type:** Conversational Workflow (Claude Code)
**Skill Domain:** LearningProductivity
**Trigger:** Manual — "I learned X from Y"

## What It Does

Captures insights from any learning source — events, conversations, articles, videos, podcasts, observations — and stores them in the Notion Aprendizajes database with proper categorization, key insights, and application notes tied to current goals.

This is the personal knowledge base builder. Every insight gets tagged, scored, and connected to active projects.

## How It Works

```
User shares learning  →  Extract metadata  →  Categorize  →  Structure insights  →  Notion
   "I learned X"           Type, Format,       Domain,          Key takeaways,       Aprendizajes
   "I attended Y"          Source, Date        Tags             Application notes     Database
```

1. **Extract:** Parse the learning source — what was learned, from whom, what type of content
2. **Categorize:** Assign Type (Event, Article, Conversation, etc.), Format (Conference, Newsletter, 1-on-1, etc.), and Domain (Product, AI, Career, etc.)
3. **Structure:** Extract 2-5 specific, actionable insights — not summaries, but principles
4. **Apply:** Write application notes specific to current context (projects, career, personal)
5. **Store:** Create a rich Notion page in the Aprendizajes database with all metadata

## Design Decisions

- **Why structured extraction?** Raw notes decay. Categorized, tagged insights are searchable and resurfaceable. The metadata makes it possible to query "show me all Product learnings from conversations" months later.
- **Why application notes?** A learning without application is trivia. Forcing a "how does this apply to my work?" step makes every entry actionable.
- **Why multiple domains?** Cross-domain insights (e.g., a leadership lesson that applies to product strategy) are the most valuable. Multi-select domains capture this.

## Architecture

```
LearningCapture (Conversational)
├── Extraction         # Parse user input for metadata
├── Categorization     # Type, Format, Domain assignment
├── Insight Structuring # Key takeaways + application
└── Notion Integration  # Create page via API
    └── notion_client.py
```

## Prompt File

> [`prompt.md`](./prompt.md)
