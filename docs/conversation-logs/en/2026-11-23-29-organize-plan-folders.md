# 29 Split the one-page plans into one folder per direction

- Date: 2026-11-23
- Status: Merged in [PR #20](https://github.com/Lc-wing/machine_learning_project/pull/20)
- Chinese version: [中文](../zh/2026-11-23-29-organize-plan-folders.md)

## Request

Organize the repository so the files are easier to tell apart. Put the plans for different directions of the same task into different folders, and add a Markdown file in each folder that explains that direction.

## Outcome

The six one-page plans used to sit side by side in `docs/research-plan/`. Each direction now has its own folder, with the explanation in that folder’s `README.md`. The index is [docs/research-plan/README.md](../../research-plan/README.md).

| Folder | Direction |
|--------|-----------|
| `image-sufficiency` | Seeing the image. The original filenames `sketch-sufficiency.html` and PDF are kept, and the review notes moved into that folder’s `notes/` |
| `difficulty-boundary` | Where brevity starts to cost accuracy |
| `matched-source` | Whether any gain still belongs to the sketch style after the sources are matched |
| `twice-used-premise` | Whether a numbered list drops a visual premise used twice |
| `restore-probability` | Whether restoring a deleted sentence should leave the answer probability unchanged |
| `length-tail` | Whether a lower mean token count pushes errors into the right tail |

The formal proposal and the talk materials belong only to the sufficiency direction, so they stay in `docs/research-proposal/` and `docs/presentation/`. Links in the repository README, the conversation logs, and the review notes now point at the new paths.
