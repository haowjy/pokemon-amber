# Connectivity Scheme Evaluation

**Date:** 2026-04-05
**Work item:** repo-restructure-connectivity
**Based on:** audit-crossrefs.md + audit-structure.md

---

## Context

The audits found 80 files (51 wiki/, 29 future/) with:
- 33 broken links
- 12 orphan files
- 14% of wiki files link to future/
- Extensive topic clusters spanning both trees with few or no cross-links
- Some files already use ad-hoc "Related Files" / "Cross-Refs" sections that work well

The goal is to pick a connectivity scheme that makes it easy for both a human author *and* an AI agent to discover all files relevant to a given topic.

---

## The Existing Pattern (What Works)

Before evaluating alternatives, note what's already working. Files like `wiki/lore/organizations/team-rocket.md`, `future/plot/_mewtwo-thread.md`, and `wiki/characters/amber-mc.md` use bottom-of-file **"Related Files"** or **"Cross-Refs"** sections with backtick-formatted paths:

```markdown
## Related Files

- **Story direction:** `future/current-direction.md`
- **TR surveillance plot:** `future/plot/team-rocket-surveillance.md`
- **Kanto-Johto War context:** `wiki/lore/history/kanto-johto-unification-war.md`
```

The `trainer-systems/` cluster is the best-connected group in the repo, and it achieves that purely through consistent use of inline links and a well-maintained index file. The Amber/Mewtwo/Ditto character cluster is the second-best connected group — same mechanism.

The problem isn't that the mechanism doesn't exist. It's that it's unevenly applied: ~38 of 80 files have zero cross-references.

---

## Scheme Evaluations

### Scheme 1: YAML `references` Field

Add a structured `references` or `related` list to front matter:

```yaml
---
type: wiki
title: Erika
related:
  - wiki/pok-locations/celadon-area/celadon-gym.md
  - future/arcs/arc-celadon.md
  - wiki/characters/kaede.md
---
```

**Schema design for this repo:**

The existing YAML schemas in CLAUDE.md would need one new optional field: `related: []` — a list of relative paths to related files. This is the minimal viable addition.

**Maintenance burden at 80 files (growing to ~150):**

High. Every time a file is renamed, moved, or created, all other files that reference it in `related:` need updating. This repo already has 33 broken links despite not systematically using path-based front matter. The audit found 5 files still referencing `arc2-discovery.md` / `arc3-acceptance.md` after a 2026-03-30 arc rename — and those were *inline* links that presumably got some attention. YAML `related` fields buried in front matter would be even more invisible when paths go stale.

There's also a duplication problem: a file that does this correctly will list the same relationships in *both* the YAML `related` field *and* its "Related Files" prose section (for human readers). That doubles the maintenance burden without doubling the value.

**Agent-friendliness:**

Moderately helpful. An agent can `grep -r "celadon-gym" .` to find files that reference a given path, but it can also do that with inline mentions. The main advantage is that `related:` creates a *guaranteed location* to look — but grep on a 80–150 file repo is fast regardless of whether references live in front matter or prose.

**Verdict:** The maintenance cost-to-benefit ratio is poor at this repo's scale. The path-staleness problem is real and already demonstrated. Don't use as the *primary* mechanism.

---

### Scheme 2: Topic Index Files

Create one index file per major entity/topic that aggregates all references to that topic across both trees. Example: `index/mewtwo.md` lists every file that discusses Mewtwo.

**How many would this repo need?**

Based on the topic clusters identified in the audit, this repo would need roughly:
- 9 character indices (Amber, Dr. Fuji, Mewtwo, Erika, Oak, Delia, Mary, Kaede, Kyle)
- 5 location clusters (Pallet, Viridian, Cinnabar, Celadon, Saffron)
- 8 plot thread indices (TR surveillance, Giovanni/Fuji jail, Mewtwo thread, forged docs, etc.)
- 6 lore system indices (trainer systems, aura, economics, Team Rocket, clans, war)
- 4 arc indices (Arc 0, Arc 1, Celadon, 4Ever)

That's ~32 index files on top of the existing 80. A separate index layer.

**Maintenance vs. value tradeoff:**

Index files front-load the maintenance: someone has to create them and keep them current. The repo already has `wiki/index.md` (stale, broken links), `wiki/lore/index.md` (one broken link), and `wiki/lore/trainer-systems/index.md` (2 broken links, but still the best-maintained index in the repo). The pattern shows that index files *work well* when they're directly adjacent to the content they organize — `trainer-systems/index.md` is good because the maintainer touches it whenever they touch the subsystem files. A separate `index/mewtwo.md` file would be geographically disconnected from the Mewtwo character file and much more likely to go stale.

