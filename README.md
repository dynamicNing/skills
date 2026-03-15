# Skills

> Claude Code 技能扩展包合集 / A collection of Claude Code skill extensions

这个仓库存放可分发的 Claude Code Skills，每个 skill 是一个独立的功能模块，能扩展 Claude 在特定任务上的能力。
This repository contains distributable Claude Code Skills — modular extensions that give Claude specialized capabilities for specific tasks.

---

## 什么是 Skill / What is a Skill

Skill 是一个包含 `SKILL.md` 及可选资源文件的目录，打包为 `.skill` 文件后可直接安装到 Claude Code。
A skill is a directory containing a `SKILL.md` plus optional resources, packaged into a `.skill` file for installation into Claude Code.

```
<skill-name>/
├── SKILL.md          # 触发描述 + 使用说明 / Trigger description + instructions
├── scripts/          # 可执行脚本 / Executable scripts
├── references/       # 参考文档 / Reference documentation
└── assets/           # 模板、资源文件 / Templates and assets
```

---

## Skills 列表 / Skills List

### 📊 `github-repo-html`

**分析本地 Git 仓库，生成可视化 HTML 报告。**
**Analyze a local Git repository and generate a visual HTML report.**

报告内容 / Report includes:
- 仓库基本信息、远程地址、分支 / Repo info, remote URL, branch
- 语言统计色条 / Language statistics bar
- 架构分层说明 / Architecture layer breakdown
- 文件目录树 / Interactive file tree
- 最近提交记录 / Recent commits
- 贡献者列表 / Contributors
- README 渲染 / Rendered README

**触发方式 / Trigger:** 对 Claude 说 "分析这个仓库生成报告" / "analyze my repo and generate an HTML report"

---

## 安装 / Installation

将 `.skill` 文件安装到 Claude Code：
Install a `.skill` file into Claude Code:

```bash
claude skill install github-repo-html.skill
```

---

## 开发新 Skill / Developing a New Skill

```bash
# 初始化 / Initialize
python3 ~/.claude/skills/skill-creator/scripts/init_skill.py <skill-name> --path .

# 打包 / Package
pip install pyyaml
python3 ~/.claude/skills/skill-creator/scripts/package_skill.py ./<skill-name> .
```

详见 [skill-creator](https://github.com/anthropics/claude-code) 文档。
See [skill-creator](https://github.com/anthropics/claude-code) documentation for details.
