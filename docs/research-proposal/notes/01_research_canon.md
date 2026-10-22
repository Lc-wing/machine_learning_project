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
- Principal evidence and style rewards are binary with coefficient 0.1; rewriting controls share the exact zero-component objective.
- SketchRL-1K contains MathVista questions (SketchThinker-R1 v1, §3); released-checkpoint MathVista comparisons require an item-level overlap audit.
