# SwarmOps Case Commander

SwarmOps Case Commander is a UiPath AgentHack project concept: a governed agent command center for exception-heavy business workflows.

Public repository:

```text
https://github.com/D0ubl3-A/swarmops-case-commander
```

## One-Liner

A UiPath-governed case command center that turns messy vendor onboarding and purchase approval requests into staged agent work, human approval gates, and audit-ready evidence.

## Demo Scenario

```text
Onboard this vendor, validate risk, prepare approval, and create the procurement handoff.
```

## Minimum Winning Flow

1. Intake: user submits a vendor onboarding / purchase approval request.
2. Case creation: system opens a staged case.
3. Delegation: bounded agents produce intake, vendor-data, compliance, approval-summary, and evidence outputs.
4. Safe automation: low-risk parsing, checks, summaries, and missing-info detection run automatically.
5. Human gate: risky actions pause for approval.
6. Final report: case timeline, agent outputs, approvals, blocked actions, and evidence manifest are shown.

## UiPath Fit

Target track: UiPath Maestro Case.

The local prototype should prove the workflow first. The UiPath layer should then become the orchestration/governance layer for case stages, human tasks, and robot/API handoffs.

## Build Rules

- Build a new working solution for the hackathon period.
- No placeholder, mock-only, or fake final integration claims.
- Public repo must include README, setup, source, assets, and MIT or Apache 2.0 license.
- Demo video must be public, show the working project, and stay under 5 minutes.
- Submission needs a presentation deck link.
- Codex/agent contribution should be documented honestly for bonus platform points.

## Current Status

```text
phase: local_prototype
primary_target: UiPath AgentHack
deadline: 2026-06-29 11:45 PM PDT
next_action: attach UiPath Maestro Case flow after Labs access is confirmed
public_repo: https://github.com/D0ubl3-A/swarmops-case-commander
```

## Project Files

- `docs/prototype-spec.md` - build spec
- `docs/demo-script.md` - video/story script
- `docs/architecture.md` - system architecture and trust boundary
- `docs/uipath-integration-contract.md` - UiPath handoff contract
- `docs/submission-package.md` - Devpost-ready text and required links
- `docs/devpost-final-draft.md` - copy/paste Devpost final draft
- `docs/validation-report.md` - current verification evidence
- `docs/deck-outline.md` - presentation deck outline
- `docs/repo-readiness.md` - public repository checklist
- `docs/finish-checklist.md` - remaining work tracker
- `docs/video-shot-list.md` - demo video shot plan
- `data/sample-case.json` - seeded demo input and expected outputs
- `prototype/` - runnable local prototype
- `prototype/swarmops_api.py` - local UiPath handoff API
- `prototype/api_check.py` - API contract verifier
- `LICENSE` - MIT license

## Run Local Prototype

From this folder:

```powershell
py -3 -m http.server 8788 -d C:\Users\aaron\.barz\apps\swarmops_case_commander
```

Open:

```text
http://127.0.0.1:8788/prototype/index.html
```

Smoke check:

```powershell
py -3 C:\Users\aaron\.barz\apps\swarmops_case_commander\prototype\smoke_check.py
```

Generate evidence artifact:

```powershell
py -3 C:\Users\aaron\.barz\apps\swarmops_case_commander\prototype\generate_evidence.py
```

Check approval transition:

```powershell
py -3 C:\Users\aaron\.barz\apps\swarmops_case_commander\prototype\interaction_check.py
```

Run UiPath handoff API:

```powershell
py -3 C:\Users\aaron\.barz\apps\swarmops_case_commander\prototype\swarmops_api.py --port 8791
```

Verify API contract:

```powershell
py -3 C:\Users\aaron\.barz\apps\swarmops_case_commander\prototype\api_check.py
```

Verified screenshot:

```text
C:\Users\aaron\.barz\artifacts\swarmops-case-commander-screenshot.png
```

Generated evidence:

```text
C:\Users\aaron\.barz\apps\swarmops_case_commander\artifacts\SO-CASE-001-evidence-report.json
C:\Users\aaron\.barz\apps\swarmops_case_commander\artifacts\SO-CASE-001-approved-evidence-report.json
```

Presentation deck:

```text
http://127.0.0.1:8788/deck/index.html
C:\Users\aaron\.barz\apps\swarmops_case_commander\artifacts\swarmops-case-commander-deck.pdf
C:\Users\aaron\.barz\artifacts\swarmops-deck-screenshot.png
```

Generated local demo video:

```text
C:\Users\aaron\.barz\apps\swarmops_case_commander\artifacts\swarmops-case-commander-demo.mp4
C:\Users\aaron\.barz\apps\swarmops_case_commander\artifacts\swarmops-case-commander-narrated-demo.mp4
```

Public asset links:

```text
https://raw.githubusercontent.com/D0ubl3-A/swarmops-case-commander/main/artifacts/swarmops-case-commander-narrated-demo.mp4
https://raw.githubusercontent.com/D0ubl3-A/swarmops-case-commander/main/artifacts/swarmops-case-commander-deck.pdf
https://raw.githubusercontent.com/D0ubl3-A/swarmops-case-commander/main/artifacts/SO-CASE-001-approved-evidence-report.json
```
