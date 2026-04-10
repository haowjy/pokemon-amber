# Repository Structure Audit

**Scope:** wiki/, future/, story/ chapter notes
**Date:** 2026-04-05
**Work item:** repo-restructure-connectivity

---

## 1. Complete Directory Tree

### wiki/

```
wiki/
├── index.md                          [wiki index — stale, broken links]
├── timeline.md                       [overall story timeline]
├── arcs/
│   └── 1-the-perfect-family/
│       ├── outline.md                [arc outline — Arc 0]
│       └── events/
│           ├── 1-mewtwo-escape.md    [event summary]
│           ├── 2-celadon-oddish-heist.md
│           ├── 3-forest-path-incident.md
│           └── 4-pallet-attack.md
├── characters/
│   ├── amber-mc.md                   [MC profile — main spoiler-heavy doc]
│   ├── delia-ketchum.md
│   ├── ditto.md                      [Amber's Ditto — minimal stub]
│   ├── dr-fuji.md
│   ├── erika.md
│   ├── kaede.md
│   ├── mary.md
│   ├── mewtwo.md                     [minimal stub]
│   └── professor-oak.md              [draft]
├── lore/
│   ├── _aura-and-bonds.md            [hidden, author-only — type: lore (non-standard)]
│   ├── _plot-secrets.md              [hidden, now gutted index pointing elsewhere]
│   ├── _world-mechanics.md           [hidden, author-only mechanics]
│   ├── aura-system.md                [published-facing aura doc]
│   ├── economy.md                    [currency, pricing examples]
│   ├── index.md
│   ├── trainer-systems.md            ⚠️ NAMING COLLISION with trainer-systems/ dir below
│   ├── crime/
│   │   └── poaching.md
│   ├── economics/
│   │   └── pokeball-pricing.md
│   ├── government/
│   │   └── champion-system.md
│   ├── history/
│   │   ├── gym-evolution.md
│   │   └── kanto-johto-unification-war.md
│   ├── mechanics/
│   │   └── pokemon-fainting.md
│   ├── organizations/
│   │   ├── ace-trainers.md
│   │   ├── ranger-union.md
│   │   └── team-rocket.md
│   ├── tech/
│   │   ├── communications.md
│   │   ├── identity-security.md
│   │   ├── index.md
│   │   └── transportation.md
│   └── trainer-systems/
│       ├── badge-system.md
│       ├── conference-system.md      [promoted from future/worldbuilding/]
│       ├── gym-system.md             [promoted from future/worldbuilding/]
│       ├── index.md
│       ├── international-licensing.md
│       ├── quest-system.md
│       └── trainer-paths.md          [promoted from future/worldbuilding/]
├── pok-locations/
│   ├── celadon-area/
│   │   ├── celadon-city.md
│   │   ├── celadon-gym.md
│   │   └── celadon-pokemon-center.md
│   ├── cinnabar-island/
│   │   ├── cinnabar-gym.md           ⚠️ title says "Cinnabar Island" (copy-paste error)
│   │   ├── cinnabar-island.md
│   │   └── flame-forest.md
│   ├── pallet-town-area/
│   │   └── pallet-town.md
│   └── viridian-area/
│       └── viridian-hinterlands.md
└── pokemon-teams/
    └── team-amber-mc.md              [hidden — Amber's team planning]
```

**Total wiki files:** 53 (51 .md + 2 .DS_Store)

---

### future/

