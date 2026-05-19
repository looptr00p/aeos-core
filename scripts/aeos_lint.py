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


def check_traceability_integrity():
    print("\n[8] Traceability Integrity")
    all_ok = True

    all_ids = {}
    malformed_ids = []

    for mem_dir in MEMORY_DIRS:
        artifacts = collect_memory_artifacts(mem_dir)
        for fname, content in artifacts:
            refs = find_traceability_refs(content)
            for prefix, ids in refs.items():
                for ref_id in ids:
                    if ref_id not in all_ids:
                        all_ids[ref_id] = []
                    all_ids[ref_id].append(fname)

    all_id_keys = set(all_ids.keys())

    for ref_id in all_id_keys:
        prefix = ref_id.split("-")[0]
        if prefix not in TRACEABILITY_PREFIXES:
            malformed_ids.append(ref_id)
            all_ok = False

    if malformed_ids:
        for mid in malformed_ids:
            print(f"  FAIL: Malformed ID prefix: {mid}")
    else:
        print("  OK:   No malformed ID prefixes")

    duplicates = {k: v for k, v in all_ids.items() if len(v) > 1 and len(set(v)) > 1}
    if duplicates:
        for dup_id, files in duplicates.items():
            print(f"  WARN: ID {dup_id} referenced in multiple files: {', '.join(files)}")
    else:
        print("  OK:   No duplicate lifecycle IDs")

    all_referenced = set()
    for mem_dir in MEMORY_DIRS:
        artifacts = collect_memory_artifacts(mem_dir)
        for fname, content in artifacts:
            refs = find_traceability_refs(content)
            for prefix, ids in refs.items():
                all_referenced.update(ids)

    defined_ids = set()
    for mem_dir in MEMORY_DIRS:
        artifacts = collect_memory_artifacts(mem_dir)
        for fname, content in artifacts:
            refs = find_traceability_refs(content)
            for prefix, ids in refs.items():
                for ref_id in ids:
                    if ref_id.split("-")[0] == prefix:
                        defined_ids.add(ref_id)

    missing = all_referenced - defined_ids
    if missing:
        for mid in sorted(missing):
            print(f"  WARN: Referenced ID not defined as artifact: {mid}")
    else:
        print("  OK:   All referenced IDs are defined as artifacts")

    return all_ok


def check_concurrent_objective_operations():
    print("\n[10] Concurrent Objective Operations")
    all_ok = True

    objectives = collect_memory_artifacts("objectives")
    incidents = collect_memory_artifacts("incidents")

    active_objectives = []
    for fname, content in objectives:
        status_match = re.search(r"## Status\s*\n\s*(\w+)", content)
        status = status_match.group(1) if status_match else ""
        if status == "ACTIVE":
            active_objectives.append((fname, content))

    open_escalations = []
    for fname, content in incidents:
        if fname.startswith("ESC-"):
            status_match = re.search(r"## Status\s*\n\s*(\w+)", content)
            status = status_match.group(1) if status_match else ""
            if status == "OPEN":
                open_escalations.append((fname, content))

    print(f"  INFO: {len(active_objectives)} ACTIVE objectives")
    print(f"  INFO: {len(open_escalations)} OPEN escalations")

    if len(active_objectives) >= 2:
        obj_ids = [re.findall(TRACEABILITY_PREFIXES["OBJ"], c) for _, c in active_objectives]
        obj_ids = [ids[0] for ids in obj_ids if ids]
        print(f"  WARN: Concurrent ACTIVE objectives detected: {', '.join(obj_ids)}")
        print(f"  INFO: Reviewer contention risk elevated under concurrent objectives")
        print(f"  INFO: Escalation accumulation rate may double under concurrency")

    if len(open_escalations) >= 2:
        esc_ids = [f for f, _ in open_escalations]
        print(f"  WARN: Multiple OPEN escalations detected: {', '.join(esc_ids)}")
        print(f"  INFO: Escalation accumulation risk — monitor resolution cadence")

    active_incidents = []
    for fname, content in incidents:
        if not fname.startswith("ESC-"):
            status_match = re.search(r"## Status\s*\n\s*(\w+)", content)
            status = status_match.group(1) if status_match else ""
            if status == "ACTIVE":
                active_incidents.append((fname, content))

    if len(active_incidents) >= 2:
        inc_ids = [f for f, _ in active_incidents]
        print(f"  WARN: Multiple ACTIVE incidents detected: {', '.join(inc_ids)}")
        print(f"  INFO: Incident resolution capacity split across concurrent incidents")

    if not active_objectives and not open_escalations and not active_incidents:
        print("  INFO: No concurrent operational pressure detected")

    return all_ok


