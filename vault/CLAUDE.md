# Obsidian vault operating rules

## Purpose
This vault is the central knowledge base for coding, research, decisions, writing drafts, and reusable technical understanding.

The goal is not to store everything.
The goal is to store useful knowledge in a structured way that stays clean, connected, and easy to navigate as projects grow.

This vault should form a usable knowledge graph through deliberate internal links.
Do not create isolated notes unless the note is intentionally temporary.

## Core behavior
- Save durable knowledge, not noise.
- Prefer clean, structured notes over raw transcript dumps.
- Before creating a new note, search for an existing relevant note and update it if appropriate.
- If unsure where something belongs, save it to Inbox.
- Do not reorganize large parts of the vault unless explicitly asked.
- Do not rename project folders or mass-edit the vault unless explicitly asked.
- Prefer updating an existing note over creating a near-duplicate.
- When creating or updating a note, always search for existing related notes first and add meaningful internal links so the vault remains navigable as a graph.

## Folder rules

### Allowed write targets
- `00 Inbox/AI Captures/`
- `00 Inbox/Session Summaries/`
- `01 Projects/*/Research/`
- `01 Projects/*/Decisions/`
- `01 Projects/*/Meetings/`
- `01 Projects/*/Snippets/`
- `01 Projects/*/Scratch/`
- `05 Writing/Ideas/`
- `05 Writing/Drafts/`
- `05 Writing/In Review/`
- `05 Writing/Ready to Publish/`
- `05 Writing/Published/`

### Protected folders
Do not write here unless explicitly instructed:
- `02 Concepts/`
- `03 Sources/`
- `04 Dashboards/`
- `90 Templates/`
- `99 Archive/`
- attachments folders
- media folders
- private or personal folders

## Default behavior
- If unsure where a note belongs, save it to `00 Inbox/AI Captures/`.
- If a note is incomplete but still worth saving, store it in Inbox rather than forcing it into a curated folder.
- Do not auto-promote notes into evergreen concepts.
- Do not create multiple notes for the same topic with slightly different names.
- Prefer one strong note over several weak notes.

## Project structure
Each project should have a home note at:

- `01 Projects/<Project Name>/<Project Name>.md`

Every project-specific note should link back to that home note in the `Related` section.

Example:
- `[[Project Alpha]]`

## Writing structure
Content meant for publishing later belongs in `05 Writing/`.

Use:
- `05 Writing/Ideas/` for rough article ideas and outlines
- `05 Writing/Drafts/` for active drafts
- `05 Writing/In Review/` for drafts being edited
- `05 Writing/Ready to Publish/` for nearly final pieces
- `05 Writing/Published/` for archived published versions with metadata and URLs

Do not store website-bound drafts in `01 Projects/` unless explicitly asked.

## Naming conventions

### Research notes
Format:
`YYYY-MM-DD topic.md`

### Decision notes
Format:
`YYYY-MM-DD decision title.md`

### Session summaries
Format:
`YYYY-MM-DD HHMMSS <Project Name> session.md`

### Snippet notes
Format:
`YYYY-MM-DD snippet title.md`

### Writing drafts
Format:
`YYYY-MM-DD article title.md`

### Concept notes
Use short, canonical titles.
Do not create several concept notes for the same idea with slightly different names.

## Required frontmatter
Every note must include frontmatter.

### Minimum required fields for project notes
- `type`
- `project`
- `created`

### Preferred fields when relevant
- `status`
- `updated`
- `source_type`
- `tags`

### Preferred fields for writing notes
- `type`
- `status`
- `publish_target`
- `slug`
- `created`
- `updated`

## Note types

### Research note
Use for:
- technical findings
- implementation notes
- design ideas
- comparisons
- extracted understanding
- debugging lessons
- tradeoff analysis

Required sections:
- `## Summary`
- `## Key points`
- `## Code or examples`
- `## Decisions implied`
- `## Open questions`
- `## Related`

### Decision note
Use for:
- architectural decisions
- tooling choices
- workflow choices
- implementation decisions worth preserving

Required sections:
- `## Context`
- `## Decision`
- `## Why`
- `## Tradeoffs`
- `## Follow up`
- `## Related`

### Session summary
Use for end-of-session capture.

Required sections:
- `## What I worked on`
- `## What changed`
- `## Decisions made`
- `## Files touched`
- `## Open questions`
- `## Next steps`
- `## Notes to promote later`
- `## Related`

### Snippet note
Use for:
- small code patterns
- commands
- implementation fragments
- useful examples

Required sections:
- `## Snippet`
- `## Why this matters`
- `## Caveats`
- `## Related`

### Writing draft
Use for:
- blog posts
- essays
- tutorials
- technical articles
- publishable content in progress

Required sections:
- `## Thesis`
- `## Audience`
- `## Outline`
- `## Draft`
- `## Supporting notes`
- `## Related`

