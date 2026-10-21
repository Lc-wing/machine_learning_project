---
name: gap-contradiction-miner
description: Gap & Contradiction Miner (文献空白与矛盾捕获器). Harvests the unsolved bottlenecks that authors admit in the Limitations / Discussion / Future Work sections of the last 1-2 years of top-venue papers, and finds pairs of strong papers whose conclusions contradict each other (A shows mechanism X hurts, B shows X is essential) to expose hidden boundary conditions or confounders. Ships scripts that search Semantic Scholar and extract those sections from arXiv. Use when the user wants high-value open problems, research gaps, contradiction analysis, a critical literature review, or to avoid trivial A+B combinations; or mentions 文献空白 / 研究空白 / 未解问题 / 局限性 / 未来工作 / 结论矛盾 / 冲突检测 / 选题.
---

# 文献空白与矛盾捕获器（Gap & Contradiction Miner）

**核心定位**：快速定位高价值的未解问题，规避低水平的简单叠加（A+B）。

**输入**：一个研究方向（例如"视觉状态空间模型"、"LLM 的长度外推"）。用户没给方向时先问清楚。可选：指定会议期刊、时间窗、侧重点、深度。

**深度**：默认"标准模式"（约 20 篇语料、找 1–3 组矛盾）。用户要求快速时用约 10 篇；要求全面时用 30–40 篇。

## 硬性规则

1. **不编造任何文献或原文**。每条 limitation 都附英文原句和出处（标题、会议/期刊、年份、章节、链接）。只读到摘要的标注"仅基于摘要"，没核实的标注"待核实"。
2. **先排除假矛盾再下结论**。定义不同、指标不同、任务不同造成的"矛盾"不算真矛盾。
3. **只用高质量工作**：顶会顶刊、或高引的预印本（标注为预印本）。
4. 默认时间窗为近 1–2 年。默认会议期刊按领域选：ML 用 NeurIPS / ICML / ICLR / JMLR / TMLR / TPAMI；CV 用 CVPR / ICCV / ECCV；NLP 用 ACL / EMNLP / NAACL；数据挖掘用 KDD / WWW。

## 工具

本 skill 自带两个只依赖 Python 标准库的脚本，路径为 `.cursor/skills/gap-contradiction-miner/scripts/`：

```bash
# 检索：按年份、会议过滤，按引用数或时间排序。查询语法支持 "短语"、+（与）、|（或）、-（非）
python3 .cursor/skills/gap-contradiction-miner/scripts/find_papers.py search '"state space model" +vision' \
  --year 2025- --venue NeurIPS,ICML,ICLR,CVPR --limit 30

# 前向引用：检查某个瓶颈是否已被后续工作解决
python3 .cursor/skills/gap-contradiction-miner/scripts/find_papers.py citing arXiv:2401.10166 \
  --year 2025- --contains "pre-training,self-supervised"

# 抽取章节：从 arXiv HTML 版抽出 Limitations / Discussion / Future Work / Conclusion / Broader Impact 原文
python3 .cursor/skills/gap-contradiction-miner/scripts/extract_sections.py 2401.10166 2305.14314
python3 .cursor/skills/gap-contradiction-miner/scripts/extract_sections.py 2401.10166 --pattern "limitation|failure" --max-chars 10000
```

使用要点：

