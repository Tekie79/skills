---
name: release-evidence-review
description: "Assess software release candidates for go/no-go readiness from exact-artifact QA, security, performance, operational, compliance-policy and human UAT evidence across projects. Use for release gates, production-readiness evidence, waivers, rollback planning and controlled promotion recommendations. Not a deployment tool; project-specific release policy always governs."
---
# Release Evidence Review

Decide whether the exact candidate has sufficient verified evidence for its intended release scope. Distinguish a feature handoff, staging UAT, and a public production release; they have different mandatory gates.

## Prepare candidate and policy

Record repository SHA, base, artifact digest/platform, environment, build provenance, supported upgrade path, release scope, required checks, gate owners, UAT approver and human release authority. Read live, versioned project-specific requirements, CI gate definitions and release policy at the candidate SHA. This generic skill never overrides stricter repository policy.

An unrun or stale test, an unrelated green run or a screenshot from another SHA does not satisfy a mandatory gate. A roadmap feature not in the release is not automatically a failure; a promised release requirement missing from the candidate is.

## Build gate ledger

Cover if applicable: source and artifact parity; format/lint/types/build/unit; API/DB/worker/schema migrations; tenant/auth/security negatives; business E2E; browser/device/accessibility; performance and scale; secrets/dependencies/licenses/provenance; backup and isolated restore; observability and rollback; human UAT; publication controls. Record direct vs supplied evidence and checked source, test counts, skips, candidate binding, freshness and ownership.

Status per gate: PASS, FAIL, BLOCKED, NOT_RUN or NOT_APPLICABLE (with approved rationale). [Evidence template](assets/release-ledger.md) defines the ledger.

## Decision precedence

1. A confirmed Blocker/security/data-integrity defect, failed mandatory gate, prohibited publication state or unwaived High primary-workflow defect means NO-GO.
2. Otherwise, missing/stale/unbound/blocked mandatory evidence or missing required sign-off means INSUFFICIENT EVIDENCE (hold).
3. With all mandatory applicable gates genuinely passed and approvals obtained, a noncritical High deferral permitted by actual policy and approved with owner, expiry, mitigation and retest may produce CONDITIONAL GO.
4. Otherwise, after all gates and approvals, recommend GO.

Never invent waivers or treat a proposed waiver as approved. Required security/tenant/integrity gates cannot be excused by arbitrary product-owner preference. A recommendation is not permission to push, merge, promote, publish, send messages, or deploy.

## Rollout and incident preparation

Describe (do not execute by default) staged rollout, operational owner, observed SLOs, alert thresholds, rollback stop conditions, backup/restore rehearsal, schema/app compatibility and post-release smoke. Do not advise a blind rollback to older application code against an incompatible newer database.

If the environment is unavailable, produce a gap-based held decision. Use [evaluation prompts](references/evaluations.md) when testing the skill's behavior.
