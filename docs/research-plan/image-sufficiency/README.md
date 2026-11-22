# 看见图像的充分性

英文计划：[HTML](sketch-sufficiency.html) · [PDF](sketch-sufficiency.pdf)。评审笔记在 [notes/skill-review.md](notes/skill-review.md)。

## 这个方向在问什么

压缩后的推理可以只写出正确的步骤，却漏掉支撑答案的视觉前提。原因是训练时的风格评判器看不见图像和题目，只根据文本像不像编号列表打分。

## 计划怎么做

在 3,000 道可核验的几何和柱状图题上，比较充分性、风格、已陈述步骤正确性、零辅助奖励四条臂。长度和训练算力对齐。强化学习之前先做试点：把省掉的句子放回去，只有答案对数概率的变化比长度更能预测错误时才继续。第一条研究问题里预先规定“被两个后续步骤使用的前提”。准确率除了在匹配长度上比较，还按基线推理长度的分位报告。

## 它不回答什么

它不重新估计论文报告的 64% 词元下降。风格奖励权重从 0.05 到 0.1 时，词元只从 65.2 变到 64.3；现有证据又停在平均 182–240 个词元的短推理上。这两个识别问题分别在 [matched-source](../matched-source/README.md) 和 [difficulty-boundary](../difficulty-boundary/README.md)。

## 同一方向的后续材料

正式计划书在 [docs/research-proposal/](../../research-proposal/sketch-sufficiency-proposal.pdf)。讲稿和幻灯片大纲在 [docs/presentation/](../../presentation/slide-outline.md)。

## English

The plan tests whether a judge that sees the image and the question can require a compressed trace to keep the visual premises the answer needs. It compares four reward arms at matched length and compute. It does not re-estimate the paper’s reported 64% token reduction.
