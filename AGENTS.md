# AGENTS.md

This file provides guidance to agents when working with the files in this project.

## Project Overview

This is a Pokemon fanfiction repository for "Pokemon: Ambertwo" - a creative writing project about an isekai'd Pokemon fan who becomes Dr. Fuji's clone, Amber. The story combines elements from anime, games, and manga with a grittier, more realistic take on the Pokemon world.

## Repository Structure

```
pokemon-amber/
├── story/           # Chapter files organized by folder
│   ├── chapterX/
│   │   ├── Xchapter.md      # Published chapter content
│   │   ├── _Xnotes.md       # Author notes (hidden)
│   │   └── _Xsummary.md     # Chapter summary
├── future/          # Brainstorming and planning for future story arcs
├── wiki/            # World-building & reference docs
│   ├── characters/          # Character profiles
│   ├── arcs/                # Story arc outlines  
│   ├── lore/                # World mechanics & systems
│   └── pok-locations/       # Location details
├── .agents/skills/  # Writing style guides & conventions (Meridian skills)
└── scripts/         # Conversion utilities
```

## File Naming Conventions

**Critical naming rules:**
- **Official content:** No leading underscore (e.g., `1chapter.md`, `amber-mc.md`)
- **Author notes/drafts:** Leading underscore (e.g., `_1notes.md`, `_1summary.md`)
- **Chapter files:** Named `Xchapter.md` inside `story/chapterX/` folders
- **Chapter notes:** Numbered to match folder (e.g., `_10notes.md` in `chapter10/`)

## YAML Front Matter Requirements

All authoring files must include YAML front matter. Key schemas:

**Story chapters:**
```yaml
---
title: "[Chapter 1] Truck-kun Strikes Again"
chapter: 1
arc: cinnabar
pov: Amber Fuji
status: draft # or published
hidden: false
created: 2025-09-20
updated: 2025-09-20
---
```

**Author notes (chapter-local):**
```yaml
---
type: note
scope: chapter
chapter: 1
spoilers: true
status: draft
hidden: true
created: 2025-09-20
updated: 2025-09-20
---
```

**Arc notes:**
```yaml
---
type: note
scope: arc
arc_id: arc01-celadon
chapters: [7, 8, 9, 10]
spoilers: true
status: draft
hidden: true
updated: 2025-09-20
---
```

**Global notes (worldbuilding, continuity, etc.):**
```yaml
---
type: note
scope: global
category: worldbuilding # or continuity, themes, mechanics
spoilers: false
status: draft
hidden: true
updated: 2025-09-20
---
```

**Wiki pages:**
```yaml
---
type: wiki
category: events # or chapters, index
title: Pallet Town Attack
requires_citations: true
status: published
updated: 2025-09-20
---
```

## Writing Style Guidelines

**Point of View:**
- Default: Amber's 1st person perspective
- Chapters 6, 13, 16 use 3rd person POV (Fuji, Oak) for critical moments Amber doesn't witness
- See `story/README.md` for details

**Punctuation:**
- Em dash: Use three hyphens `---` in source
- Ellipsis: Three periods `...` (no unicode)
- Quotes: Plain ASCII `"` and `'`
- Hyphen `-` for compound words (e.g., 8-bit); em dash `---` for breaks/asides

**Spelling:**
- `Pokemon` (ASCII) or `Pokemon` (accented) — be consistent within a file

**Content rules:**
- Keep official prose clean (no inline author commentary)
- Use `hidden: true` for content not meant to be exported
- Update `updated:` date when making substantive edits

**File organization:**
- Chapters are organized in numbered folders under `story/`
- Each chapter has three files: the chapter itself, notes, and summary
- Wiki serves as shared knowledge base for consistency tracking

## Key Writing Aids

**Style reference files** live in `.meridian/fs/styles/`. These are grounded in the actual prose from chapters 1-17 — character voices, scene-type techniques, tonal registers. Writer and critic agents load individual files via `-f` based on what the scene needs.

**Known issues** live in `.meridian/fs/issues/`. Cross-cutting problems identified during analysis — mechanical tics, emotional inconsistencies, structural limitations.

**Writing skills** (generic craft, not project-specific) are in `.agents/skills/` via the creative-writing-skills package. These include `prose-writing`, `prose-critique`, `writing-principles`, etc.

**Important:** When writing prose, read the relevant style files first. They contain specific examples from the story showing how the voice works.

## Content Organization

**Story content:**
- Linear chapter progression in numbered folders
- Each chapter includes author notes for intent/foreshadowing
- Summaries follow specific formatting for consistency

**Wiki content:**
- Characters, locations, lore, and timeline documentation
- Citations required back to specific chapters
- Organized by category (characters, arcs, lore, locations)

## Version Control Notes

The repository tracks a creative writing project with multiple content types. Most changes will be to markdown files in `story/` and `wiki/` directories. Writing conventions are defined in `.agents/skills/` and should be preserved when making edits.

## Conversation Guidelines

  When discussing ideas, don't be afraid to be harsh and critical about my ideas. Justify your critiques with specific
  examples and evidence (search the internet to support your critiques, if necessary).

  ### Planning Future Story Content (IMPORTANT)

  When discussing future/unwritten story content:

  **DO:**
  - Answer worldbuilding/mechanics questions directly (fainting rules, economics, systems)
  - Present multiple OPTIONS without advocating for any particular one
  - ASK clarifying questions: "What do you want to happen here?" "How do you see this character?"
  - Wait for confirmation before building on ideas
  - Focus on the specific question asked

  **DON'T:**
  - Invent character dialogue, motivations, or psychology unless explicitly requested
  - Suggest specific plot beats or scene structures ("Here's how the confrontation should go")
  - Build elaborate scenarios based on assumptions ("In Arc 2, here's what could happen...")
  - Present recommendations as if they're the "right" answer
  - Add narrative details beyond what was asked

  **Example:**
  - ❌ BAD: "Here's the confrontation scene with this dialogue... and then in Arc 2 you could..."
  - ✅ GOOD: "For the confrontation, what tone do you want? Should he be defensive, guilt-ridden, or something else?"