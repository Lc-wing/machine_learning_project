# One-page research plan: skill-based review and fixes

[中文版](../zh/2026-10-23-18-plan-skill-review.md)

- Date: 2026-10-23
- Status: branch [plan-skill-review](https://github.com/Lc-wing/machine_learning_project/tree/plan-skill-review), PR to main (builds on PR #9); not merged

## Request
Have Codex CLI re-review the one-page plan (docs/research-plan/sketch-sufficiency.html/.pdf) using the three installed research skill collections, fix real problems, keep it to one page, and update GitHub and Google Drive.

## Result
Codex used academic-research-suite (academic-research-skills-codex), scientific-critical-thinking (K-Dense-AI scientific-agent-skills), and brainstorming-research-ideas (Orchestra AI-Research-SKILLs). It found no critical issues, two major and four moderate ones:
1. The gap overstated things: Appendix H (Tables 13–14) already checks key-step preservation in cold-start data. The problem statement now places the gap in training-time rewards for grounded visual premises.
2. The reward intervention was ambiguous. Now only the style reward is replaced; accuracy/format rewards (Eq. 5: 0.5/0.4/0.1) stay fixed, with shared data, initialization and policy compute.
3. Judge split and negative examples added (split by problem; premise-deleted/contradicted traces; held-out human labels).
4. RQ1 now matches the annotations (visual premises vs nonvisual deductions).
5. RQ3 replaced: correctness on both images of a pair, plus an image-blind judge ablation.
6. Named the Qwen2.5-VL-7B-Instruct backbone; difficulty groups are set before training.

Full review: docs/research-plan/notes/skill-review.md.

## Verification
PDF rebuilt with headless Chrome; pdfinfo Pages: 1; render checked visually; all five sections present; numbers checked against the paper text.
