# 单页研究计划：基于技能的复审与修订

[English](../en/2026-10-23-18-plan-skill-review.md)

- 日期：2026-10-23
- 状态：分支 [plan-skill-review](https://github.com/Lc-wing/machine_learning_project/tree/plan-skill-review)，已向 main 提交 PR（基于 PR #9），未合并

## 请求
让 Codex CLI 使用三套新安装的研究技能复审单页研究计划（docs/research-plan/sketch-sufficiency.html/.pdf），修正实际问题，保持单页，并更新 GitHub 和 Google Drive。

## 结果
Codex 使用了 academic-research-suite（academic-research-skills-codex）、scientific-critical-thinking（K-Dense-AI scientific-agent-skills）和 brainstorming-research-ideas（Orchestra AI-Research-SKILLs）。没有严重问题，发现两个重要问题和四个中等问题：
1. 研究空白表述过度：论文附录 H（表 13–14）已检查冷启动数据中关键步骤的保留。问题陈述改为指出训练阶段缺少对有依据的视觉前提的奖励。
2. 奖励干预不明确。现在只替换风格奖励，准确率和格式奖励（公式 5：0.5/0.4/0.1）保持不变，数据、初始化和策略训练算力一致。
3. 补充评判模型的数据划分和负样本（按题目划分；删除或篡改前提的推理链；留出的人工标注）。
4. 研究问题 1 与标注对齐（视觉前提对比非视觉推导）。
5. 研究问题 3 改为图像对两张图都答对的比例，并加入不看图的评判模型消融。
6. 明确使用 Qwen2.5-VL-7B-Instruct；难度分组在训练前确定。

完整评审：docs/research-plan/notes/skill-review.md。

## 验证
用无头 Chrome 重新生成 PDF；pdfinfo 显示 1 页；已目视检查渲染结果；五个部分齐全；数字已与论文原文核对。
