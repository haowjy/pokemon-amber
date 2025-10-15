# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Pokemon fanfiction repository for "Pokemon: Ambertwo" - an AI-assisted creative writing project about an isekai'd Pokemon fan who becomes Dr. Fuji's clone, Amber. The story combines elements from anime, games, and manga with a grittier, more realistic take on the Pokemon world.

## Repository Structure

```
pokemon-amber/
├── story/           # Chapter files organized by folder
│   ├── chapterX/
│   │   ├── Xchapter.md      # Published chapter content
│   │   ├── _Xnotes.md       # Author notes (hidden)
│   │   └── _Xsummary.md     # Chapter summary
├── wiki/            # World-building & reference docs
│   ├── characters/          # Character profiles
│   ├── arcs/                # Story arc outlines  
│   ├── lore/                # World mechanics & systems
│   └── pok-locations/       # Location details
├── .cursor/rules/   # Writing guidelines & style rules
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

**Author notes:**
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

## Writing Style Guidelines

**Punctuation:**
- Em dash: Use three hyphens `---` in source
- Ellipsis: Three periods `...` (no unicode)
- Quotes: Plain ASCII `"` and `'`

**Content rules:**
- Keep official prose clean (no inline author commentary)
- Use `hidden: true` for content not meant to be exported
- Update `updated:` date when making substantive edits

**File organization:**
- Chapters are organized in numbered folders under `story/`
- Each chapter has three files: the chapter itself, notes, and summary
- Wiki serves as shared knowledge base for consistency tracking
- `.cursor/rules/` contains AI writing prompts and style guides

## Key Writing Aids

The `.cursor/rules/` directory contains:
- `authoring-conventions.mdc` - File naming and YAML requirements
- `general.mdc` - Punctuation and spelling conventions

### Style Guides (`.cursor/rules/styles/`)

Six specialized style guides for different scene types. All are `alwaysApply: false` - read the actual file before writing:

- **`pokemon-writer.mdc`** - Master prose guide. Read for overall narrative voice and formatting conventions (passage by passage, code blocks vs block quotes)
- **`style-normal.mdc`** - Default Amber voice for everyday scenes. Read for adult/child split, humor techniques, and tonal balance
- **`style-dialogue.mdc`** - Conversation scenes. Read before writing dialogue-heavy passages
- **`style-battle.mdc`** - Pokemon battles. Read before writing combat sequences
- **`style-discovery.mdc`** - Exploration/new location scenes. Read before writing discovery moments or first impressions of places
- **`style-summaries.mdc`** - Chapter summaries only. Read before creating `_Xsummary.md` files

**Important:** When writing prose, read the relevant style guide(s) first. The files contain specific examples from the story showing how techniques are applied.

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

The repository tracks a creative writing project with multiple content types. Most changes will be to markdown files in `story/` and `wiki/` directories. The `.cursor/rules/` files define writing conventions that should be preserved when making edits.