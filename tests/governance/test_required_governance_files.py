import os
import pytest

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
GOVERNANCE_DIR = os.path.join(BASE_DIR, "governance")

REQUIRED_GOVERNANCE_FILES = [
    "AGENTS.md",
    "PHASE_POLICY.md",
    "PERMISSION_MODEL.md",
    "REVIEW_REQUIREMENTS.md",
    "ESCALATION_POLICY.md",
    "SAFETY_RULES.md",
    "GOVERNANCE_SEVERITY_MODEL.md",
    "STATE_CLASSIFICATION_POLICY.md",
]


@pytest.mark.parametrize("filename", REQUIRED_GOVERNANCE_FILES)
def test_governance_file_exists(filename):
    filepath = os.path.join(GOVERNANCE_DIR, filename)
    assert os.path.isfile(filepath), f"Missing governance file: {filename}"


def test_no_extra_governance_files():
    existing = {f for f in os.listdir(GOVERNANCE_DIR) if os.path.isfile(os.path.join(GOVERNANCE_DIR, f))}
    expected = set(REQUIRED_GOVERNANCE_FILES)
    extra = existing - expected
    assert not extra, f"Unexpected governance files: {extra}"
