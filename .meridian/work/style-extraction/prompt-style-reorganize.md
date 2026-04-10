# Task: Reorganize Style Files — Per-Character with Natural Splits

The current style files need reorganization. The key changes:

1. **Per-character files, not one dialogue file.** Each character gets their own file(s) covering everything about how they show up in prose — narration voice (if POV character), spoken dialogue, action beats, register shifts, how they change by audience.

2. **Multiple files per character when warranted.** Don't force everything into one file. If a character has genuinely distinct modes (e.g., Amber's 1st-person narration vs her spoken dialogue vs her different emotional registers), split them naturally. But don't split artificially — Ash probably just needs one file.

3. **Drop formatting.md.** Punctuation conventions are in CLAUDE.md. Quantitative patterns (sentence stats, paragraph distributions) are reference data, not writing guidance. Absorb any character-specific patterns (Amber's sentence rhythm, paragraph style) into the relevant character files.

4. **Scene-type files stay.** Battle, discovery, emotional, tension — these are scene-bound and work fine as separate files.

5. **Tone/humor can stay or merge into character files** — decide based on whether humor mechanics are Amber-specific or cross-character.

## What exists now (read these)
Style files in .meridian/fs/styles/:
- voice-amber-1p.md, voice-fuji-3p.md, voice-oak-3p.md (narration voices)
- dialogue-voices.md (all 9 characters in one file)
- scene-battle.md, scene-discovery.md, scene-emotional.md, scene-tension.md
- tone-humor.md
- formatting.md

Also read the original analysis reports in .meridian/work/style-extraction/brainstorm/ for full context:
- amber-narrative-voice.md, third-person-pov.md, character-dialogue-voices.md, scene-type-variation.md, mechanical-patterns.md

## Principles
- Let the analysis determine splits. Don't prescribe a taxonomy.
- Each file should be self-describing — an orchestrator reading it should know when to load it.
- Include concrete examples with chapter citations.
- An orchestrator dispatching a writer for a scene should think "which characters are in this scene?" and load those character files + relevant scene-type files.

## Output
- Delete the old files that are being replaced (voice-*.md, dialogue-voices.md, formatting.md, tone-humor.md)
- Create new per-character files in .meridian/fs/styles/
- Keep scene-type files if they're fine as-is, or update them if needed
- Leave .meridian/fs/issues/ alone — those are correct
