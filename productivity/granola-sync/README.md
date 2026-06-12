# GranolaSync

**Type:** Automated Python Workflow
**Skill Domain:** LearningProductivity
**Command:** `python main.py --sync-all`

## What It Does

Syncs AI-enhanced meeting notes from [Granola](https://granola.ai) into the right Notion pages — automatically routed by folder, append-only, and idempotent. The meetings I have during the day show up as clean, structured notes under the correct project or class page, with zero copy-paste.

## How It Works

1. **Read:** Pulls meeting documents and folder membership from Granola's local cache
2. **Enrich:** Calls the Granola API to fetch the *AI-enhanced* notes panel (the cleaned-up summary, not the raw transcript)
3. **Route:** Maps each Granola folder to a destination Notion page via a routing table
4. **Convert:** Translates Granola's ProseMirror document model → Notion blocks (headings, lists, toggles, nested structure)
5. **Append:** Writes only new content using append-only Notion calls — never overwrites or deletes
6. **Track:** Records every synced doc ID in a local state ledger so re-runs are safe and idempotent

## Design Decisions

- **Why append-only?** Notes are a record, not a draft. The workflow only ever *adds* — it never issues an update or delete against Notion. If a sync runs twice, the state ledger prevents duplicates rather than relying on destructive reconciliation. Safer to operate, impossible to clobber hand-written notes.
- **Why a folder → page routing table?** Granola organizes meetings into folders (per class, per project). Notion organizes them as pages. A declarative routing map keeps the two in sync without hard-coding logic, so adding a new destination is a one-line change.
- **Why a dedicated ProseMirror converter?** Granola stores notes in ProseMirror's nested document model; Notion expects its own block schema. A standalone converter owns that structural mismatch — including Notion's "two levels of nesting per request" limit, which it handles via recursive deferred appends.
- **Why a local state ledger instead of querying Notion?** Reading back the entire destination page to diff content is slow and fragile. A small local ledger of synced doc IDs is O(1), survives across runs, and makes `--mark-synced` (acknowledge without writing) trivial for clean-slate setup.

## Architecture

```
GranolaSync/
├── main.py                # Orchestrator + CLI (dry-run, sync, sync-folder, mark-synced)
├── granola_reader.py      # Reads local cache + calls Granola API for AI-enhanced notes
├── prosemirror.py         # ProseMirror document-model parser
├── markdown_to_notion.py  # ProseMirror / markdown → Notion blocks
├── notion_writer.py       # Append-only Notion writes (handles the nesting limit)
└── state/synced.json      # Idempotency ledger of synced doc IDs
```

## Prompt File

→ [`prompt.md`](./prompt.md)
