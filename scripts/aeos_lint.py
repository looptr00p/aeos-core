#!/usr/bin/env python3
"""AEOS Core Lint — lightweight operational validation.

Validates:
- Required governance files exist
- Required protocol files exist
- Required template files exist
- Required workflow files exist
- Required memory directories exist
- Agent registry exists and is valid
- Traceability references in memory artifacts
- Workflow closure consistency (closed tasks reference objectives and handoffs)
"""

import os
import re
import sys
import yaml

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(BASE_DIR)

# ── Required file lists ──────────────────────────────────────────────

GOVERNANCE_FILES = [
    "AGENTS.md",
    "PHASE_POLICY.md",
    "PERMISSION_MODEL.md",
    "REVIEW_REQUIREMENTS.md",
    "ESCALATION_POLICY.md",
    "SAFETY_RULES.md",
    "GOVERNANCE_SEVERITY_MODEL.md",
]

PROTOCOL_FILES = [
    "TASK_PROTOCOL.md",
    "REVIEW_PROTOCOL.md",
    "CONTEXT_PROTOCOL.md",
    "MEMORY_PROTOCOL.md",
    "HANDOFF_PROTOCOL.md",
    "INCIDENT_PROTOCOL.md",
    "ADR_PROTOCOL.md",
]

TEMPLATE_FILES = [
    "objective_template.md",
    "adr_template.md",
    "task_template.md",
    "review_template.md",
    "audit_template.md",
    "handoff_template.md",
    "incident_template.md",
    "operational_report_template.md",
    "escalation_template.md",
    "governance_health_report_template.md",
]

WORKFLOW_FILES = [
    "feature_workflow.md",
    "bugfix_workflow.md",
    "architecture_change_workflow.md",
    "audit_workflow.md",
    "incident_workflow.md",
    "research_workflow.md",
]

MEMORY_DIRS = [
    "objectives",
    "decisions",
    "tasks",
    "handoffs",
    "audits",
    "incidents",
    "architecture",
    "research",
    "index",
]

# ── Traceability prefix patterns ─────────────────────────────────────

VALID_SEVERITY_LABELS = {"LOW", "MEDIUM", "HIGH", "CRITICAL"}

TRACEABILITY_PREFIXES = {
    "OBJ": r"OBJ-\d{3,}",
    "ADR": r"ADR-\d{3,}",
    "TASK": r"TASK-\d{3,}",
    "REV": r"REV-\d{3,}",
    "AUD": r"AUD-\d{3,}",
    "HND": r"HND-\d{3,}",
    "INC": r"INC-\d{3,}",
}

# ── Helpers ──────────────────────────────────────────────────────────

def check_file(filepath, label):
    if not os.path.isfile(filepath):
        print(f"  FAIL: Missing {label}: {filepath}")
        return False
    print(f"  OK:   {label}: {filepath}")
    return True


def check_dir(dirpath, label):
    if not os.path.isdir(dirpath):
        print(f"  FAIL: Missing directory {label}: {dirpath}")
        return False
    print(f"  OK:   Directory {label}: {dirpath}")
    return True


def find_traceability_refs(content):
    """Extract all traceability IDs from content."""
    refs = {}
    for prefix, pattern in TRACEABILITY_PREFIXES.items():
        refs[prefix] = set(re.findall(pattern, content))
    return refs


def collect_memory_artifacts(directory):
    """Collect all .md files in a memory directory."""
    artifacts = []
    mem_dir = os.path.join(ROOT_DIR, "memory", directory)
    if not os.path.isdir(mem_dir):
        return artifacts
    for fname in os.listdir(mem_dir):
        if fname.endswith(".md"):
            fpath = os.path.join(mem_dir, fname)
            with open(fpath, "r") as f:
                content = f.read()
            artifacts.append((fname, content))
    return artifacts


# ── Validation checks ────────────────────────────────────────────────

def check_required_files():
    print("\n[1] Required Files")
    all_ok = True

    for fname in GOVERNANCE_FILES:
        if not check_file(os.path.join(ROOT_DIR, "governance", fname), f"governance/{fname}"):
            all_ok = False

    for fname in PROTOCOL_FILES:
        if not check_file(os.path.join(ROOT_DIR, "protocols", fname), f"protocols/{fname}"):
            all_ok = False

    for fname in TEMPLATE_FILES:
        if not check_file(os.path.join(ROOT_DIR, "templates", fname), f"templates/{fname}"):
            all_ok = False

    for fname in WORKFLOW_FILES:
        if not check_file(os.path.join(ROOT_DIR, "workflows", fname), f"workflows/{fname}"):
            all_ok = False

    return all_ok


def check_memory_directories():
    print("\n[2] Memory Directories")
    all_ok = True
    for dname in MEMORY_DIRS:
        if not check_dir(os.path.join(ROOT_DIR, "memory", dname), f"memory/{dname}"):
            all_ok = False
    return all_ok


def check_agent_registry():
    print("\n[3] Agent Registry")
    reg_path = os.path.join(ROOT_DIR, "agents", "agent_registry.yaml")
    if not os.path.isfile(reg_path):
        print(f"  FAIL: agent_registry.yaml missing")
        return False

    with open(reg_path, "r") as f:
        registry = yaml.safe_load(f)

    if "agents" not in registry:
        print("  FAIL: agent_registry.yaml missing 'agents' key")
        return False

    print(f"  OK:   {len(registry['agents'])} agents registered")
    return True


