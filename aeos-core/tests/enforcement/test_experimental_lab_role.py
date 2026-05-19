from pathlib import Path

AEOS_CORE_ROOT = Path(__file__).resolve().parents[2]


def test_experimental_lab_charter_exists() -> None:
    assert (AEOS_CORE_ROOT / "docs/EXPERIMENTAL_LAB_CHARTER.md").is_file()


def test_porting_policy_exists() -> None:
    assert (AEOS_CORE_ROOT / "governance/PORTING_POLICY.md").is_file()


def test_experiment_templates_exist() -> None:
    assert (AEOS_CORE_ROOT / "templates/experiment_template.md").is_file()
    assert (AEOS_CORE_ROOT / "templates/porting_review_template.md").is_file()


def test_experiment_memory_records_exist() -> None:
    assert (AEOS_CORE_ROOT / "memory/experiments/EXP-001.md").is_file()
    assert (AEOS_CORE_ROOT / "memory/experiments/PORT-001.md").is_file()
