# QuarterlyOKRDesign

**Type:** Conversational Workflow (Claude Code + Notion API)
**Skill Domain:** LearningProductivity
**Trigger:** Manual — "Plan my Q[N] OKRs", end of quarter

## What It Does

Designs quarterly Objectives and Key Results aligned with identity pillars, validated against realistic capacity, and connected to long-term vision. Reviews the previous quarter, validates identity alignment, designs objectives with measurable KRs, adds milestones (hitos), and performs sanity checks before creating entries in Notion.

## How It Works

```
Review last Q  →  Identity check  →  Pillar allocation  →  Design OKRs  →  Sanity check  →  Notion
  What worked?     Does this align    Time distribution      Objectives +     Capacity,        OKR
  What didn't?     with who I am?     across pillars         Key Results      dependencies     entries
```

1. **Review:** Assess previous quarter — what worked, what didn't, key learnings
2. **Identity:** Validate that proposed OKRs reinforce core identity (founder, product leader, learner)
3. **Allocate:** Distribute available hours across pillars based on priorities
4. **Design:** Create 1 Objective per pillar with 2-4 measurable Key Results each
5. **Milestones:** Add hitos (checkpoints) for mid-quarter tracking
6. **Sanity check:** Verify capacity, dependencies, risks, and optionality
7. **Create:** Push OKR entries to Notion database

## Design Decisions

- **Why identity-first?** OKRs that conflict with identity get abandoned. Checking alignment upfront prevents wasted quarters.
- **Why capacity-realistic?** Ambitious goals fail when they ignore actual available hours. Explicit capacity math prevents over-commitment.
- **Why hitos?** Without mid-quarter checkpoints, you only discover you're behind when it's too late to adjust.

## Architecture

```
QuarterlyOKRDesign (Conversational + API)
├── Quarter Review      # Analyze previous quarter data
├── Identity Validator  # Check against PersonalContext.md
├── Capacity Calculator # Available hours per pillar
├── OKR Designer        # Objectives + Key Results
├── Milestone Planner   # Hitos for each KR
└── Notion Integration
    └── notion_client.py  # Create OKR entries
```

## Prompt File

> [`prompt.md`](./prompt.md)
