#!/usr/bin/env python3
"""Dependency-free inspection, routing, and session utility for EdgeLab."""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path


REQUIRED_NODE_TYPES = {
    "concept", "signal", "mechanism", "hypothesis", "experiment", "finding",
    "dataset", "regime", "indicator", "strategy", "rejection", "open-question",
}
REQUIRED_RELATIONS = {
    "supports", "contradicts", "tests", "tested_by", "depends_on", "derived_from",
    "confounded_by", "explained_by", "alternative_to", "uses_signal", "observed_in",
    "valid_in_regime", "fails_in_regime", "implemented_by", "supersedes", "related_to",
}
SYMMETRIC_RELATIONS = {"alternative_to", "related_to"}
INVERSE_RELATIONS = {"tests": "tested_by", "tested_by": "tests"}
STOPWORDS = {
    "a", "an", "and", "are", "as", "at", "be", "by", "can", "could", "do",
    "does", "for", "from", "how", "i", "in", "into", "is", "it", "me", "of",
    "on", "or", "our", "the", "this", "to", "what", "when", "with", "would",
}
RELATION_WEIGHT = {
    "supports": 1.0,
    "contradicts": 1.15,
    "tests": 1.0,
    "tested_by": 1.0,
    "confounded_by": 1.1,
    "explained_by": 1.0,
    "alternative_to": 1.0,
    "uses_signal": 0.9,
    "depends_on": 0.8,
    "derived_from": 0.8,
    "observed_in": 0.7,
    "valid_in_regime": 0.8,
    "fails_in_regime": 1.0,
    "implemented_by": 0.6,
    "supersedes": 0.8,
    "related_to": 0.45,
}


def find_root(start: Path | None = None) -> Path:
    current = (start or Path.cwd()).resolve()
    for candidate in (current, *current.parents):
        if (candidate / "research" / "graph" / "index.json").is_file():
            return candidate
    raise FileNotFoundError("Could not find research/graph/index.json in this directory or its parents")


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def load_graph(root: Path) -> dict:
    return load_json(root / "research" / "graph" / "index.json")


def node_map(graph: dict) -> dict[str, dict]:
    return {node["id"]: node for node in graph.get("nodes", [])}


def tokens(text: str) -> set[str]:
    return {
        token for token in re.findall(r"[a-z0-9]+", text.lower())
        if len(token) > 1 and token not in STOPWORDS
    }


def lexical_scores(graph: dict, query: str) -> list[tuple[float, dict]]:
    query_tokens = tokens(query)
    query_upper = query.upper().strip()
    scored: list[tuple[float, dict]] = []
    for node in graph["nodes"]:
        title_tokens = tokens(node["title"])
        tag_tokens = tokens(" ".join(node["tags"]))
        summary_tokens = tokens(node["summary"])
        score = 4.0 * len(query_tokens & title_tokens)
        score += 3.0 * len(query_tokens & tag_tokens)
        score += 1.25 * len(query_tokens & summary_tokens)
        if query_upper == node["id"] or node["id"] in query_upper:
            score += 100.0
        if score > 0:
            scored.append((score, node))
    return sorted(scored, key=lambda item: (-item[0], item[1]["id"]))


