# 03 Download the AI-Research-SKILLs library

- Date: 2026-10-21
- Status: Removed (see [04](2026-10-21-04-remove-installed-skills.md))
- Chinese version: [中文](../zh/2026-10-21-03-ai-research-skills-download.md)

## Request

Download AI-Research-SKILLs: a workflow for AI / CS master's and PhD students covering mainstream model architectures, fine-tuning strategy recommendations (LoRA and full-parameter), hyperparameter grid search, ablation study design, and Weights & Biases logging conventions.

## Outcome

- Confirmed it is a real open-source library, [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs) (MIT license), with 98 skills in 22 categories: model architecture, fine-tuning (Axolotl, LLaMA-Factory, PEFT, Unsloth), post-training, distributed training, evaluation, MLOps (including Weights & Biases), paper writing, research ideation, and more.
- The official installer had two problems:
  1. `install --all` skipped the 3 skills in category 22 (`compiler`, `research-manager`, `rigor-reviewer`).
  2. 48 skills had folder names that differ from the `name` field in their `SKILL.md`. Cursor's documentation requires the two to match, so those skills might not load.
- Wrote a sync script, `scripts/sync_ai_research_skills.py`, that pulls all 98 skills from upstream, names each folder after its `name` field, groups them by the original categories under `.cursor/skills/ai-research-skills/`, and includes the upstream license and source commit.
- Verified that all 98 folder names match their `name` fields, the content is byte-identical to the official installer's output, and re-running the script produces no changes.
- Pushed to branch `cursor/ai-research-skills-ab75` (no PR opened).

## Follow-up

Removed on request in [04](2026-10-21-04-remove-installed-skills.md); the branch was deleted locally and on GitHub.
