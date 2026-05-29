import json
from pathlib import Path

from maestro_field_map import build_maestro_field_map


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "sample-case.json"
DOC = ROOT / "docs" / "maestro-field-map.json"
OPENAPI = ROOT / "docs" / "openapi.json"


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def main():
    case = json.loads(DATA.read_text(encoding="utf-8"))
    expected = build_maestro_field_map(case)
    stored = json.loads(DOC.read_text(encoding="utf-8"))
    spec = json.loads(OPENAPI.read_text(encoding="utf-8"))

    require(stored == expected, "Maestro field map is stale; run generate_maestro_field_map.py")
    require(stored["case_id"] == case["case_id"], "Case id mismatch")
    require(len(stored["stages"]) == len(case["stages"]), "Stage count mismatch")
    require(stored["human_tasks"][0]["label"] == case["approval_queue"][0]["label"], "Human task label mismatch")
    require("live UiPath Maestro connection" in stored["claim_guard"], "Claim guard missing")

    openapi_paths = set(spec["paths"])
    for api_call in stored["api_calls"]:
        require(api_call["path"] in openapi_paths, f"API call missing from OpenAPI: {api_call['path']}")

    field_names = {item["name"] for item in stored["case_fields"]}
    for required in {"case_id", "vendor_name", "risk_flags_json", "approval_required_json", "evidence_manifest_url"}:
        require(required in field_names, f"Required field missing: {required}")

    print("swarmops maestro field map check passed")
    print(f"fields={len(stored['case_fields'])}")
    print(f"stages={len(stored['stages'])}")
    print(f"api_calls={len(stored['api_calls'])}")


if __name__ == "__main__":
    main()
