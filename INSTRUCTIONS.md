# Claude + Obsidian + Graphify clean setup kit

This guide is the single clean path for the architecture in this kit.

Use this if you want:
- Claude Code for coding and research
- Obsidian as your long-term knowledge base
- Graphify as a repo and raw-material analysis layer
- a clean place for writing website posts later
- Git for vault version history

---

## 1. What the architecture is

Use this mental model:

**Code repo / raw research files** -> **Graphify** -> **Claude reasoning** -> **Obsidian curated notes**

Roles:
- **Code repo** = source of truth for code
- **Graphify** = structure map for the repo or messy research folder
- **Obsidian vault** = source of truth for durable knowledge and writing drafts
- **Claude Code** = the agent that reads, reasons, and saves notes

Do not use Obsidian as your code repo.
Do not use Graphify as your long-term note system.
Do not let Claude write everywhere.

---

## 2. What is in this kit

### `home/.claude/CLAUDE.md`
Your global Claude rules.

Put it at:
- macOS / Linux / WSL: `~/.claude/CLAUDE.md`

### `vault/`
This is the example Obsidian vault structure.
Important files:
- `vault/CLAUDE.md`
- `vault/.gitignore`
- `vault/90 Templates/*`

### `repo/`
This is the example code repo side.
Important files:
- `repo/CLAUDE.md`
- `repo/.graphifyignore`
- `repo/.claude/settings.local.json`
- `repo/.claude/obsidian-config.json`
- `repo/.claude/scripts/save_note.py`
- `repo/.claude/hooks/create_session_summary.py`

---

## 3. Folder layout you should use

### Obsidian vault
- `00 Inbox/AI Captures/`
- `00 Inbox/Session Summaries/`
- `01 Projects/<Project Name>/Research/`
- `01 Projects/<Project Name>/Decisions/`
- `01 Projects/<Project Name>/Meetings/`
- `01 Projects/<Project Name>/Snippets/`
- `01 Projects/<Project Name>/Scratch/`
- `02 Concepts/`
- `03 Sources/`
- `04 Dashboards/`
- `05 Writing/Ideas/`
- `05 Writing/Drafts/`
- `05 Writing/In Review/`
- `05 Writing/Ready to Publish/`
- `05 Writing/Published/`
- `90 Templates/`
- `99 Archive/`

### What each area is for
- **Inbox** = raw captures and session stubs
- **Projects** = project-specific knowledge Claude may write directly
- **Concepts** = curated evergreen notes that should stay human-controlled
- **Sources** = papers, PDFs, references, links
- **Dashboards** = manual dashboards or Bases views
- **Writing** = publishable articles and drafts
- **Templates** = note templates
- **Archive** = dead or finished material

---

## 4. Why `05 Writing/` exists

This is important.

If you want notes that may be published later on your website, do not mix them into:
- project research folders
- evergreen concept folders
- Inbox

Use:
- `05 Writing/Ideas/` for rough article ideas
- `05 Writing/Drafts/` for actual drafts
- `05 Writing/In Review/` for editing stage
- `05 Writing/Ready to Publish/` for nearly final pieces
- `05 Writing/Published/` for archived published versions and URLs

This keeps internal knowledge separate from outward-facing content.

---

## 5. Where to place the files from this kit

### A. Global Claude file
Copy:
- `home/.claude/CLAUDE.md`

To:
- `~/.claude/CLAUDE.md`

If `~/.claude/` does not exist, create it.

### B. Vault files
Copy everything from:
- `vault/`

Into your actual Obsidian vault root.

Your vault root is the folder that contains `.obsidian/` when Obsidian is set up.

### C. Repo files
Copy everything from:
- `repo/`

Into the root of the code repo you want Claude to work in.

---

## 6. The first placeholders you must replace

Edit these first:

### `repo/.claude/obsidian-config.json`
Replace:
- `__VAULT_NAME__`
- `__PROJECT_NAME__`

### `repo/CLAUDE.md`
Replace:
- `__PROJECT_NAME__`
- `__INSTALL_COMMAND__`
- `__DEV_COMMAND__`
- `__TEST_COMMAND__`
- `__LINT_COMMAND__`

