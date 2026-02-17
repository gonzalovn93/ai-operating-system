# ContentPackageGenerator — Workflow Prompt

## Purpose
Generate complete LinkedIn content packages from a single idea: post + 7-slide carousel + composited images + 45-second video script.

## Architecture

### 3 Modes

| Mode | Command | Input |
|------|---------|-------|
| **Notion-first** | `python main.py <page_id>` | Fetches existing Backlog page from Content DB |
| **Quick capture** | `python main.py --quick` | Interactive: enter title, angle, key points |
| **Paste raw** | `python main.py --paste` | Paste raw notes, AI extracts structure |

### Output Per Package
- `linkedin_post.txt` — Ready-to-post LinkedIn text
- `carousel_outline.json` — 7-slide structure with text + image prompts
- `video_script.txt` — 45-second video script
- `canva_specs.json` — Design templates and specs
- `generated_images/` — AI-generated images (Gemini)
- `carousel_final/` — Composited carousel slides

### Cost
~$0.87 per package (Claude text generation + Gemini image generation)

## Voice Guide (Non-Negotiable)

All content follows a strict editorial voice:

### Tone
- Calm, reflective, confident without attitude
- Precise and self-aware
- Builder-first, emotionally honest, never performative
- The writing can smile. It should never shout.

### Hard Rules
- No emojis (zero, no exceptions)
- No hashtags (zero, unless explicitly requested)
- No sales language or universal truths
- No tip lists ("X things I learned")
- No "LinkedIn influencer" patterns
- If it sounds like a landing page, rewrite it

### Content Pillars

**1. Experience first, framework second**
If you didn't live it, don't post it. Frameworks allowed only AFTER the lived moment.

**2. Systems over tips**
Lists only if they reveal structure, tradeoffs, or a real system.

**3. Emotional honesty, never manipulation**
Show real doubt and tension, but never perform emotions for engagement.

**4. Bilingual, not duplicated**
English = operating, building, AI systems, career.
Spanish = identity, growth, purpose, lived tension.

**5. Taste is a feature**
Short paragraphs (1-2 lines). White space matters. Clean visuals.

### Required Elements (At Least ONE Per Post)
- A tradeoff you're managing
- A constraint you're working within
- Something that still doesn't work
- A decision NOT to automate
- A limit you've hit
- A thing you got wrong

### Narrative Structure
Observation → Constraint → Decision → Consequence

### Endings (Choose ONE)
- Personal redefinition ("I used to think X. Now I think Y.")
- Open tension ("Still figuring out whether...")
- Question you're sitting with ("Not sure if...")

Never end with: call to action, "What do you think?", generic takeaway, inspiration.

## Post Structure

1. **Hook:** 1-2 lines. No cliches. No "excited to share."
2. **Context:** What happened and why it mattered.
3. **Insight:** What changed in how you think, work, or decide.
4. **Close:** Grounded takeaway, intention, or observation.

## Carousel Design (7 Slides)

| Slide | Content |
|-------|---------|
| 1 | Hook + title (attention grabber) |
| 2 | Context / problem setup |
| 3-5 | Core insight, framework, or progression |
| 6 | Key takeaway or shift in thinking |
| 7 | Close + subtle CTA or open question |

Each slide includes:
- Text content (max 40 words)
- Image generation prompt (for Gemini)
- Layout guidance (text position, visual style)

## Language Routing

Content language is determined by topic tags:
- **English:** Product, AI, Tech, Career, Building, Systems
- **Spanish:** Productivity, Entrepreneurship, Peru, LatAm, Identity, Growth

## Notion Integration

- Fetches existing Backlog page (never creates new pages)
- Appends generated content to the page body
- Sets Status: Backlog → Drafted
- Sets Date property for view filtering

## Usage

```bash
python main.py <notion_page_id>     # From existing idea
python main.py --quick               # Interactive mode
python main.py --paste               # From raw notes
```

## File Structure

```
07_ContentPackageGenerator/
├── main.py                  # Orchestrator (3 modes)
├── voice_guide.md           # Editorial voice rules
├── generators/
│   ├── post_generator.py    # LinkedIn post via Claude
│   ├── carousel_generator.py # 7-slide structure
│   ├── image_generator.py   # Gemini image generation
│   ├── compositor.py        # Image + text compositing
│   └── video_script_generator.py
├── notion_sync.py           # Fetch idea + publish result
└── output/                  # Generated packages
```

## Success Criteria

- Post follows voice guide (no emojis, no cliches, no influencer tone)
- Carousel is 7 slides with clear visual direction
- Images are generated and composited
- Video script is 45 seconds, natural, conversational
- Total generation time < 3 minutes
- Content synced back to Notion with Drafted status
