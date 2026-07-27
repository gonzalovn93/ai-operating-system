# Models

**Every model choice in this system is deliberate, dated, and audited.**

The other five domains decide *what* gets done. This one decides *what runs it* —
which model for which job, refreshed against the leaderboards monthly instead of
being hardcoded once and forgotten.

> 📦 **The tooling is open source:**
> [github.com/gonzalovn93/model-stack](https://github.com/gonzalovn93/model-stack)

## Workflows

| Workflow | Trigger | What It Produces | Status |
|----------|---------|------------------|--------|
| **Pick** | `"What model should I use for X?"` | One recommendation + fallback + cost per unit of work | ✅ Active |
| **Audit** | `"Audit my models"` | Drift report across every repo, ranked by quality impact × run frequency | ✅ Active |
| **Refresh** | `"Refresh the model stack"` / monthly | Four parallel research agents → rebuilt best-per-task tables | ✅ Active |
| **Decide** | Any new pipeline design | A Model Decision Record per step, before any code is written | ✅ Active |

## Why it exists

The frontier moved **four times in the sixty days** before this was built. A stack
that isn't refreshed monthly is stale by construction — and stale is invisible,
because the old model still returns plausible output.

The first audit of this system found **180 model references — 23 deprecated, 103
stale**, including:

- A **May 2025 model** still writing production content, 14 months later
- An image model superseded by one that was **better on both leaderboards and half
  the price** — 12 files, one find-and-replace
- A video model sitting **240 Elo behind** a frontier option that also cost less
- Every Anthropic call billing prepaid API credits while a subscription sat unused
  for automation — which is what had actually been breaking pipelines, not model
  choice

## How a decision gets made

Four questions, in order, stopping as soon as one decides it:

1. **Task or judgment?** Transcription, image generation, embeddings, OCR → a
   specialist model, always. A frontier LLM doing OCR is worse *and* 20× pricier.
2. **Does a mistake cost more than the tokens?** Outward-facing or decision-critical
   → flagship. Otherwise the quality gap is invisible and the price gap is 30×.
3. **Is a human waiting?** Then latency beats benchmark score.
4. **Will it run 50+ times?** Then it's a pipeline — cascade it. Cheap model does
   the pass, expensive model judges only what's flagged.

Answers land in one of four tiers — **A** flagship, **B** workhorse, **C** bulk,
**L** local/free. Tiers are roles, not brands, so they survive the next release.

## Example

**Audit (runs on command):**

```
$ python registry/scan_models.py

23 deprecated · 103 stale · 53 current (180 references total)

## content-pipeline
  [  STALE   ] gemini-3-pro-image  ×11
               -> gemini-3.1-flash-image (Nano Banana 2)
               why: higher Elo on BOTH t2i (1261 vs 1223) and editing
                    (1248 vs 1240) at HALF the price ($67 vs $134/1k)
```

Exits `1` on actionable deprecations, so it works as a CI gate. Projects can be
marked hands-off — reported, never swept into a batch fix.

**Pick (runs on command):**

> **Use:** `claude-fable-5` — #1 creative writing; this output *is* the voice
> **Fallback:** `claude-sonnet-5` if the volume gets high
> **Cost:** ~$0.30 per post

## What changed after the first pass

Content generation and cover letters moved to the strongest writing model.
Extraction steps dropped to the cheapest tier — two jobs in one pipeline, two
different tiers, which is the whole point. Image generation got better *and*
cheaper. Model IDs moved into one constant per repo instead of scattered across
call sites, because every stale pin found was a **dated** pin.

---

*Detailed audit findings stay local — they reference private project internals.*
