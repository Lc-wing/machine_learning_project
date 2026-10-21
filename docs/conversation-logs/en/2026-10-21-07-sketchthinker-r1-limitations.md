# 07 Primary limitations and potential weaknesses of the SketchThinker-R1 methodology

- Date: 2026-10-21
- Paper: "SketchThinker-R1: Towards Efficient Sketch-Style Reasoning in Large Multimodal Models", [arXiv 2601.02825](https://arxiv.org/abs/2601.02825)
- Question: What are the primary limitations or potential weaknesses of the methodology presented in this paper?
- Chinese version: [中文](../zh/2026-10-21-07-sketchthinker-r1-limitations.md)

## Conclusion

Compressing reasoning into numbered "sketches" is not the problem in itself. The main weakness is that **the evidence covers only a narrow regime, and the key new components are never tested on their own**. The headline claim is "64% fewer reasoning tokens with no loss in accuracy". The 64% figure is computed correctly (64.7%–76.5%), but "no loss in accuracy" really amounts to "roughly the same accuracy", and only holds for reasoning that was already short, on 3B and 7B Qwen2.5-VL models.

## Scope and method

- Read the full arXiv HTML text: body, all appendices (A–K), and every table. Inspected Figures 1, 4, and 11; did not inspect the qualitative-case figures (3 and 5–10).
- Skills used:
  - Gap & Contradiction Miner: extracted the limitations the authors acknowledge and aligned the paper against conflicting literature.
  - First-Principles Assumption Inverter: identified the method's hidden premises and worked out where each would fail.
  - nature-skills: borrowed the evidence-boundary checklist from `nature-paper-xray` and the issue taxonomy and consistency check from `nature-reviewer`, without using the full three-reviewer format.
- Recomputed every EoT value and token reduction in both main tables with a script, and verified several external facts (VisuLogic's random baseline, the base model's official scores, and the literature used for comparison).

## Main limitations, ordered by impact on the conclusions

### 1. The experiments never reach the "long reasoning" regime the paper is motivated by

- The motivation is o1/R1-style reasoning that runs to thousands of tokens.
- But the Vanilla-R1 baseline averages only 182–240 reasoning tokens at evaluation (Tab. 1) and about 300 during training (Fig. 1d), with a maximum response length of 2048.
- The actual saving is about 120–185 tokens per question. The paper shows that already-short reasoning can be made shorter; it does not test the overthinking regime, where the claimed benefits would matter most and the risks are highest.

### 2. The claim of "comparable or even better accuracy" lacks statistical support

- **The gains are tiny**: +0.2 to +1.9 points at 7B. At 3B, MathVision is 1.6 points *below* Vanilla-R1 (26.9 → 25.3).
- **No error bars**: no seeds, variance, or confidence intervals anywhere in the paper. By my estimate, if MMMU uses the 900-question validation split, the standard error of accuracy alone is about 1.6 points.
- **VisuLogic carries almost no signal**: it is four-way single-choice with a measured random baseline of 24.9%; the untrained base model scores 26.0; every method in the paper lands between 25 and 28.
- **The MathVision split is not stated**: the paper does not say whether it used the 3,040-question test set or the 304-question testmini. The ratio of inference time to token count in Fig. 11 suggests testmini (my inference; the paper does not say). If so, a 0.7-point difference is about 2 questions.
- **Ablation gaps fall within the same noise**: most differences in Tabs. 4–7 are 0.2–0.6 points, so a claim like "binary reward beats dense reward" (62.8 vs. 62.6) is not supported.

### 3. The core contribution, the SketchJudge reward model, is never shown to work on its own

- **The style-reward weight barely affects length**: Tab. 5 has no ablation with a style-reward weight of 0; the lowest is 0.05. At 0.05 the model already uses 65.2 tokens, versus 64.3 at the default 0.1.
- **The length drops mainly during RL**: cold start alone gives 114.5 tokens, and adding RL brings it to 64.3 (Tab. 3a). That shortening may come from RL itself rather than from the style reward.
- **An untrained, prompted judge does about as well**: using it gives 72.1 tokens (Tab. 3d).
- **The judge's own reliability is never checked**: no accuracy or robustness evaluation of SketchJudge on held-out data.

### 4. SketchJudge is blind to content, so it likely learns surface features

- **How it was trained**: sketches GPT-5 rewrote as numbered lists were labeled 1, and the original long reasoning was labeled 0. At scoring time it sees only `[THINKING]`: no question, no image, and no knowledge of whether the answer was right.
- **Consequence**: it cannot judge whether a sketch is sufficient for the problem, so in practice it is closer to a format-and-length detector.
- **The authors acknowledge reward hacking**: with a high style weight, "the model focuses solely on achieving a higher sketch-style thinking reward and neglects correctly answering the question" (App. E).
- **The "adaptive length" claim has no evidence**: Sec. 2.2 says the model "can still generate relatively long and extensive reasoning for challenging questions", but the paper offers no evidence such as reasoning length versus difficulty.

### 5. The accuracy gain is confounded with distillation from GPT-5

- **The rewriting model matters too much**: converting the cold-start data with GPT-5 gives 62.8, with Qwen2.5-72B only 59.1 (Tab. 3b), which is below Vanilla-R1's 61.0. If conversion merely deleted words, swapping the converter should not move accuracy by 3.7 points; a likelier explanation is that GPT-5 adds or corrects content.
- **The rewriting prompt sees only the reasoning text**: it contains only `{reasoning}` (Tab. 16), so GPT-5 picks the "key steps" without seeing the image or the question, and visual details may be dropped.
- **The data checks are thin**: quality checks only asked whether key steps were preserved (5 people × 20 samples; an automated model check flagged 4.1% as missing key steps). Nobody checked whether the original long reasoning was correct.
- **Reproducibility**: the method depends on the proprietary GPT-5.
- **The clean control is missing**: a GPT-5 rewrite that keeps the original length and style.

### 6. The baseline comparison is not apples to apples, and the efficiency metric is biased

- **Different training budgets**: SketchThinker gets 20K examples of SFT plus RL plus a reward model. The baselines get only prompting, only SFT (C3oT, VeriThinker), or only RL with no cold start (L1, ThinkPrune). L1's target length is not reported, and there is no comparison at matched token budgets.
- **EoT (accuracy / tokens) is dominated by token count**:
  - Constrained CoT is 2.4 points less accurate, yet its EoT is 0.749 versus 0.335 for Vanilla-R1.
  - In Tab. 5, the 0.2:0.4:0.4 weighting loses 2 points of accuracy while EoT barely moves.
- **"Fewer tokens than every baseline" is not true**: at 7B on PhyX, Constrained CoT uses 73.4 tokens versus SketchThinker's 75.3. At 3B on MathVision, Constrained CoT (63.4) and Chain-of-Draft (71.5) both use fewer than SketchThinker's 72.7, and SketchThinker's accuracy is also below Vanilla-R1. This contradicts Tab. 2's caption, which says the method "consistently outperforms… in both answer accuracy and reasoning token cost".

### 7. Hyperparameters were selected on a test benchmark, and "generalization" is near-domain

- **Selection pressure**: every ablation is run on MMMU, which is itself an evaluation benchmark, and the default reward weights were chosen by best MMMU EoT, so the MMMU headline number is optimistic.
- **Training and evaluation domains map one to one**:

  | RL training data | Evaluation benchmark |
  |---|---|
  | MMStar | MMMU |
  | MathVista | MathVision |
  | LogicVista | VisuLogic |
  | SeePhys | PhyX |

- **Untested areas**: OCR, charts, documents, spatial reasoning, video, and open-ended generation.
- **Model coverage**: only Qwen2.5-VL at 3B and 7B.

### 8. The interpretability evidence is weak, and faithfulness is never tested

- **The human study is small**: 5 evaluators of unstated background, 20 samples, all from questions both models answered correctly; blinding is not mentioned, and the scores (3.95 vs. 4.25) come with no statistical test.
- **The model-judged comparison may favor concise text**: using Qwen3-VL-Plus as the judge gives 4.12 vs. 4.33.
- **Interpretable is not the same as faithful**: short reasoning may be written after the fact rather than reflecting the actual computation ([Turpin et al., NeurIPS 2023](https://arxiv.org/abs/2305.04388); [Lanham et al., 2023](https://arxiv.org/abs/2307.13702)).
- **Shorter can be harder to verify**: in a cold-start example in Fig. 4, the step "OD = 1/2 AC" drops the justification that D is the midpoint of BC.
- **No no-reasoning baseline**: there is no direct-answer baseline under the same protocol. If answering directly scores about the same, the reasoning was not doing much to begin with, and "compressing it without losing accuracy" is trivially true. For reference, Qwen2.5-VL-7B's official direct-answer scores are 58.6 on MMMU val and 25.07 on MathVision (under a different evaluation protocol).

### 9. The cost accounting is incomplete

- **The token count only covers reasoning**: `#Token` excludes image tokens and prompt prefill.
- **The speedup cannot be generalized**: Fig. 11 shows inference time dropping to about one third, but the serving setup (batching, inference framework) is not described.
- **The training-time comparison covers only one stage**: "training time ×0.81" compares only the RL stage (Tab. 15). It leaves out cold-start SFT, SketchJudge training, and the cost of calling GPT-5 to rewrite 20K examples.

## Limitations the authors acknowledge themselves

The paper has no Limitations section. Four admissions are scattered through the text:

- A high style weight causes reward hacking (App. E).
- Data rewritten by open-source models lowers accuracy: "at the expense of lower answer accuracy" (Tab. 3).
- Cold start alone "is largely restricted to the training set" (Sec. 3.2).
- The human study "is based on a small sample size" (App. G).

## Contradictions with prior work

**Test-time scaling vs. "shorter is fine".** [s1 (EMNLP 2025)](https://arxiv.org/abs/2501.19393) shows that forcing longer thinking improves accuracy. The overthinking line of work ([Chen et al., 2024](https://arxiv.org/abs/2412.21187)) and this paper argue that shortening reasoning does not hurt.

- **Assessment**: this is a boundary-condition contradiction. The deciding variable is problem difficulty relative to model capability, together with how long the baseline reasoning already is.
- **This paper cannot settle it**: its evidence lies entirely in the short-baseline regime, plus near-chance accuracy on VisuLogic.
- **Tension with its own sources**: its related-work section describes Vision-R1 ([Huang et al., 2025](https://arxiv.org/abs/2503.06749)) as progressively increasing reasoning length, and its cold-start data comes directly from Vision-R1.
- **Decisive experiment**: split MathVision by its 5 difficulty levels and check whether SketchThinker's accuracy gap widens with difficulty. The −1.6 at 3B on MathVision is consistent with this hypothesis but does not prove it.

## Hidden premises and where they break

| Hidden premise | Where it is built in | Extreme case where it breaks | What is needed |
|---|---|---|---|
| Key steps can be identified from the reasoning text alone | The rewriting prompt and SketchJudge never see the image or the question | Perception-heavy tasks: charts, fine-grained counting, multiple images | Compression and scoring that also see the image and question, keeping visual-evidence steps |
| Reasoning style can be judged separately from content | The style reward ignores the question and has a fixed weight | Hard multi-step problems, where uniform brevity leads to under-reasoning | A brevity reward conditioned on difficulty and correctness |
| Token count equals compute cost | `#Token` counts only reasoning tokens | High-resolution images, multiple images, or video, where image tokens dominate | End-to-end FLOPs and latency measurements |
| Multiple-choice accuracy reflects reasoning quality | All four benchmarks are mostly multiple choice | Near-chance settings like VisuLogic | Open-ended questions with verifiable answers, plus step-level evaluation |

Falsifiable prediction: on MathVision's level 4–5 problems, SketchThinker's accuracy gap versus Vanilla-R1 should widen monotonically with difficulty. If the gap stays flat across levels, the second premise holds.

## Reporting inconsistencies

These do not change the conclusions, but they hurt reproducibility:

- **Rollout batch size**: Sec. 3 says 128, App. D.3 says 512. The stated 105 training steps only work out with 128 (7 steps per epoch × 15 epochs).
- **Tab. 8 text vs. numbers**: the text says the long-reasoning cold-start baseline reached 61.8, but no 61.8 appears in the table; the highest value is 62.0.
- **Hardware**: Sec. 3 says 8× H200, App. J says 8× H800.
- **Wrong table references**: the stage ablation should be Tab. 3(a), the data-source ablation Tab. 3(c), and the training-step scaling Tab. 10.
- **Algorithm name**: GRPO is misnamed "Group Reward Proximal Optimization" (it is Group Relative Policy Optimization).
- **Missing evaluation details**: no data splits, decoding settings, number of runs, or answer-matching method anywhere in the paper.

## Experiments worth adding first

1. Apply the method to a genuinely long-reasoning model (thousands of tokens).
2. Ablate with a style-reward weight of 0.
3. Add a no-reasoning, direct-answer baseline, and report accuracy against token count as a curve.
4. Analyze results by difficulty level.
5. Report multiple seeds with confidence intervals, and select hyperparameters on a separate validation set rather than on MMMU.

## Verified external facts

- VisuLogic: 1,000 four-option single-choice questions; measured random baseline 24.9%, humans 51.4%; Qwen2.5-VL-7B-Instruct scores 26.0 ([VisuLogic paper](https://arxiv.org/abs/2504.15279)).
- Qwen2.5-VL-7B-Instruct official scores: MMMU val 58.6, MathVision 25.07 ([model card](https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct)).
