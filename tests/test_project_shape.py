from __future__ import annotations

import subprocess
import sys
import tomllib
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class ProjectShapeTests(unittest.TestCase):
    def test_mcp_config_is_parseable_and_read_constrained(self) -> None:
        config = tomllib.loads((ROOT / ".codex" / "config.toml").read_text())
        servers = config["mcp_servers"]
        self.assertEqual(set(servers), {"notion", "github"})
        for server in servers.values():
            allowed = " ".join(server["enabled_tools"]).lower()
            self.assertFalse(any(word in allowed for word in ("send", "publish", "delete", "create_article", "bookmark")))

    def test_required_skills_and_schemas_exist(self) -> None:
        for name in ("find-leads", "deep-search", "artifact-outreach"):
            content = (ROOT / ".codex" / "skills" / name / "SKILL.md").read_text()
            self.assertTrue(content.startswith("---\n"))
            self.assertIn("\n---\n", content)
            self.assertIn(f"name: {name}", content)
            self.assertIn("Notion", content)
        schema = (ROOT / "schemas" / "notion.md").read_text()
        self.assertIn("`New`, `Reviewed`, or `Rejected`", schema)

    def test_legacy_execution_package_is_absent(self) -> None:
        self.assertFalse((ROOT / "gtm_agent").exists())
        obsolete = {"publish-x-queue", "publish-x-replies", "publish-paper-outreach", "paper-outreach", "discover-and-draft-x-replies"}
        self.assertFalse((ROOT / ".claude").exists())
        self.assertFalse((ROOT / ".agents").exists())
        self.assertFalse(obsolete.intersection(path.name for path in (ROOT / ".codex" / "skills").iterdir()))

    def test_fallback_tools_are_read_only_and_have_help(self) -> None:
        for name in ("scholar.py",):
            source = (ROOT / "tools" / name).read_text()
            self.assertNotIn("requests.post", source)
            self.assertNotIn("requests.put", source)
            self.assertNotIn("requests.patch", source)
            result = subprocess.run([sys.executable, str(ROOT / "tools" / name), "--help"], capture_output=True, text=True, check=False)
            self.assertEqual(result.returncode, 0)
            self.assertTrue("never" in result.stdout.lower() or "read" in result.stdout.lower())
