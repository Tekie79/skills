---
name: qa-security-resilience
description: "Assess software security, authorization, tenant isolation, file/AI integrations, data integrity, concurrency, backups and recovery with risk-based safe testing. Use for security and resilience QA; not as a penetration-test certificate or unrestricted production scan."
---

# Security, Integrity and Recovery QA

## Objective
Test reachable security and data-loss risks, distinguish reproducible findings from theoretical threats, and verify safe recovery behavior. Use project security policy and OWASP ASVS/API guidance as references; a checklist does not constitute certification.

## Inputs
Exact candidate and required policy, available interfaces and trust boundaries, role/permission model, tenant/project scope, data classification, architecture, secrets handling, isolation target, backups/recovery expectations and authorized probe intensity.

## Workflow
1. Draw a trust map: anonymous/authenticated/guest, organizations/projects, API, browser/native session, storage, worker/jobs, exports, webhooks, AI providers/MCP, external clients and logs.
2. Enumerate permission matrix and test direct access to list/detail/write/search/file/export/audit/background job endpoints; substitute cross-tenant and within-tenant cross-project IDs in URL/body/query/cursor. UI hiding is insufficient.
3. Probe authentication/session expiration, revocation, reset/invite replay, CSRF on cookie flows, native bearer boundaries, safe error redaction, rate/size limits, and stored/reflected content injection using synthetic payloads.
4. Verify data invariants: stable canonical IDs, version lineage, transaction plus outbox atomicity, optimistic concurrency, idempotent retries, restore/soft delete and no unauthorized success mutation. Read-only checks first.
5. Review unsafe input processing: MIME/signature mismatch, SVG active content, traversal, document/XML bombs, malicious AI instructions in documents, provider schema mismatch and secret isolation; use only safe bounded fixtures.
6. For resilience, define and run **only authorized** bounded failures: database/storage/provider outage, worker interruption around commit, lease expiry, duplicate webhooks and interrupted uploads. Distinguish graceful UI state from durable consistency.
7. Verify backup alongside associated media/config and isolated restore when expressly authorized; document actual RPO/RTO evidence, not presumed values.

## Output contract
Give scope and exclusions, threat/invariant matrix, observed reproduction or static hypothesis, severity, affected tenants/users, evidence, missing authorization, residual risk and retest. A confirmed cross-tenant leak or irreversible data loss is a release blocker. A safe denial audit entry is not itself an unauthorized mutation.

## Safety
Do not scan production, collect credentials, run real malware, manipulate other tenants, destroy shared data, restore over a live system or bypass provider limits. If target identity is uncertain, stop. See [behavioral evaluations](references/evaluations.md).
