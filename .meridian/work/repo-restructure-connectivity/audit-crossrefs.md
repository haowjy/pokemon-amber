# Cross-Reference Audit: wiki/ and future/

**Date:** 2026-04-05
**Scope:** All files in `wiki/` (51 files) and `future/` (29 files) = 80 files total
**Purpose:** Identify connectivity gaps, broken links, orphan files, and one-way references to inform restructuring decisions.

---

## Summary Statistics

| Category | Count |
|----------|-------|
| Total files audited | 80 |
| wiki/ files | 51 |
| future/ files | 29 |
| Files with explicit cross-ref sections | ~24 |
| Files with NO cross-refs | ~38 |
| Broken links found | 33 |
| Confirmed orphan files (0 inbound refs) | 12 |
| Near-orphans (1 inbound ref only) | 8 |
| wiki files that reference future/ | 7 |
| future files that reference wiki/ | ~14 |

---

## Cross-Reference Patterns: What Exists

### Well-Connected Clusters

**1. Amber's core character cluster** — strongly connected
- `wiki/characters/amber-mc.md` ↔ `wiki/characters/mewtwo.md` ↔ `wiki/characters/ditto.md`
- All three cross-ref each other and `wiki/lore/aura-system.md`
- `wiki/lore/aura-system.md` ↔ `future/arcs/arc-4ever.md` and `future/arcs/arc-kitakami.md` (bidirectional)
- `wiki/pokemon-teams/team-amber-mc.md` has the broadest wiki→future linkage of any single file (references 5 future/ arc files)

**2. Trainer systems cluster** — internally well-connected
- `wiki/lore/trainer-systems/index.md` links to 8 subsystem files
- `badge-system.md`, `gym-system.md`, `conference-system.md`, `quest-system.md`, `trainer-paths.md`, `international-licensing.md`, `ranger-union.md`, `ace-trainers.md` all cross-reference each other
- `conference-system.md` → `future/worldbuilding/quarterly-conference-system.md`
- `gym-system.md` → `future/worldbuilding/gym-system-detailed.md`
- This cluster is the most systematically cross-referenced in the whole repo

**3. The Mewtwo thread** — well-connected spine
- `future/plot/_mewtwo-thread.md` ↔ `future/arcs/saga-overview.md` ↔ `future/arcs/arc1-kanto-year1.md`
- All reference `wiki/characters/mewtwo.md` and `future/plot/giovanni-fuji-jail.md`
- This is the clearest example of intentional cross-referencing

**4. Team Rocket** — cross-boundary linking
- `wiki/lore/organizations/team-rocket.md` explicitly references three future/ files: `current-direction.md`, `plot/team-rocket-surveillance.md`, `plot/giovanni-fuji-jail.md`
- One of only a handful of wiki files that actively bridge the wiki/future split

---

## The Core Problem: wiki/future Boundary Is Nearly Impermeable

**Only 7 of 51 wiki files (14%) reference any future/ file:**

1. `wiki/characters/mewtwo.md` → `future/arcs/arc-kitakami.md`
2. `wiki/lore/aura-system.md` → `future/arcs/arc-4ever.md`, `future/arcs/arc-kitakami.md`
3. `wiki/lore/organizations/team-rocket.md` → `future/current-direction.md`, `future/plot/team-rocket-surveillance.md`, `future/plot/giovanni-fuji-jail.md`
4. `wiki/lore/crime/poaching.md` → `future/plot/team-rocket-surveillance.md`
5. `wiki/lore/trainer-systems/conference-system.md` → `future/worldbuilding/quarterly-conference-system.md`
6. `wiki/lore/trainer-systems/gym-system.md` → `future/worldbuilding/gym-system-detailed.md`
7. `wiki/pokemon-teams/team-amber-mc.md` → `future/current-direction.md`, `future/arcs/arc-celadon.md`, `future/arcs/arc-kitakami.md`, `future/arcs/arc-pikachu-handoff.md`, `future/arcs/arc2-hoenn.md`

In the opposite direction, ~14 future/ files reference wiki/ content — but largely only as one-way citations ("see wiki/characters/mewtwo.md"), not with the wiki file pointing back.

**Result:** `current-direction.md` (declared source of truth) is referenced by only 7 files total, all in future/. Zero wiki/ files point to it.

---

## Broken Links (33 total)

### wiki/ broken links (20)