### Vault templates
Replace:
- `__PROJECT_NAME__`
- `__project-name-slug__`

Do this in:
- `vault/90 Templates/research-note.md`
- `vault/90 Templates/decision-note.md`
- `vault/90 Templates/session-summary.md`
- `vault/90 Templates/snippet-note.md`

---

## 7. Set up the vault as its own Git repo

At the vault root:

```bash
git init
git branch -M main
git add .
git commit -m "Initial vault structure"
```

Why do this:
- version history for notes
- rollback if Claude writes something dumb
- safe experimentation
- separate backup discipline

Do not use Git as your only sync method unless you are comfortable with merge conflicts.

---

## 8. Enable Obsidian CLI

This matters because the save script and session-summary hook use the Obsidian CLI.

In Obsidian:
1. Open Obsidian
2. Open **Settings**
3. Go to **General**
4. Find **Command line interface**
5. Enable it

The Obsidian app must be running when you use the CLI.

---

## 9. Make the scripts executable

In your repo root:

```bash
chmod +x .claude/scripts/save_note.py
chmod +x .claude/hooks/create_session_summary.py
```

---

## 10. What the automation files do

### `save_note.py`
This is your controlled save path.
Claude can use it to create:
- research notes
- decision notes
- snippet notes
- writing drafts

### `create_session_summary.py`
This is your SessionEnd hook.
When a Claude session ends, it creates:
- one timestamped session summary note in `00 Inbox/Session Summaries/`
- optionally one line in today’s daily note

---

## 11. How the Claude hook works

The file:
- `repo/.claude/settings.local.json`

Registers a `SessionEnd` hook.

That means when the Claude Code session ends, Claude runs:

```bash
python3 .claude/hooks/create_session_summary.py
```

This script reads JSON from stdin that Claude passes to it and uses your `obsidian-config.json` values to create the summary note.

---

## 12. How to test the setup

### A. Test the Obsidian CLI
With Obsidian open:

```bash
obsidian help
```

If that fails, stop and fix CLI setup before doing anything else.

### B. Test the note save script
From the repo root:

```bash
printf '%s
' 'This is a test note body.' | python3 .claude/scripts/save_note.py --type research --title "Smoke test research note" --stdin-body
```

Then check whether the note appears in:
- `01 Projects/<Project Name>/Research/`

### C. Test writing draft creation
From the repo root:

```bash
printf '%s
' 'This article will explain why the vault should be separate from the repo.' | python3 .claude/scripts/save_note.py --type writing --title "Why I keep Obsidian separate from my code repo" --stdin-body
```

Then check whether the note appears in:
- `05 Writing/Drafts/`

### D. Test the SessionEnd hook manually
From the repo root:

```bash
echo '{"session_id":"test123","cwd":"'"$PWD"'","hook_event_name":"SessionEnd","reason":"other","transcript_path":"/tmp/fake.jsonl"}' | python3 .claude/hooks/create_session_summary.py
```

Then check whether a timestamped note appears in:
- `00 Inbox/Session Summaries/`

If manual test works but real session end does not, the script is fine and the problem is hook registration.

---

## 13. How to run Claude so it sees both repo and vault rules

Best practice:
- run Claude from the code repo
- add the vault as an additional directory if needed

If you want Claude to also load the vault’s `CLAUDE.md` from the added directory, export this before running Claude:

```bash
export CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD=1
```

Then run Claude from the repo root.

---

## 14. Graphify in the architecture

Graphify should sit between the repo and your vault.

Use it for:
- understanding code structure faster
- finding relationships in large repos
- surfacing architecture insights before Claude does raw file search
- exploring messy research folders before you turn them into notes

Do not use Graphify as the long-term storage layer.
Do not point it at your entire vault on day one.

### Recommended use
- run Graphify per code repo
- optionally run Graphify on a raw research folder
- let Claude read the Graphify outputs
- let Claude write distilled notes into Obsidian

### What to keep in the repo
- `graphify-out/`
- `.graphifyignore`
- repo `CLAUDE.md`

Do not automatically dump Graphify outputs into the vault.
Only write useful conclusions into the vault.

---

