---
name: gap-contradiction-miner
description: Gap & Contradiction Miner (文献空白与矛盾捕获器). Mines the Limitations / Discussion / Future Work sections (and OpenReview reviews) of the last 1-2 years of top-venue papers for acknowledged unsolved bottlenecks, and detects pairs of strong works whose conclusions contradict each other (method A shows mechanism X hurts, method B shows X is key) to surface hidden boundary conditions or confounders. Use when the user wants high-value open problems, research gaps, literature review, contradiction analysis, or to avoid trivial A+B combinations, or asks for 文献空白 / 研究空白 / 未解问题 / 局限性 / 结论矛盾 / 冲突检测 / 选题.
---

# 文献空白与矛盾捕获器（Gap & Contradiction Miner）

**核心定位**：快速定位高价值的未解问题，规避低水平的简单叠加（A+B）。

用户给出一个研究方向，按下面四个阶段工作，最后按"输出模板"交付。

## 硬性规则

- **不得编造文献或原文**。每一条 limitation 都要附**原文引用**（英文原句）和出处（论文标题、会议/期刊、年份、章节、链接）。只读到摘要、没读到全文的，要明确标注"仅基于摘要"。
- **矛盾必须是真矛盾**。先排除"定义不同"、"指标不同"、"任务不同"造成的表面矛盾，再下结论。
- 用户没有指定时，默认时间窗为近 1–2 年，默认会议期刊按领域选（ML：NeurIPS / ICML / ICLR / JMLR / TPAMI；CV：CVPR / ICCV / ECCV；NLP：ACL / EMNLP / NAACL；数据挖掘：KDD / WWW）。

## 文献检索方式

可用 WebSearch / WebFetch 工具时优先使用：

- Semantic Scholar API
  - 检索：`https://api.semanticscholar.org/graph/v1/paper/search?query=<关键词>&year=2025-2026&fields=title,venue,year,citationCount,abstract,externalIds,openAccessPdf&limit=50`
  - 前向引用（检查某个空白是否已经被后续工作解决）：`https://api.semanticscholar.org/graph/v1/paper/<paperId>/citations?fields=title,year,venue,abstract&limit=100`
- arXiv：全文 HTML 版 `https://arxiv.org/html/<id>` 便于直接读取 Limitations 章节
- OpenReview：审稿意见中的 Weaknesses 和作者 rebuttal 里承认的问题，是 limitation 的重要补充来源
- CVF Open Access、ACL Anthology（这两个来源的论文常有独立的 Limitations 章节）

## 阶段一：建立语料

1. 检索 20–40 篇近 1–2 年的顶会顶刊论文，覆盖该方向的主要子问题和主流方法路线。
2. 记录每篇的：标题、会议/期刊、年份、链接、核心方法、核心结论、能否获取全文。

## 阶段二：Limitation 提取

1. 专门读取每篇论文的 **Limitations、Discussion、Future Work、Conclusion、Broader Impact** 章节，以及 OpenReview 上的审稿意见。
2. 逐条摘录作者承认的"未决瓶颈"，保留原文引用。
3. **过滤低价值条目**，以下情况直接丢弃或降权：
   - 套话型："we only evaluate on N datasets"、"extending to other modalities is future work"
   - 纯工程型：只要加算力或加数据就能解决的
   - 已解决型：通过前向引用检索确认，已经有后续工作解决了
4. **归并与计数**：把不同论文里本质相同的瓶颈归为一类，统计被多少篇独立工作承认过。被多个团队反复承认但仍未解决的瓶颈，价值最高。
5. 为每类瓶颈打分（1–5 分）：
   - **共识度**：多少篇独立工作承认
   - **严重性**：是否卡住了该方向的核心目标
   - **可攻克性**：在学术资源下是否有可行的切入点
   - **时效性**：是否仍未被最新工作解决

## 阶段三：冲突对齐（Contradiction Detection）

1. **列出该方向的关键机制**（例如某种正则化、预训练、注意力结构、数据增强、归一化方式、某种损失项）。
2. **针对每个机制做正反检索**。常用检索词：
   - `<机制> improves` / `<机制> hurts` / `<机制> harmful`
   - `rethinking <机制>` / `revisiting <机制>` / `is <机制> necessary`
   - `when does <机制> help` / `<机制> considered harmful` / `a closer look at <机制>`
3. **对齐成对的矛盾结论**，比如方法 A 证明机制 X 有害，方法 B 证明机制 X 关键。两边都要是高质量工作（顶会顶刊或高引）。
4. **逐项比对实验设置**，找出可能导致结论相反的差异：

   | 维度 | 工作 A | 工作 B |
   |------|--------|--------|
   | 机制 X 的具体定义/实现 | | |
   | 数据规模与分布 | | |
   | 模型规模与架构 | | |
   | 训练预算 / 超参数调优力度 | | |
   | 评测指标与协议 | | |
   | 基线是否调优充分 | | |
   | 任务类型 | | |

5. **判定矛盾类型**：
   - **表面矛盾**：X 的定义不同、指标不同、任务不同，实际上不冲突（记录下来，但不作为主要产出）
   - **边界条件型**：存在一个调节变量（如数据规模、噪声水平、模型容量），X 的作用在其两侧方向相反
   - **混淆变量型**：某个未被控制的因素（如训练时长、调参力度、数据泄漏）同时影响了 X 和结果
   - **评测缺陷型**：某一方的评测协议本身有问题
6. **提出调和假设和决定性实验**：说明隐藏的边界条件或混淆变量可能是什么，并设计一个能区分各种解释的实验（通常是沿着疑似调节变量做网格或析因扫描，同时固定其他因素）。

## 阶段四：生成研究问题（防 A+B 检查）

把高分瓶颈和真矛盾转化为研究问题。每个问题都必须通过以下检查：

- [ ] 能说清楚**为什么现有方法简单组合（A+B）解决不了**
- [ ] 有明确的科学问题（"为什么"、"何时"、"边界在哪"），而不只是"把指标再提高一点"
- [ ] 有可证伪的预期结果和最小验证实验
- [ ] 通过前向引用检索确认尚未被解决

## 输出模板

```markdown
# 文献空白与矛盾报告：<研究方向>

## 0. 范围
- 方向 / 时间窗 / 会议期刊 / 语料论文数 / 能读到全文的比例

## 1. 未决瓶颈（按综合得分排序）
### 瓶颈 1：<一句话概括>
- 承认该瓶颈的工作（附原文引用与出处）：
  - [论文 A, 会议 年份, §章节] "原文……"
  - [论文 B, 会议 年份, §章节] "原文……"
- 共识度 / 严重性 / 可攻克性 / 时效性：x / x / x / x
- 为什么尚未解决：
- 可能的切入点：

## 2. 结论矛盾
### 矛盾 1：机制 X
- 工作 A 的结论（附原文与出处）：
- 工作 B 的结论（附原文与出处）：
- 实验设置对比表：
- 矛盾类型：表面矛盾 / 边界条件型 / 混淆变量型 / 评测缺陷型
- 调和假设：
- 决定性实验：

## 3. 高价值研究问题
| # | 研究问题 | 来源（瓶颈/矛盾） | 为什么不是 A+B | 最小验证实验 | 推荐度 |
|---|----------|-------------------|----------------|--------------|--------|

## 4. 参考文献
（全部附链接；仅基于摘要的标注"仅基于摘要"，未核实的标注"待核实"）
```

## 与其他 skill 的配合

矛盾往往说明双方共享了某个没被检验的前提。找到真矛盾后，可以把背后的隐含前提交给"底层公理反转器"（`first-principles-assumption-inverter`）做进一步的反向推演。
