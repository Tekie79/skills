# Meher Flow Source and Policy Baseline

This is an **inspected source snapshot**, not a green test report or current guaranteed implementation. Source: private GitHub repository Tekie79/SlateDog, develop at SHA 11ac64cec6462d1bbb1e4e09a5a4ac4ac151e408 (inspected 2026-11-03). Feature branches may contain newer/experimental work absent from develop. Resolve the chosen exact SHA before every QA assessment.

The user-facing product is **Meher Flow**; internal names @slatedog/* and repository SlateDog may be compatibility contracts.

## Architecture pointers to refresh

- Next.js/React/TypeScript web app: apps/web, Playwright config apps/web/playwright.config.ts.
- NestJS API: apps/api, versioned REST/OpenAPI.
- PostgreSQL: packages/database, ordered migrations.
- Worker: apps/worker, transactional outbox/leases/retries.
- Local/self-hosted storage abstractions; media and Library rights/scanner decisions.
- Desktop client: apps/client, Tauri architecture; bearer vs cookie/CSRF differences.
- AI/provider/MCP integrations: optional per capability; project and organization permissions.
- Documentation: docs/ARCHITECTURE.md, docs/DOMAIN_MODEL.md, docs/RBAC.md, docs/UI_DESIGN_SYSTEM.md, docs/THEME_SYSTEM.md.
- Governance: docs/redevelopment/baseline-v1/governance/01_REQUIREMENTS_TRACEABILITY_MATRIX.md and 05_DEVELOPMENT_GOVERNANCE_AND_QUALITY_GATES.md.
- Candidate release policy: scripts/release/required-suites.json, scripts/release/security-policy.json, scripts/release/run-matrix.mjs and .github/workflows/.

At inspected develop SHA, publicationEnabled is **false** in security-policy.json. Development CI and any focused feature tests are not public-release qualification. Refresh policy on the release candidate. Never modify publication settings, approvals, protected controls or trust records as a QA side effect.

## Observed root scripts (names, not execution evidence)

Node >=22, pnpm@10.34.5 in the inspected package.json; verify versions and current lockfile:

- Non-destructive intent, still inspect build artifacts before running: corepack pnpm format:check, lint, typecheck, test, build, check:architecture, check:css-vars, assets:check, assets:extended:check, assets:extended:test, test:release:source, check:release:policy.
- Browser E2E is defined in apps/web/package.json as corepack pnpm --filter @slatedog/web test:e2e. Its config may start services, reuse a server, write artifacts and depend on seeded databases; inspect first.
- Side-effecting and explicitly opt-in: corepack pnpm test:db, test:migrations:release, db:migrate, db:seed:uat, assets:sync. None is automatically safe because of its name.
- Source package uses @axe-core/playwright and @playwright/test. No claim is made that every suite is fully passing.

Release-specific suites, allowed flags, guard variables, artifact platform sets and policy gates are dynamic. Read canonical JSON and actual run records at the candidate before making any release claim. The UAT seed and release browser smoke in the snapshot were designed for disposable local environments; do not set guard variables to force a potentially unsafe run.

## Product baseline to trace

Meher Flow Product Requirements & Development Baseline v1.1 (2026-09-01) includes: canonical entities, M0 tenancy/RBAC, M2 script/version/import, M3 Breakdown/shot list/storyboard, M4 scheduling/call sheets, M5 budget, M6 production, M7 post, M8 delivery, M9 enterprise. These are scope direction, not verified delivery statuses. Test only delivered functions or signed candidate requirements.

Source checks should inspect the current implementation of authorized project workflows; do not silently copy a stale branch's selectors, test counts, asset totals, or UI decisions into current expectations.
