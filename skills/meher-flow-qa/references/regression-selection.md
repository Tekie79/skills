# Meher Flow Risk-Based Regression Selection

## Principle
Test what changed, the dependencies it can break, and protected invariants. **Do not automatically rerun every historical suite** for a narrow UI change. Conversely, do not use a focused regression as evidence that a public release's canonical mandatory matrix is satisfied.

## Three rings

| Ring | Includes | When |
| --- | --- | --- |
| A: Direct | Changed rules, screen states and exact defect reproduction; positive/negative/boundary plus persistence | Every QA assessment of the change |
| B: Dependency | Relevant API/schema/event/worker, Scene/Shot/camera/asset shared state, impacted sibling screens, export and role differences | Derive from actual call/dependency graph |
| C: Protected | Tenant/production authorization, stable ID/version, save/data loss, audit/outbox and provider approval boundaries | Every change that can affect the invariant; run cheap static/contract proofs otherwise and flag needed runtime checks |

Release-required suites, accessibility review, native distribution, recovery and mandatory vendor validation may exceed A/B/C. The current release policy controls those gates and cannot be replaced by this table.

## Selection workflow
1. Pin candidate SHA and comparison base, enumerate changed files + migrations + flags + dependencies and CI contracts.
2. Associate changed behavior with affected domain entities, routes, API methods, DB tables, event consumers, caching and per-tenant boundary.
3. Choose direct automated cases and evidence of user task; include invalid input, cancellation, retry, reload and permissions.
4. Add dependency cases for actual shared code or state; prove whether unrelated areas are unaffected rather than assuming.
5. Preserve protected negative checks if changed API or data-flow can cross boundaries, including job, export, asset and agent paths.
6. If an existing mandatory test is skipped, zero-discovery, flaky or unavailable, record as unverified; do not substitute green lint or a visually similar check.
7. For broad refactor or release review, expand to the approved full matrix. Record scope expansion and runtime costs.

## Examples

**Shot coverage selection CSS/interaction fix:** A = play-range selection and stable horizontal position at affected widths, cross-overlap/gap semantics; B = Shot timing and camera context resolver plus animation editor selection state; C = exact Shot/Scene version persistence and permissions. An old suite that merely validates hundreds of unchanged SVG assets is not necessarily required for this focused change.

**Changing canonical Scene reconciliation:** A = altered matching, ambiguity, changed/moved/missing; B = Breakdown usage, Shot/Storyboard links, schedule references and export; C = IDs, revision lineage, tenant scoping, outbox and stale-write handling. More integration tests are required than for a shelf icon.

**Project Library asset permission change:** A = rights/list/preview/download; B = pinned/linked usages in Breakdown/Storyboard and worker derivatives; C = tenant/guest denial, signed URL expiry, trash/quarantine and audit. Treat as high exposure.

**Public release:** Read current scripts/release/required-suites.json, scripts/release/security-policy.json and release readiness evidence. An approval-disabled policy is not fixed by passing regression tests.

## Anti-patterns
- “303/303 passed” from an earlier commit treated as current proof.
- One screenshot treated as proof of hidden server-side authorization.
- 100% line coverage treated as business UAT acceptance.
- A named test with zero discoveries or skip flags marked PASS.
- Retrying a flake until it passes without retaining the first failure.
- Updating a visual golden image to silence an unreviewed regression.
- Assigning blanket NOT_APPLICABLE to missing tools instead of BLOCKED/NOT_RUN.

## Output
For each selected and excluded suite record risk, rationale, owner, exact cases, expected oracle, runtime/estimated cost only if known, environment, evidence status and residual gap. Separate scoped feature quality from full release qualification.
