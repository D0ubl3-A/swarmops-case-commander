from html.parser import HTMLParser
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROTOTYPE = ROOT / "prototype"
DATA = ROOT / "data" / "sample-case.json"


def require(condition, message):
    if not condition:
        raise AssertionError(message)


class Parser(HTMLParser):
    pass


def main():
    html = (PROTOTYPE / "index.html").read_text(encoding="utf-8")
    css = (PROTOTYPE / "styles.css").read_text(encoding="utf-8")
    js = (PROTOTYPE / "app.js").read_text(encoding="utf-8")
    data = json.loads(DATA.read_text(encoding="utf-8"))

    Parser().feed(html)
    require("SwarmOps Case Commander" in html, "HTML title missing")
    require("stageList" in html and "approvalQueue" in html and "evidenceReport" in html, "Required UI anchors missing")
    require("setApproval" in js and "exportReport" in js and "buildEvidenceReport" in js, "Required state actions missing")
    require("fetch(\"../data/sample-case.json\")" in js, "Seeded case fetch missing")
    require("command-grid" in css and "evidence-report" in css, "Core layout CSS missing")
    require(len(data["agents"]) >= 5, "Expected at least five agent outputs")
    require(data["approval_queue"][0]["status"] == "pending", "Expected pending approval gate")
    require(data["final_status"] == "pending_human_approval", "Expected pending final status")

    print("swarmops smoke check passed")
    print(f"agents={len(data['agents'])}")
    print(f"approval={data['approval_queue'][0]['status']}")
    print(f"case_id={data['case_id']}")


if __name__ == "__main__":
    main()
