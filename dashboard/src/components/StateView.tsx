import type { AEOSState, DocEntry } from "../data/types";

const STATE_COLORS: Record<string, string> = {
  IMPLEMENTED: "#3fb950",
  EXPERIMENTAL: "#d29922",
  PROPOSED: "#58a6ff",
  STRATEGIC: "#bc8cff",
  UNLABELED: "#8b949e",
};

export function StateView({ state }: { state: AEOSState }) {
  const groups = state.stateClassification;
  const order = ["IMPLEMENTED", "EXPERIMENTAL", "PROPOSED", "STRATEGIC", "UNLABELED"] as const;

  return (
    <div>
      <h2 style={{ fontSize: 18, marginBottom: 20 }}>State Classification</h2>
      <p style={{ fontSize: 14, color: "#8b949e", marginBottom: 24 }}>
        Documents grouped by explicit operational state label. UNLABELED documents have no <code>**Operational State**</code> metadata.
      </p>

      {order.map((key) => {
        const items = groups[key];
        if (!items || items.length === 0) return null;
        return (
          <div key={key} style={{ marginBottom: 28 }}>
            <h3 style={{ fontSize: 15, marginBottom: 12, display: "flex", alignItems: "center", gap: 8 }}>
              <span style={{ display: "inline-block", width: 10, height: 10, borderRadius: "50%", background: STATE_COLORS[key] }} />
              <span style={{ color: STATE_COLORS[key] }}>{key}</span>
              <span style={{ color: "#8b949e", fontWeight: 400, fontSize: 13 }}>({items.length})</span>
            </h3>
            <div style={{ background: "#161b22", borderRadius: 8, overflow: "hidden" }}>
              <table style={{ width: "100%", borderCollapse: "collapse", fontSize: 14 }}>
                <thead>
                  <tr style={{ borderBottom: "1px solid #21262d" }}>
                    <th style={{ textAlign: "left", padding: "10px 16px", color: "#8b949e", fontWeight: 500 }}>File</th>
                    <th style={{ textAlign: "left", padding: "10px 16px", color: "#8b949e", fontWeight: 500 }}>Title</th>
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
                      <td style={{ padding: "8px 16px", color: "#8b949e", fontSize: 13 }}>{item.modified || "—"}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>
        );
      })}
    </div>
  );
}

function DocRow({ item }: { item: DocEntry }) {
  return (
    <tr style={{ borderBottom: "1px solid #21262d" }}>
      <td style={{ padding: "8px 16px" }}>
        <code style={{ fontSize: 13 }}>{item.file}</code>
      </td>
      <td style={{ padding: "8px 16px", color: "#c9d1d9" }}>{item.title || "—"}</td>
      <td style={{ padding: "8px 16px", color: "#8b949e", fontSize: 13 }}>{item.modified || "—"}</td>
    </tr>
  );
}
