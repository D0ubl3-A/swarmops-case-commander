import json
import subprocess
import sys
import time
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
API = ROOT / "prototype" / "swarmops_api.py"
BASE = "http://127.0.0.1:8791"


def fetch(path, method="GET", payload=None):
    data = None
    headers = {}
    if payload is not None:
        data = json.dumps(payload).encode("utf-8")
        headers["Content-Type"] = "application/json"
    request = Request(f"{BASE}{path}", data=data, headers=headers, method=method)
    with urlopen(request, timeout=5) as response:
        return json.loads(response.read().decode("utf-8"))


def wait_for_health():
    deadline = time.time() + 10
    while time.time() < deadline:
        try:
            payload = fetch("/health")
            if payload["ok"]:
                return
        except Exception:
            time.sleep(0.2)
    raise AssertionError("API did not become healthy")


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def main():
    proc = subprocess.Popen(
        [sys.executable, str(API), "--port", "8791"],
        cwd=str(ROOT),
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    try:
        wait_for_health()
        case = fetch("/api/cases/SO-CASE-001")
        require(case["case_id"] == "SO-CASE-001", "Case endpoint returned wrong case")
        require(len(case["agents"]) == 5, "Case endpoint did not return five agents")

        handoff = fetch("/api/cases/SO-CASE-001/handoff")
        require(handoff["status"] == "pending_human_approval", "Handoff status mismatch")
        require(handoff["evidence_manifest_url"].endswith("/evidence"), "Evidence URL missing from handoff")
        require(len(handoff["agent_outputs"]) == 5, "Handoff did not include all agent outputs")

        field_map = fetch("/api/cases/SO-CASE-001/maestro-field-map")
        require(field_map["case_type"] == "SwarmOps Vendor Onboarding", "Maestro case type mismatch")
        require(len(field_map["stages"]) == 6, "Maestro field map stage count mismatch")
        require(len(field_map["case_fields"]) >= 10, "Maestro field map missing fields")
        require("live UiPath Maestro connection" in field_map["claim_guard"], "Maestro field map claim guard missing")

        approved = fetch("/api/cases/SO-CASE-001/approval", "POST", {"decision": "approved"})
        require(approved["approval_gate"]["status"] == "approved", "Approval endpoint did not approve gate")
        require(approved["final_status"] == "approved_for_handoff", "Approval endpoint final status mismatch")

        try:
            fetch("/api/cases/SO-CASE-001/approval", "POST", {"decision": "unsafe"})
            raise AssertionError("Invalid approval decision should fail")
        except HTTPError as exc:
            require(exc.code == 400, "Invalid approval decision returned wrong status")

        print("swarmops api check passed")
        print("handoff_status=pending_human_approval")
        print("approval_status=approved")
        print(f"maestro_fields={len(field_map['case_fields'])}")
    finally:
        proc.terminate()
        try:
            proc.wait(timeout=5)
        except subprocess.TimeoutExpired:
            proc.kill()


if __name__ == "__main__":
    main()
