---
name: experiment-design
description: Design falsifiable, leakage-safe experiments for trading hypotheses with causal timestamps, baselines, holdouts, robustness checks, and reproducible decision rules.
---

# Experiment Design

Route the target hypothesis, signal definitions, prior experiments/findings, datasets, regimes, alternatives, and confounders first.

## Design contract

Specify:

- the decision the experiment will change;
- causal event definition and exact information set at time `t`;
- unit of observation, overlap handling, sample construction, and exclusions;
- independent variables, outcomes, horizons, controls, and conditioning;
- null, alternative explanations, and simple baselines;
- development, validation, chronological holdout, and transfer samples;
- effect-size and uncertainty measures suited to dependence/heavy tails;
- multiple-testing and researcher-degrees-of-freedom controls;
- robustness to parameters, time scales, venues, instruments, and regimes;
- executable price and cost model when the claim is economic;
- dataset/code/config versions and artifacts needed to reproduce the run.

Audit look-ahead in pivot/impulse labels, centered windows, normalization, data cleanup, and selection. Use retrospective labels only as outcomes or clearly separated research labels.

Predeclare promotion, narrowing, rejection, and inconclusive criteria. A test that cannot plausibly falsify the claim is exploratory analysis, not validation. Use `research/templates/experiment.md` for durable designs.

