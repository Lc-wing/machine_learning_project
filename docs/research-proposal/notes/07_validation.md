# Validation and remaining boundaries

Status: completed local proposal; no research experiments run and no empirical result invented. No commit or push.

## Content review

The operational criterion requires explicit visual premises and valid deductions, checked against annotated derivations. Correct final answers alone do not qualify. Valid alternative proofs and removal of redundant visual statements are allowed. Counterfactual pairs test correctness and evidence consistency, not causal faithfulness. RQ1 has separate visual/nonvisual denominators. The main reward contrast uses identical rewritten data and cold-start weights. Compute accounting includes the judge and rollouts; equal steps are not treated as equal compute. Difficulty remains an evaluation stratum. Expected gains, sample sizes, thresholds, and resources are planned choices or hypotheses.

## Format and build

- Standard article class, 11pt, US Letter, one-inch margins; only permitted packages.
- Exact required numbered headings and Abstract/References present.
- One embedded TikZ pipeline, one datasets/metrics/baselines table, one monthly timeline table.
- Final source compiled with pdflatex twice after the last edit; no BibTeX needed.
- pdfinfo: 5 pages total. References begins on page 5; body length is 4 pages.
- Citation check: 12 cited keys, 12 entries, zero missing or uncited entries.
- Final build: zero errors, undefined citations/references, or overfull boxes. One harmless underfull bibliography paragraph remains.
- PDF pages rendered with pdftoppm and visually inspected. Revised figure and experiment table inspected again after layout correction. No clipping or overlaps observed.
- Build auxiliaries removed after validation; previews and compiler transcripts kept outside the repository in /tmp.

## Rebuild

From docs/research-proposal, run `pdflatex -interaction=nonstopmode -halt-on-error sketch-sufficiency-proposal.tex` twice, then remove the generated .aux, .log, and .out files.

## Remaining research risks

Accelerator availability is unconfirmed; judge calibration, annotation reliability, transfer beyond rendered diagrams, and detectable effect sizes require the planned pilot. No guarantee of positive results or causal faithfulness is made. The next research step is the month-one reproduction and compute pilot.
