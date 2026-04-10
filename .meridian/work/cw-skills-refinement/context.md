# Shared Context: Creative Writing Skills Refinement

This file is the shared research and principles context for all sub-tasks in this work item. Read this first. Your task-specific brief references it and builds on it.

The target repo is `/Users/jimmyyao/gitrepos/creative-writing-skills/`. It has two layers:
- **Meridian layer** (top-level `agents/` and `skills/`) — used by meridian spawns.
- **Plugin layer** (`cw/agents/` and `cw/cw-*/`) — Claude Code plugin for users without meridian.

Both layers should stay in sync.

---

## Part 1: Four Reader Reward Channels (the prescription frame)

Research across cognitive science, literary theory, and media psychology (p41 research spawn, session 13927c66) does NOT support a single dominant theory of why people enjoy reading fiction. It supports a **composite** of four separable but interacting reward channels that readers want simultaneously. Breaking any one damages enjoyment.

### 1. Transportation / absorption
Readers mentally enter the story world and become less aware of their immediate environment. Strong empirical support: meta-analysis of 132 effect sizes (van Laer et al. 2014, doi:10.1086/673383). Reading-specific flow research (Thissen et al. 2018, doi:10.3389/fpsyg.2018.02542) confirms absorption as a measurable construct with positive links to reading pleasure.

Prose that protects transportation: coherent narrative progression, consistent POV, concrete sensory grounding, minimal unearned confusion, no exposition passages that break the dream.

Prose that damages transportation: POV drift, factual/temporal inconsistencies (especially clustered in the middle of long narratives per "Lost in Stories" arxiv 2603.05890), sudden authorial intrusion, coherence gaps the reader can't paper over.

### 2. Aesthetic / stylistic pleasure
Literary language, foregrounding, novelty, and form are intrinsically rewarding — independent of plot and character. Narrativity and literariness shift readers toward an aesthetic attitude (Wimmer et al. 2023; van Peer et al. 2007). Style and suspense rely on different processing routes (Hartung et al. 2021). **Style is a separate reward channel, not decoration.**

Prose that protects the aesthetic channel: sentence-level variety, rhythm, distinctive voice, specific word choices that reward attention, sentence shapes that do work.

Prose that damages the aesthetic channel: syntactic templating (models reach for the same sentence structures repeatedly; templates are copied directly from pretraining data and NOT overwritten by alignment — Shaib et al. 2024 EMNLP, aclanthology.org/2024.emnlp-main.368), attractor-state fluency (RLHF models exhibit lower token entropy and "smoothed" output — "Creativity Has Left the Chat," arxiv 2406.05587), generic phrasing, lower uncertainty than human writers in creative tasks specifically (arxiv 2602.16162).

### 3. Social simulation / character modeling
Readers model characters as minds with motives, feelings, and perspective. Modestly supported (Dodell-Feder & Tamir 2018, doi:10.1037/xge0000395). **Important caveat:** the famous "literary fiction improves theory of mind" finding (Kidd & Castano) is contested — preregistered replications failed (Panero et al. 2016, pubmed 27642659; Kidd & Castano replication 2018/2019, doi:10.1177/1948550618775410). Treat social simulation as a real engagement mechanism but not a proven causal effect on real-world cognition.

Prose that protects social simulation: character access through concrete behavior and interiority, distinct voices per character, emotion shown through action and physical detail the reader has to interpret, characters whose inner states the reader can *model* rather than being told.

