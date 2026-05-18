import os
import pytest

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
WORKFLOWS_DIR = os.path.join(BASE_DIR, "workflows")

REQUIRED_WORKFLOW_FILES = [
    "feature_workflow.md",
    "bugfix_workflow.md",
    "architecture_change_workflow.md",
    "audit_workflow.md",
    "incident_workflow.md",
    "research_workflow.md",
]


@pytest.mark.parametrize("filename", REQUIRED_WORKFLOW_FILES)
def test_workflow_file_exists(filename):
    filepath = os.path.join(WORKFLOWS_DIR, filename)
    assert os.path.isfile(filepath), f"Missing workflow file: {filename}"


def test_no_extra_workflow_files():
    existing = {f for f in os.listdir(WORKFLOWS_DIR) if os.path.isfile(os.path.join(WORKFLOWS_DIR, f))}
    expected = set(REQUIRED_WORKFLOW_FILES)
    extra = existing - expected
    assert not extra, f"Unexpected workflow files: {extra}"
