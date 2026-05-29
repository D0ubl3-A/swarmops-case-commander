# Repo Readiness

## Current Public-Repo Status

Published:

```text
https://github.com/D0ubl3-A/swarmops-case-commander
```

Recommended repository name:

```text
swarmops-case-commander
```

## Required Files Present

- `README.md`
- `LICENSE`
- `.gitignore`
- `prototype/index.html`
- `prototype/styles.css`
- `prototype/app.js`
- `prototype/smoke_check.py`
- `prototype/interaction_check.py`
- `prototype/generate_evidence.py`
- `prototype/swarmops_api.py`
- `prototype/api_check.py`
- `prototype/openapi_check.py`
- `prototype/submission_page_check.py`
- `prototype/build_submission_site.py`
- `prototype/pages_build_check.py`
- `data/sample-case.json`
- `docs/architecture.md`
- `docs/uipath-integration-contract.md`
- `docs/uipath-maestro-build-guide.md`
- `docs/openapi.json`
- `docs/submission-package.md`
- `docs/devpost-final-draft.md`
- `docs/validation-report.md`
- `docs/deck-outline.md`
- `docs/youtube-devpost-metadata.md`
- `submission/index.html`
- `submission/submission.css`
- `.github/workflows/pages.yml`
- `deck/index.html`
- `deck/slides.css`
- `artifacts/swarmops-case-commander-deck.pdf`
- `artifacts/SO-CASE-001-evidence-report.json`
- `artifacts/SO-CASE-001-approved-evidence-report.json`
- `artifacts/swarmops-case-commander-demo.mp4`
- `artifacts/swarmops-case-commander-narrated-demo.mp4`

## Public Asset Links

- Code: https://github.com/D0ubl3-A/swarmops-case-commander
- Narrated demo video file: https://raw.githubusercontent.com/D0ubl3-A/swarmops-case-commander/main/artifacts/swarmops-case-commander-narrated-demo.mp4
- Presentation deck PDF: https://raw.githubusercontent.com/D0ubl3-A/swarmops-case-commander/main/artifacts/swarmops-case-commander-deck.pdf
- Approved evidence JSON: https://raw.githubusercontent.com/D0ubl3-A/swarmops-case-commander/main/artifacts/SO-CASE-001-approved-evidence-report.json

## Commands

Local repo was initialized and pushed. If recreating from scratch:

```powershell
git init
git add .
git commit -m "Build SwarmOps Case Commander prototype"
```

Create public GitHub repo with GitHub CLI:

```powershell
gh repo create D0ubl3-A/swarmops-case-commander --public --source . --remote origin --push
```

## Pre-Push Checks

```powershell
py -3 prototype\smoke_check.py
py -3 prototype\interaction_check.py
py -3 prototype\generate_evidence.py
py -3 prototype\api_check.py
py -3 prototype\openapi_check.py
py -3 prototype\submission_page_check.py
py -3 prototype\pages_build_check.py
```

## GitHub Pages

GitHub Pages is enabled with GitHub Actions as the source. The hosted submission page is:

```text
https://d0ubl3-a.github.io/swarmops-case-commander/
```

The repo includes `.github/workflows/pages.yml`, which builds `dist/submission-site` from the curated submission page and artifacts.

## Do Not Commit

- UiPath credentials
- browser session exports
- `.env`
- private vendor data
- unlicensed media
- raw screen recordings unless intentionally curated
