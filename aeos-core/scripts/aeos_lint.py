#!/usr/bin/env python3
"""Compatibility entrypoint for AEOS lint under aeos-core/ path."""

from __future__ import annotations

from pathlib import Path
import re
import subprocess
import sys


REQUIRED_V03_FILES = [
    "governance/GOVERNANCE_SEVERITY_MODEL.md",
    "templates/escalation_template.md",
    "docs/REVIEW_CADENCE.md",
    "templates/governance_health_report_template.md",
    "docs/OPERATIONAL_EXAMPLES.md",
]

REQUIRED_SEVERITY_LABELS = ["LOW", "MEDIUM", "HIGH", "CRITICAL"]
REQUIRED_EXPERIMENTAL_FILES = [
    "docs/EXPERIMENTAL_LAB_CHARTER.md",
    "governance/PORTING_POLICY.md",
    "templates/experiment_template.md",
    "templates/porting_review_template.md",
]


def _resolve_artifact_path(repo_root: Path, core_root: Path, rel: str) -> Path | None:
    core_path = core_root / rel
    if core_path.is_file():
        return core_path

    root_path = repo_root / rel
    if root_path.is_file():
        return root_path

    return None


def _check_v03_requirements(repo_root: Path, core_root: Path) -> list[str]:
    errors: list[str] = []

    for rel in REQUIRED_V03_FILES:
        if _resolve_artifact_path(repo_root, core_root, rel) is None:
            errors.append(f"Missing v0.3 required file: aeos-core/{rel}")

    severity_path = _resolve_artifact_path(repo_root, core_root, "governance/GOVERNANCE_SEVERITY_MODEL.md")
    if severity_path is not None:
        text = severity_path.read_text(encoding="utf-8")
        for label in REQUIRED_SEVERITY_LABELS:
            if re.search(rf"\b{label}\b", text) is None:
                errors.append(f"Missing severity label in GOVERNANCE_SEVERITY_MODEL.md: {label}")

    escalation_path = _resolve_artifact_path(repo_root, core_root, "templates/escalation_template.md")
    if escalation_path is not None:
        text = escalation_path.read_text(encoding="utf-8")
        if "ESC-001" not in text and "ESC-XXX" not in text:
            errors.append("Missing ESC-001 or ESC-XXX in escalation_template.md")

    return errors


def _check_experimental_lab_requirements(repo_root: Path, core_root: Path) -> list[str]:
    errors: list[str] = []
    for rel in REQUIRED_EXPERIMENTAL_FILES:
        if _resolve_artifact_path(repo_root, core_root, rel) is None:
            errors.append(f"Missing experimental lab required file: aeos-core/{rel}")
    return errors


def main() -> int:
    repo_root = Path(__file__).resolve().parents[2]
    core_root = repo_root / "aeos-core"
    root_lint = repo_root / "scripts" / "aeos_lint.py"

    if not root_lint.is_file():
        print(f"AEOS LINT FAILED\n- Missing delegated lint script: {root_lint}")
        return 1

    result = subprocess.run([sys.executable, str(root_lint)], cwd=repo_root, check=False)
    if result.returncode != 0:
        return result.returncode

    errors = _check_v03_requirements(repo_root, core_root)
    errors.extend(_check_experimental_lab_requirements(repo_root, core_root))
    if errors:
        print("AEOS LINT FAILED")
        for err in errors:
            print(f"- {err}")
        return 1

    print("AEOS LINT PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
