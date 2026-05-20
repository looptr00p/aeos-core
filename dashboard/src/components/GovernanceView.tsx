import type { AEOSState, DocEntry } from "../data/types";

const SECTIONS = [
  { key: "governance", label: "Governance Files", color: "#3fb950" },
  { key: "protocols", label: "Protocols", color: "#58a6ff" },
  { key: "templates", label: "Templates", color: "#d29922" },
  { key: "workflows", label: "Workflows", color: "#bc8cff" },
] as const;

export function GovernanceView({ state }: { state: AEOSState }) {
  return (
    <div>
      <h2 style={{ fontSize: 18, marginBottom: 20 }}>Governance Documents</h2>

      {SECTIONS.map(({ key, label, color }) => {
        const items = state[key] as DocEntry[];
        return (
          <div key={key} style={{ marginBottom: 28 }}>
            <h3 style={{ fontSize: 15, marginBottom: 12, display: "flex", alignItems: "center", gap: 8 }}>
              <span style={{ display: "inline-block", width: 10, height: 10, borderRadius: "50%", background: color }} />
              <span style={{ color }}>{label}</span>
              <span style={{ color: "#8b949e", fontWeight: 400, fontSize: 13 }}>({items.length})</span>
            </h3>
            <div style={{ background: "#161b22", borderRadius: 8, overflow: "hidden" }}>
              <table style={{ width: "100%", borderCollapse: "collapse", fontSize: 14 }}>
                <thead>
                  <tr style={{ borderBottom: "1px solid #21262d" }}>
                    <th style={{ textAlign: "left", padding: "10px 16px", color: "#8b949e", fontWeight: 500 }}>File</th>
                    <th style={{ textAlign: "left", padding: "10px 16px", color: "#8b949e", fontWeight: 500 }}>Title</th>
                    <th style={{ textAlign: "left", padding: "10px 16px", color: "#8b949e", fontWeight: 500 }}>State</th>
                    <th style={{ textAlign: "left", padding: "10px 16px", color: "#8b949e", fontWeight: 500 }}>Modified</th>
                  </tr>
                </thead>
                <tbody>
                  {items.map((item) => (
                    <tr key={item.path} style={{ borderBottom: "1px solid #21262d" }}>
                      <td style={{ padding: "8px 16px" }}>
                        <code style={{ fontSize: 13 }}>{item.file}</code>
                      </td>
                      <td style={{ padding: "8px 16px", color: "#c9d1d9" }}>{item.title || "—"}</td>
                      <td style={{ padding: "8px 16px", fontSize: 13, color: "#8b949e" }}>
                        {item.operationalState || "—"}
                      </td>
                      <td style={{ padding: "8px 16px", color: "#8b949e", fontSize: 13 }}>{item.modified || "—"}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>
        );
      })}

      <div style={{ marginBottom: 28 }}>
        <h3 style={{ fontSize: 15, marginBottom: 12, display: "flex", alignItems: "center", gap: 8 }}>
          <span style={{ display: "inline-block", width: 10, height: 10, borderRadius: "50%", background: "#f85149" }} />
          <span style={{ color: "#f85149" }}>Agents</span>
          <span style={{ color: "#8b949e", fontWeight: 400, fontSize: 13 }}>({state.agents.length})</span>
        </h3>
        <div style={{ display: "flex", gap: 8, flexWrap: "wrap" }}>
          {state.agents.map((a) => (
            <span
              key={a.name}
              style={{
                display: "inline-block",
                padding: "6px 14px",
                borderRadius: 8,
                fontSize: 13,
                background: a.exists ? "#3fb95022" : "#f8514922",
                color: a.exists ? "#3fb950" : "#f85149",
                border: `1px solid ${a.exists ? "#3fb95044" : "#f8514944"}`,
              }}
            >
              {a.name}
            </span>
          ))}
        </div>
      </div>
    </div>
  );
}