| File | Broken Reference | Issue |
|------|-----------------|-------|
| `wiki/index.md` | `./chapters.md` | File doesn't exist |
| `wiki/index.md` | `./arcs/1-the-perfect-family.md` | Wrong path; file is at `./arcs/1-the-perfect-family/outline.md` |
| `wiki/index.md` | `./pok-locations/celadon-city/celadon-city.md` | Folder is `celadon-area` not `celadon-city` |
| `wiki/lore/index.md` | `./training/index.md` | Should be `./trainer-systems/index.md` (folder renamed) |
| `wiki/lore/trainer-systems/index.md` | `./pokemon-league.md` | File not yet created |
| `wiki/lore/trainer-systems/index.md` | `../history/pokeball-invention.md` | File not yet created |
| `wiki/lore/trainer-systems/badge-system.md` | `trainer-licensing.md` | File doesn't exist |
| `wiki/lore/trainer-systems/quest-system.md` | `trainer-licensing.md` | File doesn't exist |
| `wiki/lore/organizations/ranger-union.md` | `../training/quest-system.md` | Old path; should be `../trainer-systems/quest-system.md` |
| `wiki/lore/organizations/ranger-union.md` | `police-force.md` | File doesn't exist |
| `wiki/lore/history/kanto-johto-unification-war.md` | `../../arcs/1-the-perfect-family.md` | Wrong path (see index.md entry above) |
| `wiki/lore/history/kanto-johto-unification-war.md` | `../tech/air-travel.md` | File doesn't exist |
| `wiki/lore/history/gym-evolution.md` | `pokeball-invention.md` | File doesn't exist |
| `wiki/lore/history/gym-evolution.md` | `../../pok-locations/celadon-city/celadon-gym.md` | Folder is `celadon-area` not `celadon-city` |
| `wiki/lore/history/gym-evolution.md` | `../../pok-locations/saffron-city/saffron-psychic-gym.md` | File/folder doesn't exist |
| `wiki/lore/history/gym-evolution.md` | `../../pok-locations/saffron-city/fighting-dojo.md` | File/folder doesn't exist |
| `wiki/lore/economics/pokeball-pricing.md` | `./economy.md` | Wrong relative path; should be `../economy.md` |
| `wiki/lore/economics/pokeball-pricing.md` | `trainer-licensing.md` | File doesn't exist |
| `wiki/pok-locations/celadon-area/celadon-pokemon-center.md` | `../../lore/training/quest-system.md` | Old path; should be `../../lore/trainer-systems/quest-system.md` |
| `wiki/pok-locations/cinnabar-island/cinnabar-island.md` | various | Minor inline path issues |

### future/ broken links (13)

| File | Broken Reference | Issue |
|------|-----------------|-------|
| `future/characters/kyle-kong.md` | `characters/sabrina.md` | File doesn't exist (sabrina not yet written) |
| `future/characters/kyle-kong.md` | `wiki/lore/aura-and-bonds.md` | Wrong path; file is `wiki/lore/_aura-and-bonds.md` (leading underscore) |
| `future/characters/kyle-kong.md` | `wiki/lore/training-culture.md` | File doesn't exist |
| `future/core/themes.md` | `arcs/arc2-discovery.md` | OLD arc name; replaced by `arcs/arc2-hoenn.md` |
| `future/core/themes.md` | `arcs/arc3-acceptance.md` | OLD arc name; no replacement file |
| `future/core/meta-notes.md` | `arcs/arc2-discovery.md` | OLD arc name |
| `future/core/meta-notes.md` | `arcs/arc3-acceptance.md` | OLD arc name |
| `future/plot/giovanni-fuji-jail.md` | `arcs/arc2-discovery.md` | OLD arc name |
| `future/plot/giovanni-fuji-jail.md` | `arcs/arc3-acceptance.md` | OLD arc name |
| `future/plot/oak-role-options.md` | `arcs/pokemon-4ever-option.md` | Never created; content absorbed into `arcs/arc-4ever.md` |
| `future/plot/oak-role-options.md` | `arcs/arc2-discovery.md` | OLD arc name |
| `future/plot/oak-role-options.md` | `arcs/arc3-acceptance.md` | OLD arc name |
| `future/plot/team-rocket-surveillance.md` | `arcs/arc2-discovery.md` | OLD arc name |
| `future/worldbuilding/economic-reality.md` | `wiki/lore/training-culture.md` | File doesn't exist |
| `future/worldbuilding/clan-system.md` | `worldbuilding/onscreen-discoveries.md` | File doesn't exist |

