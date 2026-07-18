#!/usr/bin/env python3
"""Export integer-numbered Markdown chapters for browser publishing."""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import re
from decimal import Decimal
from pathlib import Path


FRONTMATTER = re.compile(r"^---\n(.*?)\n---\n", re.S)
INLINE_ESCAPABLE = re.compile(r"\\([\\`*{}\[\]()#+\-.!_~])")


def render_inline(value: str) -> str:
    value = html.escape(value, quote=False)
    value = INLINE_ESCAPABLE.sub(r"\1", value)
    value = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", value)
    value = re.sub(r"(?<!\*)\*([^*\n]+?)\*(?!\*)", r"<em>\1</em>", value)
    return re.sub(r"`([^`\n]+?)`", r"<code>\1</code>", value)


def strip_tags(value: str) -> str:
    return html.unescape(re.sub(r"<[^>]+>", "", value))


def parse_title(frontmatter: str, path: Path) -> str:
    match = re.search(r'^title:\s*["\']?(.*?)["\']?\s*$', frontmatter, re.M)
    if not match:
        raise ValueError(f"Missing title in {path}")
    return match.group(1).strip()


def parse_chapter(frontmatter: str, path: Path) -> str:
    match = re.search(r'^chapter:\s*["\']?([0-9]+(?:\.[0-9]+)?)["\']?\s*$', frontmatter, re.M)
    if not match:
        raise ValueError(f"Missing numeric chapter in {path}")
    return match.group(1)


def convert(path: Path, chapter: str, frontmatter: re.Match[str] | None = None) -> dict[str, object]:
    raw = path.read_text(encoding="utf-8")
    frontmatter = frontmatter or FRONTMATTER.match(raw)
    if not frontmatter:
        raise ValueError(f"Missing frontmatter in {path}")

    canonical_title = parse_title(frontmatter.group(1), path)
    short_title = re.sub(r"^\[Chapter\s+\d+(?:\.\d+)?\]\s*", "", canonical_title)
    body = raw[frontmatter.end() :].lstrip()
    body = re.sub(r"^#\s+.*?\n+", "", body, count=1)

    blocks: list[str] = []
    paragraph: list[str] = []
    lines = body.splitlines()

    def flush() -> None:
        if not paragraph:
            return
        value = " ".join(part.strip() for part in paragraph).strip()
        paragraph.clear()
        if value:
            blocks.append(f"<p>{render_inline(value)}</p>")

    index = 0
    while index < len(lines):
        line = lines[index]
        if line.strip().startswith("```"):
            flush()
            index += 1
            code: list[str] = []
            while index < len(lines) and not lines[index].strip().startswith("```"):
                code.append(lines[index])
                index += 1
            while code and not code[0].strip():
                code.pop(0)
            while code and not code[-1].strip():
                code.pop()
            blocks.append("<p><code>\n" + html.escape("\n".join(code), quote=False) + "\n</code></p>")
        elif not line.strip():
            flush()
        else:
            paragraph.append(line)
        index += 1
    flush()

    rendered_html = "\n".join(blocks)
    rendered_text = "\n\n".join(strip_tags(block) for block in blocks)
    return {
        "chapter": chapter,
        "canonical_title": canonical_title,
        "short_title": short_title,
        "html": rendered_html,
        "text": rendered_text,
        "source": str(path),
        "sha256": hashlib.sha256(raw.encode("utf-8")).hexdigest(),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--story-dir", type=Path, default=Path("story"))
    parser.add_argument("--pattern", default="**/chapter*.md")
    parser.add_argument("--output", type=Path, default=Path("/tmp/fiction-publish.json"))
    parser.add_argument("--through", type=Decimal)
    parser.add_argument("--integer-only", action="store_true")
    args = parser.parse_args()

    chapters: dict[str, dict[str, object]] = {}
    for expected in args.story_dir.glob(args.pattern):
        if not expected.is_file():
            continue
        raw = expected.read_text(encoding="utf-8")
        frontmatter = FRONTMATTER.match(raw)
        if not frontmatter:
            continue
        try:
            number = parse_chapter(frontmatter.group(1), expected)
        except ValueError:
            continue
        numeric = Decimal(number)
        if args.integer_only and numeric != numeric.to_integral_value():
            continue
        if args.through is not None and numeric > args.through:
            continue
        key = str(int(numeric)) if numeric == numeric.to_integral_value() else str(numeric)
        if key in chapters:
            raise ValueError(f"Duplicate chapter {key}: {chapters[key]['source']} and {expected}")
        chapters[key] = convert(expected, key, frontmatter)

    ordered = dict(sorted(chapters.items(), key=lambda item: Decimal(item[0])))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(ordered, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Exported {len(ordered)} chapters to {args.output}")
    for item in ordered.values():
        print(f"{item['chapter']:>5}  {item['canonical_title']}  {len(item['html']):>6} HTML chars")


if __name__ == "__main__":
    main()
