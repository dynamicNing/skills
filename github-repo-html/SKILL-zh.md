---
name: github-repo-html
description: 分析本地 Git 仓库并生成详细的自包含 HTML 报告。报告涵盖远程 URL、项目描述、语言统计、架构分层、文件树、近期提交、贡献者、标签和 README。当用户要求"分析我的仓库"、"生成仓库报告"、"将项目文档化为 HTML"、"生成仓库文档"，或希望获得本地 Git/GitHub 仓库的可视化概览时使用。
---

# GitHub 仓库 HTML 报告

为本地 Git 仓库生成美观的、自包含的 HTML 报告。

## 默认行为 — 无需询问用户

| 决策项 | 默认值 |
|---|---|
| 未指定仓库路径 | 当前工作目录 |
| 输出路径 | `<仓库路径>/<仓库名>-report.html` |
| 无 README | 从代码分析生成描述；省略 README 区块 |
| 无远程 URL | 在标题区显示"本地仓库" |
| 无标签 | 完全省略标签区块 |
| 语言统计包含 Markdown/JSON/YAML | 从语言条中排除 `.md`、`.json`、`.yaml`、`.yml`、`.toml`、`.lock`；仅统计编程语言 |

无需暂停确认，直接执行所有步骤。仅在最后告知输出文件路径。

## 工作流程

### 第 1 步 — 收集原始数据

Skill 目录固定为：`~/.claude/skills/github-repo-html/`

```bash
python3 ~/.claude/skills/github-repo-html/scripts/collect_repo_info.py [/path/to/repo]
```

若用户未指定路径，省略参数（默认使用当前目录）。

输出 JSON 的键名：`repo_name`、`repo_path`、`git`、`file_tree`、`language_stats`、`readme`、`package_info`。

### 第 2 步 — 分析架构

读取关键源文件以理解架构。重点关注：

- 入口文件（`main.*`、`index.*`、`app.*`、`server.*`、`cmd/`）
- 配置文件（`Makefile`、`Dockerfile`、`docker-compose.*`、CI 配置）
- 核心模块/包（文件树前 2–3 层）
- JSON 中的 `package_info`（依赖项揭示技术栈）

识别逻辑分层（例如：CLI → 核心 → 存储，或 UI → API → DB → 缓存）。仅读取必要内容，架构明确后即停止。

### 第 3 步 — 生成 HTML

读取 `~/.claude/skills/github-repo-html/assets/report-template.html`，填充所有 `{{占位符}}`：

| 占位符 | 内容 |
|---|---|
| `{{REPO_NAME}}` | JSON 中的 `repo_name` |
| `{{REMOTE_URL}}` | `git.remote_url`，为空则填 `"本地仓库"` |
| `{{REPO_DESCRIPTION}}` | 从 README 和代码分析得出的一句话描述 |
| `{{CURRENT_BRANCH}}` | `git.current_branch` |
| `{{TECH_BADGES}}` | 每个主要框架/语言生成 `<span class="badge green">名称</span>` |
| `{{TOTAL_COMMITS}}` | `git.total_commits` |
| `{{CONTRIBUTOR_COUNT}}` | `git.contributors` 的长度 |
| `{{FIRST_COMMIT_DATE}}` | `git.first_commit_date`，为空则填 `—` |
| `{{LAST_COMMIT_DATE}}` | `git.last_commit_date`，为空则填 `—` |
| `{{PRIMARY_LANGUAGE}}` | `language_stats` 中占比最高的编程语言 |
| `{{LANG_BAR_SEGMENTS}}` | 每种语言生成 `<div class="seg" style="width:X%;background:#COLOR"></div>` |
| `{{LANG_ITEMS}}` | `<div class="lang-item"><div class="lang-dot" style="background:#COLOR"></div>语言名 (X%)</div>` |
| `{{ARCH_SUMMARY}}` | 2–3 句架构概述 |
| `{{ARCH_LAYERS}}` | 见下方架构分层格式 |
| `{{FILE_TREE_HTML}}` | 见下方文件树格式 |
| `{{COMMIT_LIST_HTML}}` | 见下方提交列表格式 |
| `{{CONTRIBUTORS_HTML}}` | 见下方贡献者格式 |
| `{{TAGS_SECTION}}` | 有标签时填完整的标签区块 HTML，否则填空字符串 `""` |
| `{{README_HTML}}` | README 转换为 HTML；无 README 则省略整个区块 |