The value proposition also overlaps heavily with Scheme 3 (cross-reference sections). A "Related Files" section at the bottom of `mewtwo.md` accomplishes most of what a `index/mewtwo.md` would accomplish, with less overhead.

**One exception:** The wiki-to-future boundary problem. A file like `current-direction.md` (the declared source of truth, zero inbound wiki links) would genuinely benefit from an index-style aggregator if that aggregator were in a prominent, author-facing location. But this is better solved by making `wiki/index.md` functional and pointing it at `current-direction.md`, not by creating 32 new index files.

**Verdict:** Too much maintenance overhead for this repo. The trainer-systems/index.md example shows that *local* index files work — lean into that rather than building a separate index layer. Don't use as primary mechanism.

---

### Scheme 3: Inline Cross-Reference Sections (Standardized)

Standardize and gap-fill the "Related Files" / "Cross-Refs" sections that some files already use. This is what the repo *already partially does*.

**Standardization:**

Pick one heading and format across all files:

```markdown
## Related

- `wiki/characters/erika.md` — character profile for the gym leader
- `future/arcs/arc-celadon.md` — arc planning for Erika's storyline
- `wiki/pok-locations/celadon-area/celadon-city.md` — location context
```

The audit found at least three existing formats: `## Related Files`, `## Cross-Refs`, and bare inline links in the prose. Standardizing to one heading (e.g., `## Related`) would make these sections greppable: `grep -n "^## Related"` across the repo.

**Gap-filling:**

The audit identified the highest-value gaps. The 38 files with zero cross-refs include several major ones (Erika, Delia, Mary, Pallet Town, all arc event files). Adding "Related" sections to these is straightforward incremental work.

**Can it be maintained?**

Yes, with a key advantage over YAML references: these sections are *read by authors* during normal editing. When you're working on `erika.md` and see the "Related" section pointing to `arc-celadon.md`, you naturally visit that arc doc. The relationship is visible in context, not buried in front matter. This also means that when a file gets renamed, the author who renames it is likely to also fix the references (compared to YAML where front matter is frequently overlooked).

The remaining staleness risk is real but manageable: broken links here are visible to any reader, unlike YAML fields.

**Agent-discoverability:**

Excellent for this repo's scale. An agent can `grep -A 20 "^## Related"` to extract the related section from any file. It can also do full-text search for a filename and find it in any Related section. Because related sections use full relative paths in backticks, they're machine-parseable.

The trainer-systems/ cluster (the best-connected group in the repo) got there entirely through this mechanism. The Mewtwo thread cluster (second-best connected) uses `## Cross-Refs` for the same purpose. The evidence is already in the repo that this works.

**GitHub rendering:** Full compatibility. Renders as a bullet list.

**Migration cost:** Low. No schema changes needed. Just: pick a standard heading, then add sections to ~38 files. The audit's "Priority Gaps" section already provides a prioritized list.

**Verdict:** This is the primary mechanism. The repo already proved it works. The problem is coverage, not mechanism design.

---

### Scheme 4: YAML Tags

Add a `tags: []` field to front matter using a controlled vocabulary:

```yaml
tags: [erika, celadon, gym-system, arc-celadon]
```

**What tag vocabulary would this repo need?**

Based on the topic clusters in the audit, a minimal useful vocabulary would be roughly:
- Characters: `amber`, `dr-fuji`, `mewtwo`, `erika`, `oak`, `delia`, `mary`, `kaede`, `kyle`, `giovanni`
- Locations: `pallet-town`, `viridian`, `cinnabar`, `celadon`, `saffron`
- Systems: `trainer-systems`, `aura`, `economics`, `team-rocket`, `clans`
- Arcs: `arc0`, `arc1-kanto`, `arc-celadon`, `arc-4ever`, `arc2-hoenn`
- Types: `character`, `location`, `lore`, `arc-plan`, `plot-thread`

~40 tags to meaningfully cover the repo. With 80+ files, average 3–4 tags per file.

**How much does it actually help discoverability?**

Moderately, with a critical limitation: **tags have no GitHub UI**. There are no tag index pages, no clickable tag clouds. A human browsing GitHub cannot use tags for navigation — they're invisible unless they know to run `grep -r "tags:.*erika" .`. Tags are purely machine-queryable.

For *agent* discoverability, tags are genuinely useful: `grep -r "tags:.*celadon" wiki/ future/` returns all files related to Celadon in one command, regardless of whether they have inline links to each other. This is a different value proposition from Scheme 3 — it finds related files *without requiring any explicit cross-references between them*.

