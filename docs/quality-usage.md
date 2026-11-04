# Using the QA/UAT Skill Collection

## Selection and ownership

- **Meher Flow**: start with the meher-flow-qa skill for feature requirements and version-specific risks.
- **Other projects**: select qa-test-design, qa-test-execution, uat-business-acceptance, qa-security-resilience, qa-ux-accessibility, qa-performance or qa-release-readiness by actual requested responsibility.
- **Cross-disciplinary release**: coordinate specialist findings, but keep evidence ownership and statuses distinct. Do not count the same CI result as independent unit, E2E and human UAT evidence.

The repository contains skills, **not a deployed test platform**. Installing a skill does not provide a database, browser, device farm, credentials or production permission.

## Everyday QA flow

1. Identify immutable candidate SHA/base, accepted business requirement, changed modules and permitted environment.
2. Design tests for the changed user journey and affected data/API/dependency graph. Include negative access, interrupted work and persistence.
3. Reuse project test commands only after inspecting their actual side effects. Prefer deterministic synthetic fixtures and fake outgoing services.
4. Execute authorized static/unit/contract checks first; then API/DB/worker and browser/device tests as required.
5. Retain test discovery, skip/flake, first-failure and retest evidence. Green CI cannot stand for an unrun browser suite.
6. Record a risk-based defect list, regression recommendations and evidence gaps.

## Business UAT flow

A director, producer, AD, coordinator or reviewer should receive a realistic **goal** without a sequence of clicks. The UAT facilitator observes completion and friction. Store build, role/tenant, task, actual outcome, evidence and accountable acceptance owner. Browser automation is technical QA, **not** a human acceptance signature.

## Release review flow

Pin build and artifact digests; read exact required suites and current security/publication policy at that SHA. A mandatory failure or disabled publication is NO-GO; missing mandatory evidence is INSUFFICIENT EVIDENCE unless a known blocking failure already controls. Only accountable humans may approve deferrals/acceptance/deployment.

## Meher Flow priority examples

- A Shot Designer timeline-range bug needs direct layout/coverage/selection E2E, Shot timing dependencies and protected canonical-save tests. It does not automatically need full archived SVG replay.
- Scene reconciliation needs stable Scene identity, alias/element usage, revision history, Shot/schedule downstream links and tenant negatives.
- Library upload/rights needs signed URL, pinned usage, scanner states, per-user favorites and immutable media version checks.
- Scheduling needs producer/AD UAT for actual stripboard, Day Plan, DOOD/conflicts and draft/published call sheet outcomes.
- AI requests need disabled-provider manual workflow and explicit approval, permissions, source trace and fake-provider failure tests.

Only assess implemented and candidate-scoped features. A Road Designer or 3D previs roadmap entry is not a failed released capability.

## Evidence rules

Check statuses: PASS, FAIL, BLOCKED, NOT_RUN, NOT_APPLICABLE. Distinguish test-not-run from target-not-available. Security/data-loss failures dominate scores, coverage percentages and UX polish. Capture exact date, SHA, test command/result and redacted artifacts for PASS. Retain first failure and identify flaky cases.

Do not place private screenplay material, real cast contacts, API tokens, production URLs with secrets or signed media links into a public skill repository, test fixture or report.
