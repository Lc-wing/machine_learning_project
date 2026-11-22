# 放回被删句子后，答案概率是否应当不变

英文计划：[HTML](restore-probability.html) · [PDF](restore-probability.pdf)。

## 这个方向在问什么

风格奖励把像编号列表的文本记为充分，不看答案概率。被删的句子如果是唯一的理由，页面上的答案可以不变，但模型并没有使用那一句。

## 计划怎么做

试点成功之前不训练新奖励。对成对的长推理和草图，把省掉的句子逐句插回固定位置，记录答案对数概率的绝对变化。对照是在同一位置插入一句长度相近、与题目无关的话，用来排除位置本身造成的变化。这个变化量必须比长度更能预测草图答错。不能的话，就不把概率移动当作删除标准。试点成功之后，才用三个随机种子训练“放回去之后对数概率仍在阈值内才允许删除”的压缩器。不改图像，也不另训一个逐步打分的过程奖励。

## 和相邻方向的差别

充分性计划用人工评分和改答案的图像对。这个计划用模型自己的答案概率，而且可以在已有输出上先算，不必先训练。

## English

The plan asks whether restoring an omitted sentence moves the answer probability enough to predict errors better than length, above an unrelated-sentence control. If the pilot fails, probability movement is not used as a deletion rule and no compressor is trained.
