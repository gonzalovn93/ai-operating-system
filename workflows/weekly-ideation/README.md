# WeeklyIdeation

**Type:** On-Demand Python Pipeline  
**Skill Domain:** ContentVoice  
**Module:** 01  

## What It Does

Generates 12–20 content ideas per week by scanning curated sources, applying 7 theme-specific prompts, and routing ideas through a source classification system. Outputs to the Notion Content database as draft entries.

## How It Works

1. **Source scanning:** Pulls recent content from configured sources (industry blogs, newsletters, trending topics)
2. **Theme routing:** Each source maps to one of 7 content themes via `source_routing.yaml`
3. **Idea generation:** Theme-specific prompts in `prompts/` generate ideas tailored to each theme
4. **Deduplication:** Checks against existing ideas in the Content database
5. **Output:** 12–20 new idea entries in Notion, each with a title, hook, theme tag, and source reference

## Design Decisions

- **Why 7 theme-specific prompts?** A single generic "generate ideas" prompt produces repetitive output. Theme-specific prompts (AI, product craft, career, leadership, etc.) produce diverse ideas that map to my content pillars.
- **Why source routing?** Not all sources are relevant to all themes. Routing ensures AI research sources feed AI-themed ideas, product blogs feed product craft ideas, etc.

## Prompt File

→ [`prompt.md`](./prompt.md)
