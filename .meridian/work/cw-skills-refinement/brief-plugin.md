# Task: Plugin layer skill port, naming alignment, and router retirement

Read `context.md` in this directory FIRST. It has the full research, principles, and repo state. This brief only covers your specific task.

Load the `skill-creator` skill before you start — you will be porting and creating skill files.

## Your scope

Three coordinated changes in the plugin layer at `/Users/jimmyyao/gitrepos/creative-writing-skills/cw/`:

1. Port critical meridian-layer skills into the plugin layer as `cw/skills/<name>/` directories.
2. Align plugin skill naming with the meridian layer (rename `cw-story-critique` → plugin-layer `prose-critique`, `cw-official-docs` → `wiki-docs`).
3. Retire `cw-router` as the default tier 2/3 entry point — keep it available only for Claude.ai web UI users.

Do NOT touch the meridian layer (top-level `agents/` or `skills/`). Other spawns are doing that.
Do NOT create or rename any agents. A different spawn is handling agent-level architectural changes.

## Change 1: Port critical skills to the plugin layer

### Why port

The meridian layer has 12 skills. The plugin layer currently has 6 old-style skills under `cw/cw-*/`. When the plugin agents were ported from meridian, they had to inline content from dropped skills, which works as a short-term port strategy but leaves the plugin agents carrying knowledge that should live in shared skills so updates propagate.

The `writing-principles` skill in particular is getting rewritten in parallel (a separate spawn) and the plugin layer cannot see it yet. Porting it is the highest-value move.

### What to port (ordered by priority)

1. **`writing-principles`** — critical. Contains the four-channel reward frame and documented failure modes. The plugin `cw-writer` and `cw-critic` agents need access.
2. **`writing-artifacts`** — needed for `.meridian/fs/` conventions in plugin agents.
3. **`writing-staffing`** — needed for orchestrator fan-out guidance in the plugin.
4. **`story-decisions`** — needed for decision capture format.
5. **`story-context`** — needed for what context to load when drafting.
6. **`story-architecture`** — needed for outliner methodology.

Lower priority (skip unless trivial):
- `knowledge-graph` — stays inlined in graph-maintainer and explorer for now.
- `prose-analysis` — specialized; port later.

### How to port each skill

- Create `cw/skills/<name>/` matching the meridian-layer `skills/<name>/` structure.
- Copy `SKILL.md` and any `resources/` files.
- Adapt the content for the plugin context:
  - Drop or replace `$MERIDIAN_WORK_DIR` references — the plugin context does not have meridian work scopes. Use explicit user-specified paths or `.meridian/fs/` as appropriate.
  - Keep `.meridian/fs/` references — the plugin stores long-lived reference material there intentionally (decision made in the prior session to enable upgrade path from plugin to meridian).
  - Drop any references to `meridian spawn` commands where the plugin can't invoke them. Replace with the equivalent plugin action if there is one, or a note that the guidance applies to meridian users and plugin users should use the slash-command entry point instead.
  - Preserve all research citations and the four-channel frame verbatim.
- Follow the skill-design principles in `context.md` part 4: description serves the caller (describes WHEN to use), body stays digestible, progressive disclosure through `resources/`, no aggressive language, no prescribed sequences.
- If the meridian-layer `writing-principles` is being rewritten in parallel and is not yet settled at the time you're porting, port the CURRENT version you see on disk and note in your report that the plugin copy will need a follow-up sync pass once the meridian rewrite lands. Coordinate by timestamp, not by assumption — read the meridian file each time.

### Plugin agent updates

After porting, update the plugin agents under `cw/agents/` to:
- Reference the newly ported skills by name instead of relying on inlined content.
- Remove the inlined content that the new skill now carries. Replace with a pointer: "See the `writing-principles` skill for the composite reward frame and documented failure modes."
- Keep skill references accurate — if the plugin agent was loading a skill that didn't exist before, it should now load the real skill via whatever mechanism the plugin layer uses for skill loading.

### What NOT to port

- `knowledge-graph` and `prose-analysis` — lower priority, skip this pass.
- Any meridian-specific skills that don't apply to plugin users (if any).

## Change 2: Plugin naming alignment

### What to rename

