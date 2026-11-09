# 26 Whether the current one-page plan hits the paper's largest pain point

- Date: 2026-11-10
- Follows: [10](2026-10-21-10-sketchthinker-future-directions.md), [24](2026-11-10-24-replace-direction-11.md), [25](2026-11-10-25-judge-image-sufficiency.md)
- Plan compared: `docs/research-plan/sketch-sufficiency.html`, titled Preserving Visual Evidence in Compressed Multimodal Reasoning. Modifications are proposed only. The plan file was not edited.
- Chinese version: [中文](../zh/2026-11-10-26-plan-versus-pain-point.md)

## Conclusion

The current one-page plan targets a major problem: a compressed trace can state only correct steps and still omit a visual premise the answer needs. It does not hit the paper's largest pain point. That pain point is that the headline is not yet identified. In Table 5 the style-reward weight moves from 0.05 to 0.1 and tokens move only from 65.2 to 64.3, and the evidence stops at 182–240 tokens on average while the introduction describes traces of thousands of tokens.

The plan already has four reward arms, matched achieved length and training compute, answer-changing image pairs, and ablations that remove judge image access and omission negatives. Those target what the reward should be. All four arms share the same compressed cold-start data, so the plan cannot separate a GPT-5 rewrite from compression, and it cannot say where the paper's reported 64% came from.

## Proposed changes, not applied

1. Add the identification gap to the problem statement: the style reward barely causes shortening on its own, and the existing evidence is on short traces. State that this plan does not re-estimate the paper's 64%.
2. Before reinforcement learning, run a small pilot that puts omitted sentences back and tests whether the change in answer log probability predicts errors better than length. If it does not, the omission-negative training target needs to change.
3. Inside the first research question, pre-specify the subset where one visual fact is used by two later steps.
4. Besides matched length, report accuracy by quantile of baseline reasoning length, so the result is not collapsed into one mean.
