# Repository Guidelines

## Project Structure & Module Organization
Drafted prose lives in `story/`, where each `chapterN/` directory bundles the published draft (`Nchapter.md`), internal notes (`_Nnotes.md`), and recap (`_Nsummary.md`). Long-term continuity tools sit in `wiki/`, organized by theme (`characters/`, `lore/`, `pok-locations/`, etc.). Shared tone, punctuation, and formatting expectations are collected in `.cursor/rules/`; skim these before starting a new scene so the voice stays consistent.

## Authoring & Review Workflow
- Open the relevant `story/chapterN/` trio together; update prose, notes, and summary in the same pass.
- Use `rg "Amber"` or similar quick searches to cross-check past appearances, quotes, or moves before introducing new details.
- Preview Markdown in your editor or reader of choice before submitting; front matter and heading hierarchy should render cleanly.

## Style & Naming Conventions
Keep Markdown ASCII-friendly: em dashes as `---`, ellipses as `...`, and straight quotes only. Every writable file begins with YAML front matter; refresh fields like `updated:` and `status:` when you change intent. Canon prose files avoid leading underscores, while in-progress or spoiler-heavy pieces use them for clarity. Chapter filenames always mirror their folder number (e.g., `story/chapter12/12chapter.md`) to support automation and human scanning alike.

## Continuity & Quality Checks
Treat lore accuracy as your test suite. Confirm summaries cite the right events, make sure `hidden:` flags are set for anything not ready to publish, and revisit `wiki/index.md` whenever you add world facts so you can drop in backlinks. Before proposing a change, reread adjacent chapters to keep tone, pacing, and character voices aligned.

## Commit & Pull Request Guidelines
Commits should stay focused and use present-tense summaries (`clarify cinnabar lab timeline`, `add oak POV notes`). When opening a PR, include a concise overview, the chapters or wiki files touched, spoiler level, and whether the change affects the Royal Road release schedule. Screenshots of rendered Markdown help reviewers catch layout quirks quickly.

## Agent Collaboration Tips
Reset context by reviewing `.cursor/rules/authoring-conventions.mdc` and `general.mdc` before drafting; these files anchor house style and terminology. Update summaries and notes alongside the main chapter so future collaborators understand your intent. Tag unanswered questions or TODOs directly in `_Nnotes.md`, and prefer `hidden: true` on experimental prose until the lead author approves publication.
