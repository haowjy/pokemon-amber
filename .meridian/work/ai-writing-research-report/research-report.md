# Research Report: Failure Modes of AI Writing and What Actually Helps

## What I did

- Read the research brief in `/private/tmp/ai-writing-research.md`.
- Searched primary sources in arXiv and ACL Anthology for:
  - documented failure modes in LLM story/creative writing,
  - evidence for or against the RLHF-vs-creativity hypothesis,
  - techniques that improve creative output with measured results.
- Prioritized primary research and venue pages over blog summaries or secondary reviews.

## Key decisions

- I treated the RLHF hypothesis skeptically and separated three different effects:
  - lexical/syntactic diversity,
  - semantic diversity,
  - writing quality or preference win rate.
- I did not collapse those into one claim, because the literature shows they can move in different directions.
- I treated preprints as preprints. Where evidence came from arXiv only, I marked it implicitly by source type and did not present it as settled consensus.

## Findings

### 1) Documented failure modes

- Early story-generation work found that large pretrained models still produce repetitive and under-diverse text under likelihood-maximizing decoding, even when they improve context conditioning and event ordering. Source: [Do Massively Pretrained Language Models Make Better Storytellers?](https://aclanthology.org/K19-1079/)
- More recent analysis of generated text found that models rely on syntactic templates at a much higher rate than human text, and that most templates seen in model output are copied from pretraining data. The paper also reports that these templates are not overwritten by fine-tuning or alignment, including RLHF. Source: [Detection and Measurement of Syntactic Templates in Generated Text](https://aclanthology.org/2024.emnlp-main.368/)
- Story-generation studies still report weak suspense generation. One EACL paper states that current LLMs are unreliable for suspenseful story generation, and that iterative planning helps. Source: [Creating Suspenseful Stories: Iterative Planning with Large Language Models](https://aclanthology.org/2024.eacl-long.147/)
- Long-form narrative work in 2026 reports consistency bugs in factual and temporal dimensions, with errors clustering in the middle of narratives. Source: [Lost in Stories: Consistency Bugs in Long Story Generation by LLMs](https://arxiv.org/abs/2603.05890)
- A 2023 INLG study found that LLM story generation can compete with human authors, but also that models may replicate real stories when world knowledge is involved, which the authors describe as resembling plagiarism. Source: [The Next Chapter: A Study of Large Language Models in Storytelling](https://aclanthology.org/2023.inlg-main.23/)

### 2) Evidence on the RLHF / alignment hypothesis

The evidence is mixed, but the hypothesis is not crazy.

- Meta’s Llama 2 report includes an explicit figure showing that RLHF reduces diversity on factual prompts, while retaining more diversity on creative prompts. Source: [Llama 2: Open Foundation and Fine-Tuned Chat Models](https://llama-2.ai/wp-content/uploads/2023/08/Llama-2-Open-Foundation-and-Fine-Tuned-Chat-Models.pdf)
- A 2024 preprint argues that RLHF-aligned Llama-2 models show lower token entropy, form attractor states, and exhibit reduced output diversity. Source: [Creativity Has Left the Chat: The Price of Debiasing Language Models](https://arxiv.org/abs/2406.05587)
- A 2025 paper on narrative generation finds that instruction tuning reduces diversity, with DPO having the strongest effect in its OLMo experiments. It also reports that a base model can be used to guide an instruct model back toward more diversity. Source: [Mind the Gap: Conformative Decoding to Improve Output Diversity of Instruction-Tuned Large Language Models](https://arxiv.org/abs/2507.20956)
- A 2025 Findings EMNLP paper found that full chat templates significantly reduce semantic and topical diversity on creative tasks, including WritingPrompts, compared to simple structure-free prompts. It also found that explicitly asking the model to "be creative" did not close the gap. Source: [The Price of Format: Diversity Collapse in LLMs](https://aclanthology.org/2025.findings-emnlp.836.pdf)
- A 2026 preprint directly frames uncertainty as a key limitation in creative writing and reports that instruction-tuned and reasoning models have lower uncertainty than base models, with the gap larger in creative writing than in functional domains. Source: [LLMs Exhibit Significantly Lower Uncertainty in Creative Writing Than Professional Writers](https://arxiv.org/abs/2602.16162)

The main counterweight:

- A 2025 preprint argues that preference-tuned models often have lower lexical and syntactic diversity, but greater effective semantic diversity than SFT or base models because they generate more high-quality outputs overall. That means "alignment hurts creativity" is too blunt if creativity is measured by semantic utility rather than form. Source: [Evaluating the Diversity and Quality of LLM Generated Content](https://arxiv.org/abs/2504.12522)

Bottom line: the field does support the narrower claim that alignment and instruction formatting can reduce surface diversity and increase determinism. It does not yet support a universal claim that RLHF makes fiction worse in every meaningful sense.

### 3) Approaches that show measurable improvement

- Iterative planning for suspenseful stories improved human evaluations in a zero-shot setup without supervised story corpora. Source: [Creating Suspenseful Stories: Iterative Planning with Large Language Models](https://aclanthology.org/2024.eacl-long.147/)
- Role decomposition and role-playing improved screenwriting quality. HoLLMwood assigns LLMs as writer, editor, and actor, and reports gains over strong baselines in coherence, relevance, interestingness, and overall quality. Source: [HoLLMwood: Unleashing the Creativity of Large Language Models in Screenwriting via Role Playing](https://aclanthology.org/2024.findings-emnlp.474/)
- Multi-modal imagination helped. A 2025 ACL Findings paper says image-guided imagination plus a multi-writer module significantly improved several creativity dimensions in story generation. Source: [A Character-Centric Creative Story Generation via Imagination](https://aclanthology.org/2025.findings-acl.82/)
- Fine-tuning on fiction is viable. A 2024 INLG challenge report describes supervised fine-tuning on public-domain books for fictional text generation and evaluates it with automatic and human assessments. Source: [A Report on LSG 2024: LLM Fine-Tuning for Fictional Stories Generation](https://aclanthology.org/2024.inlg-genchal.14/)
- Diversity-aware training can help. DivPO reports 74.6% more story diversity while maintaining similar win rates to baselines. Source: [Diverse Preference Optimization](https://arxiv.org/abs/2501.18101)
- Diversity-aware decoding can help too. Conformative decoding uses a base model to guide an instruct model and typically increases diversity while maintaining or improving quality. Source: [Mind the Gap: Conformative Decoding to Improve Output Diversity of Instruction-Tuned Large Language Models](https://arxiv.org/abs/2507.20956)
- AI feedback can help creative generation when carefully engineered. A 2025 EMNLP paper on creative greetings reports that RL-based approaches improve creative output over baselines, and an LLM-as-a-Judge reward strategy performs best and uses less human annotation. Source: [Igniting Creative Writing in Small Language Models: LLM-as-a-Judge versus Multi-Agent Refined Rewards](https://aclanthology.org/2025.emnlp-main.868.pdf)

### 4) What does not look solved

- Evaluation is still fragmented. A 2025 ACL Findings paper says creativity evaluation remains hard because existing methods either require costly annotations or do not match human judgments well. Source: [Automated Creativity Evaluation for Large Language Models: A Reference-Based Approach](https://aclanthology.org/2025.findings-emnlp.1171/)
- A 2026 survey of 57 story-generation papers says narrative coherence, character consistency, storyline diversity, and plot controllability are still challenging. Source: [Text-to-Text Automatic Story Generation: A Survey](https://aclanthology.org/2026.eacl-srw.39/)
- Writing feedback models are not yet reliable enough to be trusted blindly. A 2025 ACL paper says current models are often specific and mostly accurate, but still fail to identify the biggest writing issue and struggle to decide when criticism is appropriate. Source: [Help Me Write a Story: Evaluating LLMs' Ability to Generate Writing Feedback](https://aclanthology.org/2025.acl-long.1254/)

## Implications for a creative-writing toolkit

- Default to structure-free or minimally structured prompts when the goal is expressive variation.
- Treat "quality" and "diversity" as separate controls. The literature shows they are not the same objective.
- Add explicit planning and revision passes for suspense, coherence, and character depth instead of relying on a single generation pass.
- Provide diversity-preserving decoding or reranking modes for fiction work.
- Be cautious about hard-coding chat templates for creative tasks; multiple papers show that template structure itself can suppress variation.
- If using critique or feedback loops, validate the critic. Model-generated feedback can miss the main problem even when it sounds competent.

## State of the field

The field is active but not mature. There is no single agreed benchmark for "good fiction," and the literature mixes story generation, screenwriting, greetings, poetry, persona writing, and synthetic preference tasks. The most consistent result is that alignment and instruction formatting often narrow surface form and can reduce creativity-adjacent diversity, but the same systems can still improve quality, consistency, and human preference scores. The strongest current conclusion is not "RLHF kills fiction," but "alignment changes the tradeoff surface, and naive reward optimization is a poor proxy for literary quality."

## Verification notes

- I only used primary sources or venue pages for factual claims.
- I avoided blog summaries and secondary paper reviews.
- When a source was only available as an arXiv preprint, I treated it as provisional evidence rather than settled consensus.

## Source list

- [Do Massively Pretrained Language Models Make Better Storytellers?](https://aclanthology.org/K19-1079/)
- [The Next Chapter: A Study of Large Language Models in Storytelling](https://aclanthology.org/2023.inlg-main.23/)
- [Detection and Measurement of Syntactic Templates in Generated Text](https://aclanthology.org/2024.emnlp-main.368/)
- [Creating Suspenseful Stories: Iterative Planning with Large Language Models](https://aclanthology.org/2024.eacl-long.147/)
- [HoLLMwood: Unleashing the Creativity of Large Language Models in Screenwriting via Role Playing](https://aclanthology.org/2024.findings-emnlp.474/)
- [Creativity Has Left the Chat: The Price of Debiasing Language Models](https://arxiv.org/abs/2406.05587)
- [Small Language Models can Outperform Humans in Short Creative Writing: A Study Comparing SLMs with Humans and LLMs](https://arxiv.org/abs/2409.11547)
- [Diverse Preference Optimization](https://arxiv.org/abs/2501.18101)
- [Evaluating the Diversity and Quality of LLM Generated Content](https://arxiv.org/abs/2504.12522)
- [Mind the Gap: Conformative Decoding to Improve Output Diversity of Instruction-Tuned Large Language Models](https://arxiv.org/abs/2507.20956)
- [Automated Creativity Evaluation for Large Language Models: A Reference-Based Approach](https://aclanthology.org/2025.findings-emnlp.1171/)
- [Help Me Write a Story: Evaluating LLMs' Ability to Generate Writing Feedback](https://aclanthology.org/2025.acl-long.1254/)
- [A Character-Centric Creative Story Generation via Imagination](https://aclanthology.org/2025.findings-acl.82/)
- [Text-to-Text Automatic Story Generation: A Survey](https://aclanthology.org/2026.eacl-srw.39/)
- [LLMs Exhibit Significantly Lower Uncertainty in Creative Writing Than Professional Writers](https://arxiv.org/abs/2602.16162)
- [Lost in Stories: Consistency Bugs in Long Story Generation by LLMs](https://arxiv.org/abs/2603.05890)
