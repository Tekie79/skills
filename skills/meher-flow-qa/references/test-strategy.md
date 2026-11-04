# Risk-Based Test Strategy

## Scope and Traceability

Build an inventory of changed modules, users, permissions, canonical entities,
migrations, APIs, events, UI routes, and downstream consumers. Consult the current
requirements matrix and acceptance criteria, not only the diff. Contract tests
cover dependencies that changed indirectly through shared packages or data shapes.

Record each case with ID, requirement, risk, level, role/scope, synthetic fixture,
preconditions, steps, expected observable outcome, teardown, owner, and evidence.
Prioritize tenant/security/data integrity, primary business outcomes, common flows,
then rare/secondary cases. Pairwise selection can reduce routine combinations;
it must not omit critical authorization or destructive-action boundaries.

Use equivalence classes, boundary values, decision tables, state-transition tests,
and exploratory charters. For numeric limits test below/at/above; for collections
test empty/one/many/large. Include Unicode, long input, time zones/DST, expired
tokens, stale record versions, repeated submissions, and interrupted operations.

## Test Levels and Oracles

| Level | What to prove | SlateDog examples |
| --- | --- | --- |
| Static | Types, lint, architecture boundaries, semantic token use, unsafe patterns | Exact repository checks; parameterized scoped queries; transport/database separation |
| Unit | Deterministic business behavior and validation | Scene matching, permission decisions, parser boundaries, retry state transitions |
| Property-based | Invariants across generated inputs and seeds | String scene numbering, serialization round trips, version identity, pagination uniqueness |
| Contract | Versioned schema compatibility and errors | REST/OpenAPI, event envelopes, worker payloads, MCP capability projections |
| DB/API integration | Real constraints, transactions, scoping, concurrency | Cross-tenant ID substitution, outbox atomicity, stale-write conflicts |
| Browser/E2E | Real user journey and persistence across reload | Import -> processing -> reconciliation -> current revision; failure recovery |
| Visual/accessibility | State fidelity, keyboard semantics, responsive layout | Themes, dialogs, dense tables, print surfaces; automated plus manual checks |
| Nonfunctional | Capacity, security, resilience, operational behavior | Search/load, scanner failure, worker lease recovery, backup restore |
| UAT | Business acceptance by accountable users | Film-production personas completing realistic workflows without developer guidance |

Do not overmock the exact boundary being tested. Mock provider networks for routine
tests; use opt-in sandbox contracts for provider interoperability. Count assertions
about business outcomes, not only HTTP 200 or snapshot stability. Verify both the
returned response and durable state/audit/outbox as appropriate.

## Execution Order and Safety

1. Inspect scripts, environment selection, fixture setup, and teardown. Confirm
   allowed side effects and resource limits. Use a disposable test environment
   with synthetic users, isolated storage, Mailpit, and provider fakes by default.
2. Run static/unit/contract checks first. Use current exact root scripts from the
   project map. Capture failure output and exit code without hiding failed stages.
3. With explicit database authorization, run PostgreSQL/API/worker integrations,
   clean-install migrations, and upgrades from supported previous schema/data.
   Inspect `TEST_DATABASE_URL` safely without printing credentials. Do not rely
   solely on a database name containing `test` or an environment label.
4. Start required services with the host's tracked-process facilities. Read the
   candidate browser config to establish base URL, DB seed, ports, server reuse,
   projects, workers, retries, and artifact policy. Avoid attaching to an unrelated
   running server. Do not assume a package script named `test:e2e` exists.
5. Execute critical E2E and risk-targeted regressions, then visual/accessibility,
   exploratory, and approved nonfunctional suites. Native builds require the actual
   supported OS/toolchain; browser emulation does not validate Tauri binaries.
6. Preserve redacted traces/screenshots/logs and test-data manifests. Tear down only
   resources created for this run within scope; never remove shared volumes/data.

## Critical End-to-End Coverage

- Register/verify/login/reset/logout; invitation for existing/new users; token
  expiry/reuse; membership removal and role changes during an active session.
- Create/switch organization and production; refresh/deep-link/back/forward;
  empty membership onboarding; permission-aware navigation and direct API denial.
- FDX/Fountain/TXT/text-PDF import; invalid/image-only PDF rejection; boundary size;
  async progress; worker failure/retry; immutable original; reconciliation and
  stable Scene identity; concurrent edit conflict; current-vs-history save behavior.
- Manual Breakdown create/reuse/merge and scope correctness; optional AI suggestions,
  evidence, review/reject/accept; no canonical writes before authorization/approval.
- Library upload/version/preview/download/search/pinned usage/favorites/rights;
  malware-required pending/error; archive/trash/restore and guarded purge.
- Shot planning/Designer/storyboard/review/portability flows present in the release;
  canonical Scene and Library linkage; source artwork/history preserved; export
  round-trip fidelity and review impacts. Do not assume absent future capabilities.
- Work and contextual collaboration/search/export actually included in scope;
  tenant filters, pagination, stale data, failed writes, and immediate invalidation.
- Multi-tab/multi-user stale writes; slow/offline/reconnect; expired sessions;
  PWA update/logout/cache boundaries; desktop connection/bearer-token lifecycle.

## Advanced Techniques

- **Mutation testing:** target parsers, permission guards, reconciliation,
  idempotency, and concurrency rules; surviving mutants identify weak assertions.
  Measure runtime and restrict scope; mutation score alone is not a release gate.
- **Fuzzing:** bounded parsers, JSON DTOs, import/portability formats, filenames,
  cursor tokens and SVG validation in isolation. No live-tenant endpoint fuzzing
  without explicit scope/rate limits. Store minimal sanitized failing inputs/seeds.
- **Metamorphic tests:** reordering independent inputs does not change identity;
  import/export retains supported semantics; renumbering keeps Scene linkage;
  repeated accepted idempotency keys produce one mutation, not duplicates.
- **Model-based tests:** enumerate invitation, revision, asset lifecycle, approval,
  and job states including illegal transitions, expiry, cancellation and recovery.
- **Differential tests:** compare old/new parser or schema behavior on a reviewed
  golden corpus; document intentionally changed semantics and migration effects.
- **Fault injection:** approved DB/storage/email/provider timeouts and worker
  interruption before/after commit; check invariants rather than only recovery UI.
- **Coverage analysis:** branch/condition coverage on high-risk rules and requirement
  coverage; do not invent a universal percentage or use line coverage as correctness.

## Flakes and Defects

Record first attempt, retries, worker count, random seed, clock/network controls,
and reproduction frequency. Replace timing sleeps with observable state/conditions.
Never update visual baselines merely to silence a diff. Quarantining a required
test leaves its gate unverified; use an approved equivalent evidence method or
block release. Deduplicate findings by root cause but retain affected surfaces.

For each defect include expected/actual, minimal reproducible steps, scope/role,
candidate SHA, severity/impact, file/line or route, and evidence. Distinguish a
proven failure from an untested concern. Fix verification includes a targeted
regression plus affected integration/E2E; unrelated green suites do not close it.
