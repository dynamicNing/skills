---
name: company-one-pager
description: >
  Generate a concise, structured one-page company overview from any input (company name, stock ticker,
  URL, annual report, or raw notes). Condenses all key company information into a single standardized
  page covering: business model, competitive moat, financials, management, risks, and investment thesis.
  Use when the user asks to "summarize a company", "make a company one-pager", "公司一页纸", "公司概况",
  "一页纸分析", "company overview", "company snapshot", "公司浓缩", or wants a quick yet comprehensive
  company profile for investment research, due diligence, or business analysis.
---

# Company One-Pager Generator

Condense any company's essential information into a single, well-structured one-page overview. Output is a clean, information-dense document suitable for investment screening, business research, or quick briefings.

## Input Handling

Accept any of these inputs — never ask the user to clarify format:

| Input type | How to handle |
|---|---|
| Company name (e.g. "宁德时代") | Web search for latest data |
| Stock ticker (e.g. "300750.SZ") | Search financial data sources |
| URL (annual report, IR page) | Fetch and extract key data |
| Pasted text / uploaded file | Parse directly |
| Vague reference ("that EV battery company") | Infer, confirm if ambiguous |

## Output Format

Generate a structured one-pager in **Markdown** by default. If user requests Feishu doc, HTML, or other format, adapt accordingly.

Use this exact structure — every section is mandatory unless data is truly unavailable:

```
# [Company Name] ([Ticker]) — One-Pager
> Generated: [Date] | Data as of: [Latest available]

## 🏢 Company Snapshot
- **Full Name:** [Legal name]
- **Ticker / Market:** [e.g. 300750.SZ / 深圳创业板]
- **Founded:** [Year] | **HQ:** [City, Country]
- **Industry:** [Sector] → [Sub-sector]
- **Employees:** [Count]
- **Market Cap:** [Amount] | **Latest Price:** [Price]

## 💼 Business Model (What does it do? How does it make money?)
[2-4 sentences max. Revenue composition by segment/product with percentages.]

## 🏆 Competitive Moat
[List 3-5 key competitive advantages, one line each. Be specific, not generic.]

## 📊 Key Financials (Latest FY + 3-year trend)
| Metric | FY[N-2] | FY[N-1] | FY[N] | Trend |
|---|---|---|---|---|
| Revenue | | | | ↑/↓/→ |
| Net Profit | | | | |
| Gross Margin | | | | |
| Net Margin | | | | |
| ROE | | | | |
| Debt/Equity | | | | |
| Free Cash Flow | | | | |

## 👥 Management & Ownership
- **CEO/Chairman:** [Name], [Background in 1 sentence]
- **Top Shareholders:** [Top 3 with %]
- **Insider Ownership:** [% or description]

## 🌍 Industry Position & Competitors
- **Global Market Share:** [X%] — Rank [#N]
- **Key Competitors:** [3-5 names with brief comparison]
- **Industry Tailwinds:** [1-2 sentences]
- **Industry Headwinds:** [1-2 sentences]

## ⚠️ Key Risks
[List 3-5 most material risks, one line each. Prioritize by impact.]

## 💡 Investment Thesis (Bull vs Bear)
**🟢 Bull Case:** [2-3 sentences — why this could be a winner]
**🔴 Bear Case:** [2-3 sentences — why this could disappoint]

## 📌 Catalysts & Upcoming Events
[List 2-4 near-term events that could move the stock/business]
```

## Data Collection Strategy

### Step 1 — Gather core data

Use web search to find:
1. Company official website / IR page
2. Latest financial data (revenue, profit, margins)
3. Recent news and analyst coverage
4. Industry reports and competitive landscape

For A-share companies, prioritize these data sources:
- 东方财富 / 同花顺 for financial data
- 巨潮资讯 for filings
- Wind / iFinD for industry data

For US/HK stocks:
- Yahoo Finance, SEC EDGAR, HKEX
- Bloomberg, Seeking Alpha for analysis

### Step 2 — Cross-validate

Cross-check financial figures from at least 2 sources. Flag any data point with low confidence using `[est.]` marker.

### Step 3 — Synthesize

Fill every section. When exact data is unavailable:
- Use latest available with date noted
- Use estimates with `[est.]` marker
- Write "Data not publicly available" only as last resort

## Quality Standards

1. **Information density** — Every word earns its place. No filler sentences.
2. **Recency** — Always note the date of financial data. Prefer TTM (trailing twelve months) when available.
3. **Objectivity** — Present bull AND bear case fairly. No cheerleading.
4. **Specificity** — "35% gross margin, down from 38% YoY" beats "margins are declining"
5. **Completeness** — All sections filled. Missing data is explicitly noted, never silently omitted.

## Localization

- For Chinese companies: Output in Chinese by default, financial units in 亿元/万元
- For US/global companies: Output in English, units in $B/$M
- Respect user's language preference if specified

## Multi-company Mode

When user provides multiple companies, generate one-pagers sequentially. Add a comparison summary table at the end covering: market cap, revenue, margins, growth rate, and P/E ratio.

## Output Delivery

- **Default:** Reply directly in chat with Markdown
- **If user asks for doc:** Create Feishu doc using `feishu_doc` tool
- **If user asks for file:** Generate `.md` file and upload

## Reference

For detailed industry classification and financial metric definitions, see [references/metrics.md](references/metrics.md).
