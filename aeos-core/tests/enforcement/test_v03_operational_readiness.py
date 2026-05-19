from pathlib import Path
import subprocess
import sys

AEOS_CORE_ROOT = Path(__file__).resolve().parents[2]
REPO_ROOT = Path(__file__).resolve().parents[3]


def test_v03_required_files_exist() -> None:
    required = [
        "governance/GOVERNANCE_SEVERITY_MODEL.md",
        "templates/escalation_template.md",
        "docs/REVIEW_CADENCE.md",
        "templates/governance_health_report_template.md",
        "docs/OPERATIONAL_EXAMPLES.md",
    ]
    for rel in required:
        assert (AEOS_CORE_ROOT / rel).is_file(), f"Missing required v0.3 file: {rel}"


def test_severity_labels_exist() -> None:
    text = (AEOS_CORE_ROOT / "governance/GOVERNANCE_SEVERITY_MODEL.md").read_text(
        encoding="utf-8"
    )
    for label in ["LOW", "MEDIUM", "HIGH", "CRITICAL"]:
        assert label in text, f"Missing severity label: {label}"


def test_escalation_template_contains_esc_id() -> None:
    text = (AEOS_CORE_ROOT / "templates/escalation_template.md").read_text(encoding="utf-8")
    assert "ESC-001" in text


def test_aeos_lint_passes_with_v03_requirements() -> None:
    result = subprocess.run(
        [sys.executable, str(AEOS_CORE_ROOT / "scripts/aeos_lint.py")],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    combined = f"{result.stdout}\n{result.stderr}"
    assert result.returncode == 0, combined
    assert "AEOS LINT PASSED" in combined, combined
