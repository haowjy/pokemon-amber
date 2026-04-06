# Repo Restructure: Findability & Connectivity

## Problem

Information about the same topic is scattered across `wiki/`, `future/`, and `story/` chapter notes with no systematic cross-referencing. Connections between documents live in the author's head, not in the files.

**Example — "everything about Mewtwo" requires checking 6+ files across 3 directory trees:**
- `wiki/characters/mewtwo.md`
- `future/plot/_mewtwo-thread.md`
- `wiki/characters/amber-mc.md` (mentions connection)
- `wiki/characters/ditto.md` (shares Mew clone origin)
- `wiki/arcs/1-the-perfect-family/events/1-mewtwo-escape.md`
- `future/arcs/saga-overview.md`

Cross-references exist in some files but are manual and inconsistent. Some link forward but not back.

**The wiki/future split is artificial.** `wiki/characters/` has established characters, `future/characters/` has planned ones. Both are character docs — the difference is publication status, but they live in separate trees with no links.

`current-direction.md` is declared source of truth but nothing points back to it.

## Options to Explore

1. **YAML `references` field** — docs declare relationships, machine-searchable
2. **Topic index files** — one file per major topic collecting all references
3. **Agent-maintained connectivity** — periodic scan for cross-reference gaps
4. **Collapse wiki/future into one reference tree** — split by topic not status
5. Some combination

## Scope

- Audit current cross-references and find gaps
- Propose a connectivity scheme
- Propose any folder restructuring if warranted
- Consider how agents/skills would work within the new structure
- Don't change story content — this is about reference/planning docs

## Key Files

- `wiki/index.md` — current manual index (stale)
- `future/current-direction.md` — declared source of truth
- `future/_open-questions.md` — decision tracker
- `CLAUDE.md` — repo structure docs and YAML schemas
