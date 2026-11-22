# 编号列表是否丢掉被用两次的视觉前提

英文计划：[HTML](twice-used-premise.html) · [PDF](twice-used-premise.pdf)。

## 这个方向在问什么

改写提示要求保持原顺序的编号列表。一个图中事实如果是后面两个步骤的共同前提，列表里没有“这条被多处使用”的标记。压缩时它会像一句可以删的细节，第二次使用就变成没有根据的数字。

## 计划怎么做

选出或改写几何题，使同一个长度或角度是两个推论的前提，并标出这条依赖。在 Qwen2.5-VL-7B 上、相同长度预算下，比较编号列表和“凡被用两次的前提必须再次指向”的草图。指标是该事实的删除率，以及第二次使用处的准确率。两者相同，则命题不成立。接受另外的正确证明。

## 和相邻方向的差别

这是看见图像的充分性里的一个更窄机制，不是把已有的“删掉冗余反思”接到草图训练上。ACL 2026 的图修剪删的是低贡献反思，不保护出度至少为 2 的前提。

## English

The plan tests whether the numbered-list format, rather than brevity alone, drops a visual premise that two later steps share. The comparison is a list against a sketch that must point again at any premise used twice. Matching drop rates and second-use accuracy falsify it.
