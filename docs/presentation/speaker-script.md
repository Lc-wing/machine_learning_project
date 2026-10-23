# SketchThinker-R1 — Speaker script

English speaker script · 16 slides · 1,950 spoken words · 15:00 at 130 words per minute. Part I: 1,560 words / 12:00. Part II: 390 words / 3:00. Timing excludes unscripted discussion. Word counts exclude headings, source cues, and metadata; hyphenated words count as one.

## Slide 01 — SketchThinker-R1: Towards Efficient Sketch-Style Reasoning in Large Multimodal Models

Part I · 00:00–00:37 · 80 words · 36.9 seconds

Today I will present SketchThinker-R1, by Ruiyang Zhang, Dongzhan Zhou, and Zhedong Zheng, from the University of Macau and Shanghai AI Laboratory. This is an ICLR 2026 poster. The central question is how to shorten multimodal reasoning while preserving answer accuracy. I will explain the training pipeline, examine the results and their boundaries, then pitch our research plan on preserving visual evidence. The editable table records our group members and their contributions before we begin the main technical paper discussion.

*Source cue (not spoken): PDF p.1; title and author metadata*

## Slide 02 — Long reasoning spends tokens on repeated explanation

Part I · 00:37–01:28 · 110 words · 50.8 seconds

Multimodal reasoning models often explain every intermediate step in full sentences. That creates a practical bottleneck: generating more reasoning tokens increases decoding work and response time. The authors start from a simple observation: detailed explanations contain repetition. Their goal is to retain the key logical flow in a compact sketch. Here, sketch means concise textual reasoning, usually organized into numbered steps. It does not mean drawing another image. In this example, visual relationships lead to distances, then a triangle, and finally an area calculation. The challenge is deciding what deserves space. Shortening an explanation helps only if the remaining steps still carry the information needed to solve the problem correctly.

*Source cue (not spoken): PDF pp.1–2, Fig.1; p.8, Fig.3*

## Slide 03 — Three training stages turn sketches into a policy

Part I · 01:28–02:21 · 115 words · 53.1 seconds

The framework has three stages, each with a different job. Cold start teaches the answering model to imitate compressed reasoning traces. A separate SketchJudge then learns to distinguish sketch-style thinking from detailed thinking. Finally, reinforcement learning uses that judge alongside accuracy and format rewards. Cold start supplies examples, the judge supplies a score, and reinforcement learning applies the behavior to new visual questions across visual domains. The answering model receives the image and question. The judge receives only the thinking text. That difference becomes central to our analysis later. The original pipeline appears below the simplified redraw. Together, they show how data preparation, reward modeling, and policy training connect to produce the final sketch-generating model.

*Source cue (not spoken): PDF p.3, Fig.2; §§2.1–2.3*

## Slide 04 — Cold start teaches the model what a sketch looks like

Part I · 02:21–03:18 · 125 words · 57.7 seconds

For cold start, the authors build SketchColdStart-20K from two existing datasets. They sample ten thousand questions from LLaVA-CoT-100K and ten thousand from Vision-R1-cold. GPT-5 rewrites the long traces into short numbered steps. The conversion prompt receives the reasoning alone and asks it to preserve key facts, logic, and order while removing extra detail. These rewritten examples then supervise the multimodal policy through supervised next-token training. The default backbone is Qwen2.5-VL-7B-Instruct, with a smaller three billion parameter version also evaluated. Rewriting changes both length and content. The converter ablation shows that the teacher matters, but it does not separate shortening from corrections, omissions, or phrasing changes. Our later reward comparison therefore holds the rewritten data and cold-start weights fixed across all four principal experimental arms.

*Source cue (not spoken): PDF p.5, §3; p.14, App.D.1; p.21, Table16*

## Slide 05 — SketchJudge rewards a textual style

Part I · 03:18–04:16 · 125 words · 57.7 seconds

SketchJudge uses Qwen2.5-7B-Instruct, a language model. Each original long trace receives label zero, and its rewritten sketch receives label one. That produces forty thousand labeled traces. During reinforcement learning, the judge applies the same style prompt to generated thinking text. It sees neither the image nor the question. Answer accuracy is scored separately. This makes the supervision target clear: learn the style of concise reasoning without imposing one fixed length. A demanding question can still receive a longer sketch. The open issue is whether the score recognizes missing support. A trace can state correct calculations and look concise while leaving an essential visual premise unstated. We will use that distinction between style and explicit support to frame the first limitation and our proposed experiment.

*Source cue (not spoken): PDF p.4, §2.2; p.14, App.D.2; p.7, Table3d*

## Slide 06 — RL balances correctness, format, and thinking style

Part I · 04:16–05:21 · 140 words · 64.6 seconds

The reinforcement learning stage uses GRPO to compare responses sampled for the same question. The paper uses five rollouts per group. Each response receives zero point five for accuracy, zero point four for format, and zero point one for thinking style. The style score is binary. A correct answer that passes format and style receives a total reward of one. A wrong answer that passes those two checks receives zero point five. These examples apply the reward equation. GRPO centers and scales the group rewards to obtain relative advantages, then uses a clipped policy update to favor stronger responses. A KL penalty anchors the policy to its reference. The default objective has no explicit token penalty. Compression comes through the examples and style signal, so the reward does not directly test whether every necessary visual premise remains in the trace.

