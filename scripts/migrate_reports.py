#!/usr/bin/env python3
"""Move flat Horizon reports into year/month directories."""

from __future__ import annotations

import argparse
import re
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS_PATTERN = re.compile(r"^(\d{4})-(\d{2})-(\d{2})-summary-([a-z]+)\.md$")
DATA_PATTERN = re.compile(r"^horizon-(\d{4})-(\d{2})-(\d{2})-([a-z]+)\.md$")


def add_permalink(path: Path, date: str, language: str) -> None:
    content = path.read_text(encoding="utf-8")
    if not content.startswith("---\n"):
        raise ValueError(f"missing front matter: {path}")
    end = content.find("\n---\n", 4)
    if end == -1:
        raise ValueError(f"invalid front matter: {path}")
    front_matter = content[4:end]
    if re.search(r"^permalink:", front_matter, re.MULTILINE):
        return
    permalink = f"permalink: /{date.replace('-', '/')}/summary-{language}.html"
    updated = content[:end] + f"\n{permalink}" + content[end:]
    temp_path = path.with_suffix(".tmp")
    temp_path.write_text(updated, encoding="utf-8")
    temp_path.replace(path)


def candidates(base: Path, pattern: re.Pattern[str]):
    for source in sorted(base.glob("*.md")):
        match = pattern.match(source.name)
        if match:
            yield source, match


def migrate(apply: bool) -> int:
    moves = []
    for base, pattern in (
        (ROOT / "docs" / "_posts", DOCS_PATTERN),
        (ROOT / "data" / "summaries", DATA_PATTERN),
    ):
        for source, match in candidates(base, pattern):
            year, month, day, language = match.groups()
            target = base / year / month / source.name
            if target.exists():
                if source.read_bytes() == target.read_bytes():
                    continue
                raise FileExistsError(f"refusing to overwrite different file: {target}")
            moves.append((source, target, f"{year}-{month}-{day}", language))

    action = "APPLY" if apply else "DRY-RUN"
    for source, target, date, language in moves:
        print(f"[{action}] {source.relative_to(ROOT)} -> {target.relative_to(ROOT)}")
        if not apply:
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run(
            ["git", "mv", str(source.relative_to(ROOT)), str(target.relative_to(ROOT))],
            cwd=ROOT,
            check=True,
        )
        if target.is_relative_to(ROOT / "docs" / "_posts"):
            add_permalink(target, date, language)

    print(f"{action}: {len(moves)} report files")
    return len(moves)


def main() -> None:
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--dry-run", action="store_true")
    group.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    migrate(apply=args.apply)


if __name__ == "__main__":
    main()
