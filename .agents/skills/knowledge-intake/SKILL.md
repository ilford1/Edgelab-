---
name: knowledge-intake
description: Capture information the user teaches EdgeLab, preserve its source and epistemic status in a cumulative ledger, and promote durable research knowledge into the graph without turning claims into evidence. Use when the user says to remember, add, ingest, learn from, or build on supplied information over time.
---

# Knowledge Intake

Accumulate useful information in `research/KNOWLEDGE.md`. This is repository knowledge, not a claim that the model's global memory changed.

## Intake

Accept information directly in the prompt or process entries the user placed in `research/KNOWLEDGE.md`.

1. Preserve the user's substantive wording before interpreting it. Allocate the next `KI-YYYYMMDD-NNN` ID for that date.
2. Record capture date, source or provenance, source date when known, supplied information, classification, confidence or uncertainty, relevant topics, and status.
3. Classify the item as one or more of: source teaching, user observation, definition, mechanism proposal, hypothesis, measured evidence, correction, preference, or open question.
4. Use `unverified` when provenance is missing or the source has not been inspected. A URL is provenance, not proof that its contents were verified.
5. Append new entries. Never erase an earlier entry to make the ledger consistent. Corrections and belief changes get a new entry with `Supersedes` or `Related entries`.

If the information is ambiguous, capture it faithfully and list the smallest unresolved question. Do not invent missing venue, instrument, horizon, timestamp, sample, method, or result.

## Integrate

The ledger is the durable raw intake layer. The research graph is the curated layer.

- Keep preferences, operating conventions, rough notes, duplicates, and insufficiently specified claims in the ledger unless they warrant a project-file change explicitly requested by the user.
- For material research knowledge, use `$research-router` to find nearby nodes and duplicates, then use `$research-journal` for any graph write.
- Extend an existing graph node when the new material refines it. Create a node only when the information is genuinely distinct and fits the graph contract.
- Preserve the difference between what the source states, what the user observed, and what EdgeLab infers.
- Do not promote an observation into a hypothesis, a mechanism into evidence, an indicator into an edge, or a reported result into a finding without adequate provenance and method detail.
- Link support or contradiction only when the evidence actually bears on a defined claim. Preserve conflicts side by side.
- Mark the ledger entry `integrated` and list graph node IDs only after the graph transaction validates. Otherwise use `captured`, `held`, or `needs-source` and state why.

## Receipt

After intake, report the entry ID, what was captured, whether it was integrated or held, the reason, and the most useful next piece of information. Keep the receipt concise. Never imply that accumulated knowledge proves a trading edge or constitutes a trade signal.
