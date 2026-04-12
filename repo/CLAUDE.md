# Repo instructions

## Project basics
- Replace this section with the real package manager, test commands, and important paths for this repo.
- Main app code: `src/`
- Tests: `tests/`
- Config: `config/`

## Commands
- Install: `pnpm install`
- Dev: `pnpm dev`
- Test: `pnpm test`
- Lint: `pnpm lint`

## Working rules
- Do not change dependency versions unless asked.
- Keep edits minimal and local to the task.
- Prefer small, reviewable diffs.
- Update tests when behavior changes.

## Obsidian capture for this repo
- Project name in the vault: `__PROJECT_NAME__`
- Save research notes to `01 Projects/__PROJECT_NAME__/Research/`
- Save decision notes to `01 Projects/__PROJECT_NAME__/Decisions/`
- Save snippet notes to `01 Projects/__PROJECT_NAME__/Snippets/`
- Save session summaries to `00 Inbox/Session Summaries/`
- Link all notes to `[[__PROJECT_NAME__]]`

## Graphify workflow
- If `graphify-out/GRAPH_REPORT.md` exists, read it before broad codebase searches for architecture or design questions.
- Use Graphify outputs to understand structure first, then inspect only the most relevant files.
- Save durable findings to the Obsidian vault as research notes or decision notes.
- Do not copy raw Graphify output into the vault unless explicitly asked.
- Graphify is a repo understanding layer, not the long-term note system.

## Session wrap-up
- At the end of a meaningful session, create or update:
  - one session summary
  - zero to two research notes
  - one decision note if an architectural choice was made
