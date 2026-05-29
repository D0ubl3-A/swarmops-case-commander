import json
import zipfile
from pathlib import Path

from build_submission_bundle import BUNDLE_DIR, FILES, ZIP_PATH, main as build_bundle


REQUIRED_NAMES = {name for name, _ in FILES} | {"manifest.json"}


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def main():
    build_bundle()
    require(ZIP_PATH.exists(), "Bundle zip was not created")
    require(ZIP_PATH.stat().st_size > 0, "Bundle zip is empty")

    with zipfile.ZipFile(ZIP_PATH, "r") as archive:
        names = set(archive.namelist())
        require(REQUIRED_NAMES.issubset(names), f"Bundle missing files: {sorted(REQUIRED_NAMES - names)}")
        manifest = json.loads(archive.read("manifest.json").decode("utf-8"))

    require(manifest["links"]["hosted_submission_page"].startswith("https://"), "Hosted page link missing")
    require("Do not claim full UiPath integration" in manifest["claim_note"], "Claim note missing")

    for name in REQUIRED_NAMES:
        path = BUNDLE_DIR / name
        require(path.exists(), f"Bundle directory missing file: {name}")
        require(path.stat().st_size > 0, f"Bundle file is empty: {name}")

    print("swarmops submission bundle check passed")
    print(f"files={len(REQUIRED_NAMES)}")
    print(ZIP_PATH)


if __name__ == "__main__":
    main()
