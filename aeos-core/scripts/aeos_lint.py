#!/usr/bin/env python3
"""Compatibility entrypoint for AEOS lint under aeos-core/ path."""

from __future__ import annotations

from pathlib import Path
import subprocess
import sys


def main() -> int:
    repo_root = Path(__file__).resolve().parents[2]
    root_lint = repo_root / "scripts" / "aeos_lint.py"

    if not root_lint.is_file():
        print(f"AEOS LINT FAILED\n- Missing delegated lint script: {root_lint}")
        return 1

    result = subprocess.run([sys.executable, str(root_lint)], cwd=repo_root, check=False)
    if result.returncode == 0:
        print("AEOS LINT PASSED")
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
