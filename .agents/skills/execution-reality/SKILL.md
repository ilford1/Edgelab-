---
name: execution-reality
description: Test whether a measured trading effect remains observable and tradable under executable prices, latency, fees, slippage, queue position, impact, and capacity constraints.
---

# Execution Reality

Route the hypothesis/strategy, signal timing, dataset, indicator implementation, regimes, and relevant findings. Require a declared order type and venue; "enter at the signal price" is not an execution model.

## Reality check

Model or bound:

- signal-computation and network/order latency;
- decision-time bid/ask, spread crossing, and quote staleness;
- maker/taker fees, rebates, funding, and borrow when applicable;
- market-order slippage and depth consumption;
- limit-order queue position, fill probability, adverse selection, partial fills, and cancellations;
- market impact, participation rate, capacity, and opportunity count;
- rejected/duplicate orders, outages, rate limits, and venue rules;
- markout after fill versus after signal to expose fill selection.

Use sensitivity surfaces, not one favorable cost assumption. Compare idealized, plausible, and adverse cases, and identify the break-even cost/latency/capacity. Avoid claiming precision beyond the available book/order data.

An effect may still be useful as a trade filter or avoidance rule when direct entry is not feasible. Return which assumptions dominate economics and what live or replay evidence is needed.

