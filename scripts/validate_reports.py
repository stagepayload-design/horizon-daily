#!/usr/bin/env python3
"""Validate Horizon report paths, metadata, and archive integrity."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
POSTS = ROOT / "docs" / "_posts"
POST_PATTERN = re.compile(r"^(\d{4})-(\d{2})-(\d{2})-summary-([a-z]+)\.md$")
FIELD_PATTERN = re.compile(r"^([A-Za-z_][\w-]*):\s*(.*)$")
SECRET_PATTERNS = [
    re.compile(r"AKIA[0-9A-Z]{16}"),
    re.compile(r"\b(?:sk|ghp)_[A-Za-z0-9_-]{16,}"),
    re.compile(r"(?i)\b(?:password|token|secret)\s*[=:]\s*[^\s]{8,}"),
]


def front_matter(path: Path) -> dict[str, str]:
    content = path.read_text(encoding="utf-8")
    if not content.startswith("---\n"):
        raise ValueError("missing front matter")
    end = content.find("\n---\n", 4)
    if end == -1:
        raise ValueError("unterminated front matter")
    fields = {}
    for line in content[4:end].splitlines():
        match = FIELD_PATTERN.match(line)
        if match:
            fields[match.group(1)] = match.group(2).strip().strip('"')
    return fields


def validate() -> list[str]:
    errors = []
    permalinks = {}
    posts = sorted(POSTS.glob("**/*.md"))
    for path in posts:
        match = POST_PATTERN.match(path.name)
        if not match:
            errors.append(f"unexpected report filename: {path.relative_to(ROOT)}")
            continue
        year, month, day, language = match.groups()
        if path.parent != POSTS / year / month:
            errors.append(f"wrong year/month directory: {path.relative_to(ROOT)}")
        try:
            fields = front_matter(path)
        except ValueError as exc:
            errors.append(f"{path.relative_to(ROOT)}: {exc}")
            continue
        for required in ("layout", "title", "date", "lang", "permalink"):
            if not fields.get(required):
                errors.append(f"{path.relative_to(ROOT)}: missing {required}")
        date = f"{year}-{month}-{day}"
        if fields.get("date", "").split()[0] != date:
            errors.append(f"{path.relative_to(ROOT)}: date does not match filename")
        if fields.get("lang") != language:
            errors.append(f"{path.relative_to(ROOT)}: lang does not match filename")
        expected_permalink = f"/{year}/{month}/{day}/summary-{language}.html"
        if fields.get("permalink") != expected_permalink:
            errors.append(f"{path.relative_to(ROOT)}: unexpected permalink")
        permalink = fields.get("permalink")
        if permalink in permalinks:
            errors.append(f"duplicate permalink: {permalink}")
        elif permalink:
            permalinks[permalink] = path

        for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            if any(pattern.search(line) for pattern in SECRET_PATTERNS):
                errors.append(f"{path.relative_to(ROOT)}:{line_number}: possible secret")

    data_reports = list((ROOT / "data" / "summaries").glob("**/*.md"))
    if len(posts) != len(data_reports):
        errors.append(f"report count mismatch: docs={len(posts)}, data={len(data_reports)}")
    return errors


def main() -> None:
    errors = validate()
    if errors:
        print("Report validation failed:")
        for error in errors:
            print(f"- {error}")
        sys.exit(1)
    count = len(list(POSTS.glob("**/*.md")))
    print(f"Validated {count} reports")


if __name__ == "__main__":
    main()
