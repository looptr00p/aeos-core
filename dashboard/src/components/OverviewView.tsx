import type { AEOSState } from "../data/types";

const STATUS_COLORS: Record<string, string> = {
  ACTIVE: "#3fb950",
  DRAFT: "#8b949e",
  CLOSED: "#6e7681",
  PROPOSED: "#d29922",
};

function statusColor(s: string | null) {
  if (!s) return "#8b949e";
  return STATUS_COLORS[s] || "#8b949e";
}

export function OverviewView({ state }: { state: AEOSState }) {
  const { overview, objectives, adrs, baseline } = state;

  const activeObjectives = objectives.filter((o) => o.status === "ACTIVE");
  const draftObjectives = objectives.filter((o) => o.status === "DRAFT");
  const proposedADRs = adrs.filter((a) => a.status === "PROPOSED");

  return (
    <div>
      <h2 style={{ fontSize: 18, marginBottom: 20 }}>Overview</h2>

      <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fill, minmax(180px, 1fr))", gap: 12, marginBottom: 32 }}>
        <StatCard label="Governance Files" value={overview.governanceCount} />
        <StatCard label="Protocols" value={overview.protocolCount} />
        <StatCard label="Templates" value={overview.templateCount} />
        <StatCard label="Workflows" value={overview.workflowCount} />
        <StatCard label="Agents" value={overview.agentCount} />
        <StatCard label="Objectives" value={overview.objectiveCount} />
        <StatCard label="ADRs" value={overview.adrCount} />
        <StatCard label="Documents" value={overview.docCount} />
        <StatCard label="State-Classified" value={`${overview.stateClassifiedCount}/${overview.docCount}`} />
        <StatCard label="Knowledge Base" value={overview.knowledgeBaseCount} />
        <StatCard label="Tests" value={overview.testCount} />
        <StatCard label="Lint Checks" value={overview.lintExists ? overview.lintChecks : "N/A"} />
      </div>

      <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 24, marginBottom: 32 }}>
        <div style={{ background: "#161b22", borderRadius: 8, padding: 20 }}>
          <h3 style={{ fontSize: 15, marginBottom: 12, color: "#8b949e" }}>Active Objectives</h3>
          {activeObjectives.length === 0 ? (
            <p style={{ color: "#8b949e", fontSize: 14 }}>None</p>
          ) : (
            <ul style={{ listStyle: "none" }}>
              {activeObjectives.map((o) => (
                <li key={o.id} style={{ marginBottom: 8, fontSize: 14 }}>
                  <span style={{ color: statusColor(o.status), fontWeight: 600 }}>{o.id}</span>{" "}
                  <span style={{ color: "#c9d1d9" }}>{o.title || o.file}</span>
                </li>
              ))}
            </ul>
          )}
        </div>

        <div style={{ background: "#161b22", borderRadius: 8, padding: 20 }}>
          <h3 style={{ fontSize: 15, marginBottom: 12, color: "#8b949e" }}>Draft Objectives</h3>
          {draftObjectives.length === 0 ? (
            <p style={{ color: "#8b949e", fontSize: 14 }}>None</p>
          ) : (
            <ul style={{ listStyle: "none" }}>
              {draftObjectives.map((o) => (
                <li key={o.id} style={{ marginBottom: 8, fontSize: 14 }}>
                  <span style={{ color: statusColor(o.status), fontWeight: 600 }}>{o.id}</span>{" "}
                  <span style={{ color: "#c9d1d9" }}>{o.title || o.file}</span>
                </li>
              ))}
            </ul>
          )}
        </div>
      </div>

      <div style={{ background: "#161b22", borderRadius: 8, padding: 20, marginBottom: 24 }}>
        <h3 style={{ fontSize: 15, marginBottom: 12, color: "#8b949e" }}>Proposed ADRs</h3>
        {proposedADRs.length === 0 ? (
          <p style={{ color: "#8b949e", fontSize: 14 }}>None</p>
        ) : (
          <ul style={{ listStyle: "none" }}>
            {proposedADRs.map((a) => (
              <li key={a.id} style={{ marginBottom: 8, fontSize: 14 }}>
                <span style={{ color: "#d29922", fontWeight: 600 }}>{a.id}</span>{" "}
                <span style={{ color: "#c9d1d9" }}>{a.title || a.file}</span>
              </li>
            ))}
          </ul>
        )}
      </div>

      {baseline && (
        <div style={{ background: "#161b22", borderRadius: 8, padding: 20 }}>
          <h3 style={{ fontSize: 15, marginBottom: 8, color: "#8b949e" }}>Governance Baseline</h3>
          <p style={{ fontSize: 14 }}>
            <code>{baseline.file}</code> — Version {baseline.version}
          </p>
          <p style={{ fontSize: 13, color: "#8b949e", marginTop: 4 }}>Last modified: {baseline.modified}</p>
        </div>
      )}
    </div>
  );
}

function StatCard({ label, value }: { label: string; value: string | number }) {
  return (
    <div style={{ background: "#161b22", borderRadius: 8, padding: 16 }}>
      <div style={{ fontSize: 28, fontWeight: 700, color: "#58a6ff" }}>{value}</div>
      <div style={{ fontSize: 13, color: "#8b949e", marginTop: 4 }}>{label}</div>
    </div>
  );
}
