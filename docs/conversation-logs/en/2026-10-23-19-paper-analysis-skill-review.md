# Paper analysis, skill review, and research direction selection

[中文版](../zh/2026-10-23-19-paper-analysis-skill-review.md)

Date: 2026-10-23. Status: PR pending on branch [analysis-skill-review](https://github.com/Lc-wing/machine_learning_project/tree/analysis-skill-review). No commit made.

## Request

Produce a fresh skill-based analysis of SketchThinker-R1, answering the three prompts: methodological limitations, three research directions, and research questions with validating experiments for all three. Rewrite the one-page plan around the chosen direction and keep analysis deliverables in `docs/paper-analysis/`. For this editorial pass, remove defensive disclaimers, shorten the English by about 40% and probing by about half, fully translate the final English into Chinese, lightly revise the skill review, and update bilingual conversation indexes. Preserve verified numbers/references and leave `docs/research-proposal/` and `docs/presentation/` untouched; do not commit.

## Result and evidence

**Direction 1, preserving explicit visual support, remains the chosen plan direction.** The [English analysis](../../paper-analysis/sketchthinker-analysis.md) now has 1,768 words versus 3,058, a 42.2% reduction. Probing fell from 1,742 to 936 words, a 46.3% reduction. The [Chinese analysis](../../paper-analysis/sketchthinker-analysis.zh.md) is a complete translation of the final English, including every table, direction, protocol, success criterion, and compute budget.

The fresh assessment identifies five connected gaps: style reward validity, incremental attribution, subgroup accuracy/allocation, transfer across reasoning regimes, and full-cost accounting. Its source is the supplied [paper text](../../presentation/paper/2601.02825.txt); publication links are the [ICLR proceedings](https://proceedings.iclr.cc/paper_files/paper/2026/hash/a1f0c0cd6caaa4863af5f12608edf63e-Abstract-Conference.html) and [arXiv](https://arxiv.org/abs/2601.02825).

The analysis retains the paper's existing controls and assessments: stage/judge ablations in Table 3, long-trace initialization in Table 8, reward schedules in Table 7, scaling in Tables 9–10, interpretability in Appendix G, preservation in Appendix H, and timing in Appendix J. Table 1's 7B token reductions are 64.71%, 70.38%, 76.54%, and 66.55% on MMMU, MathVision, VisuLogic, and PhyX. Table 2's 3B MathVision accuracy falls from 26.9 to 25.3. Table 14 counts 19,182 sketches preserving key steps and 818 missing them. These findings motivate targeted controls and evaluation of trained-policy explanations.

## Skills and corrections

The [skill review](../../paper-analysis/notes/skill-review.md) records the original nine research skills: academic-research-suite, scientific-critical-thinking, peer-review, hypothesis-generation, experimental-design, scientific-brainstorming, statistical-power, brainstorming-research-ideas, and creative-thinking-for-research. They supplied evidence appraisal, rival hypotheses, candidate comparison, controlled designs, and precision planning. The present editorial pass used nature-polishing, with using-superpowers for skill discovery and verification-before-completion for final checks.

Earlier answers overstated missing ablations, inferred judge shortcuts and teacher corrections, guessed evaluation splits, and treated image interventions or controlled wins as unique causal explanations. The revision ties concerns to exact source locations, retains existing assessments, adds matched controls and content audits, and defines useful-effect thresholds with uncertainty. Light editing preserves the review's skill attribution, issue table, numerical audit, and plan rationale while removing repeated defensive wording.

## Three directions and their probing experiments

All sizes, thresholds, and caps below are proposed design choices. Shared rules separate template families before generation, freeze evaluation settings, retain wrong answers in trace scoring, and use three seeds with paired 95% problem-family intervals and separate seed-effect reporting. Pilots assess precision and throughput.

1. **Explicit visual-support preservation.** Ask whether omission-sensitive supervision improves accuracy and explanation sufficiency at matched length/compute. Render 3,000 geometry/bar-chart problems, split 1,600/400/1,000, with independent human audits on 300 test problems. Compare sufficiency, style, stated-step correctness, and zero auxiliary rewards from shared cold-start weights. Match achieved lengths; test premise deletions, alternative proofs, image-changing/nuisance pairs, and separate image-access/omission-negative ablations. Near 128 tokens, require gains of 3 accuracy points and 5 sufficiency points, both paired intervals above zero. Cap compute at 400 accelerator-hours, including rollouts and judge inference.
2. **Subgroup-constrained allocation.** Ask whether an image/question router saves tokens while keeping every prespecified group's accuracy loss within 2 points. Use the rendered split and MathVision transfer; cache frozen-policy budget curves from 64 to 2,048 tokens. Compare fixed budgets, direct answers, prompt control, fast/slow routing, and average-accuracy routing; ablate group constraints/visual features and shuffle assignments. Require 20% mean savings, simultaneous group lower bounds above −2 points, and lower worst-group loss at matched cost. Cap compute at 80 accelerator-hours.
3. **Factorial attribution and break-even.** Ask what style reward adds after each cold-start construction and when its inference savings repay preparation. Cross original long, length-preserving rewrite, and sketch traces with style present/absent, producing six cells with three seeds each. Audit content; test held-out rendered families and MathVision; compare default, direct-answer, and length-reward baselines. Measure interactions, accuracy, latency, and lifecycle costs across visual loads/batching. Require 10% lower end-to-end latency with the paired accuracy interval above −2 points; calculate break-even separately. Cap compute at 500 accelerator-hours.

## One-page plan and deliverables

The existing rewritten [one-page plan](../../research-plan/sketch-sufficiency.html), *Preserving Visual Evidence in Compressed Multimodal Reasoning*, follows Direction 1. It frames the missing-premise problem, compares four rewards on 3,000 problems, accepts alternative derivations, and includes independent human evaluation, matched compute/length, ablations, three seeds, and a pilot. This editorial pass preserves that HTML and its PDF; the analysis remains aligned with it.

Direction 1 was chosen because it directly tests the reward's target with observable omission labels and can begin with inexpensive judge diagnostics. Direction 2 overlaps adaptive allocation and needs precise group-level estimates. Direction 3 provides valuable attribution but has a larger factorial workload. The analysis folder contains the final English, full Chinese translation, and skill-review note. Both language indexes receive record 19. The root README has no documentation-folder index, so its conditional update does not apply.

## Validation and current state

Checked word counts, bilingual numbers and section/table references, table arithmetic, local links, required protocol elements, and whitespace. Hash checks confirm that presentation, formal proposal, and existing research-plan files retain their pre-edit contents. Existing working-tree changes to the plan and PDF and the untracked skill cache were preserved. Status remains PR pending on `analysis-skill-review`; no experiments or commits were made during this editorial pass.
