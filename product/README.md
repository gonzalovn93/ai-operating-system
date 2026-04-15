# Product

38 PM workflow templates — structured, opinionated, and ready to generate via natural language.

## Workflows

These run through PM Copilot (Claude Project) or directly via `python main.py {workflow}`:

| Category | Workflows | Examples |
|----------|-----------|---------|
| **Strategy** (15) | PRDs, OKRs, competitive analysis, positioning | `"Write a PRD for X"`, `"Design OKRs for Q2"` |
| **Documents** (13) | Board decks, changelogs, newsletters, case studies | `"Create a board update"`, `"Write case study for X"` |
| **Agents** (7) | Sprint planning, dependency mapping, decision logs | `"Run sprint planning"`, `"Map dependencies for X"` |
| **Desktop** (3) | Quick analysis, dashboard interpretation, Slack rewrites | Real-time, screen-context tasks |

## Key Templates

| Template | What It Produces |
|----------|------------------|
| [**PRD Template**](./prd-template/) | Problem framing, success metrics, user segments, tradeoff analysis, scope, timeline |
| [**OKR Template**](./okr-template/) | Quarterly objectives with scoring rubric, alignment check, capacity validation |
| [**Case Study Template**](./case-study-template/) | Problem → Insight → Product → Process → Outcome → Why It Matters |

## Example

**Input:**
```
"Write a PRD for a feature that lets users share game highlights on social media"
```

**Output:**
- Full PRD: problem statement, user segments, proposed solution, success metrics, risks, scope, open questions, timeline
- Saved to Google Drive as formatted Google Doc
- Tone: senior PM, problem-first, metrics-driven, challenges assumptions

## How it works

38 workflows registered in a declarative registry (`registry.py`). A single runner pipeline reads the workflow definition, applies the appropriate prompt template, calls Claude API, and outputs to Google Drive (with `--gdrive` flag) or terminal. All workflows share the same philosophy: problem-first, metrics-driven, challenge assumptions.

## Stack

Python · Claude API · Google Drive OAuth · Markdown
