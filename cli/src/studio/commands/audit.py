"""studio audit — Run governance audit and lint validation."""

import subprocess
import sys
from pathlib import Path
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
import typer

audit_app = typer.Typer()
console = Console()


@audit_app.command()
def run(
    project_path: str = typer.Argument(".", help="Path to the project directory"),
):
    """Run a full governance audit including lint and traceability checks."""

    target = Path(project_path).resolve()
    lint_script = target / "scripts" / "aeos_lint.py"

    if not lint_script.exists():
        console.print(f"[bold red]Error:[/bold red] aeos_lint.py not found at {lint_script}")
        console.print("Run [cyan]studio init[/cyan] first to set up AEOS.")
        raise typer.Exit(1)

    console.print(Panel(f"[bold]AEOS Governance Audit[/bold]\nPath: [cyan]{target}[/cyan]", border_style="yellow"))

    # Run lint
    console.print("\n[bold]Running aeos_lint.py...[/bold]\n")
    result = subprocess.run(
        [sys.executable, str(lint_script)],
        capture_output=True,
        text=True,
        cwd=str(target),
    )

    console.print(result.stdout)

    if result.returncode != 0:
        console.print(result.stderr)
        console.print("\n[bold red]Audit FAILED[/bold red]")
        raise typer.Exit(1)

    # Check for open escalations
    memory_dir = target / "memory"
    incidents_dir = memory_dir / "incidents"
    open_escalations = []
    if incidents_dir.exists():
        for f in incidents_dir.glob("ESC-*.md"):
            content = f.read_text()
            if "## Status" in content and "OPEN" in content.split("## Status")[1].split("##")[0]:
                open_escalations.append(f.name)

    if open_escalations:
        console.print(f"\n[bold red]Open Escalations:[/bold red]")
        for esc in open_escalations:
            console.print(f"  - {esc}")
        console.print("\n[bold yellow]Resolve escalations before closing objectives.[/bold yellow]")

    # Check for active incidents
    active_incidents = []
    if incidents_dir.exists():
        for f in incidents_dir.glob("INC-*.md"):
            content = f.read_text()
            if "## Status" in content and "ACTIVE" in content.split("## Status")[1].split("##")[0]:
                active_incidents.append(f.name)

    if active_incidents:
        console.print(f"\n[bold yellow]Active Incidents:[/bold yellow]")
        for inc in active_incidents:
            console.print(f"  - {inc}")

    console.print("\n[bold green]Audit PASSED[/bold green]")
