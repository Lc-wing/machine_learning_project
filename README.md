# SketchThinker-R1: Paper Analysis and Research Plan

Final project for a machine learning course. The project analyzes a recent multimodal reasoning paper, identifies its methodological limitations, proposes three research directions, and develops one of them into a research plan, a formal proposal, and a 15-minute presentation.

## Paper

Ruiyang Zhang, Dongzhan Zhou, and Zhedong Zheng. **SketchThinker-R1: Towards Efficient Sketch-Style Reasoning in Large Multimodal Models.** ICLR 2026.
[Proceedings](https://proceedings.iclr.cc/paper_files/paper/2026/hash/a1f0c0cd6caaa4863af5f12608edf63e-Abstract-Conference.html) · [arXiv:2601.02825](https://arxiv.org/abs/2601.02825) · [local PDF](docs/presentation/paper/2601.02825.pdf) · [extracted text](docs/presentation/paper/2601.02825.txt)

SketchThinker-R1 trains Qwen2.5-VL models to reason in short "sketch" traces through sketch-style cold start, a SketchJudge style reward, and RL. Reasoning tokens drop sharply (for example, 182.2 → 64.3 on 7B MMMU) while accuracy is roughly preserved.

## Research plan: Preserving Visual Evidence in Compressed Multimodal Reasoning

The analysis finds that SketchJudge rewards a textual style and never checks whether a compressed trace still states the visual evidence the answer depends on. The plan replaces the style reward with an **image-aware sufficiency reward**: a judge that sees the image, question, and sketch and rewards traces that keep the necessary visual premises. The formal proposal tests it on 3,000 geometry and bar-chart problems with Qwen2.5-VL-7B, comparing four reward arms (sufficiency, style, stated-step correctness, no auxiliary reward) under a 400 GPU-hour cap.

## Deliverables

| Deliverable | Files | Description | Status |
|---|---|---|---|
| Paper analysis | [EN (md)](docs/paper-analysis/sketchthinker-analysis.md) · [EN (pdf)](docs/paper-analysis/sketchthinker-analysis.pdf) · [ZH (md)](docs/paper-analysis/sketchthinker-analysis.zh.md) · [ZH (pdf)](docs/paper-analysis/sketchthinker-analysis.zh.pdf) | Five limitations (L1–L5), three research directions, and a research question plus validating experiment for each direction | Done |
| Analysis review notes | [skill-review.md](docs/paper-analysis/notes/skill-review.md) | Skill-based review log and attribution for the analysis | Done |
| One-page research plan | [HTML](docs/research-plan/sketch-sufficiency.html) · [PDF](docs/research-plan/sketch-sufficiency.pdf) · [review notes](docs/research-plan/notes/skill-review.md) | Problem, proposed solution, key questions, and expected outcome on one page | Done |
| Formal research proposal | [LaTeX](docs/research-proposal/sketch-sufficiency-proposal.tex) · [PDF](docs/research-proposal/sketch-sufficiency-proposal.pdf) · [notes](docs/research-proposal/notes/) | Introduction, related work, method, experimental plan, expected results and timeline; 4-page body plus references | Done |
| Speaker script | [Markdown](docs/presentation/speaker-script.md) · [Word](docs/presentation/speaker-script.docx) · [talk-content.json](docs/presentation/talk-content.json) | Script for 16 slides, 1,947 words, 15:00 at 130 wpm (analysis 12:00, plan pitch 3:00) | Done |
| Slide outline | [slide-outline.md](docs/presentation/slide-outline.md) | Slide-by-slide title, key points, visual, and timing; the current plan for the deck | Done |
| Slide deck | [PPTX](docs/presentation/sketchthinker-presentation.pptx) · [PDF](docs/presentation/output/sketchthinker-presentation.pdf) · [builder](docs/presentation/build_presentation.py) · [figures](docs/presentation/figures/) · [QA output](docs/presentation/output/) | Generated slides and figures | Older version; not yet rebuilt from the slide outline |
| Conversation logs | [index](docs/conversation-logs/README.md) · [English](docs/conversation-logs/en/README.md) · [中文](docs/conversation-logs/zh/README.md) | Bilingual record of every AI-assisted working session | Ongoing |

## Repository structure

```
.
├── README.md
├── skills-lock.json                 # sources and hashes of the installed .agents skills
├── .agents/skills/                  # 23 research skills (nature-* collection + researchwrite)
├── .cursor/
│   ├── rules/                       # conversation-logs.mdc, automl-hyperparameter-optimization.mdc
│   └── skills/                      # ai-scientist, first-principles-assumption-inverter, gap-contradiction-miner
└── docs/
    ├── paper-analysis/              # analysis (EN/ZH, md + pdf), notes/
    ├── research-plan/               # one-page plan (html + pdf), notes/
    ├── research-proposal/           # proposal (tex + pdf), notes/ 00–07
    ├── presentation/                # script, outline, pptx, builder, figures/, output/, paper/
    └── conversation-logs/           # en/ and zh/ records with README indexes
```

## Rebuilding

**Proposal** (run twice to resolve references):

```bash
cd docs/research-proposal
pdflatex sketch-sufficiency-proposal.tex && pdflatex sketch-sufficiency-proposal.tex
```

**One-page plan:**

```bash
cd docs/research-plan
google-chrome --headless --no-pdf-header-footer --print-to-pdf=sketch-sufficiency.pdf sketch-sufficiency.html
```

**Slides, script, and figures** (needs python-pptx, matplotlib, python-docx, Pillow, and Poppler; LibreOffice renders the deck to PDF):

```bash
MPLCONFIGDIR=/tmp/sketchthinker-mpl python3 docs/presentation/build_presentation.py
soffice --headless --convert-to pdf --outdir docs/presentation/output docs/presentation/sketchthinker-presentation.pptx
```

## Skills and rules

The work was done with AI coding agents (Codex CLI and Cursor) using research skill collections:

- **`.agents/skills/`**: 23 skills from [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills), covering literature search, citation and reference verification, paper reading, figures, statistics, writing, polishing, peer review, slide generation, and `researchwrite` for proposals and research plans. [`skills-lock.json`](skills-lock.json) records the source and hash of all 23.
- **`.cursor/skills/`**: [`ai-scientist`](.cursor/skills/ai-scientist/SKILL.md) (running Sakana AI's The AI Scientist), [`first-principles-assumption-inverter`](.cursor/skills/first-principles-assumption-inverter/SKILL.md), and [`gap-contradiction-miner`](.cursor/skills/gap-contradiction-miner/SKILL.md).
- **`.cursor/rules/`**: [`conversation-logs.mdc`](.cursor/rules/conversation-logs.mdc) (always on) requires a Chinese and an English record of every conversation; [`automl-hyperparameter-optimization.mdc`](.cursor/rules/automl-hyperparameter-optimization.mdc) applies to Python ML code.

## Conversation logs

Every session's request, result, and status is recorded in [docs/conversation-logs/](docs/conversation-logs/README.md), with matching files in [English](docs/conversation-logs/en/README.md) and [Chinese](docs/conversation-logs/zh/README.md).

## 中文简介

本仓库是机器学习课程期末项目：分析 ICLR 2026 论文 SketchThinker-R1，总结其方法局限，提出三个研究方向，并将“图像感知的充分性奖励”方向发展为一页研究计划、正式研究提案（LaTeX，正文 4 页加参考文献）和 15 分钟报告（讲稿与幻灯片大纲已完成，现有 `.pptx` 为旧版，尚未按新大纲重建）。论文分析有中英文两版，每次对话的结果以中英文分别记录在 `docs/conversation-logs/`。
