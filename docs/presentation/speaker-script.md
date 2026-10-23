# SketchThinker-R1 — Speaker script

English speaker script · 16 slides · 1,950 spoken words · 15:00 at 130 words per minute. Part I: 1,560 words / 12:00. Part II: 390 words / 3:00. Timing excludes unscripted discussion. Word counts exclude headings, source cues, and metadata; hyphenated words count as one.

## Slide 01 — SketchThinker-R1: Towards Efficient Sketch-Style Reasoning in Large Multimodal Models

Part I · 00:00–00:37 · 80 words · 36.9 seconds

Today I will present SketchThinker-R1, by Ruiyang Zhang, Dongzhan Zhou, and Zhedong Zheng, from the University of Macau and Shanghai AI Laboratory. This is an ICLR 2026 poster. The central question is how to shorten multimodal reasoning while preserving answer accuracy. I will explain the training pipeline, examine the results and their boundaries, then pitch our research plan on preserving visual evidence. The editable table records our group members and their contributions before we begin the main technical paper discussion.

*Source cue (not spoken): PDF p.1; title and author metadata*

## Slide 02 — Long reasoning spends tokens on repeated explanation

Part I · 00:37–01:28 · 110 words · 50.8 seconds

Multimodal reasoning models often explain every intermediate step in full sentences. That creates a practical bottleneck: generating more reasoning tokens increases decoding work and response time for a single answer. The authors' starting point is that detailed explanation contains redundancy. Their bet is that a compact sketch can retain the key logical flow while removing repeated descriptions and commentary. Here, sketch means concise textual reasoning, organized into short numbered steps. It does not mean drawing a new image. The example from the paper connects visual relationships to a short mathematical derivation. The challenge is to learn which information deserves space, because simply asking for fewer words also removes useful reasoning.

*Source cue (not spoken): PDF pp.1–2, Fig.1; p.8, Fig.3*

## Slide 03 — Three training stages turn sketches into a policy

Part I · 01:28–02:21 · 115 words · 53.1 seconds

The framework has three stages with different jobs. First, Sketch-Mode Cold Start teaches the answering model to imitate compressed reasoning traces. Second, a separate SketchJudge Reward Model learns to distinguish sketch-style thinking from normal detailed thinking. Third, Sketch-Thinking Reinforcement Learning uses that judge alongside correctness and format rewards. This division matters. Cold start supplies examples of the target behavior, the judge makes that behavior scoreable, and reinforcement learning trains the model to apply it on another collection of questions across visual domains. The answering model receives images and questions throughout. The judge receives the thinking text. The original pipeline appears below our simplified redraw so the relationship between the presentation and the source stays visible.

*Source cue (not spoken): PDF p.3, Fig.2; §§2.1–2.3*

## Slide 04 — Cold start teaches the model what a sketch looks like

Part I · 02:21–03:18 · 125 words · 57.7 seconds

For cold start, the authors construct SketchColdStart-20K. They sample ten thousand questions from LLaVA-CoT-100K and ten thousand from Vision-R1-cold. GPT-5 rewrites the existing long reasoning into short numbered steps. The conversion instructions preserve the order and key logic while removing extra details and examples. The resulting image, question, sketch, and answer examples supervise the multimodal backbone through ordinary next-token training. The default answering backbone is Qwen2.5-VL-7B-Instruct, with a separate three billion parameter version also evaluated. This stage changes both the amount of text and its wording. Therefore, its benefits combine compression with teacher rewriting. The converter ablation tests different teachers, but does not isolate shortening from all other changes to the reasoning content. That distinction matters when we design the later controlled comparison experiments.

*Source cue (not spoken): PDF p.5, §3; p.14, App.D.1; p.21, Table16*

## Slide 05 — SketchJudge rewards a textual style

Part I · 03:18–04:16 · 125 words · 57.7 seconds

