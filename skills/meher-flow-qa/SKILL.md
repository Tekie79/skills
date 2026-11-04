---
name: meher-flow-qa
description: "Plan or perform technical QA for Meher Flow (internal SlateDog repository), including functional, API/DB/worker, security, regression, UX/accessibility, performance and resilience tests. Use for Scene Breakdown, script/revisions, Scheduling, Call Sheets, Shot Designer, Storyboard, Library, AI and other delivered modules. Not human UAT sign-off or automatic public release qualification."
---
# Meher Flow — Technical QA

Assess engineering correctness of the **Meher Flow** production operating system. The internal code repository is Tekie79/SlateDog; never replace established technical identifiers merely to update branding. This skill is stand-alone and tailored to filmmakers, small studios, and creator workflows, but technical PASS is not business UAT approval.

## Mandatory orientation

1. Read [repository and policy baseline](references/repo-baseline.md) and refresh it for the exact candidate SHA; the snapshot is navigation context, not proof of present implementation.
2. Resolve candidate/ref and comparison base, product requirement IDs, implemented pages/APIs, roles, canonical entities, data boundaries, supported installation target (local/self-hosted/cloud only where actually available), and approved test environment.
3. Determine mode: test plan, source audit, authorized execution, regression selection, or retest. If environment/authority are missing, return a test-ready plan with checks BLOCKED/NOT_RUN; do not claim application tests were executed.
4. Before invoking commands, inspect current scripts, CI definitions, migration effects, Playwright configuration and environment. Do not connect to a live project/data source to run tests.

## Scope and risk

Use [module charters](references/module-charters.md) as the candidate-sensitive test menu. Build requirement-to-test coverage, not a fixed number of test cases. Discover domain implementation from source; distinguish implemented, unfinished, and planned. M0–M9 in the PRD describe a product roadmap, not a list of universally shipped features.

Meher Flow invariants take priority:

- One canonical production graph and stable IDs: Character, Scene, Shot, asset, schedule and post entities must not silently fork or detach.
- Production and organization isolation, server authorization, role and guest boundaries across search, data, export and background work.
- Immutable source/revision history; correct downstream invalidation when script, schedule, shot, or asset versions change.
- No false saved/published/approved states; stale writes, failed worker jobs and retries are recoverable without duplicate authoritative records.
- Manual capability works independently of optional AI; AI proposals require explicit authorized acceptance; provider errors are safe.
- Light-first design, accessible interaction and director-first terminology. A filmmaker should not need to understand internal rig/binding/override setup to complete primary Shot Designer tasks.

## Change-based selection

1. Inspect diff and data/API/event dependencies, shared packages/CSS, feature flags, contract consumers and security boundaries.
2. Assign T0–T3 test-selection tier (description below) and add protected tests for every changed invariant. T0 visual-only; T1 feature behavior; T2 cross-module/canonical state; T3 permission/DB/migration/release. Escalate based on actual reach. Candidate mandatory policy outranks the tier.
3. Run focused tests for changed behavior and dependent consumers. Do not automatically rerun every historical browser test or SVG fixture for a localized change; still include relevant protected-source and representative critical regression cases. A reported historical count is not fresh evidence.
4. In Shot Designer, verify *visual state and persisted state separately*. Example: choosing a coverage range must not shift horizontal timeline position, change the selected Shot unexpectedly, or expand playback to the full scene.
5. Require direct API cross-tenant negative checks when access boundaries are touched; UI-hidden actions do not prove access control.

## Levels and execution

- Static: exact diff, TypeScript/lint/architecture, schema and asset manifest validation.
- Unit and property tests: state machines, parsing/revisions, schedule constraints, range math, serialization and deterministic business rules.
- Contract/DB/API/worker: PostgreSQL constraints and transactions, outbox/audit, idempotency, auth, retries, print/export generation and integration boundaries.
- Browser/E2E: primary real workflows, refresh/persistence, errors, responsiveness, touch/keyboard, theme, visual layout and accessibility.
- Nonfunctional: isolate and measure with approved budgets; do not invent benchmarks, load limits, penetration-testing results or certification.

Use synthetic Organizations A/B, Projects A1/A2/B1, varied permission presets, and an approved disposable DB/storage. Confirm Mailpit/provider fakes; never send real call sheets, trigger production AI spend, run unauthorized external scans, drop databases, purge files, deploy or activate release policy.

## Evidence and reporting

For each case provide ID, requirement, candidate SHA, role/tenant, dataset, steps, expected durable outcome, actual results, test level, exit code, timestamp, redacted artifact and one of PASS/FAIL/BLOCKED/NOT_RUN/NOT_APPLICABLE. A source audit can PASS a source check, never an unexecuted browser or DB check. List skipped/quarantined/flaky cases and original failures.

Blocker: tenant leak, authorization bypass, data/source/scene identity corruption, broken migration or unrecoverable destructive action. High: broken primary workflow. Medium: secondary function/UX. Low: polish. A suspected issue remains a hypothesis until differentiated by evidence.

Use the [QA report](assets/qa-report.md) and [evaluation cases](references/evaluations.md). For filmmaker/product-owner acceptance use meher-flow-uat; for release decisions follow exact candidate policy, not a green development PR check.

## Example

Request: "QA the new Shot Designer coverage selector."
Deliver: focused interval/color and selection cases (this camera vs other cameras vs uncovered), overlapping shots, selected exact range playback, stable horizontal scroll/zoom, no accidental Shot edit, keyboard/touch, save/reload, plus affected timeline/camera dependencies. Exclude unrelated legacy asset corpus unless the diff actually touches its contracts; report which suites were run and which were not.
