# Validation Report

Date: 2026-05-28

## Checks Run

```powershell
py -3 C:\Users\aaron\.barz\apps\swarmops_case_commander\prototype\smoke_check.py
```

Result:

```text
swarmops smoke check passed
agents=5
approval=pending
case_id=SO-CASE-001
```

Server check:

```powershell
Invoke-WebRequest -Uri 'http://127.0.0.1:8788/prototype/index.html' -UseBasicParsing
Invoke-RestMethod -Uri 'http://127.0.0.1:8788/data/sample-case.json'
```

Observed:

```json
{
  "HtmlStatus": 200,
  "HtmlHasApp": true,
  "CaseId": "SO-CASE-001",
  "AgentCount": 5,
  "ApprovalStatus": "pending"
}
```

Headless browser screenshot:

```text
C:\Users\aaron\.barz\artifacts\swarmops-case-commander-screenshot.png
```

Deck render screenshot:

```text
C:\Users\aaron\.barz\artifacts\swarmops-deck-screenshot.png
```

Deck PDF:

```text
C:\Users\aaron\.barz\apps\swarmops_case_commander\artifacts\swarmops-case-commander-deck.pdf
```

Public GitHub repo verification:

```text
https://github.com/D0ubl3-A/swarmops-case-commander
visibility: public
default_branch: main
latest_commit: see current GitHub main branch
```

Local proof demo video:

```powershell
py -3 C:\Users\aaron\.barz\apps\swarmops_case_commander\prototype\make_demo_video.py
```

Observed output:

```text
C:\Users\aaron\.barz\apps\swarmops_case_commander\artifacts\swarmops-case-commander-demo.mp4
```

Narrated local demo video:

```powershell
py -3 C:\Users\aaron\.barz\apps\swarmops_case_commander\prototype\make_narrated_demo_video.py
```

Observed output:

```text
C:\Users\aaron\.barz\apps\swarmops_case_commander\artifacts\swarmops-case-commander-narrated-demo.mp4
```

Public asset link checks:

```text
https://raw.githubusercontent.com/D0ubl3-A/swarmops-case-commander/main/artifacts/swarmops-case-commander-narrated-demo.mp4 -> 200
https://raw.githubusercontent.com/D0ubl3-A/swarmops-case-commander/main/artifacts/swarmops-case-commander-deck.pdf -> 200
https://raw.githubusercontent.com/D0ubl3-A/swarmops-case-commander/main/artifacts/SO-CASE-001-approved-evidence-report.json -> 200
```

Evidence artifact generation:

```powershell
py -3 C:\Users\aaron\.barz\apps\swarmops_case_commander\prototype\generate_evidence.py
```

Observed output:

```text
C:\Users\aaron\.barz\apps\swarmops_case_commander\artifacts\SO-CASE-001-evidence-report.json
C:\Users\aaron\.barz\apps\swarmops_case_commander\artifacts\SO-CASE-001-approved-evidence-report.json
```

Interaction-state check:

```powershell
py -3 C:\Users\aaron\.barz\apps\swarmops_case_commander\prototype\interaction_check.py
```

Result:

```text
swarmops interaction check passed
approval=approved
final_status=approved_for_handoff
```

UiPath handoff API check:

```powershell
py -3 C:\Users\aaron\.barz\apps\swarmops_case_commander\prototype\api_check.py
```

Result:

```text
swarmops api check passed
handoff_status=pending_human_approval
approval_status=approved
```

OpenAPI contract check:

```powershell
py -3 C:\Users\aaron\.barz\apps\swarmops_case_commander\prototype\openapi_check.py
```

Result:

```text
swarmops openapi check passed
paths=5
```

Submission page check:

```powershell
py -3 C:\Users\aaron\.barz\apps\swarmops_case_commander\prototype\submission_page_check.py
```

Result:

```text
swarmops submission page check passed
links=5
```

GitHub Pages build check:

