# Verified Project Map

## Provenance and Freshness

Source: private repository `Tekie79/SlateDog`, `develop` inspected on 2026-11-01
at commit `11ac64cec6462d1bbb1e4e09a5a4ac4ac151e408` (commit date 2026-10-31).
This is a navigation baseline, not proof the current branch still matches it.
Only source/configuration inspection was performed when authoring the skill; no
application tests, deployment, load tests, or product-owner UAT were executed.

The user-facing name is **Meher Flow**; SlateDog remains an internal identifier.
Do not flag retained package/cookie/storage identifiers as branding bugs without
checking the compatibility contract.

Resolve the candidate before each assessment. With authorized GitHub CLI access:

```sh
gh api repos/Tekie79/SlateDog/commits/develop --jq .sha
```

Read files at the returned immutable SHA, not a moving branch. GitHub tools may
have different access scopes; during authoring the GitHub connector returned 404
while locally authenticated `gh` could read the private repository. A 404 alone
does not establish a missing branch or nonexistent project. Do not expose tokens
or change credentials/permissions to bypass denied access.

## Architecture and Sources

| Area | Verified baseline | Primary repository sources to refresh |
| --- | --- | --- |
| Web/PWA | Next.js, React, TypeScript; server-hosted browser client with service worker registration | `apps/web/package.json`, `apps/web/app/`, `apps/web/playwright.config.ts` |
| API | NestJS modular monolith, versioned REST/OpenAPI | `apps/api/src/`, `docs/ARCHITECTURE.md`, `/openapi.json` on approved test target |
| Data | PostgreSQL source of truth; ordered SQL migrations; tenant-scoped relationships | `packages/database/`, `docs/DATABASE_CONVENTIONS.md`, `docs/DOMAIN_MODEL.md` |
| Jobs | Separate worker; PostgreSQL transactional outbox, retries, leases, idempotency | `apps/worker/`, `docs/EVENTS.md` |
| Storage | StorageProvider, local filesystem baseline; immutable originals and versions | `docs/PROJECT_LIBRARY.md`, `docs/ARCHITECTURE.md` |
| Native | Vite/React/Tauri desktop; bearer sessions rather than browser cookie/CSRF | `apps/client/`, `docs/ARCHITECTURE.md` |
| AI/agents | Optional proposal-based AI, capability/approval boundaries; MCP HTTP/STDIO adapters | `apps/api/src/agent-platform/`, `apps/mcp-server/`, `docs/operations/agent-batch-execution.md` |
| Design | Approved light/dark references, semantic tokens, responsive workspace | `docs/UI_DESIGN_SYSTEM.md`, `docs/THEME_SYSTEM.md`, `docs/designs/references/` |
| Quality | Root scripts, DB integration, web E2E, Quality and release workflows | `package.json`, `.github/workflows/`, `DEVELOPMENT_CI_PR_READINESS.md` |
| Governance | Requirement traceability and manual UAT gate | `docs/redevelopment/baseline-v1/governance/01_REQUIREMENTS_TRACEABILITY_MATRIX.md`, `05_DEVELOPMENT_GOVERNANCE_AND_QUALITY_GATES.md` in the same directory |

## Critical Business Invariants

- Organization and Production scope apply to reads, writes, joins, files, search,
  exports, background tasks, and agent capabilities. Central server authorization
  uses permissions, not role display names. UI capability checks are not security.
- Roles include Owner, Administrator, Member, Viewer and custom permission mappings.
  Permission sets differ by module. For example, Project Library Viewer/guest
  defaults have no global Library browsing permission; do not generalize the
  screenplay module's read-only defaults to all modules. Refresh `docs/RBAC.md`.
- Permanent Scene IDs survive string scene-number changes (`12A`, `A12`, `12.1`).
  Imported source and canonical ScriptRevision content remain immutable. Ambiguous
  reconciliation leaves the previous current revision active pending human review.
- Domain writes and outbox events commit atomically. Worker retries must not
  duplicate domain writes, notifications, asset versions, or external effects.
- AI is optional. Suggestions do not become canonical data without the appropriate
  human approval and normal domain permissions/concurrency checks. Manual flows
  remain usable when AI is disabled, unavailable, or over quota.
- Library asset identity survives immutable file-version changes. Follow-current
  and pinned usages differ deliberately. Trash blocks serving; purge is privileged
  and constrained by usages/ownership; rights visibility is a separate permission.
- Required malware scanning fails closed; `disabled` or optional fallback records
  `unscanned`, not `clean`. Originals are not served while required scanning blocks.
- Browser mutations require session cookies plus CSRF. Native bearer sessions use
  their own API contract; test them separately rather than transplanting cookies.

## Delivered-Surface Discovery

