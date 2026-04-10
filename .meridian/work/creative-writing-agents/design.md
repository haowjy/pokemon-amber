# Creative Writing Skills — Meridian Package Design

## Overview

A multi-agent creative writing system built on meridian. Ships as a single repo (`creative-writing-skills`) with two distribution layers:

- **Meridian layer** (`agents/` + `skills/`) — full multi-agent workflow for meridian users
- **Plugin layer** (`creative-writing-skills/`) — derived, simplified skills for Claude Code / Claude.ai plugin users

One repo, one community, two install paths. Plugin users get craft skills. Meridian users get craft skills + agents + coordination.

## Repo Structure

```
creative-writing-skills/
├── agents/                          # meridian agents
├── skills/                          # meridian skills
├── creative-writing-skills/         # plugin layer (existing, derived from skills/)
│   ├── cw-brainstorming/
│   ├── cw-prose-writing/
│   ├── cw-story-critique/
│   ├── cw-official-docs/
│   ├── cw-style-skill-creator/
│   └── cw-router/
├── mars.toml
├── .claude-plugin/
├── zips/
└── build-plugin.sh                  # derives cw-* from skills/, builds .skill zips
```

`mars.toml` targets `agents/` and `skills/`. Plugin manifest targets `creative-writing-skills/`. The `build-plugin.sh` script generates plugin skills from meridian skills by stripping meridian concepts, keeping craft knowledge, and adding a note advertising the meridian version.

## Dependencies

```toml
[package]
name = "creative-writing-skills"
version = "2.0.0"

[dependencies.meridian-base]
url = "https://github.com/haowjy/meridian-base"

[dependencies.meridian-dev-workflow]
url = "https://github.com/haowjy/meridian-dev-workflow"
skills = ["mermaid"]
```

---

## Agents

### Orchestrators

Three orchestrators own the three major workflows. None of them write files directly.

#### writing-orchestrator

User-facing entry point. Owns the author relationship — understanding intent, gathering context, and making sure the right work gets done. Never writes files, never drafts prose. Its value is coordination altitude.

**What it does:**
- Understands what the author wants to explore, write, or decide
- Fans out researchers and brainstormers across models, synthesizes results, presents options
- Brainstorms interactively with the user (loads brainstorming skill)
- Kicks off draft-orchestrator when direction is confirmed and author says "write it"
- Kicks off knowledge-orchestrator when decisions are made and need to be recorded
- Reviews results from autonomous orchestrators, presents to user with synthesis
- Synthesizes critic reports into prioritized, actionable feedback (pattern-level: "3 of 4 critics flagged pacing in scenes 2-4")

**Skills:** writing-staffing, story-context, writing-artifacts, story-decisions, brainstorming, knowledge-graph, __meridian-spawn, __meridian-session-context, __meridian-work-coordination

**Permissions:** read + spawn. No file writes. No Edit/Write tools.

#### draft-orchestrator

Autonomous. Executes a writing plan through writer -> critic -> revise loops until converged. Picks which style files to pass to the writer, assigns critic focus areas based on the content.

**What it does:**
- Receives a scene/chapter brief with outline and approved direction
- Selects style files from `.meridian/fs/styles/` based on the task (POV, scene type, tone)
- Spawns writer with brief + style files + relevant context
- Fans out critics with different focus areas (structure, character, voice, prose, continuity)
- Synthesizes critic findings, spawns writer to revise
- Iterates until critics converge (no new substantive findings)
- Reports back with final draft + critique synthesis

**Loop:**
```
writer -> [critics in parallel, different focus areas] -> writer revises -> [critics] -> converge -> done
```

**Skills:** writing-staffing, story-context, writing-artifacts, story-decisions, __meridian-spawn

**Permissions:** read + spawn. No file writes.

#### knowledge-orchestrator

Autonomous. Keeps `.meridian/fs/` current. Triggered after brainstorming sessions, after chapters are written, after critique rounds — whenever the project's knowledge state has changed.

**What it does:**
- Figures out what changed (new chapter? brainstorm session? wiki update?)
- Dispatches the right knowledge maintenance agents:
  - session-miner after conversations/brainstorms
  - chronicler after chapters are written/revised
  - graph-maintainer after any `.meridian/fs/` updates
- Ensures `.meridian/fs/` stays coherent and cross-linked

**Skills:** writing-staffing, story-context, writing-artifacts, story-decisions, knowledge-graph, __meridian-spawn, __meridian-session-context