## 15. Graphify setup steps

Inside the repo:
1. Install Graphify
2. Initialize or run it according to its current docs
3. Create the graph for the repo
4. Install the Claude integration if you want the always-on Graphify-aware Claude workflow

Keep `.graphifyignore` in the repo root so junk paths do not pollute the graph.

Then tell Claude:
- read `graphify-out/GRAPH_REPORT.md` before broad architecture searches

That behavior is already described in `repo/CLAUDE.md`.

---

## 16. How notes should connect into a knowledge graph

Your Obsidian graph is built by links, not magic.

Every saved note should connect to something meaningful.

### Project notes
Project-specific notes should usually link to:
- `[[<Project Name>]]`
- a sibling research note
- a decision note
- a snippet note

### Writing notes
Writing drafts should usually link to:
- the project or concept note that supports the article
- the research note that contains the evidence
- the concept note that captures the reusable idea

### Why this matters
If notes do not link to anything, you just have a folder full of lonely Markdown files pretending to be a second brain.

---

## 17. What to do during normal daily use

### When coding
- Claude works in the repo
- Graphify helps Claude understand repo structure
- Claude saves durable findings as research, decision, or snippet notes

### When researching
- Claude summarizes docs and findings
- Claude saves useful outcomes to project research notes
- only strong evergreen ideas get promoted later to `02 Concepts/`

### When writing for your website
- create ideas in `05 Writing/Ideas/`
- draft articles in `05 Writing/Drafts/`
- move them through review folders manually

### End of session
- Claude creates a session summary automatically through the hook

### Weekly cleanup
- review `00 Inbox/`
- promote only the good material
- merge duplicates
- archive junk
- move article drafts forward if they are real

---

## 18. Safe operating rules

Keep these rules in your head:
- the repo is for code
- the vault is for knowledge
- Graphify is for structure discovery
- `02 Concepts/` is curated
- `05 Writing/` is for publishable content
- Inbox is allowed to be messy
- the rest should stay clean

---

## 19. Common mistakes to avoid

### Mistake 1
Putting blog drafts in project research folders

### Mistake 2
Letting Claude write to the whole vault

### Mistake 3
Running Graphify on the whole vault immediately

### Mistake 4
Storing full chat transcripts in the vault

### Mistake 5
Using Git as your only multi-device sync layer without discipline

---

## 20. Recommended first-day checklist

1. Copy `home/.claude/CLAUDE.md` to `~/.claude/CLAUDE.md`
2. Copy `vault/` contents into your actual vault
3. Copy `repo/` contents into one real code repo
4. Edit `repo/.claude/obsidian-config.json`
5. Edit `repo/CLAUDE.md`
6. Replace template placeholders
7. Enable Obsidian CLI
8. Make the scripts executable
9. Test `obsidian help`
10. Test `save_note.py`
11. Test writing draft creation
12. Test the manual SessionEnd hook
13. Start using it normally
14. Add Graphify only after the basic save flow works

---

## 21. Commands you will actually use

### Save a research note
```bash
printf '%s
' 'Summary body here' | python3 .claude/scripts/save_note.py --type research --title "JWT refresh edge cases" --stdin-body
```

### Save a decision note
```bash
printf '%s
' 'We should use rotating refresh tokens.' | python3 .claude/scripts/save_note.py --type decision --title "Use rotating refresh tokens" --stdin-body
```

### Save a snippet note
```bash
printf '%s
' 'curl -H "Authorization: Bearer <token>" ...' | python3 .claude/scripts/save_note.py --type snippet --title "Bearer token curl example" --stdin-body
```

### Save a writing draft
```bash
printf '%s
' 'This article argues that project knowledge and publishable writing should be separated.' | python3 .claude/scripts/save_note.py --type writing --title "Why internal knowledge and public writing should live in different folders" --stdin-body
```

---

## 22. Final rule of thumb

Keep the system boring.

The clean stack is:
- repo for code
- Graphify for structure
- Obsidian for memory
- `05 Writing/` for publishable drafts
- Git for vault history
- Claude hooks for the tiny deterministic parts

That is the setup that scales without turning into a haunted Markdown warehouse.
