# GranolaSync — Workflow Prompt

## Purpose
Move AI-enhanced meeting notes out of Granola and into the right Notion page automatically — routed by folder, append-only, and safe to re-run.

## Core Functionality

### Input
- Granola local cache (meeting documents + folder membership)
- A folder → Notion-page routing table
- Optional: specific document IDs, or a single folder label to scope the run

### Processing
1. Discover unsynced documents (compare cache against the local state ledger)
2. Fetch each document's AI-enhanced notes panel from the Granola API
3. Resolve the destination Notion page from the document's folder
4. Convert the ProseMirror document → Notion blocks (preserving headings, lists, and nesting)
5. Append the new blocks to the destination page (append-only; never update/delete)
6. Record the document ID in the state ledger

### Output
- New, structured note blocks appended to the correct Notion page
- Updated `synced.json` state ledger (idempotency)
- Dry-run mode prints what *would* sync, grouped by folder, before any write

## Triggers
- "Sync my Granola notes"
- "Pass my meeting notes to Notion"
- "Sync the notes from [folder]"

## Design Notes
- **Append-only by contract** — the workflow has no update or delete path.
- **Idempotent** — re-running is a no-op for already-synced documents.
- **Routing is declarative** — destinations live in a config map, not in code.