def validate(root: Path, graph: dict) -> list[str]:
    errors: list[str] = []
    if graph.get("schema_version") != 1:
        errors.append("schema_version must be 1")
    declared_types = set(graph.get("node_types", []))
    declared_relations = set(graph.get("relation_types", []))
    if declared_types != REQUIRED_NODE_TYPES:
        errors.append(f"node_types mismatch: {sorted(declared_types ^ REQUIRED_NODE_TYPES)}")
    if declared_relations != REQUIRED_RELATIONS:
        errors.append(f"relation_types mismatch: {sorted(declared_relations ^ REQUIRED_RELATIONS)}")

    ids: set[str] = set()
    present_types: set[str] = set()
    for node in graph.get("nodes", []):
        node_id = node.get("id")
        if node_id in ids:
            errors.append(f"duplicate node id: {node_id}")
        ids.add(node_id)
        node_type = node.get("type")
        present_types.add(node_type)
        if node_type not in declared_types:
            errors.append(f"{node_id}: unsupported node type {node_type}")
        for field in ("title", "summary", "status", "tags", "path", "updated"):
            if field not in node:
                errors.append(f"{node_id}: missing field {field}")
        detail_path = root / node.get("path", "")
        if not detail_path.is_file():
            errors.append(f"{node_id}: missing detail file {node.get('path')}")
    missing_examples = REQUIRED_NODE_TYPES - present_types
    if missing_examples:
        errors.append(f"no node instance for types: {sorted(missing_examples)}")

    edge_keys: set[tuple[str, str, str]] = set()
    for edge in graph.get("edges", []):
        key = (edge.get("source"), edge.get("relation"), edge.get("target"))
        if key in edge_keys:
            errors.append(f"duplicate edge: {key}")
        edge_keys.add(key)
        if key[0] not in ids:
            errors.append(f"edge source does not exist: {key[0]}")
        if key[2] not in ids:
            errors.append(f"edge target does not exist: {key[2]}")
        if key[1] not in declared_relations:
            errors.append(f"unsupported edge relation: {key[1]}")
    for source, relation, target in edge_keys:
        inverse = INVERSE_RELATIONS.get(relation)
        if inverse and (target, inverse, source) not in edge_keys:
            errors.append(f"missing inverse edge: {(target, inverse, source)}")
        if relation in SYMMETRIC_RELATIONS and (target, relation, source) not in edge_keys:
            errors.append(f"missing symmetric edge: {(target, relation, source)}")
    return errors


def route(graph: dict, query: str, max_nodes: int) -> list[tuple[float, dict, str]]:
    nodes = node_map(graph)
    lexical = lexical_scores(graph, query)
    if not lexical:
        return []
    seeds = lexical[: min(3, max_nodes)]
    selected: dict[str, tuple[float, str]] = {
        node["id"]: (score, "lexical seed") for score, node in seeds
    }
    adjacency: dict[str, list[dict]] = defaultdict(list)
    for edge in graph["edges"]:
        adjacency[edge["source"]].append(edge)
        adjacency[edge["target"]].append({
            "source": edge["target"],
            "relation": edge["relation"],
            "target": edge["source"],
        })
    candidates: list[tuple[float, str, str]] = []
    for seed_score, seed in seeds:
        for edge in adjacency[seed["id"]]:
            neighbor_id = edge["target"]
            if neighbor_id in selected:
                continue
            rel_score = RELATION_WEIGHT.get(edge["relation"], 0.3)
            score = rel_score * 10.0 + min(seed_score, 10.0) * 0.1
            reason = f"{edge['relation']} {seed['id']}"
            candidates.append((score, neighbor_id, reason))
    for score, neighbor_id, reason in sorted(candidates, key=lambda item: (-item[0], item[1])):
        if len(selected) >= max_nodes:
            break
        if neighbor_id not in selected:
            selected[neighbor_id] = (score, reason)
    ranked = sorted(
        ((score, nodes[node_id], reason) for node_id, (score, reason) in selected.items()),
        key=lambda item: (-item[0], item[1]["id"]),
    )
    return ranked[:max_nodes]


def empty_session() -> dict:
    return {
        "schema_version": 1,
        "topic": None,
        "objective": None,
        "mode": None,
        "seed_nodes": [],
        "loaded_nodes": [],
        "current_hypotheses": [],
        "current_concepts": [],
        "current_experiments": [],
        "unresolved_questions": [],
        "debate": {
            "thesis": None,
            "strongest_support": None,
            "strongest_objection": None,
            "belief_update": None,
        },
        "last_query": None,
        "updated_at": None,
    }


def save_session(root: Path, session: dict) -> None:
    path = root / "research" / "session" / "active-context.json"
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        json.dump(session, handle, indent=2, ensure_ascii=False)
        handle.write("\n")


