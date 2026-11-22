# 对齐来源之后，收益是否仍属于草图风格

英文计划：[HTML](matched-source.html) · [PDF](matched-source.pdf)。

## 这个方向在问什么

风格奖励几乎没有单独造成变短：权重从 0.05 到 0.1，词元只从 65.2 变到 64.3。冷启动文本由 GPT-5 改写，改写可以同时改内容和长度。因此论文报告的 64% 和准确率还不能归到草图风格上。

## 计划怎么做

不提出新的评判器。四条臂共用基座、题目、解码和三个随机种子：论文自己的草图流程；GPT-5 改写但保持原长度和风格，再走同样的训练；风格奖励设为 0 的强化学习；不推理直接作答。横轴是含图像词元的端到端延迟，不是准确率除以推理词元。只有草图同时胜过“保持原长度的改写”和“风格奖励为零”，收益才归于风格。

## 和相邻方向的差别

充分性计划比较的是不同奖励目标，四条臂共用已经压缩过的冷启动数据，所以回答不了改写模型是否改动了内容。这个计划专门做那一次分离。

## English

The plan attributes the reported gain to the sketch style, the rewriter, reinforcement learning, or the metric. The style is credited only when the sketch arm beats both a length-preserving rewrite from the same model and a run whose style reward is zero.