SketchJudge is a language model rather than the multimodal answering model. The default judge uses Qwen2.5-7B-Instruct. Training pairs each original long trace with label zero and its rewritten sketch with label one, producing forty thousand labeled traces. At reinforcement learning time, the same judge classifies the generated thinking text. Its prompt asks whether the reasoning contains only the key logical flow or detailed analysis. It receives neither the image nor the question. This directly supervises style, while answer accuracy is checked separately. The design also avoids a fixed target length, allowing longer sketches for demanding questions. Its central boundary is equally clear: a positive style label does not verify that a visual premise is correct or explicitly retained under the tested language-only scoring prompt.

*Source cue (not spoken): PDF p.4, §2.2; p.14, App.D.2; p.7, Table3d*

## Slide 06 — RL balances correctness, format, and thinking style

Part I · 04:16–05:21 · 140 words · 64.6 seconds

The reinforcement learning stage uses GRPO, which compares sampled responses to the same question. The paper samples five rollouts per group. Each response receives a weighted reward: zero point five for accuracy, zero point four for format, and zero point one for thinking style. The style component is binary. For a worked example, a correct answer with valid format and sketch style receives one point. If the answer is wrong but format and style pass, it receives zero point five. These are arithmetic examples of the stated reward, not experimental observations. Group rewards are centered and scaled to obtain relative advantages. A clipped policy update favors higher advantage responses, while a KL penalty limits departure from the reference policy. There is no explicit token penalty in this default objective; shorter traces emerge from style supervision during each sampled training group.

*Source cue (not spoken): PDF p.4, Eqs.2–6; p.5, §3*

## Slide 07 — Evaluate answer quality and reasoning cost separately

Part I · 05:21–06:14 · 115 words · 53.1 seconds

The main evaluation spans four benchmarks: MMMU for broad multimodal reasoning, MATH-Vision for visual mathematics, VisuLogic for visual logic, and PhyX for physics. The paper labels MATH-Vision as MathVision in its tables. Training for reinforcement learning uses SketchRL-1K, with two hundred fifty questions from each of MMStar, MathVista, LogicVista, and SeePhys. Baselines cover direct R1-style training, prompting, supervised fine tuning, and length-oriented reinforcement learning. The reported metrics are final answer accuracy and average reasoning tokens. Efficiency of Thinking divides accuracy, expressed in percentage points, by reasoning tokens. I will keep accuracy and cost visible separately, because an efficiency ratio alone hides whether a shorter model also loses correct answers rather than a single combined score.

*Source cue (not spoken): PDF p.5, §3; p.6, Tables1–2*

## Slide 08 — At 7B, tokens fall sharply across all four benchmarks

Part I · 06:14–07:16 · 135 words · 62.3 seconds

Table one provides the strongest evidence for the headline. At seven billion parameters, MMMU accuracy rises from sixty one to sixty two point eight percent, while average reasoning tokens fall from one hundred eighty two point two to sixty four point three. Across the four benchmarks, token reductions range from sixty four point seven to seventy six point five percent, calculated directly from the reported means. Accuracy also increases in every benchmark, although the margins differ. VisuLogic gains only zero point two percentage points, whereas PhyX gains one point nine. The chart shows token savings, and the adjacent table preserves the accuracy comparison. These are reported point estimates. The paper does not provide confidence intervals for these main results, so the smallest gains do not establish a reliable advantage across multiple independent repeated training runs.

*Source cue (not spoken): PDF p.6, Table1; reductions computed from table entries*

## Slide 09 — On MMMU, the 7B model improves both axes

Part I · 07:16–08:09 · 115 words · 53.1 seconds

This plot places every method from the MMMU section of Table one on the same axes. Moving left reduces reasoning tokens; moving up improves accuracy. SketchThinker-R1 occupies the upper left relative to all listed baselines. Prompting methods shorten the output, but their accuracy falls below Vanilla-R1. The supervised and length-oriented reinforcement learning baselines lie between those extremes. For this dataset and backbone, the complete sketch pipeline improves both measured objectives. This is a comparison among the reported operating points, not a complete frontier over all possible budgets. The table does not establish the best achievable accuracy for every baseline after an identical sweep of decoding settings, reward weights, and training compute and other relevant choices.

