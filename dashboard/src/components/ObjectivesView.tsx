import type { AEOSState } from "../data/types";

const STATUS_COLORS: Record<string, string> = {
  ACTIVE: "#3fb950",
  DRAFT: "#8b949e",
  CLOSED: "#6e7681",
  COMPLETE: "#3fb950",
};

export function ObjectivesView({ state }: { state: AEOSState }) {
  const objectives = state.objectives;

  return (
    <div>
      <h2 style={{ fontSize: 18, marginBottom: 20 }}>Objectives</h2>
      <div style={{ background: "#161b22", borderRadius: 8, overflow: "hidden" }}>
        <table style={{ width: "100%", borderCollapse: "collapse", fontSize: 14 }}>
          <thead>
            <tr style={{ borderBottom: "1px solid #21262d" }}>
              <th style={{ textAlign: "left", padding: "10px 16px", color: "#8b949e", fontWeight: 500 }}>ID</th>
              <th style={{ textAlign: "left", padding: "10px 16px", color: "#8b949e", fontWeight: 500 }}>Title</th>
              <th style={{ textAlign: "left", padding: "10px 16px", color: "#8b949e", fontWeight: 500 }}>Status</th>
              <th style={{ textAlign: "left", padding: "10px 16px", color: "#8b949e", fontWeight: 500 }}>State</th>
              <th style={{ textAlign: "left", padding: "10px 16px", color: "#8b949e", fontWeight: 500 }}>Modified</th>
            </tr>
          </thead>
          <tbody>
            {objectives.map((o) => (
              <tr key={o.id || o.file} style={{ borderBottom: "1px solid #21262d" }}>
                <td style={{ padding: "8px 16px" }}>
                  <code style={{ fontSize: 13, color: "#58a6ff" }}>{o.id || o.file}</code>
                </td>
                <td style={{ padding: "8px 16px", color: "#c9d1d9" }}>{o.title || "—"}</td>
                <td style={{ padding: "8px 16px" }}>
                  <StatusBadge status={o.status} />
                </td>
                <td style={{ padding: "8px 16px", fontSize: 13, color: "#8b949e" }}>
                  {o.operationalState || "—"}
                </td>
                <td style={{ padding: "8px 16px", color: "#8b949e", fontSize: 13 }}>{o.modified || "—"}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

function StatusBadge({ status }: { status: string | null }) {
  if (!status) return <span style={{ color: "#8b949e" }}>—</span>;
  const color = STATUS_COLORS[status] || "#8b949e";
  return (
    <span style={{ display: "inline-block", padding: "2px 10px", borderRadius: 12, fontSize: 12, fontWeight: 600, background: `${color}22`, color }}>
      {status}
    </span>
  );
}
