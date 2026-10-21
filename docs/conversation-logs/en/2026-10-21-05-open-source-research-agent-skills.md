# 05 Install skills from three open-source research repositories

- Date: 2026-10-21
- Status: [PR #2](https://github.com/Lc-wing/machine_learning_project/pull/2) awaiting merge (branch `cursor/research-agent-skills-ab75`)
- Chinese version: [中文](../zh/2026-10-21-05-open-source-research-agent-skills.md)

## Request

Install skills from these three sources:

1. The AI Scientist ([SakanaAI/AI-Scientist](https://github.com/SakanaAI/AI-Scientist)): an end-to-end research agent.
2. Nature-Skills ([Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills)): paper polishing, reviewer rebuttals, and publication-quality figures.
3. A prompt / skill aggregation library ([f/awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts) or awesome-cursorrules), said to contain many system instructions for PyTorch experiment design, hyperparameter tuning, and ablation study conventions.

## What the sources actually contain

| Source | Actual content | Action |
|--------|----------------|--------|
| nature-skills | A real skill repository: 23 skills, Apache-2.0 | Installed all 23 as-is |
| AI-Scientist | A full Python program, not a skill. Needs an NVIDIA GPU with CUDA, `texlive-full`, and LLM API keys; executes LLM-written code; its license requires disclosing AI-generated papers | Wrote a thin wrapper skill explaining how to deploy and run it |
| f/awesome-chatgpt-prompts (now `f/prompts.chat`) | 2,567 general-purpose prompts; only 8 mention PyTorch, hyperparameters, or ablations, and only in passing. Not skills | Nothing installed |
| PatrickJS/awesome-cursorrules | 257 Cursor rules (not skills); only 5 relate to machine learning, none cover ablation studies | Installed only the relevant hyperparameter optimization rule |

## What was installed

- **nature-skills**: installed with the official command `npx skills add Yuan1z0825/nature-skills --agent cursor --skill '*' --copy` into `.agents/skills/`, a project-level directory that Cursor reads.
  - All 23 skills are byte-identical to upstream commit `df6db0b`, and every folder name matches its `name` field.
  - Kept the installer's `skills-lock.json` so the skills can be updated with `npx skills update --project`; added the upstream license as `.agents/skills/LICENSE-nature-skills`.
  - About 41 MB, of which 34 MB are sample images bundled with `nature-figure`. Optional Python, R, and MCP dependencies of some skills were not installed.
- **ai-scientist**: added `.cursor/skills/ai-scientist/SKILL.md`, based entirely on the upstream README and `launch_scientist.py` (commit `1de1dbc`).
  - Before running, it checks for a GPU, Docker, `pdflatex`, and API keys, and stops to tell the user if anything is missing.
  - It states that runs must be containerized, warns about the cost of the default `--num-ideas` of 50, and spells out the license's AI-generated content disclosure requirement.
  - The AI-Scientist code itself was not added to this repository.
- **Hyperparameter optimization rule**: copied `automl-hyperparameter-optimization.mdc` unchanged into `.cursor/rules/`; it applies automatically when editing `.py`, `.ipynb`, and dependency files.
  - Rules not installed: the one labeled PyTorch is actually written for chemistry (RDKit, scaffold splits, plus a stray Tauri/Flask note); the LLM workflow rule is mostly about FastAPI; and both apply to every file.