*Source cue (not spoken): PDF p.6, Table1, MMMU columns*

## Slide 10 — Cold start and RL contribute together

Part I · 08:09–09:07 · 125 words · 57.7 seconds

The stage ablation explains why the authors combine imitation and reinforcement learning. On MMMU, cold start alone reaches sixty one point four percent accuracy with one hundred fourteen point five reasoning tokens. Reinforcement learning alone reaches sixty two point one percent with one hundred fifty two point two tokens. Combining both reaches sixty two point eight percent with sixty four point three tokens. That supports complementary contributions from the two stages under the tested setup. The judge ablation also favors a fine tuned seven billion parameter judge over the corresponding model used without fine tuning. However, these experiments do not isolate a unique causal mechanism inside the traces. Different converters also change final accuracy, so teacher quality and rewritten content remain part of the explanation.

*Source cue (not spoken): PDF p.7, Tables3a,3b,3d*

## Slide 11 — The 3B result exposes an accuracy boundary

Part I · 09:07–10:05 · 125 words · 57.7 seconds

The smaller model prevents us from turning the headline into a universal claim. Table two reports strong token savings at three billion parameters, but MATH-Vision accuracy falls from twenty six point nine percent for Vanilla-R1 to twenty five point three for SketchThinker-R1. That is a loss of one point six percentage points. MMMU, VisuLogic, and PhyX show positive accuracy differences. The correct reading is that compression and answer quality trade differently across tasks and model sizes. This single comparison does not identify deleted visual evidence as the cause. It motivates checking what information survives compression and evaluating harder problems separately. For our own study, accuracy and explicit explanation sufficiency will remain distinct measurements, across the full range of token budgets, even when both improve together.

*Source cue (not spoken): PDF p.6, Table2*

## Slide 12 — Appendix results refine the efficiency claim

Part I · 10:05–11:07 · 135 words · 62.3 seconds

The appendix adds useful qualifications and extensions. On MMMU, dynamic reward weighting improves on the fixed default, reaching sixty three point two percent accuracy with sixty two point five reasoning tokens. Therefore, a fixed style coefficient is a design choice rather than a demonstrated optimum across schedules. Scaling the reinforcement learning set from one thousand to five thousand examples raises the seven billion parameter model's MMMU accuracy from sixty two point eight to sixty six point one percent. The reported training time decreases from two point seven zero hours for Vanilla-R1 to two point two one hours for SketchThinker-R1 on eight H800 GPUs under that configuration. Finally, human interpretability scores improve, but that study uses only twenty jointly correct examples and five evaluators. Readability evidence is valuable; it does not independently verify complete visual support.

*Source cue (not spoken): PDF pp.16–18, Tables7,9,11; p.20, Table15*

## Slide 13 — Efficient answers leave evidence preservation unresolved

Part I · 11:07–12:00 · 115 words · 53.1 seconds

My assessment is that the paper establishes a practical training recipe for shorter multimodal reasoning, with especially strong token savings in its seven billion parameter comparisons. The evidence boundary has three parts. First, style supervision does not directly inspect visual grounding. Second, reported point estimates and limited human studies leave uncertainty about small gains and difficult subgroups. Third, reproduction requires resolving reporting inconsistencies, including different rollout batch sizes in the main text and appendix. The cold-start quality checks assess preservation of key steps, but they do not measure necessary visual premises in generated benchmark traces. That unresolved measurement problem leads to our research plan: evaluate whether compressed explanations explicitly preserve the evidence supporting their answers.

*Source cue (not spoken): PDF §2.2, Tables1–3,11–14; §3 versus App.D.3*

## Slide 14 — Pitch: preserve the evidence behind an answer

