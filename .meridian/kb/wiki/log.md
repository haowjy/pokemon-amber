# Wiki Operations Log

Append-only chronological record of ingests, queries worth saving, and
lint passes. Latest entries at the bottom.

Format: `[YYYY-MM-DD] [op] description`

Operations:
- `init` --- one-time setup
- `ingest` --- new source integrated into wiki
- `lint` --- health-check pass
- `query-saved` --- query result filed as a wiki page
- `migrate` --- bulk move from legacy structure

---

[2026-05-09] [init] Wiki initialized. Layout per `AGENTS.md`. Empty until
content migration from `wiki/` and `future/` (main repo) lands.

[2026-05-09] [migrate] Phase A complete. 80 files bulk-copied from wiki/ and
future/ to kb/wiki/. Includes: 9 characters, 8 places, 3 organizations, 16
lore subfolder files (crime, government, history, mechanics, tech,
trainer-systems split files), timeline, arc 1 outline + 4 events, team
file, kyle-kong, 5 future arcs, 5 future plot threads (mewtwo-thread
underscore dropped). Originals still present in main repo until Phase F
cleanup. Cross-refs not yet rewritten --- Phase G handles that.

[2026-05-09] [migrate] Phase B complete. Lore cluster splits done.
- aura: split into aura-system.md (concept) and aura-mechanics.md (deep dive)
- economy: renamed to economics/index.md (kept pokeball-pricing alongside)
- trainer-systems: 3 new pages from old big file --- cultural-history,
  licensing, career-paths. Old big trainer-systems.md content distributed.
- world-mechanics: split into 4 pages --- pokemon-sustenance (new),
  pokemon-fainting (existing stub expanded), pokeball-technology (new),
  power-scaling (new). Aura section was redundant with aura-mechanics
  (discarded). _plot-secrets.md is just a redirect index --- skip.

[2026-05-09] [migrate] Phase C partial. Worldbuilding decomposition started.
- Currency contradiction filed at contradictions/currency-notation.md
  (resolution: ₽ canon, ¥ legacy --- being dropped via migration)
- Stubs: sabrina.md, 8 gym stubs (pewter, cerulean, vermillion, fuchsia,
  lavender-ghost, viridian-forest-bug, east-coast-water, route-11-ground)
- Substantive new pages: viridian-gym (with TR HQ overlay),
  saffron-fighting-dojo, saffron-psychic-gym, world-opening-timeline,
  plot-threads/saffron-gym-rivalry.
Still pending in Phase C: clan-system page, 4 substantial clan pages,
clans/index.md, team-rocket.md updates (Madame Boss canon), character
page updates for Amber/Kyle economic positioning, Giovanni page (deferred
until other Giovanni-relevant files processed).

[2026-05-09] [migrate] Phase E bulk done. tone.md (from TONE.md),
themes/core-story-elements.md (from future/core/themes.md), and 4
workspace docs (current-direction, open-questions, archive, meta-notes)
all copied to their new locations.

[2026-05-09] [migrate] Phase C complete. Clan + Giovanni cluster done.
- Clan core: lore/clan-system.md (Johto vs Kanto framework, drafting status)
- Clans index: organizations/clans/index.md (14 clans cataloged + lightweight
  Kanto family mentions)
- Substantive clan pages: clans/silvertail.md (Madame Boss / TR origin canon),
  clans/viridian-house.md (Giovanni parentage / dual inheritance canon)
- Team-rocket update: appended Clan & Family Origins section linking to
  silvertail, viridian-house, and explaining the dual inheritance + org split
- Giovanni character page created: characters/giovanni.md (consolidates from
  gym-system-detailed.md, clan-system Viridian House entry, and references
  the existing plot-thread files)
- Character economic position updates: amber-mc.md gets walking-by-choice
  Oak-supported framing; kyle-kong.md gets family-money + Fighting Dojo
  desperation framing
- All currency notation in updates uses ₽ (per the contradiction resolution)

[2026-05-09] [migrate] Stubs copied (decision #10). 6 stub files migrated as
TODO markers to their new kb destinations:
- events/{kyle-meeting,pewter-gym-brock,route1-solo}.md
- arcs/{arc2-hoenn,arc3-beyond,arc-pikachu-handoff}.md
The future/plot/saffron-gym-rivalry stub is superseded by the substantive
plot-threads/saffron-gym-rivalry.md and not migrated separately.

[2026-05-09] [status] Migration content phases (A, B, C, D-stubs, E) complete.
116 markdown files in kb/. Remaining work:
- Phase D continued: content checks on plot-threads/* and arcs/* (some
  cross-cutting content may need redistribution to entity pages, e.g.
  giovanni-fuji-jail content into the new giovanni.md page)
- Phase F: delete wiki/ and future/ from main repo (destructive --- needs
  user OK)
- Phase G: cross-reference rewriting (wiki/ and future/ relative paths
  inside migrated files need normalization to kb [[wiki-link]] style)
- Phase H: populate wiki/index.md catalog
- Phase I: creative-writing-skills package update (separate repo)

[2026-05-09] [migrate] Phase G complete. 2 broken internal refs fixed in
trainer-systems/gym-system.md and trainer-systems/conference-system.md ---
both were "Primary design reference" citation links pointing to
future/worldbuilding/ source files. Converted to plain-text source notes
("content incorporated into this page") so they won't break when Phase F
removes future/ from the main repo. All other "wiki/" grep matches in kb/
are external bulbapedia URLs --- no action needed.

[2026-05-09] [migrate] Phase H complete. wiki/index.md populated with
one-line summaries for all 93 wiki pages, grouped by type: 13 characters,
19 places, 6 organizations, 7 events, 9 arcs, 6 plot-threads, 28 lore
pages across 7 subfolders, 1 theme page, 1 timeline, 1 contradiction.
Also flagged cinnabar-gym.md / cinnabar-island.md as partial duplicates
pending consolidation.

[2026-05-09] [status] Migration complete except Phase F (deletion of wiki/
and future/ from main repo --- awaiting user OK) and Phase I (separate
repo). Phase D re-evaluation: giovanni-fuji-jail.md is scene planning
content, appropriately separate from the giovanni.md entity page which
already cross-refs it. No redistribution needed.

[2026-05-09] [migrate] Phase F complete. Deleted wiki/ (43 files) and
future/ (29 files) from main repo via git rm --- 81 files total staged for
removal. All content was previously migrated to .meridian/kb/. Migration
fully complete (Phases A–H done). Remaining: Phase I (creative-writing-skills
package update, separate repo).