def print_nodes(items: list[tuple[float, dict]] | list[tuple[float, dict, str]]) -> None:
    for item in items:
        score, node = item[0], item[1]
        reason = item[2] if len(item) == 3 else "lexical match"
        print(f"{node['id']} [{node['type']}/{node['status']}] score={score:.2f} — {reason}")
        print(f"  {node['title']}: {node['summary']}")
        print(f"  {node['path']}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, help="EdgeLab workspace root")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("validate", help="Validate graph invariants and detail paths")

    search_parser = sub.add_parser("search", help="Search compact routing metadata")
    search_parser.add_argument("query")
    search_parser.add_argument("--limit", type=int, default=8)

    route_parser = sub.add_parser("route", help="Select a bounded, relation-aware subgraph")
    route_parser.add_argument("query")
    route_parser.add_argument("--max-nodes", type=int, default=7)

    show_parser = sub.add_parser("show", help="Show one node's routing record")
    show_parser.add_argument("node_id")
    show_parser.add_argument("--detail", action="store_true")

    neighbors_parser = sub.add_parser("neighbors", help="List a node's graph neighbors")
    neighbors_parser.add_argument("node_id")
    neighbors_parser.add_argument("--relation")

    sub.add_parser("session-show", help="Show active session context")
    sub.add_parser("session-clear", help="Reset active session context")
    session_set = sub.add_parser("session-set", help="Set the active subgraph by node ID")
    session_set.add_argument("node_ids", nargs="+")
    session_set.add_argument("--topic")
    session_set.add_argument("--mode")

    args = parser.parse_args()
    try:
        root = (args.root.resolve() if args.root else find_root())
        graph = load_graph(root)
    except (OSError, json.JSONDecodeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    if args.command == "validate":
        errors = validate(root, graph)
        if errors:
            for error in errors:
                print(f"ERROR: {error}")
            return 1
        print(f"OK: {len(graph['nodes'])} nodes, {len(graph['edges'])} edges, all graph invariants satisfied")
        return 0

    if args.command == "search":
        results = lexical_scores(graph, args.query)[: max(args.limit, 0)]
        print_nodes(results)
        return 0 if results else 1

    if args.command == "route":
        results = route(graph, args.query, max(args.max_nodes, 1))
        print_nodes(results)
        return 0 if results else 1

    nodes = node_map(graph)
    if args.command == "show":
        node_id = args.node_id.upper()
        if node_id not in nodes:
            print(f"error: unknown node {node_id}", file=sys.stderr)
            return 1
        print(json.dumps(nodes[node_id], indent=2, ensure_ascii=False))
        if args.detail:
            print("\n--- detail ---\n")
            print((root / nodes[node_id]["path"]).read_text(encoding="utf-8"))
        return 0

    if args.command == "neighbors":
        node_id = args.node_id.upper()
        if node_id not in nodes:
            print(f"error: unknown node {node_id}", file=sys.stderr)
            return 1
        found = False
        for edge in graph["edges"]:
            if args.relation and edge["relation"] != args.relation:
                continue
            if edge["source"] == node_id or edge["target"] == node_id:
                direction = "->" if edge["source"] == node_id else "<-"
                other = edge["target"] if direction == "->" else edge["source"]
                print(f"{node_id} {direction}[{edge['relation']}] {other} — {nodes[other]['title']}")
                found = True
        return 0 if found else 1

    session_path = root / "research" / "session" / "active-context.json"
    if args.command == "session-show":
        print(session_path.read_text(encoding="utf-8"))
        return 0
    if args.command == "session-clear":
        save_session(root, empty_session())
        print("Active session context cleared")
        return 0
    if args.command == "session-set":
        requested = [node_id.upper() for node_id in args.node_ids]
        unknown = [node_id for node_id in requested if node_id not in nodes]
        if unknown:
            print(f"error: unknown nodes: {', '.join(unknown)}", file=sys.stderr)
            return 1
        session = empty_session()
        session["topic"] = args.topic
        session["mode"] = args.mode
        session["seed_nodes"] = requested
        session["loaded_nodes"] = requested
        session["current_hypotheses"] = [node_id for node_id in requested if nodes[node_id]["type"] == "hypothesis"]
        session["current_concepts"] = [node_id for node_id in requested if nodes[node_id]["type"] == "concept"]
        session["current_experiments"] = [node_id for node_id in requested if nodes[node_id]["type"] == "experiment"]
        session["unresolved_questions"] = [node_id for node_id in requested if nodes[node_id]["type"] == "open-question"]
        save_session(root, session)
        print(f"Active subgraph set to: {', '.join(requested)}")
        return 0
    return 2


if __name__ == "__main__":
    raise SystemExit(main())

