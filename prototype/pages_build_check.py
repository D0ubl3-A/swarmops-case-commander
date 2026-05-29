from pathlib import Path

from build_submission_site import OUT, main as build_site


REQUIRED = [
    "index.html",
    "submission.css",
    ".nojekyll",
    "assets/swarmops-case-commander-narrated-demo.mp4",
    "assets/swarmops-case-commander-deck.pdf",
    "assets/SO-CASE-001-approved-evidence-report.json",
    "assets/openapi.json",
    "assets/uipath-maestro-build-guide.md",
]


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def main():
    build_site()
    for relative in REQUIRED:
        path = OUT / relative
        require(path.exists(), f"Missing built file: {relative}")
        if path.name != ".nojekyll":
            require(path.stat().st_size > 0, f"Built file is empty: {relative}")

    html = (OUT / "index.html").read_text(encoding="utf-8")
    require("SwarmOps Case Commander" in html, "Built page missing project title")
    require("UiPath" in html, "Built page missing UiPath text")

    print("swarmops pages build check passed")
    print(f"files={len(REQUIRED)}")


if __name__ == "__main__":
    main()
