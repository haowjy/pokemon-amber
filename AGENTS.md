# AGENTS.md

Project guidance for agents working in this repository.

## Project Overview

Pokemon: Ambertwo — a fanfiction about an isekai'd adult consciousness inhabiting Dr. Fuji's clone, Amber. Grittier and more realistic than canon. Combines anime, games, and manga sources.

## Repository Structure

```
pokemon-amber/
├── story/                # Chapter prose. One folder per chapter.
│   └── chX/
│       ├── chapterX.md   # Published prose
│       ├── summary.md    # What happened (load for context)
│       ├── notes.md      # Author craft notes
│       └── plan.md       # Planning for unwritten chapters
└── .meridian/kb/         # Author's working knowledge base.
    ├── wiki/             # Entity, concept, and summary pages
    ├── styles/           # Voice/tone reference for writing
    ├── issues/           # Craft backlog
    └── research/         # Raw external sources
```

See `story/AGENTS.md` for story file conventions.
See `.meridian/kb/AGENTS.md` for KB conventions and operations.

## File Naming

- **Chapter folders:** `story/chX/` (e.g., `story/ch10/`)
- **Chapter prose:** `chapterX.md` — number in filename so editor tabs are readable
- **summary.md** — what happened; load for context before writing adjacent chapters
- **notes.md** — author craft notes, character research, decisions
- **plan.md** — planning for unwritten chapters
- **No underscore prefix** — folder placement makes purpose clear
- **KB pages:** kebab-case (e.g., `amber-mc.md`, `team-rocket.md`)

## Writing Style

**Point of View**
- Default: Amber's 1st person
- Ch 6 (Fuji), Ch 13 (Oak), Ch 16 — 3rd person limited for moments Amber can't witness

**Punctuation**
- Em dash: `---` (three hyphens)
- Ellipsis: `...` (three periods, no unicode)
- Quotes: plain ASCII `"` and `'`

**Spelling**
- `Pokemon` — consistent within a file (ASCII or accented, not both)

**Content rules**
- No inline author commentary in published prose
- Update `updated:` date on chapter frontmatter when making substantive edits

## Key Writing Aids

- **Style references** — `.meridian/kb/styles/`. Voice, tone, scene-type techniques grounded in actual prose.
- **Known issues** — `.meridian/kb/issues/`. Cross-cutting craft problems to watch for.
- **Wiki** — `.meridian/kb/wiki/`. Characters, lore, plot threads, events.

## Conversation Guidelines

Be harsh and critical when evaluating ideas. Support critiques with specific examples — search the web if needed.

### Planning Future Story Content

**DO:**
- Answer worldbuilding/mechanics questions directly
- Present multiple options without advocating for one
- Ask clarifying questions before building on ideas

**DON'T:**
- Invent character dialogue or psychology unless asked
- Suggest specific plot beats or scene structures unprompted
- Build elaborate scenarios from assumptions

❌ "Here's how the confrontation should go... and then in Arc 2..."
✅ "What tone do you want for the confrontation? Defensive, guilt-ridden, something else?"
