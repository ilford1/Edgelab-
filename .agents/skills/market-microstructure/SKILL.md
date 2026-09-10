---
name: market-microstructure
description: Analyze short-horizon crypto behavior using trade, quote, order-book, liquidity, inventory, and forced-flow mechanics while identifying data and timestamp limitations.
---

# Market Microstructure

Use this skill for mechanism analysis, not as proof that a pattern predicts returns.

## Mechanism lens

Trace a plausible sequence of participants and constraints: aggressive liquidity consumption, passive provision/replenishment, queue depletion, cancellations, inventory, adverse selection, hedging/arbitrage, stops, liquidations, and cross-venue price discovery.

Prefer **response to flow** over raw activity. Ask what price accomplished relative to aggressive quantity, liquidity consumed, spread, depth, and elapsed event time. Separate contemporaneous description from forward prediction.

## Data reality

For every conclusion identify:

- venue, instrument/contract, tick and lot rules;
- exchange versus receive timestamp and clock alignment;
- aggressor classification method;
- sequence gaps, duplicates, late messages, and book reconstruction quality;
- L1 versus L2/L3 visibility and hidden/iceberg ambiguity;
- consolidated-market lead/lag and exchange-specific effects;
- whether the measurement is available before the target outcome.

Consider clock, trade, volume, price, and liquidity-event time. Do not assume candles are the natural unit. Treat delta, volume, trade count, and imbalance as potentially redundant until incremental evidence exists.

Return the leading mechanism, strongest alternatives, observable implications that distinguish them, and data limitations. Record the mechanism as proposed unless tested evidence supports it.