def check_unresolved_lifecycle_continuity():
    print("\n[9] Unresolved Lifecycle Continuity")
    all_ok = True

    tasks = collect_memory_artifacts("tasks")
    incidents = collect_memory_artifacts("incidents")

    objectives = set()
    for fname, content in collect_memory_artifacts("objectives"):
        objectives.update(re.findall(TRACEABILITY_PREFIXES["OBJ"], content))

    active_incidents = []
    open_escalations = []
    in_progress_tasks = []

    for fname, content in incidents:
        status_match = re.search(r"## Status\s*\n\s*(\w+)", content)
        severity_match = re.search(r"## Severity\s*\n\s*(\w+)", content)
        status = status_match.group(1) if status_match else ""
        severity = severity_match.group(1) if severity_match else ""
        is_escalation = fname.startswith("ESC-")

        if is_escalation and status == "OPEN":
            open_escalations.append((fname, content, severity))
        elif not is_escalation and status == "ACTIVE":
            active_incidents.append((fname, content, severity))

    for fname, content in tasks:
        status_match = re.search(r"## Status\s*\n\s*(\w+(?:_\w+)?)", content)
        status = status_match.group(1) if status_match else ""
        if status == "IN_PROGRESS":
            in_progress_tasks.append((fname, content))

    print(f"  INFO: {len(in_progress_tasks)} IN_PROGRESS tasks")
    print(f"  INFO: {len(active_incidents)} ACTIVE incidents")
    print(f"  INFO: {len(open_escalations)} OPEN escalations")

    for fname, content, severity in active_incidents:
        refs = find_traceability_refs(content)
        if not refs["TASK"] and not refs["OBJ"]:
            print(f"  FAIL: ACTIVE incident {fname} has no task or objective references")
            all_ok = False
        else:
            obj_refs = refs["OBJ"]
            valid_obj = bool(obj_refs & objectives) if obj_refs else True
            if not valid_obj:
                print(f"  FAIL: ACTIVE incident {fname} references non-existent objective")
                all_ok = False
            else:
                print(f"  OK:   ACTIVE incident {fname} ({severity}) has valid references")

    for fname, content, severity in open_escalations:
        refs = find_traceability_refs(content)
        if not refs["TASK"] and not refs["OBJ"]:
            print(f"  FAIL: OPEN escalation {fname} has no task or objective references")
            all_ok = False
        else:
            obj_refs = refs["OBJ"]
            valid_obj = bool(obj_refs & objectives) if obj_refs else True
            if not valid_obj:
                print(f"  FAIL: OPEN escalation {fname} references non-existent objective")
                all_ok = False
            else:
                print(f"  OK:   OPEN escalation {fname} ({severity}) has valid references")

    for fname, content in in_progress_tasks:
        refs = find_traceability_refs(content)
        if not refs["OBJ"]:
            print(f"  FAIL: IN_PROGRESS task {fname} has no objective reference")
            all_ok = False
        else:
            obj_ref = list(refs["OBJ"])[0]
            if obj_ref not in objectives:
                print(f"  FAIL: IN_PROGRESS task {fname} references non-existent {obj_ref}")
                all_ok = False
            else:
                print(f"  OK:   IN_PROGRESS task {fname} references valid {obj_ref}")

    if not active_incidents and not open_escalations and not in_progress_tasks:
        print("  INFO: No unresolved lifecycle artifacts found")

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
    results.append(("Traceability Integrity", check_traceability_integrity()))
    results.append(("Unresolved Lifecycle Continuity", check_unresolved_lifecycle_continuity()))
    results.append(("Concurrent Objective Operations", check_concurrent_objective_operations()))

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
