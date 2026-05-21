import os
import re
import pytest

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEMORY_DIR = os.path.join(BASE_DIR, "memory")
DOCS_DIR = os.path.join(BASE_DIR, "docs")


def read_memory_file(subdir, filename):
    filepath = os.path.join(MEMORY_DIR, subdir, filename)
    assert os.path.isfile(filepath), f"Missing file: {filepath}"
    with open(filepath, "r") as f:
        return f.read()


def test_task_004_closed():
    content = read_memory_file("tasks", "TASK-004.md")
    status_match = re.search(r"## Status\s*\n\s*(\w+)", content)
    assert status_match and status_match.group(1) == "CLOSED", f"TASK-004 expected CLOSED, got {status_match.group(1) if status_match else 'NOT FOUND'}"


def test_task_005_closed():
    content = read_memory_file("tasks", "TASK-005.md")
    status_match = re.search(r"## Status\s*\n\s*(\w+)", content)
    assert status_match and status_match.group(1) == "CLOSED", f"TASK-005 expected CLOSED, got {status_match.group(1) if status_match else 'NOT FOUND'}"


def test_task_007_closed():
    content = read_memory_file("tasks", "TASK-007.md")
    status_match = re.search(r"## Status\s*\n\s*(\w+)", content)
    assert status_match and status_match.group(1) == "CLOSED", f"TASK-007 expected CLOSED, got {status_match.group(1) if status_match else 'NOT FOUND'}"


def test_task_006_in_progress():
    content = read_memory_file("tasks", "TASK-006.md")
    status_match = re.search(r"## Status\s*\n\s*(\w+(?:_\w+)?)", content)
    assert status_match and status_match.group(1) == "IN_PROGRESS", f"TASK-006 expected IN_PROGRESS, got {status_match.group(1) if status_match else 'NOT FOUND'}"


def test_task_008_in_progress():
    content = read_memory_file("tasks", "TASK-008.md")
    status_match = re.search(r"## Status\s*\n\s*(\w+(?:_\w+)?)", content)
    assert status_match and status_match.group(1) == "IN_PROGRESS", f"TASK-008 expected IN_PROGRESS, got {status_match.group(1) if status_match else 'NOT FOUND'}"


def test_task_009_in_progress():
    content = read_memory_file("tasks", "TASK-009.md")
    status_match = re.search(r"## Status\s*\n\s*(\w+(?:_\w+)?)", content)
    assert status_match and status_match.group(1) == "IN_PROGRESS", f"TASK-009 expected IN_PROGRESS, got {status_match.group(1) if status_match else 'NOT FOUND'}"


def test_task_010_in_progress():
    content = read_memory_file("tasks", "TASK-010.md")
    status_match = re.search(r"## Status\s*\n\s*(\w+(?:_\w+)?)", content)
    assert status_match and status_match.group(1) == "IN_PROGRESS", f"TASK-010 expected IN_PROGRESS, got {status_match.group(1) if status_match else 'NOT FOUND'}"


def test_task_011_in_progress():
    content = read_memory_file("tasks", "TASK-011.md")
    status_match = re.search(r"## Status\s*\n\s*(\w+(?:_\w+)?)", content)
    assert status_match and status_match.group(1) == "IN_PROGRESS", f"TASK-011 expected IN_PROGRESS, got {status_match.group(1) if status_match else 'NOT FOUND'}"


def test_inc_001_resolved():
    content = read_memory_file("incidents", "INC-001.md")
    status_match = re.search(r"## Status\s*\n\s*(\w+)", content)
    assert status_match and status_match.group(1) == "RESOLVED", f"INC-001 expected RESOLVED, got {status_match.group(1) if status_match else 'NOT FOUND'}"


def test_inc_002_active():
    content = read_memory_file("incidents", "INC-002.md")
    status_match = re.search(r"## Status\s*\n\s*(\w+)", content)
    assert status_match and status_match.group(1) == "ACTIVE", f"INC-002 expected ACTIVE, got {status_match.group(1) if status_match else 'NOT FOUND'}"


def test_inc_003_active():
    content = read_memory_file("incidents", "INC-003.md")
    status_match = re.search(r"## Status\s*\n\s*(\w+)", content)
    assert status_match and status_match.group(1) == "ACTIVE", f"INC-003 expected ACTIVE, got {status_match.group(1) if status_match else 'NOT FOUND'}"


def test_esc_002_in_review():
    content = read_memory_file("incidents", "ESC-002.md")
    status_match = re.search(r"## Status\s*\n\s*(\w+(?:_\w+)?)", content)
    assert status_match and status_match.group(1) == "IN_REVIEW", f"ESC-002 expected IN_REVIEW, got {status_match.group(1) if status_match else 'NOT FOUND'}"


def test_esc_003_resolved():
    content = read_memory_file("incidents", "ESC-003.md")
    status_match = re.search(r"## Status\s*\n\s*(\w+)", content)
    assert status_match and status_match.group(1) == "RESOLVED", f"ESC-003 expected RESOLVED, got {status_match.group(1) if status_match else 'NOT FOUND'}"


def test_hnd_007_exists():
    content = read_memory_file("handoffs", "HND-007.md")
    assert "HND-007" in content


def test_opr_006_exists():
    content = read_memory_file("research", "OPR-006.md")
    assert "OPR-006" in content


def test_ghr_006_exists():
    content = read_memory_file("research", "GHR-006.md")
    assert "GHR-006" in content


def test_governance_debt_recovery_learnings_exists():
    filepath = os.path.join(DOCS_DIR, "GOVERNANCE_DEBT_RECOVERY_LEARNINGS.md")
    assert os.path.isfile(filepath), f"Missing file: GOVERNANCE_DEBT_RECOVERY_LEARNINGS.md"
