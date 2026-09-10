---
name: feature-engineering
description: Turn microstructure concepts into causal, real-time, testable features while controlling scale, redundancy, missingness, instability, and implementation leakage.
---

# Feature Engineering

Route the concept/hypothesis, source signals, data contract, confounders, and prior findings. A feature is a measurement candidate, not evidence.

## Feature card

Define:

- mathematical formula, units, sign convention, and expected range;
- event/clock window and update cadence;
- source fields, venue semantics, and timestamp availability;
- causal normalization and warm-up;
- denominator floors, clipping, missing/stale data, and reset behavior;
- computational complexity and latency;
- invariances and expected failure regimes;
- simpler parent features and correlated alternatives;
- leakage and repainting tests.

Prioritize levels, changes, response ratios, efficiency, elasticity, acceleration/deceleration, persistence, decay, saturation, and state transitions only when they express the mechanism. Inspect numerator and denominator separately to detect mathematical coupling.

Test incremental value with ablation/nested baselines and stability under nearby windows and scales. Do not count delta, aggressive volume, and trade count as independent confirmation without evidence. Prefer an interpretable primitive when a complex transform adds no stable holdout information.

