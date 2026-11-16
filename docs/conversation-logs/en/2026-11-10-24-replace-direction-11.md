# 24 Replace record 11 with three directions that have not been done

- Date: 2026-11-10
- Follows: [07](2026-10-21-07-sketchthinker-r1-limitations.md), [10](2026-10-21-10-sketchthinker-future-directions.md), [11](2026-10-21-11-sketchthinker-existing-directions.md)
- Question: Use the skills for forming a research direction and for stating its research question. Revisit the task in record 10. From the paper's known limitations, generate three directions that have not been done, and replace record 11.
- Chinese version: [中文](../zh/2026-11-10-24-replace-direction-11.md)

## Conclusion

Record 11's three directions (length as an input, a process reward, continuous latent thoughts) are existing methods, so they are withdrawn. The three below replace them. They do not repeat record 10 (the difficulty boundary, image-conditioned sufficiency, and separating distillation from compression).

Search used `find_papers.py`, one query at a time, to avoid Semantic Scholar rate limits. OpenReview reviews were not read.

1. **A numbered list drops a visual premise that is used twice.**
2. **A step may be deleted only when putting the deleted sentence back leaves the answer probability unchanged.**
3. **A drop in mean token count pushes errors into the right tail of the length distribution.**

## Skills used

- Assumption Inverter: take three premises that record 7 shows are still assumed, and that record 10 did not invert, and write a falsifiable proposition and a minimal experiment.
- Gap & Contradiction Miner: for each direction, say why bolting on an existing method does not answer it, and name the result that separates the two explanations.

## Direction 1: A numbered list drops a visual premise that is used twice

**Premise inverted**: Turning a long trace into an order-preserving numbered list keeps the logic. That is written into this paper's rewriting prompt (Table 16: keep the order, emit numbered steps), and it is also how stepwise compressors such as Chain-of-Draft work.

**Failure mechanism**: If one fact in the figure is a premise of two later steps (out-degree at least 2), a linear list has no mark that the fact is used in more than one place. Under compression it looks like a detail that can be cut. After the cut, the second use becomes a number with no justification.

**Why this is not A+B**: The ACL 2026 preprint [Graph-Based Chain-of-Thought Pruning](https://arxiv.org/abs/2604.05643) also turns a chain into a directed acyclic graph, but it does so to remove low-impact reflections and repeated checks. Wiring that pruner into sketch training removes redundant reflection. It does not flag a visual premise that is used twice and therefore has to stay. The query `"numbered list" +reasoning +(multimodal|vision) +(compress|concise)` returned no hits from 2024 on.

**Research question**: On items where one diagram fact is used by two later steps, does a numbered sketch drop that fact more often than a sketch that keeps the dependency, and does the accuracy loss sit on the second use?

**Minimal experiment**: Select or rewrite MathVision items in which one length or angle is used twice. Compare a numbered list with a sketch that must point again at any premise whose out-degree exceeds 1. Record how often the fact is dropped and the accuracy at the second use. The proposition fails if the two sketches match.

## Direction 2: Putting the deleted sentence back should leave the answer probability unchanged

**Premise inverted**: A short trace that still states the final answer, and that looks like a sketch, is a sufficient compression. This paper's style reward is exactly that: a numbered list scores 1, a long trace scores 0, and the answer probability is never consulted.

**Failure mechanism**: If the deleted sentence was the only justification, the model is giving the answer without it. Putting the sentence back into the sketch moves the log probability of the answer. The sentence was unused only when that probability does not move.

**Why this is not A+B**: This is not record 10's image counterfactual, because the image is not changed. It is also not a process reward of the Let's Verify Step by Step kind. The query `"confidence" +(delete|prune|compress) "chain-of-thought" step calibration` returned no hits from 2024 on.

**Research question**: If the sentences a sketch omitted are put back one at a time, does the change in the answer's log probability separate correct and incorrect items better than how short the sketch is?

**Minimal experiment**: Keep the long trace and the sketch for the same items. Insert one omitted sentence at a time and record the absolute change in the answer's log probability. Use that change to predict whether the sketch is wrong, and compare it with a predictor that uses only length. The proposition fails if it is no more accurate than length.

## Direction 3: A lower mean token count pushes errors into the right tail

**Premise inverted**: Mean reasoning tokens, divided into an efficiency ratio, measure the cost of reasoning. This paper's `#Token` and its efficiency ratio are both means.

**Failure mechanism**: Reasoning length is heavy-tailed. A style reward shortens most items, so the mean falls. A minority of items that were already long can stay long and be wrong more often. The mean hides that slice.

**Difference from existing work**: [Sprint or Delve](https://doi.org/10.24963/ijcai.2026/653) (IJCAI/ECAI 2026) already reports that length is approximately log-normal, and it uses a powered length penalty so long traces are penalized less. It changes the penalty. Its data are text math problems. It does not test whether a multimodal method that wins by style classification loses accuracy in the upper quantile of baseline length. The heavy tail itself is not a new observation. What has not been done is the quantile-conditional accuracy of a style reward.

**Research question**: After sketch training, does accuracy fall on items whose baseline reasoning length is above the 90th percentile, even while mean tokens fall by about 64% and mean accuracy holds?

**Minimal experiment**: Split each benchmark into five quantiles of Vanilla-R1 reasoning length. Report the accuracy gap, the token ratio, multiple seeds, and a confidence interval in each quantile. The proposition fails if the gap does not grow across quantiles.
