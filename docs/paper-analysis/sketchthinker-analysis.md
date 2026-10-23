# SketchThinker-R1: methodological analysis and research directions

[中文版](sketchthinker-analysis.zh.md) · Reviewed 2026-10-23 · [Review notes and skill attribution](notes/skill-review.md)

Ruiyang Zhang, Dongzhan Zhou, and Zhedong Zheng. **SketchThinker-R1: Towards Efficient Sketch-Style Reasoning in Large Multimodal Models.** ICLR 2026. [Proceedings](https://proceedings.iclr.cc/paper_files/paper/2026/hash/a1f0c0cd6caaa4863af5f12608edf63e-Abstract-Conference.html); [arXiv](https://arxiv.org/abs/2601.02825). References use the supplied [paper text](../presentation/paper/2601.02825.txt), including appendices.

## 1. Critical Analysis: What are the primary limitations or potential weaknesses of the methodology presented in this paper?

The complete pipeline substantially reduces reasoning tokens. The central questions concern reward validity, attribution, accuracy across difficulty groups, transfer, and full deployment cost.

### L1. Style supervision leaves visual-support sufficiency unmeasured

SketchJudge receives reasoning text alone and distinguishes original traces from rewritten sketches (§2.2; Appendix D.2). The conversion prompt likewise receives reasoning alone (Appendix A, Table 16). Length, numbering, and rewrite artifacts offer potential shortcuts around evaluating necessary visual premises. The answering policy receives image/question inputs, and Eq. 5 combines **0.5 accuracy + 0.4 format + 0.1 style**.

Appendix H checks cold-start key-step preservation through human ratings and a full-dataset evaluator: **19,182** sketches preserve key steps and **818** miss them (Table 14). Appendix G assesses interpretability. The remaining test concerns missing or false visual premises in learned-policy outputs, including wrong answers, and whether the reward detects them.

### L2. Style reward needs a controlled incremental-effect test

Tables 3a and 3d ablate training stages and judge fine-tuning/size. Tables 5–6 vary positive style weights. The missing contrast removes style reward while holding sketch cold-start weights and RL conditions fixed. Converter sensitivity in Table 3b also calls for an audit of information, errors, phrasing, and teacher contributions.

Appendix D.4 shares source questions across trainable baselines; Table 8 includes long-trace cold start followed by tuned RL. Extend these controls by crossing trace construction with reward choice, matching initialization, tuning effort, and measured compute. Audit length-preserving rewrites for content changes.

### L3. Aggregate efficiency hides accuracy and allocation tradeoffs

Table 1 reports these 7B differences from Vanilla-R1:

| Benchmark | Vanilla-R1 reasoning tokens | Sketch reasoning tokens | Token reduction, recomputed | Accuracy difference, percentage points |
|---|---:|---:|---:|---:|
| MMMU | 182.2 | 64.3 | 64.71% | +1.8 |
| MathVision | 221.1 | 65.5 | 70.38% | +0.7 |
| VisuLogic | 240.0 | 56.3 | 76.54% | +0.2 |
| PhyX | 225.1 | 75.3 | 66.55% | +1.9 |

At 3B, MathVision accuracy falls from **26.9 to 25.3**, a **1.6-percentage-point** loss (Table 2). On 7B PhyX, Constrained CoT uses fewer tokens (**73.4 versus 75.3**). EoT, accuracy divided by mean reasoning tokens (§3), favors brevity; accuracy–cost curves and accuracy floors expose the tradeoff more clearly.

Repeated-training uncertainty, paired evaluation details, and noninferiority analysis remain missing. Appendix E tests staged/dynamic reward schedules (Table 7); difficulty-conditioned allocation and subgroup losses remain open. MMMU serves ablation and default selection without a documented disjoint selection split, leaving selection bias unresolved.

### L4. Transfer across reasoning regimes and model families needs testing

Tables 1–2 cover Qwen2.5-VL at **3B and 7B**. The 7B means above describe relatively short traces; tail behavior and extended deliberation require separate evaluation. Appendix F scales RL data and steps (Tables 9–10), within MMMU and the same backbone family. Broader transfer tests should vary visual dependencies, reasoning lengths, and model families.

### L5. Reproduction and full-cost accounting need a unified ledger

Appendix J reports inference and training timing (Figure 11; Table 15). Extend this to rewriting, cold-start SFT, judge training/scoring, RL, image processing, and serving conditions. Vision encoding and prefill can dominate deployment cost despite shorter reasoning. Reconcile rollout batch size **128** in §3 with **512** in Appendix D.3, and **eight H200** GPUs in §3 with **eight H800** in Appendix J.

## 2. Brainstorming: Given these limitations, suggest three distinct future research directions that could address them.

### Direction 1. Learn compression that preserves explicit visual support

**Addresses L1, with L2 controls; chosen for the one-page plan.** Train a reward that distinguishes complete short derivations from equally concise traces missing necessary premises. Correct stated steps can still leave required support unstated.

[Let's Verify Step by Step](https://arxiv.org/abs/2305.20050), [VisualPRM](https://arxiv.org/abs/2503.10291), and [GM-PRM](https://arxiv.org/abs/2508.04088) provide process-supervision precedents; [Look and Think](https://aclanthology.org/2026.findings-acl.1241/) studies grounding and multimodal compression. Extend log 11's process-reward direction with omission detection at matched achieved lengths, correct-answer-but-incomplete negatives, and valid alternative derivations.

### Direction 2. Allocate reasoning budget with subgroup accuracy constraints

**Addresses L3–L4.** Learn input-conditioned budgets while bounding accuracy loss in prespecified difficulty and visual-dependency groups. This yields an allocation rule and a boundary of useful compression.

Log 11's controllable budgets, [L1](https://arxiv.org/abs/2503.04697), and [TokenSkip](https://arxiv.org/abs/2502.12067) address length control. [AdaptThink](https://arxiv.org/abs/2505.13417) and [DualMindVLM](https://arxiv.org/abs/2511.16670) address adaptive thinking and VLM fast/slow selection. Test the added value of subgroup constraints against these simpler policies.

### Direction 3. Identify training interventions that improve lifecycle efficiency

**Addresses L2 and L5.** Cross cold-start trace construction with style reward, then measure when inference savings repay preparation and training costs. Extend Table 8 with factorial attribution, content audits, and a full-cost frontier.

Keep explicit-text architecture fixed to isolate these interventions. Log 11's latent-reasoning direction and [Coconut](https://arxiv.org/abs/2412.06769) instead change representation, answering a separate research question.

## 3. Probing: For [Direction 1], what would be a potential research question? What kind of experiment could validate this idea?

### Shared experimental rules

Split by problem/template family before generating traces or image variants. Reserve public tests for transfer; record checkpoint exposure. Freeze resolution, prompts, parser, decoding, and tuning allowance; count parser failures as wrong and all explanation before the final answer as reasoning. Retain wrong answers in trace evaluation. Use the paper's MathVision name for MATH-Vision.

Use **three training seeds**, per-seed effects, paired **95%** intervals clustered by original problem family, and the seed-effect range. Prespecify primary contrasts and adjust secondary comparisons for multiplicity. Pilot paired/clustered precision and throughput before freezing protocols. Intervals spanning useful gains and losses leave the result unresolved. The following datasets, thresholds, and resource caps define the proposed experiments.

### Direction 1: image-grounded sufficiency supervision

**Question and data.** At matched reasoning length and training compute, does omission-sensitive supervision improve accuracy and explicit support beyond style and stated-step correctness rewards? Render **3,000** geometry/bar-chart problems: **1,600 training, 400 development, 1,000 test**, split by template family. Two annotators audit **300 test problems**, adjudicate alternative derivations, and blindly score every primary arm/seed, including wrong answers. A sufficient trace explicitly supplies correct visual premises and valid deductions supporting its returned answer.

**Setup.** Share compressed SFT data and Qwen2.5-VL-7B-Instruct cold-start weights across **sufficiency, style, stated-step correctness, and zero auxiliary reward** arms. Retain accuracy/format weights; use **0.1** for binary auxiliary rewards and zero without renormalization. Initialize judges from Qwen2.5-VL-3B. Sufficiency and stated-step judges receive identical image/question/trace/returned-answer inputs; style receives trace alone. Withhold gold answers during scoring. Match measured training accelerator-hours, including rollouts and judge inference; add fixed-rollout sensitivity checks. Common budget conditioning and length penalties target **64, 128, 256 tokens**, matching achieved means within **5%**. Include long reasoning and direct-answer references.

**Controls and ablations.** Match format/length across complete traces, correct-answer premise deletions, false readings, invalid deductions, redundant deletions, and alternative proofs. Require development false acceptance ≤**10%** and sufficient-trace recall ≥**70%** before RL. Test unseen templates; separately remove judge images and omission-negative training. Independently construct **200 answer-changing and 100 nuisance-edit pairs**; regenerate both traces and score both-correct answers and valid support. Accept wording valid for both images.

**Success criterion and metrics.** Near **128 achieved tokens**, require sufficiency versus style gains of **3 percentage points** in accuracy and **5 points** in human sufficiency, with both paired intervals above zero. Report necessary visual/nonvisual premise retention, grounding errors, valid proof changes, pair correctness, nuisance invariance, judge false acceptance, and end-to-end latency. Report empty unit-category counts. Compare image-blind and stated-step controls against the useful-effect threshold to test the proposed mechanisms.

**Compute.** Begin with judge and frozen-policy diagnostics. Use LoRA on two **80GB** accelerators, capped at **400 accelerator-hours**: **12 principal runs × 25 hours = 300**, plus **100** for judges, selection, and ablations. Pilot throughput; reduce data/steps equally if needed while retaining seeds and the primary contrast.

### Direction 2: subgroup-constrained budget allocation

**Question and setup.** Can a router save reasoning cost while limiting every group's accuracy loss to **2 percentage points**? Use the rendered split above, prespecified derivation-depth/visual-dependency groups, and the full MathVision test for transfer. Cache **64, 128, 256, 512, 1,024, 2,048-token** budget–outcome curves on a frozen 7B policy; measure realized lengths. Fit on training curves and select on development data. The router receives image/question features only.

**Baselines and ablations.** Compare direct answers, fixed budgets, prompt-only length control, a DualMindVLM-inspired fast/slow router, and an average-accuracy router. Use an outcome-aware oracle as an upper bound. Match achieved cost and freeze other settings. Remove subgroup constraints and visual features separately; shuffle budget assignments while preserving frequencies.

**Success criterion and metrics.** Require **20%** mean token savings against the long-budget reference, simultaneous group accuracy lower bounds above **−2 points**, and lower worst-group loss than the average-accuracy router at matched cost. Prespecify the smallest/deepest groups. Report group accuracy/cost, violations, accuracy–cost curves, and latency including routing. Flat or nonmonotonic difficulty effects remain reportable outcomes.

**Compute.** Cap cached curves, router fitting, and transfer inference at **80 accelerator-hours** on one **80GB** GPU. Pilot the longest budget first; reduce explored operating points before test access if needed.

### Direction 3: factorial attribution and deployment break-even

**Question and design.** What incremental frontier benefit does style reward deliver after each cold-start intervention, and when does it repay its cost? Cross **three trace conditions** (original long, same-rewriter length-preserving, same-rewriter sketches) with **style present/absent**, producing **six cells**. Fix Qwen2.5-VL-7B-Instruct, source questions, splits, other reward coefficients, budget mechanism, decoding, and tuning effort. Audit rewrite additions, corrections, omissions, and lengths. Test rendered held-out families and MathVision; reserve MathVista pending overlap auditing because §3 draws RL data from it.

**Baselines and measurements.** Include direct answering, the default paper pipeline, and tuned length reward. Estimate within-condition reward effects and interactions; reuse compatible Direction 1 cells. Measure accuracy, achieved tokens, latency, and preparation costs. Randomize warmed-up timing order; fix hardware/software, batching, and resolution, then vary visual-token load and batching. Include rewriting, SFT, judges, and rollouts; record API spending separately from accelerator-hours. On a common accounting basis, calculate **ΔC(N) = ΔC_prepare + N × ΔC_query** and break-even volume when signs permit.

**Success criterion.** For a prespecified workload and matched training-compute ceiling, require **10%** lower end-to-end latency with the paired accuracy interval above **−2 percentage points**. Report lifecycle savings and break-even separately. Intervals ruling out this useful frontier gain reject the added reward's practical value for that workload.

**Compute.** Use LoRA and **three seeds per cell**, capped at **500 accelerator-hours** on two **80GB** GPUs: **18 runs × 20 hours = 360**, plus **140** for preparation, judges, tuning, timing, and ablations. Pilot feasible data/step counts and share compatible runs/caches. Each direction has its own project budget.
