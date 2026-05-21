"""studio init — Bootstrap AEOS in a new or existing project."""

import os
import shutil
import typer
from pathlib import Path
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn

init_app = typer.Typer()
console = Console()

# Path to the AEOS Core template directory
# The CLI is at cli/src/studio/commands/, template is at ../../../../template
TEMPLATE_DIR = Path(__file__).parents[3] / "template"

# Fallback: if template doesn't exist relative to CLI, try relative to cwd
if not TEMPLATE_DIR.exists():
    TEMPLATE_DIR = Path.cwd().parent / "template"

PROFILES = {
    "full": {
        "description": "All governance files, all protocols, all workflows",
        "governance": None,  # None means all
        "protocols": None,
        "workflows": None,
    },
    "standard": {
        "description": "Core governance, essential protocols, main workflows",
        "governance": [
            "AGENTS.md", "PERMISSION_MODEL.md", "SAFETY_RULES.md",
            "ESCALATION_POLICY.md", "GOVERNANCE_SEVERITY_MODEL.md",
        ],
        "protocols": [
            "HANDOFF_PROTOCOL.md", "MEMORY_PROTOCOL.md", "REVIEW_PROTOCOL.md",
            "TASK_PROTOCOL.md", "ADR_PROTOCOL.md", "STATE_TRANSITION_PROTOCOL.md",
        ],
        "workflows": [
            "feature_workflow.md", "bugfix_workflow.md", "state_graph.md",
        ],
    },
    "lite": {
        "description": "Minimal governance, basic protocols, single workflow",
        "governance": ["AGENTS.md", "SAFETY_RULES.md", "ESCALATION_POLICY.md"],
        "protocols": ["HANDOFF_PROTOCOL.md", "MEMORY_PROTOCOL.md", "TASK_PROTOCOL.md"],
        "workflows": ["feature_workflow.md"],
    },
}


def _copy_dir(src: Path, dst: Path, include_files: list[str] | None = None):
    """Copy directory, optionally filtering files."""
    dst.mkdir(parents=True, exist_ok=True)
    for item in src.iterdir():
        if item.is_dir():
            if item.name.startswith("."):
                _copy_dir(item, dst / item.name)
            else:
                _copy_dir(item, dst / item.name)
        elif item.is_file():
            if include_files is None or item.name in include_files:
                shutil.copy2(item, dst / item.name)


def _copy_filtered(src: Path, dst: Path, include_files: list[str] | None = None):
    """Copy files from src to dst, filtering by include_files."""
    dst.mkdir(parents=True, exist_ok=True)
    for item in src.iterdir():
        if item.is_file() and (include_files is None or item.name in include_files):
            shutil.copy2(item, dst / item.name)


