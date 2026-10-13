#!/usr/bin/env python3
"""Create a project-specific set of editable product document templates."""

from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path
import sys


TEMPLATES = {
    "competitor": "01-competitor-analysis.md",
    "prd": "02-prd.md",
    "roadmap": "03-roadmap.md",
    "hardware": "04-hardware-requirements.md",
    "software": "05-software-requirements.md",
    "backend": "06-backend-requirements.md",
    "meeting": "07-meeting-minutes.md",
    "acceptance": "08-acceptance.md",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, help="Output directory")
    parser.add_argument("--project-name", required=True, help="Project name")
    parser.add_argument("--owner", default="待填写", help="Document owner")
    parser.add_argument(
        "--docs",
        default="all",
        help="Comma-separated names or all: " + ",".join(TEMPLATES),
    )
    parser.add_argument("--force", action="store_true", help="Overwrite existing files")
    return parser.parse_args()


def selected_docs(value: str) -> list[str]:
    if value.strip().lower() == "all":
        return list(TEMPLATES)
    names = [item.strip().lower() for item in value.split(",") if item.strip()]
    unknown = [name for name in names if name not in TEMPLATES]
    if unknown:
        raise ValueError("Unknown document type: " + ", ".join(unknown))
    return names


def main() -> int:
    args = parse_args()
    try:
        names = selected_docs(args.docs)
    except ValueError as exc:
        print(exc, file=sys.stderr)
        return 2

    skill_dir = Path(__file__).resolve().parents[1]
    template_dir = skill_dir / "assets" / "templates"
    output_dir = Path(args.output).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    replacements = {
        "{{PROJECT_NAME}}": args.project_name,
        "{{DATE}}": date.today().isoformat(),
        "{{OWNER}}": args.owner,
    }

    created: list[Path] = []
    skipped: list[Path] = []
    for name in names:
        source = template_dir / TEMPLATES[name]
        destination = output_dir / TEMPLATES[name]
        if destination.exists() and not args.force:
            skipped.append(destination)
            continue
        text = source.read_text(encoding="utf-8")
        for old, new in replacements.items():
            text = text.replace(old, new)
        destination.write_text(text, encoding="utf-8", newline="\n")
        created.append(destination)

    print(f"Created {len(created)} document template(s) in {output_dir}")
    for path in created:
        print(f"  + {path.name}")
    for path in skipped:
        print(f"  = skipped existing {path.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
