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


def sanitize_filename(name: str) -> str:
    name = re.sub(r'[\/:*?"<>|]+', " ", name).strip()
    name = re.sub(r"\s+", " ", name)
    return name[:180]


def run_obsidian(args: list[str]) -> None:
    subprocess.run(["obsidian"] + args, check=True)


def slugify_project(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def render_note(note_type: str, project_name: str, title: str, body: str) -> str:
    today = datetime.now().strftime("%Y-%m-%d")
    project_slug = slugify_project(project_name)

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
  - project/{project_slug}
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
  - project/{project_slug}
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
  - project/{project_slug}
---

# {title}

## Snippet

{body}

## Why this matters

## Caveats

## Related
- [[{project_name}]]
"""
    raise ValueError(f"Unsupported note_type: {note_type}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--type", required=True, choices=["research", "decision", "snippet"])
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
    }

    body = sys.stdin.read().strip() if args.stdin_body else ""
    today = datetime.now().strftime("%Y-%m-%d")
    file_name = f"{today} {sanitize_filename(args.title)}.md"
    note_path = f"{folder_map[args.type]}/{file_name}"

    content = render_note(args.type, project_name, args.title, body)

    run_obsidian([
        f"vault={vault_name}",
        "create",
        f"path={note_path}",
        f"content={content}"
    ])

    print(note_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
