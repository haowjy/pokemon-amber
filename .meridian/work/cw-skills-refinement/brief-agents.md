# Task: Architectural agent changes (reader-sim, character-sim rename, brainstormer split)

Read `context.md` in this directory FIRST. It has the full research, principles, and repo state. This brief only covers your specific task.

Load both the `agent-creator` skill and the `skill-creator` skill before you start — you will be writing a new agent and touching cross-references in existing agents.

## Your scope

Three coordinated changes across both layers of the repo at `/Users/jimmyyao/gitrepos/creative-writing-skills/`:

1. Create a new `reader-sim` agent (meridian + plugin copies).
2. Rename `role-player` → `character-sim` in both layers, including every cross-reference.
3. Split `brainstormer` out of `outliner` in both layers, including cross-references in `story-orchestrator`.

Do NOT touch `skills/writing-principles/` — a different spawn is rewriting that.
Do NOT touch the plugin skill roster (`cw/cw-*` directories) or port skills to the plugin layer — a different spawn is handling that.
Do NOT edit files already updated in the recent tactical pass (writer.md failure modes, prose-critique/resources/prose.md, continuity-checker.md middle drift, story-orchestrator.md four-channel synthesis, writing-staffing/resources/critics.md HoLLMwood, draft-orchestrator.md prose reasoning) unless your cross-reference work genuinely requires a small additional edit.

## Change 1: Create `reader-sim` agent

### Why this agent exists

The current architecture has a `critic` that analyzes prose from outside and a `continuity-checker` that validates facts. No agent performs the actual experience of *being* a reader. The p41 research (see `context.md` part 1) shows reader enjoyment runs through four separable reward channels — transportation, aesthetic, social simulation, flow. A reader-sim agent performs first-person reading and reports experience per channel, producing data that complements critique but is not the same as critique.

The research also notes Hartung 2017: fiction is not special because it's untrue — it works because the reader adopts a simulation stance. A reader-sim agent IS the simulation stance, performed explicitly. HoLLMwood (2024 Findings EMNLP, aclanthology.org/2024.findings-emnlp.474) validates role-decomposition for creative tasks; adding reader-sim gives the writer/critic/reader/orchestrator split the research literature supports.

### Agent shape

- **Name:** `reader-sim` (meridian layer), `cw-reader-sim` (plugin layer copy).
- **What it does:** Reads a draft in character as a reader and reports experience as it happens. Produces an experiential report structured around the four reward channels, not a craft critique. It notices what absorbs it, where attention drifts, what confuses it, where emotion lands flat, where pacing feels right, where style rewards attention, where a sentence falls into a template that makes the reader skim, where the middle of a long piece drifts out of consistency with its opening.
- **What it does NOT do:** Diagnose craft problems, propose fixes, or write rewrites. That is the critic's job. The reader-sim reports experience; the orchestrator and critic do the translation from experience to craft findings.
- **Model:** Default to a strong model suited to subtle reading — but do NOT hardcode a specific model name per the principles in `context.md` part 4. Let the profile reference `/writing-staffing` or a general "strong model for subtle reading" heuristic.
- **Tools:** Read-only. `tools: [Read, Grep, Glob]`. No Write, no Edit, no Bash unless you have a specific justification. The output is the spawn report itself, not files.
- **Sandbox:** `read-only`.
- **Skills:** Load `writing-principles` (so it knows the four-channel frame) and nothing else unless necessary. The agent should not be dependent on a lot of context.
- **Description:** Must explain when to spawn it (when an orchestrator wants experiential reader-response data on a draft), how to invoke it (`meridian spawn -a reader-sim` plus what to pass), what context it needs (the draft file, optionally the prose-critique focus spec, optionally style references), and what its output looks like (an experiential report structured by reward channel).

### Agent body guidance

Follow the agent-design principles strictly. The body should:

- Describe what the agent does in behavioral terms, not as a persona ("focus on what you notice as you read" — not "you are a literary reader").
- Explain why the reader-sim role exists with reference to the composite reward frame. The agent should understand its own purpose, not just follow instructions.
- Tell the agent to read the draft in first-person present-tense as it happens: what pulls it in, what pushes it out, where it is confused, where it is moved, where it skims, where it stops and re-reads, where a sentence is beautiful and where a sentence is templated.
- Ask the agent to structure its report by reward channel: what in this draft helps or damages transportation, aesthetic pleasure, social simulation, and flow. Not all four need content in every report — if a channel was fine, say so briefly.
- Tell the agent to pay attention to middle passages of long drafts because empirical research (Lost in Stories, arxiv 2603.05890) documents that LLM consistency errors cluster in the middle; this is a direct cue for the reader-sim to notice where transportation breaks in long narratives.
- Explicitly instruct the agent NOT to propose craft fixes, rewrites, or prescriptive advice. Its value is raw experiential signal; translation to craft findings is the critic's and orchestrator's job.
- Do not prescribe a sequence. Do not number the steps. Describe inputs, output shape, quality bar.

### Plugin layer copy

Create `cw/agents/cw-reader-sim.md` as the plugin-layer mirror. It should match the meridian version's body closely but adapt for the plugin context:
- Use the `cw-` prefix in the name.
- Reference plugin-layer skills where the meridian version references meridian-layer skills, if the skill has a plugin counterpart yet. If `writing-principles` is not yet ported to the plugin, the plugin agent should inline the relevant four-channel context briefly (2–3 paragraphs) so it still functions without the skill, with a note that the skill will replace the inlined content when it's ported. Be honest about this in a comment.
- Reference `.meridian/fs/` for knowledge conventions (same as other plugin agents).
- Keep the read-only tool restriction identical.

## Change 2: Rename `role-player` → `character-sim`

### Why rename

