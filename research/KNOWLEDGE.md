# EdgeLab Knowledge Ledger

This is the cumulative intake file for information you want EdgeLab to retain inside this repository. Invoke `$knowledge-intake` and paste the information in chat, or add a new entry below and ask EdgeLab to process it.

The ledger preserves raw teachings, observations, corrections, preferences, and sources. An entry is not automatically evidence or a validated edge. Durable research is promoted into the graph only after classification, duplicate checks, and provenance review.

## Status key

- `captured`: safely recorded in this ledger.
- `integrated`: recorded here and linked to one or more validated graph updates.
- `held`: useful, but not suitable for graph promotion yet.
- `needs-source`: missing provenance or details needed to assess the claim.
- `superseded`: retained for history and replaced by a later entry.

## Entry template

Copy this section when writing directly in the file. You may leave fields blank; `$knowledge-intake` will preserve what you supplied and identify what is missing.

```markdown
## KI-YYYYMMDD-NNN — Short title

- Status: captured
- Captured: YYYY-MM-DD
- Source: person, document, URL, dataset, or firsthand observation
- Source date: unknown
- Classification: user observation
- Topics: topic-a, topic-b
- Confidence: unknown
- Supersedes: none
- Related entries: none
- Graph nodes: none

### Supplied information

Paste the information as faithfully as possible.

### Interpretation and limits

Leave blank for EdgeLab, or note what you believe it means and what remains uncertain.
```

## Entries

New entries are appended below this line. Corrections should point back to earlier IDs rather than deleting them.

## KI-20260913-001 — Euan Sinclair on volatility edge, feedback, and execution

