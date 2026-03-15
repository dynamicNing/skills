---
name: github-repo-html
description: Analyze a local Git repository and generate a detailed, self-contained HTML report. The report covers remote URL, project description, language statistics, architecture layers, file tree, recent commits, contributors, tags, and README. Use when the user asks to "analyze my repo", "generate a repo report", "document this project as HTML", "generate repository documentation", or wants a visual overview of a local Git/GitHub repository.
---

# GitHub Repo HTML Report

Generate a beautiful, self-contained HTML report for a local Git repository.

## Defaults — never ask the user about these

| Decision | Default |
|---|---|
| Repo path not specified | Current working directory |
| Output path | `<repo-path>/<repo-name>-report.html` |
| No README | Generate a description from code analysis; omit the README section |
| No remote URL | Show "local repository" in the hero |
| No tags | Omit the tags section entirely |
| Language stats include Markdown/JSON/YAML | Exclude `.md`, `.json`, `.yaml`, `.yml`, `.toml`, `.lock` from language bar; count only programming languages |

Proceed through all steps without pausing to confirm. Only communicate at the end with the output file path.

## Workflow

### Step 1 — Collect raw data

The skill directory is always: `~/.claude/skills/github-repo-html/`

```bash
python3 ~/.claude/skills/github-repo-html/scripts/collect_repo_info.py [/path/to/repo]
```

If the path was not specified by the user, omit the argument (defaults to cwd).

Output JSON keys: `repo_name`, `repo_path`, `git`, `file_tree`, `language_stats`, `readme`, `package_info`.

### Step 2 — Analyze architecture

Read key source files to understand the architecture. Focus on:

- Entry points (`main.*`, `index.*`, `app.*`, `server.*`, `cmd/`)
- Config files (`Makefile`, `Dockerfile`, `docker-compose.*`, CI configs)
- Core modules / packages (top 2–3 levels of file tree)
- `package_info` from the JSON (dependencies reveal tech stack)

Identify logical layers (e.g., CLI → Core → Storage, or UI → API → DB → Cache). Read only what's needed — stop once the architecture is clear.

### Step 3 — Generate HTML

Read `~/.claude/skills/github-repo-html/assets/report-template.html` and fill every `{{PLACEHOLDER}}`:

| Placeholder | Content |
|---|---|
| `{{REPO_NAME}}` | `repo_name` from JSON |
| `{{REMOTE_URL}}` | `git.remote_url`, or `"local repository"` if empty |
| `{{REPO_DESCRIPTION}}` | One-sentence description from README + code analysis |
| `{{CURRENT_BRANCH}}` | `git.current_branch` |
| `{{TECH_BADGES}}` | `<span class="badge green">Name</span>` per main framework/language |
| `{{TOTAL_COMMITS}}` | `git.total_commits` |
| `{{CONTRIBUTOR_COUNT}}` | length of `git.contributors` |
| `{{FIRST_COMMIT_DATE}}` | `git.first_commit_date`, or `—` if empty |
| `{{LAST_COMMIT_DATE}}` | `git.last_commit_date`, or `—` if empty |
| `{{PRIMARY_LANGUAGE}}` | top programming language from `language_stats` |
| `{{LANG_BAR_SEGMENTS}}` | `<div class="seg" style="width:X%;background:#COLOR"></div>` per language |
| `{{LANG_ITEMS}}` | `<div class="lang-item"><div class="lang-dot" style="background:#COLOR"></div>Name (X%)</div>` |
| `{{ARCH_SUMMARY}}` | 2–3 sentence architecture overview |
| `{{ARCH_LAYERS}}` | See arch layers format below |
| `{{FILE_TREE_HTML}}` | See file tree format below |
| `{{COMMIT_LIST_HTML}}` | See commits format below |
| `{{CONTRIBUTORS_HTML}}` | See contributors format below |
| `{{TAGS_SECTION}}` | Full tags section HTML if tags exist, otherwise empty string `""` |
| `{{README_HTML}}` | README converted to HTML; omit the entire section if no README |

