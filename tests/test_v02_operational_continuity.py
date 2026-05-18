import os
import subprocess
import sys
import pytest

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEMORY_INDEX_DIR = os.path.join(BASE_DIR, "memory", "index")
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")
SCRIPTS_DIR = os.path.join(BASE_DIR, "scripts")


def test_memory_index_directory_exists():
    assert os.path.isdir(MEMORY_INDEX_DIR), "memory/index/ directory is missing"


def test_memory_index_readme_exists():
    filepath = os.path.join(MEMORY_INDEX_DIR, "README.md")
    assert os.path.isfile(filepath), "memory/index/README.md is missing"


def test_traceability_index_template_exists():
    filepath = os.path.join(MEMORY_INDEX_DIR, "traceability_index_template.md")
    assert os.path.isfile(filepath), "memory/index/traceability_index_template.md is missing"


def test_operational_report_template_exists():
    filepath = os.path.join(TEMPLATES_DIR, "operational_report_template.md")
    assert os.path.isfile(filepath), "templates/operational_report_template.md is missing"


def test_aeos_lint_script_exists():
    filepath = os.path.join(SCRIPTS_DIR, "aeos_lint.py")
    assert os.path.isfile(filepath), "scripts/aeos_lint.py is missing"


def test_governance_continuity_doc_exists():
    filepath = os.path.join(BASE_DIR, "docs", "GOVERNANCE_CONTINUITY.md")
    assert os.path.isfile(filepath), "docs/GOVERNANCE_CONTINUITY.md is missing"


def test_aeos_lint_executes_successfully():
    lint_script = os.path.join(SCRIPTS_DIR, "aeos_lint.py")
    result = subprocess.run(
        [sys.executable, lint_script],
        capture_output=True,
        text=True,
        cwd=BASE_DIR,
    )
    assert result.returncode == 0, f"aeos_lint.py failed:\n{result.stdout}\n{result.stderr}"


def test_traceability_index_template_contains_required_sections():
    filepath = os.path.join(MEMORY_INDEX_DIR, "traceability_index_template.md")
    with open(filepath, "r") as f:
        content = f.read()
    required_sections = [
        "OBJ",
        "ADR",
        "TASK",
        "REV",
        "AUD",
        "HND",
        "INC",
        "Traceability Gaps",
        "Validation Results",
    ]
    for section in required_sections:
        assert section in content, f"traceability_index_template.md missing section: {section}"


def test_operational_report_template_contains_required_sections():
    filepath = os.path.join(TEMPLATES_DIR, "operational_report_template.md")
    with open(filepath, "r") as f:
        content = f.read()
    required_sections = [
        "Reporting Period",
        "Objectives Completed",
        "Tasks Completed",
        "ADRs Created",
        "Audits Completed",
        "Governance Violations",
        "Incidents",
        "Risks",
        "Workflow Failures",
        "Context Continuity Issues",
        "Recommended Actions",
        "Open Escalations",
    ]
    for section in required_sections:
        assert section in content, f"operational_report_template.md missing section: {section}"


def test_workflow_closure_checks_execute():
    lint_script = os.path.join(SCRIPTS_DIR, "aeos_lint.py")
    result = subprocess.run(
        [sys.executable, lint_script],
        capture_output=True,
        text=True,
        cwd=BASE_DIR,
    )
    assert "Workflow Closure" in result.stdout, "aeos_lint.py missing workflow closure check"
    assert "Traceability References" in result.stdout, "aeos_lint.py missing traceability check"
