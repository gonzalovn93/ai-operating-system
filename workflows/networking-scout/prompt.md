# NetworkingScout — Workflow Prompt

## Purpose
Find people at target companies using LinkedIn, prioritize alumni from your MBA program, and draft company-specific outreach messages.

## Core Functionality

### Input
- Company name (from Companies DB)
- Optional: Role filter (PM, Director, VP)
- Optional: Tier filter (runs for all Tier 1 companies)

### Processing
1. Browse LinkedIn company people page
2. Extract profile data (name, position, LinkedIn URL, bio)
3. Detect alumni affiliation (MBA program)
4. Score and prioritize contacts
5. Generate company-specific messages
6. Populate Network DB with approval

### Output
- New entries in Network DB
- Personalized messages stored in toggle blocks
- Prioritized contact list

## Alumni Prioritization

### Detection Logic

**Sources to check:**
1. Education section: University name
2. Education section: Business school name
3. Profile headline: MBA mentions
4. Bio: school/alumni references

**Affiliation Types & Bonuses:**
- **MBA** — Highest priority (+5 bonus)
- **Undergrad** — High priority (+4 bonus)
- **Other connection** — Medium priority (+3 bonus)
- **No affiliation** — Base priority (0 bonus)

### Scoring Formula

```python
def calculate_priority_score(person):
    seniority_scores = {
        "CEO / Founder": 12, "Vice President": 11,
        "Director": 10, "Senior Manager": 8,
        "Manager": 7, "Senior PM": 8,
        "Product Manager": 6, "Individual Contributor": 5
    }
    base_score = seniority_scores.get(person["seniority"], 5)
    alumni_bonus = detect_alumni_status(person["education"])
    relevance = score_title_relevance(person["position"])

    return {
        "total": base_score + alumni_bonus + relevance,
        "breakdown": {"seniority": base_score, "alumni": alumni_bonus, "relevance": relevance}
    }
```

## Company-Specific Message Templates

### Template Structure
1. **Opening:** Personalized greeting
2. **Context:** Who you are (MBA, PM, builder)
3. **Hook:** Company-specific insight or connection
4. **Your Project:** Tailored to company domain
5. **Ask:** 15 min chat to learn about their path
6. **Close:** Professional sign-off

### Template Examples

**Consumer Tech (e.g. Notion):**
```
Hi [name],

I'm a Haas MBA '26 targeting PM roles in consumer + AI products. I've been following
[Company]'s work on [recent feature] — really impressed by how you've maintained
product craft while building AI into the core experience.

I'm currently designing my personal productivity system using Notion + Claude
(career OS, task management, OKRs), and it's been a fascinating exercise in
systems thinking. Would love 15 minutes to learn about your path to [Company].

Would you be open to a quick chat?

Best,
Gonzalo
```

**Sports/Lifestyle (e.g. Strava):**
```
Hi [name],

I'm a Haas MBA '26 and PM building GOPLAI, an AI sports-tech product that generates
highlights and performance insights for amateur athletes. I've been a [Company] user
for years and love how you balance community building with performance analytics.

Would love 15 minutes to learn about your path to [Company] and how you think about
building for athletes.

Best,
Gonzalo
```

**Haas MBA Alumni Variation:**
```
Hi [name],

Fellow Haasie here! ('26) I came across your profile and saw you're at [Company] —
congrats on the journey from Berkeley to [Company].

I'm targeting PM roles in consumer + AI and building GOPLAI (AI sports-tech). Would
love 15 minutes to learn about your path and get your advice on breaking into [Company].

Go Bears!

Best,
Gonzalo
```

**Berkeley Undergrad Alumni Variation:**
```
Hi [name],

Go Bears! I'm a Haas MBA '26 and saw you're a Cal alum at [Company].

I'm targeting PM roles in consumer + AI and would love 15 minutes to learn about
your path from Berkeley to [Company] and get your perspective on the PM role there.

Best,
Gonzalo
```

### Notion Integration

```python
# Create Network DB entry
notion.pages.create(
    parent={"database_id": "your-notion-db-id"},
    properties={
        "Name": {"title": [{"text": {"content": person["name"]}}]},
        "Position": {"rich_text": [{"text": {"content": person["position"]}}]},
        "Company": {"relation": [{"id": company_page_id}]},
        "LinkedIn": {"url": person["linkedin_url"]},
        "Outreach status": {"status": {"name": "Not reached"}}
    }
)

# Append outreach message as toggle block
notion.blocks.children.append(
    block_id=page_id,
    children=[{"type": "toggle", "toggle": {
        "rich_text": [{"text": {"content": "First contact"}}],
        "children": [{"type": "paragraph", "paragraph": {
            "rich_text": [{"text": {"content": person["draft_message"]}}]
        }}]
    }}]
)
```

## Output Example

```
NetworkingScout - Notion

Browsing LinkedIn company page...
✓ Found 28 people

Filtering for PM roles...
✓ 12 people match

Scoring and prioritizing...

═══════════════════════════════════════
TOP CONTACTS
═══════════════════════════════════════

PRIORITY 1 - Berkeley Alumni:
1. Sarah Chen
   Senior PM, AI Features | Haas MBA '22
   Score: 16 (Seniority: 8, Berkeley: +5, Relevance: +3)
   ✓ Message drafted

2. John Martinez
   Director, Product Platform | Berkeley '18
   Score: 14 (Seniority: 10, Berkeley: +4, Relevance: 0)
   ✓ Message drafted

PRIORITY 2 - High Seniority:
3. Maria Rodriguez
   VP Product | No Berkeley
   Score: 11 (Seniority: 11, Berkeley: 0, Relevance: 0)
   ✓ Message drafted

═══════════════════════════════════════

Add to Network DB? (y/n or select numbers: 1,2,5)
> 1,2,3

✓ Added 3 people to Network DB
✓ Messages stored in "[Reachout message]" toggle
✓ Ready to review in Notion!
```

## Usage

```bash
python main.py scout --company="CompanyName"          # Single company
python main.py scout --company="Name" --role="PM"     # With role filter
python main.py scout --tier=1                          # All Tier 1
python main.py scout --company="Name" --dry-run        # Preview only
python main.py scout --json                            # Structured output
```

## Success Criteria

- Extracts LinkedIn profile data accurately
- Detects alumni affiliation
- Prioritizes alumni contacts (+5 bonus)
- Generates company-specific messages
- Stores in Network DB with toggle blocks
- User reviews and approves before adding
