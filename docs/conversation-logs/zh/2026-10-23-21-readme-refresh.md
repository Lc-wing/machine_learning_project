# 重写 README.md 以反映仓库现状

[English](../en/2026-10-23-21-readme-refresh.md)

日期：2026-10-23。状态：分支 [readme-refresh](https://github.com/Lc-wing/machine_learning_project/tree/readme-refresh) 上的 PR 已开启，未合并。

## 请求

重写 `README.md`，准确反映仓库当前内容：项目概述、论文引用、带链接和状态的交付物表、目录结构、重建方法、技能与规则、对话记录。

## 结果

`README.md` 现包含：论文引用（ICLR 2026 论文集、arXiv 2601.02825、本地 PDF 与文本）；研究计划“在压缩的多模态推理中保留视觉证据”的简介；交付物表（中英文论文分析、一页研究计划、正式提案、讲稿、幻灯片大纲、标注为尚未按大纲重建的旧版幻灯片、对话记录）；目录树；重建命令（`pdflatex`、`google-chrome --headless --print-to-pdf`、`build_presentation.py` 加 LibreOffice）；技能与规则（`.agents/skills/` 中 23 个技能，其中 `skills-lock.json` 记录 21 个；`.cursor/skills/` 中 3 个；`.cursor/rules/` 中 2 条）；以及一段中文简介。

## 验证

用脚本检查了 README 中全部 34 个相对链接，均可解析。除本记录和两个索引文件外未改动其他文件。
