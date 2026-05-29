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
| Presentation deck exists | `deck/index.html` and `artifacts/swarmops-case-commander-deck.pdf` |
| Public repo exists | `https://github.com/D0ubl3-A/swarmops-case-commander` |
| Local proof demo video exists | `artifacts/swarmops-case-commander-demo.mp4` |
| Narrated local demo video exists | `artifacts/swarmops-case-commander-narrated-demo.mp4` |
| Public asset links resolve | Raw GitHub video, deck, and evidence links returned 200 |

## Remaining Validation Needed

- UiPath Maestro Case flow proof.
- Public narrated demo video check.
- Deck link check.
