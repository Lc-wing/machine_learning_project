# 29 按方向拆分一页研究计划

- 日期：2026-11-23
- 状态：已通过 [拉取请求 #20](https://github.com/Lc-wing/machine_learning_project/pull/20) 合并
- 英文版：[点此查看](../en/2026-11-23-29-organize-plan-folders.md)

## 请求

整理仓库里的文件，让其变得更容易分辨。将同一个任务里不同方向的计划放到不同的文件夹里，并在文件夹里加入该方向的 Markdown 文件进行解释。

## 结果

六份一页计划原来都平铺在 `docs/research-plan/`。现在每个方向一个文件夹，说明写在该文件夹的 `README.md`，总目录是 [docs/research-plan/README.md](../../research-plan/README.md)。

| 文件夹 | 方向 |
|--------|------|
| `image-sufficiency` | 看见图像的充分性。原文件名 `sketch-sufficiency.html` 与 PDF 保留，评审笔记移到该文件夹的 `notes/` |
| `difficulty-boundary` | 简洁从哪一级难度开始有害 |
| `matched-source` | 对齐来源之后，收益是否仍属于草图风格 |
| `twice-used-premise` | 编号列表是否丢掉被用两次的视觉前提 |
| `restore-probability` | 放回被删句子后答案概率是否应当不变 |
| `length-tail` | 平均词元下降是否把错误推进右尾 |

正式计划书和报告材料只属于充分性这一个方向，仍留在 `docs/research-proposal/` 和 `docs/presentation/`。仓库说明、对话记录和评审笔记里指向旧路径的链接已改到新位置。
