# 15 Formal research proposal: preserving visual evidence

Chinese version: [中文](../zh/2026-10-22-15-formal-research-proposal.md)

- Date: 2026-10-22
- Status: merged into `main` via [PR #7](https://github.com/Lc-wing/machine_learning_project/pull/7).
- Request: expand the merged one-page plan faithfully into a formal academic LaTeX proposal, preserving its title, with 2–4 body pages, separate references, exact required sections, a method figure, experimental table, and monthly timeline. Read the background discussions and prior review; verify references and build the PDF twice.

The proposal is complete: [PDF](../../research-proposal/sketch-sufficiency-proposal.pdf) and [LaTeX source](../../research-proposal/sketch-sufficiency-proposal.tex). `pdfinfo` reports **5 pages total**. References starts on **page 5**, so the body is **4 pages**.

The design requires explicit, grounded visual premises and valid deductions, independently checked against annotations. A correct answer alone does not establish explanation sufficiency. Answer-changing and nuisance image edits test paired correctness and evidence consistency; unchanged wording alone is not evidence of harmful deletion or causal unfaithfulness. The main comparison holds rewritten training data and initial weights fixed, matches compute including judge/rollout costs, and compares achieved average reasoning-token budgets. Difficulty is an evaluation stratum. Original-trace and same-rewriter length-preserving controls probe rewriting effects without asserting causation.

The source paper is characterized accurately: SketchJudge receives neither image nor question; the default reward includes accuracy, format, and style. Its reported 3B MathVision drop is stated without generalization. Proposed gains remain hypotheses.

All 12 cited papers were checked against primary arXiv records for title, listed author order, preprint year, and identifier. Supporting canon, evidence map, argument, section contracts, reference audit, and validation notes are in `docs/research-proposal/notes/`. The PDF uses an embedded TikZ pipeline and two tables. The final source was compiled with `pdflatex` twice, citations were checked for exact coverage, rendered pages were inspected, and build auxiliaries were removed. No experiments were run. Accelerator availability and judge performance remain research-stage uncertainties.

The requested researchwrite, nature-writing, nature-polishing, nature-figure, and nature-ref-verifier guidance informed the work. Bilingual records and both indexes were updated; the user's explicit no-commit instruction takes precedence over the logging rule's commit step. Next research step: reproduce the baseline and run the month-one throughput pilot.
