# Presentation Deck Outline

Target: UiPath AgentHack submission deck.

## Slide 1 - Title

**SwarmOps Case Commander**

Governed agent swarms for enterprise case work.

## Slide 2 - Problem

Enterprise teams want AI agents to speed up procurement, finance, HR, claims, and customer operations, but unbounded agents are risky. Real workflows require approvals, evidence, stage control, and auditability.

## Slide 3 - Solution

SwarmOps turns a messy business request into a governed case:

- staged workflow
- bounded specialist agents
- safe automatic analysis
- human approval gates
- audit-ready evidence JSON

## Slide 4 - Demo Scenario

Vendor onboarding and rush purchase approval:

```text
Onboard Northstar Components as a new vendor for a $48,500 rush purchase. Validate risk, prepare approval, and create the procurement handoff.
```

## Slide 5 - Workflow

1. Intake
2. Vendor Data Review
3. Compliance Check
4. Purchase Approval
5. Fulfillment Handoff
6. Final Audit

## Slide 6 - Agent Roles

- Intake Agent
- Vendor Data Agent
- Compliance Agent
- Approval Summary Agent
- Evidence Agent

Each agent has one scope, one output, one evidence ID, and no permission to finalize risky actions.

## Slide 7 - Human Approval Gate

Blocked high-risk action:

```text
Approve vendor setup after missing artifacts are collected.
```

Human approval changes final status from:

```text
pending_human_approval -> approved_for_handoff
```

## Slide 8 - UiPath Fit

Target track: UiPath Maestro Case.

| SwarmOps | UiPath |
| --- | --- |
| Case stages | Maestro Case stages |
| Human approval gate | Human task |
| Safe agent work | Robot/API step |
| Evidence JSON | Case artifact |
| Final status | Case completion state |

## Slide 9 - Technical Proof

Current implemented proof:

- runnable local dashboard
- seeded case data
- approval state transition
- evidence export
- generated pending and approved evidence artifacts
- smoke and interaction checks
- screenshot proof

## Slide 10 - Business Impact

SwarmOps helps operations leaders adopt AI agents without losing control. It is useful for procurement, finance, HR onboarding, claims, compliance, and customer operations.

## Slide 11 - What Codex Built

Codex helped create the bounded swarm architecture, project strategy, local prototype, validation scripts, evidence artifacts, and submission package. The agent contribution is documented through reports and generated project files.

## Slide 12 - Next Step

Connect the local prototype to UiPath Automation Cloud:

- Maestro Case stages
- Human approval task
- robot/API handoff
- evidence artifact attachment
- final demo video under 5 minutes
