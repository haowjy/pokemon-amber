# Task: Lighten the Style Files

The current style files in $MERIDIAN_FS_DIR/styles/ are over-prescribed. They catalog every instance rather than teaching the principle. A writer reading them gets a reference manual when they need a compass.

## What to change

Rewrite each style file with this approach:
- **Principle first** — state the core insight in a few sentences. What's the pattern? Why does it work?
- **Representative examples** — one or two examples that *show* the principle. Pick the best ones, not all of them.
- **Chapter pointers** — reference where the writer can see more ("see Ch. 15 confrontation, Ch. 9 caffeine rant") so they can go read the source text themselves.
- **Not exhaustive catalogs** — don't list every instance. Don't break things into 7 sub-categories with 3 examples each. A writer who internalizes the principle will produce natural variation. A writer following a checklist produces something mechanical.

The goal: a writer reads the file, understands the voice, and writes. They don't need to keep the file open as a reference while drafting.

## Current files to rewrite
Read all of these in $MERIDIAN_FS_DIR/styles/:
- char-amber-narration.md (14.7KB — way too long)
- char-amber-dialogue.md
- char-fuji.md
- char-oak.md
- char-erika.md
- char-supporting.md
- scene-battle.md
- scene-discovery.md
- scene-emotional.md
- scene-tension.md

Also read the original analysis reports in .meridian/work/style-extraction/brainstorm/ if you need more context on what the patterns actually are.

## What to preserve
- The per-character organization (Amber gets two files, Fuji/Oak get one each, etc.)
- The scene-type files staying scene-bound
- Self-describing headers so orchestrators know when to load each file
- Concrete examples with chapter citations — just fewer of them

## What to cut
- Exhaustive audience-by-audience breakdowns
- Quantitative stats (32% of dialogue paragraphs, 83% mixed, etc.) — that's analysis data, not writing guidance
- Complete lists of action beats, humor techniques numbered 1-7, etc.
- Anything that reads like a catalog rather than a guide
