# 简洁从哪一级难度开始有害

英文计划：[HTML](difficulty-boundary.html) · [PDF](difficulty-boundary.pdf)。

## 这个方向在问什么

论文的“准确率不下降”是在平均 182–240 个词元的短推理上得到的。引言写的是上千词元的长推理。s1（EMNLP 2025）表明强制想得更久可以提高准确率，所以短题上的平均数可能盖住一个难度阈值。

## 计划怎么做

不训练新的奖励。用一个会写出长推理的多模态模型，和在同一数据上训练的草图版本，按 MathVision 已公布的难度等级分别比较，并加上不推理直接作答。每个等级单独报告准确率差距、词元比、多个随机种子和置信区间，不先做总平均。差距不随难度扩大，则命题不成立。

## 和相邻方向的差别

它不决定该奖励什么。看见图像的充分性在 [image-sufficiency](../image-sufficiency/README.md)。它也不把平均准确率当成约束，因此不使用 AdaptThink 那种“想或不想”的开关。

## English

The plan maps the difficulty level at which a sketch stops matching a long trace. Levels are not averaged. A flat gap across MathVision’s difficulty labels falsifies the claim that unconditional shortening starts to cost accuracy.
