# Security, Data Integrity, and Resilience

Use a risk-based OWASP ASVS/API Security checklist as guidance; do not claim a
penetration-test certification or regulatory compliance from this review. Verify
current contracts and approved scope before probing. No production scans, real
malware, credential attacks, or destructive failure injection by default.

## Authorization and Tenant Isolation

Create synthetic Organizations A/B, Productions A1/A2/B1, and accounts with Owner,
Administrator, Member, Viewer/guest and custom permissions. Include a user with
access to both tenants to detect accidental context reuse. Test direct endpoint
calls with cross-organization and same-organization/cross-production ID substitution
in paths, bodies, nested IDs, queries, cursors, imports and background payloads.

Cover list/detail/search/count/preview/download/export, mutation/bulk endpoints,
job polling, audit, rights/security diagnostics and agent/MCP capabilities. Verify
denial with no unauthorized domain mutation, job, or success audit event, and no
existence leakage or secret error detail. Preserve policy-defined security/denial
audit events with safe scoped identifiers and redacted content; correct denial
logging is not an unauthorized side effect.
Test revoked/changed memberships on existing sessions/caches. Central permission
mapping and composite FKs matter; hidden buttons and role names are not evidence.

## Identity, API, and Supply Chain

- Browser sessions: cookie HttpOnly/Secure/SameSite policy, HTTPS, CSRF cookie/header
  checks on mutations, logout/session expiry/rotation and cross-origin behavior.
  Native bearer lifecycle needs separate storage, expiry/revocation and connection
  profile checks; no tokens in URLs, logs or browser-readable inappropriate stores.
- Verification/reset/invitation: expiry, one-time consumption, account enumeration,
  replay, race conditions, existing/new account flows and access after removal.
  Use Mailpit or an authorized sandbox, never unsolicited mail to real recipients.
- DTO validation, unknown/privileged fields, mass assignment, injection/XSS,
  parameterized SQL, rate/resource limits, CORS/CSP and error envelope redaction.
  Verify public diagnostics/production configuration boundaries and secret handling.
- For URL fetchers, imports, provider endpoints and integrations present in scope,
  test SSRF/egress allowlists, redirects, private/link-local/metadata targets and
  DNS rebinding protections using controlled fixtures, not live internal probes.
  Check unsafe redirects, webhook authenticity/replay and client deep-link trust
  only where such capabilities actually exist in the candidate.
- Lockfile/reproducible install, direct/transitive vulnerabilities, licenses, secret
  scanning, artifact/SBOM/provenance/signatures where configured. Interpret audit
  findings by exploitability/reachability and policy, not only raw counts.
  Query external advisory services only when network/data-sharing scope allows it.

Include privacy/data minimization, retention/deletion/export, consent where relevant,
support access and auditability against the project's applicable obligations.
Report gaps for legal/security owners; do not assert GDPR or other legal compliance
without an authorized specialist assessment and supporting evidence.

## File and Content Safety

Test extension/MIME/byte-signature disagreement, malformed parsers, traversal,
Unicode names, size/time/page/dimension limits, duplicate content, decompression
and XML resource exhaustion, content-disposition and scoped storage keys. Use
benign synthetic exploit fixtures and sandbox parsers; never evaluate uploaded
scripts. Test revoked access and stale signed URLs/caches for originals/derivatives.

Snapshot screenplay default limit is 20 MB; Library defaults differ by type
(images 2 MB, audio 5 MB, documents/other 25 MB, video 100 MB). Refresh actual
configuration and byte-unit semantics before boundary tests. Image-only screenplay
PDF rejection is intentional; Library `no_text` is not a failed OCR feature.

Library SVG active content/external references must be rejected and accepted SVG
originals must not be rendered inline. Required malware policy must block pending,
error, unavailable and exhausted-retry content; derivatives and activation/linking
cannot bypass it. Optional/disabled policies must retain truthful `unscanned` state.
Do not use live malware; a scanner stub or specifically authorized standard benign
test fixture suffices for the intended policy test.

## Canonical Data and Concurrency

- Stable Scene ID and immutable source/canonical revision across edits, renumbering,
  ambiguous reconciliation, restore, history and supported import/export round trips.
- Stale `recordVersion`/optimistic concurrency rejects instead of silently overwriting;
  concurrent approve/edit/import/delete/retry follows defined state transitions.
- Transactional outbox/audit exactly reflects committed domain changes; rollback
  does not leave an accepted UI success or orphaned source/job as authoritative.
- Referential and tenant constraints under concurrent writes; no duplicated canonical
  assets/elements; version-pinned vs follow-current usages remain distinct.
- Money/decimal, time zones/DST, ordering and timecode/rational-frame-rate fidelity
  when those release surfaces are in scope. Do not invent financial modules.
- Lifecycle: soft deletion/restore/retention, permissions, live usages, tombstones,
  storage ownership and typed purge confirmation. Never test real permanent purge
  outside an explicitly approved disposable fixture.

## AI, MCP, and Agent Approval

Use fake providers by default. Cover disabled/unavailable/quota/rate-limit/schema
failure, prompt injection in screenplay/files, unsupported output IDs, source-range
validation, cross-tenant/provider credential isolation, and safe error/log redaction.
Only authorized users can accept/map/merge suggestions through canonical services.
Approval must not be inferred from the model's text or a tool response.

Test replay/expiry/rejection/revocation of approval, queued capability-version drift,
idempotency, run/task scope, cooperative cancellation, and resumed execution after
a worker lease expires. Changes in authorization between submission and execution
must not grant stale privileges. HTTP and STDIO MCP project the same allowed
capabilities without bypassing authorization or importing database infrastructure.

Snapshot agent batches cap 25 tasks, 64 KiB per child input, 512 KiB total input,
64 KiB projected child result, five sequential items per worker pass, five-minute
recovery lease. Refresh before boundary tests. A cancelled batch may retain earlier
committed mutations and become partially completed: never assert global rollback.
Do not log validated arguments or provider credentials as test evidence.

## Reliability and Recovery

With authorization, inject bounded DB/storage/email/scanner/provider timeouts and
worker restarts around claim, pre-commit, post-commit and acknowledgement. Check
safe retries/backoff/jitter, stale lease ownership, dead letters, idempotent external
effects, bounded queue lag and deterministic terminal states. Do not assume an
exactly-once transport; verify at-least-once delivery plus idempotent effects.

Exercise offline/reconnect and PWA updates without asserting unsupported offline
sync. Private responses/tokens must not persist in inappropriate browser/service
worker/CDN caches or leak to the next signed-in user. Verify permissions after
resume and behavior when client/server schema versions differ.

Migration readiness includes clean install and upgrade from supported release,
constraints/backfills, lock duration, compatibility during rolling updates and
data-preserving recovery. Never run `migrate:down` simply because it exists.

Verify a write-consistent backup/restore of PostgreSQL **and** associated object/
local storage, plus encryption/configuration material needed for recovery under
approved secret procedures. Test restoration into an isolated target, canonical
relationships, file checksums/access, jobs and application health. Measure actual
RPO/RTO against approved objectives. A green backup job is not restore evidence,
and an application rollback alone cannot undo a destructive schema migration.