#### 语言颜色配置

`#3572A5` Python · `#F1E05A` JavaScript · `#3178C6` TypeScript · `#00ADD8` Go · `#DEA584` Rust · `#B07219` Java · `#A97BFF` Kotlin · `#F05138` Swift · `#701516` Ruby · `#4F5D95` PHP · `#178600` C# · `#555555` C/C++ · `#89E051` Shell · `#E34C26` HTML · `#563D7C` CSS/SCSS · `#A41E22` SQL

未列出的语言循环使用：`#58a6ff` · `#bc8cff` · `#d29922` · `#3fb950` · `#f85149`

每种语言的百分比 = 该语言行数占所有编程语言总行数的比例。

#### 架构分层格式

```html
<div class="arch-layer">
  <div class="arch-layer-header"
    onclick="this.nextElementSibling.style.display=this.nextElementSibling.style.display==='none'?'block':'none'">
    <span>🎯</span> 层名称 — 简短说明
  </div>
  <div class="arch-layer-body">
    <p>该层职责描述。</p>
    <ul>
      <li><code>path/to/file</code> — 功能说明</li>
    </ul>
  </div>
</div>
```

包含 3–6 层。图标参考：🖥️ UI · 🔌 API · 🧠 核心/逻辑 · 💾 存储 · 🔧 配置/构建 · 🧪 测试 · 🚀 CLI

#### 文件树格式

```html
<div class="tree-dir-wrap">
  <div class="tree-item dir">
    <span class="tree-toggle">▼</span>
    <span class="tree-icon">📁</span> 目录名
  </div>
  <div class="tree-children">
    <div class="tree-node">
      <div class="tree-item">
        <span class="tree-icon">📄</span> 文件名.扩展名
      </div>
    </div>
  </div>
</div>
```

文件图标：`🐍` .py · `📜` .js/.ts · `🎨` .css/.scss · `🌐` .html · `⚙️` .json/.yaml/.toml · `🐳` Dockerfile · `📝` .md · `🦀` .rs · `🐹` .go · `☕` .java · `💎` .rb · `🐘` .php · `🔧` Makefile · `📄` 默认

渲染深度最多 4 层。默认折叠深度超过 2 的目录（为 `.tree-children` 添加 `collapsed` 类，并将切换按钮设为 `▶`）。

#### 提交列表格式

```html
<div class="commit-item">
  <span class="commit-hash">abc1234</span>
  <div class="commit-msg">
    <div class="msg">提交信息</div>
    <div class="meta">作者姓名</div>
  </div>
  <div class="commit-date">2024-01-15</div>
</div>
```

#### 贡献者格式

```html
<div class="contributor">
  <div class="contributor-avatar" style="background:#1f6feb">AB</div>
  <span class="contributor-name">作者姓名</span>
</div>
```

头像缩写 = 姓名首字母（取名字和姓氏首字母，或前 2 个字符）。头像颜色循环：`#1f6feb` · `#388bfd` · `#2ea043` · `#d29922` · `#bc8cff` · `#f85149`

#### 标签区块格式

```html
<div class="section" id="tags">
  <div class="section-header">
    <span class="section-icon">🏷️</span>
    <h3>标签 / 发布版本</h3>
  </div>
  <div class="tag-list">
    <div class="tag-item">v1.0.0</div>
  </div>
</div>
```

#### README：Markdown 转 HTML

转换规则：`# H1`→`<h1>`、`` `code` ``→`<code>`、` ```block``` `→`<pre><code>`、`**b**`→`<strong>`、`*i*`→`<em>`、`[文字](url)`→`<a href="url">`、`- 项目`→`<ul><li>`、空行→段落换行。

### 第 4 步 — 写入输出文件

将完成的 HTML 写入 `<仓库路径>/<仓库名>-report.html`。

告知用户：文件路径以及可在任意浏览器中打开。仅此而已。

## 回退方案

若 Python 脚本执行失败，手动收集数据：

```bash
git -C <路径> remote get-url origin
git -C <路径> log --pretty=format:"%h|%an|%ad|%s" --date=short -20
git -C <路径> rev-list --count HEAD
git -C <路径> log --pretty=format:"%an|%ae"
```
