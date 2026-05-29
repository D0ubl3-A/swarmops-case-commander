# SwarmOps Case Commander v0.1.0

This release packages the verified local prototype and submission assets for UiPath AgentHack review.

## Included

- Runnable local command center prototype.
- Local UiPath handoff API.
- OpenAPI contract.
- UiPath Maestro build guide.
- Smoke, interaction, API, OpenAPI, submission page, and Pages build checks.
- Pending and approved evidence JSON.
- Presentation deck PDF.
- Narrated demo MP4.
- Downloadable submission bundle zip.
- Hosted GitHub Pages submission page.
- Standalone submit-now packet.
- Standalone final completion audit.

## Public Links

- Hosted submission page: https://d0ubl3-a.github.io/swarmops-case-commander/
- Repository: https://github.com/D0ubl3-A/swarmops-case-commander
- Narrated demo MP4: https://raw.githubusercontent.com/D0ubl3-A/swarmops-case-commander/main/artifacts/swarmops-case-commander-narrated-demo.mp4
- Deck PDF: https://raw.githubusercontent.com/D0ubl3-A/swarmops-case-commander/main/artifacts/swarmops-case-commander-deck.pdf
- OpenAPI contract: https://raw.githubusercontent.com/D0ubl3-A/swarmops-case-commander/main/docs/openapi.json
- Approved evidence JSON: https://raw.githubusercontent.com/D0ubl3-A/swarmops-case-commander/main/artifacts/SO-CASE-001-approved-evidence-report.json
- Submission bundle zip: https://github.com/D0ubl3-A/swarmops-case-commander/releases/download/v0.1.0/swarmops-case-commander-submission-bundle.zip
- Submit-now packet: https://github.com/D0ubl3-A/swarmops-case-commander/releases/download/v0.1.0/submit-now.md
- Final completion audit: https://github.com/D0ubl3-A/swarmops-case-commander/releases/download/v0.1.0/final-completion-audit.md

## Verification Commands

```powershell
py -3 prototype\smoke_check.py
py -3 prototype\interaction_check.py
py -3 prototype\api_check.py
py -3 prototype\openapi_check.py
py -3 prototype\submission_page_check.py
py -3 prototype\pages_build_check.py
```

## Honest Status

Implemented and verified:

- Local prototype.
- Evidence pipeline.
- Human approval state transition.
- Handoff API.
- OpenAPI contract.
- Submission page and demo artifacts.

Still external before claiming full UiPath integration:

- UiPath Automation Cloud / Maestro Case recording.
- Devpost final submission.
- YouTube upload if Devpost requires an embeddable hosted video.
