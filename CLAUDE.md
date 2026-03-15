# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 仓库用途 / Repository Purpose

这是一个存放 Claude Code Skills 的仓库。每个 skill 是一个可分发的功能扩展包。
This is a collection of Claude Code Skills — modular capability extensions for Claude.

所有文档和说明使用**中英双语**。
All documentation and descriptions should be written in **both Chinese and English**.

## Skill 结构 / Skill Structure

每个 skill 位于独立子目录，打包后生成 `.skill` 文件（zip 格式）。
Each skill lives in its own subdirectory and is packaged into a `.skill` file (zip format).

```
<skill-name>/
├── SKILL.md          # 必需：YAML frontmatter (name, description) + 使用说明
├── scripts/          # 可选：Python/Bash 脚本
├── references/       # 可选：供 Claude 读取的参考文档
└── assets/           # 可选：模板、图片等输出用资源
```

## 常用命令 / Common Commands

```bash
# 初始化新 skill / Initialize a new skill
python3 ~/.claude/skills/skill-creator/scripts/init_skill.py <skill-name> --path .

# 打包 skill / Package a skill
pip install pyyaml   # 首次需要 / required once
python3 ~/.claude/skills/skill-creator/scripts/package_skill.py ./<skill-name> .
```

## 现有 Skills / Existing Skills

| Skill | 说明 / Description |
|---|---|
| `github-repo-html` | 分析本地 Git 仓库并生成 HTML 可视化报告 / Analyze a local Git repo and generate an HTML visual report |