**Pattern:** The old arc names (`arc2-discovery.md`, `arc3-acceptance.md`) appear in 5 different files. These are stale references from before the 2026-03-30 pivot that renamed arcs. The renaming was not propagated.

---

## Orphan Files (No Inbound References)

Files with zero references from any other file in wiki/ or future/:

| File | Notes |
|------|-------|
| `wiki/pok-locations/viridian-area/viridian-hinterlands.md` | No file references it at all |
| `wiki/pok-locations/cinnabar-island/cinnabar-gym.md` | Only reachable via direct browsing |
| `wiki/pok-locations/cinnabar-island/flame-forest.md` | Mentioned inline in `cinnabar-island.md` but no formal link |
| `wiki/lore/_aura-and-bonds.md` | Listed in `lore/index.md` as "hidden reference" but nothing else links to it; the public `aura-system.md` doesn't reference it |
| `wiki/lore/tech/transportation.md` | Only in tech/index.md |
| `wiki/lore/tech/communications.md` | Only in tech/index.md |
| `wiki/lore/tech/identity-security.md` | Only in tech/index.md and `international-licensing.md` |
| `future/TONE.md` | Not referenced from any other file |
| `future/README.md` | Folder guide, not referenced |
| `future/_archive-completed.md` | Historical record, nothing points to it |
| `future/episodes/kyle-meeting.md` | Stub, not referenced |
| `future/episodes/pewter-gym-brock.md` | Stub, not referenced |
| `future/episodes/route1-solo.md` | Stub, not referenced |