- 结果里的 Year 是 Semantic Scholar 记录的首次发表年份，常常是 arXiv 上线那一年，可能比会议年份早一年。报告里写"会议 + 年份"之前要核实。
- `citing` 返回的是最新的引用，高被引论文（上万次）扫描不全。这种情况改用 `search` 加关键词和年份。
- `extract_sections.py` 会把嵌套在 Conclusion 等章节下的 "Limitations." 小段一并带出。没有 HTML 版的论文会给出 PDF 链接，改用 WebFetch 读 PDF。
- 没有 `S2_API_KEY` 时，请求走 Semantic Scholar 的公共限速池，**检索要一条一条串行执行，不要并行**。遇到 429 脚本会自动退避重试约一分钟，仍失败就稍后再试，或改用 WebSearch。设置 `S2_API_KEY` 可以大幅提高限额。
- `extract_sections.py` 没匹配到任何标题时，会列出论文的顶层章节标题，据此调整 `--pattern` 即可。
- **OpenReview 审稿意见**是 limitation 的重要补充（审稿人指出的 Weaknesses、作者 rebuttal 里承认的问题）。可以用 `https://api2.openreview.net/notes/search?term=<标题>&source=forum` 找到论文的 forum id，再用 WebFetch 读 `https://openreview.net/forum?id=<id>`。读取审稿的接口可能被人机验证拦截（返回 403 `ChallengeRequiredError`），这时跳过这一来源，并在报告中注明。
- 不能运行脚本时，退回 WebSearch / WebFetch，直接读取 Semantic Scholar API、arXiv、ACL Anthology、CVF Open Access。

## 校准案例：什么样的矛盾有价值

| 矛盾 | 一方 | 另一方 | 类型与启示 |
|------|------|--------|------------|
| BatchNorm 为什么有效 | Ioffe & Szegedy (ICML 2015)：BN 通过减少 internal covariate shift 加速训练 | Santurkar et al. (NeurIPS 2018)：BN 的收益与 internal covariate shift 关系不大，关键在于让损失曲面更平滑 | **机制解释型**：效果是真的，但流行的解释是错的 |
| 尖锐极小值与泛化 | Keskar et al. (ICLR 2017)：大 batch 训练收敛到尖锐极小值，泛化更差 | Dinh et al. (ICML 2017)：通过重参数化，尖锐极小值也能泛化得一样好 | **定义/度量型**：常用的尖锐度度量不具备重参数化不变性，结论依赖度量的选取 |
| 大模型的"涌现能力" | Wei et al. (TMLR 2022)：某些能力随规模增长突然出现 | Schaeffer et al. (NeurIPS 2023)：换成连续指标后，"突变"消失 | **评测缺陷型**：现象来自不连续的评测指标 |

好的矛盾分析不是"谁对谁错"，而是找出让两边同时成立的**隐藏变量**。

## 工作流程

### 阶段一：建立语料

1. 用 `find_papers.py search` 组合 3–5 组关键词检索，覆盖该方向的主要子问题和方法路线。高引论文和最新论文都要有。
2. 去重后挑选语料，每篇记录：标题、会议/期刊、年份、链接、arXiv 编号、核心方法、核心结论。

### 阶段二：Limitation 提取

1. 对语料中有 arXiv 编号的论文批量运行 `extract_sections.py`。没有的读 PDF，或 ACL Anthology、CVF 的页面。
2. 逐条摘录作者承认的未决瓶颈，**保留英文原句**并记录章节号。有条件时补充 OpenReview 审稿意见。
3. **过滤低价值条目**，以下几类直接丢弃或降权：
   - 套话："we only evaluate on N datasets"、"extending to other modalities is left for future work"
   - 纯资源型：加算力、加数据就能解决的（例如 "limited computational resources prevented us from scaling up"）
   - 已被解决的：用 `find_papers.py citing` 或 `search` 查后续工作，确认已有人解决
4. **归并计数**：把不同论文中本质相同的瓶颈归为一类，统计有多少个**独立团队**承认过。被多个团队反复承认、却仍未解决的瓶颈，价值最高。
5. **打分**（每项 1–5 分）：
   - 共识度：独立承认的团队数
   - 严重性：是否卡住该方向的核心目标
   - 可攻克性：在学术资源下有没有可行切入点
   - 时效性：最新工作是否仍未解决

### 阶段三：冲突对齐（Contradiction Detection）

1. **列出关键机制**：该方向反复出现的设计选择，例如某种正则化、预训练方式、注意力结构、归一化、数据增强、损失项、扫描顺序。
2. **对每个机制做正反检索**：
   - `"<机制>" +improves` / `"<机制>" +(hurts | harmful)`
   - `rethinking <机制>`、`revisiting <机制>`、`is <机制> necessary`、`when does <机制> help`、`a closer look at <机制>`
