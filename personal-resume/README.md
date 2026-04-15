# Personal Resume Skill / 个人简历 Skill

A simple, read-only Claude Code skill for storing and accessing He Bo's professional resume.

一个简单的只读 Claude Code skill，用于存储和访问何波的职业简历。

## Features / 功能特性

- 📝 Plain text Markdown storage / 纯文本 Markdown 存储
- 🔍 Easy to query via Claude / 通过 Claude 轻松查询
- 🌐 Bilingual content (Chinese) / 双语内容（中文）
- 📖 Read-only, no scripts needed / 只读，无需脚本

## Installation / 安装

```bash
# Install the skill / 安装 skill
claude skill install personal-resume.skill

# Or from this directory / 或从此目录
claude skill install ./personal-resume
```

## Usage / 使用方式

Simply ask Claude questions about the resume:

直接向 Claude 提问关于简历的问题：

```
"What's my current role?"
"我目前的职位是什么？"

"List my work experience"
"列出我的工作经历"

"What technical skills do I have?"
"我有哪些技术技能？"

"Tell me about my projects at Zuoyebang"
"介绍一下我在作业帮的项目"

"Summarize my career highlights"
"总结我的职业亮点"

"What's my experience with Electron?"
"我在 Electron 方面有什么经验？"
```

## Resume Summary / 简历概要

**Name / 姓名**: 何波 (He Bo)

**Experience / 工作经验**: 12 years / 12年

**Current Focus / 当前方向**: Frontend Development Engineer / 前端开发工程师

**Core Technologies / 核心技术**:
- Electron / Vue / NodeJS / React
- Webpack / TypeScript

**Career Highlights / 职业亮点**:
- 4 years at Zuoyebang: PC client architect, performance monitoring platform owner
- 1 year at SF Technology: Led 10-person team for logistics platform
- 2 years at Didi: JSAPI development (7M monthly PV)
- 2 years at Baidu Waimai: Led merchant platform frontend team

## File Structure / 文件结构

```
personal-resume/
├── SKILL.md           # Skill metadata and instructions
├── README.md          # This file
└── references/
    └── resume.md      # Complete resume in Markdown
```

## Updating the Resume / 更新简历

To update the resume, simply edit the file:

要更新简历，只需编辑文件：

```bash
# Edit the resume file / 编辑简历文件
open ~/.claude/skills/personal-resume/references/resume.md

# Or use your preferred editor / 或使用你喜欢的编辑器
vim ~/.claude/skills/personal-resume/references/resume.md
```

## Why This Design? / 为什么这样设计？

This skill uses a **simple, read-only approach** because:

本 skill 使用**简单的只读方式**，因为：

1. **No generation needed** - Resume is already written, just needs to be stored
2. **Easy to maintain** - Direct Markdown editing, no complex data structures
3. **Fast access** - Claude can read and answer questions immediately
4. **Portable** - Plain text format works everywhere

1. **无需生成** - 简历已经写好，只需存储
2. **易于维护** - 直接编辑 Markdown，无需复杂数据结构
3. **快速访问** - Claude 可以立即读取并回答问题
4. **可移植** - 纯文本格式随处可用

## Use Cases / 使用场景

- Quick reference during job applications / 求职申请时快速参考
- Answer interview questions about experience / 回答面试中关于经历的问题
- Generate customized resume summaries / 生成定制化的简历摘要
- Extract specific project details / 提取特定项目细节
- Compare skills with job requirements / 对比技能与职位要求

## Tips / 使用技巧

1. **Ask specific questions** - "What's my experience with Vue?" works better than "Tell me everything"
2. **Request summaries** - "Summarize my backend experience in 3 bullet points"
3. **Compare and analyze** - "Do I have the skills for a senior architect role?"
4. **Extract metrics** - "What quantifiable achievements do I have?"

1. **提出具体问题** - "我在 Vue 方面有什么经验？"比"告诉我所有信息"效果更好
2. **请求摘要** - "用3个要点总结我的后端经验"
3. **对比分析** - "我是否具备高级架构师职位的技能？"
4. **提取数据** - "我有哪些可量化的成就？"

## License / 许可证

MIT
