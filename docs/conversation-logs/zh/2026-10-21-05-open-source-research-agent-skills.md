# 05 安装三个开源科研仓库对应的技能

- 日期：2026-10-21
- 状态：[拉取请求 #2](https://github.com/Lc-wing/machine_learning_project/pull/2) 待合并（分支 `cursor/research-agent-skills-ab75`）
- 英文版：[点此查看](../en/2026-10-21-05-open-source-research-agent-skills.md)

## 请求

安装以下三个来源的技能：

1. The AI Scientist（[SakanaAI/AI-Scientist](https://github.com/SakanaAI/AI-Scientist)）：端到端的科研智能体。
2. Nature-Skills（[Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills)）：论文润色、审稿反驳、出版级绘图。
3. 提示词与技能聚合库（[f/awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts) 或 awesome-cursorrules）：据称包含大量 PyTorch 实验设计、超参数调优、消融实验规范的系统指令。

## 核实结果

| 来源 | 实际内容 | 处理 |
|------|----------|------|
| nature-skills | 真正的技能仓库，23 个技能，Apache-2.0 协议 | 原样安装全部 23 个 |
| AI-Scientist | 完整的 Python 程序，不是技能；需要英伟达 GPU 和 CUDA、`texlive-full`、大模型 API 密钥；会执行大模型写的代码；许可证要求披露论文由人工智能生成 | 编写一个轻量封装技能，说明如何部署和运行 |
| f/awesome-chatgpt-prompts（现名 `f/prompts.chat`） | 2567 条通用提示词，涉及 PyTorch、超参数或消融实验的只有零星 8 条，不是技能 | 没有安装 |
| PatrickJS/awesome-cursorrules | 257 条 Cursor 规则（不是技能），与机器学习相关的只有 5 条，没有讲消融实验的 | 只安装了对口的超参数优化规则 |

## 安装内容

- **nature-skills**：用官方命令 `npx skills add Yuan1z0825/nature-skills --agent cursor --skill '*' --copy` 安装到 `.agents/skills/`（Cursor 会读取的项目级目录）。
  - 23 个技能与上游提交 `df6db0b` 逐字节一致，文件夹名均与 `name` 字段相同。
  - 保留了安装器生成的 `skills-lock.json`，以后可以用 `npx skills update --project` 更新；补充了上游许可证 `.agents/skills/LICENSE-nature-skills`。
  - 体积约 41MB，其中 34MB 是 `nature-figure` 自带的示例图片；部分技能需要的 Python、R、MCP 可选依赖没有安装。
- **ai-scientist**：新增 `.cursor/skills/ai-scientist/SKILL.md`，内容全部来自上游的说明文档和 `launch_scientist.py`（提交 `1de1dbc`）。
  - 运行前检查 GPU、Docker、`pdflatex`、API 密钥，缺任何一项就停下并告知用户。
  - 写明必须在容器中运行、`--num-ideas` 默认值为 50 带来的花费风险，以及许可证规定的人工智能生成内容披露要求。
  - 没有把 AI-Scientist 的代码放进本仓库。
- **超参数优化规则**：原样复制 `automl-hyperparameter-optimization.mdc` 到 `.cursor/rules/`，编辑 `.py`、`.ipynb` 和依赖文件时自动生效。
  - 没有安装的规则：标为 PyTorch 的那条实际是写给化学方向的（RDKit、分子骨架划分，末尾还夹带 Tauri 和 Flask 的说明）；大模型工作流那条以 FastAPI 为主；而且两条都会作用于所有文件。
