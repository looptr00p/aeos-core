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


def test_inc_001_exists():
    content = read_memory_file("incidents", "INC-001.md")
    assert "INC-001" in content


def test_esc_002_exists():
    content = read_memory_file("incidents", "ESC-002.md")
    assert "ESC-002" in content


def test_active_incidents_have_valid_references():
    incidents_dir = os.path.join(MEMORY_DIR, "incidents")
    for fname in os.listdir(incidents_dir):
        if not fname.endswith(".md") or fname.startswith("ESC-"):
            continue
        content = read_memory_file("incidents", fname)
        status_match = re.search(r"## Status\s*\n\s*(\w+)", content)
        if status_match and status_match.group(1) == "ACTIVE":
            obj_refs = re.findall(r"OBJ-\d{3,}", content)
            task_refs = re.findall(r"TASK-\d{3,}", content)
            assert obj_refs or task_refs, f"ACTIVE incident {fname} has no objective or task references"


def test_open_escalations_have_valid_references():
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


def test_in_progress_tasks_reference_objectives():
    tasks_dir = os.path.join(MEMORY_DIR, "tasks")
    for fname in os.listdir(tasks_dir):
        if not fname.endswith(".md"):
            continue
        content = read_memory_file("tasks", fname)
        status_match = re.search(r"## Status\s*\n\s*(\w+(?:_\w+)?)", content)
        if status_match and status_match.group(1) == "IN_PROGRESS":
            obj_refs = re.findall(r"OBJ-\d{3,}", content)
            assert obj_refs, f"IN_PROGRESS task {fname} has no objective reference"
