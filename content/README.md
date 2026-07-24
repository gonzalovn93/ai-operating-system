# Content

End-to-end AI content pipeline — from ideation to published carousel to performance retro.

## Workflows

| Workflow | Trigger | What It Produces | Status |
|----------|---------|------------------|--------|
| [**ContentPackageGenerator**](./content-package-generator/) | `"Create the post for [title]"` | LinkedIn post + 7-slide carousel + video script | ✅ Active |
| [**WeeklyIdeation**](./weekly-ideation/) | Weekly | Content ideas from 80+ sources aligned with voice strategy | ✅ Active |
| [**ContentRetro**](./content-retro/) | Weekly | Post performance analysis, pattern insights, improvement recs | ✅ Active |
| [**ContentEditor**](./content-editor/) | `"Review my video script"` | Script/edit review, 12-point quality gate, clip inventory | ✅ Active |
| [**VideoThumbnailGenerator**](./video-thumbnail-generator/) | `"Generate a thumbnail for my video"` | Branded 1920×1080 LinkedIn video thumbnail (face + screen + hook) | ✅ Active |
| [**Byte**](./byte/) | `"Byte sobre [news/idea]"` | Recordable 20–40s Spanish short-form video script (IG/TikTok) from a news item or idea | ✅ Active |

## Example

**Input:**
```
"Create the post for 'Why I built an AI operating system'"
```

**Output:**
- 1 LinkedIn post written in my voice (not generic AI tone)
- 7-slide editorial carousel with composited images (Gemini-generated)
- 45-second video script for short-form content
- Total cost: ~$0.87 per package
- Notion page updated: status moves from Backlog → Drafted

## How it works

ContentPackageGenerator fetches the content idea from the Notion backlog, applies a voice guide (tone, structure, vocabulary rules), generates the post via Claude, creates carousel slides, generates images via Gemini, and composites them. Everything writes back to the same Notion page. WeeklyIdeation scans 80+ sources for theme-aligned ideas. ContentRetro analyzes LinkedIn metrics to surface what's working. VideoThumbnailGenerator turns a raw video into a branded, publish-ready thumbnail from a couple of timestamps — face frame, screen frame, and a one-line hook composited into a consistent layout.

This is the same system at work for content *generation*, not just planning: ideas in, finished posts, carousels, scripts, and thumbnails out — all in one voice.

## Stack

Claude API · Gemini · Python · LinkedIn metrics CSV · Notion API
