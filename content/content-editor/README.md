# ContentEditor

**Type:** Advisory Chat Skill
**Skill Domain:** ContentVoice
**Trigger:** `"Review my video script"` · `"Run the quality gate"` · `"Preflight [topic]"`

## What It Does

The editorial co-pilot for short-form LinkedIn video (face + screen-recording format). It reviews scripts and edits against an established standard, runs a structured quality gate before anything ships, inventories raw clips with format checks, produces pre-recording filename cards, and drafts bilingual responses to comments. It's the quality layer between "I have an idea" and "this is good enough to post."

## How It Works

1. **Load the standard:** Reads the voice guide + video editing reference before responding — every judgment is anchored to documented rules, not vibes
2. **Preflight (pre-recording):** Produces a filename card and shot plan so the raw footage is named and structured before the camera turns on
3. **Script review:** Checks structure, hook, and close; enforces the word budget (≈150–170 wpm English / 160–180 wpm Spanish); handles bilingual scripts
4. **Quality gate (post-edit):** A 12-point checklist covering pacing, audio-visual sync, cover frame, and format match before export
5. **Clip inventory:** Scans a footage folder and reports what's usable, flagging clips whose format doesn't match the target orientation
6. **Comment responses:** Drafts substantive, on-brand replies (English or Spanish) to post comments

## Format Rule (the opinionated part)

| Content type | Format |
|--------------|--------|
| Face-dominant | Vertical 9:16 |
| Screen-dominant (Notion, terminal, Claude Code) | Horizontal 16:9 |
| Picture-in-picture | Vertical 9:16 with zoomed screen |

## Design Decisions

- **Why format-by-content-type instead of blanket vertical?** Generic "always go vertical" advice assumes a mobile-first consumer audience. This content targets B2B operators — PMs and founders — who often watch on desktop, where a screen recording is unreadable squeezed into 9:16. The format follows the content, not the platform default.
- **Why advisory instead of auto-editing?** Judgment (does the hook land? is the cut too long?) is where the leverage is, and it's the part a checklist can actually improve. Mechanical clip manipulation is a separate, later phase — the skill is honest about being advisory first.
- **Why a quality gate at all?** A repeatable 12-point pass catches the same failure modes every time (dead cover frame, format mismatch, audio drift) so quality doesn't depend on remembering to check.

## Prompt File

→ [`prompt.md`](./prompt.md)