`role-player` is informal and gaming-adjacent. `character-sim` is more technically precise, symmetric with the new `reader-sim`, and avoids the "role-playing" connotation that might pattern-match the model to game/escapism registers rather than craft-exploration registers.

### What to rename

**Meridian layer:**
- Rename `agents/role-player.md` → `agents/character-sim.md`.
- Update the `name:` frontmatter field inside the renamed file from `role-player` to `character-sim`.
- Update any internal references to the agent's old name inside the body of the renamed file.

**Plugin layer:**
- Rename `cw/agents/cw-role-player.md` → `cw/agents/cw-character-sim.md`.
- Update the `name:` field and internal references inside it.

**Cross-references across both layers:**
- Grep the whole repo (`/Users/jimmyyao/gitrepos/creative-writing-skills/`) for `role-player` and `role_player` and `cw-role-player`. Update every reference in agent bodies, skill bodies, skill resources, README, and any plugin marketplace config. Do not update git history or the rename-staged-files list in git status — only update file contents.
- The story-orchestrator and draft-orchestrator both reference role-player in fan-out guidance; update those references.

**Do not rename** the file if it appears in the git staging tree as a rename already (check `git status` — the prior session may have already started a rename). If a rename is already staged and you need to modify content, just modify content.

## Change 3: Split `brainstormer` out of `outliner`

### Why split

The current `outliner` agent has a dual-mode body — one section on outlining (structural decomposition, beat sheets, arc maps), and one section on brainstorming (open exploration, generating options, tagging with `<AI>`/`<rejected>`/`<hidden>`). These are different jobs:

- **Outlining:** go deep, build structure, commit to sequence, produce a beat sheet.
- **Brainstorming:** go wide, generate options, avoid commitment, produce exploratory material the user can accept or reject.

The current story-orchestrator spawns `outliner` in brainstorming mode with prompts like "brainstorm this angle," which reads as telling the outliner not to outline. Splitting makes the fan-out pattern cleaner and lets each agent be shaped around one job.

### What to create

**Meridian layer:**
- Create `agents/brainstormer.md` as a new agent. Its body should be the brainstorming half of the outliner's current body, revised to stand alone — no residual references to outlining. Describe what brainstorming produces (options, alternative angles, tagged exploratory material), what context it needs, and how it differs from outlining.
- Edit `agents/outliner.md` to remove the brainstorming mode section. Leave only the outlining responsibilities. The agent body should be tighter and cleaner as a result.

**Plugin layer:**
- Create `cw/agents/cw-brainstormer.md` as the plugin copy.
- Edit `cw/agents/cw-outliner.md` to match the meridian-layer change.

**Cross-references:**
- Update `agents/story-orchestrator.md` and `cw/agents/cw-story-orchestrator.md` so fan-out guidance refers to `brainstormer` when brainstorming is wanted and `outliner` when outlining is wanted. Preserve the existing four-channel critic synthesis content from the recent tactical edit — do not remove or restructure it.
- Update any skill references (`skills/writing-staffing/`, etc.) that mention outliner's dual mode. If a skill currently says "the outliner also brainstorms," fix it to "spawn the brainstormer for exploration, the outliner for structure."
- Update any `writing-principles` or `brainstorming` skill files that reference the old dual-mode agent.

### Agent body guidance for brainstormer

Follow the agent-design principles. The body should:

- Describe brainstorming as wide-open option generation, not deep-dive structural work.
- Explain why it is separate from outlining — the research (HoLLMwood and the diversity-collapse findings) supports role decomposition, and the two jobs have different quality bars.
- Describe what context it needs (the prompt or question to brainstorm around, any relevant story reference, style constraints if they apply).
- Describe its output shape: a set of options or angles tagged for the user's review, not a committed structural decision.
- Not prescribe a sequence. Not claim a persona. Not hardcode models.

## Quality bar for all three changes

- Agent bodies follow `context.md` part 4 strictly: no role identity, behavioral constraints with reasoning, no aggressive language, no prescribed sequences, no hardcoded models, caller-agnostic, progressive disclosure of knowledge through skill loading.
- Every new or modified description serves the caller: what the agent does, how to invoke, what context it needs, where output goes.
- Cross-references are consistent across the meridian and plugin layers. After your edits, `grep role-player` should return nothing; `grep brainstormer` should find the new agent plus its consumers; `grep reader-sim` should find the new agent plus its consumers.
- No new agent has more tools than it needs. Reader-sim is read-only. Brainstormer does not need Bash. Character-sim is unchanged from role-player's tool set.
- The README or top-level docs of creative-writing-skills may need small updates if they list the agent roster. Update if so; leave untouched if the README doesn't enumerate agents.

## What you must NOT do

- Do not touch `skills/writing-principles/` — a different spawn is rewriting it.
- Do not port skills to the plugin layer or rename plugin skill directories — a different spawn is doing that.
- Do not retire or re-home `cw-router` — a different spawn is doing that.
- Do not hardcode model names in any agent frontmatter or body.
- Do not use aggressive language in agent prompts.
- Do not introduce numbered step sequences.
- Do not invent citations. If you need to reference research, use the citations in `context.md`.

## Report

When done, write a report that includes:
- Full list of files created, renamed, modified (paths relative to creative-writing-skills repo).
- The new reader-sim and brainstormer agent frontmatter and the first few lines of each body so the reviewer can verify framing.
- The old → new rename mapping for role-player → character-sim with a list of every cross-reference you updated.
- Any judgment calls (e.g. tool set for reader-sim, whether to keep any brainstorming content in outliner, how you handled the plugin layer's inlined-content situation).
- Anything you noticed that should be follow-up work but was out of scope (cross-references you saw but didn't touch because they were owned by a different spawn, skill content that needs updating but is being handled elsewhere).
