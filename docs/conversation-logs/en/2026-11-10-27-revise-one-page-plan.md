# 27 Apply the four proposed edits to the one-page plan

- Date: 2026-11-10
- Follows: [26](2026-11-10-26-plan-versus-pain-point.md)
- Question: Yes, you can make the changes.
- Chinese version: [中文](../zh/2026-11-10-27-revise-one-page-plan.md)

## Outcome

Edited `docs/research-plan/sketch-sufficiency.html` and re-exported the PDF in the same directory. The page count is still 1. The title, the last two research questions, the expected outcome, and the layout were left as they were.

1. The problem statement now says that raising the style-reward weight from 0.05 to 0.1 moves tokens only from 65.2 to 64.3, and that the reported parity uses short traces of 182–240 tokens rather than the thousand-token regime in the introduction. It also says this plan does not re-estimate that 64% reduction.
2. The solution now ends with a pilot before reinforcement learning: each omitted sentence is put back, and training continues only if the change in answer log probability predicts errors better than length. Otherwise the omission-negative target is revised first.
3. The first research question pre-specifies the subset of premises used by two later steps.
4. The solution now reports accuracy by quantile of baseline reasoning length, while the matched-length comparison remains.
