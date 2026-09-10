---
name: edge-validation
description: Audit whether a trading hypothesis has predictive, incremental, robust, real-time, and economically exploitable evidence; grade gaps without collapsing them into one score.
---

# Edge Validation

Load the claim plus all linked supporting and contradictory findings, tested experiments, datasets, regimes, rejections, and execution dependencies. Do not validate from summaries alone when detailed provenance affects the judgment.

## Evidence lanes

Assess separately:

1. **Phenomenon:** reliably observed with credible measurement.
2. **Prediction:** changes a future outcome distribution versus a declared baseline.
3. **Incremental information:** adds value beyond momentum, volatility, spread, activity, and correlated features.
4. **Robustness:** survives holdout, parameter perturbation, regimes, venues, and sample choices.
5. **Timeliness:** is observable and computable before the opportunity.
6. **Economics:** survives executable prices, fees, spread, slippage, latency, impact, and capacity.

For each lane cite the specific experiment/finding node, contrary evidence, and unresolved gap. Use `unmeasured`, `failed`, `mixed`, `provisional`, or `supported` rather than an arbitrary composite score unless requested.

Check selection, look-ahead, leakage, overfit thresholds, nonstationarity, overlapping observations, multiple testing, and effect uncertainty. Mechanistic plausibility can prioritize research but cannot replace predictive evidence.

End with one of: reject, narrow, keep exploratory, retest, provisionally validate, or ready for execution-aware prototyping. State the next test most likely to change that decision.