### Concept note
Use only when explicitly instructed or when promoting a curated note into `02 Concepts/`.

Required sections:
- `## Definition`
- `## Why it matters`
- `## Examples`
- `## Related`

## Knowledge graph linking rules

### Core linking rule
Every new note must contain at least:
- one link to its project home note or writing/supporting note context
- one link to a related topic, decision, source, snippet, or neighboring note when such a note exists

If no related note exists yet, add the strongest available hub link and keep the note easy to connect later.

### Project hub rule
The project home note is the central hub for all project-specific notes.
Every project-specific note must link back to that hub.

### Writing hub rule
Writing notes should link to the concept, research, or project notes that support them.
Writing notes should not float as isolated drafts.

### Linking by note type

#### Research notes
Research notes must link to:
- the project home note
- related research notes on adjacent topics if they exist
- any decision note created from that research if it exists
- relevant snippet notes if the note includes implementation details

#### Decision notes
Decision notes must link to:
- the project home note
- the research note or notes that informed the decision
- any snippet or implementation note that shows how the decision was applied

#### Session summaries
Session summaries must link to:
- the project home note
- any research notes created or updated during the session
- any decision notes created during the session
- any concept note that became relevant during the session

#### Snippet notes
Snippet notes must link to:
- the project home note
- the research or decision note that gives the snippet context
- related snippets if they solve similar problems

#### Writing drafts
Writing drafts must link to:
- the concept, project, or research notes that support the article
- other writing notes only when there is clear editorial value
- the canonical concept or research note rather than duplicating the same knowledge in the draft

#### Concept notes
Concept notes in `02 Concepts/` must link to:
- related concepts
- the source project notes they were promoted from when relevant
- decision notes or research notes that show real usage

## Related section rule
Every durable note should end with a `## Related` section.

Use this format:

## Related
- [[Project Alpha]]
- [[OAuth PKCE refresh flow]]
- [[Use rotating refresh tokens]]

Only add links with real navigational value.
Do not force links that do not help future retrieval.

## Minimum link counts
- Research note: minimum 2 links
- Decision note: minimum 2 links
- Session summary: minimum 3 links when applicable
- Snippet note: minimum 2 links
- Writing draft: minimum 2 links
- Concept note: minimum 2 links

## Link quality rules
- Prefer a small number of meaningful links over a large number of weak ones.
- Do not link every sentence.
- Do not create links only because a term appears once.
- Link notes because a future reader would actually want to jump there.
- Use exact note titles when linking.
- Reuse canonical note names instead of inventing alternate names for the same concept.

## Tagging rules
- Use tags sparingly.
- Prefer links over tags.
- Tags should be broad and stable.

Good examples:
- `ai/claude`
- `project/<project-name>`
- `decision`
- `session`
- `snippet`
- `writing`
- `website`

Do not invent lots of one-off tags.

## Duplicate prevention
Before creating a note:
1. Search for an existing note on the same topic.
2. If one exists, update it instead of creating a second version.
3. Only create a new note when the topic is genuinely distinct.
4. If two notes are related but different, cross-link them.

## Capture quality rules
- Save durable knowledge, not routine chatter.
- Summarize patterns and conclusions instead of copying full conversations.
- Keep notes readable by future-you without needing the original chat.
- Do not paste giant logs unless the log itself is the artifact being analyzed.
- Do not paste entire source files unless explicitly asked.
- Separate facts from interpretation.
- Separate conclusions from uncertainty.
- Include examples when useful.
- Include open questions when something remains unresolved.

## Writing quality rules
- Writing drafts are for publishable content, not raw scratch dumps.
- Keep internal research and outward-facing writing separate.
- Drafts may summarize internal notes, but should not become a sloppy copy-paste of them.
- When possible, trace claims in writing drafts back to supporting research or concept notes.
- Use `05 Writing/Published/` only when the piece is actually published or archived as final.

## Session summary rules
Session summaries should be concise, useful, retrieval-friendly, and understandable later without rereading the full conversation.

## Promotion rules
- Notes written by Claude should normally go to Inbox, project folders, or writing folders first.
- `02 Concepts/` is curated and should only be written when explicitly asked.
- When promoting a note from Inbox or Project Research into `02 Concepts/`, preserve links to the original project context where useful.
- Add links to related concepts when promoting a concept note.
- Do not turn a promoted concept into a disconnected rewrite.

## Safe fallback behavior
If unsure how to connect a note:
- link it to the strongest hub note available
- add one item under `Open questions` or `Supporting notes` describing what it may need to connect to later
- do not invent weak links just to satisfy the graph

If unsure where to save a note:
- save one clean Inbox note instead of several weak notes

## Safe behavior
- Never write to protected folders unless explicitly instructed.
- Never mass-edit the vault unless explicitly instructed.
- Never create note sprawl just because information exists.
- Never create several notes when one structured note would do.
- When uncertain, choose the safer and simpler option.