- Status: held
- Captured: 2026-09-13
- Source: [Outlier Trading interview with Euan Sinclair](https://www.youtube.com/watch?v=YDA449Fkwj4)
- Source date: 2022-11-08
- Classification: source teaching, mechanism proposal, strategy critique
- Topics: volatility risk premium, options, execution costs, feedback quality, position sizing, retail constraints
- Confidence: high that the interview contains the summarized claims; empirical validity and transfer to crypto are unverified
- Supersedes: none
- Related entries: none
- Graph nodes: none

### Supplied information

The user supplied the video link without a narrower extraction request. Video identity was verified from YouTube metadata as *Find Edge and Trade Volatility with Euan Sinclair | the Outlier Podcast* by Outlier Trading. The available English transcript is auto-generated.

### Source teachings

- Retail and institutional traders face structurally different games. Sinclair argues that institutions can operate specialized, low-margin strategies using scale, infrastructure, and teams that retail traders generally cannot reproduce (approximately 8:25–17:54).
- He presents the volatility risk premium as a persistent tendency rather than a uniform rule. In his account, its magnitude varies with instrument, tenor, index exposure, skew, and event context; the interview provides no dataset or effect estimate (approximately 21:04–28:24 and 32:24–35:10).
- Known uncertainty events may stretch implied volatility before resolution and produce a post-event contraction, but entry and exit timing are event-specific rather than supplied as a universal rule (approximately 25:51–26:31).
- Zero headline commissions do not remove execution costs. Bid-ask spread, financing, forced immediacy, and repeated hedge adjustments can consume an otherwise correct volatility forecast (approximately 28:30–31:48).
- Comparing current implied volatility with recent realized or historical volatility is described as a useful coarse screen, not a like-for-like forecast: the former is forward-looking and the latter backward-looking. Sinclair argues that elaborate time-series modeling may not justify its complexity for a retail trader unless it is genuinely competitive (approximately 35:52–38:16).
- Volatility measures often exhibit mean reversion, but statistically cheap volatility can remain cheap for a long time. The source therefore distinguishes selling unusually rich volatility from buying cheap volatility, for which it says a catalyst is needed (approximately 39:18–40:10).
- Theta is described as exposure bookkeeping rather than an edge. The claimed edge must come from volatility mispricing after accounting for gamma and realized movement (approximately 40:16–41:09).
- Short strangles can create misleading feedback: frequent small wins may coexist with negative expectancy when a rare large loss has not yet appeared. The source favors structures whose outcomes reveal model error sooner (approximately 41:11–43:03).
- Protective wings and other hedges can consume a large fraction of expected value. Sinclair favors sizing and diversification when feasible, while acknowledging that limited retail capital can make a trade unsuitable altogether (approximately 43:03–45:18 and 50:42–53:24).
- A stop rule implicitly assumes that reaching the loss threshold predicts worse future outcomes. The source argues that this assumption can suit a trending process and be wrong for a mean-reverting one; the exit should follow conditional forward dynamics rather than an arbitrary multiple of premium received (approximately 46:06–50:12).

### Interpretation and limits

The most transferable EdgeLab lesson is methodological: identify the actual source of expectancy, examine whether the payoff distribution gives timely diagnostic feedback, and include executable costs and state dynamics before accepting a strategy rule. These are source teachings and plausible research principles, not measured findings from this video.

Graph promotion is held because the interview concerns equity and index options, supplies no reproducible dataset or method, and does not directly test the current crypto microstructure nodes. The nearest routed nodes (`HYP-001`, `MEC-002`, `REG-001`, and `REJ-001`) share only broad ideas such as volatility, costs, and unvalidated-edge discipline. A useful next step would be to formulate one crypto-specific hypothesis—for example, whether negatively skewed short-volatility strategies create misleading validation feedback—and then attach independent data and an execution-aware test.

## KI-20260913-002 — Robot James assorted writings on edge extraction

- Status: integrated
- Captured: 2026-09-13
- Source: [Robot James assorted writings index](https://www.robotjames.blog/)
- Source date: 2020-12-01 through 2023-10-26
- Classification: source teaching, mechanism proposal, research methodology, strategy critique
- Topics: edge extraction, forced flow, price discovery, adverse selection, non-stationarity, execution, capacity, automation
- Confidence: high that the linked writings contain the summarized teachings; mechanism plausibility is moderate; predictive and economic validity are unmeasured
- Supersedes: none
- Related entries: KI-20260913-001
- Graph nodes: MEC-003

### Supplied information

The user asked EdgeLab to inspect the "here are assorted writings" section of `robotjames.blog`. The section is an archive of short practitioner essays and adapted Twitter threads. The material below is a thematic synthesis of the writings most relevant to EdgeLab, not a claim that every example remains current.

### Source teachings

- **Start from the distortion.** Frame an edge as an asset becoming mispriced under a circumstance for a participant-level reason. Identify who trades for reasons other than price, why their flow can overwhelm liquidity, and why competitors have not removed the opportunity.
- **Compete where constraints help you.** Small traders generally cannot win the same low-latency, high-scale game as specialized firms. Less scalable, operationally awkward, capacity-constrained niches may remain available precisely because they are unattractive to larger competitors.
- **Treat forced flow as a mechanism, not a signal label.** Liquidations, rebalances, hedges, urgent inventory transfers, and other price-insensitive flow can dislocate prices when large relative to available liquidity. Whether price reverts depends on information content, absorption, refill, and subsequent flow.
- **Expect adaptation.** Once participants recognize predictable flow, they trade ahead of it and provide liquidity into it. The causal source can persist while the visible return pattern moves earlier, smooths out, or vanishes from naive historical averages.
- **Model executable opportunity, not displayed history.** In illiquid markets, mid-price fills and unconditional availability can reverse the selection process: good quotes disappear in competition while bad quotes remain available. Fill probability, spread, impact, latency, and adverse selection can dominate simulated alpha.
- **Prefer signals that survive turnover.** Forecast strength must be evaluated jointly with persistence, decay across horizons, trading frequency, and costs. A slightly weaker but slower-decaying signal can be more tradable than a jumpy short-horizon predictor.
- **Measure the whole chain.** Track forecast calibration and decay, risk estimates, costs, fills, constraints, and realized performance against simple baselines. Adapt components carefully instead of responding only to aggregate PnL.
- **Separate return prediction, risk, and rebalancing.** Desired exposure comes from return and risk estimates; rebalancing restores that exposure only when the benefit exceeds transaction costs. A special rebalancing rule that appears to create returns may conceal an unmodeled return effect.
- **Capacity is part of the edge.** Performance decay under delayed execution, self-impact as size increases, and the operational burden of scaling across many small markets reveal whether an effect can support meaningful capital.
- **Automate selectively.** Manual review can be the sensing process that reveals decay and changing market structure. Automate stable mechanics, but do not freeze exploratory judgment into a rigid system merely because it looks repetitive.
- **Historical examples require venue-specific skepticism.** The archive discusses cross-venue crypto lead-lag, FTX leveraged-token rebalancing, and manipulation of an old FTX funding-mark formula. These examples illustrate mechanisms; they do not establish that the same implementation or opportunity exists on current venues.

### Interpretation and limits

The corpus strongly matches EdgeLab's existing epistemology: causal participant behavior first, simple measurable hypotheses second, then execution-aware testing. Its most durable new contribution is the explicit upstream mechanism now recorded as `MEC-003`: constrained or price-insensitive flow can create a temporary dislocation, while competition changes how and when that effect appears.

The routed neighbors were `IND-001`, `SIG-001`, `HYP-001`, and `MEC-001`. `MEC-003` is linked to `IND-001` as a candidate explanation for some flow shocks without asserting liquidation identity, and to `MEC-001` because passive absorption determines whether forced flow produces continued impact, saturation, or response decay. No finding or strategy node was created because the writings provide no controlled current-market evidence.

## KI-20260913-003 — Scott Phillips HyperTrend quant Q&A

- Status: integrated
- Captured: 2026-09-13
- Source: [Scott Phillips HyperTrend quant Q&A on X](https://x.com/ScottPh77711570/status/2096760358568628681)
- Source date: 2026-09-07 through 2026-09-09
- Classification: practitioner Q&A, source teaching, mechanism proposal, promotional claim
- Topics: cross-venue price discovery, momentum, activity, capacity, execution, carry, robustness, data quality, operational risk
- Confidence: high that the visible thread contains the paraphrased answers; empirical validity, completeness of nested replies, and current transferability are unverified
- Supersedes: none
- Related entries: KI-20260913-002
- Graph nodes: MEC-003, OQ-001

### Supplied information

The user asked EdgeLab to inspect the questions and answers beneath the supplied X post and observe what is useful. The parent post invited questions about HyperTrend's features, edge, portfolio construction, and implementation priorities. The notes below paraphrase the substantive visible replies; jokes, networking advice, and answers outside the author's stated expertise were excluded.

### Source teachings and claims

- **Cross-venue leadership can improve a local momentum input, but the catch-up window may be inaccessible.** In a reply about Hyperliquid intraday momentum, Phillips recommends taking the reference price from the price-discovery venue—said to be mostly Binance—and trading on the local venue. He also says catch-up effects resolve so quickly that non-market-makers are unlikely to capture them. This is a practitioner claim, not a measured leader-lag result.
- **Activity may persist without establishing direction.** In the abnormal-volume discussion, Phillips says volume is autocorrelated, suggests looking at trade count, and characterizes rising activity as favorable to upward moves. The durable observation is activity clustering; the directional claim remains untested and needs controls for volatility, trend, listing age, and market regime.
- **Capacity belongs inside the signal definition.** For a sub-minute signal, Phillips offers rough starting limits of 5% of average daily volume and 10% of open interest, while calling the latter aggressive. Elsewhere he says some Binance cross-sectional features may be real for a small trader but irrelevant to a larger fund because size cannot be deployed. These are heuristics, not safe universal limits or demonstrated capacity curves.
- **Execution should exploit urgency rather than assume historical mid-price fills.** For building an illiquid-alt position, he recommends patience until an urgent counterparty trades into the desired side. For mean-reversion safety, he emphasizes maximum portfolio weight, position size relative to ADV, time needed to enter and exit, and correlated groups. This reinforces an execution-aware mechanism but supplies no fill model or controlled result.
- **A feature can move, decay, disappear, or return.** Phillips distinguishes a response shifting earlier from an effect merely going dormant, citing cross-sectional momentum as having stopped for roughly a year and later returned. That anecdote motivates monitoring mechanism, timing, and regime separately; it does not establish a reusable rule for declaring an edge alive or dead.
- **Turnover can be reduced with eligibility bands.** In a carry discussion, he suggests not immediately removing an asset when it slips slightly outside the selection rank. This is a plausible hysteresis rule for reducing churn. His accompanying claim that the negative-funding side works better, and the proposed BTC/HYPE hedge, are unverified strategy claims and are not promoted into the graph.
- **Core market features and execution come before expensive alternative data.** He prioritizes trend, momentum, carry, aggression, and execution before paid on-chain or fundamental feeds, partly because vendor data can be poor. His use of Tardis for historical market data is a vendor preference, not proof that its data are complete or correct.
- **Crypto robustness requires adaptation awareness, but the thread understates validation risk.** Phillips argues that limited, changing crypto history reduces the meaning of conventional statistical significance and puts more weight on recent data and time-slice sanity checks. He also suggests inspecting the relationship between a candidate feature and future returns instead of relying only on a path-dependent strategy backtest. EdgeLab retains the useful separation between feature prediction and portfolio path, but rejects the implication that a scatter plot, recent sample, or intuition can replace chronological holdouts, multiple-testing control, baselines, uncertainty estimates, and executable-cost tests.
- **Promotional performance and product-capacity numbers are not evidence.** Claims about Sharpe above 3, roughly $100 million of capacity at Sharpe 3, a ceiling below $500 million, approximately 140 features, or a seasonality feature with Sharpe near 3 are self-reported estimates without definitions, sample periods, holdouts, costs, or independent records. They are preserved only as claims.
- **Operational and counterparty risk can dominate a paper edge.** Phillips repeatedly notes implementation mistakes, hacks, withdrawals, and venue quality as material risks. His broader point is durable: less reputable venues may offer less-contested opportunities precisely because counterparty and operational risk are higher. This is not a recommendation to use such venues.
- **Several answers are hypothesis prompts only.** The thread's remarks about multisig-controlled meme projects, shorting scam-prone coins with a rolling universe, funding deceleration, skew, CEX–DEX arbitrage, and regime switching lack enough definition or evidence for graph promotion.

### Interpretation and limits

The strongest useful synthesis is that a cross-venue signal cannot be judged independently of venue leadership, reaction speed, size, and executable implementation. A local price may visibly catch up to a leader while the monetizable window is already consumed by market makers. This refines `MEC-003` and sharpens `OQ-001`: any cross-venue test should distinguish predictive leadership from executable lag and sweep latency, participation, impact, and fees.

The main unresolved issue is empirical. The thread offers experienced practitioner priors but no reproducible data, exact feature definitions, effect sizes, or live execution records. No finding, validated edge, or strategy node was created.

## KI-20260913-004 — Riding-the-comet speed and density framework

- Status: integrated
- Captured: 2026-09-13
- Source: user commentary, derived from John “Rambo” Moulton's “riding the comet” analogy; original documentary not inspected
- Source date: unknown
- Classification: user observation, definition proposal, mechanism proposal, hypothesis
- Topics: price velocity, trade intensity, volume density, momentum, clustering, exhaustion, scalping, microstructure noise
- Confidence: high that the commentary is preserved faithfully; the proposed interpretation and predictive value are unverified
- Supersedes: none
- Related entries: KI-20260913-002, KI-20260913-003
- Graph nodes: SIG-001, CON-001, OQ-002, IND-004

### Supplied information

> Derived from Moulton “riding comet” analogy, we got microstructure in rawest form that is percentage moved over period of time. This gives clarity in identifying outlier move, momentum, clustering, reversal exhaustion. I use 2 period smoothing.
>
> Microstructure is notorious for its noise (“diddling in the middling”). So we basically need implied trade speed increase, and this is when it's optimal to scalp.
>
> Volume/price moved is thick/thin move differentiation. Density increase = increase market attempt at something, meaning current price is deviation from something people believe in as they rush in to act on a perceived opportunity. HFT liquidity-created structure is noise.

Secondary web sources attribute the comet analogy to trader John “Rambo” Moulton in the *Bulls and Bears* documentary: observed charts are the comet's historical tail, while the trader tries to join the current movement. The user's speed-and-density framework is a new interpretation built from that analogy, not a teaching verified from Moulton himself.

### Interpretation and limits

The framework contains three observables that should remain separate:

1. **Price velocity:** signed or absolute percentage/log-price change divided by a declared clock-time horizon. Two-period smoothing must specify SMA, EMA, or another causal filter. This is a price-derived signal, not microstructure by itself.
2. **Trade or volume intensity:** trades per unit time and quantity/notional per unit time, computed from event timestamps. Price movement alone cannot imply actual trade speed because the same return can arise from one large trade, many small trades, a thin book, or quote changes without trades.
3. **Volume-per-move density:** volume divided by absolute executable-price movement with a denominator floor. High density means much trading for little displacement—consistent with thickness, absorption, two-sided churn, or market making. Its inverse is price response per unit volume; high inverse response is more consistent with a thin or easily displaced market.

The proposed scalp state is plausible but unvalidated: accelerating trade intensity together with unusually high price velocity may identify an active impulse, while continued activity with falling price-response efficiency may describe saturation or exhaustion. Neither state establishes continuation, reversal, or positive net expectancy.

The belief interpretation is too strong without participant evidence. Increased density can reflect disagreement, inventory transfer, liquidation, news processing, passive absorption, or mechanical market making—not necessarily deviation from a shared fundamental belief. Likewise, HFT-created structure can contain noise, liquidity, adverse selection, and genuine price discovery; it should be measured rather than discarded categorically.

`SIG-001` and `CON-001` were refined to preserve these distinctions. `OQ-002` records the testable unresolved question. No finding, validated edge, indicator, or strategy was created.

### Continuation — research indicator

On 2026-09-13 the user explicitly asked to turn this entry into an indicator. `IND-004` now records the new MMT v3 `Comet Speed Density Lab` prototype. It keeps price speed, actual trade activity, and volume-per-move density visible as separate components and labels response fade as an unvalidated research state, not a trade signal.

## KI-20260913-005 — Side-specific book dispersion around taker exhaustion

- Status: integrated
- Captured: 2026-09-13
- Source: user commentary; no external source supplied
- Source date: unknown
- Classification: user observation, mechanism proposal, hypothesis, open question
- Topics: order book, taker activity, spread, depth dispersion, liquidity retreat, replenishment, exhaustion, LTF reversal
- Confidence: unverified; the measure, venue, instrument, horizon, sample, and observed outcomes are unspecified
- Supersedes: none
- Related entries: KI-20260913-004
- Graph nodes: MEC-001, CON-001, OQ-003

### Supplied information

> Think I found an interesting look for LTF reversal points following vol. I'm not HFT, so can't explore too deep into this. Anyways, vol is characterized by increase in book and taker activity. Heavy taking blows open spreads while pull/replace liquidity increases stdev of price depth. If you calculate the latter by side, what you'll find is the book depth opposite side of taking increases (stdev price depth decreases) while the book side where the taking is occurring is pulling liquidity and retreating (stdev price depth increasing). When there's a peak in spread/stdev price depth of the side which is getting taken (spread increases, heavy taker activity; stdev price decreases, taker activity is getting countered), I reckon that's your cue to fade the move.

### Interpretation and limits

The proposed participant sequence is coherent when stated directionally. During aggressive buying, market buys consume asks; nearby ask liquidity may cancel or retreat, ask-side depth may spread farther from the touch, and the quoted spread may widen. Bid-side depth may simultaneously accumulate or concentrate. The sell case is the mirror image.

The candidate reversal information is not the extreme by itself. A stronger real-time sequence would be: taker pressure remains elevated, but the consumed side begins to replenish or concentrate nearer the touch, spread and consumed-side dispersion stop worsening or roll over, and executable price response weakens. That would be consistent with counter-liquidity absorbing the impulse. It still predicts neither reversal nor profitable fading without testing.

“Standard deviation of price depth” is ambiguous. It could mean quantity-weighted dispersion of price levels from the best quote or mid, dispersion of depth quantities across levels, or time-series variability of aggregate depth. These measures can move in different directions. The commentary also says both that consumed-side dispersion peaks/increases and that it decreases when taking is countered. EdgeLab interprets the latter as a proposed rollover after the peak, but preserves this as unresolved rather than silently choosing a formula.

Important alternatives include informed flow that continues through apparent replenishment, spoofed or fleeting displayed depth, ordinary spread recovery, tick-size and depth-band artifacts, asynchronous trade/book timestamps, dropped book events, and mechanically higher dispersion when the best quote is removed. Entering a fade while the spread is widest may also create severe adverse selection and poor executable prices.

`MEC-001` and `CON-001` were refined with the side-specific sequence. `OQ-003` records the unresolved definition and falsification test. No finding, validated reversal edge, indicator, or strategy was created.

## KI-20260913-006 — St. Hubert street-quant carry retrospective

- Status: integrated
- Captured: 2026-09-13
- Source: [St. Hubert street-quant strategy retrospective on X](https://x.com/ArbStHubert/status/2040132619413979596)
- Source date: 2026-04-04
- Classification: source-reported observation, strategy critique, rejection, implementation lesson
- Topics: funding arbitrage, perp-perp, spot-perp, dirty carry, basis, execution, fees, balance management, infrastructure
- Confidence: high that the eight-post thread contains the extracted claims; performance, methodology, costs, and generalizability are independently unverified
- Supersedes: none
- Related entries: KI-20260913-002, KI-20260913-003
- Graph nodes: REJ-002, OQ-001

### Supplied information

The user supplied the X thread for extraction. The author describes conclusions from roughly 6–12 months of trading “street quant” strategies and says approximately four months were spent on cross-venue perp–perp funding arbitrage.

### Source-reported observations

- **Cross-venue perp–perp funding capture failed as a standalone implementation.** The author reports months gaining roughly 3–6%, followed by losses that returned the system to break-even. The stated bottleneck was forecasting the future funding-rate spread while incorporating fees and execution.
- **Adding basis did not repair the forecast.** The author says funding was too noisy for a systematically exploitable forecast and that including basis added complexity without solving the problem. This is a scoped personal result, not evidence that all implementations or regimes fail.
- **Infrastructure and venue operations were material.** Building the initial cross-venue foundation was described as difficult, though reusable modules made later work easier. Venue balance management remained a recurring operational burden.
- **Economic PnL and incentive farming served different objectives.** The failed perp–perp implementation was still described as useful for generating leveraged delta-neutral volume and farming venue points. Points or rewards must therefore be separated from trading PnL when assessing expectancy.
- **Dirty carry was reported more favorably.** After adapting a Scott Phillips outline and trading on Bybit, Gate, Hyperliquid, and Lighter, the author characterizes dirty carry as easy to implement, useful for volume/points, and potentially profitable and reliable. No exact rules, sample, returns, drawdowns, costs, or incentive-adjusted results are supplied.
- **Long spot–short perp was reported as more intuitive and linear.** The claimed return sources were funding plus convergence. The author notes the lack of perp–perp leverage advantage and continued balance-management friction, but calls the approach profitable and reliable without providing records.
- **The author plans to retain spot–perp and dirty carry.** The proposed foundation includes cross-sectional trend following, basic carry, basic mean reversion, and statistical arbitrage before more speculative research.
- **Failed research still produced reusable infrastructure.** The author treats the unprofitable exploration as useful because exchange adapters, balance systems, and strategy modules can be reused. This is an engineering-learning benefit, separate from strategy expectancy.

### Interpretation and limits

The durable lesson is that cross-venue perp funding capture is not riskless arbitrage. It combines a forecast of relative funding at the relevant settlement times with basis risk, asynchronous execution, fees, slippage, margin fragmentation, transfers, venue constraints, and counterparty risk. Being delta-neutral to small price moves does not neutralize these dependencies.

The reported 3–6% months and later giveback are too underspecified to become a finding. It is unknown which venues and contracts were used for the failed implementation, whether PnL included points, how funding was predicted, how positions were sized, which period was tested, and whether fees, financing, slippage, liquidations, and transfers were fully marked.

`REJ-002` preserves the scoped failure of a naive standalone perp–perp implementation and its reopening conditions. It is linked to `OQ-001` because cross-venue transfer and executability depend on venue-specific clocks, data, fees, and liquidity. Dirty-carry and spot–perp claims remain in the ledger only; no finding or active strategy node was created.

## KI-20260914-001 — Polish Quant Momo Engine methodology and claims

- Status: held
- Captured: 2026-09-14
- Source: [Polish Quant Momo Engine thread on X](https://x.com/PolishQuant/status/2098142886369882467?s=20)
- Source date: 2026-09-11
- Classification: source teaching, indicator description, methodology claim, hypothesis, source-reported measured evidence
- Topics: momentum, order flow, feature redundancy, horizon signing, rank IC, walk-forward validation, compression, exhaustion, MMT v3
- Confidence: high that the visible two-post thread and attached chart contain the paraphrased claims; formulas, code, test design, results, and cross-market transfer are independently unverified
- Supersedes: none
- Related entries: KI-20260913-002, KI-20260913-004, KI-20260913-005
- Graph nodes: IND-006 (source-inspired implementation only; evidence status remains held)

### Supplied information

The user asked EdgeLab to inspect the supplied X post. Polish Quant presents the free MMT v3 `Momo Engine` as a composite research/trading display intended to combine momentum, order flow, compression, and exhaustion across timeframes. The visible continuation post describes the author's feature-screening process and its claimed out-of-sample result.

### Source teachings and claims

- **Composite momentum score:** The lower pane is described as a score scaled to approximately ±20, blending volatility-scaled momentum from three horizons with an order-flow input. Price candles reuse the score's directional colour.
- **Compression gate:** A squeeze or coil state dims the score and shades the pane, signaling that the directional read should receive less weight until range expansion.
- **Exhaustion markers:** Yellow and teal triangles mark one capitulation-low or blow-off-high event per extreme. The exact extreme, reset, and confirmation rules are not disclosed.
- **Tape summary:** A live card combines aggressor activity relative to its own baseline with net buy/sell pressure, then maps them to labels such as dormant, balanced, accumulating, distributing, aggressive, or climax.
- **Suggested interpretation:** Rising score through zero plus aligned candle colour and aggressive participation is presented as continuation confluence; a stretched score plus a turn marker is presented as a tiring move; a coil state is presented as a reason to avoid acting.
- **Feature screening:** The author says the first six-factor draft failed screening. On roughly two years and 17,500 hourly BTC bars, candidates were ranked using rank IC in an out-of-sample walk-forward.
- **Redundancy finding:** MACD, RSI, and ROC are reported to have correlations from about 0.80 to 0.97, so treating them as three confirmations would repeatedly count one price-derived factor.
- **Horizon signing:** The author reports shorter-horizon BTC mean reversion and daily-horizon trend, and therefore signs each feature according to its forecast horizon instead of assuming momentum has the same direction at every horizon.
- **Claimed incremental inputs:** Order flow and volume are said to be the only inputs that added information beyond price. The final model is described as a small orthogonal set, with volume demoted to a conviction gate rather than another directional vote.
- **Visual scope:** The attached chart shows BTC on Hyperliquid at 12-hour resolution. The research claim refers to hourly BTC data, while the promotional claim extends to all markets and timeframes.

### EdgeLab assessment

- **Phenomenon — provisional/source-reported:** Feature redundancy among price oscillators is plausible and the stated correlations are directionally credible, but the exact feature variants, windows, sample, and correlation method are absent.
- **Prediction — unmeasured:** No forward target, forecast horizon, rank-IC values, fold-level results, baseline, confidence interval, or decay curve is supplied. An out-of-sample label is not enough to establish prediction.
- **Incremental information — provisional/source-reported:** Screening correlated price factors is good practice. However, the thread does not show neutralized or conditional IC, formal ablations, or whether order flow, volume, volatility, and compression remain incremental to one another. Semantic tape labels must not be counted again as independent confirmation of their underlying inputs.
- **Robustness — unmeasured:** The claim that one normalization is comparable across instruments and timeframes is much broader than the disclosed hourly BTC sample. Venue, test dates, bar construction, parameter search, multiple-testing control, regime stability, and transfer to the displayed 12-hour Hyperliquid chart are unknown.
- **Timeliness — unmeasured:** The design could be causal, but the code is needed to verify multi-timeframe bar alignment, rolling normalization, squeeze thresholds, extreme resets, and whether turn markers repaint or depend on future-confirmed pivots.
- **Economics — unmeasured:** There are no executable entry/exit rules, fills, fees, spread, slippage, latency, impact, turnover, drawdown, or capacity results. The indicator may be useful as a display without establishing a tradable edge.

### Decision and next discriminating evidence

Keep exploratory. The durable lesson is the research discipline—deduplicate correlated price transforms, align feature direction with the forecast horizon, and require non-price inputs to demonstrate incremental value—not the promotional claim that the finished score transfers universally.

The source still does not disclose enough method or evidence to define a finding or validated hypothesis. `IND-006` was subsequently created only as a transparent, source-inspired indicator implementation. The most useful next material remains the author's exact MMT script plus the research notebook or tables showing feature formulas, forward-return target and horizon, walk-forward train/test dates, rank IC by fold, ablations, parameter-search history, and results after executable costs.

### Implementation continuation — 2026-09-14

The user supplied the full visible input menu and asked for a behavioral reconstruction with the EdgeLab Aurora visual system. `indicators/mmt/aurora-momo-engine-replica.mmt` now preserves all 15 supplied labels and defaults. It implements three causal lookback horizons, volatility scaling, horizon-dependent signing, a separately normalized aggressor-flow component, a conviction-only volume gate, compression dampening, one confirmed turn marker per extreme, a live tape summary, painted candles, and a bounded Aurora HUD.

The authenticated MMT v3 editor compiled the exact local source with zero errors and zero warnings, saved it as `Aurora Momo Engine`, attached it to the live BTC/USD Binance futures chart, and rendered its chart and lower-pane visuals. The live input dialog was visually checked against the supplied menu. This establishes implementation and settings parity only. The author’s formulas remain unavailable, so exact numerical parity and the claimed out-of-sample edge are not established.

### Panel-only visual revision — 2026-09-14

The user subsequently narrowed the presentation contract to the lower pane. The current implementation adds a dedicated `Visual` settings tab and a graded Blue / Red palette, while removing the HUD, candle recoloring, exhaustion markers, and main-chart compression shading at the source. The supplied Engine inputs and the score, tape, threshold, and compression computations remain intact. The exact revised source compiled with zero errors and zero warnings, rebuilt on the live chart, and was visually checked with Blue / Red selected. This is a visual-scope revision only and does not change the evidence status of the reconstruction or establish parity with the author's undisclosed formulas.
