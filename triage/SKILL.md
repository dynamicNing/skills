---
name: triage
description: "Obsidian 第二大脑：批量扫描 raw 原文，按高/中/低价值重新判断，写 triage 输出和 JSON 缓存；高/中都进入后续 digest 队列。触发词：/triage、筛选、分层、重新判断、raw 积压。 English: triage raw sources into high/medium/low processing queues."
---

# Triage / 筛选

## 用途 / Purpose

你是知识分拣员。目标是快速判断 raw 原文是否值得后续 `/digest`，并把状态写入 JSON 缓存。
You classify raw sources for later digest. You do not create wiki nodes.

`/triage` 只做筛选，不做沉淀。

## 启动前 / Read First

在 secondBrain 仓库内执行时，先读取：

1. `_workspace/docs/pipeline-spec.md`
2. `_workspace/docs/format-spec.md`
3. `_workspace/docs/execution-sop.md`
4. `_workspace/docs/cache-spec.md`
5. `AGENTS.md` 和 `CLAUDE.md`（如存在）

必须遵守 `_workspace/_system/config/source-scope.json`。

## 写入边界 / Write Boundaries

`/triage` 只能写：

- `_workspace/outputs/triage-<source>-<YYYY-MM-DD>.md`
- `_workspace/cache/raw-processing-cache.json`

不能写 `wiki/`，不能写 `raw/`。

## 参数 / Arguments

支持：

- `--source <name>`：来源键，如 `cubox`、`general`、`notions`、`dedao`、`podcast`。
- `--limit <n>`：最多处理 n 篇，默认 50，单次不超过 100。
- `--since <YYYY-MM>`：按文件名或 mtime 过滤。
- `--dir <path>`：扫描指定 raw 目录。
- `--revalue`：按当前新标准重新判断，但保留已 digested 项的 digest 状态。

无参数时，优先从启用来源中找未 triage 的 raw，默认 limit 50。

## 工作流程 / Workflow

### Step 0: 读取范围和缓存

1. 读取 `_workspace/_system/config/source-scope.json`。
2. 读取 `_workspace/cache/raw-processing-cache.json`；不存在时按 `cache-spec` 初始化。
3. 只处理启用来源。
4. 跳过内容哈希未变化且已有 triage 状态的文件，除非用户明确要求 `--revalue`。
5. 对已 `digest.status = digested` 的文件，不重新判断价值；保留原 digest 信息。

旧的 `_workspace/outputs/triage-log.md` 只作历史参考，不再作为幂等状态源。

### Step 1: 列出候选文件

根据 `--source`、`--dir`、`--since`、`--limit` 列出 raw 文件。每次最多 100 篇。

每篇只读取：

- frontmatter 或元数据。
- 标题。
- 正文前 500-800 字符。

不要读全文；全文阅读属于 `/digest`。

### Step 2: 三档判断

`triage.status` 只用：`high`、`medium`、`low`、`skipped`。

#### High / 高价值

后续必须 `/digest`。适合：

- 明确有 durable claims、判断框架、长期可复用机制。
- 深度访谈、课程、书籍笔记、人物经历。
- 与用户长期关注主题高度相关。
- 能补充或修正已有 wiki 节点。
- 有强人文故事、选择、代价、命运转折。
- 有趣、鲜活、反直觉、新颖，能长期召回。
- 重复观点但提供新证据、新案例或更好表达。

#### Medium / 中价值

后续也要 `/digest`，只是优先级低于 high。适合：

- 有观点但密度一般。
- 有案例或方法，但需要结合其他材料才更有价值。
- 时效性较强但仍含可沉淀判断。
- 主题相关但优先级不如 high。

#### Low / 低价值

暂不处理，但保留记录。适合：

- 纯新闻聚合、短期快讯、产品发布。
- 纯技术命令/API/安装教程，且不服务长期知识。
- 营销噪音、网页剪藏噪音、缺正文内容。
- 没有新判断、新证据、新案例，也不能强化已有观点。

注意：不要用过窄的“长期知识”标准。人文故事、有趣性、观点新颖、重复强化，都可以构成高/中价值。

### Step 3: 写缓存

每个 raw_path 在 `_workspace/cache/raw-processing-cache.json` 中写入或更新：

```json
{
  "raw_path": "raw/knowledge/notions/example.md",
  "source_key": "notions",
  "content_hash": "sha256:...",
  "title": "标题",
  "triage": {
    "status": "high",
    "score": 5,
    "reasons": ["interesting", "durable_claim"],
    "triaged_at": "YYYY-MM-DD",
    "triage_output": "_workspace/outputs/triage-notions-YYYY-MM-DD.md",
    "next_action": "digest_required"
  },
  "digest": {
    "status": "not_started",
    "started_at": null,
    "completed_at": null,
    "target_nodes": [],
    "claim_count": 0,
    "digest_log": null
  },
  "last_used_at": null,
  "notes": ""
}
```

`triage.reasons` 优先使用：

- `human_story`
- `interesting`
- `novel_view`
- `useful`
- `durable_claim`
- `reinforces_existing`
- `personal_relevance`

`next_action`：

- high → `digest_required`
- medium → `digest_candidate`
- low/skipped → `no_action`

### Step 4: 写 triage 输出

输出到 `_workspace/outputs/triage-<source>-<YYYY-MM-DD>.md` 或带批次名的同类文件。

建议格式：

```markdown
---
type: "triage"
source: "notions"
scanned: 50
date: "YYYY-MM-DD"
cache: "_workspace/cache/raw-processing-cache.json"
---

# Triage — notions

统计：高价值 N | 中价值 N | 低价值 N | 跳过 N

## 高价值

### 1. [[raw/knowledge/notions/xxx.md]]
- 主题：...
- 建议：`/digest`，可能更新 [[概念A]] [[人物B]]
- 原因：human_story / interesting / durable_claim / ...

## 中价值

- [[raw/...]] — 主题 | 原因 | 建议

## 低价值

- [[raw/...]] — 原因
```

### Step 5: 汇报

告诉用户：

- 扫描多少篇。
- 高/中/低数量。
- 下一批建议优先 digest 的前 5-10 篇。
- 输出文件路径和缓存状态。

## 禁止事项 / Do Not

- 不要写 `wiki/`。
- 不要一次扫描超过 100 篇。
- 不要强行控制高价值比例；宁可多保留高/中候选，不要过早杀掉有趣材料。
- 不要把 medium 当作“不处理”；medium 也进入 digest 队列。
- 不要把缓存当成知识层；缓存只存状态。
