# 04 删除此前安装或下载的所有 skill

- 日期：2026-10-21
- 状态：已完成

## 请求

删除上述所有对话中安装或下载的 skills。

## 结果

`main` 分支自始至终未被改动；删除后在整台机器上搜索，没有残留的相关 `SKILL.md`。

| 对象 | 处理方式 |
|------|----------|
| 98 个 AI-Research-SKILLs 及同步脚本（分支 `cursor/ai-research-skills-ab75`，无 PR） | 从本地和 GitHub 删除该分支 |
| 两个自写研究 skill（[PR #1](https://github.com/Lc-wing/machine_learning_project/pull/1) 分支） | 在分支上提交删除，使其与 `main` 无差异；未直接删分支，以免自动关闭 PR |
| 云电脑上的临时文件 | 删除克隆的上游仓库、安装器工作目录 `~/.orchestra`、npx 缓存及临时核对文件 |

PR #1 标题改为 `[Removed] ...` 并更新说明，之后由仓库所有者关闭。