@init_app.command()
def run(
    project_path: str = typer.Argument(".", help="Path to the project directory"),
    profile: str = typer.Option("standard", "-p", "--profile", help="Governance profile: full, standard, lite"),
    force: bool = typer.Option(False, "-f", "--force", help="Overwrite existing AEOS files"),
):
    """Bootstrap AEOS governance framework in a project."""

    profile = profile.lower()
    if profile not in PROFILES:
        console.print(f"[bold red]Error:[/bold red] Unknown profile '{profile}'. Choose: {', '.join(PROFILES.keys())}")
        raise typer.Exit(1)

    target = Path(project_path).resolve()
    if not target.exists():
        console.print(f"[bold red]Error:[/bold red] Path does not exist: {target}")
        raise typer.Exit(1)

    profile_config = PROFILES[profile]

    console.print(Panel(
        f"[bold]AEOS Bootstrap[/bold]\n"
        f"Profile: [cyan]{profile}[/cyan] — {profile_config['description']}\n"
        f"Target: [cyan]{target}[/cyan]",
        title="Initializing AEOS",
        border_style="green",
    ))

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
    ) as progress:

        # 1. Copy .aegos/
        task = progress.add_task("[cyan]Copying governance framework...", total=None)
        aegos_src = TEMPLATE_DIR / ".aegos"
        aegos_dst = target / ".aegos"

        if aegos_dst.exists() and not force:
            console.print(f"[yellow]Warning:[/yellow] .aegos/ already exists. Use --force to overwrite.")
        else:
            if aegos_dst.exists():
                shutil.rmtree(aegos_dst)

            # Copy governance with profile filter
            governance_src = aegos_src / "governance"
            governance_dst = aegos_dst / "governance"
            _copy_filtered(governance_src, governance_dst, profile_config["governance"])

            # Copy protocols with profile filter
            protocols_src = aegos_src / "protocols"
            protocols_dst = aegos_dst / "protocols"
            _copy_filtered(protocols_src, protocols_dst, profile_config["protocols"])

            # Copy workflows with profile filter
            workflows_src = aegos_src / "workflows"
            workflows_dst = aegos_dst / "workflows"
            _copy_filtered(workflows_src, workflows_dst, profile_config["workflows"])

            # Copy all templates (always useful)
            templates_src = aegos_src / "templates"
            templates_dst = aegos_dst / "templates"
            _copy_dir(templates_src, templates_dst)

        progress.update(task, description="[green]Governance framework copied")

        # 2. Copy .opencode/
        task = progress.add_task("[cyan]Copying OpenCode configuration...", total=None)
        opencode_src = TEMPLATE_DIR / ".opencode"
        opencode_dst = target / ".opencode"

        if opencode_dst.exists() and not force:
            console.print(f"[yellow]Warning:[/yellow] .opencode/ already exists. Use --force to overwrite.")
        else:
            if opencode_dst.exists():
                shutil.rmtree(opencode_dst)
            shutil.copytree(opencode_src, opencode_dst)

        progress.update(task, description="[green]OpenCode configuration copied")

        # 3. Copy memory/
        task = progress.add_task("[cyan]Creating memory structure...", total=None)
        memory_src = TEMPLATE_DIR / "memory"
        memory_dst = target / "memory"

        if memory_dst.exists() and not force:
            console.print(f"[yellow]Warning:[/yellow] memory/ already exists. Skipping.")
        else:
            shutil.copytree(memory_src, memory_dst)

        progress.update(task, description="[green]Memory structure created")

        # 4. Copy scripts/
        task = progress.add_task("[cyan]Copying validation scripts...", total=None)
        scripts_src = TEMPLATE_DIR / "scripts"
        scripts_dst = target / "scripts"

        if scripts_dst.exists() and not force:
            console.print(f"[yellow]Warning:[/yellow] scripts/ already exists. Use --force to overwrite.")
        else:
            scripts_dst.mkdir(parents=True, exist_ok=True)
            shutil.copy2(scripts_src / "aeos_lint.py", scripts_dst / "aeos_lint.py")

        progress.update(task, description="[green]Validation scripts copied")

        # 5. Copy AGENTS.md
        task = progress.add_task("[cyan]Copying agent constraints...", total=None)
        agents_src = TEMPLATE_DIR / "AGENTS.md"
        agents_dst = target / "AGENTS.md"

        if agents_dst.exists() and not force:
            console.print(f"[yellow]Warning:[/yellow] AGENTS.md already exists. Use --force to overwrite.")
        else:
            shutil.copy2(agents_src, agents_dst)

        progress.update(task, description="[green]Agent constraints copied")

        # 6. Copy project-charter.md
        task = progress.add_task("[cyan]Creating project charter template...", total=None)
        charter_src = TEMPLATE_DIR / "project-charter.md"
        charter_dst = target / "project-charter.md"

        if charter_dst.exists() and not force:
            console.print(f"[yellow]Warning:[/yellow] project-charter.md already exists. Skipping.")
        else:
            shutil.copy2(charter_src, charter_dst)

        progress.update(task, description="[green]Project charter created")

    console.print("\n[bold green]AEOS initialized successfully![/bold green]")
    console.print(f"\nNext steps:")
    console.print(f"  1. Edit [cyan]project-charter.md[/cyan] with your project details")
    console.print(f"  2. Run [cyan]studio validate[/cyan] to check setup")
    console.print(f"  3. Start an OpenCode session — the director agent will guide you")
    console.print(f"\nGovernance profile: [bold]{profile}[/bold]")
    console.print(f"  Governance files: {profile_config['governance'] if profile_config['governance'] else 'all'}")
    console.print(f"  Protocols: {profile_config['protocols'] if profile_config['protocols'] else 'all'}")
    console.print(f"  Workflows: {profile_config['workflows'] if profile_config['workflows'] else 'all'}")
