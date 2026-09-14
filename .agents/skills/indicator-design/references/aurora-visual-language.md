# Aurora visual language for MMT v3

Use this reference when an indicator needs a polished, luminous dark-chart presentation similar to an aurora ribbon. This is a visual encoding pattern, not a signal recipe. Preserve the indicator's calculations, confirmation timing, thresholds, and research status.

## Decompose the visual before coding

Map every layer to one job:

- core line: the primary state or center value;
- aura envelope: an indicator-defined range, uncertainty, or state boundary;
- hue: direction or regime, with a neutral transition color when needed;
- HUD: compact state and data-availability summary;
- marker: a sparse, confirmed state transition;
- lower diagnostic pane: a compact histogram plus an optional causal trace around a meaningful reference level.

If a layer has no defined semantic job, omit it. Do not let extra glow, opacity, or width imply stronger confidence.

## Semantic mapping format

Before writing visual code, fill this mapping from the target indicator. Do not carry names or formulas from another indicator.

| Visual role | Target source | Units/scale | Update event | State meaning |
| --- | --- | --- | --- | --- |
| Primary overlay | `[series or state]` | `[price, score, ratio, etc.]` | `[tick, update, close]` | `[what the line means]` |
| Inner/outer bounds | `[existing bounds or justified range function]` | `[same units as overlay]` | `[event]` | `[what being inside/outside means]` |
| Histogram value | `[diagnostic series]` | `[units and visible range]` | `[event]` | `[meaning above/below reference]` |
| Trace value | `[same series smoothed, or named companion]` | `[units]` | `[event]` | `[why the trace is useful]` |
| Marker transition | `[confirmed state change]` | `[timestamp and y location]` | `[event]` | `[exact trigger]` |
| HUD fields | `[state and availability fields]` | `[display units]` | `[event]` | `[decision supported]` |

Then define `stateAColor`, `stateBColor`, and `neutralColor` from those meanings. Do not infer market meaning from the palette itself. If the target indicator has no meaningful bounds, histogram, trace, marker, or HUD field, omit that layer.

## Palette presets

Choose a palette after assigning the target indicator's state meanings. `State A` and `State B` are deliberately semantic placeholders, not predefined market directions.

| Palette | State A | State B | Accent/trace | Neutral | Dark panel |
| --- | --- | --- | --- | --- | --- |
| Aurora Borealis | `#42F0DE` / `rgb(66,240,222)` | `#FF6589` / `rgb(255,101,137)` | `#B27EFF` / `rgb(178,126,255)` | `#8FA3BF` / `rgb(143,163,191)` | `#070C17` / `rgb(7,12,23)` |
| Ice & Ember | `#58C7FA` / `rgb(88,199,250)` | `#FF8A5B` / `rgb(255,138,91)` | `#B7A6FF` / `rgb(183,166,255)` | `#9BA8B8` / `rgb(155,168,184)` | `#09101A` / `rgb(9,16,26)` |
| Electric Orchid | `#52E3C2` / `rgb(82,227,194)` | `#F05BD7` / `rgb(240,91,215)` | `#8E7CFF` / `rgb(142,124,255)` | `#A0A7B8` / `rgb(160,167,184)` | `#0A0B18` / `rgb(10,11,24)` |
| Solar Flare | `#F7D154` / `rgb(247,209,84)` | `#FF5A7A` / `rgb(255,90,122)` | `#FF9E64` / `rgb(255,158,100)` | `#AAB3C2` / `rgb(170,179,194)` | `#110C12` / `rgb(17,12,18)` |
| Polar Night | `#55D6FF` / `rgb(85,214,255)` | `#9B7BFF` / `rgb(155,123,255)` | `#E7F0FF` / `rgb(231,240,255)` | `#91A0B5` / `rgb(145,160,181)` | `#07111B` / `rgb(7,17,27)` |

Use Aurora Borealis as the default when the user asks for this visual style without specifying a palette. Offer the other presets as inputs, plus a custom mode when the indicator already exposes colors.

### Intensity ramp

Keep the base RGB stable and grade alpha by visual role:

| Layer | Suggested alpha |
| --- | --- |
| Background wash | 4-8 |
| Outer boundary or bloom | 12-30 |
| Inner fill | 28-48 |
| Glow line | 55-90 |
| Quiet histogram bar | 90-130 |
| Normal histogram bar | 140-190 |
| Core line or marker | 225-255 |

For continuous signed or state-ordered values, build a role-based scale rather than hard-coded market labels:

```mmt
stateScale = color.scale(
  at: [-100.0, -50.0, 0.0, 50.0, 100.0],
  colors: [stateBPeak, stateBMid, neutralColor, stateAMid, stateAPeak],
  space: colorspace.rgb,
  easing: easing.smootherstep,
)
```

Map the scale domain to the target indicator's declared range. Color intensity encodes magnitude only when magnitude is an actual indicator variable; it must never manufacture confidence. Preserve visible neutral values and check that the states remain distinguishable by luminance as well as hue.

## Layered bloom

MMT has no special bloom shader. Produce the glow by plotting the same causal series three times, from back to front:

```mmt
plot (
  bloom = plot.line(title: "Bloom", width: 9.0, showLabel: false, showValue: false)
  glow = plot.line(title: "Glow", width: 4.8, showLabel: false, showValue: false)
  core = plot.line(title: "Core", width: 1.7)
)

on chart.close {
  bloom.plot(primaryValue, color: color.withAlpha(stateColor, 16))
  glow.plot(primaryValue, color: color.withAlpha(stateColor, 72))
  core.plot(primaryValue, color: color.withAlpha(stateColor, 245))
}
```

Starting ranges:

- outer bloom: width 8-10, alpha 10-25;
- inner glow: width 4-6, alpha 50-90;
- core: width 1.4-2.0, alpha 220-255.

