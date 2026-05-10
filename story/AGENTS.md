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

## Loading Context

When drafting or critiquing a chapter, load in this order:

1. **Style files** — `.meridian/kb/styles/` (voice, tone, scene type)
2. **Recent summaries** — `story/ch{N-2}/summary.md` through `story/ch{N}/summary.md` (last 2–3 chapters)
3. **Current plan** — `story/ch{N}/plan.md` if drafting a new chapter
4. **Character/lore pages** — `.meridian/kb/wiki/characters/` and relevant lore as needed

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
