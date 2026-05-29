# UiPath Maestro Build Guide

This guide turns the local SwarmOps prototype into a concrete UiPath Maestro Case demo path. Use it only after UiPath Automation Cloud / Maestro access is available.

## Local API

Start the handoff API:

```powershell
py -3 C:\Users\aaron\.barz\apps\swarmops_case_commander\prototype\swarmops_api.py --port 8791
```

Verify the API:

```powershell
py -3 C:\Users\aaron\.barz\apps\swarmops_case_commander\prototype\api_check.py
```

OpenAPI contract:

```text
C:\Users\aaron\.barz\apps\swarmops_case_commander\docs\openapi.json
```

Machine-readable Maestro field map:

```text
C:\Users\aaron\.barz\apps\swarmops_case_commander\docs\maestro-field-map.json
GET http://127.0.0.1:8791/api/cases/SO-CASE-001/maestro-field-map
```

Verify the field map before configuring Maestro:

```powershell
py -3 C:\Users\aaron\.barz\apps\swarmops_case_commander\prototype\maestro_field_map_check.py
```

## Maestro Case Shape

Create one case type:

```text
SwarmOps Vendor Onboarding
```

Create these stages:

1. Intake
2. Vendor Data Review
3. Compliance Check
4. Human Approval
5. Fulfillment Handoff
6. Final Audit

## Data Fields

Recommended case fields:

| Field | Type | Source |
| --- | --- | --- |
| `case_id` | Text | `SO-CASE-001` |
| `vendor_name` | Text | `Northstar Components` |
| `requested_purchase_amount` | Number | `48500` |
| `urgency` | Text | `rush` |
| `final_status` | Text | API handoff/evidence payload |
| `risk_flags_json` | Text/JSON | `GET /api/cases/SO-CASE-001/handoff` |
| `agent_outputs_json` | Text/JSON | `GET /api/cases/SO-CASE-001/handoff` |
| `evidence_json` | Text/JSON/File | `GET /api/cases/SO-CASE-001/evidence` |

## API Steps

1. In the intake stage, call:

```text
GET http://127.0.0.1:8791/api/cases/SO-CASE-001
```

2. In Vendor Data Review or Compliance Check, call:

```text
GET http://127.0.0.1:8791/api/cases/SO-CASE-001/handoff
```

3. Store `risk_flags`, `agent_outputs`, and `approval_required` on the case.

4. Optional setup aid: fetch the field map and copy the listed stages, case fields, API calls, and human task into the Maestro case configuration.

```text
GET http://127.0.0.1:8791/api/cases/SO-CASE-001/maestro-field-map
```

5. In Human Approval, create a human task using this label:

```text
Approve vendor setup after missing artifacts are collected
```

6. When the reviewer approves, call:

```text
POST http://127.0.0.1:8791/api/cases/SO-CASE-001/approval
Content-Type: application/json

{"decision":"approved"}
```

7. Store the returned evidence report as the final case artifact.

8. In Final Audit, attach or display:

```text
GET http://127.0.0.1:8791/api/cases/SO-CASE-001/evidence
```

## Demo Recording Checklist

Record these moments:

- Case type and six stages in UiPath.
- API call or connector step fetching the handoff payload.
- Human approval task with the high-risk vendor setup language.
- Approval callback returning `approved_for_handoff`.
- Evidence JSON attached, displayed, or referenced as the final audit artifact.
- Local SwarmOps command center showing the same case, agents, approval gate, and evidence.

## Honest Submission Language

Use this after the Maestro recording exists:

```text
SwarmOps uses a local handoff API that UiPath Maestro Case calls for case data, bounded agent outputs, approval requirements, and evidence JSON. The demo records the Maestro case stages and human task while SwarmOps provides the agent/evidence layer.
```

Use this until the Maestro recording exists:

```text
The local SwarmOps prototype and handoff API are implemented and verified. UiPath Maestro Case is the target orchestration layer; the repo includes the OpenAPI contract and build guide for the case stages, human task, and evidence artifact handoff.
```
