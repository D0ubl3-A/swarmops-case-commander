# Demo Video Shot List

Target: under 5 minutes.

## Core Story

SwarmOps Case Commander shows how enterprises can let AI agents accelerate case work without giving up human control, auditability, or governance.

## Shots

1. Title: SwarmOps Case Commander.
2. Problem: unbounded agents are risky in procurement, finance, HR, claims, and operations.
3. Workflow: vendor onboarding and rush purchase approval.
4. Prototype proof: command center with case timeline, approval gate, agent outputs, and evidence JSON.
5. Agent proof: five bounded agents, each with one scope and evidence ID.
6. Human gate: high-risk vendor setup is blocked until a person approves.
7. Evidence proof: pending and approved JSON artifacts are generated and validated.
8. UiPath fit: Maestro Case stages, human task, robot/API step, case artifact.
9. Closing: fast enough for operations, controlled enough for enterprise trust.

## Narration Draft

SwarmOps Case Commander is a governed agent command center for enterprise case work. The demo uses vendor onboarding and purchase approval because it has the exact pattern enterprises struggle with: messy intake, missing documents, compliance risk, and state-changing actions that need approval.

The system opens a case, delegates safe analysis to bounded agents, blocks high-risk actions for human approval, and produces audit-ready evidence JSON. The local prototype already runs with a seeded case, five agent outputs, a pending approval gate, approval-state verification, and generated evidence artifacts.

For UiPath AgentHack, the target integration is UiPath Maestro Case. Maestro owns the case stages and human task. SwarmOps returns the plan, risk flags, agent outputs, and evidence manifest. That turns agent chaos into governed automation: fast enough for operations, controlled enough for enterprise trust.
