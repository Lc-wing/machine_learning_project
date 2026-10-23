# SketchThinker-R1 presentation: slide outline

16 slides, 15:00 total (Part I paper analysis 12:00, Part II research plan pitch 3:00). Timing follows speaker-script.md at 130 words per minute. The .pptx has not been rebuilt from this outline yet.

## Slide 01 — SketchThinker-R1: Towards Efficient Sketch-Style Reasoning in Large Multimodal Models
Part I · 00:00–00:37 · 80 words

- ICLR 2026 poster; Ruiyang Zhang, Dongzhan Zhou, Zhedong Zheng (University of Macau, Shanghai AI Laboratory)
- Question: shorten multimodal reasoning while keeping accuracy
- Group member/contribution table (placeholder, unchanged)

Visual: Existing cover slide, kept as is

## Slide 02 — Long reasoning spends tokens on repeated explanation
Part I · 00:37–01:28 · 110 words

- Long traces cost decoding time and tokens
- Sketch = concise numbered textual steps, not drawing
- Compression only helps if remaining steps still support the answer

Visual: Paper Fig. 1 / Fig. 3 example (paper-fig1-000.jpg, paper-fig3-left-case.png)

## Slide 03 — Three training stages turn sketches into a policy
Part I · 01:28–02:21 · 115 words

- Cold start → SketchJudge → RL
- Policy sees image + question; judge sees thinking text only
- That input gap drives the later analysis

Visual: pipeline-redraw.svg with original Fig. 2 below

## Slide 04 — Cold start teaches the model what a sketch looks like
Part I · 02:21–03:18 · 125 words

- SketchColdStart-20K: 10K LLaVA-CoT-100K + 10K Vision-R1-cold
- GPT-5 rewrites long traces into short numbered steps
- Rewrite prompt sees reasoning only

Visual: Long-vs-sketch trace pair

## Slide 05 — SketchJudge rewards a textual style
Part I · 03:18–04:16 · 125 words

- Judge: Qwen2.5-7B-Instruct, text only
- Long trace = 0, sketch = 1; 40K labelled traces
- Scores style, not visual support

Visual: Judge input/label diagram

## Slide 06 — RL balances correctness, format, and thinking style
Part I · 04:16–05:21 · 140 words

- GRPO, 5 rollouts per group
- Reward = 0.5 accuracy + 0.4 format + 0.1 style
- Binary style score

Visual: Reward equation with weight bar

## Slide 07 — Evaluate answer quality and reasoning cost separately
Part I · 05:21–06:14 · 115 words

- Benchmarks: MMMU, MathVision, VisuLogic, PhyX
- RL set: 250 each from MMStar, MathVista, LogicVista, SeePhys
- Accuracy and token cost reported separately

Visual: Benchmark/data table

## Slide 08 — At 7B, tokens fall sharply across all four benchmarks
Part I · 06:14–07:16 · 135 words

- 7B MMMU accuracy 61.0 → 62.8
- Avg. reasoning tokens 182.2 → 64.3
- Token cuts on all four benchmarks

Visual: tokens-7b.svg

## Slide 09 — On MMMU, the 7B model improves both axes
Part I · 07:16–08:09 · 115 words

- MMMU accuracy vs tokens
- SketchThinker-R1 upper-left of baselines
- Prompting shortens but loses accuracy

Visual: accuracy-vs-tokens-mmmu.svg

## Slide 10 — Stage ablations leave the reward effect unresolved
Part I · 08:09–09:07 · 125 words

- Cold start alone 61.4% / 114.5 tokens; RL alone 62.1% / 152.2
- Combination best
- Incremental effect of style reward not isolated

Visual: stages-ablation.svg; accuracy-delta-3b.svg

## Slide 11 — Five limitations define the next tests
Part I · 09:07–10:18 · 155 words

- L1 reward validity: judge never checks missing visual support
- L2 attribution: style-reward effect under shared cold start
- L3 accuracy tradeoff (3B MathVision 26.9 → 25.3); L4 transfer (one backbone family, two scales)
- L5 full cost and reproduction (batch 128 vs 512; 8×H200 vs 8×H800)

Visual: Five-row limitation table, L1 highlighted

## Slide 12 — Three directions target different interventions
Part I · 10:18–11:12 · 115 words

- D1 reward: preserve explicit visual support, catch omitted premises
- D2 allocation: image-conditioned budget router
- D3 attribution and lifecycle cost ledger
- We pick D1: testable through the judge first

Visual: Three-column direction cards, D1 highlighted

## Slide 13 — Probe D1: does omission detection add value?
Part I · 11:12–12:00 · 105 words

- Probe: does omission detection add value at matched length/compute?
- Paired judge items: complete / missing-premise (correct answer) / harmless deletion
- Compare sufficiency vs style vs stated-step correctness vs zero auxiliary

Visual: Paired-trace probe diagram

## Slide 14 — Pitch: preserve the evidence behind an answer
Part II · 12:00–13:00 · 130 words

- Sufficient trace = explicit correct visual premises + valid deductions
- Triangle example: read 40° and 60° from image → 80°
- Image checks stated facts, does not fill omissions; stated-step judge gets same inputs

Visual: Annotated triangle with supported vs silent-import traces

## Slide 15 — Four rewards share data, initialization, and compute
Part II · 13:00–14:00 · 130 words

- 3,000 geometry/bar-chart problems; 1,600 / 400 / 1,000 by template family
- Four arms on Qwen2.5-VL-7B: sufficiency, style, stated-step correctness, zero auxiliary; 3 seeds
- One budget-conditioned policy (64/128/256 tokens); human audit of 300 test items; 200 + 100 image pairs

Visual: Arm × seed grid with data split bar

## Slide 16 — Gate first; test useful gains within the compute cap
Part II · 14:00–15:00 · 130 words

- Judge gate: false acceptance ≤ 10%, sufficient-trace recall ≥ 70% before RL
- Success near 128 tokens: +3 pts accuracy and +5 pts human sufficiency vs style, CIs above 0
- 400 GPU-hour cap: 12 runs × 25 h + 100 h shared

Visual: Gate → train → evaluate timeline with compute bar
