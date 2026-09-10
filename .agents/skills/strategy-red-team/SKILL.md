---
name: strategy-red-team
description: Try to falsify or break a proposed trading strategy through statistical, regime, dependency, execution, operational, and incentive-aware failure analysis.
---

# Strategy Red Team

Load the strategy and trace every essential dependency back through indicators, signals, hypotheses, experiments, findings, datasets, and regimes. A strategy cannot be better validated than its weakest essential dependency.

## Attack surface

- Hidden look-ahead, outcome-conditioned events, leakage, and survivorship.
- Threshold/window overfit, multiple testing, unstable interactions, and redundant filters.
- Regime/venue/instrument concentration and adverse structural change.
- Unrealistic fills, latency, spread, fees, slippage, impact, queue, funding, and capacity.
- Signal crowding, decay after publication/deployment, and participant adaptation.
- Data gaps, stale state, clock drift, book corruption, exchange outages, and operational recovery.
- Risk concentration, tail loss, path dependency, drawdown, and correlated simultaneous positions.
- Ambiguous rules that make replay and live behavior diverge.

Construct the strongest survival case as well as the strongest failure case. Rank attacks by probability times damage and by how cheaply they can be tested.

Define kill criteria, degradation alerts, safe-disable behavior, and evidence that would restore confidence. Preserve failures as findings/rejections; do not tune them away after seeing the holdout.