```powershell
py -3 C:\Users\aaron\.barz\apps\swarmops_case_commander\prototype\pages_build_check.py
```

Result:

```text
swarmops pages build check passed
files=8
```

Submit packet check:

```powershell
py -3 C:\Users\aaron\.barz\apps\swarmops_case_commander\prototype\submit_packet_check.py
```

Result:

```text
swarmops submit packet check passed
required_items=9
```

Submission bundle check:

```powershell
py -3 C:\Users\aaron\.barz\apps\swarmops_case_commander\prototype\submission_bundle_check.py
```

Result:

```text
swarmops submission bundle check passed
files=10
```

Final completion audit check:

```powershell
py -3 C:\Users\aaron\.barz\apps\swarmops_case_commander\prototype\final_audit_check.py
```

Result:

```text
swarmops final audit check passed
required_items=9
```

Hosted submission page check:

```text
https://d0ubl3-a.github.io/swarmops-case-commander/ -> 200
content includes "SwarmOps Case Commander" -> true
```

Versioned release check:

```text
https://github.com/D0ubl3-A/swarmops-case-commander/releases/tag/v0.1.0
assets: openapi.json, SO-CASE-001-approved-evidence-report.json, swarmops-case-commander-deck.pdf, swarmops-case-commander-narrated-demo.mp4, swarmops-case-commander-submission-bundle.zip
```

## Requirements Covered

| Requirement | Evidence |
| --- | --- |
| User can run local prototype | Served at `http://127.0.0.1:8788/prototype/index.html` |
| Seeded case loads | Server check returned `SO-CASE-001` |
| Agent plan visible | Screenshot shows bounded agent work panel |
| At least five agent outputs | Smoke check returned `agents=5` |
| Risky action blocked | Smoke/server check returned `approval=pending`; screenshot shows approval gate |
| Evidence report generated | Screenshot shows audit-ready JSON |
| Export control exists | `Export evidence` button in UI and `exportReport` in app.js |
| Evidence artifact can be generated without browser click | `prototype/generate_evidence.py` |
| Human approval state transition is implemented | `prototype/interaction_check.py` and approved evidence artifact |
| UiPath handoff API exists | `prototype/swarmops_api.py` |
| UiPath handoff API contract passes | `prototype/api_check.py` |
| OpenAPI contract exists | `docs/openapi.json` |
| OpenAPI contract passes | `prototype/openapi_check.py` |
| Static submission page exists | `submission/index.html` |
| Submission page check passes | `prototype/submission_page_check.py` |
| Pages build workflow exists | `.github/workflows/pages.yml` |
| Pages build check passes | `prototype/pages_build_check.py` |
| Submit packet exists | `docs/submit-now.md` |
| Submit packet check passes | `prototype/submit_packet_check.py` |
| Submission bundle exists | `artifacts/swarmops-case-commander-submission-bundle.zip` |
| Submission bundle check passes | `prototype/submission_bundle_check.py` |
| Final completion audit exists | `docs/final-completion-audit.md` |
| Final completion audit check passes | `prototype/final_audit_check.py` |
| Hosted submission page is live | `https://d0ubl3-a.github.io/swarmops-case-commander/` returned 200 |
| Versioned release exists | `https://github.com/D0ubl3-A/swarmops-case-commander/releases/tag/v0.1.0` |
| Presentation deck exists | `deck/index.html` and `artifacts/swarmops-case-commander-deck.pdf` |
| Public repo exists | `https://github.com/D0ubl3-A/swarmops-case-commander` |
| Local proof demo video exists | `artifacts/swarmops-case-commander-demo.mp4` |
| Narrated local demo video exists | `artifacts/swarmops-case-commander-narrated-demo.mp4` |
| Public asset links resolve | Raw GitHub video, deck, and evidence links returned 200 |

## Remaining Validation Needed

- UiPath Maestro Case flow proof.
- Public narrated demo video check.
- Deck link check.
