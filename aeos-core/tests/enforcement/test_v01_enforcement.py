from pathlib import Path
import subprocess
import sys

AEOS_CORE_ROOT = Path(__file__).resolve().parents[2]
REPO_ROOT = Path(__file__).resolve().parents[3]


def test_aeos_lint_script_exists() -> None:
    assert (AEOS_CORE_ROOT / "scripts/aeos_lint.py").is_file()


def test_aeos_lint_exits_successfully() -> None:
    result = subprocess.run(
        [sys.executable, str(AEOS_CORE_ROOT / "scripts/aeos_lint.py")],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    combined = f"{result.stdout}\n{result.stderr}"
    assert result.returncode == 0, combined
    assert "AEOS LINT PASSED" in combined, combined


def test_ci_workflow_exists() -> None:
    assert (REPO_ROOT / ".github/workflows/aeos-validation.yml").is_file()
