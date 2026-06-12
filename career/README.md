# Career

AI-powered workflows to systematize job search, networking, and applications — from discovery to tailored materials.

## Workflows

| Workflow | Trigger | What It Produces | Status |
|----------|---------|------------------|--------|
| [**JobHunter**](./job-hunter/) | `"Find PM jobs"` | PM roles from 18 target companies, scored and deduped → Notion | ✅ Active (weekly) |
| [**NetworkingScout**](./networking-scout/) | `"Find people at [company]"` | Scored contacts with outreach suggestions → Notion | ✅ Active |
| [**ApplicationBlitz**](./application-blitz/) | `"Generate materials for [job]"` | Tailored resume PDF + cover letter | ✅ Active |
| [**RelationshipNurture**](./relationship-nurture/) | `"Who do I need to follow up with?"` | Cadence-based nurture report + follow-up drafts → Notion | ✅ Active |

## Example

**Input:**
```
"Find PM jobs at companies with <500 employees in the Bay Area"
```

**Output:**
- 12 roles scraped from Ashby, Greenhouse, Workday, Eightfold, TalentBrew
- Each scored for fit (title, experience level, location, company stage)
- Deduplicated against existing Notion Applications DB entries
- Top 3: Anthropic — PM AI Safety (92%), Notion — PM Platform (88%), Stripe — PM Payments (85%)
- Each entry includes: fit score, key requirements, application link, full job description

## How it works

JobHunter scrapes 18 target companies across 6 ATS platforms, filters for PM roles matching expertise and US location, deduplicates against Notion, scores each role, and writes results with full job descriptions. NetworkingScout finds contacts at those companies and scores by Berkeley alumni affinity. ApplicationBlitz takes a job description and generates a tailored resume (PDF via reportlab) and cover letter using Claude. RelationshipNurture keeps the warm connections warm — a cadence engine that surfaces who's overdue and drafts context-aware follow-ups.

The workflows form a pipeline: discover roles → find warm connections → nurture them over time → generate application materials.

## Stack

Python · Claude API · Notion API · reportlab (PDF) · Scheduled automations
