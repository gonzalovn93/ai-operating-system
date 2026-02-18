# JobHunter

**Type:** Automated Python Workflow  
**Skill Domain:** CareerOS  
**Command:** `python main.py hunt`  

## What It Does

Automatically discovers PM roles from target companies by scanning their public career pages, filters for relevance, and writes qualified opportunities to a Notion database — ready for review and action.

## How It Works

1. **Discovery:** Iterates through a configured list of target companies and their career page endpoints
2. **Filtering:** Applies an expertise filter to match roles against target criteria (PM roles, seniority level, location)
3. **Enrichment:** Extracts key details — title, team, location, job description highlights, and application link
4. **Scoring:** Ranks opportunities by fit against my profile and preferences
5. **Output:** Writes qualified roles to the Notion Applications database with structured properties

**Flags:**
- `--json` — Output structured JSON instead of Notion writes (useful for piping to other workflows)
- `--dry-run` — Preview results without writing to Notion

## Design Decisions

- **Why not just use LinkedIn job alerts?** LinkedIn alerts are noisy and generic. This system targets specific companies I've researched, applies custom filtering logic, and writes directly to my pipeline — no manual copy-paste.
- **Why Notion as the destination?** The Applications database is part of a larger system. Job entries link to the Companies database and the Network database, creating a connected pipeline where I can see which roles I've found, who I know at that company, and what materials I've generated — all in one view.
- **Why raw httpx instead of Notion SDK?** The official `notion-client` Python package has gaps (no `databases.query()`). Raw httpx calls with a custom helper module are more reliable.

## Architecture

```
job_hunter/
├── job_hunter.py              # Main orchestrator
├── linkedin_job_search.py     # LinkedIn job discovery
├── expertise_filter.py        # Role relevance filtering
└── scrapers/                  # Company-specific career page parsers
```

## Output

Each discovered role creates a Notion database entry with:
- Company name (linked to Companies DB)
- Role title
- Team / product area
- Location
- Application URL
- Fit score
- Status (default: "New")
- Date discovered

## Prompt File

→ [`prompt.md`](./prompt.md) — Contains the SKILL.md routing definition and filtering criteria