```
future/
├── README.md                         ⚠️ NO YAML front matter
├── TONE.md                           [story tone/approach guidance]
├── _archive-completed.md             [completed decisions archive]
├── _open-questions.md                [active decision tracker]
├── current-direction.md              [declared source of truth]
├── arcs/
│   ├── arc-4ever.md                  [seed-status arc idea]
│   ├── arc-celadon.md                [seed-status]
│   ├── arc-kitakami.md               [seed-status]
│   ├── arc-pikachu-handoff.md        [seed-status]
│   ├── arc1-kanto-year1.md           [planned, next arc]
│   ├── arc2-hoenn.md                 [draft]
│   ├── arc3-beyond.md                [draft]
│   └── saga-overview.md              [high-level saga structure]
├── characters/
│   └── kyle-kong.md                  [planned character — not yet written]
├── core/
│   ├── meta-notes.md                 [meta-authorial notes]
│   └── themes.md                     [confirmed story themes]
├── episodes/
│   ├── kyle-meeting.md               [scene draft]
│   ├── pewter-gym-brock.md           [scene draft]
│   └── route1-solo.md                [scene draft]
├── plot/
│   ├── _mewtwo-thread.md             [seed-status plot thread]
│   ├── forged-documents.md           [confirmed plot thread]
│   ├── giovanni-fuji-jail.md         [planned]
│   ├── oak-role-options.md           [decided]
│   ├── saffron-gym-rivalry.md        [draft]
│   └── team-rocket-surveillance.md   [idea-to-explore]
├── team/                             ⚠️ EMPTY DIRECTORY
└── worldbuilding/
    ├── clan-system.md                [idea-to-explore — Johto/Kanto clan distinction]
    ├── economic-reality.md           [confirmed — partially promoted to wiki]
    ├── gym-system-detailed.md        [confirmed — partially promoted to wiki]
    └── quarterly-conference-system.md [confirmed — partially promoted to wiki]
```

**Total future files:** 26 .md files + 1 empty directory

---

### story/ chapter notes (for cross-reference analysis)

17 chapters each with `_Xnotes.md` and `_Xsummary.md`. Notable notes files examined:
- Ch1, Ch5, Ch10 — substantive, contain worldbuilding/character detail inline
- Ch3 — beats/continuity focused
- Ch7, Ch12, Ch15 — minimal (near-empty body after YAML header)
- Ch17 — explicit cross-refs to wiki/future docs

---

## 2. Category Analysis: What Lives Where and Why

### wiki/ breakdown

| Subdirectory | Content Type | Location Rationale |
|---|---|---|
| `characters/` | Character profiles for written chars | Sensible — established cast |
| `lore/` | World mechanics, systems, history | Sensible — but highly fragmented |
| `lore/trainer-systems/` | Trainer progression system | Sensible — high-quality promoted docs |
| `lore/tech/` | Communications, transport, identity | Sensible grouping |
| `lore/economics/` | Pokeball pricing | ⚠️ One file; duplicates scope with `lore/economy.md` |
| `lore/crime/` | Poaching | ⚠️ One file; should be a section of a broader lore doc |
| `lore/government/` | Champion system | ⚠️ One file orphan |
| `lore/history/` | Gym evolution, Kanto-Johto war | Reasonable grouping |
| `lore/mechanics/` | Pokemon fainting | ⚠️ One file orphan |
| `lore/organizations/` | Team Rocket, Rangers, Ace Trainers | Sensible grouping |
| `arcs/` | Event summaries + arc outline | ⚠️ Only covers Arc 0; future arcs are in future/ |
| `pok-locations/` | Location docs | Sensible |
| `pokemon-teams/` | Amber's team planning | ⚠️ Single hidden file with its own subdirectory; no siblings likely |

### future/ breakdown

| Subdirectory | Content Type | Location Rationale |
|---|---|---|
| `arcs/` | Future arc plans | Sensible — unwritten content |
| `characters/` | Planned characters | Sensible — mirrors wiki/characters/ by status |
| `core/` | Themes, meta-notes | Reasonable; somewhat arbitrary vs. other folders |
| `episodes/` | Scene drafts | ⚠️ Redundant with `plot/`? These are specific scenes; plot/ has threads |
| `plot/` | Plot threads and decisions | Sensible |
| `team/` | (empty) | ⚠️ Abandoned — should be removed |
| `worldbuilding/` | World system details | ⚠️ Partially promoted to wiki/; originals not retired |

---

## 3. wiki/future Split Analysis

### The Intended Split

AGENTS.md describes:
- `wiki/` = world-building & reference docs for consistency tracking
- `future/` = brainstorming and planning for future story arcs

The distinction is **publication/certainty status** — wiki is established fact about the written story, future is speculation about unwritten content.

### Where the Split Works

- `wiki/characters/` has Erika, Mary, Kaede, Dr. Fuji, Amber (all appear in Ch1–17)
- `future/characters/` has Kyle Kong (first appears in unwritten arc)
- `wiki/arcs/1-the-perfect-family/` covers Arc 0 (written)
- `future/arcs/arc1-kanto-year1.md` covers Arc 1 (unwritten)
- `future/current-direction.md` is appropriately in future/ as planning doc

### Where the Split Breaks Down

**1. Worldbuilding that transcends the split**

