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
        self.assertEqual(set(servers), {"notion", "x", "github", "linkedin_fresh"})
        self.assertEqual(servers["x"]["command"], "npx")
        self.assertEqual(servers["x"]["startup_timeout_sec"], 300)
        self.assertEqual(servers["linkedin_fresh"]["command"], "zsh")
        self.assertEqual(servers["linkedin_fresh"]["startup_timeout_sec"], 300)
        for name in ("notion", "x", "github"):
            server = servers[name]
            allowed = " ".join(server["enabled_tools"]).lower()
            self.assertFalse(any(word in allowed for word in ("send", "publish", "delete", "create_article", "bookmark")))

    def test_required_skills_and_schemas_exist(self) -> None:
        for name in ("find-leads", "deep-search", "x-reply-angles", "polish-x-drafts", "artifact-outreach"):
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

    def test_scholar_tool_has_help(self) -> None:
        result = subprocess.run([sys.executable, str(ROOT / "tools" / "scholar.py"), "--help"], capture_output=True, text=True, check=False)
        self.assertEqual(result.returncode, 0)
        self.assertTrue("never" in result.stdout.lower() or "read" in result.stdout.lower())
