#!/usr/bin/env python3
"""Compile annotated chapter Markdown into commentless chapter prose."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


ANNOTATED_SUFFIX = ".annotated.md"
HTML_COMMENT = re.compile(r"<!--.*?-->", flags=re.DOTALL)


def output_path(source: Path) -> Path:
    if not source.name.endswith(ANNOTATED_SUFFIX):
        raise ValueError(f"annotated source must end in {ANNOTATED_SUFFIX}: {source}")
    return source.with_name(source.name[: -len(ANNOTATED_SUFFIX)] + ".md")


def compile_text(text: str, source: Path) -> str:
    starts = text.count("<!--")
    complete = len(HTML_COMMENT.findall(text))
    if starts != complete:
        raise ValueError(f"unclosed HTML comment in {source}")

    return HTML_COMMENT.sub("", text)


def process(source: Path, check: bool) -> bool:
    destination = output_path(source)
    compiled = compile_text(source.read_text(encoding="utf-8"), source)

    if check:
        if not destination.exists() or destination.read_text(encoding="utf-8") != compiled:
            print(f"stale: {destination}", file=sys.stderr)
            return False
        print(f"current: {destination}")
        return True

    temporary = destination.with_suffix(destination.suffix + ".tmp")
    temporary.write_text(compiled, encoding="utf-8")
    temporary.replace(destination)
    print(f"compiled: {source} -> {destination}")
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="fail if compiled output is stale")
    parser.add_argument(
        "--all",
        action="store_true",
        help="compile every story/ch*/chapter*.annotated.md source",
    )
    parser.add_argument("sources", nargs="*", type=Path)
    args = parser.parse_args()

    sources = list(args.sources)
    if args.all:
        sources.extend(sorted(Path("story").glob("ch*/chapter*.annotated.md")))
    sources = list(dict.fromkeys(sources))
    if not sources:
        parser.error("provide an annotated chapter source or use --all")

    try:
        results = [process(source, args.check) for source in sources]
    except (OSError, ValueError) as error:
        print(error, file=sys.stderr)
        return 2
    return 0 if all(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
