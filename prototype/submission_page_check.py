from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PAGE = ROOT / "submission" / "index.html"
CSS = ROOT / "submission" / "submission.css"
METADATA = ROOT / "docs" / "youtube-devpost-metadata.md"

REQUIRED_TEXT = [
    "SwarmOps Case Commander",
    "UiPath AgentHack",
    "Narrated Demo MP4",
    "Presentation Deck PDF",
    "OpenAPI Contract",
    "UiPath Maestro Build Guide",
    "Submission Honesty",
]

REQUIRED_LINKS = [
    "https://github.com/D0ubl3-A/swarmops-case-commander",
    "artifacts/swarmops-case-commander-narrated-demo.mp4",
    "artifacts/swarmops-case-commander-deck.pdf",
    "docs/openapi.json",
    "docs/uipath-maestro-build-guide.md",
]


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def main():
    html = PAGE.read_text(encoding="utf-8")
    css = CSS.read_text(encoding="utf-8")
    metadata = METADATA.read_text(encoding="utf-8")

    for text in REQUIRED_TEXT:
        require(text in html, f"Submission page missing text: {text}")

    for link in REQUIRED_LINKS:
        require(link in html or link in metadata, f"Submission page/metadata missing link: {link}")

    require("grid-template-columns" in css, "Submission CSS missing responsive grid")
    require("YouTube Title" in metadata, "Metadata file missing YouTube title")
    require("Upload Checklist" in metadata, "Metadata file missing upload checklist")

    print("swarmops submission page check passed")
    print(f"links={len(REQUIRED_LINKS)}")


if __name__ == "__main__":
    main()
