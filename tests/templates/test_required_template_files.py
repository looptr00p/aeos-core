import os
import pytest

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")

REQUIRED_TEMPLATE_FILES = [
    "objective_template.md",
    "adr_template.md",
    "task_template.md",
    "review_template.md",
    "audit_template.md",
    "handoff_template.md",
    "incident_template.md",
    "operational_report_template.md",
    "escalation_template.md",
    "governance_health_report_template.md",
]


@pytest.mark.parametrize("filename", REQUIRED_TEMPLATE_FILES)
def test_template_file_exists(filename):
    filepath = os.path.join(TEMPLATES_DIR, filename)
    assert os.path.isfile(filepath), f"Missing template file: {filename}"


def test_no_extra_template_files():
    existing = {f for f in os.listdir(TEMPLATES_DIR) if os.path.isfile(os.path.join(TEMPLATES_DIR, f))}
    expected = set(REQUIRED_TEMPLATE_FILES)
    extra = existing - expected
    assert not extra, f"Unexpected template files: {extra}"
