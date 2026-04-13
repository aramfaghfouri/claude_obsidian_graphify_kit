#!/usr/bin/env python3
import argparse
import json
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "obsidian-config.json"


def run_obsidian(args: list[str]) -> None:
    subprocess.run(["obsidian"] + args, check=True)


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-") or "untitled"


def project_tag(project_name: str) -> str:
    return project_name.lower().replace(" ", "-")


def render_note(note_type: str, project_name: str, title: str, body: str) -> str:
    today = datetime.now().strftime("%Y-%m-%d")
    ptag = project_tag(project_name)

    if note_type == "research":
        return f"""---
type: research
project: {project_name}
status: inbox
source_type: claude
created: {today}
updated: {today}
tags:
  - ai/claude
  - project/{ptag}
---

# {title}

## Summary

{body}

## Key points

## Code or examples

## Decisions implied

## Open questions

## Related
- [[{project_name}]]
"""
    if note_type == "decision":
        return f"""---
type: decision
project: {project_name}
status: active
created: {today}
decision_date: {today}
tags:
  - decision
  - project/{ptag}
---

# {title}

## Context

{body}

## Decision

## Why

## Tradeoffs

## Follow up

## Related
- [[{project_name}]]
"""
    if note_type == "snippet":
        return f"""---
type: snippet
project: {project_name}
created: {today}
tags:
  - snippet
  - project/{ptag}
---

# {title}

## Snippet

{body}

## Why this matters

## Caveats

## Related
- [[{project_name}]]
"""
    if note_type == "writing":
        return f"""---
type: writing
status: draft
publish_target: website
slug: {slugify(title)}
created: {today}
updated: {today}
tags:
  - writing
  - website
---

# {title}

## Thesis

{body}

## Audience

## Outline

## Draft

## Supporting notes

## Related
"""
    raise ValueError(f"Unsupported note_type: {note_type}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--type", required=True, choices=["research", "decision", "snippet", "writing"])
    parser.add_argument("--title", required=True)
    parser.add_argument("--stdin-body", action="store_true")
    args = parser.parse_args()

    config = json.loads(CONFIG_PATH.read_text())
    vault_name = config["vault_name"]
    project_name = config["project_name"]

    folder_map = {
        "research": config["folders"]["research"],
        "decision": config["folders"]["decisions"],
        "snippet": config["folders"]["snippets"],
        "writing": config["folders"]["writing_drafts"],
    }

    body = sys.stdin.read().strip() if args.stdin_body else ""
    today = datetime.now().strftime("%Y-%m-%d")
    safe_title = re.sub(r'[\\/:*?"<>|]+', "-", args.title).strip()
    file_name = f"{today} {safe_title}.md"
    note_path = f"{folder_map[args.type]}/{file_name}"

    content = render_note(args.type, project_name, args.title, body)

    run_obsidian([
        f"vault={vault_name}",
        "create",
        f"path={note_path}",
        f"content={content}",
    ])

    print(note_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