Part II · 12:00–13:00 · 130 words · 60.0 seconds

Our plan is titled Preserving Visual Evidence in Compressed Multimodal Reasoning. The question is whether image-conditioned sufficiency supervision improves the accuracy and length tradeoff beyond style supervision. We define a sufficient trace as an explicit set of correct visual premises and valid deductions supporting its returned answer. Consider a triangle whose two given angles appear only in the image. A calculation that silently imports those readings leaves its premises unstated. A compact trace that explicitly states the angle readings and then applies the triangle sum supplies independently checkable support. We accept validated alternative derivations and allow redundant statements to disappear. This targets explanation sufficiency, not a claim about the model's hidden causal reasoning. We will test visual omission, reward effectiveness, and whether any advantage survives controls for rewriting and compute.

*Source cue (not spoken): Research plan; proposal §§1,3; illustrative example*

## Slide 15 — Compare evidence and style under shared data and compute

Part II · 13:00–14:00 · 130 words · 60.0 seconds

The planned experiment uses one seven billion parameter answering model and a separate image-conditioned judge. Three reward arms share the same rewritten examples and cold-start weights: evidence reward, style reward, and a zero auxiliary component. Evidence and style are binary and carry the same coefficient. We plan twenty four hundred rendered geometry and bar-chart problems, split by template family, plus checked answer-changing and nuisance-edit image pairs. The judge learns from supported traces, missing-premise negatives, wrong readings, and invalid deductions. We will compare answer accuracy, necessary-premise retention, human sufficiency, and paired-image correctness. Operating points must match achieved average reasoning lengths within five percent. Compute accounting includes rollouts and judge inference. Separate rewriting controls and an image-ablated judge test the contribution of content changes and visual access on the held-out test problems.

*Source cue (not spoken): Proposal §§3–4; all sample sizes and targets are planned*

## Slide 16 — A six-month plan with explicit success and null outcomes

Part II · 14:00–15:00 · 130 words · 60.0 seconds

The six-month schedule begins with reproduction and a compute pilot, then diagram annotation, judge calibration, policy training, controlled tests, and a final human audit. Before policy training, the judge must meet development targets of at most ten percent false acceptance and at least seventy percent sufficient-trace recall. We retain three training seeds and reduce the number of budget settings if measured compute exceeds available capacity. Our prediction is improved premise retention and accuracy at matched lengths and compute. The experiment also has clear null outcomes: no accuracy gain, poor judge transfer, or gains that disappear under resource controls weaken that prediction. Retention gains alone support explanation quality. The deliverable is a controlled answer to the evidence-preservation question, with calibrated judgments, reproducible comparisons, and published failure cases alongside any successful results.

*Source cue (not spoken): Proposal §§3–5; planned milestones, thresholds, and resources*

## Word counts per slide

| Slide | Part | Words | Time window |
|---|---|---:|---|
| 1 | I | 80 | 00:00–00:37 |
| 2 | I | 110 | 00:37–01:28 |
| 3 | I | 115 | 01:28–02:21 |
| 4 | I | 125 | 02:21–03:18 |
| 5 | I | 125 | 03:18–04:16 |
| 6 | I | 140 | 04:16–05:21 |
| 7 | I | 115 | 05:21–06:14 |
| 8 | I | 135 | 06:14–07:16 |
| 9 | I | 115 | 07:16–08:09 |
| 10 | I | 125 | 08:09–09:07 |
| 11 | I | 125 | 09:07–10:05 |
| 12 | I | 135 | 10:05–11:07 |
| 13 | I | 115 | 11:07–12:00 |
| 14 | II | 130 | 12:00–13:00 |
| 15 | II | 130 | 13:00–14:00 |
| 16 | II | 130 | 14:00–15:00 |
| **Part I** | | **1,560** | **12:00** |
| **Part II** | | **390** | **3:00** |
| **Total** | | **1,950** | **15:00** |
