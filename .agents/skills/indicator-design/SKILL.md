---
name: indicator-design
description: Design transparent, non-repainting, real-time trading research indicators from defined signals and validated hypotheses, with causal computation and testable states.
---

# Indicator Design

Route the hypothesis, signal definitions, data contract, findings, regimes, and execution constraints. If predictive or real-time evidence is missing, produce a research instrument and label it unvalidated rather than implying a trade signal.

## Specification

Define:

- purpose and decision supported;
- exact causal inputs, timestamps, units, and venue semantics;
- formula/state machine, initialization, warm-up, and reset behavior;
- update cadence and event clock;
- normalization using information available through `t`;
- stale/missing/out-of-order data behavior;
- output scale, raw component display, and confidence/availability state;
- alerts, if requested, as explicit transitions with debouncing/cooldown;
- expected regimes and invalidation/failure states;
- parity tests between historical replay and live incremental computation.

Ban centered smoothing, future pivots, repainting, silent backfill, and thresholds selected solely on the final holdout. Keep numerator/denominator visible for response ratios. Prefer a small set of interpretable states to an opaque composite score.

Trace the indicator to source signals with `derived_from` and from signals with `implemented_by`. An indicator implements evidence; it does not create evidence.