The maintenance burden is lower than path-based schemes because tags don't break when files are renamed. The vocabulary can expand without breaking existing tags.

**Verdict:** Useful as a *lightweight complement* to Scheme 3, not as a standalone. Tags help agents do cluster discovery ("find everything about Celadon") while cross-reference sections help with navigation ("from this file, where do I go next?"). They solve different problems. Use tags for the ~10 most cross-cutting topics only; adding 40-tag vocabularies invites tag sprawl.

---

### Scheme 5: Directory Restructuring (Merge wiki/future)

Merge `wiki/` and `future/` into a unified reference tree, using YAML `status` (or a new `stage` field) to encode the wiki/future distinction instead of directory location.

**Proposed new tree:**

```
ref/
├── characters/
│   ├── amber-mc.md          [status: published]
│   ├── erika.md             [status: published]
│   ├── kyle-kong.md         [status: planned]
├── arcs/
│   ├── arc0-cinnabar/       [status: published]
│   ├── arc1-kanto-year1.md  [status: planned]
│   ├── arc-celadon.md       [status: planned]
├── lore/
│   ├── trainer-systems/     [status: published]
│   ├── clan-system.md       [status: idea-to-explore]
├── planning/
│   ├── current-direction.md
│   ├── _open-questions.md
│   ├── saga-overview.md
```

**Arguments for:**

The audit confirms the wiki/future split is the primary driver of disconnection. Only 7 of 51 wiki files (14%) reference any future/ file. The split is semantic — publication status — but it's enforced by directory location, which forces authors to cross a tree boundary to link related content. Erika's character file (`wiki/characters/erika.md`) and the arc that features her (`future/arcs/arc-celadon.md`) would naturally be adjacent in `ref/characters/` and `ref/arcs/` without the boundary.

The audit's structural analysis confirms the distinction often breaks down: `wiki/lore/_aura-and-bonds.md` and `wiki/lore/_world-mechanics.md` are functionally planning docs that live in wiki/ because they use `hidden: true`. The `future/worldbuilding/` files have canonical content that was already promoted into wiki/. The line is blurry in practice.

**Arguments against:**

1. **Migration cost is high.** Renaming 80 files and updating every relative path in every file, plus updating `.agents/skills/`, `CLAUDE.md`, chapter notes cross-refs, and `story/README.md`. The 33 currently broken links suggest path maintenance is already difficult — a mass rename would create 33+ new broken links immediately.

2. **The split encodes useful semantics.** "Is this published canon or planning?" is a genuinely important distinction for this project. An agent writing prose needs to know whether a lore doc is established fact or speculation. The directory location currently answers this at a glance. Moving to YAML status requires reading front matter to get the same information, and the audit shows YAML compliance is inconsistent (15+ non-standard status values, many files missing required fields).

3. **The problem is solvable at lower cost.** The cross-reference gaps that make topics hard to find can be fixed with inline "Related" sections (Scheme 3) without touching file paths. A reader finding `wiki/characters/erika.md` with a proper "Related" section pointing to `future/arcs/arc-celadon.md` navigates to the planning content in one click — the tree boundary becomes irrelevant.

4. **Story/ would still be separate.** Even after merging wiki/future, `story/` chapter notes would remain a third tree. The fundamental multi-tree problem doesn't fully go away.

**What would actually improve:** The `current-direction.md` gap (zero wiki inbound links) is the clearest argument for merging. But that's fixable with a single link addition to `wiki/index.md`.

**Verdict:** Don't do this. High cost, meaningful loss of semantic clarity, and the core discoverability problem is solvable without it. Revisit only if cross-reference section maintenance proves unsustainable at 150+ files.

---

### Scheme 6: Hybrid Approaches

**Recommended hybrid: Scheme 3 (primary) + Scheme 4 (selective)**

**Scheme 3 as the backbone:**
- Standardize all cross-reference sections to `## Related` heading
- Gap-fill the ~38 files that have zero cross-refs, starting with the audit's high-priority list
- The inline sections are the human-readable navigation layer and the agent-parseable link graph

**Scheme 4 as a lightweight complement:**
- Add `tags:` to front matter for the ~10 most cross-cutting topics only
- Suggested minimal tag vocabulary: `[amber, mewtwo, erika, team-rocket, celadon, pallet-town, trainer-systems, clan-system, arc1-kanto, aura]`
- This enables "find all Celadon files" queries without requiring every Celadon file to explicitly link every other Celadon file
- Do NOT add tags to stubs or minimal files — only to substantive docs

