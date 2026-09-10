---
name: research-journal
description: Persist EdgeLab research as versionable graph nodes and typed edges, update active context, preserve provenance, contradictions, rejections, and belief changes, and validate graph integrity.
---

# Research Journal

Use for durable research changes. Follow the [graph contract](../../../research/graph/GRAPH_CONTRACT.md) and templates under `research/templates/`.

## Before writing

Route by title, tags, and nearby relations to detect duplicates. Decide whether the result extends an existing node, creates genuinely new knowledge, narrows a claim, or supersedes a prior formulation.

## Write transaction

1. Allocate the next stable ID for the correct node type. Never recycle IDs.
2. Write or update the detailed Markdown with evidence/decision provenance, information-time boundary, uncertainty, failures, and artifact references.
3. Add or update the compact routing entry in `research/graph/index.json` without copying full notes.
4. Add only supported typed edges. Add required inverse or symmetric edges.
5. Preserve every material supporting, null, and contradictory finding. Do not overwrite a prior result with a newer one.
6. Preserve rejected ideas with the reason, decisive evidence, scope, and reopening conditions. Link narrower successors using `supersedes` when warranted.
7. Update `research/session/active-context.json` with IDs and a concise belief update; do not place evidence there.
8. Run `.\tools\test.ps1` on Windows, or the equivalent Python commands elsewhere.

Measured results must identify experiment and dataset versions, sample dates, code/config/artifacts, effect and uncertainty, baselines, holdout status, costs, and known failure regimes. If any are missing, mark the finding provisional or incomplete.

Do not manufacture a graph update merely to finish the loop. Update durable memory only when research produced a meaningful definition, hypothesis, design, result, decision, rejection, or open question. The user's explicit scope controls what may be changed.