Four `future/worldbuilding/` docs cover systems that apply to the entire story, not just future arcs. Three of them have already been partially promoted to `wiki/lore/trainer-systems/`, but the originals haven't been retired. This creates a dual-source problem:

| future/ file | wiki/ counterpart | Overlap |
|---|---|---|
| `future/worldbuilding/gym-system-detailed.md` | `wiki/lore/trainer-systems/gym-system.md` | Core mechanics promoted; future/ retains arc-specific politics (Giovanni, Saffron rivalry) |
| `future/worldbuilding/quarterly-conference-system.md` | `wiki/lore/trainer-systems/conference-system.md` | Structure promoted; future/ retains story timing/tournament arc |
| `future/worldbuilding/economic-reality.md` | `wiki/lore/trainer-systems/trainer-paths.md` | Framework promoted; future/ retains character-specific details |
| `future/worldbuilding/clan-system.md` | *(no wiki counterpart)* | Fully in future; idea-to-explore status |

The promoted wiki docs are cleaner and better organized. The future/ originals have "Wiki promotion note" headers acknowledging this, but they still exist in parallel. Agents can't easily tell which is authoritative for a given piece of information.

**2. Hidden files in wiki/ that belong conceptually in future/**

Three `_` prefixed files in `wiki/lore/` are actually author-only reference material that doesn't fit wiki's "established fact" purpose:
- `wiki/lore/_world-mechanics.md` — hidden game-mechanics rules agents shouldn't cite
- `wiki/lore/_aura-and-bonds.md` — author-only aura system detail
- `wiki/lore/_plot-secrets.md` — now gutted, was a spoiler index

These are functionally the same as `future/` planning docs. They live in wiki/ but are hidden, implying the tree location doesn't map to publication status the way it should. `_plot-secrets.md` is now empty but still exists.

**3. Mewtwo as the canonical example from the brief**

The brief's example — "everything about Mewtwo requires 6+ files across 3 trees" — still holds. The files exist as described, with no systematic cross-referencing:
- `wiki/characters/mewtwo.md` — minimal stub (`status: stub`), no body content
- `future/plot/_mewtwo-thread.md` — seed-status plot thread
- `wiki/characters/amber-mc.md` — mentions connection
- `wiki/characters/ditto.md` — shares Mew clone origin
- `wiki/arcs/1-the-perfect-family/events/1-mewtwo-escape.md`
- `future/arcs/saga-overview.md`

The mewtwo.md wiki stub is the most prominent gap: it should be the authoritative reference but has no content.

**4. The arc doc split**

`wiki/arcs/` covers only Arc 0 with event files. `future/arcs/` covers all planned arcs. There's no `wiki/arcs/` entry for Arc 0's planning context (that lives in future). The wiki arc structure is an event log, not a planning tool — the distinction is reasonable but undocumented.

---

## 4. Duplicate and Near-Duplicate Documents

### Confirmed Duplicates (Same Topic, Two Trees)

| Doc A | Doc B | Nature |
|---|---|---|
| `future/worldbuilding/gym-system-detailed.md` | `wiki/lore/trainer-systems/gym-system.md` | Partial promotion — overlapping core content |
| `future/worldbuilding/quarterly-conference-system.md` | `wiki/lore/trainer-systems/conference-system.md` | Partial promotion |
| `future/worldbuilding/economic-reality.md` | `wiki/lore/trainer-systems/trainer-paths.md` | Partial promotion |
| `wiki/lore/_aura-and-bonds.md` | `wiki/lore/aura-system.md` | Same topic, same tree — one hidden author-ref, one published-facing |

### Structural Duplications (Same Purpose, Different Levels)

| File | Issue |
|---|---|
| `wiki/lore/trainer-systems.md` | Same name as `wiki/lore/trainer-systems/` directory. The .md file is a comprehensive trainer systems overview (400+ lines); the directory contains more granular docs. Redundant scope, naming collision |
| `wiki/lore/economy.md` | Broad economy overview, but `wiki/lore/economics/pokeball-pricing.md` exists in a subdirectory. Economics/ has only one file — no reason to be a subdirectory |
| `wiki/lore/_plot-secrets.md` | Gutted — now just a pointer to other files. Zero value as a document; should be deleted |

### One-File Orphan Subdirectories (future fragmentation)

These subdirectories exist for a single file each, with no siblings likely to arrive:
- `wiki/lore/crime/` → `poaching.md`
- `wiki/lore/economics/` → `pokeball-pricing.md`
- `wiki/lore/government/` → `champion-system.md`
- `wiki/lore/mechanics/` → `pokemon-fainting.md`
- `wiki/pokemon-teams/` → `team-amber-mc.md`

All of these could be files directly in `wiki/lore/` (or a broader subdirectory) without needing their own directory.

---

## 5. Chapter Notes — Worldbuilding Duplication

### Notes with significant worldbuilding content

**Chapter 5 (`_5notes.md`)**
Contains inline worldbuilding docs for:
- Licensing system (Junior Permit vs Trainer ID)
- Gym pricing (₽10,000 / ₽4,000)
- Gym structure (lobby, greenhouses, facilities)
- Money/poverty mechanics

**What's now in wiki:** The licensing system and trainer tiers are in `wiki/lore/trainer-systems.md`. The gym structure is in `wiki/lore/trainer-systems/gym-system.md`. **The chapter 5 notes have not been updated to cross-reference these wiki docs.** The inline details in Ch5 notes are now functionally redundant with (and sometimes inconsistent with) the wiki docs.

**Chapter 10 (`_10notes.md`)**
Contains detailed character profiles for Erika, Mary, Kaede (team compositions, Bulbapedia sources, personality notes). The same characters now have wiki files at `wiki/characters/erika.md`, `wiki/characters/mary.md`, `wiki/characters/kaede.md`. **The character notes in Ch10 duplicate the wiki profiles** and use Bulbapedia links rather than referencing the internal wiki. Chapters 8, 9, and 11 notes have the same pattern — they re-document Erika/Mary/Kaede inline.

**Chapter 17 (`_17notes.md`)**
The only chapter notes file that actively cross-references wiki and future:
- Explicitly links to `wiki/characters/professor-oak.md`
- Explicitly links to `future/arcs/arc-kitakami.md`
- Contains well-structured foreshadowing notes

This is the target pattern for all notes files — Ch17 shows what cross-referencing looks like when it's done.

**Chapter 1 (`_1notes.md`)**
Contains canon-research notes (Bulbapedia sources for Amber/Mewtwo origin). These are external references, not internal wiki links — appropriate since they predate most wiki content.

### Notes with minimal content

Chapters 7, 12, 15 have almost no content beyond the YAML header and a story file pointer. These are placeholder files that haven't been filled in.

### Pattern Summary

| Chapter | Status | Worldbuilding in Notes | Cross-refs to wiki/future |
|---|---|---|---|
| Ch1 | Substantive | Canon research | External Bulbapedia only |
| Ch2 | Partially substantive | Some | Some Bulbapedia |
| Ch3 | Substantive | Some | None |
| Ch5 | Very substantive | Licensing, gym, economics | None (predates wiki docs) |
| Ch7 | Minimal | None | None |
| Ch8 | Substantive | Characters | External Bulbapedia only |
| Ch9 | Substantive | Characters | External Bulbapedia only |
| Ch10 | Substantive | Characters, economics | External Bulbapedia only |
| Ch11 | Substantive | Characters | External Bulbapedia only |
| Ch12 | Minimal | None | None |
| Ch13 | Some | Some | `wiki/characters/ditto.md` |
| Ch15 | Minimal | None | None |
| Ch17 | Substantive | Foreshadowing | Both wiki/ and future/ |

**Key gap:** Ch5–Ch11 notes document worldbuilding inline that is now codified in wiki/. They don't point to wiki/ for those topics. An agent reading only the chapter notes would develop a different (often less complete) picture than one reading the wiki docs.

---

## 6. YAML Front Matter Compliance Report

### Schema Definitions (from AGENTS.md)

AGENTS.md defines schemas for:
1. Story chapters
2. Author notes (chapter-local)
3. Arc notes
4. Global notes (worldbuilding)
5. Wiki pages

### Wiki Files (expected schema: `type: wiki`, `title`, `category`, `requires_citations`, `status`, `updated`)

**Compliant:** Most wiki files follow the pattern well.

**Violations:**

| File | Issue |
|---|---|
| `wiki/characters/ditto.md` | Missing `requires_citations` |
| `wiki/characters/mewtwo.md` | Missing `requires_citations`; `status: stub` is not in schema (should be `draft`) |
| `wiki/characters/professor-oak.md` | Missing `requires_citations` |
| `wiki/lore/_aura-and-bonds.md` | `type: lore` — not a valid type (schema shows `type: wiki` or `type: note`); `status: author-reference` is non-standard |
| `wiki/lore/_plot-secrets.md` | `type: note, scope: global` — is this a wiki page or a note? Inconsistent classification in wiki/ tree |
| `wiki/lore/_world-mechanics.md` | `type: note, scope: global` — same ambiguity |
| `wiki/lore/crime/poaching.md` | Missing `requires_citations` |
| `wiki/lore/mechanics/pokemon-fainting.md` | Missing `requires_citations` |
| `wiki/lore/organizations/ace-trainers.md` | Missing `canon` field (present on most, absent here) |
| `wiki/lore/trainer-systems/international-licensing.md` | Missing `requires_citations` |
| `wiki/pok-locations/cinnabar-island/cinnabar-gym.md` | `title: Cinnabar Island` — wrong title (should be "Cinnabar Gym"); copy-paste error |
| `wiki/pok-locations/cinnabar-island/cinnabar-island.md` | `category: pok-locations` while most location files use `category: locations` (inconsistent) |
| `wiki/pok-locations/cinnabar-island/flame-forest.md` | Same `category: pok-locations` inconsistency |
| `wiki/pok-locations/viridian-area/viridian-hinterlands.md` | Same |
| `wiki/lore/history/gym-evolution.md` | `category: history` — all other lore files use `category: lore` |
| `wiki/index.md` | `canon: false` — not in schema for wiki pages; stale links to non-existent `./chapters.md` and `./arcs/1-the-perfect-family.md` |
| `wiki/pokemon-teams/team-amber-mc.md` | `type: wiki, category: pokemon-teams` — novel category with no siblings; hidden file |

**Non-standard `status` values in wiki/:**
- `stub` (mewtwo.md) — not in schema
- `author-reference` (_aura-and-bonds.md) — not in schema
- `index` (_plot-secrets.md) — not in schema
- `published` (erika.md, kaede.md, mary.md) — valid but few files reach this status

### Future Files (expected schema: `type: note`, `scope`, `category`, `spoilers`, `status`, `hidden`, `updated`)

**Violations:**

| File | Issue |
|---|---|
| `future/README.md` | NO YAML front matter at all |
| `future/arcs/arc-4ever.md` | Missing `category` field |
| `future/arcs/arc-celadon.md` | Missing `category` field |
| `future/arcs/arc-kitakami.md` | Missing `category` field |
| `future/arcs/arc-pikachu-handoff.md` | Missing `category` field |
| `future/current-direction.md` | `scope: story` — not in schema (schema shows `scope: arc`, `scope: chapter`, `scope: global`) |
| `future/_open-questions.md` | Same `scope: story` |
| `future/TONE.md` | Same `scope: story` |
| `future/arcs/arc1-kanto-year1.md` | `scope: story` |
| `future/core/meta-notes.md` | `scope: story` |
| All future/worldbuilding/ files | `scope: story` |
| Multiple future files | Missing `created` field (required per schema examples) |

**Non-standard `status` values in future/:**
- `seed` (arc files) — not in schema
- `confirmed` — not in schema (schema shows `draft`)
- `planned` — not in schema
- `decided` (oak-role-options.md) — not in schema
- `idea-to-explore` — not in schema
- `index` — not in schema
- `completed` — not in schema
- `active` — not in schema
- `planning` — not in schema

### Chapter Notes (expected schema: `type: note`, `scope: chapter`, `chapter`, `spoilers`, `status`, `hidden`, `created`, `updated`)

**Violations (near-universal):**

| File | Issues |
|---|---|
| `story/chapter3/_3notes.md` through `story/chapter17/_17notes.md` (most) | Missing `type: note`; missing `scope: chapter`; missing `chapter` number; missing `spoilers`; missing `created` |
| `story/chapter5/_5notes.md` | Has only `description`, `hidden`, `status`, `updated` |
| `story/chapter1/_1notes.md` | Best compliance — has `type`, `scope`, `chapter`, `story_file`, `spoilers`, `hidden`, `title`, `description`, `status`, `created`, `updated` but also has non-standard `title` and `description` fields |

Only Ch1 notes substantially follow the intended schema. Chapters 3–17 notes (except Ch17) use a simplified schema with just `description`, `hidden`, `status`, `updated`. None include `type: note`, `scope: chapter`, or `chapter: X`.

---

## 7. Summary of Issues by Priority

### High Priority (Structural Problems)

1. **`wiki/lore/trainer-systems.md` naming collision** — A `.md` file and a directory share the same base name. This causes ambiguity for any tool or agent navigating the tree. The file is a comprehensive overview; the directory has granular sub-docs. One needs to be renamed or merged.

2. **Partial promotions leave dual sources** — Three `future/worldbuilding/` docs have canonical content promoted to `wiki/lore/trainer-systems/`, but the originals remain. Each future file has a "Wiki promotion note" header, but the content not promoted (arc-specific politics, character planning) is mixed in the same file. Agents can't tell from file paths which tree has the authoritative version.

3. **Mewtwo wiki stub is empty** — `wiki/characters/mewtwo.md` has `status: stub` with no content. This is the character most in need of a reference doc (per the brief's canonical example) but is the most incomplete.

4. **Chapter notes don't reference wiki** — Notes for Chs 5–11 contain worldbuilding and character detail that is now codified in wiki docs, but don't link to them. An agent using chapter notes for context gets stale, potentially inconsistent information.

### Medium Priority (Organization Issues)

5. **One-file orphan subdirectories** — `wiki/lore/crime/`, `wiki/lore/economics/`, `wiki/lore/government/`, `wiki/lore/mechanics/`, `wiki/pokemon-teams/` each hold a single file with no siblings. These add directory overhead without organizational benefit.

6. **Hidden author-reference files in wiki/** — `wiki/lore/_aura-and-bonds.md` and `wiki/lore/_world-mechanics.md` are author-only planning docs that happen to live in wiki/. They should either be in `future/` (planning) or a dedicated author-reference section. Their presence in wiki/ creates type confusion (`type: lore` vs `type: wiki`).

7. **`wiki/lore/_plot-secrets.md` is empty** — Contains only a pointer to other files. Should be deleted.

8. **`future/team/` is an empty directory** — Residual structure from a planning session; should be removed.

9. **`wiki/index.md` is stale** — References `./chapters.md` (doesn't exist) and `./arcs/1-the-perfect-family.md` (path wrong — file is at `./arcs/1-the-perfect-family/outline.md`).

### Lower Priority (YAML Cleanup)

10. **`scope: story`** used throughout `future/` but not defined in AGENTS.md schema. The schema defines `scope: arc`, `scope: chapter`, `scope: global`. `scope: story` is used for docs that are "story-planning-wide" — a reasonable concept but undocumented.

11. **`status` values are not standardized** — 15+ distinct status values across the repo (draft, published, stub, seed, confirmed, planned, decided, idea-to-explore, active, completed, planning, index, author-reference, etc.). The schema defines only `draft` and `published`. The expanded vocabulary is useful but undocumented.

12. **`cinnabar-gym.md` has wrong title** — `title: Cinnabar Island` should be `title: Cinnabar Gym`.

13. **`category: pok-locations` vs `category: locations`** inconsistency in location files.

14. **`category: history`** in `gym-evolution.md` while all sibling files use `category: lore`.

15. **Most chapter notes missing required YAML fields** — `type`, `scope`, `chapter`, `spoilers`, `created` absent from the majority of chapter notes files.

---

## 8. Cross-Reference Coverage

Files that link to both wiki/ and future/ (the healthy pattern):
- `story/chapter17/_17notes.md` ✅
- `story/chapter13/_13notes.md` (partial — one wiki link) ✅
- Several `future/worldbuilding/` docs (link to wiki/ counterparts and other future/ docs) ✅
- Some wiki files (link to future/ arcs, e.g., `wiki/lore/aura-system.md`, `wiki/characters/mewtwo.md`)

Files about the same topic with NO links to each other:
- `wiki/characters/professor-oak.md` ↔ `future/arcs/arc-kitakami.md`
- `wiki/lore/organizations/team-rocket.md` ↔ `future/plot/team-rocket-surveillance.md`
- `wiki/characters/ditto.md` ↔ `future/plot/_mewtwo-thread.md`
- `wiki/lore/government/champion-system.md` ↔ `future/arcs/saga-overview.md`
- Chapter notes for Chs 5–11 ↔ wiki lore docs they relate to

The cross-referencing pattern improves significantly after Ch13 — earlier notes predate the wiki docs and were never updated.
