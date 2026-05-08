---
name: prune
description: "Obsidian 第二大脑：月度修剪 wiki，发现近义、重复、低质量、过宽或过窄节点，提出合并/清理/归档建议并在确认后执行。触发词：/prune、修剪、清理 wiki、去重、合并概念。 English: prune and merge confirmed wiki nodes with user approval."
---

# Prune / 修剪

## 用途 / Purpose

你是知识园丁。目标是让 wiki 保持可用、可信、不过度膨胀。
You maintain wiki quality by proposing and, after approval, applying cleanup to confirmed nodes.

## 启动前 / Read First

在 secondBrain 仓库内执行时，先读取：

1. `_workspace/docs/pipeline-spec.md`
2. `_workspace/docs/format-spec.md`
3. `_workspace/docs/execution-sop.md`
4. `_workspace/docs/cache-spec.md`
5. `AGENTS.md` 和 `CLAUDE.md`（如存在）

## 写入边界 / Write Boundaries

`/prune` 只能修改 `wiki/`。

如果合并、归档或改名影响了已 digest 产物引用，可以同步更新 `_workspace/cache/raw-processing-cache.json` 中相关 `digest.target_nodes`。

不能修改 `raw/`。不能手工修改 `wiki/_index.md` 或 `wiki/_lint_report.md`。

## 工作流程 / Workflow

### Step 1: 扫描 wiki

扫描：

- `wiki/concepts/`
- `wiki/topics/`
- `wiki/people/`

记录每个节点：

- frontmatter 是否完整。
- `review_status`、`confirmed`、`updated_at`。
- 一句话定义是否为空。
- 核心观点数量。
- 来源数量。
- 是否引用不存在的 raw。
- 是否被其他节点引用。

可以参考 `node _workspace/scripts/lint.js --write`，但不要手工改生成报告。

### Step 2: 识别问题

重点识别：

#### A. 近义 / 重复节点

名称不同但承载同一机制或判断。判断是否应该：

- 合并为一个主节点。
- 保留为不同切面并互相链接。
- 把重复 claims 留作强化证据。

重复不一定是坏事；如果提供新来源、新案例、新表达，可以保留。

#### B. 低质量节点

- claim 与节点名明显不相关。
- 只有机械摘要，没有判断。
- 来源缺失或来源不在 raw。
- frontmatter 不符合格式。

#### C. 僵尸节点

- 没有实质 claims。
- 一句话定义为空。
- `review_status: stub` 且长期未被激活。
- 只有孤立来源，无法支撑独立概念。

#### D. 粒度问题

- 过宽：什么都能塞进去，导致节点不可用。
- 过窄：只服务一篇原文，且没有未来复用价值。
- topic / people / concepts 边界混乱。

### Step 3: 出报告

先只输出建议，不执行删除或合并。

建议格式：

```markdown
## 建议合并

### 组 1：A / B / C
- 问题：...
- 建议主节点：[[A]]
- 保留：...
- 迁移：...
- 风险：...

## 建议清理

### [[节点名]]
- 问题：...
- 建议：删除无关 claims / 补来源 / 改定义 / 拆分

## 建议归档或删除

### [[节点名]]
- 问题：...
- 建议：archive / delete
- 理由：...
```

每次建议修改不超过 20 个节点。

### Step 4: 等用户确认

必须由用户最终决定合并、删除、归档或保留。

用户逐项确认后再执行。不能未经确认删除任何文件。

### Step 5: 执行修改

执行时：

- 合并：把有效 claims 和来源迁移到主节点，保留来源链接。
- 清理：删除无关 claims，补齐定义、相关概念和来源。
- 归档：设置 `review_status: "archived"`，保留来源和说明。
- 删除：仅在用户明确确认后删除文件。
- 更新 `updated_at` 和 `confirmed: true`。
- 必要时更新缓存里的 `digest.target_nodes`。

### Step 6: 验证

执行后运行：

```bash
node _workspace/scripts/lint.js --write
node _workspace/scripts/stats.js --write
```

汇报新增/减少节点数、仍存在的问题、下一轮建议。

## 禁止事项 / Do Not

- 不要自动删除。
- 不要一次处理超过 20 个节点的实际修改。
- 不要因为观点重复就机械删除；先判断它是否提供新证据、新案例或更好表达。
- 不要手工改脚本生成产物。
