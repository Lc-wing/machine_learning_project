# 01 Design and install two research skills (first version)

- Date: 2026-10-21
- Status: Removed (see [04](2026-10-21-04-remove-installed-skills.md)); redesigned later in [06](2026-10-21-06-research-skills-redesign.md)
- Chinese version: [中文](../zh/2026-10-21-01-research-skills-v1.md)

## Request

Install the following two skills on the cloud machine:

- **First-Principles Assumption Inverter**: list 3–5 default premises that top-venue papers in a field have followed over the past five years; imagine each premise failing under an extreme edge regime (ultra-low compute, non-Gaussian noise, severe distribution shift); and work backward to the new inductive bias the system would need.
- **Gap & Contradiction Miner**: harvest the unsolved bottlenecks that authors admit in the Discussion and Future Work sections of top-venue papers from the last 1–2 years; and find places where two strong lines of work reach contradictory conclusions, to surface hidden boundary conditions or confounders.

## Outcome

- Wrote two skills, `first-principles-assumption-inverter` and `gap-contradiction-miner`, under the repository's `.cursor/skills/` directory. They are project-level skills, so they are available on any cloud machine opened for this repository, regardless of which environment it uses.
- Both skills include hard rules (no fabricated references, every claim cited), a staged workflow, an output template, and a pre-delivery self-check. They reference each other so they can be chained.
- Committed to branch `cursor/research-skills-ab75` and opened [PR #1](https://github.com/Lc-wing/machine_learning_project/pull/1).

## Follow-up

- Removed on request in [04](2026-10-21-04-remove-installed-skills.md); the repository owner then closed PR #1.
- A more complete version, with runnable search and section-extraction scripts, was designed in [06](2026-10-21-06-research-skills-redesign.md).
