# Berkeley Optometry Clinic — Voice Scheduling Agent

## Overview

An AI voice agent that handles inbound phone calls for Berkeley Optometry Clinic. The agent (Maya) can schedule, reschedule, and cancel appointments through natural phone conversation. Built with Claude as the reasoning engine, OpenAI Whisper for speech-to-text, and OpenAI TTS for text-to-speech.

## Architecture

```
Caller (phone / mic / browser)
        │
        ▼
   ┌─────────┐     ┌──────────────┐     ┌─────────────┐
   │ Audio In │────▶│ OpenAI       │────▶│ Claude API  │
   │ (mic/    │     │ Whisper STT  │     │ (reasoning  │
   │  Twilio) │     └──────────────┘     │  + tools)   │
   └─────────┘                           └──────┬──────┘
                                                │
                                         Tool calls
                                                │
                              ┌─────────────────┼─────────────────┐
                              │           │           │           │
                        ┌─────▼──┐  ┌────▼───┐  ┌───▼────┐ ┌───▼─────┐
                        │Calendar│  │Booking │  │Lookup/ │ │Escalate │
                        │ Check  │  │ Create │  │Cancel  │ │ /End    │
                        └────────┘  └────────┘  └────────┘ └─────────┘
                                                │
                                         ┌──────▼──────┐
                                         │ OpenAI TTS  │────▶ Speaker / Twilio
                                         │ (streaming) │
                                         └─────────────┘
```

## Tech Stack

| Layer | Provider | Model/Service | Cost | Purpose |
|-------|----------|---------------|------|---------|
| **Reasoning** | Anthropic | `claude-haiku-4-5` | $0.80/$4 per 1M tokens | Conversation logic, tool use, call flow |
| **Speech-to-Text** | OpenAI | `whisper-1` | $0.006 per 1M tokens | Transcribe caller's voice to text |
| **Text-to-Speech** | OpenAI | `gpt-4o-mini-tts` (nova voice) | $0.006 per 1M tokens | Maya's voice with tone instructions |
| **Calendar** | Local | `calendar_sim.py` (JSON) | Free | Simulated availability, booking, rescheduling |
| **Audio I/O** | Local | `sounddevice` (PCM) | Free | Mic recording + speaker playback |
| **Transcripts** | Local | Markdown files | Free | Saved to `output/` after each call |

**Estimated cost per test call (~10 turns): ~$0.004**

## Agent Identity

**Name:** Maya
**Role:** Appointment scheduling assistant
**Tone:** Warm, calm, professional. Trained medical receptionist — never robotic, never overly casual.
**Constraint:** 2-3 sentences max per turn (this is a phone call, not a chat).

---

## System Design

### Information Required Before Booking

| Field | Required | Validation |
|-------|----------|------------|
| Full name (first + last) | Yes | Ask to spell if unclear |
| Phone number | Yes | 10 digits, read back for confirmation |
| Appointment type | Yes | New patient (60 min) or follow-up (30 min) |
| Preferred date + time | Yes | Must be within 1-30 day booking window |
| Backup date/time | Nice-to-have | Asked if first choice unavailable |

**NOT collected** (HIPAA boundary): DOB, insurance, symptoms, reason for visit, medical history.

### Calendar Rules

```
Clinic hours:       Monday-Friday, 9:00 AM - 5:00 PM Pacific
Booking window:     1-30 days out from today
Slot granularity:   30-minute blocks
Lunch block:        12:00 PM - 1:00 PM daily (unavailable)
Last new patient:   4:00 PM (needs 60 min + 15 min buffer)
Last follow-up:     4:30 PM (needs 30 min)
Double-booking:     Not allowed
Holidays:           Configurable list
```

### Appointment Duration

| Type | Duration | Buffer After |
|------|----------|-------------|
| New patient | 60 min (2 slots) | 15 min (paperwork) |
| Follow-up | 30 min (1 slot) | 0 min |

### Handling Conflicting/Ambiguous Time Preferences

| Scenario | Agent Behavior |
|----------|---------------|
| Preferred slot taken | Offer 2 closest alternatives from same day, then adjacent days |
| Outside clinic hours | "We're open Monday through Friday, nine to five. Would [nearest weekday] work?" |
| Vague preference ("next week, mornings") | Pick 2-3 morning slots spread across the week |
| Beyond booking window (>30 days) | "I can book up to 30 days out. The latest I have is [date]." |
| Calendar fully booked that week | "That week is fully booked. The earliest I have is [slot]." |
| Two preferences given ("Tuesday or Thursday") | Check both, present best option from each |

### Rescheduling & Cancellation

| Action | Identity Check | Process |
|--------|---------------|---------|
| Reschedule | Name + phone OR confirmation ID | Look up -> cancel old -> book new |
| Cancel | Name + phone OR confirmation ID | Look up -> confirm details -> cancel -> offer rebook |
| No match found | — | "I'm not finding that appointment. Could you double-check?" -> 2 attempts then escalate |

### Urgent Cases — Immediate Escalation

| Trigger | Reason |
|---------|--------|
| Eye emergency, sudden vision loss, pain, injury | Clinical — Maya not qualified |
| Caller distressed, crying, raised voice | Emotional — needs a human |
| Asks for specific doctor/staff by name | Relationship — can't route internally |
| Complaint about previous visit | Sensitive — needs human judgment |
| 2 failed clarification attempts | UX — Maya is stuck |
| Persistent out-of-scope request after redirect | Needs human authority |

### Edge Cases

| Edge Case | Handling |
|-----------|---------|
| Caller hangs up mid-booking | Save partial transcript, mark "abandoned" |
| Returning caller (name+phone match) | Mention existing upcoming appointment before double-booking |
| Wants multiple appointments | Book one at a time, offer next after first completes |
| Agent stuck in tool loop | Max 5 tool calls per turn, then surface error |
| STT returns gibberish | Count consecutive unclear turns — escalate after 2 |
| Max call duration | 5 minutes — after that, offer to call back or escalate |

