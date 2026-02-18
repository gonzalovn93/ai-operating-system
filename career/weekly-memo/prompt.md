# WeeklyRecruitingMemo — Workflow Prompt

## Purpose
Generate a strategic weekly recruiting memo with interactive task approval, then create approved tasks in Notion.

## Core Functionality

### Input
- All 3 Notion databases (Companies, Network, Applications)
- Previous week's activity
- Current pipeline status

### Processing
1. Analyze recruiting pipeline health
2. Identify priority actions (applications, networking, follow-ups)
3. Generate strategic memo (not just a digest)
4. Present in chat with approval interface
5. Create approved tasks in Task Management DB
6. Store memo in Networking page

## Memo Structure

```markdown
📋 Weekly Recruiting Memo — Week of [Date]

═══════════════════════════════════════
EXECUTIVE SUMMARY
═══════════════════════════════════════

Pipeline Status:
• [X] active applications ([Y] interviews, [Z] final rounds)
• [X] networking conversations ([Y] warm leads)
• [X] new Tier 1 job openings this week

Strategic Focus This Week:
✓ [Priority 1]
✓ [Priority 2]

Critical Path:
🔴 [Time-sensitive item with deadline]

═══════════════════════════════════════
PRIORITY TASKS
═══════════════════════════════════════

TASK 1: [Task Name]
├─ Context: [Why this matters now]
├─ Action: [Specific steps]
├─ Time: [Estimated time]
├─ Priority: HIGH / MEDIUM / LOW
└─ Deadline: [If applicable]

[ ] APPROVE    [ ] SKIP

═══════════════════════════════════════
PIPELINE HEALTH DASHBOARD
═══════════════════════════════════════

Applications by Stage: Not applied | Applied | Interview | Offer
Network Coverage: Companies with gaps vs. well-covered
Warm Leads Going Cold: >3 weeks without contact

═══════════════════════════════════════
INSIGHTS & RECOMMENDATIONS
═══════════════════════════════════════
[Strategic observations and pivot suggestions]
```

## Task Generation Logic

### Type 1: Apply to New Jobs
**Trigger:** New jobs with Status="Not applied"
**Priority:** Tier 1 companies, approaching deadlines, high-interest areas

### Type 2: Network at Gap Companies
**Trigger:** Tier 1 companies with 0-1 contacts

### Type 3: Follow Up Warm Leads
**Trigger:** Warm relationships + last contact >3 weeks ago

### Type 4: Prepare for Interviews
**Trigger:** Interviews scheduled within 7 days

### Type 5: Weekly Networking Quota
**Trigger:** Standard weekly cold outreach goal

## Pipeline Health Metrics

```python
# Application funnel
{"not_applied": X, "applied": X, "interview": X, "offer": X, "rejected": X}
# + conversion rates between stages

# Network coverage per company
{"company": {"total_contacts": X, "warm_contacts": X, "alumni": X}}
# + companies with gaps (< 2 contacts)

# Warm leads going cold
[contacts where relationship="Warm" AND last_contact > 3 weeks ago]
```

## Interactive Approval

```python
# Display memo, then prompt:
# "Approve tasks? (Enter: 1,3,5 | 'all' | 'none')"
# Parse response → create approved tasks in Notion
```

## Output Example

```
Generating weekly recruiting memo...
✓ Analyzed 52 jobs in Applications DB
✓ Analyzed 23 contacts in Network DB
✓ Analyzed 16 Tier 1 companies

═══════════════════════════════════════
PRIORITY TASKS
═══════════════════════════════════════

TASK 1: Apply to 3 Tier 1 Jobs
├─ Jobs:
│  • Notion - AI Product Manager (SF) - Closes 2/14 🔴
│  • YouTube - Senior PM, Creator Tools (MTV) - Posted 2/8
│  • Perplexity - Product Manager (SF) - Posted 2/9
├─ Time: 2 hours (with ApplicationBlitz)
├─ Priority: HIGH
└─ Deadline: Friday 2/14

TASK 2: Network at Companies with Gaps
├─ Companies: OpenAI, Slack, Perplexity (0 contacts each)
├─ Time: 1.5 hours
└─ Priority: MEDIUM

TASK 3: Follow Up - Warm Leads
├─ People:
│  • Sarah Chen (Strava, Senior PM) - Last: 3 weeks ago
│  • John Martinez (YouTube, Director) - Last: 4 weeks ago
├─ Time: 30 min
└─ Priority: MEDIUM

Approve tasks? (1,3,5 | 'all' | 'none')
> 1,3

✓ Approved tasks: 1, 3
✓ Created 2 tasks in Notion Task Management
✓ Memo stored in Notion Networking page
```

## Usage

```bash
python main.py memo           # Standard weekly run
python main.py memo --now     # Generate immediately
python main.py memo --preview # Preview without task creation
```

## Success Criteria

- Strategic memo with actionable insights (not just a data dump)
- Interactive task approval in chat
- Approved tasks created in Notion
- Memo archived for historical reference
- Total interaction < 5 minutes
