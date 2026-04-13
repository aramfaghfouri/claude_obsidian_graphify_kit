# Repo instructions

## Project basics
- Replace the placeholders in this file with the real commands for this repo.
- Keep code changes in the repo.
- Keep durable knowledge in the Obsidian vault.

## Commands
- Install: `__INSTALL_COMMAND__`
- Dev: `__DEV_COMMAND__`
- Test: `__TEST_COMMAND__`
- Lint: `__LINT_COMMAND__`

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
- Save publishable writing drafts to `05 Writing/Drafts/`
- Link all project notes to `[[__PROJECT_NAME__]]`

## Graphify workflow
- If `graphify-out/GRAPH_REPORT.md` exists, read it before broad codebase searches for architecture or design questions.
- Use Graphify outputs to understand structure first, then inspect only the most relevant files.
- Save durable findings to the Obsidian vault as research notes, decision notes, or snippets.
- Do not copy raw Graphify output into the vault unless explicitly asked.

## Session wrap-up
- At the end of a meaningful session, create or update:
  - one session summary
  - zero to two research notes
  - one decision note if a real architectural choice was made
  - one snippet note if a command or pattern is worth keeping
