import json
from pathlib import Path

from maestro_field_map import build_maestro_field_map


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "sample-case.json"
OUTPUT = ROOT / "docs" / "maestro-field-map.json"


def main():
    case = json.loads(DATA.read_text(encoding="utf-8"))
    payload = build_maestro_field_map(case)
    OUTPUT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(OUTPUT)
    print(f"fields={len(payload['case_fields'])}")
    print(f"stages={len(payload['stages'])}")
    print(f"api_calls={len(payload['api_calls'])}")


if __name__ == "__main__":
    main()
