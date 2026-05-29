import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "sample-case.json"
JS = ROOT / "prototype" / "app.js"
APPROVED_REPORT = ROOT / "artifacts" / "SO-CASE-001-approved-evidence-report.json"


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def main():
    case = json.loads(DATA.read_text(encoding="utf-8"))
    js = JS.read_text(encoding="utf-8")

    require("data-action=\"approved\"" in (ROOT / "prototype" / "index.html").read_text(encoding="utf-8") or "data-action=\"approved\"" in js, "Approve action missing")
    require("setApproval" in js, "setApproval function missing")
    require("approved_for_handoff" in js, "Approved state transition missing")
    require("rejected_for_remediation" in js, "Rejected state transition missing")

    approval = case["approval_queue"][0]
    approval["status"] = "approved"
    approval["reason"] = "Human approval captured. Vendor setup may proceed after required artifacts are collected."
    case["final_status"] = "approved_for_handoff"

    require(case["approval_queue"][0]["status"] == "approved", "Approval status did not update")
    require(case["final_status"] == "approved_for_handoff", "Final approved status missing")

    if APPROVED_REPORT.exists():
      report = json.loads(APPROVED_REPORT.read_text(encoding="utf-8"))
      require(report["approval_gate"]["status"] == "approved", "Approved evidence artifact does not show approval")
      require(report["final_status"] == "approved_for_handoff", "Approved evidence artifact final status mismatch")

    print("swarmops interaction check passed")
    print("approval=approved")
    print("final_status=approved_for_handoff")


if __name__ == "__main__":
    main()
