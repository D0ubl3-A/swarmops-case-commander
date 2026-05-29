import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OPENAPI = ROOT / "docs" / "openapi.json"
API = ROOT / "prototype" / "swarmops_api.py"


REQUIRED_PATHS = [
    "/health",
    "/api/cases/SO-CASE-001",
    "/api/cases/SO-CASE-001/handoff",
    "/api/cases/SO-CASE-001/approval",
    "/api/cases/SO-CASE-001/evidence",
]


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def main():
    spec = json.loads(OPENAPI.read_text(encoding="utf-8"))
    api = API.read_text(encoding="utf-8")

    require(spec["openapi"].startswith("3."), "OpenAPI version missing")
    require(spec["info"]["title"] == "SwarmOps Case Commander API", "OpenAPI title mismatch")

    implementation_markers = [
        "/health",
        "/api/cases/",
        "/handoff",
        "/approval",
        "/evidence",
    ]

    for path in REQUIRED_PATHS:
        require(path in spec["paths"], f"Missing OpenAPI path: {path}")

    for marker in implementation_markers:
        require(marker in api, f"API implementation missing marker: {marker}")

    decision = spec["components"]["schemas"]["ApprovalDecision"]["properties"]["decision"]["enum"]
    require(decision == ["approved", "rejected", "pending"], "Approval enum mismatch")

    print("swarmops openapi check passed")
    print(f"paths={len(REQUIRED_PATHS)}")


if __name__ == "__main__":
    main()
