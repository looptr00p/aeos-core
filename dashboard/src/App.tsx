import { useState, useEffect } from "react";
import { OverviewView } from "./components/OverviewView";
import { StateView } from "./components/StateView";
import { ObjectivesView } from "./components/ObjectivesView";
import { ADRView } from "./components/ADRView";
import { GovernanceView } from "./components/GovernanceView";
import { BaselineView } from "./components/BaselineView";
import { RisksView } from "./components/RisksView";
import type { AEOSState } from "./data/types";

const TABS = [
  { id: "overview", label: "Overview" },
  { id: "state", label: "State Classification" },
  { id: "objectives", label: "Objectives" },
  { id: "adrs", label: "ADRs" },
  { id: "governance", label: "Governance" },
  { id: "baseline", label: "Baseline" },
  { id: "risks", label: "Risks" },
] as const;

export default function App() {
  const [state, setState] = useState<AEOSState | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [activeTab, setActiveTab] = useState("overview");

  useEffect(() => {
    fetch("/aeos-state.json")
      .then((r) => {
        if (!r.ok) throw new Error(`Failed to load aeos-state.json (${r.status})`);
        return r.json();
      })
      .then(setState)
      .catch((e) => setError(e.message));
  }, []);

  if (error) {
    return (
      <div style={{ maxWidth: 720, margin: "80px auto", padding: "0 24px" }}>
        <h1 style={{ color: "#f85149" }}>Dashboard Error</h1>
        <p>{error}</p>
        <p style={{ marginTop: 16 }}>
          Run <code>npm run scan</code> in the dashboard directory first.
        </p>
      </div>
    );
  }

  if (!state) {
    return (
      <div style={{ maxWidth: 720, margin: "80px auto", padding: "0 24px" }}>
        <p>Loading AEOS governance state...</p>
      </div>
    );
  }

  return (
    <div>
      <header style={{ borderBottom: "1px solid #21262d", padding: "16px 24px", display: "flex", alignItems: "center", justifyContent: "space-between" }}>
        <div>
          <h1 style={{ fontSize: 20, fontWeight: 600 }}>AEOS Governance Dashboard</h1>
          <p style={{ fontSize: 13, color: "#8b949e" }}>Read-only observability layer — repository markdown is the source of truth</p>
        </div>
        <div style={{ fontSize: 12, color: "#8b949e" }}>
          Scanned: {state.scannedAt?.split("T")[0] || "unknown"}
        </div>
      </header>

      <nav style={{ borderBottom: "1px solid #21262d", padding: "0 24px", display: "flex", gap: 0, overflowX: "auto" }}>
        {TABS.map((tab) => (
          <button
            key={tab.id}
            onClick={() => setActiveTab(tab.id)}
            style={{
              padding: "12px 16px",
              background: "none",
              border: "none",
              borderBottom: activeTab === tab.id ? "2px solid #58a6ff" : "2px solid transparent",
              color: activeTab === tab.id ? "#e1e4e8" : "#8b949e",
              cursor: "pointer",
              fontSize: 14,
              fontWeight: activeTab === tab.id ? 600 : 400,
              whiteSpace: "nowrap",
            }}
          >
            {tab.label}
          </button>
        ))}
      </nav>

      <main style={{ padding: "24px", maxWidth: 1100, margin: "0 auto" }}>
        {activeTab === "overview" && <OverviewView state={state} />}
        {activeTab === "state" && <StateView state={state} />}
        {activeTab === "objectives" && <ObjectivesView state={state} />}
        {activeTab === "adrs" && <ADRView state={state} />}
        {activeTab === "governance" && <GovernanceView state={state} />}
        {activeTab === "baseline" && <BaselineView state={state} />}
        {activeTab === "risks" && <RisksView state={state} />}
      </main>
    </div>
  );
}
