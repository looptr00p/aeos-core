"""studio status — Show project state: agents, memory, backlog."""

import os
import re
from pathlib import Path
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
import typer

status_app = typer.Typer()
console = Console()

TRACEABILITY_PREFIXES = {
    "OBJ": r"OBJ-\d{3,}",
    "TASK": r"TASK-\d{3,}",
    "ADR": r"ADR-\d{3,}",
    "REV": r"REV-\d{3,}",
    "AUD": r"AUD-\d{3,}",
    "HND": r"HND-\d{3,}",
    "INC": r"INC-\d{3,}",
    "ESC": r"ESC-\d{3,}",
    "ST": r"ST-\d{3,}",
}


def _find_ids(content: str) -> dict[str, list[str]]:
    refs = {}
    for prefix, pattern in TRACEABILITY_PREFIXES.items():
        refs[prefix] = re.findall(pattern, content)
    return refs


def _get_status(content: str) -> str:
    match = re.search(r"## Status\s*\n\s*(\w+(?:_\w+)?)", content)
    return match.group(1) if match else "UNKNOWN"


def _scan_memory_dir(base: Path, subdir: str) -> list[tuple[str, str, str]]:
    """Scan a memory directory and return (filename, status, content) tuples."""
    results = []
    mem_dir = base / "memory" / subdir
    if not mem_dir.exists():
        return results
    for f in sorted(mem_dir.glob("*.md")):
        content = f.read_text()
        status = _get_status(content)
        results.append((f.name, status, content))
    return results


@status_app.command()
def run(
    project_path: str = typer.Argument(".", help="Path to the project directory"),
):
    """Show the current state of an AEOS-governed project."""

    target = Path(project_path).resolve()
    memory_dir = target / "memory"

    if not memory_dir.exists():
        console.print(f"[bold red]Error:[/bold red] Not an AEOS project. No memory/ directory found at {target}")
        raise typer.Exit(1)

    console.print(Panel(f"[bold]AEOS Project Status[/bold]\nPath: [cyan]{target}[/cyan]", border_style="blue"))

    # Objectives
    objectives = _scan_memory_dir(target, "objectives")
    if objectives:
        table = Table(title="Objectives")
        table.add_column("ID", style="cyan")
        table.add_column("Status", style="bold")
        for fname, status, _ in objectives:
            aid = fname.replace(".md", "")
            status_color = {"ACTIVE": "green", "CLOSED": "dim", "DRAFT": "yellow"}.get(status, "white")
            table.add_row(aid, f"[{status_color}]{status}[/{status_color}]")
        console.print(table)
    else:
        console.print("[dim]No objectives found[/dim]")

    # Tasks
    tasks = _scan_memory_dir(target, "tasks")
    if tasks:
        table = Table(title="Tasks")
        table.add_column("ID", style="cyan")
        table.add_column("Status", style="bold")
        for fname, status, _ in tasks:
            aid = fname.replace(".md", "")
            status_color = {"IN_PROGRESS": "yellow", "CLOSED": "dim", "DRAFT": "white"}.get(status, "white")
            table.add_row(aid, f"[{status_color}]{status}[/{status_color}]")
        console.print(table)
    else:
        console.print("[dim]No tasks found[/dim]")

    # Decisions (ADRs)
    adrs = _scan_memory_dir(target, "decisions")
    if adrs:
        table = Table(title="Architecture Decisions")
        table.add_column("ID", style="cyan")
        table.add_column("Status", style="bold")
        for fname, status, _ in adrs:
            aid = fname.replace(".md", "")
            status_color = {"PROPOSED": "yellow", "ACTIVE": "green", "REPLACED": "dim"}.get(status, "white")
            table.add_row(aid, f"[{status_color}]{status}[/{status_color}]")
        console.print(table)
    else:
        console.print("[dim]No architecture decisions found[/dim]")

    # Incidents
    incidents = _scan_memory_dir(target, "incidents")
    if incidents:
        table = Table(title="Incidents & Escalations")
        table.add_column("ID", style="cyan")
        table.add_column("Status", style="bold")
        for fname, status, _ in incidents:
            aid = fname.replace(".md", "")
            status_color = {"ACTIVE": "red", "OPEN": "red", "RESOLVED": "green", "IN_REVIEW": "yellow"}.get(status, "white")
            table.add_row(aid, f"[{status_color}]{status}[/{status_color}]")
        console.print(table)
    else:
        console.print("[dim]No incidents or escalations[/dim]")

    # State transitions
    transitions = _scan_memory_dir(target, "state-log")
    if transitions:
        console.print(f"\n[bold]State Transitions:[/bold] {len(transitions)} recorded")
    else:
        console.print("[dim]No state transitions recorded[/dim]")

    # Artifact counts
    console.print("\n[bold]Artifact Summary[/bold]")
    total = 0
    for subdir in ["objectives", "tasks", "decisions", "handoffs", "reviews", "audits", "incidents", "state-log"]:
        count = len(list((memory_dir / subdir).glob("*.md"))) if (memory_dir / subdir).exists() else 0
        total += count
        console.print(f"  {subdir}: {count}")
    console.print(f"  [bold]Total: {total}[/bold]")

    # Agent check
    opencode_json = target / ".opencode" / "opencode.json"
    if opencode_json.exists():
        import json
        config = json.loads(opencode_json.read_text())
        agents = config.get("agent", {})
        console.print(f"\n[bold]Agents:[/bold] {len(agents)} configured")
        for name, agent_config in agents.items():
            model = agent_config.get("model", "unknown")
            mode = agent_config.get("mode", "unknown")
            console.print(f"  {name} ({mode}) — {model}")
