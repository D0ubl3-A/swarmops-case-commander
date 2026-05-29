# Devpost Final Draft

## Project Name

SwarmOps Case Commander

## Tagline

Governed agent swarms for enterprise case work: fast automation, human approval, and audit-ready evidence.

## Public Links

- Code: https://github.com/D0ubl3-A/swarmops-case-commander
- Narrated demo video file: https://raw.githubusercontent.com/D0ubl3-A/swarmops-case-commander/main/artifacts/swarmops-case-commander-narrated-demo.mp4
- Presentation deck PDF: https://raw.githubusercontent.com/D0ubl3-A/swarmops-case-commander/main/artifacts/swarmops-case-commander-deck.pdf
- Approved evidence JSON: https://raw.githubusercontent.com/D0ubl3-A/swarmops-case-commander/main/artifacts/SO-CASE-001-approved-evidence-report.json

## Elevator Pitch

SwarmOps Case Commander turns messy enterprise case work into governed agent execution. Instead of allowing unbounded agents to make risky business changes, it gives each agent a narrow scope, routes high-risk actions through a human approval gate, and exports audit-ready evidence that a reviewer can inspect.

## What It Does

The prototype demonstrates a vendor onboarding and rush purchase approval workflow. A seeded business request opens a case, creates staged work, delegates safe analysis to bounded agents, blocks the state-changing vendor setup action for approval, and generates evidence JSON before and after the human approval transition.

The working local prototype shows:

- A case timeline for intake, vendor review, compliance, approval, fulfillment handoff, and audit.
- Five bounded agents with evidence IDs and scoped outputs.
- A high-risk approval gate that prevents unsafe automation.
- Pending and approved evidence artifacts.
- A presentation deck and narrated demo video artifact.

## Why It Matters

Enterprise teams want the speed of AI agents, but they cannot let autonomous systems approve vendors, accept compliance risk, send external messages, or create purchase orders without control. SwarmOps shows a practical pattern for deploying agents inside real business processes: automate safe analysis, pause risky decisions, and preserve every important output as evidence.

This can apply beyond procurement to claims, HR onboarding, finance exceptions, security reviews, and operations handoffs.

## UiPath Track Fit

Target track: UiPath Maestro Case.

The intended integration is for UiPath Maestro Case to own case stages, human tasks, and governed orchestration. SwarmOps acts as the bounded agent and evidence layer that returns risk flags, agent outputs, approval requirements, and an evidence manifest.

Current verified state: the local prototype, evidence generation, approval transition, public repo, deck PDF, and narrated demo artifact are implemented and public. UiPath Automation Cloud / Maestro Case proof is the next required integration step before claiming a fully connected UiPath implementation.

## Built With

- HTML, CSS, and JavaScript for the local command center.
- Python for smoke checks, interaction verification, evidence generation, and demo video rendering.
- UiPath Maestro Case integration contract and case-stage design.
- Codex-assisted agent-swarm planning, implementation, verification, and packaging.

## How We Built It

We started by designing the trust boundary: agents can propose analysis and evidence, but high-risk actions remain blocked until human approval. Then we built a local case command center around a vendor onboarding scenario, added deterministic evidence artifacts, wrote smoke and interaction checks, produced a deck, and generated a narrated demo video from the verified screenshots and evidence state.

The repo includes the integration contract needed to connect the local evidence layer to UiPath Maestro Case once Automation Cloud access is available.

## Challenges

The main challenge was keeping the demo honest while still making it compelling. It would be easy to label a local prototype as a complete UiPath integration. Instead, the project separates what is already verified from what remains to be connected in UiPath, so judges can inspect real code and evidence without inflated claims.

## Accomplishments

- Working local prototype.
- Five bounded agent outputs.
- Human approval gate with verified state transition.
- Generated pending and approved evidence JSON.
- Public GitHub repo.
- Presentation deck PDF.
- Narrated demo video artifact.
- UiPath Maestro Case integration contract.

## What Is Next

1. Build the Maestro Case stages in UiPath Automation Cloud.
2. Add the human approval task in UiPath.
3. Connect the SwarmOps evidence JSON as a case artifact.
4. Record the public YouTube demo with UiPath proof and the existing local prototype proof.
5. Submit the final Devpost project with the GitHub repo, video, and deck.

## Final Submission Honesty Note

Use this wording until the UiPath flow is actually connected:

> The local SwarmOps prototype and evidence pipeline are implemented and verified. UiPath Maestro Case is the target orchestration layer, and the repo includes the integration contract for the case stages, human task, and evidence artifact handoff.

Do not use "fully integrated with UiPath" unless there is a real Automation Cloud / Maestro Case recording or screenshot proving it.
