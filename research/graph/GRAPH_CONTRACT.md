# EdgeLab graph contract

This file defines the stable abstraction between EdgeLab's reasoning and the current file-backed storage.

## Stable interface

A node has an immutable unique ID, one supported type, a routing-sized title and summary, a status, tags, a path to detailed Markdown, and an update date. An edge is a directed triple `(source, relation, target)` with an optional short note.

The graph index is discovery metadata, not the research corpus. Do not put full evidence, long arguments, tables, or code in it. Detailed content belongs at the node's `path`.

## Supported node types

- `concept`: a stable definition or analytic construct.
- `signal`: an observable, time-indexed measurement.
- `mechanism`: a participant-level causal account.
- `hypothesis`: a falsifiable predictive claim.
- `experiment`: a test design or executed test.
- `finding`: a result with provenance and uncertainty.
- `dataset`: a versioned data source and quality description.
- `regime`: a defined market state used for conditioning.
- `indicator`: a real-time implementation of one or more signals.
- `strategy`: rules intended to monetize or avoid risk from an edge.
- `rejection`: preserved record of a failed or abandoned idea.
- `open-question`: a material unresolved question.

## Supported relation types

`supports`, `contradicts`, `tests`, `tested_by`, `depends_on`, `derived_from`, `confounded_by`, `explained_by`, `alternative_to`, `uses_signal`, `observed_in`, `valid_in_regime`, `fails_in_regime`, `implemented_by`, `supersedes`, and `related_to`.

Use the listed relation vocabulary exactly. Put nuance in the edge note or detailed node rather than inventing near-synonyms.

Defined inverse pairs:

- `tests` <-> `tested_by`
- `implemented_by` is represented from research object to implementation; use `derived_from` from the implementation back to its evidence or specification.
- `alternative_to` and `related_to` are symmetric and should normally be stored in both directions.

Evidence edges are intentionally directional: a finding `supports` or `contradicts` a hypothesis. Do not add invented inverse relation names.

## Retrieval invariant

Read `index.json` and `research/session/active-context.json` first. Select seed nodes by explicit ID, exact tags, and lexical similarity. Traverse only relations relevant to the task and cap the initial subgraph. Load detailed Markdown only after a node survives routing. Expand one hop at a time and stop when another node is unlikely to change the answer, confidence, or next test.

The active session is a cache, not evidence. It may prioritize adjacent-turn nodes but must not override the graph or the user's current topic.

## Update invariant

- Never delete or rewrite contradictory evidence merely to make the graph consistent.
- Never change a rejection back into an active hypothesis without adding a new reason, date, and `supersedes` relationship where appropriate.
- Prefer extending an existing node over creating a duplicate.
- Findings must identify evidence provenance and distinguish measured results from inference or illustration.
- Record what was knowable at decision time. Retrospective labels must be marked as such.
- A strategy cannot inherit stronger evidence than its weakest essential dependency.
- Update the detailed note and index atomically within the same change, then validate.

## Migration boundary

A future adapter may store nodes and edges in SQLite, Neo4j, embeddings, or a hybrid system. It must preserve IDs, types, relation semantics, summaries, detail references, provenance, and bounded traversal behavior. Skills should request nodes by this contract rather than depend on JSON formatting.

