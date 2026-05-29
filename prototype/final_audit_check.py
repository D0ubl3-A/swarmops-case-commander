from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
AUDIT = ROOT / "docs" / "final-completion-audit.md"

REQUIRED_TEXT = [
    "Final Completion Audit",
    "Verified Deliverables",
    "Remaining External Gates",
    "https://d0ubl3-a.github.io/swarmops-case-commander/",
    "https://github.com/D0ubl3-A/swarmops-case-commander/releases/tag/v0.1.0",
    "swarmops-case-commander-submission-bundle.zip",
    "https://github.com/D0ubl3-A/swarmops-case-commander/releases/download/v0.1.0/submit-now.md",
    "https://github.com/D0ubl3-A/swarmops-case-commander/releases/download/v0.1.0/final-completion-audit.md",
    "Fully integrated with UiPath Maestro Case",
    "Final Devpost form submitted",
    "ready to submit with conservative language",
]


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def main():
    text = AUDIT.read_text(encoding="utf-8")
    for item in REQUIRED_TEXT:
        require(item in text, f"Final audit missing: {item}")
    print("swarmops final audit check passed")
    print(f"required_items={len(REQUIRED_TEXT)}")


if __name__ == "__main__":
    main()
