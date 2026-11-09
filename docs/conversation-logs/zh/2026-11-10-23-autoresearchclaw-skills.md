# 23 安装 AutoResearchClaw 的技能

- 日期：2026-11-10
- 状态：分支 `cursor/autoresearchclaw-skills-ab75`，待合并
- 英文版：[点此查看](../en/2026-11-10-23-autoresearchclaw-skills.md)

## 请求

安装 [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) 的技能。

## 结果

装的是提交 `be4ba475`（2026-08-19）。22 个技能放在 `.cursor/skills/`，许可证全文在 `.cursor/LICENSE-AutoResearchClaw`（MIT）。

- 仓库自带的 20 个技能，来自 `researchclaw/skills/builtin/`：实验方法 8 个（文献检索、假设、实验设计、统计报告、科学写作、可视化、系统综述、元分析），领域 8 个（生物、化学、量子、强化学习、视觉分类与检测、预训练、对齐），工具 4 个（PyTorch 训练、数据加载、混合精度、分布式训练）。
- `.claude/skills/` 里多出来的两个：`a-evolve`（根据失败记录改进智能体）、`researchclaw`（调用 23 阶段自动科研流水线）。

核对过：每个 `name` 都与文件夹同名，描述都不超过 1024 字符，技能之间没有指向仓库外的相对链接。

没有安装 AutoResearchClaw 的 Python 包，也没有运行流水线。`researchclaw` 这个技能会让智能体执行生成的实验代码，使用前需要自己的配置和 API 密钥。编号 22 留给尚未合并的 academic-research-skills 记录，所以这次是 23。
