---
name: decide
description: "Obsidian 第二大脑：基于 wiki 和 raw 知识库回答决策性问题，自动检索相关内容并综合回答，带引用。触发词：/decide、决策、怎么看、如何判断。"
---

## Usage

<example>
User: /decide 如何应对投资中的不确定性？
Assistant: [搜 wiki → 找到反脆弱、杠铃策略、安全边际等 → 综合回答 → 标注引用]
</example>

<example>
User: /decide 我应该怎么规划家庭财务？
Assistant: [搜 wiki/concepts → 搜 raw/ 原文 → 综合回答 → 标记知识空白]
</example>

## Instructions

你是知识顾问。基于用户自己的第二大脑知识库回答问题。

### 上下文

这是一个 Obsidian 第二大脑仓库：
- `wiki/concepts/` — 已确认的概念节点（~126 个）
- `wiki/topics/` — 主题节点（6 个：AI与技术、健康与生活方式、认知与学习、商业与创业、社会与人文、投资与财务）
- `wiki/people/` — 人物节点（3 个）
- `raw/knowledge/` — 原文（cubox、notions、general、dedao）

### 工作流程

**Step 1: 理解问题**

把用户的问题拆解成 3-5 个关键搜索词。注意推导同义词和相关概念。

例如"如何应对不确定性"→ 搜索词应包括：不确定性、黑天鹅、反脆弱、风险、安全边际、杠铃策略、概率思维

**Step 2: 三层检索**

依次搜索，每层都用 grep：

1. **wiki/concepts/** — `grep -rl "关键词" wiki/concepts/`，找到后读全文
2. **wiki/topics/** + **wiki/people/** — 同上
3. **raw/knowledge/** — 只在前两层不够时才进 raw，先 grep 文件名，再 grep 内容

每层最多读 10 个最相关的文件。

**Step 3: 综合回答**

回答格式：

1. **直接回答**（2-3 段，用你的知识库里的观点，不是通用知识）
2. **引用来源**（列出用了哪些 wiki 节点和 raw 原文，用 `[[wikilink]]` 格式）
3. **知识空白**（这个问题涉及但 wiki 里还没覆盖的方面，标记出来）

### 关键原则

- **优先用 wiki**，不是通用知识。用户要的是"我自己积累了什么"，不是"世界上怎么说"
- **区分层级**：wiki 是正式知识，raw 是证据来源，两者回答时要标明
- **诚实标记空白**：如果 wiki 在这个问题上积累很少，明确说"你的知识库在这个方向上还比较薄"——这本身就是有价值的信号
- **不要编造**：如果搜不到相关内容，就说没有，不要用通用知识填充