- `cw/cw-story-critique/` → consolidate into the ported `cw/skills/prose-critique/` from Change 1. The old `cw-story-critique/` directory and its contents become the new skill's starting point (adapted), merged with anything additional from the meridian `prose-critique` skill.
- `cw/cw-official-docs/` → consolidate into `cw/skills/wiki-docs/`. Same pattern — adapt the old content, merge with anything from the meridian `wiki-docs` skill.
- `cw/cw-brainstorming/`, `cw/cw-prose-writing/`, `cw/cw-style-skill-creator/` — these don't have clean meridian-layer equivalents. Leave them alone for this spawn unless they become unreachable after the other changes. If they should be migrated to `cw/skills/<name>/`, flag it in your report as follow-up rather than doing it yourself — the naming alignment here is specifically for the two skills that have direct meridian equivalents with divergent names.

### Cross-reference updates after renames

- Grep the whole `cw/` tree for `cw-story-critique` and `cw-official-docs`. Update every reference in plugin agents, READMEs, plugin marketplace config, and any skill body or resource that mentions them. After your edits, those old names should not appear outside git-tracked rename history.
- Plugin command entries (if there are slash commands like `/cw:story-critique`) need to update to `/cw:prose-critique` and `/cw:wiki-docs`. Check for any `marketplace.json` or `plugin.json` files under `cw/` or `.claude-plugin/` that list commands.
- README and top-level plugin docs should use the new names.

## Change 3: Retire `cw-router` as tier 2/3 default

### Context

The `cw-router` skill was the original plugin's natural-language entry point — it routed user input to the appropriate cw-* skill. In tier 2 (Cowork) and tier 3 (Claude Code plugin), the better entry point is `cw-story-orchestrator`, which coordinates the agents directly. Tier 4 (Claude.ai web UI) can't install agents, so the router remains the fallback for web UI users only.

### What to change

- Do NOT delete `cw-router` or its content. It stays in place for tier 4 users.
- Update plugin marketplace config (whatever `marketplace.json` or `plugin.json` drives tier 2/3 installation) so that installing the plugin in tier 2/3 does not activate the router as the primary entry point. The primary entry point for tier 2/3 should be `cw-story-orchestrator`.
- Update the plugin README to clearly document the tier model: tier 4 users use the router; tier 2/3 users use the orchestrator. If the README already does this and just needs a note that the router is web-UI-only going forward, add that.
- Update any cross-references in other plugin skills that currently say "use the router" — they should point to the orchestrator for the common case.

## Quality bar

- Skill bodies follow `context.md` part 4 strictly. No role identity, no aggressive language, no prescribed sequences. Descriptions trigger loading by describing when to use the skill, not how.
- Progressive disclosure: description (short, triggers) → SKILL.md body (digestible, core teaching) → resources (on-demand depth). Each level adds new information; no repetition.
- Plugin skills reference `.meridian/fs/` for long-lived knowledge and follow the same convention as the existing plugin agents. Do NOT introduce a new storage root.
- Citations from the meridian layer are preserved verbatim in the plugin port. Do not invent new citations. Do not drop research grounding.
- After your edits, grep the plugin layer for the old skill names (`cw-story-critique`, `cw-official-docs`) and confirm they only appear in git history or in the retained tier-4 router references, not in live agent or skill content.
- Plugin agents should no longer inline content that the ported skills now carry. Replace with pointers to the skill.

## What you must NOT do

- Do not touch the meridian layer (top-level `agents/` or `skills/`).
- Do not create or rename agents.
- Do not delete `cw-router` or its content.
- Do not port `knowledge-graph` or `prose-analysis` (lower priority).
- Do not hardcode models in skill bodies.
- Do not use aggressive language.
- Do not fabricate citations.
- Do not collide with the other spawns: do NOT rewrite `skills/writing-principles/SKILL.md` (that's a separate spawn's exclusive scope) and do NOT touch agent files (another separate spawn owns that). For the plugin port of `writing-principles` specifically, copy the CURRENT state of the meridian file at the time you read it and flag the need for a follow-up sync in your report.

## Report

When done, write a report that includes:
- Full list of files created, renamed, modified, or deleted (relative to the creative-writing-skills repo).
- Which meridian skills you ported and which you deliberately skipped (with reason).
- A before/after mapping of the plugin skill naming changes.
- The specific marketplace/plugin config changes you made to retire the router as tier 2/3 default.
- Any coordination notes: if you had to read a file another spawn might be editing, note the timestamp or content state you saw.
- Any judgment calls (what counted as "inlined content worth replacing" versus "content the agent should keep directly," whether any plugin skill needed more adaptation than a straight copy).
- Anything you noticed that should be follow-up work but was out of scope.
