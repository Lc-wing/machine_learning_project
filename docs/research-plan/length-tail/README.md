# 平均词元下降是否把错误推进右尾

英文计划：[HTML](length-tail.html) · [PDF](length-tail.pdf)。

## 这个方向在问什么

论文的词元数和思考效率都是平均数，而推理长度是重尾的。风格奖励把大多数题压短，平均数就下降；少数本来就很长的题可以仍然很长，并且更常答错。

## 计划怎么做

不改训练惩罚。在 Qwen2.5-VL-7B 上按论文的数据复现草图训练和 Vanilla-R1。每个基准按基线推理长度分成五档。每一档报告准确率差距、词元比、端到端延迟、多个随机种子和置信区间。主要对比是高于第 90 百分位的题和低于中位数的题。平均降幅只作参照。差距不随档位变大，则命题不成立。右尾掉点本身不能说明评判器应该看见图像。

## 和相邻方向的差别

IJCAI/ECAI 2026 的 Sprint or Delve 已经用对数正态描述长度，并减轻对长推理的惩罚。那个工作改的是惩罚形式，数据是文本数学题。这里不改惩罚，只检查风格奖励在多模态基准各长度档上的准确率。难度计划按题目难度分层；这一计划按基线推理长度分层。

## English

The plan reads the reported mean token reduction by quintile of baseline length. It does not change the training penalty. A flat accuracy gap across quintiles falsifies the claim that the mean hides losses on the longest items.
