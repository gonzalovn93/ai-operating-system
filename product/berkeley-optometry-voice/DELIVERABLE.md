# Submission

Repository: https://github.com/gonzalovn93/ai-operating-system/tree/main/product/berkeley-optometry-voice
Source code: `C:\Users\gonza\berkeley-optometry-voice\`

## Deployment

The current assignment runs locally via `python main.py` (terminal with mic/speaker) or `python server.py` (browser-based UI at localhost:8000). The system uses OpenAI for voice I/O (Whisper STT + TTS) and Anthropic Claude for conversational reasoning. The calendar is a realistic simulation with real time logic, conflict detection, and JSON persistence. No external calendar or telephony integration is required to test the full agent flow.

## 1. System Explanation

This system is a voice appointment scheduling agent for Berkeley Optometry Clinic. Its purpose is to handle inbound phone calls — scheduling, rescheduling, and cancelling appointments — while detecting when escalation to a human is required.

Controller / orchestration policy:

- The controller executes a fixed voice loop: capture audio, transcribe (STT), reason and act (Claude + tools), synthesize response (TTS), play audio.
- If STT returns empty or unintelligible text, the system prompts the caller to repeat without invoking the reasoning model. After 2 consecutive failures, escalation is triggered.
- If a tool call fails (e.g., slot no longer available during booking), the error is returned to the model as a tool result, and the model adapts its response to the caller.
- If the model enters a tool-use loop (more than 5 tool calls in a single turn), the system breaks the loop and surfaces a graceful error.
- If the caller goes silent for 5 seconds, the system prompts "Are you still there?" If no speech is detected after 2 prompts, the call is ended and the transcript is saved with outcome "abandoned."
- The system never collects health information, insurance details, or medical history. These boundaries are enforced in the system prompt, not in application code.

Operational note:

- A typical scheduling call is 6-10 conversational turns and completes in under 2 minutes. Estimated cost per call is ~$0.004 using Claude Haiku 4.5. Transcripts are saved as Markdown files in `output/` after each call.

The end-to-end workflow is:

1. **Call initiation**
   - The system plays Maya's greeting: "Thank you for calling Berkeley Optometry Clinic. This is Maya, your scheduling assistant. How can I help you today?"
   - The conversation manager is initialized with the system prompt and 7 tool schemas.

2. **Audio capture and transcription**
   - The system records from the caller's microphone (or browser audio) until 1.5 seconds of silence is detected.
   - The audio is converted to WAV format and sent to OpenAI Whisper (`whisper-1`) for transcription.
   - If transcription returns empty, Maya asks the caller to repeat.

3. **Intent identification**
   - The transcribed text is sent to Claude Haiku 4.5 as a user turn in the conversation.
   - The model identifies the caller's intent: schedule, reschedule, cancel, availability inquiry, or out-of-scope.
   - Intent identification happens within the first 1-2 exchanges.

4. **Information collection**
   - For scheduling: the model collects full name, phone number, appointment type (new patient or follow-up), and preferred date/time.
   - The model collects at most 2 fields per turn to keep the conversation natural.
   - The model confirms each piece of information by reading it back.
   - For rescheduling/cancellation: the model first uses `lookup_appointment` to find the existing appointment by name + phone or confirmation ID.

5. **Availability check (tool call)**
   - The model calls `check_availability` with the preferred date, time, and appointment type.
   - The calendar simulation generates real 30-minute slots based on:
     - Clinic hours: Monday-Friday, 9 AM - 5 PM
     - Lunch block: 12 PM - 1 PM (unavailable)
     - Appointment durations: new patient = 60 min (2 slots + 1 buffer), follow-up = 30 min (1 slot)
     - Booking window: 1-30 days out
     - Conflict detection against existing bookings
   - The tool returns up to 4 available slots.
   - If no slots match the preference, the system searches up to 8 days ahead and returns the nearest alternatives.

6. **Confirmation and booking**
   - The model reads back all details: name, appointment type, date, time.
   - The model asks the caller to verbally confirm.
   - Only after confirmation does the model call `book_appointment`.
   - The booking tool verifies the slot is still available (race condition guard), creates the appointment, and returns a confirmation ID.
   - If the caller is a returning patient (name + phone match an existing upcoming appointment), the tool flags this in the response.

7. **Confirmation delivery**
   - The model offers to send a confirmation message.
   - If accepted, the model calls `send_confirmation` with patient name, phone, and appointment summary.
   - In Phase 2a, this prints a mock SMS to the console. In Phase 3, this will use Twilio.

8. **Escalation detection**
   - The model monitors for escalation triggers throughout the conversation:
     - Eye emergency, sudden vision loss, pain, or injury
     - Caller distress (crying, raised voice)
     - Request for a specific doctor or staff member by name
     - Complaint about a previous clinical visit
     - 2 failed clarification attempts
     - Persistent out-of-scope request after initial redirect
   - When triggered, Maya says: "I want to make sure you get the right help. Let me connect you with a member of our team right now."
   - The model immediately calls `escalate_to_human` with a reason string.

9. **Call termination**
   - The model calls `end_call` only after: the action is completed (booked, cancelled, or rescheduled), confirmation has been offered, and goodbye has been said by name.
   - The transcript recorder saves the full conversation to `output/transcript_YYYYMMDD_HHMMSS.md` with token usage and outcome.

10. **Calendar state persistence**
    - All appointments are stored in `calendar_data.json` with start/end times, patient info, and cancellation status.
    - This file persists across calls, so a second caller can see that earlier bookings have consumed slots.
    - Cancelled appointments are soft-deleted (flagged, not removed) so the slot becomes available again.

Simple pipeline view:

```text
Caller Audio -> Whisper STT -> Claude Haiku 4.5 (reasoning + tools)
                                       |
                    +------------------+------------------+
                    |          |           |               |
              check_avail  book_appt  lookup/cancel  escalate/end
                    |          |           |               |
                    +----------+-----------+---------------+
                                       |
                               OpenAI TTS (Maya's voice) -> Caller Speaker
```

## 2. Task Classification: Rule-Based vs Agent-Based

| Task | Classification | Why |
| --- | --- | --- |
| Audio capture and silence detection | Rule-based | This is signal processing with fixed thresholds (RMS volume, silence duration). No interpretation needed. |
| Speech-to-text transcription | API-based (Whisper) | Whisper is a specialized model, not an agent. It converts audio to text with no reasoning. |
| Intent identification | Agent-based | The caller's intent can be expressed in countless ways. The model must interpret natural language to classify the intent. |
| Information extraction (name, phone, date) | Agent-based | Callers express information in varied, informal ways ("next Monday maybe morning?"). The model must parse and normalize this. |
| Conversational flow management | Agent-based | The model must decide what to ask next, when to confirm, and when to proceed — adapting to each caller's pace and style. |
| Slot generation (30-min blocks, clinic hours) | Rule-based | Slots are generated from fixed rules: weekdays only, 9-5, no lunch, 30-min granularity. No judgment needed. |
| Conflict detection | Rule-based | Checking whether a time range overlaps an existing booking is arithmetic, not interpretation. |
| Duration calculation by type | Rule-based | New patient = 60 min + 15 min buffer, follow-up = 30 min. Fixed business rules. |
| Booking window enforcement | Rule-based | 1-30 days out from today. A date comparison, not a judgment call. |
| Appointment booking | Rule-based | Writing a record to the calendar is execution logic. The agent decides *what* to book; the tool executes it. |
| Returning patient detection | Rule-based | Name + phone string matching against existing records. Deterministic. |
| Appointment lookup | Rule-based | Searching by confirmation ID or name + phone is a database query, not reasoning. |
| Appointment cancellation | Rule-based | Soft-deleting a record by confirmation ID. Execution logic. |
| Confirmation message assembly | Agent-based | The model composes a natural-language summary tailored to what was booked. Templates would sound robotic. |
| Escalation detection | Agent-based | Detecting distress, urgency, or out-of-scope requests requires semantic understanding. Keywords alone would miss subtle cues. |
| Text-to-speech synthesis | API-based (OpenAI TTS) | TTS is a specialized model. The voice instructions ("warm, professional") are fixed, not agent-controlled. |
| Transcript recording | Rule-based | Appending speaker + text + timestamp to a list. No interpretation. |
| Date/time parsing | Rule-based | Converting "next Monday" or "April 10" to a datetime is deterministic string parsing with known formats. |
| Call termination decision | Agent-based | The model must judge whether the conversation has reached a natural conclusion before ending. |
| Audio playback | Rule-based | Playing PCM bytes through the speaker is hardware I/O. No reasoning. |

### Detailed Task-by-Task Justification

**Audio capture and silence detection**
This is rule-based because the system uses fixed RMS thresholds (0.02) and durations (1.5 seconds of silence) to determine when the caller has stopped speaking. An agent would add latency and cost to a task that is solved by simple signal processing.

**Speech-to-text transcription**
Whisper is used as a tool, not as an agent. It receives audio bytes and returns text. It does not reason about context, manage state, or make decisions. The system treats its output as raw input for the reasoning layer.

**Intent identification**
This is agent-based because callers express intent in unpredictable ways: "I need to see someone," "Can I move my appointment?," "What times do you have Thursday?" Deterministic keyword matching would be brittle and fail on paraphrases, indirect requests, or compound intents.

**Information extraction**
This is agent-based because callers provide information in varied formats: "My name's Sarah, S-A-R-A-H, last name Chen," "Maybe two-ish on Thursday?," "Five one zero, five five five, twelve thirty-four." The model must normalize these into structured fields while maintaining conversational flow.

**Conversational flow management**
This is agent-based because the model must dynamically decide: which field to collect next, whether to ask one or two questions, when to confirm what it heard, and when to proceed to booking. A state machine could approximate this but would feel robotic and fail on caller deviations.

**Slot generation**
This is rule-based because available slots are generated from fixed business rules. The clinic hours, lunch block, and slot granularity are constants. An agent would be wasteful and could introduce inconsistencies.

**Conflict detection**
This is rule-based because overlap detection is a range comparison: does the proposed appointment's [start, end] intersect any existing booking's [start, end]? This is arithmetic, not judgment.

**Duration calculation by type**
This is rule-based because appointment durations are fixed business rules: 60 minutes for new patients (plus 15-minute buffer), 30 minutes for follow-ups. An agent making this determination would introduce unnecessary variability.

**Booking window enforcement**
This is rule-based because checking whether a date falls between tomorrow and 30 days from now is a date comparison. No semantic reasoning is needed.

**Appointment booking**
This is rule-based because once the agent has determined *what* to book, the actual record creation is execution logic: assign a confirmation ID, write the record, return the result.

**Returning patient detection**
This is rule-based because matching a name and phone number against existing records is deterministic string comparison. The result is binary: match or no match.

**Escalation detection**
This is agent-based because escalation triggers include subjective signals: distress, frustration, urgency about symptoms. Keyword matching ("emergency," "pain") would catch some cases but miss others ("I can barely see," "this is really upsetting"). The model can interpret tone and context.

**Confirmation message assembly**
This is agent-based because the confirmation must sound natural and include the right level of detail. A template like "Your appointment is on {date} at {time}" works for SMS but sounds flat when spoken aloud. The model adapts phrasing to the conversation context.

**Date/time parsing**
This is rule-based because the parsing logic handles known formats ("next Monday," "April 10," "tomorrow") through deterministic string matching and date arithmetic. The model extracts the date expression; the tool normalizes it.

**Call termination decision**
This is agent-based because the model must assess whether the booking is confirmed, the confirmation was offered, and the caller seems satisfied before ending. Premature termination would be a bad experience; the model must read conversational cues.

## 3. Why All Tasks Were Not Assigned to the Agent

### Risks of Full Agent Control

If the model controlled slot generation, conflict detection, and booking, a single hallucinated time could result in a double-booked appointment. The calendar logic requires deterministic guarantees that an LLM cannot provide.

### Cost Implications

The current design sends only conversational turns to Claude. If slot generation, date parsing, conflict detection, and calendar management were also handled by the model, each turn would require a much larger prompt with the full calendar state. For a 10-turn call, this would roughly triple token usage from ~1,250 to ~3,750 tokens per call.

### Latency Implications

Voice agents are latency-sensitive — callers expect responses within 1-2 seconds. Each additional model call adds 500-1500ms. By keeping calendar operations deterministic and local, the system avoids round-trip latency for tasks that execute in microseconds in code.

### Error Propagation Risks

If the model miscalculated appointment duration (e.g., treating a 60-minute new patient appointment as 30 minutes), it would create a conflict that the deterministic system would have prevented. Isolating calendar logic from the reasoning layer contains errors to their respective domains.

### Auditability

Healthcare scheduling, even at the receptionist level, benefits from clear audit trails. Deterministic slot generation and booking means every appointment can be traced back to explicit rules: this slot was offered because it fell within clinic hours, didn't conflict with existing bookings, and matched the requested appointment duration. The model's contribution — interpreting the caller's preferences — is captured in the transcript.

## 4. Estimated Token Calculation if All Tasks Were Agent-Based

Assume the system handles **50 calls per day**, which would be a reasonable volume for a small optometry clinic.

If every task were handled by the agent — including slot generation, conflict detection, date parsing, booking, and cancellation — each turn would require:

Estimated tokens per call in an all-agent design (10 turns average):

- System prompt with full calendar rules, slot logic, and all business rules: **~800 tokens**
- Full calendar state (all existing appointments) passed each turn: **~400 tokens** (grows with bookings)
- Per-turn conversation context (cumulative): **~150 tokens avg**
- Per-turn model reasoning + tool simulation: **~200 tokens avg**
- Total input per call: **~800 + (10 turns x (400 + 150)) = ~6,300 tokens**
- Total output per call: **~10 turns x 200 = ~2,000 tokens**
- **Total per call: ~8,300 tokens**

Assumptions:

- Model: `claude-haiku-4-5` ($0.80/$4.00 per 1M tokens input/output)
- 50 calls/day
- 10 turns average per call
- No retries included
- Calendar state grows linearly with bookings

Estimated daily total:

- `50 calls x 8,300 tokens = 415,000 tokens/day`

Estimated monthly total at 30 days:

- `415,000 x 30 = 12,450,000 tokens/month`

Estimated monthly cost:

- Input: ~6,300 x 50 x 30 = 9,450,000 tokens x $0.80/1M = **$7.56**
- Output: ~2,000 x 50 x 30 = 3,000,000 tokens x $4.00/1M = **$12.00**
- **Total: ~$19.56/month**

This design would also be less reliable because the model would be responsible for arithmetic and state management tasks it is not optimized for.

## 5. Estimated Token Calculation for Your Actual Design

In the actual architecture, deterministic code handles:
- Slot generation from clinic rules
- Conflict detection via range comparison
- Date/time parsing
- Booking record creation
- Calendar state management
- Duration and buffer calculation
- Returning patient detection

The model handles only:
- Conversational reasoning (intent, information extraction, flow)
- Tool invocation decisions
- Natural language responses

Estimated tokens per call in the actual design (10 turns average):

- System prompt with persona, call flow rules, and tool schemas: **~650 tokens**
- Per-turn conversation context (cumulative): **~150 tokens avg**
- Tool results returned to model (structured JSON, compact): **~80 tokens avg per tool call, ~3 tool calls per call = ~240 total**
- Total input per call: **~650 + (10 x 150) + 240 = ~2,390 tokens**
- Per-turn model output (2-3 sentences + occasional tool call): **~80 tokens avg**
- Total output per call: **~10 x 80 = ~800 tokens**
- **Total per call: ~3,190 tokens**

Why these estimates are reasonable:

- The **2,390 input tokens** are lower because the model never receives calendar state, slot lists, or booking records — only compact tool results.
- The **800 output tokens** reflect Maya's constraint of 2-3 sentences per turn.
- Tool calls add minimal tokens because the schemas are narrow and results are structured JSON.

Estimated daily total for the actual design:

- `50 calls x 3,190 tokens = 159,500 tokens/day`

Estimated monthly total at 30 days:

- `159,500 x 30 = 4,785,000 tokens/month`

Estimated monthly cost:

- Input: ~2,390 x 50 x 30 = 3,585,000 tokens x $0.80/1M = **$2.87**
- Output: ~800 x 50 x 30 = 1,200,000 tokens x $4.00/1M = **$4.80**
- **Total: ~$7.67/month**

Add voice costs:

- Whisper STT: ~10 seconds of audio per turn x 10 turns x 50 calls = ~83 minutes/day. At $0.006/min = **~$0.50/day = ~$15/month**
- OpenAI TTS: ~50 words per response x 10 turns x 50 calls = ~25,000 words/day. At ~750 tokens/1000 words = ~18,750 tokens/day x 30 = 562,500 tokens/month x $0.015/1M = **~$0.25/month**

**Total estimated monthly cost (50 calls/day): ~$23/month**

Comparison:

| Design | Tokens/call | Tokens/month (50 calls/day) | LLM cost/month | Reduction |
| --- | --- | --- | --- | --- |
| All-agent | ~8,300 | ~12,450,000 | ~$19.56 | — |
| Actual (hybrid) | ~3,190 | ~4,785,000 | ~$7.67 | **61.6%** |

Scaling view:

| Calls/day | Actual design tokens/day | Estimated monthly LLM cost | Total with voice |
| --- | --- | --- | --- |
| 10 | 31,900 | ~$1.53 | ~$5 |
| 50 | 159,500 | ~$7.67 | ~$23 |
| 100 | 319,000 | ~$15.34 | ~$46 |
| 500 | 1,595,000 | ~$76.70 | ~$230 |

The hybrid architecture keeps costs well below $50/month for a typical small clinic volume, while the all-agent design would cost roughly 2.5x more at every scale point.

## 6. Tech Stack

| Layer | Provider | Model/Service | Cost | Purpose |
|-------|----------|---------------|------|---------|
| Reasoning | Anthropic | `claude-haiku-4-5` | $0.80/$4 per 1M tokens | Conversation logic, tool use, call flow |
| Speech-to-Text | OpenAI | `whisper-1` | $0.006 per 1M tokens | Transcribe caller's voice to text |
| Text-to-Speech | OpenAI | `gpt-4o-mini-tts` (nova) | $0.006 per 1M tokens | Maya's voice with tone instructions |
| Calendar | Local | `calendar_sim.py` (JSON) | Free | Simulated availability, booking, rescheduling |
| Audio I/O | Local | `sounddevice` / browser WebRTC | Free | Mic recording + speaker playback |
| Transcripts | Local | Markdown files | Free | Saved to `output/` after each call |

## 7. Tools

| Tool | Type | Purpose | When Used |
|------|------|---------|-----------|
| `check_availability` | Calendar (deterministic) | Find open slots by date/time/type | Before offering any times to caller |
| `book_appointment` | Calendar (deterministic) | Create appointment with conflict guard | After caller verbally confirms details |
| `lookup_appointment` | Calendar (deterministic) | Find existing appointment | For reschedule/cancel flows |
| `cancel_appointment` | Calendar (deterministic) | Soft-delete by confirmation ID | After confirming with caller |
| `send_confirmation` | Communication (mock) | Send SMS confirmation | After successful booking |
| `escalate_to_human` | Workflow control | Transfer to human staff | Emergencies, complaints, stuck states |
| `end_call` | Workflow control | Terminate the call | After action completed + goodbye |

## 8. File Structure

```
berkeley-optometry-voice/
|-- main.py              # Entry point — terminal voice loop
|-- server.py            # FastAPI server — browser-based UI
|-- conversation.py      # Claude API manager with tool-use loop
|-- prompt.py            # System prompt + 7 tool schemas
|-- calendar_sim.py      # Simulated calendar with real time logic
|-- tools.py             # Tool dispatcher
|-- audio.py             # Mic recording + speaker playback
|-- stt.py               # OpenAI Whisper speech-to-text
|-- tts.py               # OpenAI TTS text-to-speech
|-- transcript.py        # Markdown transcript recorder
|-- requirements.txt     # Python dependencies
|-- .env                 # API keys (not committed)
|-- calendar_data.json   # Calendar state (auto-generated)
|-- templates/
|   +-- index.html       # Browser UI for testing
+-- output/              # Call transcripts saved here
```

## 9. Test Scenarios

| # | Scenario | What to Say | Expected Behavior |
|---|----------|-------------|-------------------|
| 1 | Happy path | "I'd like to schedule a new patient appointment for next Monday morning" | Collects name, phone, checks availability, confirms, books, sends confirmation |
| 2 | Slot conflict | Book a slot, then try to book the same slot again | Agent offers alternative times |
| 3 | Vague time | "Sometime next week, maybe afternoon?" | Agent offers 2-3 specific afternoon slots |
| 4 | Reschedule | "I need to reschedule my appointment" | Looks up by name+phone or ID, cancels old, books new |
| 5 | Cancel | "I need to cancel my appointment" | Looks up, confirms, cancels, offers to rebook |
| 6 | Urgent escalation | "I'm having sudden vision loss" | Immediate escalation to human |
| 7 | Staff request | "I need to speak to Dr. Smith" | Escalation — can't route internally |
| 8 | Out of scope | "How much does an eye exam cost?" | Redirects once, escalates if pressed |
| 9 | Weekend request | "Do you have anything Saturday?" | Informs Mon-Fri hours, offers nearest weekday |
| 10 | Returning patient | Book twice with same name and phone | Agent mentions existing upcoming appointment |
