# Evidence table
| Claim | Source | Strength/status | Section | Risk/control |
|---|---|---|---|---|
| Style judge lacks image and question | https://arxiv.org/html/2601.02825v1 §2.2 | evidence-backed | Introduction/Related Work | distinguish answering model |
| Reward has accuracy, format and style | same, Eq. 5 | evidence-backed | Related Work | give all components |
| 3B MATH-Vision decreases 26.9 to 25.3 | same, Table 2 | evidence-backed | Introduction | no causal or universal inference |
| Rewriting might explain part of gains | same, §3 and converter ablation | hypothesis | Related Work/Experiments | identical-data reward contrast; separate rewrite controls |
| Concise traces may omit necessary visual facts | merged plan; to be tested | hypothesis | Introduction/Expected Results | count visual and nonvisual deletion rates separately |
| Evidence reward improves tradeoff | merged plan | hypothesis | Abstract/Expected Results | matched achieved average tokens and compute |
| Paired edits alone establish harmful deletion | external review rejects this | unsupported; forbidden | none | assess independent sufficiency, regenerate traces, nuisance edits |
| Correct answers establish sufficiency | external review rejects this | unsupported; forbidden | none | premise/deduction rubric and human-held-out validation |
| Benchmark/model/method context | verified arXiv records in reference audit | evidence-backed | Related Work/Experiments | no unsupported numerical performance claims |

## Audit evidence and design updates (2026-10-22)
The earlier audit verified SketchRL-1K MathVista exposure and the paper's five-rollout setting (§3). The current protocol fixes shared rollout settings after a throughput pilot. The current compute arithmetic is four arms ×three seeds =12 runs; 12×25+100 =400 accelerator-hours. This is a proposed ceiling, not measured throughput.

## Synchronization evidence (2026-10-23)

| Claim / choice | Authority and locator | Disposition |
|---|---|---|
| Cold-start key-step evaluation exists: 19,182 preserved / 818 missing | Supplied paper text, Appendix H, Table 14 | Acknowledge; restrict gap to training-time reward and learned-policy sufficiency |
| Stage/judge/schedule/long-trace controls exist | Tables 3, 7, 8; Appendix D.4 | Acknowledge; isolate shared-initialization reward contrast |
| Correct stated steps can omit required support | HTML plan, Problem Statement / Proposed Solution | Operational motivation, tested through deletion negatives and stated-step baseline |
| Data, reward arms, seed count, judge gate, success margins, cap | Revised analysis, Probing / Direction 1 | Planned design; synchronized across proposal, slides 13–16 and scripts |
| VisualPRM multimodal process-supervision precedent | arXiv:2503.10291; ICLR 2026 VisualPRM400K proceedings | Verified title/version mapping in reference audit |

Paper numeric checks are reproducible in `docs/presentation/build_presentation.py` and `output/number-verification.json`. No proposed number is presented as a paper result.
