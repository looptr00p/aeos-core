import type { AEOSState } from "../data/types";

export function ADRView({ state }: { state: AEOSState }) {
  const adrs = state.adrs;

  return (
    <div>
      <h2 style={{ fontSize: 18, marginBottom: 20 }}>Architecture Decision Records</h2>
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
            {adrs.map((a) => (
              <tr key={a.id || a.file} style={{ borderBottom: "1px solid #21262d" }}>
                <td style={{ padding: "8px 16px" }}>
                  <code style={{ fontSize: 13, color: "#58a6ff" }}>{a.id || a.file}</code>
                </td>
                <td style={{ padding: "8px 16px", color: "#c9d1d9" }}>{a.title || "—"}</td>
                <td style={{ padding: "8px 16px" }}>
                  <span style={{ display: "inline-block", padding: "2px 10px", borderRadius: 12, fontSize: 12, fontWeight: 600, background: "#d2992222", color: "#d29922" }}>
                    {a.status || "—"}
                  </span>
                </td>
                <td style={{ padding: "8px 16px", fontSize: 13, color: "#8b949e" }}>
                  {a.operationalState || "—"}
                </td>
                <td style={{ padding: "8px 16px", color: "#8b949e", fontSize: 13 }}>{a.modified || "—"}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}