3. **配对**：找到"A 说 X 有害，B 说 X 关键"这样的两组工作。两组都要是高质量工作。
4. **逐项对比实验设置**：

   | 维度 | 工作 A | 工作 B |
   |------|--------|--------|
   | X 的具体定义和实现 | | |
   | 数据规模与分布 | | |
   | 模型规模与架构 | | |
   | 训练预算、调参力度 | | |
   | 评测指标与协议 | | |
   | 基线是否充分调优 | | |
   | 任务类型 | | |

5. **判定矛盾类型**：
   - **表面矛盾**：定义、指标或任务不同，实际不冲突（记录但不作为主要产出）
   - **边界条件型**：存在调节变量（数据规模、噪声水平、模型容量、序列长度等），X 的作用在其两侧方向相反
   - **混淆变量型**：有未被控制的因素（训练时长、调参力度、数据泄漏、实现细节）同时影响了 X 和结果
   - **定义/度量型**：双方对同一概念的度量方式不同，见校准案例中的尖锐极小值
   - **机制解释型**：现象一致，但对原因的解释相互冲突，见校准案例中的 BatchNorm
   - **评测缺陷型**：至少一方的评测协议有问题，见校准案例中的"涌现能力"
6. **提出调和假设和决定性实验**：说明隐藏变量可能是什么，并设计一个能区分各种解释的实验。通常是沿着疑似调节变量做扫描或析因实验，同时固定其他因素。写清楚每种解释分别预测什么结果。

### 阶段四：生成研究问题（防 A+B 检查）

把高分瓶颈和真矛盾转化为研究问题。**以下情况判定为 A+B，必须改写或删除**：

- 贡献可以概括为"把方法 A 用到场景 B"或"把 A 和 B 结合"，却说不出朴素结合为什么会失败
- 没有新的科学问题，只是"把指标再提高一点"
- 预期收益只是两个方法收益的简单相加

**通过检查的研究问题**至少满足以下一条：说清楚了朴素结合为什么失败（存在冲突或干扰）；能调和一组真矛盾；针对的是至少两个独立团队承认的瓶颈。此外，每个问题都要有可证伪的预期结果和最小验证实验，并且已用前向引用确认尚未被解决。

## 输出模板

```markdown
# 文献空白与矛盾报告：<研究方向>

## 0. 范围
- 方向 / 时间窗 / 会议期刊 / 语料篇数 / 读到全文的比例 / 是否使用了 OpenReview 审稿意见

## 1. 未决瓶颈（按综合得分排序）
### 瓶颈 1：<一句话概括>
- 承认该瓶颈的工作：
  - [论文 A, 会议 年份, §章节] "英文原句……"
  - [论文 B, 会议 年份, §章节] "英文原句……"
- 共识度 / 严重性 / 可攻克性 / 时效性：x / x / x / x
- 后续工作核查：<检索方式与结论>
- 为什么至今未解决：
- 可能的切入点：

## 2. 结论矛盾
### 矛盾 1：机制 X
- 工作 A 的结论（原句与出处）：
- 工作 B 的结论（原句与出处）：
- 实验设置对比表：
- 矛盾类型：
- 调和假设：
- 决定性实验（各解释的预测分别是什么）：

## 3. 高价值研究问题
| # | 研究问题 | 来源（瓶颈/矛盾） | 为什么不是 A+B | 最小验证实验 | 推荐度 |
|---|----------|-------------------|----------------|--------------|--------|

## 4. 参考文献
（全部附链接；仅基于摘要的标注"仅基于摘要"，未核实的标注"待核实"）
```

报告很长时，问用户是否要保存为 Markdown 文件。

## 与底层公理反转器配合

一组真矛盾往往说明双方共享了某个没被检验的前提。找到真矛盾后，可以把这个隐含前提交给 `first-principles-assumption-inverter` 做反向推演。
