---
name: qa-test-execution
description: "Implement or execute authorized software QA tests across unit, integration, API, database, browser E2E and visual checks; collect reproducible evidence and diagnose failures. Use for test automation and regression execution in a verified safe environment; not for unsanctioned production testing or human UAT sign-off."
---

# Test Automation and Evidence

## Purpose
Select and run the smallest justified automated suite, or build missing assertions when test-code changes are explicitly requested. Preserve factual evidence from first attempt through retest. Project-specific scripts and required suites take precedence over generic commands.

## Preflight
Confirm exact candidate SHA/base, clean or documented dirty working tree, test framework, commands, target URLs, environment identity, test DB, storage, fake email/provider endpoints, synthetic identities, rate limits, allowed side effects and rollback/teardown. A hostname or database name containing test does **not** prove isolation. If execution safety cannot be established, stay read-only and mark execution BLOCKED.

## Workflow
1. Inspect project instructions, manifests, CI, present tests, fixture generation, reporters and scripts. Do not invent commands or silently install dependencies.
2. Map each requested business assertion to existing cases and gaps. Prefer unit/contract tests for pure rules, real DB/API tests for integrity and authorization, and browser E2E for user interaction and persisted outcomes; do not overmock the boundary under test.
3. Select focused change tests, critical dependency contracts and protected security/integrity checks. Capture initial discovery counts and explicit skipped/filtered/quarantined cases; zero discovered tests is not a pass.
4. With authorization, run nonmutating static tests before isolated integration/browser tests. Track exact command, SHA, OS/tool versions, start/end, exit status, discovered/passed/failed/skipped, fixture ID and redacted log/trace/screenshot paths.
5. For failures classify reproducible product defect, test defect, infrastructure failure, flake or unknown. Preserve first failure, rerun deterministically with recorded seed and conditions. Do not use retry success to conceal a genuine failure.
6. Assert UI/API response **and** persistent state, audit/outbox/events, idempotency and access denial when relevant. Re-run a minimal targeted regression after authorized fixes plus impacted dependencies.
7. Tear down only resources created for the run. Stop on unexpected real-data access, outward messages, provider charges, secret exposure or cross-tenant data.

## Output contract
Provide an evidence ledger by check ID with PASS, FAIL, BLOCKED, NOT_RUN or NOT_APPLICABLE; explain actual command, exit status, execution counts, fixtures, SHA, observed outcome, artifacts and next action. Separate inherited CI evidence from independently executed verification. Human UAT is never an automation side effect.

## Example
Input: Test an autosave fix in a script editor with a disposable database.
Expected: capture typed content, network failure and recovery, reload confirmation, stale-write conflict and a DB assertion. A green unit test alone cannot establish the browser workflow.

## Boundaries
No unrestricted fuzz/load, migrations, cleanup, live messaging, release workflows or provider calls without matching explicit authorization. Build-only or static-only results must not be described as runtime UAT. See [behavioral evaluations](references/evaluations.md).
