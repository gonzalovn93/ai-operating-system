# ApplicationBlitz — Workflow Prompt

## Purpose
Generate tailored resume, cover letter, and application answers in under 5 minutes for any PM role.

## Core Functionality

### Input
- Job from Applications DB (URL or Notion page ID)
- Job description (fetched automatically)
- Company context from Companies DB

### Processing
1. Analyze job description (key requirements, skills, culture signals)
2. Select relevant experiences from background
3. Generate tailored resume (emphasize relevant experience)
4. Write cover letter (if needed)
5. Answer common application questions

### Output
- Tailored resume (PDF via reportlab)
- Cover letter (DOCX or PDF)
- Application answers (text file)
- All saved to `outputs/applications/{company}-{role}/`

## Resume Generation Strategy

### Company-Type Tailoring

**For Consumer/AI Companies:**
- Emphasize: Startup AI experience, consumer product sense
- Lead with: AI-native PM positioning
- Highlight: 0→1 experience, product craft

**For Big Tech:**
- Emphasize: Scale experience, platform work
- Lead with: Years of PM experience
- Highlight: Cross-functional leadership, data-driven decisions

**For Fintech:**
- Emphasize: Fintech platform experience
- Lead with: Fintech PM positioning
- Highlight: Payments, onboarding, enterprise

**For Sports/Consumer Lifestyle:**
- Emphasize: Sports-tech startup
- Lead with: PM for athletes/communities
- Highlight: Consumer engagement, domain passion

### Dynamic Experience Ordering

Reorder resume sections based on the target role type:
- AI-focused → Startup first, then enterprise, then consumer
- Consumer/Scale → Consumer scale first, then startup, then enterprise
- Fintech → Fintech first, then marketplace, then startup

## Cover Letter Template

```
[Your Name]
[Date]

Dear [Hiring Manager],

[P1: Positioning + excitement about the specific role]
[P2: Most relevant experience, matched to job requirements]
[P3: Why this company — specific product insight, not generic]
[P4: Current project and how it connects]
[P5: Close — what you'd bring + thank you]

Best regards,
[Your Name]
```

## Application Question Templates

### "Why do you want to work here?"
```
Three reasons:
1. Product Philosophy: [Company]'s approach to [specific aspect]
2. Impact at Scale: Opportunity to build for [users]
3. Team & Culture: [Company's] focus on [specific value]
```

### "Tell us about a 0→1 product you built"
```
Problem → Solution → Approach → Impact → Key Learning
(Always include a specific metric and a user behavior insight)
```

### "Describe your PM approach"
```
Three principles:
1. Start with the Problem, Not the Solution (example)
2. Bias Toward Shipping & Iteration (example)
3. Data + Intuition (example)
```

## Usage

```bash
python main.py blitz --url="https://company.com/careers/12345"
python main.py blitz --job-id="notion-page-id"
python main.py blitz --job-id="id" --preview   # No file output
python main.py blitz --json                      # Structured output
```

## Success Criteria

- Generates tailored resume in < 2 minutes
- Resume emphasizes relevant experiences per job
- Cover letter includes company-specific hooks
- Application answers are compelling and specific
- Total time < 5 minutes per application
