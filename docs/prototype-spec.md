# Prototype Spec

## Product

SwarmOps Case Commander

## Target User

Automation leads and operations managers in procurement, finance, HR, claims, and customer operations.

## Problem

Enterprise teams want AI agents to move work faster, but unbounded agents are hard to trust. Messy business workflows need case stages, evidence, approvals, and clear responsibility.

## Core Demo

Vendor onboarding and purchase approval.

Input:

```text
Onboard Northstar Components as a new vendor for a $48,500 rush purchase. Validate risk, prepare approval, and create the procurement handoff.
```

## Case Stages

1. Intake
2. Vendor Data Review
3. Compliance Check
4. Purchase Approval
5. Fulfillment Handoff
6. Final Audit

## Agents

| Agent | Responsibility | Safe Actions | Approval-Gated Actions |
| --- | --- | --- | --- |
| Intake Agent | Normalize request and missing fields | parse request, classify urgency | none |
| Vendor Data Agent | Check vendor completeness | validate required fields, flag missing docs | approve vendor record |
| Compliance Agent | Risk and policy check | flag amount threshold, sanctions/doc checklist | accept compliance risk |
| Approval Summary Agent | Draft approval memo | summarize risk, amount, urgency | send approval / create PO |
| Evidence Agent | Build audit trail | compile events, outputs, blockers | finalize case |

## Prototype Requirements

- Create a case from seeded input.
- Generate agent outputs from deterministic logic or real model output if available.
- Show case timeline.
- Mark risky actions as blocked pending approval.
- Let user approve or reject at least one action.
- Produce final audit/evidence report.
- Export JSON report for video/submission proof.

## UI Requirements

- First screen is the actual command center, not a landing page.
- Dense operational layout: case list/sidebar, active case timeline, agent output panel, approval queue, evidence report.
- No giant marketing hero.
- No nested cards.
- Text must fit on desktop and mobile.
- Use professional enterprise styling with clear status colors.

## Backend Requirements

- A minimal local API is acceptable for prototype.
- Store case state in JSON or SQLite.
- Keep state transitions explicit.
- Every agent output gets an evidence ID.
- Every approval changes case state and is logged.

## UiPath Integration Plan

Local prototype proves product behavior.

UiPath phase should map:

- Maestro Case -> case stages
- Human task -> approval gate
- Robot/API step -> safe automation step
- External service call -> SwarmOps plan/evidence JSON
- Final artifact -> audit report

## Acceptance Criteria

- User can run local prototype.
- Seeded case loads.
- Agent plan is visible.
- At least five agent outputs are visible.
- At least one risky action is blocked.
- Human approval changes the case state.
- Final evidence report is generated.
- Demo script can show the complete flow in under five minutes.