**What this doesn't include:**
- YAML `related` field (path maintenance too costly for this repo's size and rename frequency)
- Topic index files (overhead exceeds benefit; local index files where they already exist are fine)
- Directory restructuring (high cost, low marginal benefit if Scheme 3 is properly implemented)

---

## Comparison Table

| Criterion | YAML references | Topic indexes | Inline cross-refs | YAML tags | Dir restructure | Hybrid (3+4) |
|---|---|---|---|---|---|---|
| **Maintenance burden** | High (path staleness) | High (separate index layer) | Medium (visible in context) | Low (no paths) | Very high (migration) | Medium-low |
| **Agent discoverability** | Good (structured) | Good (aggregated) | Good (grep-able sections) | Good (cluster search) | Good (colocation) | Excellent |
| **Author discoverability** | Poor (hidden in FM) | Medium (separate file) | Excellent (inline) | Poor (no GitHub UI) | Good (colocation) | Excellent |
| **Migration cost** | Medium | Medium | Low | Low | Very high | Low |
| **Break risk** | High (path changes) | Medium | Low | Very low | Very high initially | Low |
| **GitHub compatibility** | Yes | Yes | Yes | Yes (invisible) | Yes | Yes |
| **Already works in this repo** | No | Partially (local indexes) | Yes (7+ well-connected files) | No | N/A | Yes |
| **Scales to 150 files** | Poor | Poor | Good | Good | N/A | Good |

---

## Recommendation

**Use the hybrid of Scheme 3 + selective Scheme 4.**

### Phase 1: Fix broken links (immediate)

These cause navigation failure and should be done before anything else:

1. Update 5 files still referencing `arc2-discovery.md` / `arc3-acceptance.md` to current arc names
2. Fix `wiki/lore/index.md` → `./training/` path (should be `./trainer-systems/`)
3. Fix `wiki/lore/organizations/ranger-union.md` → old `training/` paths
4. Fix `wiki/pok-locations/celadon-area/celadon-pokemon-center.md` → old `training/` path
5. Fix `wiki/index.md` broken folder names (`celadon-city` → `celadon-area`)

### Phase 2: Standardize cross-reference sections

- Choose `## Related` as the standard heading (shorter than "Related Files", same meaning)
- Add `## Related` sections to the 10 highest-value gap files identified in the audit:
  - `wiki/characters/erika.md` → celadon-gym.md, kaede.md, arc-celadon.md
  - `wiki/pok-locations/pallet-town-area/pallet-town.md` → delia-ketchum.md, professor-oak.md
  - `wiki/characters/amber-mc.md` → add future/arcs/saga-overview.md, future/current-direction.md
  - `wiki/lore/aura-system.md` → add wiki/lore/_aura-and-bonds.md (so public doc knows hidden one exists)
  - `future/worldbuilding/clan-system.md` ↔ `wiki/lore/organizations/team-rocket.md`
  - All 4 event files in `wiki/arcs/1-the-perfect-family/events/` → relevant character files
- Convert existing `## Related Files` and `## Cross-Refs` headings to `## Related` for consistency

### Phase 3: Add selective tags

Add `tags:` to front matter for substantive files touching these 10 cross-cutting topics:
`amber`, `mewtwo`, `erika`, `team-rocket`, `celadon`, `pallet-town`, `trainer-systems`, `clan-system`, `arc1-kanto`, `aura`

This enables agent cluster queries without the path-staleness risk of YAML references.

### What NOT to do

- **Don't create a YAML `related` field.** The path maintenance cost is higher than the benefit over Scheme 3 inline sections. The same agents that can parse `related: []` YAML can also grep `^## Related` sections.
- **Don't merge wiki/future directories.** The semantic distinction is real and valuable. The connectivity gap is solvable at much lower cost.
- **Don't build 32 topic index files.** The trainer-systems/index.md shows that *local* indexes work — adjacent to the content they organize. Remote aggregator indexes go stale.

### Why this recommendation

The repo has a working proof of concept in the trainer-systems/ cluster and the Mewtwo thread cluster — both well-connected, both using inline cross-reference sections. The problem isn't mechanism; it's coverage. The solution is proportionate: fix broken links, fill in the ~38 files that have zero cross-refs, standardize the heading, add lightweight tags for cluster discovery. Total work: roughly 40–50 file edits, no renames, no schema overhauls.

At 150 files the same approach still works. At 300+ files it might show strain (that's when YAML `related` or topic indexes become worth their cost), but this project is unlikely to reach that scale.
