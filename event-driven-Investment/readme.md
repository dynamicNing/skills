# Event-Driven Investment Circles

## Overview

Treat "event" as a process of structural break, not a headline. Build a four-layer concentric map from event core to tradable instruments, then output testable long/short choices with risk boundaries.

## Workflow

### 1. Define the event before analyzing

Treat input as an event only when most conditions hold:

- Existing order is breaking (old consensus no longer explains pricing behavior).
- Repricing pressure exists (valuation anchor, discount rate, or cash-flow path is changing).
- Structural path shifts (industry chain, capital routing, policy regime, or risk premium).
- Process nature is visible (`异响 -&gt; 扩散 -&gt; 确认 -&gt; 共识`) rather than one-off noise.

If conditions are weak, state that it is likely "information noise, not structural event", and provide what evidence is still missing.

### 2. Build the concentric circles

#### Circle 0 (Core event)

State:

- What happened and what old assumption is invalid.
- Which stage the event is in (`异响/扩散/确认/共识`).
- Which key variable changed first (policy, demand, supply, rates, liquidity, regulation, geopolitics, technology).

#### Circle +1 (Logic direction)

Infer first-order transmission paths. Use directional language:

- "Raises/lowers growth expectation"
- "Widens/narrows margin"
- "Compresses/expands risk premium"
- "Pulls forward/delays capex cycle"
- "Shifts pricing power upstream/downstream"

#### Circle +2 (Node diffusion)

Map where the direction spreads:

- Macro nodes: growth, inflation, real rates, credit spread, FX, liquidity.
- Industry nodes: upstream materials, core equipment, software/services, distribution channels, end-demand sectors.
- Capital nodes: passive/active flow, policy funds, leverage funding, hedging demand.

For each node, provide:

- Impact sign (`++`, `+`, `0`, `-`, `--`)
- Time lag (`immediate`, `1-3m`, `3-12m`, `12m+`)
- Confidence and key validation datapoint.

#### Circle +3 (Tradable mapping)

Map nodes to instruments and both directions when possible:

- China A-shares
- Hong Kong equities
- U.S. equities
- ETFs / indices
- Derivatives (index futures, options, commodity futures, volatility products, FX proxies)

For each instrument, include:

- `方向` (`Long`/`Short`/`Pair`)
- `逻辑桥` (node -&gt; instrument link)
- `催化` (what will move it)
- `失效条件` (falsification trigger)
- `拥挤度` (low/medium/high)

### 3. Add probability/payoff discipline

For every major thesis, score:

- `Probability` (0-100%)
- `Payoff` (expected upside/downside asymmetry)
- `Time to play out`
- `Data confidence`

Provide at least one opposite-side scenario:

- Base case
- Bull case
- Bear case

State what evidence would force a view update.

### 4. Use sources actively and explicitly

When current or fast-changing information is involved, search before concluding.

Use this sequence:

1. Read the local full source list if available:
   - `搜索信源-主题分组汇总.md` (workspace root)
2. If missing or incomplete, use fallback groups in:
   - [references/source-groups.md](references/source-groups.md)
3. Prioritize primary sources first (official data, regulators, company IR/filings), then media/KOL/sentiment.
4. Cross-check key claims with at least two independent sources.
5. Attach source list with publication dates and direct links.

### 5. Enforce output structure

Always output in this order:

1. `事件判定`
2. `同心圆推演`
3. `投资映射清单`
4. `情景树与动态更新条件`
5. `风险与反例`
6. `信息源`

Use this minimum table format in `投资映射清单`:

| 市场                     | 标的                      | 方向            | 逻辑桥        | 催化               | 失效条件        | 概率 | 赔率                    | 时窗         |
| ------------------------ | ------------------------- | --------------- | ------------- | ------------------ | --------------- | ---- | ----------------------- | ------------ |
| A股/港股/美股/ETF/衍生品 | Ticker or instrument name | Long/Short/Pair | Node -&gt; Asset | Observable trigger | Clear falsifier | %    | High/Med/Low or numeric | Time horizon |

### 6. Apply quality and safety guardrails

- Distinguish facts, inference, and speculation explicitly.
- Avoid fabricating ticker symbols, contract codes, or policy details.
- Mark uncertain mappings as `待验证`.
- Keep tone analytical and falsifiable; avoid deterministic predictions.
- State that output is research analysis, not personalized investment advice.

## Quick start prompt examples

- "Use $event-driven-investment-circles: 美国推出超预期AI算力出口限制，帮我做四层同心圆和可交易映射。"
- "Use $event-driven-investment-circles: 国内地产政策边际转向是否构成事件？给我多空两套方案。"
- "Use $event-driven-investment-circles: 黄金快速突破历史高位，做跨市场标的与衍生品映射。"