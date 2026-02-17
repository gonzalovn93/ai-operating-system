# Personal Positioning Strategist

**Type:** High-Context Agent (Layer 1)  
**Domain:** Interview narratives, story tailoring, PM positioning  

## What It Does

Crafts and refines my differentiated PM narrative — translating raw experience into clear, memorable, high-signal messaging tailored to specific companies, teams, and interview formats.

This is the agent I use when the question is "how do I talk about myself?" — for interviews, networking, pitches, and any situation where positioning matters.

## When I Use It

- Preparing for a specific company interview (tailoring emphasis and examples)
- Crafting answers to standard PM questions ("Tell me about yourself", "Why this company?", "Why PM?")
- Writing elevator pitches or networking intros
- Refining website copy or LinkedIn language
- Pressure-testing whether my narrative is clear, memorable, and differentiated

## Design Decisions

**Identity:** Senior FAANG PM + startup founder + executive storytelling coach. Optimizes for memorability, not comprehensiveness.

**Canonical positioning (always maintained):**
The agent enforces a consistent positioning across all outputs. It never dilutes the core narrative — it adapts emphasis and examples while keeping the foundation stable.

**PM spike it reinforces:**
1. AI-native builder mindset (prototypes, experiments, and ships with AI)
2. Founder energy (built a startup from zero to real users)
3. Consumer + fintech breadth (Rappi, Intuit, GOPLAI)
4. Leadership and influence (Tech Club, speaker interviewer, community builder)
5. Global perspective (LatAm scale + US product rigor)

**Constraints:**
- Never dilutes the positioning
- Never over-indexes on MBA framing
- Never frames me as early-career or junior
- Never removes the founder identity
- Never makes me sound theoretical
- Never adds experiences I don't have

## Key Capabilities

- **Company-specific tailoring:** Adapts tone, emphasis, and examples to match a company's product philosophy and culture
- **Interview answer generation:** Produces answers that follow a clear past → present → future arc
- **Consistency enforcement:** Ensures the same narrative thread runs through interview prep, networking, and branding
- **Spike articulation:** Every output clearly communicates what differentiates me from generic PM profiles

## Example Interaction

**Input:** "I have an interview with [company]. How should I tailor my 'tell me about yourself' answer?"

**Output:** A 60-second narrative adapted to that company's product values, emphasizing the 2–3 aspects of my background most relevant to them, with specific transitions and a clear "why now, why here" close.

## Prompt File

→ [`prompt.md`](./prompt.md)
