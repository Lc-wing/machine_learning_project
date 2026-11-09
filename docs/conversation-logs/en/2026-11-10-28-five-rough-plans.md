# 28 One-page English plans for the other five directions

- Date: 2026-11-10
- Follows: [10](2026-10-21-10-sketchthinker-future-directions.md), [24](2026-11-10-24-replace-direction-11.md), [27](2026-11-10-27-revise-one-page-plan.md)
- Question: Using the relevant research skills, write a full-English rough research plan, to the same requirements, for each of the other five directions.
- Chinese version: [中文](../zh/2026-11-10-28-five-rough-plans.md)

## Outcome

The five plans are paired HTML and PDF files in `docs/research-plan/`. Each exported PDF is one page. The sections match the revised sufficiency plan: a working title, a problem statement of one or two sentences, one paragraph of solution, two or three research questions, one sentence of expected outcome, plus a comparison table. Image-conditioned sufficiency is not repeated.

| File | Direction |
|------|-----------|
| `difficulty-boundary` | Where brevity starts to cost accuracy |
| `matched-source` | Whether any gain remains after the rewriter and the style reward are controlled |
| `twice-used-premise` | Whether a numbered list drops a visual premise used twice |
| `restore-probability` | Whether restoring a deleted sentence should leave the answer probability unchanged |
| `length-tail` | Whether a lower mean token count pushes errors into the right tail |

The Assumption Inverter supplies a falsifying outcome in each plan. The Gap & Contradiction Miner supplies the nearest existing work and why it cannot simply be attached. The difficulty plan does not use AdaptThink’s average-accuracy switch. The twice-used plan does not use a pruner whose job is to delete redundant reflections. The tail plan does not treat Sprint or Delve’s penalty as its contribution. The probability plan does not proceed to training if the pilot fails. The source-identification plan credits the style only if it beats both a length-preserving rewrite and a style reward of zero.
