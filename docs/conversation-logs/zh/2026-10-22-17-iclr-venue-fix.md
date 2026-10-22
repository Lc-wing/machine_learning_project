# 17 SketchThinker-R1 发表信息更正：ICLR 2026

英文版：[English](../en/2026-10-22-17-iclr-venue-fix.md)

- 日期：2026-10-22
- 状态：分支 [`iclr-venue-fix`](https://github.com/Lc-wing/machine_learning_project/tree/iclr-venue-fix)；已创建 [PR #9](https://github.com/Lc-wing/machine_learning_project/pull/9)，未合并。
- 请求：SketchThinker-R1（Zhang、Zhou、Zheng；arXiv:2601.02825）已作为海报论文发表于 ICLR 2026（[OpenReview](https://openreview.net/forum?id=ZSMDuKtYbt)、[会议论文集 PDF](https://proceedings.iclr.cc/paper_files/paper/2026/file/a1f0c0cd6caaa4863af5f12608edf63e-Paper-Conference.pdf)）。此前误作仅有 arXiv 版本；需全部更正、重新生成输出，并核对所用数字是否不同。

结论：所有把该论文写成仅 arXiv 或预印本的地方均已改为 ICLR 2026。会议版与 arXiv 第一版所用数字完全一致，未改动任何数字。

- 演示文稿（`docs/presentation/`，本次一并加入）：`build_presentation.py` 封面会议行改为 `ICLR 2026`；`talk-content.json`、幻灯片备注、`speaker-script.md` 和 `speaker-script.docx` 中第一页讲稿由“这是 arXiv 2026 预印本”改为“这是 ICLR 2026 海报论文”（仍为 1,950 词、15 分钟）；同步更新 `output/number-verification.json` 的会议字段和 `output/qa_report.md` 的封面说明。重新生成 pptx，用 LibreOffice 重新渲染 `output/sketchthinker-presentation.pdf`（16 页），并检查第一页。
- 研究计划书：参考文献 `sketch` 条目改为引用 ICLR 2026 版本，附 OpenReview 链接，保留 arXiv 编号；文献核查笔记记录了本次更正。pdflatex 编译三遍：共五页，正文止于第四页，参考文献在第五页，无警告和坏盒。当前 TeX 环境下 Qwen2.5-VL 条目出现的一处无关欠满行，已改为左对齐排版消除。
- 一页研究计划：标题行改为“based on SketchThinker-R1 (ICLR 2026)”；用无头 Chrome 重新生成 PDF，仍为一页。
- 数字核对：会议版 PDF 与 arXiv 第一版的文本比对显示正文、表格及 28 页分页相同，差别仅为页眉和新增的致谢。奖励系数 0.5/0.4/0.1 以及所用表 1、表 2 数值均未变化。
- 保持不变：`paper/2601.02825.*` 是 arXiv 第一版提取源，其中的“Preprint”页眉属实；论文参考文献表、技能文件和早期对话记录中的“预印本”指其他文献或当时状态。
- 同时把第 15、16 号记录更新为已通过 PR #7、PR #8 合并。
