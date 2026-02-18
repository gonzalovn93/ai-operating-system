# ContentPackageGenerator

**Type:** On-Demand Python Pipeline  
**Skill Domain:** ContentVoice  
**Module:** 07 (Primary)  

## What It Does

Generates a complete LinkedIn content package from a single idea: written post, 7-slide carousel with composited images, and a 45-second video script. One command, full creative output.

## How It Works

Three input modes:
- **Notion-first:** `python main.py <page_id>` — Pull an idea from the Content database and generate a full package
- **Quick mode:** `python main.py --quick "idea here"` — Generate from a one-line idea
- **Paste mode:** `python main.py --paste` — Generate from clipboard content

**Pipeline:**
1. Idea intake (from Notion, CLI, or clipboard)
2. Post drafting via Claude API, guided by a `voice_guide.md` that maintains consistent writing voice
3. Carousel structure generation (7 slides with headline, body, and visual direction per slide)
4. Image compositing via Gemini
5. Video script generation (45-second format)
6. Output packaging into a timestamped directory

## Design Decisions

- **Why one module instead of three?** This module replaced three earlier ones (PostDrafting, VisualGeneration, VideoScripting). Running three separate commands to produce one post created friction. Consolidating into a single pipeline — one input, full output — is the right UX.
- **Why keep the legacy modules?** They still work for edge cases. Sometimes I only need a text draft, not a full carousel. The legacy modules serve as escape hatches. This mirrors how real product systems evolve: consolidate the happy path, keep alternatives available.
- **Why a voice guide?** Consistency across posts matters more than any individual post being perfect. The `voice_guide.md` codifies my writing style — tone, sentence structure, vocabulary, what to avoid — so every output sounds like me, not like generic AI.
- **Why Claude for text + Gemini for images?** Each model has different strengths. Claude produces better structured writing; Gemini handles image generation and compositing. Using the right tool for each task beats forcing one model to do everything.

## Output Structure

```
output/<page_id>_<timestamp>/
├── post.md              # LinkedIn post text
├── carousel/
│   ├── slide_1.png      # 7 composited carousel images
│   ├── slide_2.png
│   └── ...
├── video_script.md      # 45-second video script
└── metadata.json        # Generation parameters and source info
```

## Prompt File

→ [`prompt.md`](./prompt.md)
