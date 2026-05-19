import os
import re
import pytest

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEMORY_DIR = os.path.join(BASE_DIR, "memory")


def read_memory_file(subdir, filename):
    filepath = os.path.join(MEMORY_DIR, subdir, filename)
    assert os.path.isfile(filepath), f"Missing file: {filepath}"
    with open(filepath, "r") as f:
        return f.read()


def test_inc_003_exists():
    content = read_memory_file("incidents", "INC-003.md")
    assert "INC-003" in content


def test_task_010_exists():
    content = read_memory_file("tasks", "TASK-010.md")
    assert "TASK-010" in content


def test_task_011_exists():
    content = read_memory_file("tasks", "TASK-011.md")
    assert "TASK-011" in content


def test_rev_008_exists():
    content = read_memory_file("reviews", "REV-008.md")
    assert "REV-008" in content


def test_rev_009_exists():
    content = read_memory_file("reviews", "REV-009.md")
    assert "REV-009" in content


def test_hnd_006_exists():
    content = read_memory_file("handoffs", "HND-006.md")
    assert "HND-006" in content


def test_opr_005_exists():
    content = read_memory_file("research", "OPR-005.md")
    assert "OPR-005" in content


def test_ghr_005_exists():
    content = read_memory_file("research", "GHR-005.md")
    assert "GHR-005" in content


def test_esc_002_status_in_review():
    content = read_memory_file("incidents", "ESC-002.md")
    status_match = re.search(r"## Status\s*\n\s*(\w+(?:_\w+)?)", content)
    assert status_match, "ESC-002 missing status field"
    assert status_match.group(1) == "IN_REVIEW", f"ESC-002 status expected IN_REVIEW, got {status_match.group(1)}"


def test_esc_003_status_open():
    content = read_memory_file("incidents", "ESC-003.md")
    status_match = re.search(r"## Status\s*\n\s*(\w+)", content)
    assert status_match, "ESC-003 missing status field"
    assert status_match.group(1) == "OPEN", f"ESC-003 status expected OPEN, got {status_match.group(1)}"
