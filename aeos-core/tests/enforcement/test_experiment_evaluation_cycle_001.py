from pathlib import Path

AEOS_CORE_ROOT = Path(__file__).resolve().parents[2]


def test_evaluation_cycle_artifacts_exist() -> None:
    assert (AEOS_CORE_ROOT / "memory/objectives/OBJ-EXP-001.md").is_file()
    assert (AEOS_CORE_ROOT / "memory/tasks/TASK-EXP-001.md").is_file()
    assert (AEOS_CORE_ROOT / "memory/reviews/REV-EXP-001.md").is_file()
    assert (AEOS_CORE_ROOT / "memory/audits/AUD-EXP-001.md").is_file()
    assert (AEOS_CORE_ROOT / "memory/handoffs/HND-EXP-001.md").is_file()


def test_operating_notes_and_portability_assessment_exist() -> None:
    assert (AEOS_CORE_ROOT / "docs/EXPERIMENTAL_LAB_OPERATING_NOTES.md").is_file()
    assert (AEOS_CORE_ROOT / "memory/experiments/PORTABILITY_RISK_ASSESSMENT_001.md").is_file()


def test_porting_remains_deferred() -> None:
    port_review = (AEOS_CORE_ROOT / "memory/experiments/PORT-001.md").read_text(encoding="utf-8")
    assert "DEFER" in port_review
    assert "Porting remains deferred" in port_review
