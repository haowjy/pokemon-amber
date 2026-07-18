# Content-source adapters

## Selection order

1. Use the project's existing publishing/export command when it produces the required title, ordering, HTML, and text.
2. Use already-rendered HTML or documents when they are canonical and current.
3. Adapt the canonical source into a temporary normalized chapter set without changing source files.
4. Use the bundled Markdown adapter only when its assumptions match the project.

## Bundled Markdown/frontmatter adapter

`scripts/export_markdown_frontmatter.py` is optional. It expects Markdown files matching a configurable glob and YAML-like frontmatter containing numeric `chapter:` and `title:` fields.

```bash
python3 ~/.codex/skills/sync-fiction-platforms/scripts/export_markdown_frontmatter.py \
  --story-dir <root> \
  --pattern '<glob>' \
  --output /tmp/fiction-publish.json
```

Use `--integer-only` when the authorized scope excludes fractional chapter numbers. Do not use this adapter for a project whose canonical metadata or Markdown semantics differ; write a task-local adapter instead.

## Normalization checks

- Preserve deliberate emphasis and paragraph breaks.
- Remove source-only metadata and the duplicated chapter heading when the destination has a separate title field.
- Keep a plain-text fallback alongside rich HTML.
- Retain source provenance and a content hash when practical.
- Compare chapter count and titles with the authorized scope before opening a live editor.
