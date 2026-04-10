# Task: Re-frame writing-principles around the four reader reward channels

Read `context.md` in this directory FIRST. It contains the full research, principles, and repo state you need. This brief only covers your specific task.

Also load the `skill-creator` skill before you start — it has the authoring conventions for SKILL.md files.

## Your scope

Only touch the meridian-layer skill at `/Users/jimmyyao/gitrepos/creative-writing-skills/skills/writing-principles/`. Do not touch the plugin layer — a separate spawn is handling that. Do not touch any agent files.

## The problem

The current `writing-principles/SKILL.md` leads with "You Are Fighting Your Training" — the diagnosis frame. That frame is true and research-backed, but it is only HALF the story. It gives the model something to resist without giving it a positive target to aim at.

The p41 research (see `context.md`) shows that reader enjoyment is a composite of four separable reward channels. The p42 research shows AI writing failures are specific documented failure modes against those channels. Together they give the skill both a positive prescription (protect the four channels) and a diagnosis (here are the specific failure shapes your training produces against each channel).

The skill should be reorganized to lead with the positive prescription and position the diagnosis as "here is the specific shape your failures take against each reward channel."

## What you're producing

A rewritten `skills/writing-principles/SKILL.md`. You may also add or revise files under `skills/writing-principles/resources/` if the body gets long enough to need progressive disclosure — but prefer keeping the core teaching in the SKILL.md body and using resources only for specialized depth (e.g. per-failure-mode deep dives, citations list, canonical craft sources).

## Framing to use

The skill should teach, roughly in this order:

1. **Fiction is a composite reward experience.** Open with the positive frame: readers enjoy fiction through four separable but composable reward channels (transportation, aesthetic, social simulation, flow). Breaking any one damages enjoyment. Cite the research. Emphasize that protecting all four requires calibration, not a single rule.

2. **Fiction is not special because it is untrue.** Hartung 2017 finding. The reader adopts a simulation stance; the text invites it. This reframes fiction as "prose that invites and rewards a particular reader stance," not "prose that omits information." Important for preventing the cargo-cult "never tell anything" version of the skill.

3. **Your training has specific failure modes against each channel.** Here the "fighting your training" content lives, but organized BY which reward channel the failure damages. Syntactic templating → aesthetic damage. Attractor-state fluency → aesthetic damage. Labeled emotions and stock physical tells → social simulation damage. Middle-drift consistency bugs → transportation damage. Over-elaboration and dense exposition at the wrong moment → flow damage. The generalized "helpfulness instinct" applies across all four — it is the root cause; the specific failures are its surface expressions. Cite the documented research for each failure mode (see `context.md` part 3 for the full citation list).

4. **The craft tradition supports this.** Brief section (not the whole skill) grounding the composite-reward frame in craft lineage. Gardner's "vivid and continuous dream" (transportation), Hemingway's iceberg and Baxter's subtext (social simulation via inference), Wood's partial perspective (social simulation), Le Guin's truthful selection and carrier-bag theory (pattern, rhythm, relation), Saunders's and Forster's mutual intelligence contract (the reader as collaborator). This is not an authority flex — it is evidence that the frame is not a lab artifact; it matches what serious craft writers have independently converged on.

5. **Implications for how you draft.** Concrete guidance the writer can apply. Protect narrative coherence for transportation. Offer sentence-level variety and distinctive voice for aesthetic pleasure. Give character access through concrete behavior and interiority for social simulation. Provide readable challenge for flow. When you feel the urge to label an emotion, explain subtext, resolve ambiguity prematurely, or tie off an ending — notice which channel you would damage and calibrate. "Show don't tell" is the rough shorthand for the social-simulation + aesthetic calibration but it is not a law.

6. **This is opinionated about the diagnosis, less opinionated about the prescription.** The skill should say explicitly: the four-channel frame is the diagnosis and is research-backed. Specific writing disciplines (how much to show versus tell, how dense to make subtext, how much exposition to allow) are project choices that live in project-local style files. The skill gives opinions with pedigree; project style files override where needed. This preserves neutrality on stylistic questions where craft tradition disagrees with itself while keeping the skill's teeth where the evidence is strong.

## Quality bar

- Opens with a description that triggers loading when an agent is drafting or critiquing fiction. The description should reference the composite-reward frame so other agents know what this skill teaches.
- Body follows the agent-design principles in `context.md` part 4: no role identity, behavioral constraints with reasoning, no aggressive language, no prescribed sequences, no hardcoded models.
- Body stays digestible — prefer specific examples and cited failure modes over long prose. A few hundred lines is the ceiling; if you're pushing past that, push detail into `resources/`.
- Each level (description, body, resources) adds new information and does not restate previous levels.
- Every major claim that comes from research has a citation with a verifiable source path (arxiv ID, aclanthology URL, DOI). The citation list in `context.md` part 3 is your canonical reference; do not invent citations.
- Preserve existing content that still applies — don't redo work that's already research-grounded. Read the current SKILL.md and the current resources before rewriting so you understand what's there.
- If the skill's existing top section ("You Are Fighting Your Training" or equivalent) is still useful as a meta-framing, keep its insight but subordinate it to the four-channel frame. Don't delete it; reposition it.

## What you must NOT do

- Do not touch any file outside `skills/writing-principles/`.
- Do not hardcode models or model rankings.
- Do not prescribe numbered steps or sequences.
- Do not use ALL CAPS, "CRITICAL", "MUST", or "NEVER" in agent-facing instructions.
- Do not fabricate citations. Use only what is in `context.md` or what you can verify.
- Do not port anything to the plugin layer — that is a different spawn's job.

## Report

When done, write a report that includes:
- Files changed (paths relative to the creative-writing-skills repo).
- Structural summary of the new SKILL.md (section headers in order).
- Any judgment calls you made and why.
- Anything you noticed that should be follow-up work but was out of scope.
