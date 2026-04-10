# Task: Create Style Files from Voice Analysis Reports

You have five detailed analysis reports from agents who read all 17 chapters of Pokemon: Ambertwo. Your job is to synthesize these into style files for `$MERIDIAN_FS_DIR/styles/` and log identified writing issues separately.

## Important principles

- Let the analysis determine how the style files are organized. Don't force a predetermined taxonomy.
- The style files should teach a writer how to reproduce these patterns. Include concrete examples (the reports are full of them).
- Distinguish between **intentional patterns to reproduce** (style files) and **issues to fix** (logged separately). Tics, inconsistencies, and craft problems go in the issues, not the style files.
- Style files should be self-describing — an orchestrator reading them should understand what kind of scene/character/register each one covers without needing external documentation.
- Some dimensions are character-bound (Amber's adult/child split), some are scene-bound (action pacing), and some are both (the dual-lens discovery mode is both scene-type AND character-specific to Amber). Let the files reflect that naturally.
- The story has 3 POV characters: Amber (1st person, most chapters), Fuji (3rd person, chapters 6 and 13), Oak (3rd person, chapter 16). Each has a distinct voice.
- Characters also have distinct dialogue voices that are separate from their narration/POV voice.
- Action/battle technique should be relatively consistent across POVs — it's scene-bound, not character-bound. The character lens colors it but the underlying mechanics stay the same.

## What to create

### Style files in .meridian/fs/styles/
Organize however the analysis suggests. Each file should:
- Describe what it covers and when a writer should use it
- Include concrete examples with chapter citations
- Be specific enough to actually guide writing, not just describe patterns abstractly

### Writing issues in .meridian/fs/issues/
Log issues the analysis identified — things to fix, not things to reproduce. Each issue should be a separate file or clearly separated entry with:
- What the issue is
- Evidence (quotes, counts, chapter references)
- Scope (word-level tic, scene-level inconsistency, structural problem, etc.)
- Which chapters are affected

Examples of issues from the reports:
- Mechanical tics: "for a moment" x29, "cut through the" x19, "before I could" x16
- Emotional scene inconsistency: middle chapters don't commit to the emotional prose register
- Battle scale: prose technique doesn't differentiate small fights from apocalyptic confrontations
- Ch. 11 emotional gap: high-stakes content but Amber is passive, reads as observation not feeling

## What NOT to do
- Don't copy the reports wholesale. Synthesize across all five — the same pattern often shows up in multiple reports from different angles.
- Don't include the `_ref-*` files or project-local skill content. These style files replace those.
- Don't prescribe naming conventions from above — name files based on what they contain.

## Reports to synthesize
The five analysis reports are in .meridian/work/style-extraction/brainstorm/:
- amber-narrative-voice.md (Opus) — Amber's 1st person voice: sentence patterns, adult/child split, humor mechanics, tonal range, pop culture references
- third-person-pov.md (GPT-5.4) — Fuji and Oak 3rd person chapters: how voice shifts, each character's POV style, transition techniques
- character-dialogue-voices.md (GPT-5.4) — per-character speech patterns: Amber, Fuji, Oak, Erika, Kayla, Mary, Stephen, Delia, Ash
- scene-type-variation.md (Sonnet) — how prose shifts by scene type: battle, discovery, emotional, comedy, exposition, tension
- mechanical-patterns.md (GPT-5.2) — quantitative patterns: sentence length, openers, paragraph structure, punctuation, dialogue mechanics, repetition
