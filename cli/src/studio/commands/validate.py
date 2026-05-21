"""studio validate — Run aeos_lint.py and pytest."""

import subprocess
import sys
from pathlib import Path
from rich.console import Console
from rich.panel import Panel
import typer

validate_app = typer.Typer()
console = Console()


@validate_app.command()
def run(
    project_path: str = typer.Argument(".", help="Path to the project directory"),
    tests: bool = typer.Option(True, "--tests/--no-tests", help="Run pytest if tests/ exists"),
):
    """Run governance lint and optionally pytest validation."""

    target = Path(project_path).resolve()
    lint_script = target / "scripts" / "aeos_lint.py"
    tests_dir = target / "tests"

    if not lint_script.exists():
        console.print(f"[bold red]Error:[/bold red] aeos_lint.py not found at {lint_script}")
        console.print("Run [cyan]studio init[/cyan] first to set up AEOS.")
        raise typer.Exit(1)

    console.print(Panel(f"[bold]AEOS Validation[/bold]\nPath: [cyan]{target}[/cyan]", border_style="blue"))

    # Run lint
    console.print("\n[bold]Step 1: Governance Lint[/bold]\n")
    lint_result = subprocess.run(
        [sys.executable, str(lint_script)],
        capture_output=True,
        text=True,
        cwd=str(target),
    )

    console.print(lint_result.stdout)

    if lint_result.returncode != 0:
        console.print(lint_result.stderr)
        console.print("\n[bold red]Validation FAILED — lint errors[/bold red]")
        raise typer.Exit(1)

    # Run tests if requested and tests/ exists
    if tests and tests_dir.exists():
        console.print("\n[bold]Step 2: Pytest[/bold]\n")
        test_result = subprocess.run(
            [sys.executable, "-m", "pytest", str(tests_dir), "-v"],
            capture_output=True,
            text=True,
            cwd=str(target),
        )

        console.print(test_result.stdout)

        if test_result.returncode != 0:
            console.print(test_result.stderr)
            console.print("\n[bold red]Validation FAILED — test errors[/bold red]")
            raise typer.Exit(1)
    elif tests and not tests_dir.exists():
        console.print("\n[dim]No tests/ directory found. Skipping pytest.[/dim]")

    console.print("\n[bold green]All validations PASSED[/bold green]")
