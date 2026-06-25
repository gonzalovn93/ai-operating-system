# VideoThumbnailGenerator — Spec / Prompt

The specification the script implements. Attach to a Claude Code session to generate or evolve LinkedIn video thumbnails.

---

## Goal

One job: make a senior PM, founder, or operator stop scrolling and tap play. Produce a custom thumbnail per video, branded consistently so the feed becomes recognizable after 3–4 posts.

## Technical Requirements

- **Dimensions:** 1920 × 1080 px (16:9)
- **Format:** PNG or JPG, sRGB
- **File size:** under 2 MB
- Also emit a 400 px-wide preview (simulates the LinkedIn mobile feed).

## Layout (locked template)

- **Face — left ~30%.** A still from the talking-head footage, chest up, well-lit, looking at or near the camera. Rounded + softly feathered edge; no hard rectangle border.
- **Screen — right ~55%.** A real screenshot of the key screen moment (Notion, terminal, Claude, etc.), tilted 2–3° with a subtle drop shadow. Legible as a signal, not readable.
- **Hook — bottom, full width.** One line, 6–8 words max. Bold clean sans-serif (Inter Black). White with a soft dark shadow (or a dark semi-transparent pill). Legible at 400 px wide.
- **Background.** Dark navy / near-black (`#1a1a2e` / `#0f0f1a`) or a subtle gradient. Not pure black, not white. Clean — no patterns or textures.

## Style Rules

1. Clean and minimal — two visual elements + one text element, nothing else.
2. No emojis, icons, or logos. The face and the screen are the branding.
3. No clickbait — no red arrows, circles, or shocked faces. This is a professional feed.
4. Consistent across videos — same layout, font, and color scheme every time.
5. The face looks natural, like a real frame from the video (because it is).
6. The screen content is always a real screenshot, never a mockup.

## Inputs Per Thumbnail

1. **Face frame** — exported from the talking-head footage (I provide the timestamp of my best on-camera moment). `ffmpeg -i video.mp4 -ss 00:00:06 -frames:v 1 face.png`
2. **Screen frame** — a screenshot or extracted frame of the key screen moment.
3. **Hook text** — the one-line hook, e.g. "I run my whole life in Notion + AI", "50 workflows. One AI system.", "What my PM toolkit actually looks like".

## Naming

```
[YYYYMMDD]_[topic]_thumbnail.png
[YYYYMMDD]_[topic]_thumbnail_preview.png
```

## Quality Checks (enforced)

- Exactly 1920 × 1080; under 2 MB (auto JPG fallback).
- Hook auto-sized to fit one line and stay legible at 400 px.
- Crop the face above any baked-in subtitle band so captions never bleed into the card.

## What It Should NOT Look Like

YouTube clickbait, a Canva template with stock graphics, an all-text image, a random auto-selected frame, or a cluttered >3-element composition. If it requires reading to understand, it failed — the composition alone should signal "tech/builder walkthrough."
