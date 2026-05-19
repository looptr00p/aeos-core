from pathlib import Path

AEOS_CORE_ROOT = Path(__file__).resolve().parents[2]


def test_governance_audit_cycle_artifacts_exist() -> None:
    assert (AEOS_CORE_ROOT / "memory/objectives/OBJ-AUD-001.md").is_file()
    assert (AEOS_CORE_ROOT / "memory/tasks/TASK-AUD-001.md").is_file()
    assert (AEOS_CORE_ROOT / "memory/audits/AUD-EXP-002.md").is_file()
    assert (AEOS_CORE_ROOT / "memory/experiments/PORTING_CANDIDATE_REVIEW_001.md").is_file()
    assert (AEOS_CORE_ROOT / "memory/audits/FORMAT_READABILITY_AUDIT_001.md").is_file()
    assert (AEOS_CORE_ROOT / "memory/handoffs/HND-AUD-001.md").is_file()


def test_port_001_stays_deferred() -> None:
    port_review = (AEOS_CORE_ROOT / "memory/experiments/PORT-001.md").read_text(encoding="utf-8")
    assert "DEFER" in port_review
    assert "Porting remains deferred" in port_review
