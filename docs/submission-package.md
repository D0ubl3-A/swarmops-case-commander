# Submission Package

## Devpost Title

```text
SwarmOps Case Commander
```

## Tagline

```text
Governed agent swarms for enterprise case work: fast automation, human approval, and audit-ready evidence.
```

## Short Description

SwarmOps Case Commander turns exception-heavy workflows into staged case work where bounded AI agents handle safe analysis, risky actions pause for human approval, and every output becomes audit-ready evidence.

## What It Does

The prototype demonstrates vendor onboarding and purchase approval. A user submits a messy business request, the system opens a case, bounded agents produce intake, vendor-data, compliance, approval-summary, and evidence outputs, a high-risk action is blocked for human approval, and the final evidence report can be exported as JSON.

## Why It Matters

Enterprises want agent productivity, but they cannot trust unbounded automation with state-changing business actions. SwarmOps shows a safer pattern: agents can move the work forward while humans keep control over approvals, risk, and final claims.

## How It Uses UiPath

Target integration: UiPath Maestro Case orchestrates the case stages and human approval gate. SwarmOps provides the external agent/evidence layer that returns risk flags, agent outputs, and an evidence manifest.

Current state: local prototype is implemented and verified. UiPath Automation Cloud / Maestro Case integration remains the next required step before final submission claims.

## Built With

- HTML/CSS/JavaScript local prototype
- Python smoke checker
- UiPath Maestro Case integration plan
- Local UiPath handoff API with OpenAPI contract
- Codex-assisted agent-swarm planning and implementation

## Demo Video Requirements

- Under 5 minutes.
- Show the actual prototype running.
- Show seeded case input.
- Show case timeline.
- Show bounded agent outputs.
- Show pending human approval gate.
- Click approve or reject.
- Show final evidence JSON.
- Explain UiPath Maestro Case mapping.

## Links To Include

- Public GitHub repo: https://github.com/D0ubl3-A/swarmops-case-commander
- Hosted submission page: https://d0ubl3-a.github.io/swarmops-case-commander/
- Versioned release: https://github.com/D0ubl3-A/swarmops-case-commander/releases/tag/v0.1.0
- Submission bundle: https://github.com/D0ubl3-A/swarmops-case-commander/releases/download/v0.1.0/swarmops-case-commander-submission-bundle.zip
- Local proof demo video: `C:\Users\aaron\.barz\apps\swarmops_case_commander\artifacts\swarmops-case-commander-demo.mp4`
- Narrated upload candidate: `C:\Users\aaron\.barz\apps\swarmops_case_commander\artifacts\swarmops-case-commander-narrated-demo.mp4`
- Public narrated video file: https://raw.githubusercontent.com/D0ubl3-A/swarmops-case-commander/main/artifacts/swarmops-case-commander-narrated-demo.mp4
- Public YouTube demo video: pending
- Presentation deck PDF: https://raw.githubusercontent.com/D0ubl3-A/swarmops-case-commander/main/artifacts/swarmops-case-commander-deck.pdf
- Approved evidence JSON: https://raw.githubusercontent.com/D0ubl3-A/swarmops-case-commander/main/artifacts/SO-CASE-001-approved-evidence-report.json
- Local prototype path: `C:\Users\aaron\.barz\apps\swarmops_case_commander`
- Screenshot proof: `C:\Users\aaron\.barz\artifacts\swarmops-case-commander-screenshot.png`

## Required Before Final Submission

- Confirm UiPath Labs / Automation Cloud access.
- Build or record Maestro Case flow.
- Public repo is published with MIT license.
- Create presentation deck.
- Upload or re-record the narrated public demo video using `artifacts/swarmops-case-commander-narrated-demo.mp4` as the base.
- Verify public links and judging access.
