# 25 The six research questions, and whether image-conditioned sufficiency should be the plan

- Date: 2026-11-10
- Follows: [10](2026-10-21-10-sketchthinker-future-directions.md), [14](2026-10-21-14-research-plan.md), [24](2026-11-10-24-replace-direction-11.md)
- Question: Analyze every research question in the six directions, then judge whether choosing image-conditioned sufficiency as the concrete plan is appropriate and whether it hits the paper's most central problem.
- Chinese version: [中文](../zh/2026-11-10-25-judge-image-sufficiency.md)

The six directions are the three in record 10 plus the three in record 24 that replaced record 11. Record 11's existing methods are not part of these six.

## Conclusion

Image-conditioned sufficiency is a sound choice for the compression criterion to learn next. It hits the fact that the sketch judge treats format as sufficiency.

The paper's headline is that sketch style cuts reasoning tokens by 64% with no loss in accuracy. That sentence depends on two prior facts. First, in Table 5 the style-reward weight moves from 0.05 to 0.1 and tokens move only from 65.2 to 64.3; the shortening happens in the RL stage, and the reward itself is barely isolated. Second, the evidence stops at short traces of 182–240 tokens on average, while the introduction is about traces of thousands of tokens. Those two facts are directions 3 and 1. Sufficiency answers what the reward should be. It does not answer whether the shortening and the accuracy in the paper were produced by the sketch reward.

The one-page plan already includes a difficulty threshold and a same-rewriter, length-preserving control. That bundle is a better plan than sufficiency alone. The control should remain the main experiment. Sufficiency is the new training target.

## The six research questions

### 1. Does the accuracy gap widen with difficulty?

The question asks whether, on a multimodal model that writes thousands of tokens, the accuracy gap between a sketch and a long trace grows monotonically with difficulty.

A widening gap means unconditional shortening keeps accuracy only on easy items. A flat gap means brevity stays safe inside the long-reasoning regime. The paper's own 7B setup cannot run this, because the baseline averages 182–240 tokens. The question does not say which kind of step was deleted.

### 2. Does text-only deletion remove visual evidence?

The question asks whether deleting steps from the reasoning text alone disproportionately deletes readings, spatial relations, and constraints that appear only in the figure, and whether showing the image and the question to the compressor and the judge keeps those steps on perception-heavy items.

Fewer dropped visual steps and higher accuracy for the image-aware arm means the style label is the wrong training target. No difference across arms means the judge's blindness to the image is not the source of the errors. The question does not separate shortening that comes from the style reward, from RL itself, or from the GPT-5 rewrite.

### 3. After the sources are matched, does the sketch style still win?

The question asks whether, once the rewriter, the training steps, and the token budget match, and the x-axis is end-to-end latency including image tokens, the sketch still beats a same-model rewrite that keeps the original length and beats answering with no reasoning.

If the sketch loses to the length-preserving rewrite, the gain came from the rewriter changing content. If the sketch ties the arm whose style reward weight is 0, the sketch judge did not cause the shortening. If the sketch beats both controls, the style itself has a gain. This is the question among the six that audits the paper's causal claim directly.

### 4. Does a numbered list drop a visual premise that is used twice?

The question asks whether, when one fact in the figure is used by two later steps, a numbered sketch drops it more often than a sketch that keeps the dependency, and whether the accuracy loss sits on the second use.

This is a narrower mechanism inside question 2: a linear list has no mark for out-degree greater than 1. It can hold on these items while average sufficiency still looks fine. The sample size depends on finding or rewriting enough twice-used facts in MathVision.

### 5. Does the answer probability stay still when a deleted sentence is restored?

The question asks whether putting the sketch's omitted sentences back one at a time separates correct and incorrect items, by the change in the answer's log probability, better than the sketch's length does.

A large change that tracks errors means the deleted sentence was used and the compression was not sufficient. A score no better than length means a change in probability cannot be the deletion rule. Inserting a sentence changes the context, so the probability can move because of position. The experiment has to fix the insertion site and compare against inserting an unrelated sentence. It can be computed on outputs the paper already produces, without training a new model first.

### 6. Does accuracy fall in the upper tail?

The question asks whether, after sketch training, accuracy falls on items whose baseline reasoning length is above the 90th percentile, even while mean tokens fall by about 64% and mean accuracy holds.

A gap that grows with the quantile means the mean hides losses on long items, and the efficiency ratio does not hold. A flat gap means the mean can stand in for cost in this paper. The question audits the metric. A bad tail does not say that the judge should see the image.

## How they sit against the paper

| Research question | What it audits | Place relative to the headline |
|-------------------|----------------|--------------------------------|
| 1 Difficulty | The long-reasoning regime named in the introduction | Prior: the regime the evidence is in |
| 2 Seeing the image | A sketch being defined as a format | Mechanism: what the reward should be |
| 3 Matched sources | Where the shortening and the accuracy come from | Prior: whether the cause holds |
| 4 A premise used twice | The numbered-list format | A special case of question 2 |
| 5 Restoring a sentence | Whether deleted text was used | A measurement for question 2 |
| 6 The right tail | The mean as a metric | Whether the metric misleads |

The headline is blocked first by questions 3 and 1. Question 2 becomes the criterion most worth training once that cause holds.
