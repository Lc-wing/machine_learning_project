# 03 下载 AI-Research-SKILLs

- 日期：2026-10-21
- 状态：已删除（见 [04](2026-10-21-04-remove-installed-skills.md)）

## 请求

下载 AI-Research-SKILLs：面向 AI / CS 方向硕博生的工作流，覆盖主流模型架构搭建、微调策略参数推荐（LoRA、全参数）、超参数网格搜索、消融实验设计与 Wandb 训练日志追踪规范。

## 结果

- 确认这是真实存在的开源库 [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs)（MIT 协议），共 98 个 skill、22 个大类，涵盖模型架构、微调（Axolotl、LLaMA-Factory、PEFT、Unsloth）、后训练、分布式训练、评测、MLOps（含 Weights & Biases）、论文写作、科研选题等。
- 官方安装器的两个问题：
  1. `install --all` 漏装了第 22 类的 3 个 skill（`compiler`、`research-manager`、`rigor-reviewer`）。
  2. 有 48 个 skill 的文件夹名与 `SKILL.md` 中的 `name` 字段不一致，而 Cursor 官方文档要求两者相同，否则可能无法加载。
- 为此编写了同步脚本 `scripts/sync_ai_research_skills.py`：从上游拉取全部 98 个 skill，按 `name` 命名文件夹，按原分类放在 `.cursor/skills/ai-research-skills/` 下，并附上游许可证和对应 commit。
- 验证：98 个 skill 文件夹名均与 `name` 一致，内容与官方安装器结果逐字节相同，脚本重复执行结果不变。
- 推送到分支 `cursor/ai-research-skills-ab75`（未开 PR）。

## 后续

在 [04](2026-10-21-04-remove-installed-skills.md) 中应要求删除，该分支已从本地和 GitHub 删除。
