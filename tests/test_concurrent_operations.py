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


def test_obj_005_exists():
    content = read_memory_file("objectives", "OBJ-005.md")
    assert "OBJ-005" in content


def test_task_007_exists():
    content = read_memory_file("tasks", "TASK-007.md")
    assert "TASK-007" in content


def test_task_008_exists():
    content = read_memory_file("tasks", "TASK-008.md")
    assert "TASK-008" in content


def test_task_009_exists():
    content = read_memory_file("tasks", "TASK-009.md")
    assert "TASK-009" in content


def test_inc_002_exists():
    content = read_memory_file("incidents", "INC-002.md")
    assert "INC-002" in content


def test_esc_003_exists():
    content = read_memory_file("incidents", "ESC-003.md")
    assert "ESC-003" in content


def test_concurrent_active_objectives_valid():
    # OBJ-004 and OBJ-005 closed after concurrent simulation. At least 1 ACTIVE objective (OBJ-003) must remain.
    objectives_dir = os.path.join(MEMORY_DIR, "objectives")
    active_count = 0
    for fname in os.listdir(objectives_dir):
        if not fname.endswith(".md"):
            continue
        content = read_memory_file("objectives", fname)
        status_match = re.search(r"## Status\s*\n\s*(\w+)", content)
        if status_match and status_match.group(1) == "ACTIVE":
            active_count += 1
            obj_refs = re.findall(r"OBJ-\d{3,}", content)
            assert obj_refs, f"ACTIVE objective {fname} has no traceability ID"
    assert active_count >= 1, "Expected at least 1 ACTIVE objective"


def test_open_escalation_accumulation_valid():
    # Concurrent simulation closed. OBJ-004 and OBJ-005 are CLOSED; ESC-003 is RESOLVED.
    # All OPEN escalations (if any) must reference an objective or task.
    incidents_dir = os.path.join(MEMORY_DIR, "incidents")
    for fname in os.listdir(incidents_dir):
        if not fname.endswith(".md") or not fname.startswith("ESC-"):
            continue
        content = read_memory_file("incidents", fname)
        status_match = re.search(r"## Status\s*\n\s*(\w+)", content)
        if status_match and status_match.group(1) == "OPEN":
            obj_refs = re.findall(r"OBJ-\d{3,}", content)
            task_refs = re.findall(r"TASK-\d{3,}", content)
            assert obj_refs or task_refs, f"OPEN escalation {fname} has no objective or task references"
