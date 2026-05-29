const fallbackCase = {
  case_id: "SO-CASE-001",
  title: "Northstar Components vendor onboarding",
  request: "Onboard Northstar Components as a new vendor for a $48,500 rush purchase. Validate risk, prepare approval, and create the procurement handoff.",
  vendor: {
    name: "Northstar Components",
    category: "manufacturing supplier",
    requested_purchase_amount: 48500,
    urgency: "rush",
    missing_fields: ["W-9", "bank verification letter", "sanctions screening confirmation"],
  },
  stages: ["intake", "vendor_data_review", "compliance_check", "purchase_approval", "fulfillment_handoff", "final_audit"],
  agents: [
    {
      name: "Intake Agent",
      output: "Request classified as rush vendor onboarding with purchase approval required.",
      risk: "low",
      evidence_id: "EV-001",
    },
    {
      name: "Vendor Data Agent",
      output: "Vendor record is incomplete. Three required onboarding artifacts are missing.",
      risk: "medium",
      evidence_id: "EV-002",
    },
    {
      name: "Compliance Agent",
      output: "Purchase exceeds standard low-risk threshold and requires approval before vendor setup.",
      risk: "high",
      evidence_id: "EV-003",
    },
    {
      name: "Approval Summary Agent",
      output: "Drafted approval memo with amount, urgency, missing artifacts, and policy gate.",
      risk: "medium",
      evidence_id: "EV-004",
    },
    {
      name: "Evidence Agent",
      output: "Compiled case timeline, risk flags, blocked actions, and approval requirements.",
      risk: "low",
      evidence_id: "EV-005",
    },
  ],
  approval_queue: [
    {
      id: "APP-001",
      label: "Approve vendor setup after missing artifacts are collected",
      status: "pending",
      risk: "high",
      reason: "Vendor setup and purchase handoff are state-changing business actions.",
    },
  ],
  final_status: "pending_human_approval",
};

const cloneCase = (value) => JSON.parse(JSON.stringify(value));

let caseState = cloneCase(fallbackCase);

const formatStage = (stage) =>
  stage
    .split("_")
    .map((part) => part.charAt(0).toUpperCase() + part.slice(1))
    .join(" ");

const getApproval = () => caseState.approval_queue[0];

const buildTimeline = () => {
  const approval = getApproval();
  const blockedStage = approval.status === "pending" ? "purchase_approval" : null;
  return caseState.stages.map((stage, index) => {
    let status = "done";
    if (stage === blockedStage) status = "blocked";
    if (index > caseState.stages.indexOf("purchase_approval") && approval.status === "pending") status = "pending";
    if (approval.status === "rejected" && index >= caseState.stages.indexOf("purchase_approval")) status = "blocked";
    return { stage, status };
  });
};

const buildEvidenceReport = () => {
  const approval = getApproval();
  const timeline = buildTimeline();
  const report = {
    case_id: caseState.case_id,
    title: caseState.title,
    final_status: caseState.final_status,
    generated_at: new Date().toISOString(),
    vendor: caseState.vendor,
    bounded_agents: caseState.agents.map((agent) => ({
      agent: agent.name,
      evidence_id: agent.evidence_id,
      risk: agent.risk,
      output: agent.output,
    })),
    approval_gate: {
      id: approval.id,
      label: approval.label,
      status: approval.status,
      risk: approval.risk,
      reason: approval.reason,
    },
    case_timeline: timeline,
    ui_path_mapping: {
      maestro_case: "Case stages and state transitions",
      human_task: "Approval gate for vendor setup",
      robot_or_api_step: "Safe agent outputs and evidence compilation",
      final_artifact: "Audit-ready evidence JSON",
    },
  };
  return JSON.stringify(report, null, 2);
};

const setText = (id, value) => {
  document.getElementById(id).textContent = value;
};

