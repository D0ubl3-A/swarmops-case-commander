import json
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "sample-case.json"
OUT_DIR = ROOT / "artifacts"
PENDING_OUT = OUT_DIR / "SO-CASE-001-evidence-report.json"
APPROVED_OUT = OUT_DIR / "SO-CASE-001-approved-evidence-report.json"


def build_timeline(case):
    approval = case["approval_queue"][0]
    stages = []
    purchase_index = case["stages"].index("purchase_approval")
    for index, stage in enumerate(case["stages"]):
        status = "done"
        if approval["status"] == "pending" and stage == "purchase_approval":
            status = "blocked"
        elif approval["status"] == "pending" and index > purchase_index:
            status = "pending"
        elif approval["status"] == "rejected" and index >= purchase_index:
            status = "blocked"
        stages.append({"stage": stage, "status": status})
    return stages


def build_report(case):
    approval = case["approval_queue"][0]
    return {
        "case_id": case["case_id"],
        "title": case["title"],
        "final_status": case["final_status"],
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "vendor": case["vendor"],
        "bounded_agents": [
            {
                "agent": agent["name"],
                "evidence_id": agent["evidence_id"],
                "risk": agent["risk"],
                "output": agent["output"],
            }
            for agent in case["agents"]
        ],
        "approval_gate": {
            "id": approval["id"],
            "label": approval["label"],
            "status": approval["status"],
            "risk": approval["risk"],
            "reason": approval["reason"],
        },
        "case_timeline": build_timeline(case),
        "ui_path_mapping": {
            "maestro_case": "Case stages and state transitions",
            "human_task": "Approval gate for vendor setup",
            "robot_or_api_step": "Safe agent outputs and evidence compilation",
            "final_artifact": "Audit-ready evidence JSON",
        },
    }


def main():
    case = json.loads(DATA.read_text(encoding="utf-8"))
    OUT_DIR.mkdir(exist_ok=True)
    PENDING_OUT.write_text(json.dumps(build_report(case), indent=2), encoding="utf-8")

    approved_case = json.loads(json.dumps(case))
    approved_case["approval_queue"][0]["status"] = "approved"
    approved_case["approval_queue"][0]["reason"] = "Human approval captured. Vendor setup may proceed after required artifacts are collected."
    approved_case["final_status"] = "approved_for_handoff"
    APPROVED_OUT.write_text(json.dumps(build_report(approved_case), indent=2), encoding="utf-8")

    print(PENDING_OUT)
    print(APPROVED_OUT)


if __name__ == "__main__":
    main()
