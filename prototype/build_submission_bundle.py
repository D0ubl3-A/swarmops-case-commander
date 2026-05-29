import json
import shutil
import zipfile
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BUNDLE_DIR = ROOT / "artifacts" / "submission_bundle"
ZIP_PATH = ROOT / "artifacts" / "swarmops-case-commander-submission-bundle.zip"

FILES = [
    ("README.md", ROOT / "README.md"),
    ("submit-now.md", ROOT / "docs" / "submit-now.md"),
    ("devpost-final-draft.md", ROOT / "docs" / "devpost-final-draft.md"),
    ("youtube-devpost-metadata.md", ROOT / "docs" / "youtube-devpost-metadata.md"),
    ("uipath-maestro-build-guide.md", ROOT / "docs" / "uipath-maestro-build-guide.md"),
    ("openapi.json", ROOT / "docs" / "openapi.json"),
    ("approved-evidence.json", ROOT / "artifacts" / "SO-CASE-001-approved-evidence-report.json"),
    ("deck.pdf", ROOT / "artifacts" / "swarmops-case-commander-deck.pdf"),
    ("narrated-demo.mp4", ROOT / "artifacts" / "swarmops-case-commander-narrated-demo.mp4"),
]

LINKS = {
    "hosted_submission_page": "https://d0ubl3-a.github.io/swarmops-case-commander/",
    "repository": "https://github.com/D0ubl3-A/swarmops-case-commander",
    "release": "https://github.com/D0ubl3-A/swarmops-case-commander/releases/tag/v0.1.0",
}


def copy_files():
    if BUNDLE_DIR.exists():
        shutil.rmtree(BUNDLE_DIR)
    BUNDLE_DIR.mkdir(parents=True)

    manifest_files = []
    for bundle_name, source in FILES:
        if not source.exists():
            raise FileNotFoundError(source)
        destination = BUNDLE_DIR / bundle_name
        shutil.copy2(source, destination)
        manifest_files.append({"name": bundle_name, "bytes": destination.stat().st_size})

    manifest = {
        "name": "SwarmOps Case Commander submission bundle",
        "created_at": datetime.now(timezone.utc).isoformat(),
        "links": LINKS,
        "files": manifest_files,
        "claim_note": "Do not claim full UiPath integration unless Automation Cloud / Maestro footage is recorded.",
    }
    (BUNDLE_DIR / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")


def zip_bundle():
    if ZIP_PATH.exists():
        ZIP_PATH.unlink()
    with zipfile.ZipFile(ZIP_PATH, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(BUNDLE_DIR.iterdir()):
            archive.write(path, path.name)
    print(ZIP_PATH)
    print(f"bytes={ZIP_PATH.stat().st_size}")


def main():
    copy_files()
    zip_bundle()


if __name__ == "__main__":
    main()
