---
name: meher-flow-uat
description: "Design and facilitate filmmaker-focused User Acceptance Testing for Meher Flow: producers, assistant directors, directors, crew, editors, reviewers and content creators completing real workflows. Use for business UAT plans, test scripts, pilot sessions, usability feedback, acceptance evidence, and owner sign-off tracking. Not automated QA, simulated user approval or release activation."
---
# Meher Flow — Film Production UAT

The goal is to establish whether filmmakers and small production teams can complete their work **without developer guidance**, not just whether technical tests pass. Separate human UAT, automated browser evidence and public-release authority.

## Establish a candidate and users

Read the [real-world acceptance journeys](references/scenarios.md). Identify exact candidate version/SHA, delivered modules and release scope, product requirement IDs, target environment, synthetic production, approved user roles, allowed actions, and actual sign-off owner. Confirm current terminology and UX against the candidate, not only older design screenshots.

Use a mix of first-time indie producer, experienced production manager/1st AD, director/DP, coordinator, cast/crew guest, editor/post supervisor, client reviewer and small content creator when relevant. People may hold multiple roles; validate permissions as configured instead of assuming role labels grant access.

## Prepare business charters

Build scenarios around outcomes: import and correct a screenplay; assign recurring elements once; schedule a shoot; issue a revised call sheet in a safe sandbox; plan camera coverage without rigging terminology; review a storyboard; collaborate and restore a failed operation. Scope only functions actually shipped or explicitly required by the candidate.

For each charter record:
- Persona and business goal, synthetic starting production/episode and prerequisites.
- User-facing task phrased naturally; do not provide step-by-step developer hints.
- Expected outcome, including correct authoritative record/version, private data restrictions and useful error messages.
- Interrupted/negative path and observation points: discoverability, clicks/steps if observed, mistakes, recovery, confidence and accessibility.
- Participant's actual result, assistance, evidence, defect/feature-request classification, tester/date and approving owner.

A feature can technically work but fail UAT when a director cannot find Camera or has to manually register its rig; or when a 1st AD cannot identify current approved call sheets. Do not trade away version safety to make workflows shorter.

## Facilitate

1. Brief participants on the goal, not the exact buttons. Provide a synthetic role-specific fixture and task, using sandbox email and fake provider destinations.
2. Observe task completion across page changes, refresh, navigation and saved state. Include a failed network/service response or access denial where safe.
3. Record what the person actually did and whether they needed intervention. Differentiate user confusion, missing requirements, implementation defect and requested enhancement.
4. Use PASS/FAIL/BLOCKED/NOT_RUN/NOT_APPLICABLE per task, linked to actual observations. Do not convert a mock session, generated script or Playwright result into human success.
5. Product-owner sign-off is approved/rejected/NOT_OBTAINED, with real attestation. An agent never signs for a director, project owner or release officer.

Do not publish call sheets to real contacts, submit paid AI jobs, modify production data, deploy, or invoke destructive cleanup as part of UAT preparation. Favor local/self-hosted workflows and core tasks without external AI where supported.

## Deliverables

Provide [UAT session pack](assets/uat-pack.md) with traceability, persona tasks, outcome, observations, evidence, issue IDs, sign-off and remaining risks. Use [evaluation cases](references/evaluations.md) when maintaining this skill. For automated/API/DB defects refer to meher-flow-qa; for public release use the current project policy and separate release evidence review.

## Example

Request: "Can an independent director plan a scene in the new Shot Designer?"
Give the director a staged room and two named characters. Ask them to place characters, add a camera and light, select just one Shot interval, review the storyboard and return later to reopen the saved plan. Observe whether they find features without having to discover binding/rig internals, and whether they understand Scene-wide vs Shot-only edits. No success claim until a real participant runs the journey.
