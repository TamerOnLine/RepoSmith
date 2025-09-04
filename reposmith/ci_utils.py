# reposmith/ci_utils.py
from __future__ import annotations

import textwrap
from pathlib import Path

from .core.fs import write_file

def ensure_github_actions_workflow(
    root_dir: Path,
    path: str = ".github/workflows/test-main.yml",
    *,
    py: str = "3.12",
    program: str = "app.py",  # Retained for backward compatibility – no longer used
    force: bool = False,
) -> str:
    """
    Generate a GitHub Actions workflow that runs unit tests (unittest).

    Args:
        root_dir (Path): The root directory where the workflow file will be created.
        path (str, optional): Relative path to the GitHub Actions workflow YAML file.
            Defaults to ".github/workflows/test-main.yml".
        py (str, optional): Python version to be used in the workflow. Defaults to "3.12".
        program (str, optional): Unused. Retained for backward compatibility. Defaults to "app.py".
        force (bool, optional): If True, overwrite the workflow file if it exists.

    Returns:
        str: The path of the written workflow file as a string.
    """
    wf_path = Path(root_dir) / path
    wf_path.parent.mkdir(parents=True, exist_ok=True)

    yml = textwrap.dedent(f"""
    name: Run tests
    on: [push, pull_request]
    jobs:
      test:
        runs-on: ubuntu-latest
        steps:
          - name: Checkout repository
            uses: actions/checkout@v4

          - name: Set up Python
            uses: actions/setup-python@v5
            with:
              python-version: "{py}"

          - name: Install dependencies (if any)
            run: |
              if [ -f requirements.txt ]; then python -m pip install -r requirements.txt; fi

          - name: Run unit tests
            run: |
              if [ -d tests ]; then
                python -m unittest discover -s tests -v
              else
                echo "No tests directory found. Skipping."
              fi
    """).lstrip()

    return write_file(wf_path, yml, force=force, backup=True)
