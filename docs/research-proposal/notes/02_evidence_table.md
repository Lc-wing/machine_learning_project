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
The supplied `/workspace/codex-audit-recheck.md` is the revision brief. It verifies SketchRL-1K MathVista exposure and the source's five-rollout setting against https://arxiv.org/html/2601.02825v1 (§3). Our four-rollout groups are a compute choice. Venue additions follow the report's verified publication records; all preprint author lists, titles, and years remain unchanged. The prospective 9K-run and 2,880u GPU-hour capacity calculations are planning arithmetic, not measured throughput.
