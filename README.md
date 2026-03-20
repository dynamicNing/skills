# Skills

> Claude Code 技能扩展包合集 / A collection of Claude Code skill extensions

这个仓库存放可分发的 Claude Code Skills，每个 skill 是一个独立的功能模块，能扩展 Claude 在特定任务上的能力。
This repository contains distributable Claude Code Skills — modular extensions that give Claude specialized capabilities for specific tasks.

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

#### 使用方法 / How to Use

安装 skill 后，在 Claude Code 中进入任意本地仓库目录，直接用自然语言触发：
After installing, open Claude Code in any local repo directory and trigger it naturally:

```
# 分析当前目录
帮我分析这个仓库，生成 HTML 报告

# 分析指定路径
帮我分析 ~/projects/myapp 这个仓库，生成详细说明文档

# English
analyze this repo and generate an HTML report
generate a repository report for ~/projects/myapp
```

Claude 会自动：
Claude will automatically:

1. 收集 git 信息（远程地址、提交记录、贡献者等）/ Collect git metadata
2. 读取关键源文件，分析架构分层 / Read key files and analyze architecture
3. 生成自包含 HTML 文件 / Generate a self-contained HTML file
4. 输出到 `<仓库名>-report.html`，用浏览器直接打开即可 / Output to `<repo-name>-report.html`, open with any browser

---

### 📈 `signal-to-trade`

**事件驱动投资分析，从信号到可交易标的的完整推演框架。**
**Event-driven investment analysis — a full framework from signal to tradable instruments.**

将市场事件视为结构性断裂（而非单纯标题），通过四层同心圆模型推演：
Treats market events as structural breaks (not headlines), analyzed through a four-layer concentric model:

- **Circle 0** 事件核心 / Core event — 判定事件性质与所处阶段 / Qualify the event and its stage
- **Circle +1** 逻辑方向 / Logic direction — 一阶传导路径 / First-order transmission paths
- **Circle +2** 节点扩散 / Node diffusion — 宏观/行业/资本节点映射 / Macro, industry, and capital nodes
- **Circle +3** 可交易映射 / Tradable mapping — A股/港股/美股/ETF/衍生品 / A-shares, HK, US, ETFs, derivatives

输出含概率/赔率纪律的多空方案和 Base/Bull/Bear 情景树。
Outputs long/short theses with probability/payoff scoring and Base/Bull/Bear scenario trees.

**触发方式 / Trigger:** "事件驱动分析"、"同心圆推演"、"多空方案"、"signal-to-trade" / any event investment analysis request

#### 使用示例 / Examples

```
Use $signal-to-trade: 美国推出超预期AI算力出口限制，帮我做四层同心圆和可交易映射。
Use $signal-to-trade: 国内地产政策边际转向是否构成事件？给我多空两套方案。
Use $signal-to-trade: 黄金快速突破历史高位，做跨市场标的与衍生品映射。
```

> 📖 **来源说明 / Source Credit：** 本 skill 的方法论框架来源于微信公众号**「老钱日日谈」**。
> The methodology and analytical framework of this skill is sourced from the WeChat public account **"老钱日日谈"**.

---

## 安装 / Installation

### 方式一：通过 `npx skills`（推荐）

安装全部 skills / Install all skills:
```bash
npx skills add dynamicNing/skills
```

安装指定 skill / Install a specific skill:
```bash
npx skills add dynamicNing/skills --skill github-repo-html
```

### 方式二：通过 Claude Code CLI

先下载 `.skill` 文件，再安装 / Download the `.skill` file, then install:
```bash
claude skill install github-repo-html.skill
```

### 方式三：直接克隆仓库

```bash
npx skills add https://github.com/dynamicNing/skills
```

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

## 开发新 Skill / Developing a New Skill

```bash
# 初始化 / Initialize
python3 ~/.claude/skills/skill-creator/scripts/init_skill.py <skill-name> --path .

# 打包 / Package
pip install pyyaml
python3 ~/.claude/skills/skill-creator/scripts/package_skill.py ./<skill-name> .
```
