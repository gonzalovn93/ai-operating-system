# Competitor Intelligence Agent — Perplexity AI

## 1. Company and Strategic Context

Perplexity AI is a Series B+ AI-powered answer engine ($20B valuation, ~$200M ARR) competing in the AI search market against Google (AI Overviews), OpenAI (SearchGPT/ChatGPT Search), Microsoft (Copilot), and Anthropic — its business model is freemium subscription (Pro at $20/mo) plus enterprise licensing and API access. This agent serves Perplexity's **Head of Product**, providing weekly structured intelligence on competitor product moves, distribution deals, hiring signals, and developer ecosystem changes to inform roadmap prioritization and competitive positioning decisions.

## 2. Agent Prompt

```
You are a Competitor Intelligence Agent for Perplexity AI.

Your job is to monitor four competitors — Google (AI Overviews), OpenAI (SearchGPT), Microsoft Copilot, and Anthropic — and produce a structured weekly intelligence report for Perplexity's Head of Product.

You have access to a web_search tool. Use it strategically — not broadly.

## Your monitoring scope

For each competitor, track signals in four categories:

1. PRODUCT MOVES — New features, UI changes, model upgrades, API changes, search mode updates, citation behavior changes
2. DISTRIBUTION & PARTNERSHIPS — Enterprise deals, browser integrations, device partnerships, ISP/telco bundling
3. TALENT & HIRING — Job postings that signal infrastructure investment, new capability areas, or strategic pivots
4. DEVELOPER ECOSYSTEM — New APIs, pricing changes, developer tool launches, third-party integrations

## Your search strategy

Run targeted searches. For each competitor, search:
- "[Competitor] product update [current month]"
- "[Competitor] search AI news [current month]"
- "[Competitor] partnership announcement [current month]"
- "[Competitor] job postings AI search [current month]"

Do not search more than 3-4 queries per competitor. Filter signal from noise.

## What counts as signal vs noise

SIGNAL (include):
- A competitor ships a feature that directly competes with Perplexity's answer engine, citations, or Pro Search
- A competitor announces a distribution deal that expands their search surface (devices, browsers, enterprise)
- Hiring patterns suggest a competitor is building toward real-time web grounding or citation-based answers
- Pricing changes that could pressure Perplexity's subscription model

NOISE (exclude):
- Generic AI news not specific to search
- Opinion pieces and speculation without product evidence
- Earnings calls without product implications
- Anything older than 30 days

## Output format

Produce a structured Markdown report with this exact schema:

---
# Perplexity Competitor Intelligence Report
**Date:** [today]
**Prepared for:** Head of Product, Perplexity AI
**Monitoring period:** Last 30 days

## Executive Summary
2-3 sentences. What is the single most important competitive development this week? What should the Head of Product do with this information?

## Competitor Snapshots

### Google (AI Overviews)
**Threat level:** [High / Medium / Low]
**Key signal:** [One sentence]
**Details:** [2-3 sentences with source]
**Strategic implication for Perplexity:** [One sentence]

### OpenAI (SearchGPT / ChatGPT Search)
[same structure]

### Microsoft Copilot
[same structure]

### Anthropic
[same structure]

## Signals to Watch
3 bullet points — early signals that aren't yet material but could become important in 30-60 days.

## Recommended Actions
2-3 specific, actionable recommendations for the Head of Product based on this week's findings.

---

Be specific. Cite sources inline. Do not include information you cannot verify through your search results. If a competitor category has no material signal this week, say so explicitly rather than filling space.
```

## 3. Technologies Used

| Technology | Role | Justification |
|---|---|---|
| **Claude Sonnet (Anthropic API)** | Core LLM for reasoning, synthesis, and report generation | Strong at structured output, tool use, and long-context synthesis. The tool_use API enables the agent to autonomously decide when and what to search. |
| **Tavily Search API** | Web search tool | Purpose-built for AI agents. Returns structured results (title, URL, content snippet) with recency filtering (`days` parameter). Free tier provides 1,000 searches/month — sufficient for weekly scans of 4 competitors. |
| **Python** | Orchestration runtime | Lightweight agent loop (~80 lines). No framework overhead — direct API calls with a while loop that handles tool use and response parsing. |
| **python-dotenv** | Environment variable management | Keeps API keys out of source code via `.env` file (gitignored). |
| **Notion (output destination)** | Report storage and delivery | Reports are appended to a Notion page as Toggle Heading 2 blocks, organized chronologically. The Head of Product can expand any week's report without leaving their workspace. |
| **Windows Task Scheduler** | Automation | Runs the agent every Monday at 9:00 AM via `schtasks`. No cloud infrastructure required. |

## 4. Inputs

