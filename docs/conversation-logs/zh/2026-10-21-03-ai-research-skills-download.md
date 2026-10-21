# 03 下载 AI-Research-SKILLs 技能库

- 日期：2026-10-21
- 状态：已删除（见 [04](2026-10-21-04-remove-installed-skills.md)）
- 英文版：[点此查看](../en/2026-10-21-03-ai-research-skills-download.md)

## 请求

下载 AI-Research-SKILLs：面向人工智能和计算机方向硕博生的工作流，覆盖主流模型架构搭建、微调策略参数推荐（低秩适配 LoRA、全参数微调）、超参数网格搜索、消融实验设计，以及 Wandb 训练日志追踪规范。

## 结果

- 确认这是真实存在的开源库 [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs)（MIT 协议），共 98 个技能、22 个大类，涵盖模型架构、微调（Axolotl、LLaMA-Factory、PEFT、Unsloth）、后训练、分布式训练、评测、机器学习运维（含 Weights & Biases）、论文写作、科研选题等。
- 官方安装器有两个问题：
  1. "全部安装"模式漏装了第 22 类的 3 个技能（`compiler`、`research-manager`、`rigor-reviewer`）。
  2. 有 48 个技能的文件夹名与 `SKILL.md` 中的 `name` 字段不一致，而 Cursor 官方文档要求两者相同，否则可能无法加载。
- 为此编写了同步脚本 `scripts/sync_ai_research_skills.py`：从上游拉取全部 98 个技能，按 `name` 字段命名文件夹，按原分类放在 `.cursor/skills/ai-research-skills/` 下，并附上上游许可证和对应的提交编号。
- 验证：98 个技能的文件夹名均与 `name` 字段一致，内容与官方安装器的结果逐字节相同，脚本重复执行结果不变。
- 推送到分支 `cursor/ai-research-skills-ab75`（没有开拉取请求）。

## 后续

在 [04](2026-10-21-04-remove-installed-skills.md) 中应要求删除，该分支已从本地和 GitHub 上删除。