---

## Call Flow

```
1. Greeting
   Maya: "Thank you for calling Berkeley Optometry Clinic.
          This is Maya, your scheduling assistant. How can I help you today?"

2. Identify Intent (1 exchange)
   |-- Schedule new appointment
   |-- Reschedule existing
   |-- Cancel existing
   |-- Availability question
   +-- Out of scope -> redirect or escalate

3. Collect Information (2 fields at a time max)
   |-- Name + appointment type
   +-- Phone + preferred date/time

4. Check Availability (tool call)
   |-- Available -> confirm details
   +-- Unavailable -> offer 2 alternatives

5. Confirm Before Booking
   "Just to confirm — [name], [type] appointment on [day] at [time]. Is that right?"

6. Book + Confirm (tool calls)
   |-- book_appointment -> get confirmation ID
   +-- send_confirmation -> SMS to caller

7. Goodbye
   "You're all set, [name]. Your confirmation number is [ID].
    We'll see you on [date]. Have a great day!"
   +-- end_call
```

---

## Tools (7)

| Tool | Purpose | When Used |
|------|---------|-----------|
| `check_availability` | Find open slots by date/time/type | Before offering any times |
| `book_appointment` | Create appointment | After caller verbally confirms |
| `lookup_appointment` | Find existing appointment | For reschedule/cancel flows |
| `cancel_appointment` | Cancel by confirmation ID | After confirming with caller |
| `send_confirmation` | Send SMS confirmation | After booking |
| `escalate_to_human` | Transfer to human staff | Emergencies, complaints, stuck |
| `end_call` | End the call | After action completed + goodbye |

---

## File Structure

```
berkeley-optometry-voice/
|-- main.py              # Entry point — voice loop
|-- conversation.py      # Claude API manager with tool-use loop
|-- prompt.py            # System prompt + 7 tool schemas
|-- calendar_sim.py      # Simulated calendar (Phase 2a)
|-- tools.py             # Tool dispatcher
|-- audio.py             # Mic recording + speaker playback
|-- stt.py               # OpenAI Whisper speech-to-text
|-- tts.py               # OpenAI TTS text-to-speech
|-- transcript.py        # Markdown transcript recorder
|-- requirements.txt     # Python dependencies
|-- .env                 # API keys (not committed)
|-- calendar_data.json   # Simulated calendar state (auto-generated)
+-- output/              # Call transcripts saved here
```

---

## Phase Roadmap

### Phase 1 — Core Agent Logic (COMPLETE)
- [x] Voice loop (mic -> STT -> Claude -> TTS -> speaker)
- [x] System prompt with persona, call flow, escalation rules
- [x] Tool-use conversation loop
- [x] Transcript recording

### Phase 2a — Simulated Calendar + Voice Swap (COMPLETE)
- [x] Swap STT to OpenAI Whisper
- [x] Swap TTS to OpenAI TTS (gpt-4o-mini-tts with voice instructions)
- [x] Realistic simulated calendar with real time logic
- [x] Appointment durations and conflict detection
- [x] Rescheduling and cancellation flows (lookup + cancel tools)
- [x] Returning patient detection
- [x] Updated system prompt with all rules
- [x] LLM optimized to claude-haiku-4-5 (5x cheaper, 2x faster)

### Phase 2b — Real Calendar Integration
- [ ] Google Calendar API for availability + booking
- [ ] OAuth setup and token management
- [ ] Timezone handling (Pacific)
- [ ] Clinic hours / holiday enforcement
- [ ] Same tool interface — only backend changes

### Phase 3 — Telephony (Twilio)
- [ ] Inbound call handling via Twilio Voice webhooks
- [ ] Replace local mic/speaker with Twilio media streams
- [ ] SMS confirmations via Twilio Messaging
- [ ] Call recording and compliance

### Phase 4 — Persistence & Admin
- [ ] Patient records database
- [ ] Appointment persistence (Notion or Postgres)
- [ ] Admin dashboard for clinic staff
- [ ] Daily appointment summary

### Phase 5 — Production
- [ ] Deploy as FastAPI server
- [ ] Latency optimization (streaming TTS, parallel STT)
- [ ] Logging, monitoring, cost tracking
- [ ] Spanish language support

---

## How to Test

### Option 1: Local (laptop mic + speakers)

Requires: Python 3.10+, working microphone, API keys.

```bash
cd berkeley-optometry-voice/
pip install -r requirements.txt

# Create .env file with:
# OPENAI_API_KEY=sk-...
# ANTHROPIC_API_KEY=sk-ant-...

python main.py
```

Speak into your mic when you see the listening indicator. Press Ctrl+C to end.

### Option 2: Team testing (future — web interface)

A browser-based interface using WebRTC for audio would let anyone test without local setup. This is planned for Phase 3+.

### Option 3: Phone testing (future — Twilio)

A real phone number that anyone can call. Planned for Phase 3.

---

## Test Scenarios

Run these to validate the agent:

1. **Happy path** — Schedule a new patient appointment for next Monday morning
2. **Slot conflict** — Try to book a time that's already taken
3. **Vague time** — Say "sometime next week, maybe afternoon?"
4. **Reschedule** — Book, then call back to reschedule
5. **Cancel** — Book, then call back to cancel
6. **Escalation** — Say "I'm having sudden vision loss" or "I need to speak to Dr. Smith"
7. **Out of scope** — Ask about pricing or insurance
8. **Weekend request** — Ask for a Saturday appointment
9. **Returning patient** — Book twice with the same name and phone
10. **Silence** — Say nothing and see if Maya prompts you
