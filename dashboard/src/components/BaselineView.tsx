import type { AEOSState } from "../data/types";

export function BaselineView({ state }: { state: AEOSState }) {
  const baseline = state.baseline;

  if (!baseline) {
    return (
      <div>
        <h2 style={{ fontSize: 18, marginBottom: 20 }}>Governance Baseline</h2>
        <p style={{ color: "#8b949e" }}>No baseline document found in repository.</p>
      </div>
    );
  }

  return (
    <div>
      <h2 style={{ fontSize: 18, marginBottom: 20 }}>Governance Baseline</h2>

      <div style={{ background: "#161b22", borderRadius: 8, padding: 24, marginBottom: 24 }}>
        <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 16 }}>
          <div>
            <div style={{ fontSize: 13, color: "#8b949e", marginBottom: 4 }}>File</div>
            <code>{baseline.file}</code>
          </div>
          <div>
            <div style={{ fontSize: 13, color: "#8b949e", marginBottom: 4 }}>Version</div>
            <span style={{ fontSize: 16, fontWeight: 600 }}>{baseline.version}</span>
          </div>
          <div>
            <div style={{ fontSize: 13, color: "#8b949e", marginBottom: 4 }}>Path</div>
            <code style={{ fontSize: 13 }}>{baseline.path}</code>
          </div>
          <div>
            <div style={{ fontSize: 13, color: "#8b949e", marginBottom: 4 }}>Last Modified</div>
            <span>{baseline.modified || "—"}</span>
          </div>
        </div>
      </div>

      <div style={{ background: "#161b22", borderRadius: 8, padding: 24, marginBottom: 24 }}>
        <h3 style={{ fontSize: 15, marginBottom: 12, color: "#8b949e" }}>Recommended Git Tag</h3>
        <code>aeos-v0.3-governance-baseline</code>
      </div>

      {baseline.risks && baseline.risks.length > 0 && (
        <div style={{ background: "#161b22", borderRadius: 8, padding: 24 }}>
          <h3 style={{ fontSize: 15, marginBottom: 12, color: "#8b949e" }}>Baseline Snapshot Metrics</h3>
          <p style={{ fontSize: 14, color: "#c9d1d9" }}>
            {baseline.risks.length} operational risks documented in baseline.
          </p>
          <ul style={{ listStyle: "none", marginTop: 12 }}>
            {baseline.risks.map((risk, i) => (
              <li key={i} style={{ fontSize: 14, padding: "6px 0", borderBottom: "1px solid #21262d", color: "#c9d1d9" }}>
                {risk}
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}