**Permissions:** read + spawn. No file writes.

---

### Writers

#### writer

Drafts prose from scene briefs and style files. Its output is draft text — not final, subject to critique and revision. Follows the project's established voice and conventions.

**Skills:** prose-writing, writing-principles, story-context

**Permissions:** workspace-write

#### outliner

Structures story at the arc, chapter, and beat level. Produces outlines and mermaid diagrams for arc structure, timeline visualization, and character relationship maps.

**Skills:** story-architecture, brainstorming, mermaid

**Permissions:** workspace-write

#### wiki-editor

Creates and updates polished, reader-facing reference pages in `wiki/` (or wherever the project keeps reader-facing docs). Maintains link discipline — every entity mention gets a link on first appearance, relationship diagrams embedded via mermaid. Distinct from knowledge maintenance agents that maintain `.meridian/fs/`.

**Skills:** wiki-docs, mermaid, knowledge-graph

**Permissions:** workspace-write + WebSearch, WebFetch

---

### Critics

#### critic

Reviews drafts against style guides and craft principles. Focus-area driven — the orchestrator specifies which dimension to examine. Each spawn gets one focus area and goes deep on it.

**Focus areas** (specified in prompt, catalog in writing-staffing skill):
- **structure** — plot logic, pacing, scene necessity, stakes, setup/payoff
- **character** — motivation coherence, arc progression, relationship dynamics
- **voice** — dialogue quality, POV consistency, subtext, voice drift
- **prose** — line-level quality, rhythm, clarity, repetition, show vs tell
- **continuity** — facts, timeline, geography, character state

Each focus area has a dedicated resource in the prose-critique skill.

**Skills:** prose-critique, writing-principles

**Permissions:** read-only

#### continuity-checker

Cross-references content for contradictions across the full project. Maintains awareness of timeline, character state, geography, and established facts. Uses the knowledge graph to find what to cross-reference.

**Skills:** prose-critique (continuity resource), knowledge-graph

**Permissions:** read-only

---

### Knowledge Maintenance

#### session-miner

Extracts decisions, facts, and commitments from conversations and brainstorm sessions. Mines past sessions for story direction choices, character decisions, rejected alternatives, worldbuilding commitments, open questions deferred. Writes findings to `.meridian/fs/` with inline decision annotations.

**Skills:** __meridian-session-context, story-decisions, writing-artifacts

**Permissions:** workspace-write

#### chronicler

Extracts story facts from written chapters — character state, timeline events, canon facts, relationship changes. Reads the manuscript and produces compressed, annotated entries in `.meridian/fs/`. Not a copy of the chapter — a synthesis of what changed in the project's factual state.

**Skills:** knowledge-graph, writing-artifacts

**Permissions:** workspace-write

#### graph-maintainer

Keeps relationship maps and cross-links current across all `.meridian/fs/` content. Runs the knowledge-graph parsing script, rebuilds connection maps, flags orphaned documents and missing back-links, updates mermaid relationship diagrams.

**Skills:** knowledge-graph, mermaid, writing-artifacts

**Permissions:** workspace-write

---

### Research & Exploration

#### researcher

Web research via search and fetch. Focus area specified in the prompt — the writing-staffing skill teaches the orchestrator which focus to specify.

**Research focus areas** (catalog in writing-staffing skill):
- **craft** — narrative technique, how published authors handle X, craft book references
- **world** — real-world references for worldbuilding (history, science, culture, geography)
- **genre** — conventions, reader expectations, tropes, market context
- **sensitivity** — representation, authenticity, community perspectives, common pitfalls
- **fact-check** — verifying specific claims (dates, locations, technical details)

The researcher produces thorough reports with trade-off analysis and source URLs. Its report is the deliverable.

**Skills:** none (prompt-driven)

**Permissions:** read-only + WebSearch, WebFetch

#### explorer

Fast, cheap local content reading. Navigates the project's files and knowledge graph to gather context before more expensive agents run. Also mines past sessions for historical context. The agent other agents call when they need to understand what exists.

**Skills:** knowledge-graph, __meridian-session-context

**Permissions:** read-only

---

### Style

#### style-analyzer

Analyzes the author's writing samples and produces style files to `.meridian/fs/styles/`. Run against different sample chapters to extract different voices. Run against scene-type chapters to extract scene techniques. Each output is a standalone reference file.

