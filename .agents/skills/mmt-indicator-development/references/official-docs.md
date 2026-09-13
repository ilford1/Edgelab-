# MMT Scripting v3 official references

Use these official pages as the source of truth. Re-open the manifest for substantial work because the language and catalog are versioned.

## Normative and generated references

- Scripting v3 overview: https://docs.mmt.gg/scripting/v3
- Machine-readable manifest: https://docs.mmt.gg/scripting/v3/machine/manifest.json
- Agent primer: https://docs.mmt.gg/scripting/v3/machine/agent-primer.md
- Built-in catalog JSON: https://docs.mmt.gg/scripting/v3/machine/catalog.json
- Language specification JSON: https://docs.mmt.gg/scripting/v3/machine/language-spec.json
- Diagnostics JSON: https://docs.mmt.gg/scripting/v3/machine/diagnostics.json
- Reference index JSON: https://docs.mmt.gg/scripting/v3/machine/reference-index.json
- Human-readable language reference: https://docs.mmt.gg/scripting/v3/reference
- Built-in catalog: https://docs.mmt.gg/scripting/v3/reference/catalog
- Compiler diagnostics: https://docs.mmt.gg/scripting/v3/reference/diagnostics

The generated reference states that its catalog and diagnostics come from the same normative authority used by the compiler and language service. Prefer those artifacts for exact names and signatures.

## Core guides

- First indicator: https://docs.mmt.gg/scripting/v3/getting-started/first-indicator
- Data and update events: https://docs.mmt.gg/scripting/v3/guides/data-and-events
- Inputs and visuals: https://docs.mmt.gg/scripting/v3/guides/inputs-and-visuals
- Repainting and confirmed values: https://docs.mmt.gg/scripting/v3/guides/repainting
- Performance: https://docs.mmt.gg/scripting/v3/performance

## Order-flow examples

- Intrabar order flow: https://docs.mmt.gg/scripting/v3/examples/intrabar-order-flow
- Large prints: https://docs.mmt.gg/scripting/v3/examples/trade-tape
- Volume-delta absorption: https://docs.mmt.gg/scripting/v3/examples/vd-absorption
- Open-interest regimes: https://docs.mmt.gg/scripting/v3/examples/oi-regimes
- Liquidity profile workstation: https://docs.mmt.gg/scripting/v3/examples/liquidity-profile

The examples establish useful patterns, not proof of predictive value. In the current documentation, individual trades use `subscribe(data.trades, minSize: ...)` with `on <name>.trade(tr)`; candle, volume-delta, and open-interest examples use `data.ohlcv`, `data.vd`, and `data.oi`. Order-book subscriptions are described as pull-only. Verify all exact fields, filters, query methods, retention behavior, and availability in the current catalog before implementation.

## Known semantic traps

- Period sources distinguish completed values from `forming` values.
- `on <period>.update` is live; `on <period>.close` is close-confirmed.
- Earlier values and optional market data can be `null`.
- History indexing looks backward; do not add offsets copied from another language without checking MMT semantics.
- There is no direct `timeframe * int`; convert through seconds with the documented time helpers.
- Multiple subscriptions may have separate handlers; shared runtime values belong in `state`.
- Order-book and volume-profile subscriptions are queried from another source's handler rather than driving their own handler.
- The diagnostics registry documents unsupported constructs and typing rules. Use the reported code instead of trial-and-error syntax invention.
