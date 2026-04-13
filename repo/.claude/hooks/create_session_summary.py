#!/usr/bin/env python3
import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "obsidian-config.json"


def run_obsidian(args: list[str]) -> None:
    subprocess.run(["obsidian"] + args, check=True)


def main() -> int:
    payload = json.load(sys.stdin)

    config = json.loads(CONFIG_PATH.read_text())
    vault_name = config["vault_name"]
    project_name = config["project_name"]
    summary_folder = config["folders"]["session_summaries"]
    daily_note_enabled = config.get("daily_note_enabled", False)

    now = datetime.now()
    file_stamp = now.strftime("%Y-%m-%d %H%M%S")
    title_stamp = now.strftime("%Y-%m-%d %H:%M:%S")
    created = now.strftime("%Y-%m-%d %H:%M")
    note_name = f"{file_stamp} {project_name} session.md"
    note_path = f"{summary_folder}/{note_name}"

    cwd = payload.get("cwd", "")
    reason = payload.get("reason", "")
    transcript_path = payload.get("transcript_path", "")
    session_id = payload.get("session_id", "")

    content = f"""---
type: session-summary
project: {project_name}
created: {created}
status: inbox
source_type: claude-code
session_id: {session_id}
session_end_reason: {reason}
repo_cwd: "{cwd}"
transcript_path: "{transcript_path}"
tags:
  - session
  - ai/claude
---

# {title_stamp} Session Summary

## What I worked on

## What changed

## Decisions made

## Files touched

## Open questions

## Next steps

## Notes to promote later

## Related
- [[{project_name}]]
"""

    run_obsidian([
        f"vault={vault_name}",
        "create",
        f"path={note_path}",
        f"content={content}",
    ])

    if daily_note_enabled:
        daily_line = f"- Session ended for [[{note_name[:-3]}]] (reason: {reason})\n"
        run_obsidian([
            f"vault={vault_name}",
            "daily:append",
            f"content={daily_line}"
        ])

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