Produces files like:
- `voice-amber-1p.md` — first-person narration voice
- `voice-fuji-3p.md` — third-person character voice
- `scene-battle.md` — battle scene techniques
- `tone-grief.md` — heavy emotional register
- `formatting.md` — mechanical conventions (em dashes, ellipsis, etc.)

**Skills:** writing-artifacts

**Permissions:** workspace-write

---

### Role-Playing

#### role-player

Becomes a character for freeform, unscripted conversation. Discovery through performance — the author (or another agent) interacts with the character to find voice, test dynamics, explore reactions in unplotted situations. Stays in character, doesn't break to explain, doesn't over-narrate.

Works with whatever character context it's given — a full `.meridian/fs/` profile with voice style and character state, or just a two-sentence sketch in the prompt. Both are valid. Early-stage characters that don't have files yet can be role-played from a description alone.

**When files exist:** Loads voice style from `.meridian/fs/styles/voice-*.md` and character state from `.meridian/fs/characters/`. The combination gives it voice patterns AND factual grounding (what the character knows, where they are in the story, their relationships).

**Ad hoc mode:** Character description comes entirely from the prompt. "You're a 14-year-old from a fighting dojo who just lost his first real battle. You're proud, stubborn, and your dad is watching. React." No files needed. Useful for:
- Characters that don't exist yet
- One-off NPCs the author is sketching
- "What if" scenarios with modified character traits
- Exploring a character before committing to a profile

**Use cases:**
- **Voice discovery** — hear how a character sounds in different emotional states
- **Relationship testing** — play out unscripted encounters between characters
- **Stress testing** — confront a character with unexpected situations, see authentic reactions
- **Group dynamics** — orchestrator fans out multiple role-players as different characters, gives them a situation, lets them interact
- **Unplotted exploration** — "What would this character do if...?" — not for canon, for understanding
- **Ad hoc sketching** — describe a character on the fly, interact with them to discover who they are before writing anything down

**Fan-out pattern:** The writing-orchestrator spawns multiple role-players as different characters in the same scene. Each loads a different voice + character state. They interact autonomously while the author observes. The session-miner can later extract voice patterns, relationship dynamics, and character insights from the transcripts.

**Skills:** writing-principles (to avoid AI-isms while in character)