**Semi-orphans** (only 1 inbound reference, and it's a broken one):
- `wiki/arcs/1-the-perfect-family/outline.md` — wiki/index.md has a broken link to it; no valid link
- `wiki/lore/trainer-systems/ace-trainers.md` — only referenced from trainer-systems/index.md

---

## One-Way Links: A References B, B Does Not Reference A

These are the most actionable gaps — fixing them requires adding a single back-reference to the B file.

### High-Priority One-Way Links

| A (has reference) | B (missing back-ref) | Why It Matters |
|-------------------|----------------------|---------------|
| `wiki/characters/dr-fuji.md` | `wiki/characters/ditto.md` | Dr. Fuji created Ditto; Ditto's file doesn't reference its creator |
| `wiki/pok-locations/celadon-area/celadon-gym.md` | `wiki/characters/erika.md` | The gym file doesn't link to Erika's character page |
| `wiki/characters/erika.md` | `wiki/pok-locations/celadon-area/celadon-gym.md` | Erika's file doesn't link to her own gym's page |
| `wiki/characters/erika.md` | `future/arcs/arc-celadon.md` | No link from Erika's file to the arc she features in |
| `wiki/characters/kaede.md` | `wiki/characters/erika.md` | Kaede is Erika's close associate; Erika doesn't reference Kaede |
| `wiki/pok-locations/pallet-town-area/pallet-town.md` | `wiki/characters/delia-ketchum.md` | Pallet Town article doesn't link to its most prominent resident |
| `wiki/pok-locations/pallet-town-area/pallet-town.md` | `wiki/characters/professor-oak.md` | Pallet Town doesn't link to Oak |
| `wiki/lore/history/kanto-johto-unification-war.md` | `wiki/lore/organizations/team-rocket.md` | team-rocket.md links to the war, war article doesn't link back |
| `future/arcs/arc1-kanto-year1.md` | `future/arcs/arc-celadon.md` | Arc 1 sets up Celadon but doesn't reference the arc file |
| `future/worldbuilding/economic-reality.md` | `future/characters/kyle-kong.md` | Economic reality discusses Kyle but kyle-kong.md doesn't reference it |
| `future/worldbuilding/clan-system.md` | `wiki/lore/history/kanto-johto-unification-war.md` | Clan system references the war article; war article doesn't reference clan system |
| `future/worldbuilding/clan-system.md` | `wiki/lore/economy.md` | Clan system references economy.md; economy.md doesn't reference clan system |
| `wiki/arcs/1-the-perfect-family/events/` (all 4 event files) | `wiki/characters/amber-mc.md`, `wiki/characters/dr-fuji.md`, etc. | Arc events involve main characters but none of the event files link to character pages, and character pages don't link to event files |

### The `current-direction.md` Gap

`future/current-direction.md` is declared the **source of truth** for the whole project. It is referenced by:
- `future/_open-questions.md`
- `future/arcs/arc1-kanto-year1.md`
- `future/arcs/arc-pikachu-handoff.md`
- `future/arcs/saga-overview.md`
- `wiki/pokemon-teams/team-amber-mc.md`
- `future/plot/forged-documents.md`
- `future/plot/oak-role-options.md`
- `future/plot/team-rocket-surveillance.md`
- `future/worldbuilding/economic-reality.md` (via `current-direction.md`)
- `future/worldbuilding/quarterly-conference-system.md`

**Not referenced by:** Any of the 51 wiki/ files except `team-amber-mc.md`. The declared source of truth has no inbound links from the reference/canon section of the repo.

---

## Topic Clusters Spanning wiki/future With No Cross-Links

These are thematically related groups that exist on both sides of the wiki/future divide without connecting to each other.

### 1. The Celadon Cluster

**What exists:**
- `wiki/characters/erika.md` (449 lines, detailed character doc)
- `wiki/characters/kaede.md` (detailed, Erika's associate)
- `wiki/pok-locations/celadon-area/celadon-city.md`
- `wiki/pok-locations/celadon-area/celadon-gym.md`
- `wiki/pok-locations/celadon-area/celadon-pokemon-center.md`
- `future/arcs/arc-celadon.md` (the arc plan for Celadon)

**Connectivity:** Almost none. `celadon-gym.md` links to `celadon-city.md` and `celadon-pokemon-center.md` but NOT to `erika.md`. `erika.md` links to nothing. `kaede.md` links to nothing. `arc-celadon.md` references `wiki/pokemon-teams/team-amber-mc.md` but not `erika.md`, `kaede.md`, or the location files. The character files for the Celadon arc's central figures are disconnected from both the location files and the arc plan.

### 2. The Pallet Town / Origin Cluster

**What exists:**
- `wiki/pok-locations/pallet-town-area/pallet-town.md`
- `wiki/characters/delia-ketchum.md`
- `wiki/characters/professor-oak.md`
- `wiki/arcs/1-the-perfect-family/outline.md` + 4 event files
- `future/arcs/arc1-kanto-year1.md` (Ch 18 departure)

**Connectivity:** `pallet-town.md` cites story chapters but doesn't link to `delia-ketchum.md` or `professor-oak.md`. The arc event files cite chapters only and never link to character files. The four characters most associated with Pallet (Amber, Fuji, Oak, Delia) have character files but the location article mentions none of them.

### 3. The Giovanni/Viridian Cluster

**What exists:**
- `wiki/lore/organizations/team-rocket.md`
- `future/plot/giovanni-fuji-jail.md`
- `future/worldbuilding/gym-system-detailed.md` (has detailed Viridian Gym / Giovanni section)
- `future/arcs/arc1-kanto-year1.md` (has Viridian Gym — first challenge section)
- `future/worldbuilding/clan-system.md` (has Viridian House / Giovanni family section)

**Connectivity:** `team-rocket.md` references `giovanni-fuji-jail.md` (good). But `giovanni-fuji-jail.md` does NOT reference `team-rocket.md`. The clan-system.md has a detailed section on Viridian House (Giovanni's family lineage) that connects to Team Rocket history, but `team-rocket.md` doesn't know `clan-system.md` exists. The gym-system-detailed.md's Giovanni section doesn't link to `giovanni-fuji-jail.md`.

### 4. The Worldbuilding Promotion Gap

Three future/ worldbuilding files have explicit "wiki promotion note" headers indicating their canonical content was migrated to wiki/ files:
- `future/worldbuilding/economic-reality.md` → promoted to `wiki/lore/trainer-systems/trainer-paths.md`
- `future/worldbuilding/gym-system-detailed.md` → promoted to `wiki/lore/trainer-systems/gym-system.md`
- `future/worldbuilding/quarterly-conference-system.md` → promoted to `wiki/lore/trainer-systems/conference-system.md`

**Problem:** The wiki files don't back-reference the future/ originals (except the two cross-refs that were already there: conference-system.md → quarterly-conference-system.md, gym-system.md → gym-system-detailed.md). The future/ files still contain story-specific planning content (character-specific economic positioning, Saffron gym politics, arc arrival timing) that the wiki files don't contain. But there's no clear mechanism to tell a reader "there's more detail about this topic in future/."

### 5. Character Files Across the wiki/future Split

The most structurally jarring gap: the same type of content (character documentation) exists in both directories, split by publication status.

| wiki/ character | future/ content about them | Cross-link? |
|-----------------|---------------------------|------------|
| `wiki/characters/amber-mc.md` | `future/arcs/*` (her whole journey) | amber-mc.md has no links to future/arcs/ |
| `wiki/characters/professor-oak.md` | `future/arcs/arc-4ever.md`, `arc-kitakami.md`, `arc-pikachu-handoff.md` | Only inline mentions; no formal cross-refs |
| `wiki/characters/delia-ketchum.md` | `future/_open-questions.md` (#6 Delia resolution) | No cross-link |
| `wiki/characters/mary.md` | `future/_open-questions.md` (#1 Mary companion?) | No cross-link |
| `wiki/characters/mewtwo.md` | `future/plot/_mewtwo-thread.md` | mewtwo.md IS in _mewtwo-thread.md's cross-refs ✓; mewtwo.md has a cross-refs section that includes arc-kitakami.md ✓ — **this pair is well connected** |
| (no wiki file) | `future/characters/kyle-kong.md` | wiki/ has no Kyle page at all |
| (no wiki file) | `future/characters/sabrina.md` (referenced but doesn't exist) | Neither tree has a Sabrina file |

---

## Files With No Cross-References At All

These files contain content but include zero links to other files in the repo:

| File | Size/Status |
|------|------------|
| `wiki/characters/delia-ketchum.md` | Full character doc |
| `wiki/characters/erika.md` | 449 lines, extensive |
| `wiki/characters/kaede.md` | Full character doc |
| `wiki/characters/mary.md` | Full character doc |
| `wiki/lore/_world-mechanics.md` | Comprehensive mechanics reference |
| `wiki/lore/_aura-and-bonds.md` | Detailed author-only mechanics |
| `wiki/lore/trainer-systems.md` | 12,000+ chars, comprehensive |
| `wiki/arcs/1-the-perfect-family/outline.md` | Arc outline |
| `wiki/arcs/1-the-perfect-family/events/1-mewtwo-escape.md` | Event file |
| `wiki/arcs/1-the-perfect-family/events/2-project-chimera.md` | Event file |
| `wiki/arcs/1-the-perfect-family/events/3-oak-letter.md` | Event file |
| `wiki/arcs/1-the-perfect-family/events/4-pallet-attack.md` | Event file |
| `wiki/pok-locations/pallet-town-area/pallet-town.md` | Location doc |
| `wiki/pok-locations/viridian-area/viridian-hinterlands.md` | Location doc |
| `wiki/pok-locations/cinnabar-island/cinnabar-gym.md` | Location doc |
| `wiki/pok-locations/cinnabar-island/flame-forest.md` | Location doc |
| `future/TONE.md` | Guide doc |
| `future/core/meta-notes.md` | Has broken refs, no valid refs |
| `future/episodes/kyle-meeting.md` | Stub |
| `future/episodes/pewter-gym-brock.md` | Stub |
| `future/episodes/route1-solo.md` | Stub |
| `future/plot/saffron-gym-rivalry.md` | Stub |

---

## Structural Observations

### 1. Two hidden mechanics files contain canon content nobody references

`wiki/lore/_aura-and-bonds.md` and `wiki/lore/_world-mechanics.md` are detailed author-only references for world mechanics (elemental cultivation, type opposition, progression systems, fainting rules, Pokeball technology). The public `aura-system.md` doesn't reference `_aura-and-bonds.md` despite being a less detailed version of the same topic. When writers look at `aura-system.md`, they don't know the deeper author doc exists.

### 2. The trainer-systems.md duplication problem

`wiki/lore/trainer-systems.md` is a 12,000+ character comprehensive document covering trainer culture. `wiki/lore/trainer-systems/index.md` is a hub linking to 8 subsystem files covering the same material in modular form. These two files coexist without either referencing the other, creating redundancy and confusion about which is authoritative.

### 3. The arc naming stale references problem

Five future/ files still reference `arc2-discovery.md` and `arc3-acceptance.md` — old arc names from before the 2026-03-30 pivot. These were renamed to `arc2-hoenn.md` and the others, but the stale references were never updated. A reader following these links finds nothing.

### 4. Character pages are islands

Character files in `wiki/characters/` (Erika, Kaede, Delia, Mary) contain extensive canon information but have no outbound links to related characters, locations, or arcs. They are encyclopedia entries that end with no "see also." The exception is the Amber/Mewtwo/Ditto cluster which explicitly cross-references each other.

### 5. Event files are citation-only

The four event files in `wiki/arcs/1-the-perfect-family/events/` cite story chapters only. A character might be central to an event but their character page has no link to that event, and the event file has no link to their character page. The arc event system and the character system are parallel structures that don't know about each other.

---

## Priority Gaps to Fix

### Immediate (broken links causing navigation failure)

1. Update 5 files still referencing `arc2-discovery.md` / `arc3-acceptance.md` to current arc names
2. Fix `wiki/lore/index.md` → `./training/index.md` (should be `./trainer-systems/index.md`)
3. Fix `wiki/lore/organizations/ranger-union.md` → `../training/` paths (old folder name)
4. Fix `wiki/pok-locations/celadon-area/celadon-pokemon-center.md` → old training/ path
5. Fix `wiki/index.md` broken folder names (`celadon-city` → `celadon-area`)

### High Value (common topics with no cross-links)

6. Add cross-refs between `wiki/characters/erika.md` ↔ `wiki/pok-locations/celadon-area/celadon-gym.md` ↔ `future/arcs/arc-celadon.md`
7. Add `wiki/pok-locations/pallet-town-area/pallet-town.md` → `wiki/characters/delia-ketchum.md`, `wiki/characters/professor-oak.md`
8. Add `wiki/lore/aura-system.md` → `wiki/lore/_aura-and-bonds.md` (so the public doc knows the detailed one exists)
9. Add `future/worldbuilding/clan-system.md` ↔ `wiki/lore/organizations/team-rocket.md` (Giovanni family context)
10. Add `wiki/characters/amber-mc.md` → `future/arcs/saga-overview.md` or `future/current-direction.md` (the canonical source for her journey)

### Structural (requires decision)

11. **The wiki/future split**: Determine whether character files should be unified (one tree, tag by status) or kept split with explicit cross-tree linking
12. **trainer-systems.md vs trainer-systems/index.md**: Decide which is authoritative; add a reference from one to the other
13. **The promoted worldbuilding files**: Add consistent "see future/worldbuilding/X for arc-planning detail" links from the wiki files that absorbed their canonical content
14. **Create missing files that many things reference**: `trainer-licensing.md`, `police-force.md`, `characters/sabrina.md` — or update the references to remove the broken links

---

## File Inventory by Directory

### wiki/ — 51 files

```
wiki/
├── index.md                           [BROKEN LINKS: 3]
├── timeline.md                        [no cross-refs]
├── characters/
│   ├── amber-mc.md                    [has cross-refs ✓]
│   ├── mewtwo.md                      [has cross-refs ✓]
│   ├── dr-fuji.md                     [partial cross-refs]
│   ├── ditto.md                       [has cross-refs ✓]
│   ├── delia-ketchum.md               [NO cross-refs]
│   ├── erika.md                       [NO cross-refs — major gap]
│   ├── kaede.md                       [NO cross-refs]
│   ├── mary.md                        [NO cross-refs]
│   └── professor-oak.md               [partial cross-refs]
├── arcs/
│   └── 1-the-perfect-family/
│       ├── outline.md                 [NO cross-refs, near-orphan]
│       └── events/
│           ├── 1-mewtwo-escape.md     [NO cross-refs]
│           ├── 2-project-chimera.md   [NO cross-refs]
│           ├── 3-oak-letter.md        [NO cross-refs]
│           └── 4-pallet-attack.md     [NO cross-refs]
├── lore/
│   ├── index.md                       [BROKEN LINK: training/ path]
│   ├── aura-system.md                 [has cross-refs ✓]
│   ├── economy.md                     [has cross-refs]
│   ├── trainer-systems.md             [NO cross-refs, REDUNDANT with trainer-systems/]
│   ├── _plot-secrets.md               [index only, points to wiki/characters/]
│   ├── _aura-and-bonds.md             [NO cross-refs, near-orphan]
│   ├── _world-mechanics.md            [NO cross-refs]
│   ├── crime/
│   │   └── poaching.md                [has cross-refs ✓, including future/]
│   ├── economics/
│   │   └── pokeball-pricing.md        [BROKEN LINKS: 2]
│   ├── history/
│   │   ├── gym-evolution.md           [BROKEN LINKS: 4]
│   │   └── kanto-johto-unification-war.md [BROKEN LINKS: 2]
│   ├── mechanics/
│   │   └── pokemon-fainting.md        [has cross-refs ✓]
│   ├── organizations/
│   │   ├── ace-trainers.md            [minimal cross-refs]
│   │   ├── ranger-union.md            [BROKEN LINKS: 2, old paths]
│   │   └── team-rocket.md             [has cross-refs ✓, including future/]
│   ├── tech/
│   │   ├── index.md                   [has cross-refs]
│   │   ├── communications.md          [minimal]
│   │   ├── identity-security.md       [minimal]
│   │   └── transportation.md          [minimal]
│   └── trainer-systems/
│       ├── index.md                   [BROKEN LINKS: 2, hub file]
│       ├── ace-trainers.md            [minimal]
│       ├── badge-system.md            [has cross-refs, 1 BROKEN]
│       ├── conference-system.md       [has cross-refs ✓, → future/]
│       ├── gym-system.md              [has cross-refs ✓, → future/]
│       ├── international-licensing.md [has cross-refs]
│       ├── quest-system.md            [has cross-refs, 1 BROKEN]
│       ├── ranger-union.md            → (lives in organizations/ actually)
│       └── trainer-paths.md           [has cross-refs]
├── pok-locations/
│   ├── celadon-area/
│   │   ├── celadon-city.md            [has cross-refs]
│   │   ├── celadon-gym.md             [has cross-refs, missing ↔ erika.md]
│   │   └── celadon-pokemon-center.md  [BROKEN LINK: old path]
│   ├── cinnabar-island/
│   │   ├── cinnabar-island.md         [partial]
│   │   ├── cinnabar-gym.md            [NO cross-refs, orphan]
│   │   └── flame-forest.md            [NO cross-refs, near-orphan]
│   ├── pallet-town-area/
│   │   └── pallet-town.md             [NO cross-refs — major gap]
│   └── viridian-area/
│       └── viridian-hinterlands.md    [NO cross-refs, orphan]
└── pokemon-teams/
    └── team-amber-mc.md               [has cross-refs ✓✓, best wiki→future linker]
```

### future/ — 29 files

```
future/
├── README.md                          [folder guide, not cross-ref'd]
├── TONE.md                            [orphan]
├── _archive-completed.md              [orphan]
├── _open-questions.md                 [has cross-refs]
├── current-direction.md               [SOURCE OF TRUTH — 0 inbound from wiki/]
├── arcs/
│   ├── arc-4ever.md                   [has cross-refs ✓]
│   ├── arc-celadon.md                 [partial cross-refs]
│   ├── arc-kitakami.md                [has cross-refs ✓]
│   ├── arc-pikachu-handoff.md         [has cross-refs ✓]
│   ├── arc1-kanto-year1.md            [has cross-refs ✓]
│   ├── arc2-hoenn.md                  [stub, 3 lines]
│   ├── arc3-beyond.md                 [stub, 3 lines]
│   └── saga-overview.md               [has cross-refs ✓]
├── characters/
│   └── kyle-kong.md                   [BROKEN LINKS: 3]
├── core/
│   ├── meta-notes.md                  [BROKEN LINKS: 2 (old arc names)]
│   └── themes.md                      [BROKEN LINKS: 2 (old arc names)]
├── episodes/
│   ├── kyle-meeting.md                [stub, orphan]
│   ├── pewter-gym-brock.md            [stub, orphan]
│   └── route1-solo.md                 [stub, orphan]
├── plot/
│   ├── _mewtwo-thread.md              [has cross-refs ✓]
│   ├── forged-documents.md            [has cross-refs]
│   ├── giovanni-fuji-jail.md          [BROKEN LINKS: 2 (old arc names)]
│   ├── oak-role-options.md            [BROKEN LINKS: 3]
│   ├── saffron-gym-rivalry.md         [stub, near-orphan]
│   └── team-rocket-surveillance.md    [BROKEN LINK: 1 (old arc name)]
└── worldbuilding/
    ├── clan-system.md                 [has Related Files section ✓, some broken]
    ├── economic-reality.md            [has Related Files ✓, 1 broken]
    ├── gym-system-detailed.md         [has Related Files ✓]
    └── quarterly-conference-system.md [has Related Files ✓]
```

---

*Audit complete. 80 files read. 33 broken links, 12 confirmed orphans, 7 wiki→future links (14% of wiki files).*
