# 06 重新设计并安装两个科研 skill

- 日期：2026-10-21
- 状态：[PR #3](https://github.com/Lc-wing/machine_learning_project/pull/3) 待合并（分支 `cursor/ideation-skills-ab75`）

## 请求

按 [01](2026-10-21-01-research-skills-v1.md) 中同样的功能描述，设计并安装"底层公理反转器"和"文献空白与矛盾捕获器"两个 skill。

## 结果

与第一版相比，这一版配有可实际运行的脚本和校准案例。

### `gap-contradiction-miner`（文献空白与矛盾捕获器）

- **Limitation 提取**：摘录作者承认的瓶颈并保留英文原句，可补充 OpenReview 审稿意见；过滤套话和纯资源型条目，按独立团队数归并，从共识度、严重性、可攻克性、时效性四方面打分，用前向引用确认尚未被解决。
- **冲突对齐**：正反检索配对矛盾结论，逐项对比实验设置，按表面、边界条件、混淆变量、定义/度量、机制解释、评测缺陷六类判定，并设计能区分各种解释的决定性实验。
- **防 A+B 检查**：给出明确判定标准。
- **校准案例**：BatchNorm 机制之争（Ioffe & Szegedy 2015 vs Santurkar et al. 2018）、尖锐极小值与泛化（Keskar et al. 2017 vs Dinh et al. 2017）、"涌现能力"是否为评测假象（Wei et al. 2022 vs Schaeffer et al. 2023）。
- **脚本**（只依赖 Python 标准库，位于 `scripts/`）：
  - `find_papers.py`：调用 Semantic Scholar，`search` 按年份和会议过滤检索，`citing` 列出前向引用；遇到 429 自动退避重试。
  - `extract_sections.py`：从 arXiv HTML 版抽取 Limitations、Discussion、Future Work、Conclusion、Broader Impact 等章节原文，包括嵌套的 "Limitations." 小段；公式保留为 LaTeX；遇到 Acknowledgments / References 自动截止；无 HTML 版时给出 PDF 链接。

### `first-principles-assumption-inverter`（底层公理反转器）

- **公理提取**：从架构、数据/分布、优化/动力学、资源、评测、问题定义六类排查隐含前提，保留 3–5 条，每条至少 2 篇主流论文作为采用证据。
- **反向推演**：五种反转方式（否定、弱化、反向、常量变变量、推向极端），在极端工况下写出失效机制、证据强度、可观测症状和最小验证实验。
- **新命题**：借助"失效来源 → 候选归纳偏置"表写出可证伪命题，并做新颖性、非稻草人、可行性、非 A+B 自检。
- **校准案例**：随机标签与泛化（Zhang et al. 2017）、Deep Double Descent（Nakkiran et al. 2020）、ConvNeXt（Liu et al. 2022）、Mamba（Gu & Dao, COLM 2024）。
- 复用 `gap-contradiction-miner` 的脚本建立语料、阅读方法章节和查新。

## 验证与已知限制

- 两个 skill 的 frontmatter 合规，`name` 与文件夹同名。
- 文档中的示例命令都在真实论文上跑通过：Mamba、VMamba、QLoRA、Attention Is All You Need，以及无效输入。
- 没有 `S2_API_KEY` 时走 Semantic Scholar 公共限速池，连续检索会被限速；可在 Cursor Dashboard → Cloud Agents → Secrets 添加。
- Semantic Scholar 的 Year 是首次发表年份（常为 arXiv 年份），可能比会议年份早一年。
- OpenReview 读取审稿意见的接口会被人机验证拦截（403），因此只作为可选来源。

## 备注

原 PR #1 在工作过程中被关闭，因此改为从 `main` 新开分支、只带两次新提交，开了 PR #3，并删除了旧分支 `cursor/research-skills-ab75`。