**Permissions:** read-only (doesn't write files — the value is the conversation itself, mined later by session-miner)

---

## Skills

### Coordination Skills (loaded by orchestrators)

#### writing-staffing

Which agents for which writing tasks. Critic focus area catalog, research focus area catalog, effort scaling, model fan-out patterns for brainstorming and critique.

**Resources:**
- `resources/critics.md` — critique focus area catalog with guidance on when to use each
- `resources/researchers.md` — research focus area catalog
- `resources/builders.md` — writer, outliner, wiki-editor dispatch guidance
- `resources/knowledge.md` — session-miner, chronicler, graph-maintainer dispatch
- `resources/role-play.md` — role-player dispatch, multi-character fan-out, voice discovery patterns

**Consumers:** writing-orchestrator, draft-orchestrator, knowledge-orchestrator

#### story-context

What context to pass between writing agents. The writing parallel of context-handoffs from dev-workflow. Teaches which chapters, wiki pages, style files, outlines, and `.meridian/fs/` artifacts to pass via `-f` when spawning. Poor handoffs cause writers to invent contradictions and critics to miss relevant context.

**Consumers:** writing-orchestrator, draft-orchestrator, writer

#### writing-artifacts

Where agent output goes. Defines the `.meridian/fs/` structure and `$MERIDIAN_WORK_DIR/` conventions. Teaches when to promote from work dir to fs.

**`.meridian/fs/` structure (durable project knowledge):**
```
.meridian/fs/
├── styles/              # voice, scene-type, tone guides (style-analyzer output)
├── characters/          # character state + decision annotations
├── world/               # locations, lore, systems, factions
├── timeline/            # chronology, event ordering
├── canon/               # established facts from chapters
└── graphs/              # relationship maps, knowledge graph output
```

**`$MERIDIAN_WORK_DIR/` structure (temporary work scratch):**
```
$MERIDIAN_WORK_DIR/
├── outline/             # current outline being worked
├── drafts/              # draft iterations
├── critique-reports/    # critic output for this round
└── brainstorm/          # brainstorm captures
```

Durable knowledge gets promoted to `.meridian/fs/` by the orchestrator when work completes. Decisions are baked inline with the artifacts they relate to, not in separate files.

**Consumers:** all orchestrators, style-analyzer, chronicler, session-miner

#### story-decisions

Recording and mining story direction decisions. What was decided, what was rejected, why. Teaches proactive capture (record as you go) and retroactive mining (extract from past sessions).

Decisions are written inline with the artifacts they relate to in `.meridian/fs/`. A character state entry includes why that age was chosen. A timeline entry includes why events are ordered that way. Not a separate decisions file.

**Consumers:** writing-orchestrator, knowledge-orchestrator, session-miner

---

### Craft Skills (loaded by specialist agents)

#### prose-writing

How to write prose. Covers technique for drafting fiction — not project-specific voice (that comes from style files in `.meridian/fs/styles/`). Supports two modes:
- **Interactive** — back-and-forth with author in conversation
- **Autonomous** — receives a brief, produces a draft

**Consumers:** writer

#### brainstorming

How to capture story brainstorming. Minimal elaboration, source tagging (`<AI>`, `<hidden>`), preserve creative freedom. Supports two modes:
- **Interactive** — back-and-forth with author
- **Autonomous** — receives a scoped prompt, explores, produces a structured brainstorm report (for fan-out pattern)

**Resources:**
- `resources/chapter-planning.md` — beat and scene exploration
- `resources/character-development.md` — motivations, arcs, relationships
- `resources/worldbuilding.md` — world elements, systems, cultures
- `resources/continuity-timeline.md` — timeline tracking, contradiction handling

**Consumers:** writing-orchestrator, outliner

#### prose-critique

Adversarial reading methodology. The writing parallel of dev-workflow's review skill. Focus-area driven with dedicated resources per area. Teaches the critic to find what doesn't work, not confirm what does.

**Resources:**
- `resources/structure.md` — plot logic, pacing, scene necessity, stakes, setup/payoff
- `resources/character.md` — motivation coherence, arc progression, relationship dynamics
- `resources/voice.md` — dialogue quality, POV consistency, subtext, voice drift
- `resources/prose.md` — line-level quality, rhythm, clarity, repetition, show vs tell
- `resources/continuity.md` — facts, timeline, geography, character state

**Consumers:** critic, continuity-checker

#### prose-analysis

Mechanical prose analysis — scripts that produce quantitative signals the critic uses to inform subjective judgment. Not quality verdicts. Comparison against the project's own baseline, not universal benchmarks (research shows there are no reliable universal thresholds).

**What the scripts measure:**
- Sentence length distribution (mean, variance) — compare across chapters for consistency
- Sentence opener variety
- Lexical variability (MATTR, not raw TTR)
- Dialogue-to-narration ratio per scene
- Repetition detection (echoed words, repeated phrases)
- Pronoun distribution (POV consistency check)

**AI antipattern awareness (resource, not scripts):**
- Research-backed signals: lower lexical variability, fewer personal pronouns, more positive-emotion language, shallow interiority, low subtext
- Community-identified structural patterns: "clean but hollow" prose, generic arc progression, repetitive emotional choreography, overused metaphor clusters, tidy-summary endings
- Explicitly framed: these are investigation triggers, not proof. Word-level "slop lists" are folklore, not reliable detection.

**Resources:**
- `resources/analysis-scripts/` — bash/python scripts for mechanical metrics
- `resources/antipatterns.md` — AI writing antipatterns (research-backed vs folklore, honestly labeled)
- `resources/baseline.md` — how to establish and compare against project baseline

**Consumers:** critic, style-analyzer

#### wiki-docs

Encyclopedic reference documentation for reader-facing pages. Link discipline (every entity mention linked on first appearance), mermaid relationship diagrams, citation conventions. Teaches the difference between wiki/ (reader-facing, polished, spoiler-managed) and .meridian/fs/ (author/agent-facing, annotated, everything included).

**Resources:**
- `resources/page-patterns.md` — examples from minimal to complex
- `resources/citation-guide.md` — how to cite chapters and sources

**Consumers:** wiki-editor

#### story-architecture

Arc structure, narrative design, pacing, beat frameworks. Teaches the outliner how to structure story at multiple levels — saga, arc, chapter, scene. Not prescriptive about methodology (plotters vs pantsers vs hybrid) — teaches structural thinking that applies regardless of process.

**Consumers:** outliner

#### writing-principles

Anti-patterns that AI writing agents systematically violate. The writing parallel of dev-principles. Loaded by writers and critics to prevent and catch common failures.

**Principles:**
- Don't over-elaborate beyond what was asked
- Don't flatten voice into generic AI prose
- Don't info-dump worldbuilding (reveal through experience, conversation, consequences)
- Show, don't tell (demonstrate states through action, not narration)
- Don't resolve tension prematurely
- Don't homogenize character voices
- Don't add unsolicited emotional commentary
- Preserve ambiguity when the author hasn't decided
- Match the project's established prose style, don't introduce a new one
- Understate rather than overstate emotional moments

**Consumers:** writer, critic

---

### Tool Skills (loaded by any agent that needs them)

#### knowledge-graph

Navigation skill. Parses all markdown files and builds a map of how the project's documents connect. Any agent loads it when they need to orient on the project or find related content.

**What it parses:**
- Explicit markdown links (`[text](path)`)
- Wikilinks (`[[entity-name]]`)
- Mermaid relationship blocks in wiki pages
- Entity name mentions (grep across .md files)
- YAML front matter references
- `See:` reference patterns

**What it outputs:**
- Full connectivity graph
- Orphaned documents (nothing links to them)
- Missing back-links (A -> B but B doesn't -> A)
- Clusters of related content
- Entity mention map (which docs mention which entities)

**Bundled:** `resources/graph.sh` — the parsing script agents execute

**Consumers:** explorer, continuity-checker, wiki-editor, graph-maintainer, writing-orchestrator

#### mermaid

Mermaid diagram syntax and validation. Pulled from meridian-dev-workflow as a dependency. Used for relationship diagrams in wiki pages, arc structure visualizations, timeline flows, knowledge graph output.

**Consumers:** outliner, wiki-editor, graph-maintainer, explorer, continuity-checker

---

## File Layers

### Author's space (visible repo, author controls structure)

```
wiki/                        # reader-facing reference pages (polished, spoiler-managed)
story/                       # manuscript (however the author organizes it)
future/                      # planning docs (author's system)
```

Agents read from here. The wiki-editor writes to `wiki/`. Agents don't reorganize the author's manuscript or planning structure.

### Agent-maintained project knowledge (.meridian/fs/)

```
.meridian/fs/
├── styles/                  # voice, scene-type, tone guides
│   ├── voice-*.md           #   character voices / POV styles
│   ├── scene-*.md           #   scene-type techniques
│   ├── tone-*.md            #   tonal registers
│   └── formatting.md        #   mechanical conventions
├── characters/              # character state + decision annotations
├── world/                   # locations, lore, systems, factions
├── timeline/                # chronology, event ordering
├── canon/                   # established facts from chapters
└── graphs/                  # relationship maps, knowledge graph output
```

Maintained by knowledge maintenance agents (session-miner, chronicler, graph-maintainer). Both humans and agents read it. Quality bar: readable prose with clear structure, not agent shorthand. Decisions baked inline with reasoning.

### Work scratch ($MERIDIAN_WORK_DIR/)

```
$MERIDIAN_WORK_DIR/
├── outline/                 # current outline being worked
├── drafts/                  # draft iterations
├── critique-reports/        # critic output
└── brainstorm/              # brainstorm captures
```

Temporary, scoped to current work item. Archived when work completes. Durable knowledge promoted to `.meridian/fs/` before closing out.

---

## Key Patterns

### Brainstorm Fan-Out

Writing-orchestrator fans out brainstormers across different models for creative diversity:

```
User: "How should Amber meet Kyle on Route 1?"
    |
writing-orchestrator (scopes the question)
    |-- brainstormer A (model X) -> combat-meeting angle
    |-- brainstormer B (model Y) -> comedic-misunderstanding angle
    |-- brainstormer C (model Z) -> shared-threat angle
    |
writing-orchestrator synthesizes -> presents options to user
```

Each brainstormer loads brainstorming skill, runs in autonomous mode, produces structured report. Different models bring different creative sensibilities.

### Draft/Critique Loop

Draft-orchestrator runs the revision pipeline:

```
writer (with style files + brief)
    |
    v
critics in parallel:
    |-- critic (focus: structure)
    |-- critic (focus: voice)
    |-- critic (focus: continuity)
    |
    v
draft-orchestrator synthesizes findings
    |
    v
writer revises (with critique synthesis)
    |
    v
critics again -> converge? -> done
```

### Knowledge Update Flow

After any content change, knowledge-orchestrator updates project knowledge:

```
"New chapter drafted"
    |-- chronicler (extract facts from chapter -> .meridian/fs/)
    |-- session-miner (extract decisions from drafting sessions -> .meridian/fs/)
    |-- graph-maintainer (update relationships, rebuild links)

"Brainstorming session ended"
    |-- session-miner (extract decisions/commitments -> .meridian/fs/)
    |-- graph-maintainer (update if new entities surfaced)
```

### Full Workflow

```
User: "I want to figure out how Amber meets Kyle"
    |
writing-orchestrator fans out brainstormers
    |
synthesizes, presents options to user
    |
user picks direction, iterates
    |
writing-orchestrator -> knowledge-orchestrator
    |-- session-miner records decisions to .meridian/fs/
    |
user: "ok write it"
    |
writing-orchestrator -> draft-orchestrator
    |-- writer drafts -> critics review -> revise -> converge
    |
draft-orchestrator reports back
    |
writing-orchestrator presents draft + critique synthesis to user
    |
knowledge-orchestrator runs
    |-- chronicler extracts facts from new chapter
    |-- graph-maintainer updates relationships
```

---

## Plugin Derivation

`build-plugin.sh` generates `creative-writing-skills/cw-*` from `skills/`:

| Meridian skill | Plugin skill |
|---|---|
| `brainstorming` | `cw-brainstorming` |
| `prose-writing` | `cw-prose-writing` |
| `prose-critique` | `cw-story-critique` |
| `wiki-docs` | `cw-official-docs` |
| (style-analyzer agent logic) | `cw-style-skill-creator` |
| (writing-orchestrator routing) | `cw-router` |

**Derivation rules:**
- Strip meridian concepts (spawns, work dirs, `-f` references, autonomous mode)
- Strip coordination-layer references (writing-staffing, story-context, etc.)
- Keep craft knowledge intact
- Simplify to single-session conversational context
- Add note: "For multi-agent workflows with autonomous drafting, critique loops, and knowledge maintenance, see the meridian version of this package"

Coordination skills (writing-staffing, story-context, writing-artifacts, story-decisions) and tool skills (knowledge-graph) have no plugin equivalents — they only make sense with agents.

---

## Research Findings (informing skill content)

### Prose Quality Metrics (from research spawns)

No reliable universal benchmarks exist for "good prose." The prose-analysis skill uses metrics as signals, not verdicts:

- Sentence length variance: weak signal. Useful for baseline comparison, not as a target.
- Readability scores (Flesch-Kincaid): not a quality predictor for fiction.
- Vocabulary richness (raw TTR): methodologically weak. Use MATTR if measuring.
- Perplexity: very low can indicate bland writing. Not a quality metric.
- Adverb/filter word density: modest effect sizes, genre-confounded. Investigation triggers, not rules.
- No single accepted universal benchmark exists across literary traditions.

Source: Ashok et al. (EMNLP 2013), van Cranenburgh (EACL 2017), van Dalen-Oskam (2023), OpenMEVA (ACL 2021).

### AI Antipatterns (from research spawns)

Research-backed signals of AI-generated prose:
- Lower lexical variability and higher repetitiveness
- Fewer personal pronouns, more positive-emotion language
- Shallow character interiority, low dialogue subtext
- "Clean but hollow" prose, generic arc progression
- Tidy-summary endings, repetitive emotional choreography

Community-identified but not research-proven:
- "Slop word" lists (delve, tapestry, etc.) — model-version dependent, near-random for Claude
- Single-phrase heuristics — useful for editorial triage, not proof

Source: Kobak et al. (2024), BEA 2025, Ghostbuster (NAACL 2024), RAID (ACL 2024), Nature HSSCOMMS (2025).

### Writing Task Taxonomy (from research spawns)

Professional fiction writing lifecycle phases: Ideation -> Research/Worldbuilding -> Outlining -> Drafting -> Revision -> External Feedback/Editing -> Publishing.

Tasks writers delegate to AI: brainstorming, outlining, research support, developmental feedback, grammar/cleanup, word/phrase alternatives.

Tasks writers keep: final voice decisions, emotionally pivotal scenes, publishable text without revision, authorship decisions.

Biggest unmet need: automated continuity validation across chapters, unified "story operations" layer combining drafting/continuity/revision.

Source: EFA, Jane Friedman, Reedsy, Gotham 2025 AI survey, AO3 TOS, writing community forums.
