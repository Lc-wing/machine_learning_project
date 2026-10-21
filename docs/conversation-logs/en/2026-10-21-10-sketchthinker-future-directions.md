# 10 Three future directions that address the SketchThinker-R1 limitations

- Date: 2026-10-21
- Follows: [07](2026-10-21-07-sketchthinker-r1-limitations.md)
- Question: Given these limitations, suggest three distinct future research directions that could address them.
- Chinese version: [中文](../zh/2026-10-21-10-sketchthinker-future-directions.md)

## Conclusion

The three directions are three different scientific questions, not another combination of existing methods:

1. **Difficulty-conditioned brevity**: at what difficulty brevity starts to cost accuracy.
2. **Image-conditioned sufficiency compression**: whether the dropped steps were visual evidence the answer depends on.
3. **Separating distillation, budget, and real cost**: whether the reported gain comes from compression, or from the GPT-5 rewrite and unequal training.

## Skills used

- Stage three of the Assumption Inverter: turn the premises that already fail in [07](2026-10-21-07-sketchthinker-r1-limitations.md) into falsifiable propositions.
- Stage four of the Gap & Contradiction Miner: each direction has to say why bolting method A onto method B would not answer it.
- Novelty search with `find_papers.py` (2025 onward). The closest prior work is AdaptThink (EMNLP 2025; text-only, binary think-or-not), Learning to Think Fast and Slow for Visual Language Models (uses the length variation already present in pretrained VLMs), and Thinking Fast and Right together with AALC (rewards that trade accuracy against length). Each direction below states how it differs.

## Direction 1: Where brevity starts to hurt

**Limitations addressed**: the experiments never enter the long-reasoning regime; the style reward has a fixed weight and the claim that hard questions still get long traces has no evidence; the contradiction with "forcing longer thinking helps" (s1, 2025) is unresolved.

**Proposition**: on a multimodal reasoner that actually produces thousands of tokens, the accuracy gap against a long-reasoning baseline widens monotonically with difficulty, and above some threshold the loss from unconditional shortening exceeds the tokens saved.

**Why this is not A+B**: AdaptThink chooses between thinking and not thinking on text math problems, and its objective is to skip thinking while keeping average accuracy. Wiring that switch into SketchJudge, still constrained by average accuracy, lets losses on hard items be averaged away by easy ones, which is exactly what Table 1 cannot show. The missing piece is the **difficulty-stratified boundary**, not a switch.

**Difference from recent work**: Learning to Think Fast and Slow for Visual Language Models exploits the length variation a pretrained VLM already has. It does not test where shortening starts to cost accuracy, and it is not run on a long reasoner that overthinks.

**Minimal experiment**: take a genuinely long multimodal reasoner and report the accuracy gap and token count on each of MathVision's five difficulty levels, with multiple seeds and confidence intervals. The proposition fails if the gap does not widen with difficulty.

## Direction 2: Compression and judging must see the image

**Limitations addressed**: SketchJudge reads only the thinking trace and learns format and length; the rewriting prompt never sees the image or the question; the interpretability study measures readability, not faithfulness.

**Proposition**: dropping steps from the reasoning text alone disproportionately drops visual-evidence steps (readings, spatial relations, constraints visible only in the figure). A compressor and a judge that see the image, the question, and the trace, and that score whether the remaining steps still entail the answer, should beat text-only compression on perception-heavy items.

**Why this is not A+B**: attaching a vision encoder to the current judge changes nothing if the label is still "does this look like a numbered list". The label has to become sufficiency: does deleting this step change the answer.

**Difference from recent work**: faithfulness work studies text chain-of-thought (Turpin et al., 2023; Lanham et al., 2023). The same search used for this note found no 2025-or-later paper matching visual, reasoning compression, and faithfulness together.

**Minimal experiment**: build counterfactual images that change exactly one visual fact the sketch omits. If the model's answer changes while the sketch text does not, the trace was not using that evidence. Compare three compressors: text only, image plus question, and steps retained because they survive the intervention.

## Direction 3: Separate the source of the gain before claiming efficiency

**Limitations addressed**: the accuracy gain is confounded with GPT-5 distillation; baseline training budgets are unequal; efficiency is accuracy divided by token count and is dominated by the denominator; the token count excludes image tokens, and the training-time comparison covers only the RL stage.

**Proposition**: once the rewriting source, the training steps, and the total token budget are matched, and the x-axis is end-to-end latency including image tokens, the advantage of sketch-style reasoning over "a rewrite by the same model that keeps the original length" and over "answering with no reasoning" shrinks sharply. Whatever advantage remains should sit on items where reasoning text dominates the cost, not on items where image tokens do.

**Why this is not A+B**: a stronger rewriting model, or one more length penalty, does not identify where the gain comes from. The required control **changes style while holding the content source fixed**.

**Difference from recent work**: Thinking Fast and Right and AALC study how a reward should trade accuracy against length. They still measure generated tokens, they omit vision prefill, and they do not separate distillation from compression.

**Minimal experiment**: four arms, same base model, same data, same decoding, multiple seeds. (1) The paper's method. (2) A GPT-5 rewrite that keeps the original length and style, then the same training. (3) RL with the style reward set to 0. (4) Direct answering with no reasoning. Report accuracy against latency, not a single efficiency ratio. If (1) no longer beats (2) and (3), "the sketch style itself is what helps" is false.

## Priority

| Direction | Novelty | Claim it can refute | Cost | Suggestion |
|-----------|---------|---------------------|------|------------|
| 1. Difficulty boundary | Adjacent text work exists; the long multimodal regime is still open | "No loss in accuracy" | Moderate; needs a long reasoner | Do first; it targets the headline |
| 2. Image-conditioned sufficiency | Visual compression plus faithfulness is essentially open | "The sketch keeps the key steps" | Higher; needs image interventions | Second; it targets whether the method is real |
| 3. Separating the source of the gain | An experimental-design contribution, not a new model | "64% at no accuracy cost comes from the sketch style" | Low; reproducible at 7B | In parallel with direction 1; cheapest |
