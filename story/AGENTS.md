# story/AGENTS.md

Agent guidance for working with story files.

## Structure

One folder per chapter. Folders are named `chX` (e.g., `ch10`).

```
story/ch10/
  chapter10.md    ← published prose
  summary.md      ← what happened (load this for context before writing)
  notes.md        ← author craft notes, research, decisions
  plan.md         ← planning / what to write next (unwritten chapters)
```

Not every folder has all four files:
- **Published chapters** (ch1–ch17): `chapterX.md` + `summary.md` + `notes.md`
- **In-progress chapters** (ch17.5, ch18–ch20): `plan.md` + optional `notes.md`, no `chapterX.md` yet

No underscore prefix. No numbering in non-prose filenames. The folder name carries the chapter number.

## The Iceberg

Three layers, each serving a different job:

1. **Chapter prose** (`chapterX.md`) — tip of the iceberg. Stands alone. The reader never needs the wiki.
2. **Chapter notes** (`notes.md`) — the bridge. Links out to wiki pages that support each scene. Explains *what matters for this chapter* without duplicating wiki content. When you sit down to draft, the notes tell you which wiki pages to load and why they matter here.
3. **Wiki** (`$MERIDIAN_CONTEXT_KB_DIR/wiki/`) — the full iceberg beneath. Canon worldbuilding, systems, characters, lore. Source of truth. Notes link into it; prose never references it.

Notes should link to specific wiki pages using [GitHub URLs][kb-base] (per root `AGENTS.md` link guidance). Group links by scene or topic so the relevant worldbuilding is findable at drafting time.

[kb-base]: https://github.com/haowjy/writing-kb/blob/main/pokemon-amber/kb/wiki/

## Loading Context

When drafting or critiquing a chapter, load in this order:

1. **Chapter notes** — `story/ch{N}/notes.md` (links to relevant wiki pages, author decisions, scene-specific context)
2. **Style files** — `$MERIDIAN_CONTEXT_KB_DIR/styles/` (voice, tone, scene type)
3. **Recent summaries** — `story/ch{N-2}/summary.md` through `story/ch{N}/summary.md` (last 2–3 chapters)
4. **Current plan** — `story/ch{N}/plan.md` if drafting a new chapter
5. **Wiki pages** — follow links from the notes; load character/lore pages as needed

Do not load all summaries at once — load only the ones adjacent to the chapter being worked on.

## Point of View

Default: Amber's **1st person** perspective.

Exceptions (3rd person limited):
- Ch 6 — Fuji POV
- Ch 13 — Oak POV
- Ch 16 — 3rd person for a critical moment Amber doesn't witness

When drafting, confirm the POV for the chapter from the plan or notes before writing.

## Prose Conventions

See root `AGENTS.md` for full style rules. Key points:
- Em dash: `---` (three hyphens)
- Ellipsis: `...` (three periods, no unicode)
- Quotes: plain ASCII `"` and `'`
- `Pokemon` — consistent within a file (ASCII or accented)
- No inline author commentary in published prose

## Linking to Story Files

From KB: `../../story/ch10/chapter10.md`
From agent prompt: `story/ch10/summary.md`

For links to references outside this repo (especially KB files resolved via `$MERIDIAN_CONTEXT_KB_DIR`), follow root `AGENTS.md` link guidance: do not use local filesystem path links; use GitHub URLs (reference-style links preferred).
