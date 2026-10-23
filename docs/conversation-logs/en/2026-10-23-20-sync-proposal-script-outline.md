# Sync proposal and speaker script with the revised plan; slide outline

[中文版](../zh/2026-10-23-20-sync-proposal-script-outline.md)

Date: 2026-10-23. Status: PR open on branch [sync-proposal-ppt](https://github.com/Lc-wing/machine_learning_project/tree/sync-proposal-ppt); merged in [PR #12](https://github.com/Lc-wing/machine_learning_project/pull/12).

## Request

Bring the formal research proposal and the presentation in line with the revised one-page plan (`docs/research-plan/sketch-sufficiency.html`) and the revised paper analysis. Mid-task the scope changed: finish the proposal and speaker script, and replace the slide rebuild with a slide-by-slide outline. Upload results to Google Drive.

## Result

- `docs/research-proposal/sketch-sufficiency-proposal.tex/.pdf`: rewritten for D1 (image-aware sufficiency reward). 3,000 geometry/bar-chart problems split 1,600/400/1,000 by template family; four reward arms (sufficiency, style, stated-step correctness, zero auxiliary); Qwen2.5-VL-7B; three seeds; one budget-conditioned policy (64/128/256 tokens); judge gate (false acceptance ≤ 10%, recall ≥ 70%); success near 128 tokens is +3 points accuracy and +5 points human sufficiency over style; 400 GPU-hour cap (12 runs × 25 h + 100 h). VisualPRM ([arXiv:2503.10291](https://arxiv.org/abs/2503.10291)) added as reference 13. Notes 00–06 updated.
- `docs/presentation/speaker-script.md/.docx` and `talk-content.json`: slides 11–13 follow the revised limitations L1–L5, three directions and the D1 probe; slides 14–16 pitch the new plan. Slide 1 unchanged. 1,947 spoken words, 15:00 at 130 wpm (Part I 12:00, Part II 3:00).
- `docs/presentation/slide-outline.md`: new 16-slide outline (title, key points, visual, timing). The `.pptx`, builder, figures and output files stay at the `main` versions; the deck has not been rebuilt.

## Verification

`pdflatex` build: 5 pages (4-page body plus a references page). No `2,400`, "three arms" or per-budget wording remains in the proposal or script. Paper numbers (e.g. 61.0→62.8, 182.2→64.3, MathVision 26.9→25.3 at 3B) checked against `docs/presentation/paper/2601.02825.txt`.