Keep all three layers on the exact same value. Width and opacity create depth; different values would change the meaning.

## Nested aura bands

Use one or two declared envelopes derived from the target indicator's existing range semantics. This may be a statistical band, uncertainty interval, state boundary, or price range. Do not introduce a new range calculation merely to obtain the look. Draw low-alpha boundary lines and place gradient fills between each upper/lower pair.

```mmt
fill aura = fill.between(upperPlot, lowerPlot)

on chart.close {
  aura.fill(
    topValue: upperBound,
    bottomValue: lowerBound,
    topColor: color.withAlpha(stateAColor, 10),
    bottomColor: color.withAlpha(stateBColor, 42),
  )
}
```

Use alpha about 18-30 for outer boundaries and 45-70 for inner boundaries. Two fills are usually enough. Keep candles legible and avoid opaque blocks.

## Compact diagnostic pane

Use a short separate pane when a target diagnostic should remain visible without competing with the primary chart. The reusable format combines thin histogram bars with an optional softly glowing causal trace. Center it on zero only when zero has real semantic meaning; otherwise use the indicator's declared neutral or reference level.

```mmt
pane signalPane = pane(title: "[TARGET PANE TITLE]", height: 0.16)

plot (
  stateAWash = plot.histogram(title: "State A tint", showLabel: false, showValue: false, on: signalPane)
  stateBWash = plot.histogram(title: "State B tint", showLabel: false, showValue: false, on: signalPane)
  valueBars = plot.histogram(title: "[TARGET VALUE]", showLabel: false, showValue: false, on: signalPane)
  traceGlow = plot.line(title: "Trace glow", width: 5.0, showLabel: false, showValue: false, on: signalPane)
  traceCore = plot.line(title: "[TARGET TRACE]", width: 1.6, on: signalPane)
  referenceLine = plot.line(title: "[REFERENCE LEVEL]", width: 0.7, showLabel: false, showValue: false, on: signalPane)
)

on chart.close {
  stateAWash.plot(upperVisibleBound, color: color.withAlpha(stateAColor, 6))
  stateBWash.plot(lowerVisibleBound, color: color.withAlpha(stateBColor, 6))
  valueBars.plot(diagnosticValue, color: color.withAlpha(barStateColor, 145))
  traceGlow.plot(traceValue, color: color.withAlpha(traceColor, 55))
  traceCore.plot(traceValue, color: color.withAlpha(traceColor, 225))
  referenceLine.plot(referenceValue, color: color.withAlpha(neutralColor, 34))
}
```

Design rules:

- keep pane height near 0.12-0.18;
- use a declared visible range with 10-20% headroom; make it symmetric only for meaningfully signed data;
- assign palette roles from the target state semantics rather than assuming teal means positive and magenta means negative;
- keep backdrop washes extremely faint so they read as atmosphere, not data;
- render histogram bars at medium alpha and the smoothed trace as a 5 px glow plus 1.4-1.8 px core;
- use a brighter reference line than the background, but weaker than the data;
- smooth causally with current-and-prior observations only, and expose the smoothing length;
- if bars and line represent different quantities, name both and document their units instead of implying they are interchangeable.

The histogram should retain small neutral observations rather than disappearing. Grade opacity or color intensity by magnitude, but keep bar height tied to the actual diagnostic value.

## Fixed HUD card

Build the card with a small `boxPool(anchor: anchor.topLeft)` and `labelPool(anchor: anchor.topLeft)`. Use one dark panel, an optional low-alpha shadow, one thin accent border, and a compact monospaced text hierarchy.

Recommended starting values:

- panel alpha 230-245;
- shadow or bloom alpha 10-20;
- border width 1 and accent alpha 110-160;
- title 12-14 px, state 10-12 px, metadata 8-10 px.

The HUD should report only decision-relevant fields defined in the semantic mapping, such as state, component balance, availability, and confirmation status. Use the target indicator's terminology and units. Clear every keyed entity when the HUD is disabled.

## Halo markers

Create a halo and core at the same timestamp and y-coordinate using stable keys. The halo is larger and translucent; the core is small and opaque. Plot only the confirmed transition defined in the semantic mapping. Do not invent a crossover, threshold, or divergence merely to create markers.

## Performance and causality

- Use bounded pools with explicit maximums and stable keys.
- Avoid unbounded per-tick entities and decorative objects for every bar.
- Use only information available through the event timestamp.
- Distinguish forming from close-confirmed states.
- Keep raw diagnostics available even when the default view is compact.
- Do not use future pivots, centered smoothing, or visual offsets that make a signal appear earlier.

## Verification gate

Before adopting the style:

1. Compile with 0 errors and 0 warnings against the authenticated current catalog.
2. Add it to a live chart and visually inspect only the selected overlay, bands, HUD, markers, and diagnostic-pane layers.
3. Pan, zoom, and change timeframe; confirm the HUD stays fixed and the diagnostic pane retains its declared scale and reference level.
4. Test warm-up, missing data, neutral values, extremes, and disabled-layer states.
5. Compare raw output, transitions, and alerts before and after styling; they must be unchanged.
6. Check replay/live parity separately. A successful render is not predictive or economic evidence.

## Official MMT references

- Inputs and visual configuration: <https://docs.mmt.gg/scripting/v3/guides/inputs-and-visuals>
- Plot lines and gradient fills: <https://docs.mmt.gg/scripting/v3/reference/catalog/plot>
- Color alpha and scaling: <https://docs.mmt.gg/scripting/v3/reference/catalog/color>
- Anchored bounded entity pools: <https://docs.mmt.gg/scripting/v3/reference/catalog/entities>
- Official viewport-HUD example: <https://docs.mmt.gg/scripting/v3/examples/viewport-hud>
