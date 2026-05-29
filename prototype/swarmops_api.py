import argparse
import json
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse

from generate_evidence import build_report


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "sample-case.json"


def load_case():
    return json.loads(DATA.read_text(encoding="utf-8"))


def clone_case(case):
    return json.loads(json.dumps(case))


def apply_decision(case, decision):
    updated = clone_case(case)
    approval = updated["approval_queue"][0]
    if decision == "approved":
        approval["status"] = "approved"
        approval["reason"] = "Human approval captured. Vendor setup may proceed after required artifacts are collected."
        updated["final_status"] = "approved_for_handoff"
    elif decision == "rejected":
        approval["status"] = "rejected"
        approval["reason"] = "Human reviewer rejected the handoff. Case requires remediation before vendor setup."
        updated["final_status"] = "rejected_for_remediation"
    elif decision == "pending":
        approval["status"] = "pending"
        updated["final_status"] = "pending_human_approval"
    else:
        raise ValueError("decision must be approved, rejected, or pending")
    return updated


def uipath_handoff(case):
    approval = case["approval_queue"][0]
    return {
        "case_id": case["case_id"],
        "status": case["final_status"],
        "stage": "vendor_data_review",
        "risk_flags": [
            {
                "level": agent["risk"],
                "evidence_id": agent["evidence_id"],
                "reason": agent["output"],
            }
            for agent in case["agents"]
            if agent["risk"] in {"medium", "high"}
        ],
        "agent_outputs": [
            {
                "agent": agent["name"],
                "evidence_id": agent["evidence_id"],
                "risk": agent["risk"],
                "output": agent["output"],
            }
            for agent in case["agents"]
        ],
        "approval_required": [
            {
                "id": approval["id"],
                "label": approval["label"],
                "risk": approval["risk"],
                "status": approval["status"],
            }
        ],
        "evidence_manifest_url": f"/api/cases/{case['case_id']}/evidence",
    }


class SwarmOpsHandler(BaseHTTPRequestHandler):
    server_version = "SwarmOpsAPI/1.0"

    def do_GET(self):
        path = urlparse(self.path).path
        case = load_case()
        if path == "/health":
            self.send_json({"ok": True, "service": "swarmops-case-commander"})
        elif path == f"/api/cases/{case['case_id']}":
            self.send_json(case)
        elif path == f"/api/cases/{case['case_id']}/handoff":
            self.send_json(uipath_handoff(case))
        elif path == f"/api/cases/{case['case_id']}/evidence":
            self.send_json(build_report(case))
        else:
            self.send_json({"error": "not_found", "path": path}, HTTPStatus.NOT_FOUND)

    def do_POST(self):
        path = urlparse(self.path).path
        case = load_case()
        if path != f"/api/cases/{case['case_id']}/approval":
            self.send_json({"error": "not_found", "path": path}, HTTPStatus.NOT_FOUND)
            return

        try:
            length = int(self.headers.get("Content-Length", "0"))
            payload = json.loads(self.rfile.read(length).decode("utf-8") or "{}")
            updated = apply_decision(case, payload.get("decision", ""))
        except (json.JSONDecodeError, ValueError) as exc:
            self.send_json({"error": "invalid_request", "message": str(exc)}, HTTPStatus.BAD_REQUEST)
            return

        self.send_json(build_report(updated))

    def log_message(self, format, *args):
        return

    def send_json(self, payload, status=HTTPStatus.OK):
        body = json.dumps(payload, indent=2).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(body)


def run(host, port):
    server = ThreadingHTTPServer((host, port), SwarmOpsHandler)
    print(f"SwarmOps API listening on http://{host}:{port}")
    server.serve_forever()


def main():
    parser = argparse.ArgumentParser(description="Run the SwarmOps UiPath handoff API.")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", default=8791, type=int)
    args = parser.parse_args()
    run(args.host, args.port)


if __name__ == "__main__":
    main()
