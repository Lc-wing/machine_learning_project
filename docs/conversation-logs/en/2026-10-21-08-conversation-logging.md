# 08 Store every conversation's results in the repository as Markdown

- Date: 2026-10-21
- Status: [PR #4](https://github.com/Lc-wing/machine_learning_project/pull/4) awaiting merge (branch `cursor/conversation-logs-ab75`); storage switched to Chinese and English versions in [09](2026-10-21-09-bilingual-logs.md)
- Chinese version: [中文](../zh/2026-10-21-08-conversation-logging.md)

## Request

Store the results of all conversations above and all future conversations in the repository as Markdown (on a new branch).

## Outcome

- Created branch `cursor/conversation-logs-ab75` with one record per conversation and an index page.
- Each record covers the request, the conclusion or outcome, the evidence, and any related PR or branch with its current status. Analysis questions (such as [07](2026-10-21-07-sketchthinker-r1-limitations.md)) are saved in full.
- Added the project rule `.cursor/rules/conversation-logs.mdc` (always applied): once merged into `main`, every agent working in this repository appends a record and updates the index after each conversation.
- Until the merge, results from later conversations in this session keep being committed to this branch.
- Opened [PR #4](https://github.com/Lc-wing/machine_learning_project/pull/4).

## Follow-up

In [09](2026-10-21-09-bilingual-logs.md), the records were split into a Chinese version (`zh/`) and an English version (`en/`).
