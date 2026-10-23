# 研究计划书与演讲稿同步修订版计划；幻灯片大纲

[English version](../en/2026-10-23-20-sync-proposal-script-outline.md)

日期：2026-10-23。状态：分支 [sync-proposal-ppt](https://github.com/Lc-wing/machine_learning_project/tree/sync-proposal-ppt) 已创建拉取请求，未合并。

## 请求

让正式研究计划书和演讲材料与修订后的单页计划（`docs/research-plan/sketch-sufficiency.html`）及修订后的论文分析一致。任务中途范围调整：完成计划书和演讲稿，幻灯片改为逐页大纲，不重建；结果上传到 Google Drive。

## 结果

- `docs/research-proposal/sketch-sufficiency-proposal.tex/.pdf`：围绕方向一（感知图像的充分性奖励）重写。3,000 道几何与柱状图题，按模板族划分为 1,600/400/1,000；四个奖励组（充分性、风格、已述步骤正确性、零辅助奖励）；Qwen2.5-VL-7B；三个随机种子；一个按预算条件化的策略（64/128/256 个词元）；评判器门槛（误接受率 ≤ 10%，召回率 ≥ 70%）；在约 128 个词元处，相对风格奖励准确率提高 3 个百分点、人工充分性提高 5 个百分点即为成功；算力上限 400 GPU 小时（12 次训练 × 25 小时 + 100 小时）。新增参考文献 VisualPRM（[arXiv:2503.10291](https://arxiv.org/abs/2503.10291)），共 13 篇。同步更新笔记 00–06。
- `docs/presentation/speaker-script.md/.docx` 与 `talk-content.json`：第 11–13 页对应修订后的局限 L1–L5、三个方向和方向一的验证；第 14–16 页介绍新计划；第 1 页不变。口述 1,947 词，按每分钟 130 词计 15:00（第一部分 12:00，第二部分 3:00）。
- `docs/presentation/slide-outline.md`：新的 16 页大纲（标题、要点、视觉、时间）。`.pptx`、构建脚本、图和输出文件保持 `main` 版本，尚未重建幻灯片。

## 验证

`pdflatex` 编译为 5 页（正文 4 页加参考文献 1 页）。计划书和演讲稿中已无 `2,400`、“三个奖励组”或按预算分别训练的旧表述。论文数字（如 61.0→62.8、182.2→64.3、3B 上 MathVision 26.9→25.3）已对照 `docs/presentation/paper/2601.02825.txt` 核实。