def check_traceability_references():
    print("\n[4] Traceability References")
    all_ok = True

    for mem_dir in MEMORY_DIRS:
        artifacts = collect_memory_artifacts(mem_dir)
        for fname, content in artifacts:
            refs = find_traceability_refs(content)
            for prefix, ids in refs.items():
                for ref_id in ids:
                    print(f"  OK:   {fname} references {ref_id}")

    if not any(collect_memory_artifacts(d) for d in MEMORY_DIRS):
        print("  INFO: No memory artifacts found to validate (expected in Phase 0)")

    return all_ok


def check_workflow_closure():
    print("\n[5] Workflow Closure Validation")
    all_ok = True

    tasks = collect_memory_artifacts("tasks")
    if not tasks:
        print("  INFO: No task artifacts found to validate (expected in Phase 0)")
        return all_ok

    objectives = set()
    handoffs = set()
    adrs = set()
    incidents = set()

    for fname, content in collect_memory_artifacts("objectives"):
        objectives.update(re.findall(TRACEABILITY_PREFIXES["OBJ"], content))
    for fname, content in collect_memory_artifacts("handoffs"):
        handoffs.update(re.findall(TRACEABILITY_PREFIXES["HND"], content))
    for fname, content in collect_memory_artifacts("decisions"):
        adrs.update(re.findall(TRACEABILITY_PREFIXES["ADR"], content))
    for fname, content in collect_memory_artifacts("incidents"):
        incidents.update(re.findall(TRACEABILITY_PREFIXES["INC"], content))

    for fname, content in tasks:
        refs = find_traceability_refs(content)

        is_closed = "CLOSE" in content.upper() or "COMPLETE" in content.upper()

        if is_closed:
            if not refs["OBJ"]:
                print(f"  FAIL: Closed task {fname} does not reference an objective")
                all_ok = False
            else:
                obj_ref = list(refs["OBJ"])[0]
                if obj_ref not in objectives:
                    print(f"  FAIL: Closed task {fname} references non-existent {obj_ref}")
                    all_ok = False
                else:
                    print(f"  OK:   Closed task {fname} references valid {obj_ref}")

            if not refs["HND"]:
                print(f"  FAIL: Closed task {fname} does not reference a handoff")
                all_ok = False
            else:
                hnd_ref = list(refs["HND"])[0]
                if hnd_ref not in handoffs:
                    print(f"  FAIL: Closed task {fname} references non-existent {hnd_ref}")
                    all_ok = False
                else:
                    print(f"  OK:   Closed task {fname} references valid {hnd_ref}")

        if refs["ADR"]:
            for adr_ref in refs["ADR"]:
                if adr_ref not in adrs:
                    print(f"  FAIL: Task {fname} references non-existent {adr_ref}")
                    all_ok = False
                else:
                    print(f"  OK:   Task {fname} references valid {adr_ref}")

        if refs["INC"]:
            for inc_ref in refs["INC"]:
                if inc_ref not in incidents:
                    print(f"  FAIL: Task {fname} references non-existent {inc_ref}")
                    all_ok = False
                else:
                    print(f"  OK:   Task {fname} references valid {inc_ref}")

    return all_ok


def check_v03_documents():
    print("\n[6] v0.3 Operational Documents")
    all_ok = True

    v03_docs = [
        ("governance/GOVERNANCE_SEVERITY_MODEL.md", os.path.join(ROOT_DIR, "governance", "GOVERNANCE_SEVERITY_MODEL.md")),
        ("docs/REVIEW_CADENCE.md", os.path.join(ROOT_DIR, "docs", "REVIEW_CADENCE.md")),
        ("docs/OPERATIONAL_EXAMPLES.md", os.path.join(ROOT_DIR, "docs", "OPERATIONAL_EXAMPLES.md")),
    ]
    for label, filepath in v03_docs:
        if not check_file(filepath, label):
            all_ok = False

    v03_templates = [
        ("templates/escalation_template.md", os.path.join(ROOT_DIR, "templates", "escalation_template.md")),
        ("templates/governance_health_report_template.md", os.path.join(ROOT_DIR, "templates", "governance_health_report_template.md")),
    ]
    for label, filepath in v03_templates:
        if not check_file(filepath, label):
            all_ok = False

    return all_ok


def check_severity_labels():
    print("\n[7] Severity Label Validation")
    all_ok = True

    severity_file = os.path.join(ROOT_DIR, "governance", "GOVERNANCE_SEVERITY_MODEL.md")
    if not os.path.isfile(severity_file):
        print(f"  FAIL: GOVERNANCE_SEVERITY_MODEL.md not found")
        return False

    with open(severity_file, "r") as f:
        content = f.read()

    for label in VALID_SEVERITY_LABELS:
        if f"### {label}" in content:
            print(f"  OK:   Severity level {label} defined")
        else:
            print(f"  FAIL: Severity level {label} not defined")
            all_ok = False

    return all_ok


# ── Main ─────────────────────────────────────────────────────────────

def main():
    print("=" * 60)
    print("AEOS Core Lint — Operational Validation")
    print("=" * 60)

    results = []
    results.append(("Required Files", check_required_files()))
    results.append(("Memory Directories", check_memory_directories()))
    results.append(("Agent Registry", check_agent_registry()))
    results.append(("Traceability References", check_traceability_references()))
    results.append(("Workflow Closure", check_workflow_closure()))
    results.append(("v0.3 Documents", check_v03_documents()))
    results.append(("Severity Labels", check_severity_labels()))

    print("\n" + "=" * 60)
    print("Summary")
    print("=" * 60)

    all_pass = True
    for name, passed in results:
        status = "PASS" if passed else "FAIL"
        print(f"  [{status}] {name}")
        if not passed:
            all_pass = False

    print("=" * 60)

    if all_pass:
        print("ALL CHECKS PASSED")
        return 0
    else:
        print("SOME CHECKS FAILED")
        return 1


if __name__ == "__main__":
    sys.exit(main())
