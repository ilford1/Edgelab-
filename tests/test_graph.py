import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
GRAPH = ROOT / "research" / "graph" / "index.json"
GRAPHCTL = ROOT / "tools" / "graphctl.py"


class GraphContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.graph = json.loads(GRAPH.read_text(encoding="utf-8"))

    def run_graphctl(self, *args):
        return subprocess.run(
            [sys.executable, str(GRAPHCTL), "--root", str(ROOT), *args],
            text=True,
            capture_output=True,
            check=False,
        )

    def test_validator_accepts_repository(self):
        result = self.run_graphctl("validate")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("all graph invariants satisfied", result.stdout)

    def test_route_is_small_and_relevant(self):
        result = self.run_graphctl(
            "route", "diminishing price response aggressive buying exhaustion", "--max-nodes", "7"
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        node_lines = [line for line in result.stdout.splitlines() if line and not line.startswith(" ")]
        self.assertLessEqual(len(node_lines), 7)
        self.assertIn("HYP-001", result.stdout)
        self.assertIn("SIG-001", result.stdout)

    def test_every_requested_type_and_relation_is_present(self):
        node_types = {node["type"] for node in self.graph["nodes"]}
        used_relations = {edge["relation"] for edge in self.graph["edges"]}
        self.assertEqual(node_types, set(self.graph["node_types"]))
        self.assertEqual(used_relations, set(self.graph["relation_types"]))

    def test_contradictory_evidence_is_preserved(self):
        relevant = [
            edge for edge in self.graph["edges"]
            if edge["target"] == "HYP-001" and edge["relation"] in {"supports", "contradicts"}
        ]
        self.assertEqual({edge["relation"] for edge in relevant}, {"supports", "contradicts"})

    def test_index_paths_resolve_inside_workspace(self):
        for node in self.graph["nodes"]:
            detail = (ROOT / node["path"]).resolve()
            self.assertTrue(detail.is_relative_to(ROOT))
            self.assertTrue(detail.is_file(), node["path"])


if __name__ == "__main__":
    unittest.main()

