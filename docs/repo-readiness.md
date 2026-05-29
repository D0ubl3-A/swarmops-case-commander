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
- `data/sample-case.json`
- `docs/architecture.md`
- `docs/uipath-integration-contract.md`
- `docs/submission-package.md`
- `docs/validation-report.md`
- `docs/deck-outline.md`
- `deck/index.html`
- `deck/slides.css`
- `artifacts/swarmops-case-commander-deck.pdf`
- `artifacts/SO-CASE-001-evidence-report.json`
- `artifacts/SO-CASE-001-approved-evidence-report.json`

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
```

## Do Not Commit

- UiPath credentials
- browser session exports
- `.env`
- private vendor data
- unlicensed media
- raw screen recordings unless intentionally curated
