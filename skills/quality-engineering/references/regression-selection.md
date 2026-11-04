# Change-Impact and Regression Selection

Regressions are selected from evidence and dependency impact, not from an arbitrary global test count. Resolve a candidate SHA and base SHA; compare changes in code, schema, shared packages, contracts, authorization, events, fixtures, build tooling, and observable UI.

## Selection tiers (guidance, not automatic approval)

| Tier | Example impact | Required reasoning and example checks |
| --- | --- | --- |
| T0 localized presentation | Copy, spacing, icon or a CSS variable with no behavior changes | Static/style rules, targeted rendered state, keyboard/focus and nearby screen checks; inspect shared CSS reach |
| T1 local behavior | One form, menu, filter, calculation or component | Unit/component cases plus primary user/browser journey and error states; review affected API/data paths |
| T2 shared/cross-domain state | Shared form service, serializer, cache, script revision, integrations | All changed-domain tests plus contract/API/DB tests, direct consumer E2E, concurrency/retry, relevant critical cross-domain journeys |
| T3 platform/security/operational | RBAC, tenancy, identity, migrations, outbox, storage, release, recovery | Mandatory project policy, security/tenant negative matrix, data integrity, upgrade/recovery and affected end-to-end tests; no shortcuts to release qualification |

Escalate on observed risk even when file names seem harmless. A shared UI token can impact every route; a one-line query/filter change can leak another tenant. Where security boundaries are touched, negative authorization tests are always included even if classified T0/T1 elsewhere.

## Protected invariants

Evaluate applicability for every candidate: tenant and project isolation; server-side authorization; immutable IDs and version history; no silent data loss; retries/idempotency; valid audit/outbox behavior; safe file/source access; exportability; manual operation when AI is disabled; privacy on caches, search and links; ability to cancel without accidental authoritative mutations.

Include a minimal protected smoke suite spanning login, role/tenant denial, primary production graph, refresh/save and error handling when those capabilities exist. Do not assume a future planned feature is installed.

## Change graph procedure

1. List changed files, API types, DB tables, shared tokens, build switches and migrations.
2. Trace each to readers/writers, related workflows, and contracts; note untested links.
3. Match risk to existing tests and identify missing regression or UAT charters.
4. Record chosen suites, excluded suites (why), and policy-mandatory suites separately.
5. Fail closed on unverified mandatory gates; do not claim "all regression tests passed" from a scoped run.

Use risk-based prioritization without weakening release policy. A focused feature QA result is not the same as a public-release qualification.