*Source cue (not spoken): PDF p.4, Eqs.2–6; p.5, §3*

## Slide 07 — Evaluate answer quality and reasoning cost separately

Part I · 05:21–06:14 · 115 words · 53.1 seconds

Evaluation covers MMMU, MathVision, VisuLogic, and PhyX: broad reasoning, visual mathematics, visual logic, and physics. MathVision is the paper's name for MATH-Vision. The reinforcement learning set contains two hundred fifty questions from each of MMStar, MathVista, LogicVista, and SeePhys, giving one thousand examples. The trainable baselines share source questions, with different trace-construction methods. Comparisons include prompting, supervised training, and length-oriented reinforcement learning. The main evaluation measurements are answer accuracy and average reasoning tokens. Efficiency of Thinking divides accuracy by token count. That ratio rewards brevity, but it can rise when accuracy falls. I will therefore keep the two measurements separate and read each efficiency claim alongside its corresponding accuracy comparison throughout the results that follow.

*Source cue (not spoken): PDF p.5, §3; p.6, Tables1–2*

## Slide 08 — At 7B, tokens fall sharply across all four benchmarks

Part I · 06:14–07:16 · 135 words · 62.3 seconds

Table one gives the strongest evidence for the headline. At seven billion parameters, MMMU accuracy rises from sixty one to sixty two point eight percent. Average reasoning tokens fall from one hundred eighty two point two to sixty four point three. Across all four benchmarks, the recomputed token reductions range from sixty four point seven to seventy six point five percent. Accuracy increases in each comparison, with gains ranging from zero point two points on VisuLogic to one point nine on PhyX. The plot shows reasoning token counts, and the table preserves accuracy beside them. One useful boundary is that Constrained CoT uses fewer tokens on PhyX: seventy three point four versus seventy five point three. The sketch method combines strong compression with better accuracy, rather than attaining the shortest output in every listed comparison.

*Source cue (not spoken): PDF p.6, Table1; reductions computed from table entries*

## Slide 09 — On MMMU, the 7B model improves both axes

Part I · 07:16–08:09 · 115 words · 53.1 seconds

This plot puts the MMMU operating points on common axes. Left means fewer reasoning tokens; up means higher accuracy. SketchThinker-R1 sits above and to the left of the listed baselines. Prompting shortens responses but loses accuracy relative to Vanilla-R1. Supervised methods and length-oriented reinforcement learning occupy intermediate positions. The full pipeline therefore improves both reported measurements here. To compare accuracy and cost frontiers, we would also need matched budget sweeps, tuning effort, and measured training compute. The paper reports operating points without repeated-training intervals. That matters especially for small accuracy differences. Our own experiment will compare achieved lengths and show seed variation separately from uncertainty caused by sampling different problem families from the evaluation population.

*Source cue (not spoken): PDF p.6, Table1, MMMU columns*

## Slide 10 — Stage ablations leave the reward effect unresolved

Part I · 08:09–09:07 · 125 words · 57.7 seconds

The ablations support combining cold start with reinforcement learning. On MMMU, cold start alone reaches sixty one point four percent with one hundred fourteen point five tokens. Reinforcement learning alone reaches sixty two point one percent with one hundred fifty two point two tokens. Together they reach sixty two point eight percent with sixty four point three tokens. Judge fine-tuning also helps. The appendix tests reward schedules, scaling, and a tuned long-trace cold-start baseline. These are meaningful experimental controls. The remaining attribution test removes style reward while keeping the compressed cold-start weights and other RL conditions fixed. Likewise, the cold-start quality audit checks preserved key steps, but learned-policy sufficiency needs its own independent evaluation. That leads to five specific limitations and the experiments they motivate.

*Source cue (not spoken): PDF p.7, Tables3a/3b/3d; pp.16–17, Tables5–8; p.19, Table14*

## Slide 11 — Five limitations define the next tests

Part I · 09:07–10:18 · 155 words · 71.5 seconds

The first limitation is reward validity. SketchJudge scores text style, while Appendix H checks cold-start preservation. Neither directly measures missing visual support in the learned policy's outputs. Second is attribution: we still need the incremental effect of style reward under shared cold-start weights and RL conditions. Third is the accuracy tradeoff. At three billion parameters, MathVision accuracy drops from twenty six point nine to twenty five point three percent. Difficulty groups, repeated training, and a disjoint selection split deserve attention. Fourth is transfer. Results cover one backbone family at two scales; longer deliberation and other families need testing. Fifth is full cost and reproduction. Appendix J reports timing, but a unified ledger must include preparation and judge costs. Batch size is reported as one hundred twenty eight versus five hundred twelve, and hardware as eight H200 versus eight H800. These gaps point to targeted follow-up experiments rather than a rejection of the demonstrated token savings.

*Source cue (not spoken): Revised analysis L1–L5; paper §2.2, Tables1–3/7–15, App.D.3–J*

