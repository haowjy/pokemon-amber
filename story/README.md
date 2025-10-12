# Story Structure

Preferred layout for chapter-local notes:

- `story/chapterX/` (folder per chapter)
  - `chapterX.md` (chapter file)
  - `_Xnotes.md` (primary author notes for this chapter)
  - `_Xsummary.md` (chapter summary for reference)
  - `characters.md` (optional, chapter-specific character notes)
  - `pokemon.md` (optional, chapter-specific Pokemon notes)

Current state
- Chapters live under `story/chapterX/chapterX.md`.
- Notes and summaries are numbered to match the chapter folder: `_Xnotes.md`, `_Xsummary.md` (e.g., `story/chapter10/_10notes.md`).

Notes/summary filename change (October 2025)
- Old names: `_notes.md`, `_summary.md`
- New names: `_Xnotes.md`, `_Xsummary.md` where `X` is the chapter number (e.g., `_14summary.md`).
- Rationale: Easier skimming in editors and file pickers; reduces ambiguity when multiple chapter folders are open; consistent with authoring conventions that prefer clear, sortable filenames.

Linking
- When linking from the wiki, prefer: `../story/chapterX/_Xnotes.md` and `../story/chapterX/_Xsummary.md`.
