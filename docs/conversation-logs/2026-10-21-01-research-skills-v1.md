# 01 设计并安装两个科研 skill（第一版）

- 日期：2026-10-21
- 状态：已删除（见 [04](2026-10-21-04-remove-installed-skills.md)），后在 [06](2026-10-21-06-research-skills-redesign.md) 重新设计

## 请求

为云端电脑安装以下两个 skill：

- **底层公理反转器（First-Principles Assumption Inverter）**：列出某方向近 5 年顶会顶刊普遍遵循的 3–5 个默认前提；设想这些前提在极端边缘工况（超低算力、非高斯噪声、分布剧烈漂移）下失效；倒推需要引入的新归纳偏置。
- **文献空白与矛盾捕获器（Gap & Contradiction Miner）**：抓取最近 1–2 年顶刊顶会论文 Discussion 与 Future Work 中作者承认的未决瓶颈；寻找领域内两组高水平工作结论矛盾的地方，挖掘隐藏的边界条件或混淆变量。

## 结果

- 编写了 `first-principles-assumption-inverter` 和 `gap-contradiction-miner` 两个 skill，放在仓库的 `.cursor/skills/` 下（项目级 skill，随仓库在任何云电脑上可用，不依赖具体环境）。
- 两个 skill 都包含：硬性规则（不编造文献、必须给出处）、分阶段工作流程、输出模板、交付前自检，并互相引用以便串联使用。
- 提交到分支 `cursor/research-skills-ab75`，开了 [PR #1](https://github.com/Lc-wing/machine_learning_project/pull/1)。

## 后续

- 在 [04](2026-10-21-04-remove-installed-skills.md) 中应要求删除，PR #1 随后被仓库所有者关闭。
- 在 [06](2026-10-21-06-research-skills-redesign.md) 中重新设计了更完整的版本（附带可运行的检索与章节抽取脚本）。