The snapshot contains controllers for identity, organizations/productions, roles,
scripts/scenes, Breakdown, Library, Work, shot planning/Designer/review/portability,
AI providers, agent plans/platform, and MCP. Routes include account settings,
organization search/admin, production script/revision/reconciliation, scene
Breakdown, Library, Work, and exports. Discover actual endpoints and module routes
from the candidate; file existence alone does not prove end-to-end completion.

The roadmap includes scheduling, budgets, production/post operations, delivery,
and enterprise controls. Do not assume these are fully implemented. Mark absent
out-of-release roadmap functions as out of scope; if a signed release requirement
promises them, their absence is a requirement gap instead. Billing/payments are
not established by this snapshot and must not be invented as existing features.

## Root Toolchain and Baseline Commands

Snapshot requires Node.js >=22 and pins `pnpm@10.34.5`. Verify lockfile, Corepack,
CI Node version, scripts, and workspace filters before running anything.

```sh
corepack pnpm format:check
corepack pnpm lint
corepack pnpm typecheck
corepack pnpm test
corepack pnpm build
corepack pnpm check:architecture
corepack pnpm check:css-vars
corepack pnpm assets:check
corepack pnpm assets:extended:check
corepack pnpm assets:extended:test
corepack pnpm test:release:source
corepack pnpm check:release:policy
```

These are verified script names, not execution results or a guaranteed complete
CI reproduction. Some build shared packages or write build artifacts. Use
`format:check`, not the mutating `format` command, for an audit. Avoid root `clean`
or automatic source rewrites. Read the current scripts and CI setup first.

`corepack pnpm test:db`, `test:migrations:release`, `db:migrate`, and `db:seed:uat`
are real root scripts but can mutate databases. The README says opt-in integration
suites migrate/truncate a disposable database. A test-name guard is not sufficient:
verify host, database identity, credentials, storage, and isolation explicitly.
Do not run seeds/migrations or start Compose as a side effect of static review.

## Verified CI and Release Caveats

At the inspected SHA, development PR/push checks route through
`scripts/development-ci.mjs`, which explicitly reports `publicReleaseReady: false`.
Development green does not mean the full root or release suites passed. Release
suite authority is `scripts/release/required-suites.json`; release control authority
is `scripts/release/security-policy.json`, not an ad hoc command list.

**Publication is explicitly disabled** in that policy at the snapshot. Trust
public key/controller/builder fields are unset, and R3/R4/R6/R7 and native evidence
are among unresolved activation requirements. Re-read the current policy and
associated evidence; no amount of local testing grants permission to turn it on.
Server/desktop release workflows validate; promotion admits, it does not imply a
working enabled publication path. Do not label public release ready from green CI.

Ordinary web browser command verified in `apps/web/package.json`:
`corepack pnpm --filter @slatedog/web test:e2e`. Its default Playwright config
starts the full dev stack unless `PLAYWRIGHT_EXTERNAL_SERVER=true`; non-CI reuse
can attach to an existing server. Review the selected specs before running, since
historical drivers may rely on frozen IDs or write under repository docs.

The distinct release browser smoke in `scripts/release/playwright.config.mjs`
uses one Chromium worker, zero retries, no server reuse, and only
`scripts/release/browser-regression.spec.mjs`. Canonical suite sequence:

```sh
pnpm packages:build
pnpm db:seed:uat
pnpm --filter @slatedog/web exec playwright test --config=../../scripts/release/playwright.config.mjs --reporter=json
```

This is a side-effecting sequence, not safe static preflight. The suite declares
`RUN_UX_UAT_E2E=true`, `UAT_SEED_CONFIRM=meher-flow-uat`, and
`NEXT_PUBLIC_API_URL=http://localhost:4000`. The config also requires `CI=true`
and `LOCAL_STORAGE_PATH` matching `/tmp/meher-flow-synthetic-[a-z0-9-]+`.
Database, browser installation, ports, and synthetic storage still need explicit
verification. Do not set these guard values merely to bypass a refusal.

Release suites explicitly enable individual storyboard API/worker integration
flags and require machine-readable reporters. A skipped suite or zero discovered
tests is not success. The ordinary API integration script also does not replace
`corepack pnpm --filter @slatedog/api test:sd11:integration` for Shot Review.
Read manifests/canonical suite lists for the exact current flags and coverage.

Release validation includes locked dependency install, scanners, OCI/container
smoke and source parity; install can run permitted lifecycle scripts. The canonical
asset suite includes the mutating `assets:sync`, unlike a read-only asset check.
Use an approved isolated checkout and verify generated changes rather than
running the release matrix indiscriminately in a user's working tree.

Current frozen recovery guidance expects zero pending migrations, writers fenced
during preparation, and a distinct human activation decision. Recovery restores
matching DB/media/config/roles/keys with compatible image digests into an approved
target; it is not old images against a newer schema. Refresh
`docs/operations/SELF_HOSTED_RECOVERY.md`, `DISTRIBUTION_AND_INSTALLATION.md`,
and the release-readiness register before making an operational recommendation.
