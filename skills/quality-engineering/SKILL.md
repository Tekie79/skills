---
name: quality-engineering
description: "Plan, inspect, execute, or triage risk-based software quality testing across projects. Use for functional QA, API/database/browser tests, change-impact regression, contract tests, reliability, accessibility, performance test selection, and defect verification. For Meher Flow-specific work prefer meher-flow-qa. Not a substitute for human UAT sign-off or a release authorization."
---
# Quality Engineering

Use for engineering QA of a named product and candidate, not generic code generation or business-user acceptance. Be project-neutral: do not import Meher Flow assumptions into other applications. Produce executable cases and an evidence-based assessment rather than a count of hypothetical tests.

## Identify the assessment

1. Establish project/repository, immutable candidate revision, comparison revision, relevant requirements, supported surfaces, users/roles, target environment, and mode: plan, static inspection, authorized execution, or defect retest.
2. Separate confirmed functionality from roadmap intent. Read the candidate's instructions, test commands, policy, migrations, API contracts, and existing tests before choosing commands.
3. If checkout, environment, tool access or permission is missing, plan or inspect read-only and mark runtime checks BLOCKED or NOT_RUN; do not invent passes. A CI badge/supplied report is attributed evidence, not proof of an independently executed test.
4. Ask only for details that materially affect safe execution; never request credentials in chat.

## Select proportionate regression

Apply [regression selection](references/regression-selection.md). Start with the changed behavior, then data/contract consumers, known regression paths, and protected invariants. Do not run all historical tests by default; do not omit security/data integrity because a UI diff looks small. Record excluded suites and rationale. Candidate policy and explicit required gates override the tier suggestions.

## Design cases

Create requirement -> risk -> observable result -> test level -> owner -> evidence traceability. Use boundary values, state transitions, negative permissions, empty/error/loading states, retries, concurrency, accessibility and representative devices. A passing HTTP response or screenshot alone does not prove persistence or business semantics. Prefer unit tests for deterministic rules, API/DB integration for boundaries, browser tests for real workflows, and human review for usability.

Provide a bounded synthetic fixture manifest with two organizations if tenant-scoped, distinct permissions, stable seed and teardown scope. Keep production data, real messages, external paid providers, and private user content out of test fixtures.

## Execute safely, when authorized

- Read the exact script, environment selectors and side effects before running it. Confirm test database and storage are disposable and isolated; names containing "test" are insufficient.
- Run non-mutating static checks first; proceed to isolated deterministic tests and authorized DB/API/browser checks according to risk.
- Do not deploy, publish, change credentials/permissions, seed a shared database, migrate, purge, load-test live services, scan unauthorised targets, or install unapproved dependencies as an incidental test action.
- Capture candidate SHA, command, exit code, timestamp, environment, tool version, dataset, redacted logs, screenshots/traces, retries and known skips.
- Stop on unexpected external writes, live-data exposure, secret leakage or target ambiguity. Never turn a flaky retry into an invisible pass.

## Defects and verdicts

Statuses: PASS, FAIL, BLOCKED, NOT_RUN, NOT_APPLICABLE. PASS must match its test level and have execution/inspection evidence; NOT_APPLICABLE needs an explicit reason. File findings as confirmed failures or labeled hypotheses with a discriminating test.

Severity: Blocker for tenant/auth/data-loss or destructive integrity failure; High for broken primary work; Medium for secondary incorrect behavior; Low for polish. Use the target project's stricter policy when present. Include reproducible steps, expected/actual, scope, evidence, impact, suggested fix, and required retest. After a fix, rerun targeted tests plus affected dependency checks.

Use [QA evidence template](assets/qa-plan.md) for plans/results. For release decisions route to release-evidence-review or the project's specific release governance. Never conflate agent-run QA with human UAT.

## Example

Input: "Review a permission-sensitive asset upload change; unit tests passed, but staging is unavailable."
Output: a risk-ranked upload/permission/worker matrix, direct API cross-tenant negatives, immutable version and retry tests, supplied unit results marked as supplied, browser/DB gates BLOCKED, and no claim of UAT approval or release readiness.

To evaluate this skill's behavior (not the product), use [evaluation cases](references/evaluations.md).