#### Language color palette

`#3572A5` Python · `#F1E05A` JavaScript · `#3178C6` TypeScript · `#00ADD8` Go · `#DEA584` Rust · `#B07219` Java · `#A97BFF` Kotlin · `#F05138` Swift · `#701516` Ruby · `#4F5D95` PHP · `#178600` C# · `#555555` C/C++ · `#89E051` Shell · `#E34C26` HTML · `#563D7C` CSS/SCSS · `#A41E22` SQL

For unlisted languages cycle: `#58a6ff` · `#bc8cff` · `#d29922` · `#3fb950` · `#f85149`

Calculate each language's percentage from its share of total lines among programming languages only.

#### Arch layers format

```html
<div class="arch-layer">
  <div class="arch-layer-header"
    onclick="this.nextElementSibling.style.display=this.nextElementSibling.style.display==='none'?'block':'none'">
    <span>🎯</span> Layer Name — short tagline
  </div>
  <div class="arch-layer-body">
    <p>Description of this layer's responsibility.</p>
    <ul>
      <li><code>path/to/file</code> — what it does</li>
    </ul>
  </div>
</div>
```

Include 3–6 layers. Icons: 🖥️ UI · 🔌 API · 🧠 Core/Logic · 💾 Storage · 🔧 Config/Build · 🧪 Tests · 🚀 CLI

#### File tree format

```html
<div class="tree-dir-wrap">
  <div class="tree-item dir">
    <span class="tree-toggle">▼</span>
    <span class="tree-icon">📁</span> dirname
  </div>
  <div class="tree-children">
    <div class="tree-node">
      <div class="tree-item">
        <span class="tree-icon">📄</span> filename.ext
      </div>
    </div>
  </div>
</div>
```

File icons: `🐍` .py · `📜` .js/.ts · `🎨` .css/.scss · `🌐` .html · `⚙️` .json/.yaml/.toml · `🐳` Dockerfile · `📝` .md · `🦀` .rs · `🐹` .go · `☕` .java · `💎` .rb · `🐘` .php · `🔧` Makefile · `📄` default

Render up to depth 4. Collapse dirs deeper than 2 by default (add `collapsed` class to `.tree-children`, set toggle to `▶`).

#### Commits format

```html
<div class="commit-item">
  <span class="commit-hash">abc1234</span>
  <div class="commit-msg">
    <div class="msg">Commit message</div>
    <div class="meta">Author Name</div>
  </div>
  <div class="commit-date">2024-01-15</div>
</div>
```

#### Contributors format

```html
<div class="contributor">
  <div class="contributor-avatar" style="background:#1f6feb">AB</div>
  <span class="contributor-name">Author Name</span>
</div>
```

Avatar initials = first letters of first and last name (or first 2 chars). Cycle avatar colors: `#1f6feb` · `#388bfd` · `#2ea043` · `#d29922` · `#bc8cff` · `#f85149`

#### Tags section format

```html
<div class="section" id="tags">
  <div class="section-header">
    <span class="section-icon">🏷️</span>
    <h3>Tags / Releases</h3>
  </div>
  <div class="tag-list">
    <div class="tag-item">v1.0.0</div>
  </div>
</div>
```

#### README: Markdown → HTML

Convert inline: `# H1`→`<h1>`, `` `code` ``→`<code>`, ` ```block``` `→`<pre><code>`, `**b**`→`<strong>`, `*i*`→`<em>`, `[t](url)`→`<a href="url">`, `- item`→`<ul><li>`, blank lines→paragraph breaks.

### Step 4 — Write output

Write the completed HTML to `<repo-path>/<repo-name>-report.html`.

Tell the user: the file path and that they can open it in any browser. Nothing else.

## Fallback

If the Python script fails, gather data manually:

```bash
git -C <path> remote get-url origin
git -C <path> log --pretty=format:"%h|%an|%ad|%s" --date=short -20
git -C <path> rev-list --count HEAD
git -C <path> log --pretty=format:"%an|%ae"
```
