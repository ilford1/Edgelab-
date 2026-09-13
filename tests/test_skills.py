import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = ROOT / ".agents" / "skills"
EXPECTED = {
    "adversarial-debate",
    "edge-hypothesis",
    "market-microstructure",
    "mmt-indicator-development",
    "experiment-design",
    "edge-validation",
    "feature-engineering",
    "execution-reality",
    "strategy-red-team",
    "indicator-design",
    "knowledge-intake",
    "research-journal",
    "research-router",
}


def parse_simple_frontmatter(content: str) -> dict[str, str]:
    match = re.match(r"^---\n(.*?)\n---\n", content, re.DOTALL)
    if not match:
        raise AssertionError("missing or malformed YAML frontmatter")
    values = {}
    for raw_line in match.group(1).splitlines():
        if not raw_line.strip():
            continue
        key, separator, value = raw_line.partition(":")
        if not separator:
            raise AssertionError(f"malformed frontmatter line: {raw_line}")
        values[key.strip()] = value.strip().strip('"').strip("'")
    return values


class SkillPackageTests(unittest.TestCase):
    def test_expected_skill_set(self):
        actual = {path.name for path in SKILLS_ROOT.iterdir() if path.is_dir()}
        self.assertEqual(actual, EXPECTED)

    def test_skill_frontmatter_and_metadata(self):
        for skill_name in sorted(EXPECTED):
            with self.subTest(skill=skill_name):
                folder = SKILLS_ROOT / skill_name
                content = (folder / "SKILL.md").read_text(encoding="utf-8")
                metadata = parse_simple_frontmatter(content)
                self.assertEqual(metadata.get("name"), skill_name)
                description = metadata.get("description", "")
                self.assertTrue(description)
                self.assertLessEqual(len(description), 1024)
                self.assertNotIn("<", description)
                self.assertNotIn(">", description)
                self.assertRegex(skill_name, r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
                self.assertNotRegex(content, r"(?m)^\s*\[TODO:[^\n]*\]\s*$")

                ui_path = folder / "agents" / "openai.yaml"
                self.assertTrue(ui_path.is_file())
                ui = ui_path.read_text(encoding="utf-8")
                self.assertIn("interface:", ui)
                self.assertIn("display_name:", ui)
                self.assertIn("short_description:", ui)
                self.assertIn(f"${skill_name}", ui)


if __name__ == "__main__":
    unittest.main()
