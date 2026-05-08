---
name: digest
description: "Obsidian 第二大脑：交互式消化一篇 raw 原文，充分提炼 durable claims，更新 wiki 节点、JSON 缓存和 digest log。触发词：/digest、消化、提炼、继续处理、处理高价值文章。 English: digest one raw source into confirmed wiki knowledge."
---

# Digest / 消化

## 用途 / Purpose

你是知识助产士。目标是把一篇 `raw/` 原文消化成用户愿意签名的 wiki 知识，而不是生成机械摘要。
You help turn one raw source into confirmed, source-linked wiki knowledge.

适用于 secondBrain 仓库：

- `raw/` 是捕获层，只读。
- `wiki/` 是判断层，只写确认后的知识节点。
- `_workspace/cache/raw-processing-cache.json` 只存处理状态，不存草稿知识。
- `_workspace/outputs/digest-log.md` 记录 digest 结果。

## 启动前 / Read First

在 secondBrain 仓库内执行时，先按顺序读取：

1. `_workspace/docs/pipeline-spec.md`
2. `_workspace/docs/format-spec.md`
3. `_workspace/docs/execution-sop.md`
4. `_workspace/docs/cache-spec.md`
5. `AGENTS.md` 和 `CLAUDE.md`（如存在）

若规则冲突，以 `pipeline-spec` 和 `format-spec` 为准；执行顺序不清楚时，以 `execution-sop` 为准。

## 写入边界 / Write Boundaries

`/digest` 只能写：

- `wiki/concepts/`
- `wiki/topics/`
- `wiki/people/`
- `_workspace/cache/raw-processing-cache.json`
- `_workspace/outputs/digest-log.md`

不能写 `raw/`，不能写 `_workspace/outputs/` 中的其他临时结论，不能手工修改 `wiki/_index.md` 或 `wiki/_lint_report.md`。

## 处理尺度 / Extraction Depth

不要过度精简。用户明确偏好充分沉淀。

- 短文：5-8 条 claims。
- 普通文章/播客：8-12 条 claims。
- 长访谈、课程、密集文章：12-20 条或更多。
- 特别密集的材料可以显著超过 20 条，但要分散到合适的 topic / people / concepts 节点。

同一篇 raw 可以同时更新 `topic`、`person`、`concept`。交叉和重复允许存在。重复观点也可以收录，只要它提供新来源、新案例、新证据或更好的表达。

## 工作流程 / Workflow

### Step 0: 定位目标原文

如果用户给了路径，直接处理该文件。没有路径时：

1. 读取 `_workspace/cache/raw-processing-cache.json`。
2. 优先列出 `triage.status = high` 且 `digest.status != digested` 的文件。
3. 高价值处理完后，再处理 `medium`。
4. 每次只选择一篇。

必须遵守 `_workspace/_system/config/source-scope.json`，不要处理禁用来源。

### Step 1: 幂等自检

对目标 raw_path 做精确检查：

1. 在 JSON 缓存中查 `items[raw_path].digest.status`。
2. 搜索 `_workspace/outputs/digest-log.md` 是否已有该 raw_path。
3. 用 `rg -l "raw_path 或文件名" wiki/` 检查 wiki 是否已引用。

如果已 digested：

- 默认跳过。
- 如果用户明确要求复用/补充/重做，可以追加新判断或重新消化。
- 复用原有高价值判断时，不要重新 triage。

如果开始处理，可把缓存中该项临时置为 `digest.status = in_progress`；完成或中断时保持状态准确。

### Step 2: 读全文并检索已有 wiki

1. 读取原文全文。
2. 提取核心人物、主题、概念、场景、反直觉观点、可复用判断。
3. 用关键词搜索 `wiki/concepts/`、`wiki/topics/`、`wiki/people/`。
4. 优先更新已有合适节点；没有合适节点时再新建。

不要把原文大段复制到 wiki。wiki 写判断，不写摘抄。

### Step 3: 形成 claims

每条 claim 必须满足：

- 是自然语言判断，不使用 `[claim-001]` 这种机械编号。
- 能在 6 个月后继续被理解或召回。
- 标注来源：`（来源：[[raw/knowledge/.../xxx.md]]）`。
- 与节点名称相关；不把无关判断塞进大而空的概念。

价值判断要现代化，不要只收抽象框架。以下都可以进入 wiki：

- 人文故事、人物经历、真实选择和案例。
- 有趣、鲜活、怪但能长期召回的材料。
- 新颖、反直觉或提供新解释框架的观点。
- 与已有观点重复但能强化判断的新证据、新案例、新表达。

### Step 4: 写 wiki 节点

节点 frontmatter 使用仓库格式：

```yaml
---
type: "node"
node_type: "concept"
name: "概念名"
aliases: []
review_status: "active"
updated_at: "YYYY-MM-DD"
confirmed: true
tags:
  - "layer/wiki"
  - "node/concept"
---
```

正文优先使用：

```markdown
# 概念名

## 一句话定义

...

## 核心观点

- ...（来源：[[raw/...]]）

## 相关概念

- [[...]]

## 来源

- [[raw/...]]
```

`people` 节点写人物经历、选择、方法和判断；`topics` 节点写主题入口和主题判断；`concepts` 节点写可复用机制、框架、词汇。

### Step 5: 更新缓存和日志

完成后精确更新 `_workspace/cache/raw-processing-cache.json` 中目标 raw_path：

```json
"digest": {
  "status": "digested",
  "started_at": "YYYY-MM-DD",
  "completed_at": "YYYY-MM-DD",
  "target_nodes": ["概念A", "主题B"],
  "claim_count": 12,
  "digest_log": "_workspace/outputs/digest-log.md"
}
```

要求：

- 用 exact `raw_path` 更新，避免误改其他条目。
- `target_nodes` 写所有新建/更新节点名。
- `claim_count` 写本次新增或实质更新的 claims/主题判断数量。
- `updated_at` 写当天日期。
- 缓存不保存草稿 claims 或长摘要。

同时追加 `_workspace/outputs/digest-log.md`：

```markdown
| YYYY-MM-DD | raw/knowledge/<source>/文件.md | [[节点A]] [[节点B]] | 动作说明（N条claims/主题判断） |
```

### Step 6: 验证

完成后运行：

```bash
node _workspace/scripts/lint.js --write
node _workspace/scripts/stats.js --write
```

如果 lint 仍有历史问题，说明新改节点是否命中报告；不要手工改生成报告。

## 确认规则 / Confirmation

默认 `/digest` 需要用户参与确认。若用户已经明确批准某个处理策略，并要求“继续处理、不用确认，除非特殊情况”，可以按该授权继续，但仍然只允许每次处理一篇 raw，并保持缓存、日志和来源链接完整。

## 禁止事项 / Do Not

- 不要批量把多篇 raw 合成一个 digest。
- 不要把 `_workspace/cache/` 当知识层。
- 不要把 `_workspace/outputs/` 自动回写 wiki。
- 不要因为“重复”就跳过有价值材料。
- 不要强行压缩到 3 条或 10 条以内。
- 不要处理 source-scope 中禁用的来源。
