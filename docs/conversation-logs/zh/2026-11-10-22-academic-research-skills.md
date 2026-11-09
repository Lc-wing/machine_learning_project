# 22 安装 academic-research-skills

- 日期：2026-11-10
- 状态：分支 `cursor/academic-research-skills-ab75`，待合并
- 英文版：[点此查看](../en/2026-11-10-22-academic-research-skills.md)

## 请求

安装 [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills)。

## 结果

按官方“项目级技能”方式，装的是 v3.24.2（提交 `6d938867`，2026-11-06）。五个技能放在 `.cursor/skills/`，Cursor 会读取这个目录。`shared/` 放在 `.cursor/skills/shared/`，因为技能正文用相对路径 `../shared/` 引用它。许可证全文在 `.cursor/LICENSE-academic-research-skills`。

| 技能 | 作用 |
|------|------|
| `deep-research` | 文献检索与综述 |
| `academic-paper` | 论文写作 |
| `academic-paper-reviewer` | 审稿 |
| `academic-pipeline` | 把检索、写作、审稿、修改串成一条流程 |
| `sr-screener` | 系统综述的文献筛选 |

核对过：五个 `name` 都与文件夹同名，描述都不超过 1024 字符；从技能目录出发的 `../shared/` 能找到 `output_language_pair.md` 和 `handoff_schemas.md`。

协议是 CC BY-NC 4.0，仅限非商业使用。核心技能是提示词，没有安装可选的 Python、Pandoc 或 PDF 工具。Claude Code 的插件命令和钩子在 Cursor 里不会运行。

记录 21 的状态改为已通过拉取请求 #13 合并。
