import os
import yaml
import pytest

BASE_DIR = os.path.join(os.path.dirname(__file__), "..", "..")
AGENTS_DIR = os.path.join(BASE_DIR, "agents")
REGISTRY_PATH = os.path.join(AGENTS_DIR, "agent_registry.yaml")

REQUIRED_AGENT_FIELDS = [
    "agent_id",
    "name",
    "role",
    "business_objective",
    "scope",
    "non_goals",
    "inputs",
    "outputs",
    "permissions",
    "forbidden_actions",
    "memory_policy",
    "tools",
    "escalation_rules",
    "validation_rules",
    "audit_requirements",
    "handoff_protocol",
    "dependencies",
    "lifecycle_stage",
    "success_metrics",
    "failure_modes",
]

EXPECTED_AGENTS = [
    "director-agent",
    "architect-agent",
    "implementer-agent",
    "reviewer-agent",
    "auditor-agent",
    "qa-agent",
    "documentation-agent",
]


def test_agent_registry_exists():
    assert os.path.isfile(REGISTRY_PATH), "agent_registry.yaml is missing"


def test_agent_registry_has_agents():
    with open(REGISTRY_PATH, "r") as f:
        registry = yaml.safe_load(f)
    assert "agents" in registry, "agent_registry.yaml must contain 'agents' key"
    assert len(registry["agents"]) >= len(EXPECTED_AGENTS), "agent_registry.yaml is missing agents"


@pytest.mark.parametrize("agent_id", EXPECTED_AGENTS)
def test_agent_definition_exists(agent_id):
    agent_dir_name = agent_id.replace("-agent", "")
    agent_file = os.path.join(AGENTS_DIR, agent_dir_name, f"{agent_id.replace('-', '_')}.yaml")
    assert os.path.isfile(agent_file), f"Missing agent definition: {agent_file}"


def test_all_agents_have_required_fields():
    agent_dirs = ["director", "architect", "implementer", "reviewer", "auditor", "qa", "documentation"]
    for agent_dir in agent_dirs:
        yaml_files = [f for f in os.listdir(os.path.join(AGENTS_DIR, agent_dir)) if f.endswith(".yaml")]
        for yaml_file in yaml_files:
            filepath = os.path.join(AGENTS_DIR, agent_dir, yaml_file)
            with open(filepath, "r") as f:
                agent = yaml.safe_load(f)
            for field in REQUIRED_AGENT_FIELDS:
                assert field in agent, f"{filepath} missing required field: {field}"


def test_no_agent_can_self_approve():
    agent_dirs = ["director", "architect", "implementer", "reviewer", "auditor", "qa", "documentation"]
    for agent_dir in agent_dirs:
        yaml_files = [f for f in os.listdir(os.path.join(AGENTS_DIR, agent_dir)) if f.endswith(".yaml")]
        for yaml_file in yaml_files:
            filepath = os.path.join(AGENTS_DIR, agent_dir, yaml_file)
            with open(filepath, "r") as f:
                agent = yaml.safe_load(f)
            forbidden = agent.get("forbidden_actions", [])
            assert "Self-approve any decision" in forbidden or \
                   "self-approve" in " ".join(forbidden).lower() or \
                   "Self-approve implementation" in forbidden, \
                f"{filepath} must forbid self-approval"


def test_no_unrestricted_permissions():
    agent_dirs = ["director", "architect", "implementer", "reviewer", "auditor", "qa", "documentation"]
    restricted_levels = {"READ_ONLY", "DOCS_ONLY", "TESTS_ONLY", "LIMITED_IMPLEMENTATION", "CRITICAL_SYSTEM_CHANGE"}
    for agent_dir in agent_dirs:
        yaml_files = [f for f in os.listdir(os.path.join(AGENTS_DIR, agent_dir)) if f.endswith(".yaml")]
        for yaml_file in yaml_files:
            filepath = os.path.join(AGENTS_DIR, agent_dir, yaml_file)
            with open(filepath, "r") as f:
                agent = yaml.safe_load(f)
            permissions = agent.get("permissions", [])
            for perm in permissions:
                assert perm in restricted_levels or perm in {"READ_ALL", "GOVERNANCE_REVIEW", "APPROVAL_AUTHORITY"}, \
                    f"{filepath} has unrestricted permission: {perm}"
