# Research canon
The merged HTML plan governs scope; older discussion logs are background, not verified scientific evidence. The external review corrects the earlier counterfactual inference.

- SketchThinker-R1's SketchJudge sees only the thinking text, neither image nor question (§2.2).
- Its default total reward is 0.5 accuracy + 0.4 format + 0.1 thinking style (§2.3).
- Table 2 reports MATH-Vision accuracy 26.9 for Vanilla-R1 and 25.3 for SketchThinker-R1 at 3B. This is one reported comparison, not evidence of a universal effect.
- GPT-5 trace rewriting is reported; its causal contribution to gains remains a hypothesis. A length-preserving rewrite can change content.
- A fixed reward coefficient does not impose identical output lengths. Appendix E includes other schedules.
- Correctness, explicit explanation sufficiency, and causal faithfulness are distinct. Only the first two are targets.
- Necessary premises are relative to an admissible checked derivation; alternative derivations must be accepted. Redundant visual statements may be removed.
- One 7B answering model; a separate smaller judge is an implementation component. Difficulty is an evaluation stratum, not a proposed deployment gate.

## Terminology ledger
| Canonical term | Meaning |
|---|---|
| evidence-preserving compression | shortening while retaining premises and valid support |
| explanation sufficiency | explicit supported derivation, not latent computation |
| necessary-premise retention (NPR) | fraction of annotated required visual premises explicitly retained |
| paired-image correctness | both members answered correctly |
| GRPO | Group Relative Policy Optimization |
| MATH-Vision | canonical dataset name |
| I, q, z, a, L(z), B | image, question, trace, answer, trace token count, target budget |

All new sample sizes, thresholds and training choices in the proposal are planned design choices, not existing evidence or confirmed resources.

## Audit revision (2026-10-22)
- Sufficiency maximizes over reviewer-validated derivations, with graph-indexed coverage and a binary validity check bound to the returned answer. Empty categories have coverage 1; category summaries exclude them and macro-average.
- RQ1 measures semantic omission of originally correct necessary units within retained derivations, separately from grounding errors and valid proof changes.
- Principal sufficiency, style, and stated-step correctness rewards are binary with coefficient 0.1. The zero-auxiliary arm retains 0.5 accuracy and 0.4 format without renormalization. All four share compressed cold-start data and initialization.
- SketchRL-1K contains MathVista questions (SketchThinker-R1 v1, §3); released-checkpoint MathVista comparisons require an item-level overlap audit.

## Current protocol (2026-10-23)

- Source authority: revised HTML plan, revised English paper analysis, and skill-review notes. The analysis supplies numerical protocol detail omitted from the compact HTML.
- Render 3,000 geometry/bar-chart problems; family split 1,600 training / 400 development / 1,000 test before traces or variants.
- Two annotators audit 300 test problems across all four arms and three seeds, retaining wrong answers and valid alternative derivations.
- Qwen2.5-VL-7B-Instruct policy; judges initialized from Qwen2.5-VL-3B. Sufficiency and stated-step judges share image/question/trace/returned-answer inputs; style sees trace alone; gold answers withheld from judge scoring.
- Judge gate: development false acceptance ≤10% and sufficient recall ≥70%, before RL.
- One budget-conditioned policy per arm/seed; target 64/128/256 tokens; achieved means within 5%; measured training compute includes rollouts and judge scoring; fixed-rollout sensitivity.
- Primary success near 128 achieved tokens: sufficiency versus style ≥3 accuracy points and ≥5 human-sufficiency points, both paired 95% intervals above zero. Cluster by original problem family; report individual seed effects and range separately.
- Independently checked 200 answer-changing and 100 nuisance pairs. Separate image-access and omission-negative-training ablations.
- Two 80GB accelerators; 12 principal runs ×25 accelerator-hours +100 shared hours =400 total. All occupied devices count; reduce data/steps equally after throughput pilot, retaining seeds and primary contrast.
- Paper labels use MathVision; MATH-Vision remains the dataset's formal name. VisualPRM and Let's Verify Step by Step position correctness supervision; omission-sensitive completeness is the discriminating target.
