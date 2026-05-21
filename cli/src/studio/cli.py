"""AEOS Studio CLI entry point."""

import typer
from rich.console import Console

from studio.commands.init import init_app
from studio.commands.status import status_app
from studio.commands.audit import audit_app
from studio.commands.validate import validate_app

app = typer.Typer(
    name="studio",
    help="AEOS Studio — CLI for AI Engineering Operating System",
    add_completion=False,
)

console = Console()

app.add_typer(init_app, name="init", help="Bootstrap AEOS in a new or existing project")
app.add_typer(status_app, name="status", help="Show project state: agents, memory, backlog")
app.add_typer(audit_app, name="audit", help="Run governance audit and lint validation")
app.add_typer(validate_app, name="validate", help="Run aeos_lint.py and pytest")

@app.command()
def version():
    """Show AEOS Studio version."""
    from studio import __version__
    console.print(f"[bold green]AEOS Studio[/bold green] v{__version__}")

if __name__ == "__main__":
    app()
