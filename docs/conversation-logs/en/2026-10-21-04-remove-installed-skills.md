# 04 Remove every skill installed or downloaded so far

- Date: 2026-10-21
- Status: Done
- Chinese version: [中文](../zh/2026-10-21-04-remove-installed-skills.md)

## Request

Delete all skills installed or downloaded in the conversations above.

## Outcome

The `main` branch was never modified. After the removal, a search of the whole machine found no remaining related `SKILL.md` files.

| Item | Action |
|------|--------|
| 98 AI-Research-SKILLs skills and the sync script (branch `cursor/ai-research-skills-ab75`, no PR) | Deleted the branch locally and on GitHub |
| The two self-written research skills (branch of [PR #1](https://github.com/Lc-wing/machine_learning_project/pull/1)) | Committed their removal so the branch has no diff against `main`; did not delete the branch, to avoid auto-closing the PR |
| Temporary files on the cloud machine | Deleted the cloned upstream repositories, the installer's `~/.orchestra` working directory, the npx cache, and temporary verification files |

PR #1 was retitled `[Removed] ...` with an updated description, and the repository owner then closed it.
