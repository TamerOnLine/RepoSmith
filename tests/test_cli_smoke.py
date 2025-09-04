
import unittest
import tempfile
from pathlib import Path
import sys
import subprocess
import os
import json

class TestCLISmoke(unittest.TestCase):
    def setUp(self):
        self.ctx = tempfile.TemporaryDirectory()
        self.root = Path(self.ctx.name) / "proj"
        self.root.mkdir()

    def tearDown(self):
        self.ctx.cleanup()

    def _run(self, args):
        # Run the CLI via module to avoid PATH issues
        subprocess.run([sys.executable, "-m", "reposmith.main"] + args, check=True, cwd=self.root)

    def test_init_basic_without_venv(self):
        self._run(["init", "--no-venv", "--entry", "run.py", "--with-gitignore", "--with-license", "--with-vscode", "--author", "TestUser", "--year", "2099"])
        # files exist
        for rel in ["requirements.txt", "run.py", ".gitignore", "LICENSE", ".vscode/settings.json", ".vscode/launch.json", "project.code-workspace"]:
            self.assertTrue((self.root / rel).exists(), f"missing {rel}")

        # check license metadata
        lic = (self.root / "LICENSE").read_text(encoding="utf-8")
        self.assertIn("TestUser", lic)
        self.assertIn("2099", lic)

        # check vscode interpreter fallback without venv
        settings = json.loads((self.root / ".vscode" / "settings.json").read_text(encoding="utf-8"))
        expected = "python.exe" if os.name == "nt" else "python3"
        self.assertEqual(settings.get("python.defaultInterpreterPath"), expected)

if __name__ == "__main__":
    unittest.main(verbosity=2)