Prose that damages social simulation: labeled emotions ("she felt sad"), stock physical tells (clenched fists, shaky breaths, averted eyes used mechanically — the show-don't-tell rule applied without the specificity that makes it work), homogenized voices across characters, collapsed ambiguity where the narrator explains what the character doesn't know.

### 4. Flow / challenge-fit
Reading is most pleasurable when the text is challenging enough to engage but not so hard that fluency breaks (Thissen et al. 2018, inverted-U). Flow is a real construct in reading, separate from transportation and aesthetic reward.

Prose that protects flow: readable challenge, pacing that matches the scene's work, sentences that support rather than obstruct the reader's comprehension.

Prose that damages flow: over-elaboration, dense exposition at the wrong moment, uneven challenge, readability breaks for no reward, style choices that impede rather than reward attention.

### Critical insight
Readers want **all four channels at once.** A skill that optimizes only for withholding/inference damages aesthetic, transportation, and flow. Over-explaining breaks inference. Under-explaining breaks coherence. Generic style breaks aesthetic pleasure. Impenetrable style breaks flow. **Good prose is calibration across multiple reward channels, not a single "withhold more" rule.**

One more research finding that matters for the framing: **fiction is not special because it is untrue.** Hartung et al. 2017 (pubmed 28983269) — the same short story labeled "fictional" vs "factual" showed no meaningful difference in immersion, appreciation, or reading time. Fiction works because the reader adopts a *simulation stance*, not because the text disclaims factuality. This means you should not frame fiction as "the opposite of exposition." Frame it as "prose that invites and rewards a particular reader stance."

---

## Part 2: Good Fiction from First Principles (the craft lineage)

From the p40 research spawn. The earlier "fiction is controlled withholding" hypothesis is **partly right and too narrow**. Craft tradition across Hemingway, Forster, Wood, Baxter, Gardner, Le Guin, and Saunders converges on: fiction is a **designed mental experience**, not a data-delivery format. The common denominator is not "hide information" but "arrange experience so the reader has to do meaningful cognitive work."

Three recurring craft models:
- **Immersion / dream** — Gardner's "vivid and continuous dream." Matches the transportation channel.
- **Inference / subtext** — Hemingway's iceberg ("Death in the Afternoon" ch. 16, "may omit things that he knows"), Baxter's "The Art of Subtext," Wood's focalization and partial perspective in "How Fiction Works." Matches social simulation + withholding as a sub-mechanism.
- **Shared intelligence contract** — Saunders's "mutual assumption of intelligence," Forster's "the reader must sit down alone and struggle with the writer." The writer respects the reader as an active collaborator.

What the withholding frame misses:
- **Causal structure** (Forster's "what happens next and why") — fiction needs organized progression, not just gaps.
- **Truthful selection** (Le Guin) — minimalism is not the goal; fit, relation, and truthfulness are.
- **Pattern and rhythm** at sentence, scene, and structural levels — aesthetic reward lives here.
- **People, not mechanisms** (Le Guin's carrier-bag theory) — fiction is a container of relations, not a conflict engine.

"Show don't tell" is a rough shorthand for how to protect social simulation and aesthetic channels — it is not a law. Good fiction still needs orientation, pacing, causal clarity, and sometimes explicit statement. The cargo-cult version ("never tell, never explain") breaks transportation and flow. The real version is: *transmit experience through concrete action and context when you can, because the reader reconstructing feeling is the reward, but don't impede coherence or flow in service of that.*

If you want one craft formulation that sits closest to the cross-tradition consensus, it is Gardner's "vivid and continuous dream," with Hemingway, Baxter, and Wood explaining the mechanisms underneath it.

---

## Part 3: Documented AI Writing Failure Modes (the diagnosis frame)

From the p42 research spawn. The earlier "RLHF helpfulness breaks fiction" hypothesis is supported in a narrower form: **alignment training and chat-template formatting measurably reduce surface diversity and increase determinism in creative generation.** It does NOT support a universal claim that RLHF makes fiction worse in every way — diversity and quality are separable, and preference-tuned models can have greater effective semantic diversity even with lower lexical variety (arxiv 2504.12522).

The honest framing is: **alignment changes the tradeoff surface, and naive reward optimization is a poor proxy for literary quality.**

Documented failure modes an agent should be aware of:

1. **Syntactic templating** — models reach for the same sentence structures repeatedly. Templates are copied directly from pretraining data. Fine-tuning and alignment do NOT overwrite them. Source: "Detection and Measurement of Syntactic Templates in Generated Text," Shaib et al. 2024 EMNLP, aclanthology.org/2024.emnlp-main.368. Damages the aesthetic channel.

2. **Lower uncertainty than human writers** — instruction-tuned and reasoning models have lower token-level uncertainty than base models and than human professional writers, with the gap larger in creative writing than in functional domains. Source: arxiv 2602.16162 (2026 preprint). Damages aesthetic + social simulation (characters feel flattened when every sentence picks the expected word).

3. **Chat-template diversity collapse** — chat templates THEMSELVES suppress topical and semantic diversity on creative tasks, independent of content. Explicitly telling the model "be creative" does NOT close the gap. Source: "The Price of Format: Diversity Collapse in LLMs," 2025 Findings EMNLP, aclanthology.org/2025.findings-emnlp.836. Damages aesthetic channel. Not fully fixable from the prompt side; mitigate with looser prompt shapes.

4. **Attractor-state fluency** — RLHF-aligned models show lower token entropy and form attractor states. Prose feels "smoothed" rather than "written." Source: "Creativity Has Left the Chat," arxiv 2406.05587. Damages aesthetic channel.

5. **Middle-drift consistency bugs** — in long-form narratives, factual and temporal consistency errors cluster in the MIDDLE of narratives, not openings or endings. Source: "Lost in Stories," arxiv 2603.05890. Damages transportation channel.

6. **Weak suspense generation** — LLMs are unreliable for suspenseful story generation; iterative planning improves it. Source: "Creating Suspenseful Stories," 2024 EACL, aclanthology.org/2024.eacl-long.147. Maps to the withholding dimension that good suspense requires.

7. **The generalized helpfulness failure** — the model is trained to be helpful (explain clearly, deliver complete information, resolve ambiguity, correct misunderstanding). Fiction is anti-helpful at precise moments: subtext should not be stated, foreshadowing should not connect immediately to its payoff, unreliable narrators should not be corrected, dramatic irony requires withholding, mysteries require telegraphing the solution only at the right moment. This is the generalized diagnosis behind most AI prose failures — labeled emotions, collapsed ambiguity, tied-off endings, explained subtext, over-dramatized worldbuilding. Resist the urge to help when the reader wants to work for it.

### Empirical backing for the multi-agent architecture
HoLLMwood (2024 Findings EMNLP, aclanthology.org/2024.findings-emnlp.474) found that role decomposition into writer / editor / actor roles improves screenwriting over strong single-agent baselines in coherence, relevance, interestingness, and overall quality. This directly validates the writer / critic / reader-sim / orchestrator fan-out pattern in this repo.

---

## Part 4: Agent & Skill Design Principles

From the mined `__meridian-spawn/resources/agent-design-principles.md`. These govern how every agent and skill in this repo should be written.

**Agents vs skills.** An agent is an actor (runs, produces output, spawned expensive and independent). A skill is knowledge (loaded into an agent's context, composable, cheap). Wrong direction is costly both ways. A skill should have multiple consumers — if only one agent loads it, the knowledge belongs in that agent's body.

**No role identity.** Don't say "you are a senior editor" or "you are a literary critic." PRISM (arxiv 2603.18507) shows persona prompting activates instruction-following mechanisms that interfere with knowledge retrieval and reasoning on discriminative tasks. Every persona variant reduced accuracy. Describe behaviors directly instead. Not "you are a careful reviewer" but "focus on correctness — does the prose protect the four reward channels?"

**Explain WHY.** Every constraint includes reasoning. Claude generalizes from explanations; rules without reasons get followed literally and miss the point. Bad: "Never resolve ambiguity." Good: "Don't resolve ambiguity prematurely because the reader's cognitive work IS the reward in the social-simulation channel. When you explain what a character is feeling, you collapse the modeling the reader was doing — the prose becomes information, not experience."

**Right altitude.** Behavioral heuristics with reasoning. Too specific is brittle. Too vague assumes context the model doesn't have. The sweet spot is heuristics + why, trusting the model to apply the principle.

**Dial back aggressive language.** No ALL CAPS, no CRITICAL, no "you MUST," no "NEVER." Modern models overtrigger on aggressive language and apply rules rigidly where they don't fit. Use normal language: "resist the urge to explain" not "NEVER EXPLAIN."

**Description design.** Descriptions serve the consumer (caller deciding whether to use). Body serves the entity itself. Skill descriptions describe *when* to use (situations/contexts), not *how* (commands/syntax). Agent descriptions cover what-it-does, how-to-invoke (include `meridian spawn -a <name>`), what-context-it-needs, where-output-goes.

**Progressive disclosure.** Three loading levels: description (always in context, short, triggers loading) → SKILL.md body (loaded on trigger, digestible, few hundred lines max) → bundled resources (loaded on demand from body references with guidance on when to read them). Each level adds new info, never restates previous levels.

**Agent body: don't assume your caller.** No references to `--from`, `-f`, or "the draft-orchestrator spawns you with..." The agent can't distinguish context sources. Caller-agnostic agents are reusable.

**Don't prescribe sequences.** No "Step 1, Step 2, Step 3." Anthropic guidance: "think thoroughly" beats hand-written step plans. Describe inputs, outputs, quality bar, tools available, escalation triggers — let the model choose the sequence.

**Don't hardcode models.** Write "fan out across diverse strong models" and point at `meridian models list` / `/writing-staffing`. Rankings drift monthly.

**Prompt layout (priority order, not a template).** Open with what-the-agent-does and why-it-matters → behavioral constraints with reasoning → core workflow and quality bar → per-mode guidance (escalation, edge cases). Primacy/recency effects push constraints to the front.

**Tool restrictions.** `tools:` allowlist scopes Bash / enforces on OpenCode and Codex. `disallowed-tools:` denylist genuinely strips tools on Claude — use for hard boundaries like `[Agent]` on orchestrators that must route through `meridian spawn`.

---

## Part 5: Current State of the Repo

At `/Users/jimmyyao/gitrepos/creative-writing-skills/`:

**Meridian layer (top-level):**
- `agents/`: chronicler, continuity-checker, critic, draft-orchestrator, explorer, graph-maintainer, knowledge-orchestrator, outliner, researcher, role-player, session-miner, story-orchestrator, style-analyzer, wiki-editor, writer (15 agents)
- `skills/`: brainstorming, knowledge-graph, prose-analysis, prose-critique, prose-writing, story-architecture, story-context, story-decisions, wiki-docs, writing-artifacts, writing-principles, writing-staffing (12 skills)

**Plugin layer (`cw/`):**
- `cw/agents/`: mirrors the meridian agent roster with `cw-` prefixed filenames (15 agents)
- `cw/cw-brainstorming/`, `cw/cw-official-docs/`, `cw/cw-prose-writing/`, `cw/cw-router/`, `cw/cw-story-critique/`, `cw/cw-style-skill-creator/` (6 old-style skills, pre-meridian naming)

**Recent work already landed (do not redo):**
- writer.md has a "Known Failure Modes of Your Training" section
- prose-critique/resources/prose.md has "Documented AI Failure Modes to Hunt For"
- continuity-checker.md has "Where Errors Cluster"
- story-orchestrator.md has the four-channel reader reward framework in "Critic Synthesis"
- writing-staffing/resources/critics.md has the HoLLMwood note
- draft-orchestrator.md has prose reasoning instead of templated prompt examples

**Still open (this work item's scope):**
- `writing-principles` skill needs re-framing around the four reward channels as positive prescription (currently leads with "fighting your training" diagnosis only)
- `reader-sim` agent does not exist (new role — performs reading, reports experience per channel)
- `role-player` should rename to `character-sim` (symmetric with reader-sim, drops gaming connotation)
- `outliner` has a dual-mode body (outlining + brainstorming) that should split — `brainstormer` as its own agent
- Plugin layer has stale skill names and missing skill ports (`writing-principles` especially, since plugin agents rely on inlined content)
- `cw-router` should be retired as tier 2/3 default (orchestrator is better entry point; router stays for Claude.ai web UI)
