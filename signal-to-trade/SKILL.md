---
name: signal-to-trade
description: >
  Event-driven investment analysis using a four-layer concentric circle model. Treats market events
  as structural breaks (not headlines), maps transmission from event core to tradable instruments,
  and outputs long/short theses with probability/payoff discipline and risk boundaries. Use when the
  user wants to analyze a macro/policy/market event for investment implications, build tradable
  mappings across A-shares, HK, US equities, ETFs, or derivatives, or generate multi-scenario
  (base/bull/bear) investment frameworks. Trigger phrases include "事件驱动", "同心圆推演", "多空方案",
  "可交易映射", "signal-to-trade", or any request to analyze a specific event for
  trading/investment implications.
---

# Event-Driven Investment Circles

Treat "event" as a structural break process, not a headline. Build a four-layer concentric map from event core to tradable instruments, then output testable long/short theses with risk boundaries.

## Step 1: Event Qualification

Only treat input as an event when most of these conditions hold:

- Existing order is breaking (old consensus no longer explains pricing).
- Repricing pressure exists (valuation anchor, discount rate, or cash-flow path is changing).
- Structural path shifts (industry chain, capital routing, policy regime, or risk premium).
- Process nature is visible (`异响 → 扩散 → 确认 → 共识`) rather than one-off noise.

If conditions are weak, state: "likely information noise, not structural event" — and list what evidence is still missing.

## Step 2: Four-Layer Concentric Circle Analysis

### Circle 0 — Core Event
- What happened and what old assumption is now invalid.
- Which stage: `异响 / 扩散 / 确认 / 共识`
- Which key variable changed first: policy / demand / supply / rates / liquidity / regulation / geopolitics / technology

### Circle +1 — Logic Direction
Infer first-order transmission using directional language:
- "Raises/lowers growth expectation"
- "Widens/narrows margin"
- "Compresses/expands risk premium"
- "Pulls forward/delays capex cycle"
- "Shifts pricing power upstream/downstream"

### Circle +2 — Node Diffusion
Map where the direction spreads across three node types:

| Node type | Examples |
|---|---|
| Macro | Growth, inflation, real rates, credit spread, FX, liquidity |
| Industry | Upstream materials, core equipment, software/services, distribution channels, end-demand sectors |
| Capital | Passive/active flow, policy funds, leverage funding, hedging demand |

For each node provide: impact sign (`++/+/0/-/--`), time lag (`immediate/1-3m/3-12m/12m+`), confidence level, and key validation datapoint.

### Circle +3 — Tradable Mapping
Map nodes to instruments across markets: A-shares, HK equities, US equities, ETFs/indices, derivatives (index futures, options, commodity futures, volatility products, FX proxies).

For each instrument include: `方向` (Long/Short/Pair), `逻辑桥` (node → asset link), `催化` (observable trigger), `失效条件` (falsification trigger), `拥挤度` (low/medium/high).

## Step 3: Probability / Payoff Discipline

For every major thesis, score:
- `Probability` (0–100%)
- `Payoff` (expected upside/downside asymmetry)
- `Time to play out`
- `Data confidence`

Provide at least three scenarios: **Base case**, **Bull case**, **Bear case** — and state what evidence would force a view update.

## Step 4: Source Research

When current or fast-changing information is involved, search before concluding.

Source priority sequence:
1. Read local full source list if available: `搜索信源-主题分组汇总.md` (workspace root)
2. If missing or incomplete, use fallback groups in: [references/source-groups.md](references/source-groups.md)
3. Prioritize primary sources first (official data, regulators, company IR/filings), then media/KOL/sentiment.
4. Cross-check key claims with at least two independent sources.
5. Attach source list with publication dates and direct links.

## Step 5: Mandatory Output Structure

Always output in this order:

1. **事件判定** — Is this a structural event or noise?
2. **同心圆推演** — Circle 0 → +1 → +2 → +3
3. **投资映射清单** — Table format (see below)
4. **情景树与动态更新条件** — Base/Bull/Bear + what changes the view
5. **风险与反例** — What would invalidate the thesis
6. **信息源** — Sources with dates and links

### 投资映射清单 minimum table format

| 市场 | 标的 | 方向 | 逻辑桥 | 催化 | 失效条件 | 概率 | 赔率 | 时窗 |
|---|---|---|---|---|---|---|---|---|
| A股/港股/美股/ETF/衍生品 | Ticker or instrument name | Long/Short/Pair | Node → Asset | Observable trigger | Clear falsifier | % | High/Med/Low | Time horizon |

## Quality Guardrails

- Distinguish facts, inference, and speculation explicitly.
- Avoid fabricating ticker symbols, contract codes, or policy details.
- Mark uncertain mappings as `待验证`.
- Keep tone analytical and falsifiable; avoid deterministic predictions.
- State that output is research analysis, not personalized investment advice.

## Quick Start Examples

- "Use $signal-to-trade: 美国推出超预期AI算力出口限制，帮我做四层同心圆和可交易映射。"
- "Use $signal-to-trade: 国内地产政策边际转向是否构成事件？给我多空两套方案。"
- "Use $signal-to-trade: 黄金快速突破历史高位，做跨市场标的与衍生品映射。"
