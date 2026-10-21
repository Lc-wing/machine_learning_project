# 05 安装三个开源科研仓库对应的 skill

- 日期：2026-10-21
- 状态：[PR #2](https://github.com/Lc-wing/machine_learning_project/pull/2) 待合并（分支 `cursor/research-agent-skills-ab75`）

## 请求

安装以下三个来源的 skill：

1. The AI Scientist（[SakanaAI/AI-Scientist](https://github.com/SakanaAI/AI-Scientist)）：端到端科研智能体。
2. Nature-Skills（[Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills)）：论文润色、审稿反驳、出版级绘图。
3. Awesome Claude Prompts / Skills 聚合库（[f/awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts) 或 awesome-cursorrules）：据称包含大量 PyTorch 实验设计、超参数调优、消融实验规范的系统指令。

## 核实结果

| 来源 | 实际内容 | 处理 |
|------|----------|------|
| nature-skills | 真正的 skill 仓库，23 个 skill，Apache-2.0 | 原样安装全部 23 个 |
| AI-Scientist | 完整的 Python 程序，不是 skill；需要 NVIDIA GPU + CUDA、`texlive-full`、大模型 API Key；会执行大模型写的代码；许可证要求 AI 生成论文必须披露 | 编写一个薄封装 skill，说明如何部署和运行 |
| f/awesome-chatgpt-prompts（现名 `f/prompts.chat`） | 2567 条通用提示词，涉及 PyTorch / 超参数 / 消融的只有零星 8 条，不是 skill | 未安装 |
| PatrickJS/awesome-cursorrules | 257 条 Cursor 规则（不是 skill），机器学习相关仅 5 条，没有讲消融实验的 | 只装了对口的超参数优化规则 |

## 安装内容

- **nature-skills**：用官方方式 `npx skills add Yuan1z0825/nature-skills --agent cursor --skill '*' --copy` 安装到 `.agents/skills/`（Cursor 读取的项目级目录）。
  - 23 个 skill 与上游 `df6db0b` 逐字节一致，文件夹名均与 `name` 相同。
  - 保留安装器生成的 `skills-lock.json`，以后可用 `npx skills update --project` 更新；补充了上游许可证 `.agents/skills/LICENSE-nature-skills`。
  - 体积约 41MB，其中 34MB 是 `nature-figure` 自带的示例图片；部分 skill 的 Python、R、MCP 可选依赖未安装。
- **ai-scientist**：新增 `.cursor/skills/ai-scientist/SKILL.md`，内容全部来自上游 README 和 `launch_scientist.py`（commit `1de1dbc`）。
  - 运行前检查 GPU、Docker、`pdflatex`、API Key，缺任何一项就停下告知用户。
  - 写明必须容器化运行、`--num-ideas` 默认 50 的花费风险、许可证规定的 AI 生成内容披露。
  - 没有把 AI-Scientist 的代码放进本仓库。
- **超参数优化规则**：原样复制 `automl-hyperparameter-optimization.mdc` 到 `.cursor/rules/`，编辑 `.py`、`.ipynb`、依赖文件时自动生效。
  - 未装的规则：PyTorch 那条实为化学方向（RDKit、分子骨架划分，末尾夹带 Tauri/Flask 说明），LLM 工作流那条以 FastAPI 为主，且两条都会挂到所有文件上。
