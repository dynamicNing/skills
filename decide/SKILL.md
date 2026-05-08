---
name: decide
description: "Obsidian 第二大脑：基于 wiki 优先、raw 补充来回答决策性问题，输出带引用的判断和知识空白。触发词：/decide、决策、怎么看、如何判断、用我的知识库。 English: answer decisions from the user's own wiki-first knowledge base."
---

# Decide / 使用

## 用途 / Purpose

你是知识顾问。目标是用用户自己的 secondBrain 回答决策性问题，而不是给通用百科式答案。
You answer from the user's own wiki-first knowledge base, with raw as supporting evidence.

## 启动前 / Read First

在 secondBrain 仓库内执行时，先读取：

1. `_workspace/docs/pipeline-spec.md`
2. `_workspace/docs/format-spec.md`
3. `_workspace/docs/execution-sop.md`
4. `_workspace/docs/cache-spec.md`
5. `AGENTS.md` 和 `CLAUDE.md`（如存在）

必须遵守 `_workspace/_system/config/source-scope.json`。

## 写入边界 / Write Boundaries

`/decide` 只能写 `_workspace/outputs/`。

默认不写 `wiki/`，不写 `raw/`，不把回答自动回写为正式知识。只有当某篇 raw 被明确作为决策依据时，才可以按 `cache-spec` 更新 `last_used_at`。

## 工作流程 / Workflow

### Step 1: 拆问题

把用户问题拆成 3-8 个搜索词，包括：

- 关键词。
- 同义词。
- 相关概念。
- 可能的人物或主题。

例如“如何应对投资中的不确定性”：搜索 `不确定性`、`黑天鹅`、`反脆弱`、`安全边际`、`风险预算`、`概率思维`、`资产配置`。

### Step 2: wiki 优先检索

按顺序搜索：

1. `wiki/concepts/`
2. `wiki/topics/`
3. `wiki/people/`

每层最多读最相关的 10 个文件。优先使用 `rg`。

先看 wiki，因为 wiki 是正式知识层。不要一开始就用通用知识或 raw 淹没回答。

### Step 3: raw 补充

当 wiki 不够时，再搜 `raw/knowledge/` 中启用来源：

- 先按文件名和标题搜。
- 再按正文搜。
- 只读取最相关的 raw。
- 明确标注 raw 是证据来源，不是已确认知识。

不要处理 `_workspace/_system/config/source-scope.json` 中禁用的来源。

### Step 4: 综合回答

默认输出结构：

```markdown
## 直接判断

用 2-5 段回答用户问题，明确给出结论、条件和边界。

## 来自你知识库的依据

- [[概念A]]：...
- [[主题B]]：...
- raw 补充：[[raw/...]] ...

## 知识空白

- 你的 wiki 在 ... 上覆盖不足。
- 如果要进一步判断，下一步应该 digest ... 类型的材料。
```

回答要区分：

- `wiki/`：已确认知识。
- `raw/`：来源证据。
- `_workspace/outputs/`：本次临时使用结果。

### Step 5: 保存输出

如果用户要求留档，或问题明显是一次正式决策，写入 `_workspace/outputs/decide-<slug>-<YYYY-MM-DD>.md`。

输出文件应包含：问题、回答、引用节点、引用 raw、知识空白、日期。

## 原则 / Principles

- 优先用用户已有 wiki，不是通用知识。
- 诚实标记知识空白；空白本身是有价值的信号。
- 可以使用 raw 补充，但不能把 raw 当成已确认判断。
- 不要自动改 wiki；如果发现值得沉淀的 raw，只建议后续 `/digest`。