| Input | Format | Frequency | Structured? | Preprocessing |
|---|---|---|---|---|
| Web search results from Tavily API | JSON (title, URL, content snippet, score) | On each agent run (weekly) | Semi-structured — Tavily returns JSON but content field is raw text | Formatted into Markdown blocks before being passed back to Claude as tool results |
| Current date | String (e.g., "March 30, 2026") | Injected at runtime | Structured | Formatted via `datetime.now().strftime()` and included in the user message so the agent knows the current time period |
| System prompt (competitive monitoring scope) | Text | Static per run | Unstructured | None — passed directly as the `system` parameter to the Claude API |

**Search queries generated by the agent (typical run):**
- `Google AI Overviews product update March 2026`
- `OpenAI SearchGPT ChatGPT search news March 2026`
- `Microsoft Copilot search AI partnership March 2026`
- `Anthropic AI search product updates Claude March 2026`
- `Google Microsoft OpenAI Anthropic job postings AI search hiring March 2026`
- `OpenAI API pricing ChatGPT SearchGPT developer tools March 2026`

The agent typically executes 6-8 searches per run. Each search returns up to 5 results via Tavily's `advanced` search depth, filtered to the last 30 days.

## 5. Outputs

**Output schema:**

```markdown
# Perplexity Competitor Intelligence Report
**Date:** [YYYY-MM-DD]
**Prepared for:** Head of Product, Perplexity AI
**Monitoring period:** Last 30 days

## Executive Summary
[2-3 sentences — most important development + recommended action]

## Competitor Snapshots
### [Competitor Name] — Threat: [High/Medium/Low]
- **Key signal:** [One sentence]
- **Details:** [2-3 sentences with inline source citations]
- **Strategic implication:** [One sentence]

[Repeated for each of 4 competitors]

## Signals to Watch
[3 bullet points — early/emerging signals]

## Recommended Actions
[2-3 numbered, specific recommendations]
```

**Frequency:** Weekly (every Monday at 9:00 AM), with option for on-demand runs.

**Consumer:** Head of Product, Perplexity AI.

**Confidence scoring:** Implicit through threat level assignments (High / Medium / Low) per competitor. The agent is instructed to only include information it can verify through search results and to explicitly state "no material signal" when a category lacks evidence, rather than fabricating findings.

**Delivery:** Reports are saved locally as timestamped Markdown files (`output/report_YYYYMMDD_HHMM.md`) and appended to a Notion page as collapsible Toggle Heading 2 blocks organized by date.

### Sample Output (March 30, 2026)

---
# Perplexity Competitor Intelligence Report
**Date:** March 30, 2026
**Prepared for:** Head of Product, Perplexity AI
**Monitoring period:** Last 30 days

## Executive Summary
March 2026 marked the most aggressive month in AI search competition, with Google expanding AI Overviews ad integration, OpenAI launching GPT-5.4 with computer control capabilities, Microsoft rolling out Agent 365 at scale, and Anthropic shipping 14+ major releases including 1M context at standard pricing. The most critical development is the convergence toward autonomous AI agents across all platforms, fundamentally shifting from reactive search to proactive task execution — a paradigm that directly challenges Perplexity's conversational search model.

## Competitor Snapshots

### Google (AI Overviews) — Threat: High
**Key signal:** AI Overviews now serve ads above, below, and within search results, expanding commercial opportunity for advertisers while maintaining citation behavior.
**Details:** March 2026 saw Google's most significant AI Overviews monetization push, with ads eligible to appear directly integrated within AI-generated responses depending on geography, language, and user intent. The March Core Update also prioritized content that AI trusts to cite, raising quality bars for source inclusion. Google's AI Mode is handling an increasing proportion of queries with original, authoritative content favored for citations.
**Strategic implication for Perplexity:** Google's ad integration validates commercial viability of AI search while their citation quality requirements could create opportunities if Perplexity maintains higher editorial standards.

### OpenAI (SearchGPT / ChatGPT Search) — Threat: High
**Key signal:** GPT-5.4 launched with native computer-use capabilities and SearchGPT integrated search at $10/1k calls, while massive hiring push targets enterprise adoption.
**Details:** OpenAI shipped GPT-5.4 with 75% OSWorld-Verified computer control, 1M context, and 33% fewer factual errors. SearchGPT web search is now production-ready at competitive pricing ($10/1k calls vs $25/1k for non-reasoning models). The company is aggressively hiring 3,500+ employees to reach 8,000 by year-end, with enterprise sales as fastest-growing segment.
**Strategic implication for Perplexity:** OpenAI's enterprise focus and computer-use capabilities signal a shift toward autonomous agents that could bypass traditional search entirely.

