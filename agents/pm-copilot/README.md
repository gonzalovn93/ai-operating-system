# PM Copilot

**Type:** High-Context Agent (Layer 1) + Static Prompts (Layer 4)  
**Domain:** Product management workflows — PRDs, OKRs, strategy, analysis  

## What It Does

A comprehensive product management toolkit with 38 workflows spanning document generation, strategic analysis, and interactive review. Think of it as a senior PM teammate available on demand.

This skill operates across two layers:
- **Layer 1 (Agents):** Interactive review, tradeoff analysis, tech review, case prep — tasks requiring judgment and iteration
- **Layer 4 (Static Prompts):** PRDs, OKRs, user stories, sizing — repeatable generation tasks

## When I Use It

- Writing a PRD, vision doc, or strategy narrative
- Running a market sizing or pricing exercise
- Preparing for a PM case interview
- Reviewing and critiquing a document
- Generating OKRs, user stories, or acceptance criteria
- Conducting competitive analysis or postmortem analysis

## The 38 Workflows

| Type | Count | Examples |
|------|-------|---------|
| **Prompts** | 15 | OKR, JTBD, RTF, Metrics Framework, Risk Assessment, A/B Test Design, Market Sizing, Pricing, Business Canvas, Unit Economics, Sprint Planning, Dependency Mapping, Capacity Planning, Product Critique, Portfolio Review |
| **Documents** | 13 | PRD, User Stories, Executive Summary, Competitive Analysis, Launch Plan, Market Research, Narrative Memo, Decision Doc, Board Deck, Investor Memo, Changelog, Newsletter, Roadmap |
| **Agents** | 7 | PRD Review, Tradeoff Analysis, Tech Review, Interview Synthesis, Data Analysis, Postmortem, Case Prep |
| **Desktop** | 3 | Stakeholder Alignment, Status Update, Persuasion Brief |

## Design Decisions

**Architecture:** Data-driven registry pattern. All 38 workflows are defined declaratively in a single registry file (~600 lines). A universal runner handles the execution pipeline: input parsing → prompt assembly → Claude API → output formatting → optional Google Drive upload.

**Why this matters:** Adding a new workflow means adding ~15 lines to the registry — no new files, no new logic. This is the same pattern used in production workflow engines: declarative definitions + a universal executor.

**Philosophy:**
- Problem-first (always starts with the problem space before solutions)
- Metrics-driven (every output includes success criteria)
- Challenge assumptions (agents push back on weak reasoning)
- Senior PM tone (outputs read like they were written by a staff PM, not a junior associate)

**Output:** Formatted documents pushed to Google Drive via OAuth, or local markdown/PDF files.

## Example Interaction

**Input:** `"Write a PRD for a feature that lets users share highlights from GOPLAI to Instagram Stories"`

**Output:** A structured PRD with problem statement, user segments, JTBD, proposed solution, success metrics, risks, and open questions — formatted and uploaded to Google Drive.

## Prompt File

→ [`prompt.md`](./prompt.md)

> **Note:** The prompt file contains the master system prompt. Individual workflow definitions live in the registry and are too extensive to include individually, but the architecture and a representative sample are documented here.
