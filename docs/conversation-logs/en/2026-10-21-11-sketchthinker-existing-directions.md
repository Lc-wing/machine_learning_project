# 11 Three more directions, prior work allowed

- Date: 2026-10-21
- Follows: [07](2026-10-21-07-sketchthinker-r1-limitations.md), [10](2026-10-21-10-sketchthinker-future-directions.md)
- Question: Give three more directions. They may already have been done.
- Chinese version: [中文](../zh/2026-10-21-11-sketchthinker-existing-directions.md)

## Conclusion

Unlike record 10, these three do not aim at an empty niche. Each takes an existing method and points it at a claim this paper did not establish.

1. **Make length an input**: budget forcing from s1, L1, and TokenSkip.
2. **Reward step correctness instead of style**: process reward models, as in Let's Verify Step by Step.
3. **Stop deleting the justification; move the reasoning into a continuous latent space**: Coconut.

## Direction 1: Length as an input, not a fixed reward

**Existing work**: s1 (EMNLP 2025) truncates or extends thinking to a chosen budget at inference time. L1 uses the gap from a target length as an RL reward, and this paper already includes it as a baseline. TokenSkip (EMNLP 2025) drops tokens by estimated semantic importance and exposes the length as a control.

**Limitation it addresses**: the style reward weight is fixed, and the claim that hard questions still get long traces has no evidence. Efficiency, defined as accuracy divided by token count, collapses the whole tradeoff into one number. The paper's own L1 baseline has no cold start and does not report the target length, so this line of work was not actually tested fairly here.

**What to do**: condition training on a target length, and report accuracy at several budgets instead of a single efficiency ratio. The budget can be a coarse difficulty estimate or a user choice.

## Direction 2: Reward whether each step is right, not whether it looks like a sketch

**Existing work**: Lightman et al., Let's Verify Step by Step (ICLR 2024), train a process reward model to score each reasoning step rather than only the final answer.

**Limitation it addresses**: SketchJudge is trained with the label "numbered list = 1, long trace = 0", sees neither the question nor the image, and the authors themselves observe reward hacking at high style weight. A process reward moves the supervision from format to step correctness, so the model can no longer win by merely looking like a sketch.

**What to do**: label each numbered step with a checkable signal (a computable expression, a matched option, or a visual question that confirms a fact in the figure). Add only that reward during RL and set the style reward to 0, so "being short" and "being right step by step" can be separated.

## Direction 3: Think in a continuous latent space instead of deleting the justification

**Existing work**: Coconut (Hao et al., 2024) treats the last hidden state as a continuous thought and stops writing every step out as text. This paper's related work lists that family as "output-based efficient reasoning" and does not compare against it.

**Limitation it addresses**: sketches get short by dropping checkable justifications (in a cold-start example, "OD = 1/2 AC" omits "D is the midpoint of BC"). Latent thoughts reduce visible tokens rather than the steps themselves, so they do not need a format-only judge and they do not need a GPT-5 rewrite.

**What to do**: on the same base model, compare accuracy and end-to-end latency for three arms: the paper's sketch, Coconut-style continuous thoughts, and answering with no reasoning. If continuous thoughts are more accurate at the same latency, then "the reasoning has to be written out as short text" is not what produces the gain.
