# story/AGENTS.md

Agent guidance for working with story files.

## Structure

One folder per chapter. Folders are named `chX` (e.g., `ch10`).

```
story/ch10/
  chapter10.annotated.md ← editable source with craft comments, when used
  chapter10.md           ← generated commentless prose for reading/publishing
  summary.md      ← what happened (load this for context before writing)
  notes.md        ← author craft notes, research, decisions
  plan.md         ← planning / what to write next (unwritten chapters)
```

Not every folder has every file. Chapters using line-level annotation have both `chapterX.annotated.md` and its compiled `chapterX.md`; older chapters may have only `chapterX.md` until they enter this workflow.

No underscore prefix. No numbering in non-prose filenames. The folder name carries the chapter number.

## The Iceberg

Three layers, each serving a different job:

1. **Chapter prose** (`chapterX.annotated.md` source; compiled `chapterX.md`) — tip of the iceberg. The compiled prose stands alone. The reader never needs the wiki.
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

Exceptions (3rd person):
- Ch 6 — Fuji, limited
- Ch 13 — Fuji, limited
- Ch 16 — near-omniscient, not really anchored to a POV

When drafting, confirm the POV for the chapter from the plan or notes before writing.

## Annotated Prose and Compilation

When `chapterX.annotated.md` exists, it is the **only editable prose source**. Never revise its generated `chapterX.md` directly.

Place reasoning in a standalone comment block after the paragraph or dialogue unit it supports. The `<!--` opener must begin on its own line; never append it to prose:

```md
Oak studied him with a grin. "Being Champion isn't easy, is it?"

<!--
Establishes shared experience while letting Oak test how Lance is carrying the office.
-->
```

Annotation rules:

- Explain function; do not merely paraphrase the prose.
- Annotate decisions worth preserving, not every self-evident sentence. If a line has no defensible purpose, revise or delete it instead of inventing a justification.
- Update or delete an annotation whenever its prose changes.
- Keep comments out of `chapterX.md`; the compiler removes every HTML comment.

Compile one or more annotated chapters with:

```sh
python3 scripts/compile_chapter.py story/ch17.5/chapter17.5.annotated.md
```

Use `--check` to verify that generated prose is current without rewriting it:

```sh
python3 scripts/compile_chapter.py --check story/ch17.5/chapter17.5.annotated.md
```

Compile or check every annotated chapter at once:

```sh
python3 scripts/compile_chapter.py --all
python3 scripts/compile_chapter.py --all --check
```

## Prose Conventions

See root `AGENTS.md` for full style rules. Key points:
- **Selective detail:** Do not inventory scenes. Foregrounded details create reader expectations; omit incidental measurements and logistics unless they matter.
- Em dash: `---` (three hyphens)
- Ellipsis: `...` (three periods, no unicode)
- Quotes: plain ASCII `"` and `'`
- `Pokeball`, `Pokedex`, `Potion`
- `Pokemon` or `Pokémon`, never both in one file

## Revision Workflow

- For requested prose revisions, edit `chapterX.annotated.md` when it exists, compile `chapterX.md`, and leave both uncommitted for author review. If no annotated source exists, edit `chapterX.md` directly until that chapter is migrated.
- Record important line-level reasoning in the annotated source while revising. Report what changed and any unresolved concern to the author; do not duplicate every annotation in chat unless asked. Commit only with explicit author approval.
- Update `CHANGELOG.md` with substantive published-prose revisions. Record the resulting reader-visible change, not the editing process; omit routine metadata, notes, formatting, and typo fixes.

## Linking to Story Files

From KB: `../../story/ch10/chapter10.md`
From agent prompt: `story/ch10/summary.md`

For links to references outside this repo (especially KB files resolved via `$MERIDIAN_CONTEXT_KB_DIR`), follow root `AGENTS.md` link guidance: do not use local filesystem path links; use GitHub URLs (reference-style links preferred).
