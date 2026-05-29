import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "dist" / "submission-site"

FILES = [
    (ROOT / "submission" / "index.html", OUT / "index.html"),
    (ROOT / "submission" / "submission.css", OUT / "submission.css"),
    (ROOT / "artifacts" / "swarmops-case-commander-narrated-demo.mp4", OUT / "assets" / "swarmops-case-commander-narrated-demo.mp4"),
    (ROOT / "artifacts" / "swarmops-case-commander-deck.pdf", OUT / "assets" / "swarmops-case-commander-deck.pdf"),
    (ROOT / "artifacts" / "SO-CASE-001-approved-evidence-report.json", OUT / "assets" / "SO-CASE-001-approved-evidence-report.json"),
    (ROOT / "docs" / "openapi.json", OUT / "assets" / "openapi.json"),
    (ROOT / "docs" / "uipath-maestro-build-guide.md", OUT / "assets" / "uipath-maestro-build-guide.md"),
]


def copy_file(src, dst):
    if not src.exists():
        raise FileNotFoundError(src)
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)


def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    for src, dst in FILES:
        copy_file(src, dst)
    (OUT / ".nojekyll").write_text("", encoding="utf-8")
    print(OUT)
    print(f"files={len(FILES) + 1}")


if __name__ == "__main__":
    main()
