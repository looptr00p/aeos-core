import os
import pytest

BASE_DIR = os.path.join(os.path.dirname(__file__), "..", "..")
PROTOCOLS_DIR = os.path.join(BASE_DIR, "protocols")

REQUIRED_PROTOCOL_FILES = [
    "TASK_PROTOCOL.md",
    "REVIEW_PROTOCOL.md",
    "CONTEXT_PROTOCOL.md",
    "MEMORY_PROTOCOL.md",
    "HANDOFF_PROTOCOL.md",
    "INCIDENT_PROTOCOL.md",
    "ADR_PROTOCOL.md",
]


@pytest.mark.parametrize("filename", REQUIRED_PROTOCOL_FILES)
def test_protocol_file_exists(filename):
    filepath = os.path.join(PROTOCOLS_DIR, filename)
    assert os.path.isfile(filepath), f"Missing protocol file: {filename}"


def test_no_extra_protocol_files():
    existing = {f for f in os.listdir(PROTOCOLS_DIR) if os.path.isfile(os.path.join(PROTOCOLS_DIR, f))}
    expected = set(REQUIRED_PROTOCOL_FILES)
    extra = existing - expected
    assert not extra, f"Unexpected protocol files: {extra}"
