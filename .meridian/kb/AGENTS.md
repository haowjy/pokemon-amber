# kb/AGENTS.md

The kb is an LLM-maintained author wiki: a persistent, compounding artifact
of everything known about Pokemon: Ambertwo, with the LLM doing the
cross-referencing and bookkeeping. Inspired by the Karpathy LLM-wiki
pattern, adapted for an author's working knowledge --- includes spoilers,
intent, and unrevealed canon.

## Layout

- `wiki/`           Entity, concept, and summary pages. The wiki proper.
- `research/`       Raw external sources (Pokemon canon notes, real-world
                    refs) cited by wiki pages. Inputs, not knowledge.
- `styles/`         Voice/tone reference loaded by writer agents.
                    About *how to write*, not *what is true*.
- `issues/`         Craft backlog --- recurring prose patterns,
                    mechanical tics. Workflow queue, not knowledge.

## What lives in `wiki/`

| Folder              | Page type | What it holds                                  |
|---------------------|-----------|------------------------------------------------|
| `characters/`       | Entity    | One page per named character                   |
| `places/`           | Entity    | Cities, routes, buildings, regions             |
| `organizations/`    | Entity    | Team Rocket, Ranger Union, Ace Trainers, etc.  |
| `events/`           | Entity    | Specific story moments (Pallet attack, etc.)   |
| `arcs/`             | Concept   | Arc-level pages, both canon and planned        |
| `plot-threads/`     | Concept   | Ongoing storylines spanning multiple chapters  |
| `lore/`             | Concept   | Mechanics, systems, worldbuilding              |
| `themes/`           | Concept   | Abstract author concerns                       |
| `summaries/`        | Summary   | Per-chapter and per-research-source summaries  |
| `contradictions/`   | Backlog   | Canon facts that conflict, awaiting resolution |
| `index.md`          | Catalog   | Every page with a one-line summary             |
| `log.md`            | Log       | Append-only operations record                  |
| `timeline.md`       | Synthesis | Cross-cutting chronology                       |

## Page conventions

Every wiki page should:

- Have a clear subject (the page name = the subject)
- Cite chapters by `[chN]` or `[chN §X]` for any claim grounded in
  published prose
- Cite `research/<file>` for any claim grounded in external research
- Cross-link other wiki pages with `[[page-name]]` style references
- Include status as a property: `canon` | `drafting` | `speculation`
  - `canon` --- locked in by published chapters, cite which
  - `drafting` --- author has decided, not yet shown in prose
  - `speculation` --- under consideration, not committed

Author notes / spoilers / intent are welcome on any page --- this is an
author wiki, not a reader wiki. Mark unrevealed material clearly so a
reader-mode export could filter it later if ever needed.

## Operations

The three things agents do with the kb. Each operation has an entry-point
agent in the creative-writing-skills package.

### Ingest

When a new chapter publishes or a research source is added, integrate it:

1. Read the source
2. Write a summary page in `wiki/summaries/`
3. Identify entities/concepts the source touches; update their pages
4. Update `wiki/index.md` for any new pages
5. Append a line to `wiki/log.md`

Entry point: `chronicler` agent. For chapter ingest, pass the chapter
file. For research ingest, pass the research file.

### Query

When asked something about the project, prefer the wiki over re-reading
chapters:

1. Read `wiki/index.md` to locate relevant pages
2. Read those pages, follow cross-references
3. If the answer is worth keeping, file it as a new concept page or
   update an existing one

Entry point: `explorer` agent for fast lookup.

### Lint

Periodic health check:

- Orphan pages (no incoming links from index or other pages)
- Stale claims (entity page contradicts latest chapter summary)
- Missing cross-references (entity mentioned in summary but no page exists)
- Broken `[[wiki-link]]` references
- Canon contradictions --- file to `wiki/contradictions/`
- Craft issues --- file to `kb/issues/`

Entry point: `chronicler` or `continuity-checker`.

## What does NOT belong in the wiki

- Raw chapter prose --- stays in `story/` (main repo)
- Author voice rules --- `kb/styles/`
- Recurring prose problems --- `kb/issues/`
- Generic writing craft --- `.agents/skills/` (creative-writing-skills package)

## Sync

This kb is synced to a separate repo via meridian's autosync feature. Tool
state (sessions, work-items, locks) stays in the main repo's `.meridian/`
and is NOT part of the kb sync.

Chapters live in the main repo at `story/chapterX/`. Wiki pages reference
them by canonical `[chN]` notation without filesystem paths.