## Slide 12 — Three directions target different interventions

Part I · 10:18–11:12 · 115 words · 53.1 seconds

Three directions follow from those gaps. Direction one changes what we reward: preserve explicit visual support, including premises a short trace leaves out. Existing multimodal process reward models already check steps; the new comparison asks whether detecting omissions adds value. Direction two changes how we allocate inference compute. An image-conditioned router would choose budgets while constraining accuracy loss in prespecified difficulty and visual-dependency groups. Direction three changes how we attribute training gains and count costs. Cross trace construction with style reward, then calculate when inference savings repay preparation and training. These directions address supervision, allocation, and lifecycle efficiency. We choose the first because omission-sensitive judgment can be tested directly before fully committing to policy training.

*Source cue (not spoken): Revised analysis Directions 1–3; process supervision and budget-control primary sources linked there*

## Slide 13 — Probe D1: does omission detection add value?

Part I · 11:12–12:00 · 105 words · 48.5 seconds

The probing question is whether omission-sensitive supervision improves accuracy and explicit support at matched length and compute. Start with paired judge examples: a complete trace, a correct-answer trace missing a visual premise, and a harmless redundant-step deletion. Keep their length and format comparable. A useful judge must reject the missing support and accept the valid compression. Then compare sufficiency against style, stated-step correctness, and zero auxiliary reward. Independent human evaluation includes wrong answers and alternative proofs. Checked image pairs test both-correct answers and valid support, with nuisance edits checking invariance. That sequence turns the supervision gap into a measurable experiment, which I will now pitch.

*Source cue (not spoken): Revised analysis §3, Direction 1; HTML plan, Proposed Solution*

## Slide 14 — Pitch: preserve the evidence behind an answer

Part II · 12:00–13:00 · 130 words · 60.0 seconds

Our plan is called Preserving Visual Evidence in Compressed Multimodal Reasoning. A sufficient trace must explicitly state correct visual premises and valid deductions supporting its returned answer. Here, the triangle has two angle labels visible only in the image. Reading forty and sixty degrees, then applying the triangle sum, supports eighty degrees. If the trace silently imports those readings, its arithmetic can be correct while its support is incomplete. The image checks stated facts; it does not fill omissions. We accept validated complete alternative proofs and allow redundant steps to disappear. The sufficiency judge learns from supported traces, premise deletions with correct answers, false readings, invalid deductions, and harmless redundant-step deletions. A stated-step correctness judge receives exactly the same inputs, making completeness the key experimental difference between their supervision targets.

*Source cue (not spoken): HTML plan; revised analysis, Direction 1; illustrative geometry example*

## Slide 15 — Four rewards share data, initialization, and compute

Part II · 13:00–14:00 · 130 words · 60.0 seconds

We will render three thousand geometry and bar-chart problems, split by template family into sixteen hundred training, four hundred development, and one thousand test problems. Four arms share compressed cold-start data and Qwen2.5-VL-7B weights: sufficiency, style, stated-step correctness, and zero auxiliary reward. Each uses three seeds and one shared budget-conditioned policy targeting sixty four, one hundred twenty eight, and two hundred fifty six tokens. Achieved means must match within five percent, and training compute includes rollouts and judge scoring. Two annotators audit three hundred test problems across every arm and seed, including wrong answers. Two hundred answer-changing pairs and one hundred nuisance pairs test visual robustness. Separate ablations remove judge image access and omission-negative training. Long reasoning and direct answers provide reference points for interpreting both accuracy and compression.

*Source cue (not spoken): Revised analysis, Direction 1: data, setup, controls and ablations*

## Slide 16 — Gate first; test useful gains within the compute cap

Part II · 14:00–15:00 · 130 words · 60.0 seconds

We begin with frozen-policy judge diagnostics and a measured throughput pilot. Before policy training, development false acceptance must be at most ten percent, with sufficient-trace recall at least seventy percent. Near one hundred twenty eight achieved tokens, success requires three percentage points more accuracy and five points more human sufficiency than style supervision, with both paired confidence intervals above zero. We report family-clustered uncertainty and each seed's effect. Two eighty-gigabyte accelerators support a four hundred accelerator-hour cap: twelve principal runs at twenty five hours, plus one hundred hours for shared preparation, judges, selection, evaluation, and ablations. If throughput falls short, we reduce data or steps equally while retaining seeds and the primary contrast. The outcome will show when explicit-support supervision improves compressed reasoning and when it offers no useful advantage.

*Source cue (not spoken): Revised analysis, Direction 1: judge gate, success criterion and compute*

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
| 11 | I | 155 | 09:07–10:18 |
| 12 | I | 115 | 10:18–11:12 |
| 13 | I | 105 | 11:12–12:00 |
| 14 | II | 130 | 12:00–13:00 |
| 15 | II | 130 | 13:00–14:00 |
| 16 | II | 130 | 14:00–15:00 |
| **Part I** | | **1,560** | **12:00** |
| **Part II** | | **390** | **3:00** |
| **Total** | | **1,950** | **15:00** |
