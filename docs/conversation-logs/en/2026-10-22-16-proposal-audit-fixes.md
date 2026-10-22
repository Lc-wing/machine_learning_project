# 16 Proposal audit fixes

Chinese version: [中文](../zh/2026-10-22-16-proposal-audit-fixes.md)

- Date: 2026-10-22
- Status: completed locally on `proposal-fixes`; no commit or push.
- Request: apply audit findings 1–12 and 14 plus M1–M5, optionally 13; preserve preprint authors, tighten hedging, keep the body within four pages, rebuild with pdflatex, and add bilingual session records.

Updated [LaTeX](../../research-proposal/sketch-sufficiency-proposal.tex) and [PDF](../../research-proposal/sketch-sufficiency-proposal.pdf), using `/workspace/codex-audit-recheck.md` as the revision brief and researchwrite revision guidance. Supporting canon, evidence, and validation notes were refreshed.

| Finding | Change |
|---|---|
| 1 | Maximize sufficiency over reviewer-validated graphs with graph-specific coverage. |
| 2 | Exclude benchmarks from new training/selection; audit item overlap for released SketchThinker-R1 MathVista comparisons. |
| 3 | Add 9K runs (up to 36), 2,880u GPU-hours/month, 80u hours/run before overhead, pilot accounting, and scope reduction. |
| 4 | Identify Vanilla-R1-3B and the 1.6 percentage-point MATH-Vision decrease. |
| 5 | Explain four rollouts versus the source's five as a compute choice. |
| 6 | Match binary auxiliary reward support and coefficient; isolate probability reward as an ablation. |
| 7 | Measure semantic omission; separate grounding errors, invalid steps, and valid proof changes. |
| 8 | Include encoding, prefill, reasoning decoding, and final-answer decoding in latency. |
| 9 | Explain why a fixed reward coefficient does not fix trace length. |
| 10 | Reference the pipeline, reward, experiment table, and labeled timeline. |
| 11 | Append six conference venues and DeepSeek-R1's Nature publication; preserve all preprint metadata and author lists, including MATH-Vision. |
| 12 | Standardize MATH-Vision naming. |
| 13 | Apply optional binary D(z) cleanup with graph-specific validity. |
| 14 | Add the separate SketchThinker-R1-7B checkpoint baseline. |
| M1 | Bind the supported trace conclusion to the returned answer; count all explanation tokens. |
| M2 | Define atomic units, empty-category handling, counts, and macro-aggregation. |
| M3 | Extract normalized binary label-token probability and calibrate on development data. |
| M4 | Stabilize group advantages with epsilon and zero advantages for equal rewards. |
| M5 | Use the exact same zero-component reward for compressed, original, and length-preserving controls. |

Removed repetitive caveats and tightened prose without turning hypotheses into findings. Retained 11pt type and one-inch Letter margins. Final pdflatex passes ran from `docs/research-proposal`; no BibTeX is needed. Checks confirm five total pages, References starting on page 5, 12 resolved citations, unchanged preprint author lists/titles/years, zero LaTeX warnings, and zero overfull boxes. Rendered method, experiment, and timeline pages were inspected. Build auxiliaries were removed; the final log is in `/tmp/proposal-audit-final.log`. No experiments were run. Both language indexes include this record.
