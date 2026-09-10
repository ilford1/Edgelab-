---
name: research-router
description: Route EdgeLab research questions through the compact knowledge graph, reuse active session context, and load only a small relevant subgraph. Use before broad research-repository reading or when tracing related evidence.
---

# Research Router

Select context; do not conduct the domain analysis itself.

## Route

1. Read `research/session/active-context.json` and `research/graph/index.json` only.
2. Parse the query into task, entities, horizon, market/venue, named IDs, and evidence need.
3. Reuse active nodes when the topic is adjacent. Re-route when the topic or decision changes materially.
4. Choose explicit IDs first, then tag/title/summary matches. `.\tools\graphctl.ps1 route "<query>" --max-nodes 7` can produce deterministic candidates on Windows.
5. Expand the graph one hop along relations that can change the answer. Prioritize `contradicts`, `supports`, `confounded_by`, `explained_by`, `alternative_to`, `tests`, and `tested_by` for claims.
6. Start with 5–8 nodes and load details for only 2–5 material nodes. Expand only when a missing dependency, contradiction, or provenance question matters.
7. State the selected node IDs and why, then hand the subgraph to the relevant skill.
8. Update the active-session file with IDs and concise debate state. Do not copy full node contents into it.

## Task-aware traversal

- Debate: hypothesis, support, contradiction, mechanisms, alternatives, confounders.
- Experiment: hypothesis, signals, datasets, earlier experiments/findings, regimes, confounders.
- Validation: hypothesis/strategy, every supporting and contradicting finding, tested experiments, regimes, execution dependencies.
- Indicator: validated hypothesis, signal definitions, implementation, data dependencies, failure regimes.
- Journal: target nodes, nearby possible duplicates, and relationships being changed.

Stop when another hop is unlikely to alter the conclusion, confidence, or next discriminating test. Never recursively read all detailed notes.

Follow the [graph contract](../../../research/graph/GRAPH_CONTRACT.md). Treat illustrative nodes as architecture fixtures, not evidence.
