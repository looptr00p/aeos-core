#!/usr/bin/env node
/**
 * AEOS Repository Scanner — Deterministic
 *
 * Reads repository markdown files and outputs aeos-state.json.
 * No AI parsing. No semantic classification. No inference.
 *
 * Usage: node scripts/scan-aeos-repo.mjs
 * Run from: dashboard/ directory (sibling to governance/, memory/, docs/)
 */

import { readdirSync, readFileSync, statSync, writeFileSync, mkdirSync, existsSync } from "fs";
import { join, relative } from "path";
import { fileURLToPath } from "url";
import { dirname } from "path";

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);
// scripts/ is inside dashboard/, so go up 2 levels to reach repo root
const ROOT = join(__dirname, "..", "..");
const OUTPUT = join(__dirname, "..", "generated", "aeos-state.json");

// --- Helpers ---

function readLines(filePath) {
  try {
    return readFileSync(filePath, "utf-8").split("\n");
  } catch {
    return [];
  }
}

function extractField(lines, pattern) {
  for (const line of lines) {
    const m = line.match(pattern);
    if (m) return m[1]?.trim() || null;
  }
  return null;
}

function extractHeading(lines) {
  for (const line of lines) {
    if (line.startsWith("# ") && !line.startsWith("# AEOS")) {
      return line.replace(/^#\s*/, "").trim();
    }
  }
  return null;
}

function extractOperationalState(lines) {
  return extractField(lines, /\*\*Operational State\*\*:\s*(.+)/);
}

function extractStatus(lines) {
  let found = false;
  for (const line of lines) {
    if (line.trim() === "## Status") {
      found = true;
      continue;
    }
    if (found && line.trim() && !line.startsWith("#")) {
      return line.trim();
    }
    if (found && line.startsWith("#")) {
      return null;
    }
  }
  return null;
}

function extractTitle(lines) {
  let found = false;
  for (const line of lines) {
    if (line.trim() === "## Title") {
      found = true;
      continue;
    }
    if (found && line.trim()) {
      return line.trim();
    }
    if (found && line.startsWith("##")) {
      return null;
    }
  }
  return null;
}

function extractPurpose(lines) {
  let found = false;
  const parts = [];
  for (const line of lines) {
    if (line.trim() === "## Purpose") {
      found = true;
      continue;
    }
    if (found && line.startsWith("## ")) break;
    if (found && line.trim()) parts.push(line.trim());
  }
  return parts.join(" ").slice(0, 200) || null;
}

function extractRisks(lines) {
  const risks = [];
  let inSection = false;
  for (const line of lines) {
    const trimmed = line.trim();
    if (
      trimmed.startsWith("## Known Operational Risks") ||
      trimmed.startsWith("## Known Risks") ||
      trimmed.startsWith("## Operational Risks") ||
      trimmed.startsWith("## Risks") ||
      trimmed.startsWith("## Risk")
    ) {
      inSection = true;
      continue;
    }
    if (inSection && trimmed.startsWith("## ")) break;
    if (inSection && trimmed.startsWith("- ")) {
      risks.push(trimmed.replace(/^- /, ""));
    }
  }
  return risks.length ? risks : null;
}

function walkDir(dir) {
  try {
    return readdirSync(dir).filter((f) => f.endsWith(".md")).sort();
  } catch {
    return [];
  }
}

function fileMtime(filePath) {
  try {
    return statSync(filePath).mtime.toISOString().split("T")[0];
  } catch {
    return null;
  }
}

function relPath(filePath) {
  return relative(ROOT, filePath);
}

// --- Scanners ---

function scanGovernance() {
  const dir = join(ROOT, "governance");
  return walkDir(dir).map((f) => {
    const path = join(dir, f);
    const lines = readLines(path);
    return {
      file: f,
      path: relPath(path),
      title: extractHeading(lines),
      operationalState: extractOperationalState(lines),
      modified: fileMtime(path),
    };
  });
}

function scanProtocols() {
  const dir = join(ROOT, "protocols");
  return walkDir(dir).map((f) => {
    const path = join(dir, f);
    const lines = readLines(path);
    return {
      file: f,
      path: relPath(path),
      title: extractHeading(lines),
      modified: fileMtime(path),
    };
  });
}

function scanTemplates() {
  const dir = join(ROOT, "templates");
  return walkDir(dir).map((f) => {
    const path = join(dir, f);
    const lines = readLines(path);
    return {
      file: f,
      path: relPath(path),
      title: extractHeading(lines),
      modified: fileMtime(path),
    };
  });
}

function scanWorkflows() {
  const dir = join(ROOT, "workflows");
  return walkDir(dir).map((f) => {
    const path = join(dir, f);
    const lines = readLines(path);
    return {
      file: f,
      path: relPath(path),
      title: extractHeading(lines),
      modified: fileMtime(path),
    };
  });
}

function scanAgents() {
  const dir = join(ROOT, "agents");
  try {
    return readdirSync(dir)
      .filter((d) => !d.includes("registry"))
      .sort()
      .map((d) => {
        const yamlPath = join(dir, d, "agent.yaml");
        return {
          name: d,
          path: relPath(yamlPath),
          exists: existsSync(yamlPath),
        };
      });
  } catch {
    return [];
  }
}

function scanObjectives() {
  const dir = join(ROOT, "memory", "objectives");
  return walkDir(dir).map((f) => {
    const path = join(dir, f);
    const lines = readLines(path);
    return {
      file: f,
      path: relPath(path),
      id: extractField(lines, /\*\*Traceability ID\*\*:\s*(.+)/),
      title: extractTitle(lines),
      status: extractStatus(lines),
      operationalState: extractOperationalState(lines),
      modified: fileMtime(path),
    };
  });
}

function scanADRs() {
  const dir = join(ROOT, "memory", "decisions");
  return walkDir(dir).map((f) => {
    const path = join(dir, f);
    const lines = readLines(path);
    return {
      file: f,
      path: relPath(path),
      id: extractField(lines, /\*\*Traceability ID\*\*:\s*(.+)/),
      title: extractTitle(lines),
      status: extractStatus(lines),
      operationalState: extractOperationalState(lines),
      modified: fileMtime(path),
    };
  });
}

function scanDocs() {
  const dir = join(ROOT, "docs");
  return walkDir(dir).map((f) => {
    const path = join(dir, f);
    const lines = readLines(path);
    return {
      file: f,
      path: relPath(path),
      title: extractHeading(lines),
      operationalState: extractOperationalState(lines),
      modified: fileMtime(path),
    };
  });
}

function scanBaseline() {
  const dir = join(ROOT, "docs");
  const files = walkDir(dir);
  const baselineFile = files.find((f) => f.startsWith("GOVERNANCE_BASELINE"));
  if (!baselineFile) return null;
  const path = join(dir, baselineFile);
  const lines = readLines(path);
  const version = extractField(lines, /#\s*AEOS Governance Baseline\s+(v[\d.]+)/i) || "unknown";
  const risks = extractRisks(lines);
  return {
    file: baselineFile,
    path: relPath(path),
    version,
    risks,
    modified: fileMtime(path),
  };
}

function scanKnowledgeBase() {
  const dir = join(ROOT, "gpt_knowledge_base");
  let count = 0;
  function countFiles(d) {
    try {
      for (const entry of readdirSync(d, { withFileTypes: true })) {
        const full = join(d, entry.name);
        if (entry.isDirectory()) countFiles(full);
        else if (entry.name.endsWith(".md")) count++;
      }
    } catch {}
  }
  countFiles(dir);
  return count;
}

function scanLintStatus() {
  const lintPath = join(ROOT, "scripts", "aeos_lint.py");
  if (!existsSync(lintPath)) return { exists: false, checkCount: 0 };
  const lines = readLines(lintPath);
  let checkCount = 0;
  for (const line of lines) {
    if (line.match(/^def check_/)) checkCount++;
  }
  // Subtract helper functions (check_file, check_dir)
  checkCount = Math.max(0, checkCount - 2);
  return { exists: true, checkCount };
}

function scanTestCount() {
  let count = 0;
  function countTests(dir) {
    try {
      for (const entry of readdirSync(dir, { withFileTypes: true })) {
        const full = join(dir, entry.name);
        if (entry.isDirectory()) countTests(full);
        else if (entry.name.startsWith("test_") && entry.name.endsWith(".py")) count++;
      }
    } catch {}
  }
  countTests(join(ROOT, "tests"));
  countTests(join(ROOT, "aeos-core", "tests"));
  return count;
}

// --- Main ---

function main() {
  const governance = scanGovernance();
  const protocols = scanProtocols();
  const templates = scanTemplates();
  const workflows = scanWorkflows();
  const agents = scanAgents();
  const objectives = scanObjectives();
  const adrs = scanADRs();
  const docs = scanDocs();
  const baseline = scanBaseline();
  const kbCount = scanKnowledgeBase();
  const lint = scanLintStatus();
  const testCount = scanTestCount();

  // Group docs by operational state
  const stateGroups = {
    IMPLEMENTED: [],
    EXPERIMENTAL: [],
    PROPOSED: [],
    STRATEGIC: [],
    UNLABELED: [],
  };
  for (const d of docs) {
    const key = d.operationalState || "UNLABELED";
    if (stateGroups[key]) stateGroups[key].push(d);
    else stateGroups.UNLABELED.push(d);
  }

  const state = {
    scannedAt: new Date().toISOString(),
    rootPath: ROOT,
    overview: {
      governanceCount: governance.length,
      protocolCount: protocols.length,
      templateCount: templates.length,
      workflowCount: workflows.length,
      agentCount: agents.length,
      objectiveCount: objectives.length,
      adrCount: adrs.length,
      docCount: docs.length,
      stateClassifiedCount: docs.filter((d) => d.operationalState).length,
      knowledgeBaseCount: kbCount,
      testCount,
      lintChecks: lint.checkCount,
      lintExists: lint.exists,
    },
    objectives,
    adrs,
    governance,
    protocols,
    templates,
    workflows,
    agents,
    stateClassification: stateGroups,
    baseline,
  };

  mkdirSync(join(__dirname, "..", "generated"), { recursive: true });
  writeFileSync(OUTPUT, JSON.stringify(state, null, 2), "utf-8");
  console.log(`Scanned ${ROOT}`);
  console.log(`Output: ${OUTPUT}`);
  console.log(`Objectives: ${objectives.length}, ADRs: ${adrs.length}, Docs: ${docs.length}`);
  console.log(`Governance: ${governance.length}, Protocols: ${protocols.length}, Templates: ${templates.length}`);
  console.log(`State-classified docs: ${state.overview.stateClassifiedCount}/${docs.length}`);
}

main();
