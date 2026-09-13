---
name: mmt-indicator-development
description: Design, implement, debug, and review custom indicators in MMT Scripting v3. Use for MMT scripts, event-driven market-data subscriptions, plots and panes, order-flow displays, alerts, compiler diagnostics, repainting behavior, or performance work; do not treat an indicator implementation as evidence that a trading edge exists.
---

# MMT Indicator Development

Build against the current official Scripting v3 contract. Read [references/official-docs.md](references/official-docs.md) before writing or correcting syntax. For an exact callable, data source, record field, or diagnostic, consult the current machine-readable catalog rather than guessing from Pine Script or another language.

## Define the indicator contract

Before implementation, establish the minimum facts that change the design:

- What market behavior is measured, and whether it is descriptive, predictive, or a strategy rule.
- Required subscriptions and whether each source is event-driven or pull-only.
- The event that drives each calculation: trade, period open/update/close, or another documented event.
- Whether each output is live/forming or confirmed, its warm-up behavior, and its missing-data behavior.
- Visual outputs, user inputs, alerts, symbol/timeframe scope, and expected history size.

If the request belongs to EdgeLab research, preserve the chain from hypothesis to observable signal to indicator. Use the research and indicator-design skills when needed; this skill only establishes a correct MMT implementation and does not validate predictive or economic value.

## Implement with Scripting v3 semantics

- Declare the script, subscriptions, inputs, surfaces, panes, plots, state, and handlers explicitly.
- Keep work in the handler for the event that actually changes it. Use `state` only to connect handlers or retain runtime values.
- Treat subscription values and history reads as nullable. Preserve absence with a typed nullable value or an early return when zero would be misleading.
- Use confirmed series and close handlers for close-confirmed promises. Use forming values or update/trade handlers only when the output is intentionally live, and label that behavior clearly.
- Use `context.exchange`, `context.symbol`, `context.timeframe`, `context.tickSize`, and related chart context as instantiation constants; chart or configuration changes restart the script.
- Prefer relative or market-scaled thresholds over unexplained fixed contract sizes. Expose only settings that materially change interpretation.
- Subscribe only to data actually used. Filter event streams at subscription time when the documented source supports it.
- Bound rolling collections and entity pools. Reuse stable keyed entities for the same logical object and keep repeated handler work obvious.

For tape or order-flow indicators, keep per-print logic in the documented trade handler and aggregate into a separate state only when a bar-level view is also required. Do not infer a liquidation feed, full-depth event stream, aggressor field, or millisecond clock merely because the concept needs one; verify that MMT exposes the source and exact semantics in the current catalog. If it does not, state the platform limitation and implement only an honest proxy the user accepts.

## Validate

1. Compile in MMT when platform access is available and resolve diagnostics by their stable code using the official registry.
2. Check warm-up, nulls, first-bar behavior, event resets, and missing optional data.
3. Check replay and live behavior separately; confirm forming outputs can change and confirmed outputs do not repaint.
4. Test representative symbols, timeframes, tick sizes, and realistic history. Inspect entity retention and handler cost for event-heavy scripts.
5. Verify plots, panes, tables, markers, and alerts express the declared contract without implying unsupported certainty.

If MMT execution is unavailable, report the result as a syntax-informed draft and do not claim it compiled or ran.

## Deliver

Return the complete script or edited file together with a compact note covering required data, live-versus-confirmed behavior, important defaults, known platform limitations, and the actual validation performed.
