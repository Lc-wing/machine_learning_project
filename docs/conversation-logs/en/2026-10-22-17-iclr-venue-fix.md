# 17 SketchThinker-R1 venue correction: ICLR 2026

Chinese version: [中文](../zh/2026-10-22-17-iclr-venue-fix.md)

- Date: 2026-10-22
- Status: branch [`iclr-venue-fix`](https://github.com/Lc-wing/machine_learning_project/tree/iclr-venue-fix); [PR #9](https://github.com/Lc-wing/machine_learning_project/pull/9) open, not merged.
- Request: SketchThinker-R1 (Zhang, Zhou, Zheng; arXiv:2601.02825) was published at ICLR 2026 as a poster ([OpenReview](https://openreview.net/forum?id=ZSMDuKtYbt), [proceedings PDF](https://proceedings.iclr.cc/paper_files/paper/2026/file/a1f0c0cd6caaa4863af5f12608edf63e-Paper-Conference.pdf)). Earlier work treated it as arXiv-only; fix every instance, rebuild outputs, and check whether any number used differs.

Result: every arXiv-only or preprint framing of the paper now says ICLR 2026. The proceedings version matches arXiv v1 in every number used, so no number changed.

- Presentation (`docs/presentation/`, added in this PR): cover venue line `ICLR 2026` in `build_presentation.py`; slide 1 script "This is an arXiv 2026 preprint." became "This is an ICLR 2026 poster." in `talk-content.json`, the slide notes, `speaker-script.md` and `speaker-script.docx` (still 1,950 words / 15:00); venue field in `output/number-verification.json`; cover line in `output/qa_report.md`. Rebuilt the pptx, re-rendered `output/sketchthinker-presentation.pdf` (16 pages) with LibreOffice and inspected slide 1.
- Proposal: the `sketch` bibliography entry now cites the ICLR 2026 version with an OpenReview link and keeps the arXiv ID; the reference audit note records the correction. Three pdflatex passes: 5 pages, body ends on page 4, References on page 5, no warnings or bad boxes (an unrelated underfull line in the Qwen2.5-VL entry, which appeared under the current TeX installation, was fixed with ragged-right setting).
- Research plan: header now reads "based on SketchThinker-R1 (ICLR 2026)"; PDF regenerated with headless Chrome, 1 page.
- Number check: a text diff of the proceedings PDF against arXiv v1 shows the same body, tables and 28-page pagination; differences are only the running header and an added acknowledgment. Reward weights 0.5/0.4/0.1 and all Table 1/2 values used are unchanged.
- Left as is: `paper/2601.02825.*` is the arXiv v1 extraction source (its "Preprint" header is genuine); "preprint" wording inside the papers' own reference lists, skills, and earlier conversation records describes other works or past state.
- Also updated records 15 and 16 to show they were merged through PR #7 and PR #8.
