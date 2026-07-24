# Byte

**Type:** Generative Chat Skill
**Skill Domain:** ContentVoice
**Trigger:** `"Byte sobre [news/idea]"` · `"Genera un byte de esto: [text/link]"`

## What It Does

Turns a news item or a raw idea into a **recordable 20–40 second video script** — in Spanish, for the Instagram + TikTok short-form channel — in one pass. Paste a headline, a link, or a one-line idea; get back a face-to-camera script with a standalone hook, timed beats, a word count matched to the target length, and a short caption. It closes the gap between "I saw something worth reacting to" and "I know exactly what to say on camera."

This is the short-form counterpart to the longer LinkedIn video workflow ([ContentEditor](../content-editor/)): different channel, different language, different register — same voice discipline.

## How It Works

1. **Input:** a news link/headline, or an idea in one line
2. **Structure:** maps the material onto a fixed 4-beat arc — hook → what happened → *my read* → open close
3. **Word budget:** sizes the script to 20–40s at Spanish delivery speed (160–180 wpm ≈ 55–120 words) and cuts anything over budget
4. **Voice pass:** enforces the channel's spoken, warm register — no CTA, no emojis, no neutral summary
5. **Output:** standalone hook (to rehearse the first 3s), beats with timecodes, word count + duration, a non-CTA close, an optional text overlay, and a short caption

## The Arc (the opinionated part)

| Beat | Time | Job |
|------|------|-----|
| Hook | 0:00–0:03 | The sharpest take first — never "here's the news that…" |
| What happened | 0:03–0:10 | One sentence, in my words, already angled |
| **My read** | 0:10–0:30 | The differentiator: connect the news to something I actually did or decided |
| Close | 0:30–0:40 | A feeling or an open tension — never a CTA |

## Design Decisions

- **Why "connect," not "react"?** A generic reaction to a news item could be filmed by any creator. The rule that carries the whole skill is that the middle beat must tie the news to a lived decision or tradeoff — that's what makes it mine and not a repost with a face on it. If a script would work for anyone reacting to the same headline, it gets rewritten.
- **Why a template skill, not a coded pipeline?** The channel is brand-new and the discipline for its first 90 days is *consistency over infrastructure*. A generator I have to maintain would be the exact trap I'm trying to avoid — building the system instead of publishing. A prompt-shaped skill produces a script in seconds with nothing to run or break.
- **Why open with a take and never the tool's name?** Opening on "there's a new AI tool that…" buries the reason to keep watching. The hook is my read; the news is context underneath it. For tool-driven items the script opens on the problem, never the product name.
- **Why Spanish-native, not translated?** The short-form channel serves Latinos who want the tech ecosystem explained from the inside. Translated scripts read as translated. This writes natively from the beat structure, in a spoken Peru-neutral register.

## Prompt File

→ [`prompt.md`](./prompt.md)
