# Rewrite README.md to reflect the repository

[中文版](../zh/2026-10-23-21-readme-refresh.md)

Date: 2026-10-23. Status: PR open on branch [readme-refresh](https://github.com/Lc-wing/machine_learning_project/tree/readme-refresh); not merged.

## Request

Rewrite `README.md` so it accurately reflects the current repository: project overview, paper citation, deliverables table with links and status, structure tree, rebuild instructions, skills and rules, and conversation logs.

## Result

`README.md` now has: paper citation (ICLR 2026 proceedings, arXiv 2601.02825, local PDF/text); a summary of the research plan "Preserving Visual Evidence in Compressed Multimodal Reasoning"; a deliverables table (paper analysis EN/ZH, one-page plan, formal proposal, speaker script, slide outline, slide deck marked as an older version not yet rebuilt, conversation logs); a repository tree; rebuild commands (`pdflatex`, `google-chrome --headless --print-to-pdf`, `build_presentation.py` plus LibreOffice); skills and rules (23 skills in `.agents/skills/`, of which `skills-lock.json` lists 21; three `.cursor/skills/`; two `.cursor/rules/`); and a short Chinese summary.

## Verification

A script checked all 34 relative links in the README; none are broken. No other files changed except this record and the two index files.
