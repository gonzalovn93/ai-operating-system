# PM Recruiting Strategist

**Type:** High-Context Agent (Layer 1)  
**Domain:** Pipeline strategy, company targeting, sequencing  

## What It Does

Designs and maintains the strategic layer of my recruiting process — which companies to target, how to prioritize, when to push vs. pause, and how to sequence outreach for maximum leverage.

This agent handles *strategy*, not execution. It doesn't write outreach messages or resumes. It decides where to aim and in what order.

## When I Use It

- When evaluating whether a company or role is worth pursuing
- When planning a recruiting wave (which companies, what sequence, how many touches)
- When reassessing strategy after new information (a rejection, an inbound, a timeline shift)
- When I need a go/no-go decision on spending time on an opportunity
- When comparing role types (Senior PM vs. AI PM vs. Strategy PM vs. Platform PM)

## Design Decisions

**Identity:** Thinks like a PM running recruiting as a product. Companies are segments. Outreach is a funnel. Pipeline health is a metric.

**Operating style:** Strategic, opinionated, structured. Forces tradeoffs. Pushes toward decisions, not deliberation.

**Key frameworks it uses:**
- Tier 1 / Tier 2 / Tier 3 company classification
- Fit scoring (0–10) across PM culture, product scope, narrative angle, and traction probability
- Risk-balanced portfolio (dream roles + strong base cases)
- Networking sequencing (who first, how to ladder toward referrals)

**Constraints:**
- Optimizes for long-term career leverage, not just getting *an* offer
- Avoids overextension — explicitly flags when I'm spread too thin
- Does not write messages (that's a different skill)

## Key Capabilities

- **Company evaluation:** For any company, produces a structured assessment — fit score, narrative angle, gaps to address, probability of traction, and recommended approach (network first vs. apply directly)
- **Pipeline design:** Weekly goals, action lists, status tracking, and decision checkpoints
- **Positioning strategy:** Which experiences to foreground for which company, when to lean into the founder narrative vs. enterprise PM narrative
- **Compensation analysis:** When offers arise, compares across dimensions including risk, liquidity, scope, and long-term trajectory

## Example Interaction

**Input:** "Should I pursue [Company X]? They have a PM role open but it's a platform team, not consumer."

**Output:** A structured assessment with fit score, the narrative angle I'd use, specific gaps I'd need to address, whether to network or apply first, and an explicit recommendation with reasoning.

## Prompt File

→ [`prompt.md`](./prompt.md)
