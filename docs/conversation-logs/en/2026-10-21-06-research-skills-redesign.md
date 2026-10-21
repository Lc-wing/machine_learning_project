# 06 Redesign and install the two research skills

- Date: 2026-10-21
- Status: [PR #3](https://github.com/Lc-wing/machine_learning_project/pull/3) awaiting merge (branch `cursor/ideation-skills-ab75`)
- Chinese version: [中文](../zh/2026-10-21-06-research-skills-redesign.md)

## Request

Design and install the First-Principles Assumption Inverter and the Gap & Contradiction Miner, using the same functional description as in [01](2026-10-21-01-research-skills-v1.md).

## Outcome

Compared with the first version, this one ships runnable scripts and calibration examples.

### Gap & Contradiction Miner (`gap-contradiction-miner`)

- **Limitation extraction**: quotes the bottlenecks authors admit, verbatim, optionally supplemented with OpenReview reviews; filters out boilerplate and purely resource-bound items; groups items by the number of independent teams acknowledging them; scores consensus, severity, tractability, and timeliness; and uses forward citations to confirm the problem is still open.
- **Contradiction alignment**: pairs opposing conclusions through searches in both directions, compares experimental setups item by item, classifies each contradiction as apparent, boundary condition, confounder, definition/measurement, mechanistic explanation, or evaluation flaw, and designs a decisive experiment that separates the explanations.
- **A+B check**: explicit criteria for rejecting ideas that merely combine method A with method B.
- **Calibration examples**: the BatchNorm mechanism debate (Ioffe & Szegedy 2015 vs. Santurkar et al. 2018), sharp minima and generalization (Keskar et al. 2017 vs. Dinh et al. 2017), and whether LLM "emergent abilities" are an evaluation artifact (Wei et al. 2022 vs. Schaeffer et al. 2023).
- **Scripts** (Python standard library only, in `scripts/`):
  - `find_papers.py`: queries Semantic Scholar; `search` filters by year and venue, `citing` lists forward citations; backs off and retries automatically on HTTP 429.
  - `extract_sections.py`: pulls the original text of Limitations, Discussion, Future Work, Conclusion, and Broader Impact sections from arXiv's HTML rendering, including "Limitations." paragraphs nested under other sections; keeps math as LaTeX; stops at Acknowledgments / References; prints the PDF link when no HTML version exists.

### First-Principles Assumption Inverter (`first-principles-assumption-inverter`)

- **Premise extraction**: searches six categories (architecture, data/distribution, optimization/dynamics, resources, evaluation, problem formulation) and keeps 3–5 premises, each backed by at least two mainstream papers that adopt it.
- **Inversion**: five inversion operators (negate, weaken, reverse, constant-to-variable, push to an extreme); for each extreme regime it records the failure mechanism, strength of evidence, observable symptoms, and a minimal verification experiment.
- **New propositions**: uses a "failure source → candidate inductive bias" table to write falsifiable propositions, then self-checks novelty, non-straw-man, feasibility, and non-A+B.
- **Calibration examples**: random labels and generalization (Zhang et al. 2017), Deep Double Descent (Nakkiran et al. 2020), ConvNeXt (Liu et al. 2022), and Mamba (Gu & Dao, COLM 2024).
- Reuses the Gap Miner's scripts to build a corpus, read method sections, and check novelty.

## Verification and known limitations

- Both skills have valid frontmatter, and each `name` matches its folder.
- Every example command in the docs was run against real papers: Mamba, VMamba, QLoRA, "Attention Is All You Need", plus invalid input.
- Without `S2_API_KEY`, requests go through Semantic Scholar's shared public rate limit, so back-to-back searches get throttled. A key can be added in the Cursor dashboard under Cloud Agents → Secrets.
- The year Semantic Scholar reports is the first publication year (often the arXiv year), which can be a year earlier than the venue year.
- OpenReview's endpoint for reading reviews is blocked by a bot challenge (HTTP 403), so reviews are only an optional source.

## Note

The original PR #1 was closed while this work was in progress, so a fresh branch was created from `main` carrying only the two new commits, PR #3 was opened, and the old branch `cursor/research-skills-ab75` was deleted.
