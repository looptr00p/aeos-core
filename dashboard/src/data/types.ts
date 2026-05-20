export interface DocEntry {
  file: string;
  path: string;
  title: string | null;
  operationalState?: string | null;
  modified: string | null;
}

export interface ObjectiveEntry extends DocEntry {
  id: string | null;
  status: string | null;
}

export interface ADREntry extends DocEntry {
  id: string | null;
  status: string | null;
}

export interface AgentEntry {
  name: string;
  path: string;
  exists: boolean;
}

export interface BaselineEntry {
  file: string;
  path: string;
  version: string;
  risks: string[] | null;
  modified: string | null;
}

export interface OverviewData {
  governanceCount: number;
  protocolCount: number;
  templateCount: number;
  workflowCount: number;
  agentCount: number;
  objectiveCount: number;
  adrCount: number;
  docCount: number;
  stateClassifiedCount: number;
  knowledgeBaseCount: number;
  testCount: number;
  lintChecks: number;
  lintExists: boolean;
}

export interface StateGroups {
  IMPLEMENTED: DocEntry[];
  EXPERIMENTAL: DocEntry[];
  PROPOSED: DocEntry[];
  STRATEGIC: DocEntry[];
  UNLABELED: DocEntry[];
}

export interface AEOSState {
  scannedAt: string;
  rootPath: string;
  overview: OverviewData;
  objectives: ObjectiveEntry[];
  adrs: ADREntry[];
  governance: DocEntry[];
  protocols: DocEntry[];
  templates: DocEntry[];
  workflows: DocEntry[];
  agents: AgentEntry[];
  stateClassification: StateGroups;
  baseline: BaselineEntry | null;
}
