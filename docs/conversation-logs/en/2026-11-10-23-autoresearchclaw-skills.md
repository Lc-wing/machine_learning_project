# 23 Install AutoResearchClaw skills

- Date: 2026-11-10
- Status: Branch `cursor/autoresearchclaw-skills-ab75`, awaiting merge
- Chinese version: [中文](../zh/2026-11-10-23-autoresearchclaw-skills.md)

## Request

Install the skills from [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw).

## Outcome

Installed commit `be4ba475` (2026-08-19). Twenty-two skills are under `.cursor/skills/`. The license is `.cursor/LICENSE-AutoResearchClaw` (MIT).

- The 20 built-in skills from `researchclaw/skills/builtin/`: 8 experiment skills (literature search, hypothesis, experimental design, statistical reporting, scientific writing, visualization, systematic review, meta-analysis), 8 domain skills (biology, chemistry, quantum, reinforcement learning, vision classification and detection, pretraining, alignment), and 4 tooling skills (PyTorch training, data loading, mixed precision, distributed training).
- Two skills that exist only under `.claude/skills/`: `a-evolve` (improve an agent from failure records) and `researchclaw` (invoke the 23-stage autonomous research pipeline).

Checked: every `name` matches its folder, every description is at most 1024 characters, and the skills have no relative links outside their own folders.

The AutoResearchClaw Python package was not installed, and the pipeline was not run. The `researchclaw` skill tells the agent to execute generated experiment code, and it needs the user's own config and API key. Number 22 is left for the unmerged academic-research-skills record, so this one is 23.