const renderStages = () => {
  const stageList = document.getElementById("stageList");
  stageList.innerHTML = "";
  buildTimeline().forEach((item, index) => {
    const row = document.createElement("div");
    row.className = "stage-item";
    row.innerHTML = `
      <span class="stage-index">${String(index + 1).padStart(2, "0")}</span>
      <span class="stage-name">${formatStage(item.stage)}</span>
      <span class="stage-status ${item.status}">${item.status}</span>
    `;
    stageList.appendChild(row);
  });
};

const renderAgents = () => {
  const agentList = document.getElementById("agentList");
  agentList.innerHTML = "";
  caseState.agents.forEach((agent) => {
    const item = document.createElement("article");
    item.className = "agent-item";
    item.innerHTML = `
      <div class="agent-meta">
        <span class="agent-name">${agent.name}</span>
        <span class="risk-pill ${agent.risk}">${agent.risk}</span>
      </div>
      <p>${agent.output}</p>
      <span class="evidence-id">${agent.evidence_id}</span>
    `;
    agentList.appendChild(item);
  });
};

const renderApproval = () => {
  const approval = getApproval();
  const approvalQueue = document.getElementById("approvalQueue");
  approvalQueue.innerHTML = "";
  const item = document.createElement("article");
  item.className = "approval-item";
  const isClosed = approval.status !== "pending";
  item.innerHTML = `
    <div class="approval-title">
      <strong>${approval.label}</strong>
      <span class="risk-pill ${approval.risk}">${approval.risk}</span>
    </div>
    <p>${approval.reason}</p>
    <div class="approval-actions">
      <button class="action-button approve" type="button" data-action="approved" ${isClosed ? "disabled" : ""}>Approve</button>
      <button class="action-button reject" type="button" data-action="rejected" ${isClosed ? "disabled" : ""}>Reject</button>
    </div>
  `;
  approvalQueue.appendChild(item);
};

const renderReport = () => {
  const approval = getApproval();
  const evidenceReport = document.getElementById("evidenceReport");
  evidenceReport.textContent = buildEvidenceReport();
  setText("approvalState", approval.status);
  setText("reportState", caseState.final_status === "approved_for_handoff" ? "Ready" : "Draft");
  setText("caseStatus", caseState.final_status.replaceAll("_", " "));
  setText("blockedCount", approval.status === "pending" ? "1" : "0");
};

const render = () => {
  setText("caseId", caseState.case_id);
  setText("caseTitle", caseState.title);
  setText("mainTitle", caseState.title);
  setText("requestText", caseState.request);
  setText("agentCount", String(caseState.agents.length));
  setText("evidenceCount", String(caseState.agents.length));
  setText("stageSummary", `${caseState.stages.length} stages`);
  renderStages();
  renderAgents();
  renderApproval();
  renderReport();
};

const setApproval = (status) => {
  const approval = getApproval();
  approval.status = status;
  if (status === "approved") {
    caseState.final_status = "approved_for_handoff";
    approval.reason = "Human approval captured. Vendor setup may proceed after required artifacts are collected.";
  } else {
    caseState.final_status = "rejected_for_remediation";
    approval.reason = "Human reviewer rejected vendor setup until missing artifacts and risk checks are resolved.";
  }
  render();
};

const exportReport = () => {
  const blob = new Blob([buildEvidenceReport()], { type: "application/json" });
  const url = URL.createObjectURL(blob);
  const link = document.createElement("a");
  link.href = url;
  link.download = `${caseState.case_id.toLowerCase()}-evidence-report.json`;
  link.click();
  URL.revokeObjectURL(url);
};

const resetCase = () => {
  caseState = cloneCase(fallbackCase);
  render();
};

document.addEventListener("click", (event) => {
  const actionButton = event.target.closest("[data-action]");
  if (actionButton) {
    setApproval(actionButton.dataset.action);
  }
});

document.getElementById("exportButton").addEventListener("click", exportReport);
document.getElementById("resetButton").addEventListener("click", resetCase);

fetch("../data/sample-case.json")
  .then((response) => {
    if (!response.ok) throw new Error("Case data unavailable");
    return response.json();
  })
  .then((data) => {
    caseState = data;
    render();
  })
  .catch(() => {
    render();
  });
