# Personal Claude rules

## Core behavior
- Be direct, practical, and concise.
- Prefer small, safe, reviewable changes over broad refactors.
- Before creating a new file, check whether an existing file should be updated instead.
- State tradeoffs briefly when they matter.
- Do not assume project structure without checking the repo first.

## Coding workflow
- Preserve existing architecture unless explicitly asked to restructure it.
- Do not change dependency versions unless asked.
- Do not rename files, move folders, or refactor large areas unless there is a strong reason and the user asked for it.
- When changing behavior, update tests if the repo has tests.
- Prefer copy-pasteable commands.
- For risky work, prefer a branch-first workflow.

## Working style
- First understand the local context before editing.
- Search before creating duplicates.
- Make minimal changes that fully solve the task.
- Keep explanations readable and easy to scan.
- Use explicit filenames and paths when relevant.

## Knowledge capture to Obsidian
- Treat Obsidian as the knowledge base, not the code repo.
- Save raw captures and partial notes to the Obsidian vault, not into source folders.
- When capturing knowledge, prefer:
  - one session summary
  - one or two research notes
  - a decision note if a real decision was made
- Do not dump full raw chat transcripts into the vault unless explicitly asked.
- Do not paste large source files into the vault unless the code itself is the knowledge artifact.
- Summarize patterns, decisions, edge cases, and useful snippets instead of dumping noise.

## Obsidian write behavior
- Default destination for uncertain note placement is `00 Inbox/AI Captures/`.
- Prefer updating an existing relevant note over creating a duplicate.
- Do not write to evergreen or curated notes unless explicitly asked.
- Use the vault's local `CLAUDE.md` rules when writing into the Obsidian vault.
- When saving a project note, always link it back to the project home note.

## Obsidian linking behavior
- Do not create isolated notes.
- Every saved note should link to its project home note.
- Add links to related research, decisions, snippets, or concepts when they already exist.
- Prefer a few strong links over many weak ones.
- Update existing notes instead of creating near-duplicates.

## Session wrap-up
- At the end of a meaningful work session, produce a short summary containing:
  - what was worked on
  - what changed
  - important decisions
  - open questions
  - next steps
- Keep session summaries useful for future retrieval, not conversational.

## What to avoid
- Do not create note sprawl.
- Do not create near-duplicate notes with slightly different titles.
- Do not use excessive tags.
- Do not invent folder destinations when the vault rules already define them.
- Do not write to protected folders unless explicitly instructed.

## Preferred output shape for saved notes
- Separate facts from decisions.
- Separate decisions from open questions.
- Include concrete examples when helpful.
- Use explicit titles.
- Keep notes clean enough that they can be reused later without rereading the whole session.
