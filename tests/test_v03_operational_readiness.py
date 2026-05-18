import os
import subprocess
import sys
import pytest

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GOVERNANCE_DIR = os.path.join(BASE_DIR, "governance")
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")
DOCS_DIR = os.path.join(BASE_DIR, "docs")
SCRIPTS_DIR = os.path.join(BASE_DIR, "scripts")


def test_governance_severity_model_exists():
    filepath = os.path.join(GOVERNANCE_DIR, "GOVERNANCE_SEVERITY_MODEL.md")
    assert os.path.isfile(filepath), "governance/GOVERNANCE_SEVERITY_MODEL.md is missing"


def test_escalation_template_exists():
    filepath = os.path.join(TEMPLATES_DIR, "escalation_template.md")
    assert os.path.isfile(filepath), "templates/escalation_template.md is missing"


def test_review_cadence_exists():
    filepath = os.path.join(DOCS_DIR, "REVIEW_CADENCE.md")
    assert os.path.isfile(filepath), "docs/REVIEW_CADENCE.md is missing"


def test_governance_health_report_template_exists():
    filepath = os.path.join(TEMPLATES_DIR, "governance_health_report_template.md")
    assert os.path.isfile(filepath), "templates/governance_health_report_template.md is missing"


def test_operational_examples_exists():
    filepath = os.path.join(DOCS_DIR, "OPERATIONAL_EXAMPLES.md")
    assert os.path.isfile(filepath), "docs/OPERATIONAL_EXAMPLES.md is missing"


def test_severity_model_contains_all_levels():
    filepath = os.path.join(GOVERNANCE_DIR, "GOVERNANCE_SEVERITY_MODEL.md")
    with open(filepath, "r") as f:
        content = f.read()
    for level in ["LOW", "MEDIUM", "HIGH", "CRITICAL"]:
        assert f"### {level}" in content, f"GOVERNANCE_SEVERITY_MODEL.md missing severity level: {level}"


def test_severity_model_contains_required_fields():
    filepath = os.path.join(GOVERNANCE_DIR, "GOVERNANCE_SEVERITY_MODEL.md")
    with open(filepath, "r") as f:
        content = f.read()
    required_fields = [
        "description",
        "examples",
        "required review",
        "required audit",
        "human approval",
        "escalation",
        "rollback",
    ]
    for field in required_fields:
        assert field.lower() in content.lower(), f"GOVERNANCE_SEVERITY_MODEL.md missing field: {field}"


def test_escalation_template_contains_required_fields():
    filepath = os.path.join(TEMPLATES_DIR, "escalation_template.md")
    with open(filepath, "r") as f:
        content = f.read()
    required_fields = [
        "ESC-",
        "severity",
        "triggering condition",
        "affected systems",
        "operational impact",
        "governance impact",
        "required reviewers",
        "required approvals",
        "rollback requirements",
        "resolution status",
        "follow-up actions",
    ]
    for field in required_fields:
        assert field.lower() in content.lower(), f"escalation_template.md missing field: {field}"


def test_governance_health_report_template_contains_required_fields():
    filepath = os.path.join(TEMPLATES_DIR, "governance_health_report_template.md")
    with open(filepath, "r") as f:
        content = f.read()
    required_fields = [
        "reporting period",
        "governance violations",
        "unresolved escalations",
        "workflow failures",
        "audit completion rate",
        "review latency",
        "handoff quality",
        "recurring incidents",
        "operational bottlenecks",
        "governance drift",
        "corrective actions",
    ]
    for field in required_fields:
        assert field.lower() in content.lower(), f"governance_health_report_template.md missing field: {field}"


def test_review_cadence_contains_all_cycles():
    filepath = os.path.join(DOCS_DIR, "REVIEW_CADENCE.md")
    with open(filepath, "r") as f:
        content = f.read()
    for cycle in ["Daily", "Weekly", "Monthly", "Quarterly"]:
        assert cycle in content, f"REVIEW_CADENCE.md missing review cycle: {cycle}"


def test_operational_examples_contains_all_lifecycles():
    filepath = os.path.join(DOCS_DIR, "OPERATIONAL_EXAMPLES.md")
    with open(filepath, "r") as f:
        content = f.read()
    required_lifecycles = [
        "Objective Lifecycle",
        "ADR Lifecycle",
        "Task Lifecycle",
        "Review Lifecycle",
        "Audit Lifecycle",
        "Incident Lifecycle",
        "Escalation Lifecycle",
        "Handoff Lifecycle",
    ]
    for lifecycle in required_lifecycles:
        assert lifecycle in content, f"OPERATIONAL_EXAMPLES.md missing lifecycle: {lifecycle}"


def test_aeos_lint_validates_severity_labels():
    lint_script = os.path.join(SCRIPTS_DIR, "aeos_lint.py")
    result = subprocess.run(
        [sys.executable, lint_script],
        capture_output=True,
        text=True,
        cwd=BASE_DIR,
    )
    assert result.returncode == 0, f"aeos_lint.py failed:\n{result.stdout}\n{result.stderr}"
    assert "Severity Labels" in result.stdout, "aeos_lint.py missing severity label check"
    assert "v0.3 Documents" in result.stdout, "aeos_lint.py missing v0.3 document check"
