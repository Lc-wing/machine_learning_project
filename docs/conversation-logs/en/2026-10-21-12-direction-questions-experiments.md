# 12 A research question and a validating experiment for every direction

- Date: 2026-10-21
- Follows: [10](2026-10-21-10-sketchthinker-future-directions.md), [11](2026-10-21-11-sketchthinker-existing-directions.md)
- Question: For every direction, what would be a potential research question? What kind of experiment could validate this idea?
- Chinese version: [中文](../zh/2026-10-21-12-direction-questions-experiments.md)

## How these were written

Each research question is falsifiable, as the Assumption Inverter requires. Each experiment separates "the idea is right" from a competing explanation, as the Gap & Contradiction Miner requires, instead of reporting one more aggregate score.

## First group: boundaries that are not yet tested

### Direction 1: Where brevity starts to hurt

- **Research question**: On a multimodal reasoner that writes thousands of tokens, does the accuracy gap against a long-reasoning baseline widen monotonically with problem difficulty?
- **Experiment**: Take a genuinely long multimodal reasoner and compare sketch-style reasoning with the long baseline on each of MathVision's five difficulty levels. Per level, report the accuracy gap, the token count, multiple seeds, and a confidence interval.
- **Validates the idea if**: the gap widens with difficulty. Unconditional shortening then does cost accuracy, and difficulty is the boundary.
- **Refutes it if**: the gap does not change with difficulty. That boundary is not there.

### Direction 2: Compression and judging must see the image

- **Research question**: Does deleting steps from the reasoning text alone disproportionately delete visual evidence, and does showing the image and the question to the compressor and the judge keep those steps on perception-heavy items?
- **Experiment**: Build counterfactual images that change exactly one visual fact the sketch omits. If the answer changes while the sketch text does not, that step was dropped visual evidence. Then compare three compressors: text only, image plus question, and steps kept only when they survive the intervention. Measure accuracy on these items, and the share of deleted steps that were visual evidence.
- **Validates the idea if**: the image-aware compressor drops fewer visual steps and scores higher.
- **Refutes it if**: the three arms match on accuracy and on what they delete. Not seeing the image was not the problem.

### Direction 3: Separate the source of the gain

- **Research question**: Once the rewriting source, the training steps, and the total token budget match, and the x-axis is end-to-end latency including image tokens, does the sketch style still beat a same-model rewrite that keeps the original length, and beat answering with no reasoning?
- **Experiment**: Four arms, same base model, same data, same decoding, multiple seeds. (1) The paper's method. (2) A GPT-5 rewrite that keeps the original length and style, then the same training. (3) RL with the style reward set to 0. (4) Direct answering. Report accuracy against latency.
- **Validates the idea if**: arm 1 still beats arms 2 and 3 along that curve. The gain then comes from the sketch style itself.
- **Refutes it if**: arm 1 does not beat arm 2 or arm 3. The "64% at no accuracy cost" then comes from distillation, budget, or the metric, not from the style.

## Second group: existing methods pointed at claims this paper did not establish

### Direction 4: Make length an input

- **Research question**: If target length is an input, does the length the model actually generates track that target, and is accuracy higher at the budget that matches the sketch model's average length?
- **Existing work**: budget forcing in s1, L1, and TokenSkip. This paper's L1 baseline has no cold start and does not report the target length.
- **Experiment**: Condition training on a target length and evaluate at budgets of 32, 64, 128, 256, and 512 tokens. Compare with the paper's sketch model, which has a single operating point, and with a long-reasoning baseline that is not conditioned on length. Record how far the actual length misses the target, and the accuracy at each budget.
- **Validates the idea if**: actual length moves with the target, and accuracy is higher near the sketch model's average length.
- **Refutes it if**: actual length ignores the target, or no budget beats the fixed style reward.

### Direction 5: Reward whether the step is right, not whether it looks like a sketch

- **Research question**: With the style reward set to 0 and only step correctness rewarded, does accuracy rise at a similar length, and does the share of high-reward wrong answers fall?
- **Existing work**: Lightman et al., Let's Verify Step by Step (ICLR 2024).
- **Experiment**: Two arms, same RL setup. (A) The paper's style reward. (B) A step-correctness reward only, style reward 0. Label steps with a checkable signal: a computable expression, a matched option, or a visual question that confirms a fact in the figure. Report final accuracy, length, and the rate of high reward with a wrong answer.
- **Validates the idea if**: arm B is more accurate at a similar length and has fewer high-reward wrong answers.
- **Refutes it if**: the arms match on accuracy and on that error rate. Replacing the style label did not change behavior.

### Direction 6: Move the reasoning into a continuous latent space

- **Research question**: At the same end-to-end latency, are continuous latent thoughts more accurate than a short text sketch, especially on items where the short text drops a premise the answer needs?
- **Existing work**: Coconut (Hao et al., 2024).
- **Experiment**: Three arms, same base model: the paper's sketch, Coconut-style continuous thoughts, and answering with no reasoning. Report accuracy against latency. Separately score the items whose correct answer depends on a premise the sketch omits, such as "D is the midpoint of BC".
- **Validates the idea if**: latent thoughts are more accurate at the same latency, and the margin is larger on those items.
- **Refutes it if**: latent accuracy is close to answering with no reasoning, so the hidden state is not carrying the dropped steps; or latent thoughts still lose to the sketch at the same latency.
