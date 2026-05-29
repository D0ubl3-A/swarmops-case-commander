import json


CASE_TYPE = "SwarmOps Vendor Onboarding"
API_BASE_URL = "http://127.0.0.1:8791"

BLOCKED_ACTIONS = [
    "approve vendor record",
    "accept compliance risk",
    "create purchase order",
    "send external vendor email",
    "finalize case",
]

ALLOWED_AUTOMATION = [
    "parse request",
    "classify urgency",
    "identify missing fields",
    "draft approval memo",
    "compile audit trail",
]


def titleize(value):
    return " ".join(part.capitalize() for part in value.split("_"))


def compact_json(value):
    return json.dumps(value, separators=(",", ":"), sort_keys=True)


def risk_flags(case):
    return [
        {
            "level": agent["risk"],
            "evidence_id": agent["evidence_id"],
            "reason": agent["output"],
        }
        for agent in case["agents"]
        if agent["risk"] in {"medium", "high"}
    ]


def agent_outputs(case):
    return [
        {
            "agent": agent["name"],
            "evidence_id": agent["evidence_id"],
            "risk": agent["risk"],
            "output": agent["output"],
        }
        for agent in case["agents"]
    ]


def field(name, field_type, value, source, uipath_use, required=True):
    return {
        "name": name,
        "type": field_type,
        "required": required,
        "value": value,
        "source": source,
        "uipath_use": uipath_use,
    }


def build_maestro_field_map(case):
    case_id = case["case_id"]
    approval = case["approval_queue"][0]
    handoff_path = f"/api/cases/{case_id}/handoff"
    evidence_path = f"/api/cases/{case_id}/evidence"
    approval_path = f"/api/cases/{case_id}/approval"
    flags = risk_flags(case)
    outputs = agent_outputs(case)

    return {
        "case_type": CASE_TYPE,
        "case_id": case_id,
        "source_case_file": "data/sample-case.json",
        "api_base_url": API_BASE_URL,
        "stages": [
            {
                "order": index + 1,
                "key": stage,
                "label": titleize(stage),
                "source": "data/sample-case.json:stages",
            }
            for index, stage in enumerate(case["stages"])
        ],
        "case_fields": [
            field("case_id", "Text", case_id, f"GET /api/cases/{case_id}", "Primary case identifier"),
            field("vendor_name", "Text", case["vendor"]["name"], f"GET /api/cases/{case_id}", "Case title and vendor search key"),
            field(
                "requested_purchase_amount",
                "Number",
                case["vendor"]["requested_purchase_amount"],
                f"GET /api/cases/{case_id}",
                "Approval threshold and routing input",
            ),
            field("urgency", "Text", case["vendor"]["urgency"], f"GET /api/cases/{case_id}", "Case priority"),
            field("final_status", "Text", case["final_status"], handoff_path, "Case state"),
            field(
                "missing_fields_json",
                "JSON/Text",
                compact_json(case["vendor"]["missing_fields"]),
                f"GET /api/cases/{case_id}",
                "Reviewer checklist",
            ),
            field("risk_flags_json", "JSON/Text", compact_json(flags), handoff_path, "Compliance and approval routing"),
            field("agent_outputs_json", "JSON/Text", compact_json(outputs), handoff_path, "Agent work summary"),
            field(
                "approval_required_json",
                "JSON/Text",
                compact_json(approval),
                handoff_path,
                "Human task payload",
            ),
            field("evidence_manifest_url", "Text", evidence_path, handoff_path, "Final audit artifact location"),
        ],
        "api_calls": [
            {
                "name": "health_check",
                "method": "GET",
                "path": "/health",
                "stage": "intake",
                "purpose": "Confirm the SwarmOps handoff API is reachable before case creation.",
                "expected_status": 200,
            },
            {
                "name": "load_case",
                "method": "GET",
                "path": f"/api/cases/{case_id}",
                "stage": "intake",
                "purpose": "Load seeded vendor, request, stages, agents, and pending approval state.",
                "expected_status": 200,
            },
            {
                "name": "load_handoff",
                "method": "GET",
                "path": handoff_path,
                "stage": "vendor_data_review",
                "purpose": "Populate risk, agent output, and approval fields in Maestro Case.",
                "expected_status": 200,
            },
            {
                "name": "record_human_decision",
                "method": "POST",
                "path": approval_path,
                "stage": "purchase_approval",
                "purpose": "Record approved, rejected, or pending reviewer decision.",
                "request_example": {"decision": "approved"},
                "expected_status": 200,
            },
            {
                "name": "load_evidence",
                "method": "GET",
                "path": evidence_path,
                "stage": "final_audit",
                "purpose": "Attach or display the audit-ready evidence report.",
                "expected_status": 200,
            },
        ],
        "human_tasks": [
            {
                "id": approval["id"],
                "stage": "purchase_approval",
                "label": approval["label"],
                "status": approval["status"],
                "risk": approval["risk"],
                "reviewer_instruction": approval["reason"],
                "blocked_actions": BLOCKED_ACTIONS,
                "allowed_automation": ALLOWED_AUTOMATION,
            }
        ],
        "acceptance_checks": [
            "Six Maestro stages are visible in order.",
            "Case fields match data/sample-case.json and the handoff endpoint.",
            "Human approval task uses the APP-001 label.",
            "Approval callback returns final_status approved_for_handoff for an approved decision.",
            "Evidence JSON is attached, displayed, or linked in Final Audit.",
        ],
        "claim_guard": "This is a verified local handoff package. Do not claim a live UiPath Maestro connection until Automation Cloud footage exists.",
    }
