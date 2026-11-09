# 22 Install academic-research-skills

- Date: 2026-11-10
- Status: Branch `cursor/academic-research-skills-ab75`, awaiting merge
- Chinese version: [中文](../zh/2026-11-10-22-academic-research-skills.md)

## Request

Install [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills).

## Outcome

Installed v3.24.2 (commit `6d938867`, 2026-11-06) the way the project documents a project-level install. The five skills are under `.cursor/skills/`, which Cursor reads. `shared/` is at `.cursor/skills/shared/`, because the skill text links to it with the relative path `../shared/`. The full license is `.cursor/LICENSE-academic-research-skills`.

| Skill | Role |
|-------|------|
| `deep-research` | Literature search and review |
| `academic-paper` | Paper writing |
| `academic-paper-reviewer` | Review |
| `academic-pipeline` | Chains search, writing, review, and revision |
| `sr-screener` | Screening for a systematic review |

Checked: each `name` matches its folder, every description is at most 1024 characters, and `../shared/` from a skill directory resolves to `output_language_pair.md` and `handoff_schemas.md`.

The license is CC BY-NC 4.0, so use is non-commercial. The core skills are prompts. Optional Python, Pandoc, and PDF tools were not installed. Claude Code plugin commands and hooks do not run in Cursor.

Record 21 is updated: it was merged in PR #13.