### Microsoft Copilot — Threat: Medium
**Key signal:** Agent 365 launches May 1st at $15/user/month with Anthropic partnership for "Copilot Cowork" autonomous task execution.
**Details:** Microsoft announced Agent 365 as "the control plane for AI agents" with registration, access control, and interoperability across M365 apps. Copilot Cowork, built with Anthropic's Claude, takes tasks, creates plans, and executes them across Office applications in background. Microsoft 365 E7 bundle positions agents as core productivity infrastructure.
**Strategic implication for Perplexity:** Microsoft's agent orchestration layer could make search a backend function rather than frontend experience, requiring Perplexity to consider integration strategies.

### Anthropic — Threat: Medium
**Key signal:** 1M context window now available at standard pricing with no surcharge, eliminating the 2x premium for long-context requests.
**Details:** Anthropic shipped 14+ major releases in March including 1M context at standard pricing (78.3% MRCR v2 performance vs GPT-5.4's 36.6%), computer use in research preview, Claude Code for parallel development workflows, and Claude Dispatch for persistent agent threads. Media limits increased 6x to 600 images/PDFs per request.
**Strategic implication for Perplexity:** Anthropic's pricing efficiency and partner-first go-to-market could pressure Perplexity's direct subscription model while their context capabilities enable deeper document analysis.

## Signals to Watch
- **Agent orchestration convergence**: All four competitors are moving toward agent-first experiences that complete tasks rather than just answer questions, potentially reducing direct search volume
- **Enterprise integration acceleration**: Microsoft's E7 bundling and OpenAI's technical ambassador hiring suggest enterprise AI search will be embedded in productivity workflows rather than standalone tools
- **Computer vision + search fusion**: Anthropic's 600 image/PDF limits and OpenAI's computer-use capabilities signal multimodal search experiences that go beyond text-based queries

## Recommended Actions
1. **Evaluate agent capabilities roadmap**: Consider how Perplexity can evolve from answer engine to task completion platform, particularly for research-intensive workflows where citations provide unique value
2. **Accelerate enterprise partnerships**: With Microsoft, OpenAI, and Anthropic all pursuing enterprise integration strategies, Perplexity should strengthen partnerships with productivity tools and knowledge management platforms
3. **Monitor pricing pressure**: Anthropic's elimination of context surcharges and OpenAI's competitive search pricing ($10/1k calls) may require subscription model adjustments or usage-based tiers to maintain competitiveness

---

## 6. Knowledge Sources Used

| Source | Type | Purpose |
|---|---|---|
| **System prompt (competitive context)** | Encoded assumptions | Defines Perplexity's strategic position, its core product (answer engine, citations, Pro Search), and the 4 signal categories that matter for competitive monitoring. This acts as the agent's "institutional knowledge." |
| **Competitor list and monitoring scope** | Encoded in prompt | Google (AI Overviews), OpenAI (SearchGPT), Microsoft (Copilot), Anthropic — chosen because they represent the four most direct threats to Perplexity's AI search positioning across different vectors (incumbent search, AI-native search, enterprise productivity, foundation model provider). |
| **Signal vs. noise filtering rules** | Encoded in prompt | Explicit rules for what counts as strategically relevant vs. background noise, calibrated to Perplexity's competitive concerns (e.g., citation behavior changes are signal; generic AI news is noise). |
| **Tavily web search (real-time)** | Live data source | Provides the raw intelligence — news articles, blog posts, press releases, job postings — that the agent synthesizes. No persistent historical database; each run starts fresh with current web data. |

The agent does **not** maintain a persistent knowledge base or historical competitor database. Each weekly run is independent, relying on the 30-day recency filter in Tavily to capture the relevant window. This is a deliberate design choice: it keeps the system simple and avoids stale data compounding over time. Historical context accumulates in the Notion page as weekly reports stack chronologically.

## 7. Tools the Agent Has Access To

### `web_search`

| Attribute | Detail |
|---|---|
| **What it does** | Searches the web via Tavily API with `advanced` search depth, returning up to 5 results per query. Each result includes title, URL, and content snippet. Supports a `days_back` parameter to filter by recency (default: 30 days). |
| **When it is used** | The agent calls this tool 6-8 times per run — typically 1-2 targeted queries per competitor (e.g., `"Google AI Overviews product update March 2026"`), plus 1-2 cross-competitor queries for hiring or ecosystem signals. |
| **How the agent decides to use it** | The system prompt provides a search strategy template (`[Competitor] + [category] + [current month]`), but the agent has autonomy to adapt queries based on initial results. If early searches reveal a major event, the agent may search for follow-up details rather than mechanically completing all template queries. |
| **Known failure modes** | (1) Tavily occasionally returns results outside the requested date range, requiring the agent to filter by reading content. (2) For very recent events (<24 hours), Tavily may not yet have indexed relevant articles. (3) Job posting searches often return aggregator pages rather than primary sources, reducing signal quality for the Talent & Hiring category. (4) The free tier is limited to 1,000 searches/month — at ~8 searches per weekly run, this provides ~125 weeks of runway, but concurrent use with other projects could exhaust the quota. |

The agent has only one tool. This is intentional — adding more tools (e.g., a dedicated job board scraper, an RSS monitor, a social media API) would increase coverage but also increase complexity, cost, and failure surface area. For a weekly cadence monitoring 4 competitors, a single high-quality web search tool provides sufficient coverage.

## 8. What the Agent Does Well

1. **Signal-to-noise filtering is genuinely useful.** The agent consistently distinguishes between material competitive developments (a new product launch, a pricing change, a major partnership) and background noise (opinion pieces, speculation, generic AI coverage). In the March 30 run, it correctly identified Google's AI Overviews ad integration as a high-threat signal while ignoring several generic "AI is changing search" articles that appeared in search results.

2. **Structured output reduces cognitive load.** The threat-level assignments (High/Medium/Low) and one-sentence key signals mean a Head of Product can scan all four competitors in under 30 seconds without reading the full report. The Toggle Heading 2 format in Notion means historical reports don't clutter the page.

3. **The agent's search strategy is efficient.** By limiting to 3-4 queries per competitor and using targeted `[Company] + [category] + [month]` patterns, the agent avoids the common failure mode of over-searching (which wastes API calls and increases noise). A typical run uses 6-8 Tavily searches — well within free tier limits and fast enough to complete in under 2 minutes.

4. **Recommended actions are specific and grounded.** Rather than generic advice ("stay competitive"), the agent produces recommendations tied to specific findings (e.g., "monitor pricing pressure from Anthropic's elimination of context surcharges"). This is because the prompt explicitly requires recommendations to be "based on this week's findings."

5. **The system is operationally simple.** Four files, two API keys, one scheduled task. No database, no vector store, no multi-agent framework. This means it actually runs reliably every Monday without maintenance — unlike more complex systems that tend to break silently.

## 9. Where the Agent Fails

### Failure 1: Job posting intelligence is shallow

The Talent & Hiring category consistently produces the weakest intelligence. When searching for `"[Competitor] job postings AI search"`, Tavily returns job aggregator pages (LinkedIn listings, Indeed summaries) rather than the kind of structured job board data that would reveal strategic hiring patterns. The agent ends up reporting surface-level observations like "OpenAI is hiring 3,500+ employees" rather than the more valuable signal of *what specific roles* indicate a strategic pivot.

**What I had to fix:** I considered adding a dedicated job board scraper (e.g., via Apify) but decided the added complexity wasn't worth it for a weekly cadence. Instead, I adjusted the prompt to frame hiring signals as one of four categories rather than a primary focus, and accepted that this category would be the weakest.

### Failure 2: Windows encoding broke emoji output

The first run crashed immediately with a `UnicodeEncodeError` because Windows' default `cp1252` encoding can't handle the emoji characters (magnifying glass, colored circles) in the print statements. This is a platform-specific failure that wouldn't occur on macOS or Linux.

**Fix:** Added `sys.stdout.reconfigure(encoding="utf-8")` at the top of `agent.py`.

### Failure 3: The agent sometimes front-loads reasoning text before the report

In early runs, the agent would output a paragraph of "thinking out loud" text (e.g., "Now I have comprehensive intelligence on all four competitors. Let me compile the structured report:") before the actual Markdown report. This preamble text gets saved into the output file, polluting the clean report format.

**What I had to fix:** This is a known behavior with Claude when using tool results — the model sometimes narrates its reasoning before producing structured output. The prompt was adjusted to emphasize "Produce a structured Markdown report" as the direct output instruction, which reduced but did not fully eliminate the preamble. A production system would strip non-Markdown content from the output programmatically.

### Failure 4: No deduplication across weeks

Because each run is independent (no persistent state), the agent has no awareness of what it reported last week. If a competitor's biggest news persists for multiple weeks (e.g., a major product launch gets covered for 3-4 weeks), the agent will report it as "new" each time. A production system would need a simple deduplication layer — even just comparing this week's key signals against last week's stored report.

### Failure 5: `.env` file format sensitivity

The initial `.env` file was created with labels on separate lines ("Anthropic Key" / "sk-ant-...") instead of the required `KEY=value` format. `python-dotenv` silently failed to parse it, causing the Tavily client to throw a `MissingAPIKeyError`. The error message didn't indicate that the `.env` file existed but was malformed — it just said "no API key provided."

**Fix:** Reformatted the `.env` file to use proper `KEY=value` syntax. This is a usability issue — the system should validate `.env` format on startup and provide a clear error message.
