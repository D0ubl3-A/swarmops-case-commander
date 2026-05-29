from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "docs" / "submit-now.md"

REQUIRED = [
    "SwarmOps Case Commander",
    "https://d0ubl3-a.github.io/swarmops-case-commander/",
    "https://github.com/D0ubl3-A/swarmops-case-commander",
    "https://github.com/D0ubl3-A/swarmops-case-commander/releases/tag/v0.1.0",
    "https://github.com/D0ubl3-A/swarmops-case-commander/releases/download/v0.1.0/swarmops-case-commander-submission-bundle.zip",
    "https://github.com/D0ubl3-A/swarmops-case-commander/releases/download/v0.1.0/final-completion-audit.md",
    "swarmops-case-commander-narrated-demo.mp4",
    "swarmops-case-commander-deck.pdf",
    "openapi.json",
    "SO-CASE-001-approved-evidence-report.json",
    "Do not claim unless proven with UiPath footage",
]


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def main():
    text = PACKET.read_text(encoding="utf-8")
    for item in REQUIRED:
        require(item in text, f"Submit packet missing: {item}")
    print("swarmops submit packet check passed")
    print(f"required_items={len(REQUIRED)}")


if __name__ == "__main__":
    main()
