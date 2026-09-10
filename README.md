# EdgeLab

EdgeLab is a local Codex workspace for adversarial research into short-horizon crypto and market microstructure. Its small core lives in `AGENTS.md`; reusable methods live in repository-scoped skills; persistent research lives in a typed, file-backed graph.

The design follows Codex's native project conventions:

- `AGENTS.md` supplies the workspace agent's defining behavior.
- `.agents/skills/<skill>/SKILL.md` supplies progressively loaded methods.
- `research/graph/index.json` is the compact routing index.
- `research/**/<NODE-ID>.md` contains detailed notes loaded only when relevant.
- `research/session/active-context.json` caches the active subgraph between adjacent turns.

No separate "custom agent" configuration format is assumed. Open Codex in this folder (or start a new task rooted here) and the project instructions and skills are discovered automatically. Restart or open a new task after changing `AGENTS.md` if an existing task has already loaded its instruction chain.

## Mental model

```text
query
  -> compact graph index
  -> seed nodes + relation-aware expansion
  -> small active subgraph
  -> relevant skill
  -> reasoned answer
  -> append/update graph with provenance
```

The storage adapter is deliberately simple. Node IDs, node types, relation types, summaries, paths, and provenance form the stable conceptual contract. A later SQLite, Neo4j, or vector-backed implementation can expose the same contract without changing how EdgeLab reasons.

## Start using it

From this folder, ask naturally or invoke a skill explicitly:

```text
Debate mode: I think aggressive buying with falling price response predicts reversal.

$research-router find the smallest subgraph relevant to absorption near impulse exhaustion.

$edge-hypothesis turn this observation into a falsifiable hypothesis.

$experiment-design design a leakage-safe test using event time.

$edge-validation audit HYP-001 and tell me what is still unproven.

$indicator-design specify a real-time indicator without using future pivots.

$strategy-red-team try to destroy the proposed strategy after costs.

$research-journal record this result and preserve the conflicting finding.
```

Conversational modes are routing shortcuts, not hidden configuration:

- **Debate mode** invokes adversarial debate and maintains a live thesis/counter-thesis.
- **Hypothesis mode** formalizes observations without jumping to a strategy.
- **Experiment mode** creates a falsifiable, leakage-safe design.
- **Validation mode** audits predictive, incremental, robust, and economic evidence.
- **Indicator mode** maps validated signals to causal, real-time computations.
- **Red-team mode** searches for execution, regime, and statistical failure.
- **Journal mode** writes durable graph updates after you approve or request recording.

## Graph commands

The dependency-free helper reads and validates the graph without scanning detailed notes:

```powershell
.\tools\graphctl.ps1 validate
.\tools\graphctl.ps1 search "price response aggressive buying"
.\tools\graphctl.ps1 route "Could diminishing price response imply exhaustion?" --max-nodes 7
.\tools\graphctl.ps1 show HYP-001
.\tools\graphctl.ps1 neighbors HYP-001 --relation contradicts
.\tools\graphctl.ps1 session-show
.\tools\graphctl.ps1 session-set HYP-001 SIG-001 MEC-001
.\tools\graphctl.ps1 session-clear
```

The PowerShell wrapper uses a normal Python installation when available and falls back to Codex's bundled Python runtime. On other platforms, call `python tools/graphctl.py ...` directly.

`route` performs lexical seed selection followed by bounded, relation-weighted traversal. It is deterministic and intentionally modest: the research skill applies judgment about whether another hop would materially change the answer.

## Repository map

```text
AGENTS.md                         small EdgeLab identity
.agents/skills/                   modular methods
research/graph/index.json         routing summaries + typed edges
research/graph/schema.json        machine-readable contract
research/graph/GRAPH_CONTRACT.md  invariants and migration boundary
research/session/                 reusable active subgraph
research/templates/               node and study templates
research/<node-type>/             detailed notes
tools/graphctl.py                  search, route, inspect, validate
tests/                            structural and adversarial behavior checks
```

## Adding research

1. Route first and check for an existing node that should be extended.
2. Create or revise the detailed Markdown note.
3. Add or update its compact index entry and typed edges.
4. Add inverse edges where the relationship has a defined inverse.
5. Preserve conflicting findings and rejected hypotheses as first-class nodes.
6. Record evidence origin, time availability, dataset/version, and uncertainty.
7. Run `.\tools\test.ps1` (or the equivalent Python commands on another platform).

Use the templates in `research/templates/`. The worked example in the initial graph is explicitly illustrative; it is architecture test data, not evidence of a trading edge.

## Safety and scope

EdgeLab is a research system, not an autonomous trader. It may analyze supplied or retrieved data and design experiments. It must not fabricate results, place trades, enable alerts, or mutate external systems unless a user explicitly requests and authorizes the specific action.
