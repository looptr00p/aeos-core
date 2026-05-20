import type { AEOSState } from "../data/types";

export function RisksView({ state }: { state: AEOSState }) {
  const baseline = state.baseline;
  const risks = baseline?.risks;

  if (!risks || risks.length === 0) {
    return (
      <div>
        <h2 style={{ fontSize: 18, marginBottom: 20 }}>Risks / Watch Items</h2>
        <p style={{ color: "#8b949e" }}>No explicit risks found in baseline document.</p>
      </div>
    );
  }

  return (
    <div>
      <h2 style={{ fontSize: 18, marginBottom: 8 }}>Risks / Watch Items</h2>
      <p style={{ fontSize: 14, color: "#8b949e", marginBottom: 24 }}>
        Extracted from <code>{baseline.file}</code> — Known Operational Risks section. No risks are inferred or invented.
      </p>

      <div style={{ background: "#161b22", borderRadius: 8, overflow: "hidden" }}>
        {risks.map((risk, i) => (
          <div
            key={i}
            style={{
              padding: "14px 20px",
              borderBottom: i < risks.length - 1 ? "1px solid #21262d" : "none",
              display: "flex",
              gap: 12,
              alignItems: "flex-start",
            }}
          >
            <span
              style={{
                display: "inline-flex",
                alignItems: "center",
                justifyContent: "center",
                width: 24,
                height: 24,
                borderRadius: "50%",
                background: "#d2992222",
                color: "#d29922",
                fontSize: 12,
                fontWeight: 600,
                flexShrink: 0,
              }}
            >
              {i + 1}
            </span>
            <span style={{ fontSize: 14, color: "#c9d1d9", lineHeight: 1.5 }}>{risk}</span>
          </div>
        ))}
      </div>
    </div>
  );
}
