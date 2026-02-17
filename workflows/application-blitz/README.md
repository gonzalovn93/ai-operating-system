# ApplicationBlitz

**Type:** Automated Python Workflow  
**Skill Domain:** CareerOS  
**Command:** `python main.py blitz`  

## What It Does

Generates tailored application materials — resume (PDF) and cover letter — for a specific role. Analyzes the job description, maps it against my experience, and produces materials optimized for that particular opportunity.

## How It Works

1. **Job analysis:** Parses the job description to extract key requirements, preferred skills, team context, and success criteria
2. **Experience mapping:** Maps JD requirements against my background to identify the strongest proof points and any gaps
3. **Resume generation:** Produces a tailored PDF resume using `reportlab`, emphasizing the experiences most relevant to this specific role
4. **Cover letter generation:** Drafts a cover letter that connects my background to the role's specific needs
5. **Output:** Local files (PDF + markdown) + Notion database entry linking to the application

## Design Decisions

- **Why PDF generation via reportlab?** Consistent formatting across every application. No manual Word editing, no template drift. The same clean layout every time.
- **Why job analysis as a separate step?** Understanding *what they're actually looking for* before writing materials produces dramatically better tailoring. Most applicants skip this step — they customize the header and leave the rest generic.
- **Why link to Notion?** Each application entry connects to the Companies and Network databases. I can see at a glance: what role I applied for, who I know there, and what materials I used.

## Architecture

```
application_blitz/
├── application_blitz.py      # Main orchestrator
├── job_analyzer.py           # JD parsing and requirement extraction
├── resume_generator.py       # Tailored PDF resume generation
└── cover_letter_generator.py # Cover letter drafting
```

## Prompt File

→ [`prompt.md`](./prompt.md)
