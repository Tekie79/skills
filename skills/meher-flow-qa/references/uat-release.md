# UAT and Release Gates

## Two Separate Decisions

Distinguish feature quality/UAT readiness from authorization and readiness for
public distribution. Read current governance, `scripts/release/required-suites.json`,
`scripts/release/security-policy.json`, release-readiness registers, and relevant
workflows at the candidate SHA before interpreting CI. Never substitute this
skill's generic checklist for stricter project policy.

At the skill's inspected SHA, publication is disabled by policy, owner trust
fields are unset, and development CI explicitly is not release qualification.
If those facts persist, public publication is **NO-GO**, even if a feature looks
ready for UAT. Do not change policy, dispatch workflows or manufacture trust
receipts to make the conclusion green. Report missing verification separately
from a proven application defect.

## Business UAT

Map each signed requirement to observable outcomes and a real accountable
acceptance owner. Suggested synthetic personas are production Owner/Admin,
coordinator/Member, read-only Viewer/guest, custom-permission user, and a second
organization's unrelated user. Resolve actual permissions per module; do not
assume role names alone determine capabilities.

| Charter | Acceptance outcomes |
| --- | --- |
| Access and onboarding | Register/verify/invite/login; find/create the correct production; denied users cannot access another tenant; sign-out/reset works |
| Screenplay workflow | Import supported source, see processing, review ambiguous matches, preserve original/current history and stable Scene links |
| Creative planning | Authorized manual Breakdown and release-scoped shots/storyboard work; correct save, refresh, review and export results |
| Project Library | Upload/find/version/reuse assets, correct rights visibility and pinning, safe errors, trash/restore/guarded purge in disposable data |
| Collaboration and recovery | Two users edit concurrently; useful conflict/error feedback; no false saved state; background failures can be retried safely |
| Optional AI | Disable AI and complete manual work; enabled sandbox produces reviewable proposals; reject/accept behaves with explicit permissions |
| Devices and accessibility | Primary outcomes on supported desktop/mobile/PWA/native surfaces with keyboard/assistive technology as required |

Each case must state role/tenant, data, preconditions, steps, expected business
outcome, actual result, evidence, status, issue IDs, tester/date and acceptance
owner. Avoid generic "works as expected." Include realistic errors and recovery,
not only a guided happy path. Separate usability friction from requirement failure.

Where asked to save application UAT evidence, use the project's convention
`docs/uat/<milestone>/<date>/` inside the target repository with authorization;
do not write there automatically during skill development. Store redacted logs,
issue references and actual sign-off. AI-generated scenarios or simulated sessions
are not product-owner acceptance. Missing human approval remains "not obtained."

## Release Evidence Matrix

| Gate | Minimum evidence |
| --- | --- |
| Scope and traceability | Accepted requirements, exact SHA/base, changed surfaces, canonical entities/permissions/events, exclusions |
| Candidate integrity | Exact immutable artifacts/digests, supported platforms, reproducible build and source parity; no dirty-worktree substitution |
| Engineering | Required format/root lint/lint coverage/types/architecture/CSS/assets/build/unit results, not only maintained-source development checks |
| DB and APIs | Real PostgreSQL/API/worker integrations, tenant-isolation negatives, schema/contract and clean/upgrade/recovery evidence required by current release policy |
| Business regressions | Critical E2E and current storyboard/Shot Review suites as applicable; missing flags/zero tests/skips are not passed coverage |
| UX and compatibility | Required browser/device/visual/accessibility/print/PWA/native evidence; release Chromium smoke cannot certify all platforms |
| Security/distribution | Fresh dependency/container/secret/workflow scans, license/asset redistribution rights, SBOM/provenance/signatures/trust and required image/platform set |
| Performance | Approved SLOs/budgets, representative load/profile, no unaccepted regression; document applicability and evidence gaps |
| Operations | Approved installer/Compose smoke, observability, verified backup plus isolated restore, RPO/RTO, compatible application/schema recovery |
| UAT and authority | Recorded owner execution/sign-off, permitted waivers, current policy enabled/admission valid and separate deployment authority |

The inspected security policy requires images `api`, `worker`, `web`,
`recovery-tools` on `linux/amd64` and `linux/arm64`; also visual-platform,
synthetic-recovery, R3/R4/R6/R7, and native Linux/Windows checks. Its scan freshness
is 24 hours and approval freshness 8 hours. Refresh those values, digests, run IDs,
attestations, signers and current candidate binding rather than trusting old
screenshots or prose. Do not invent meanings or receipt formats for named R-gates;
read their canonical release-readiness definitions.

`release-validate.yml` performs exact-SHA admitted validation under protected
environment controls; server/desktop workflows call validation and promotion
performs admission. `scripts/release/run-matrix.mjs` rejects failed, cancelled,
missing or skipped mandatory validation. Local output is not a substitute for
required GitHub-enforced provenance, approvals or protected branch/environment
settings. Verify these live only with appropriate read access.

## Decision Algorithm

1. Set decision scope: feature UAT readiness, staging candidate, or public release.
   Record mandatory gates from current project policy and approved acceptance plan.
2. If a Blocker/security/data-integrity failure exists, or a known mandatory gate
   fails, or public publication policy forbids the requested action: **NO-GO**.
3. An unresolved High finding also means **NO-GO**, even if other evidence is
   missing, unless it already has a policy-permitted, accountable owner's explicit
   deferral with rationale, mitigation, expiry and retest date. Security/data-integrity
   issues and mandatory policy gate failures cannot use this deferral. An absent
   or merely proposed waiver is not approval.
4. Otherwise if a mandatory gate is `BLOCKED`, `NOT_RUN`, missing, flaky without
   equivalent accepted evidence, stale/mismatched, or unsigned where signatures
   are required: **INSUFFICIENT EVIDENCE** (release held). Missing UAT approval
   is included here; do not manufacture it or turn it into a software defect.
5. With all mandatory applicable gates passed, required approvals present and only
   explicitly accepted residual risk, recommend **CONDITIONAL GO** if a High has a
   valid permitted deferral; otherwise **GO**. Non-applicability must be justified
   and accepted, not used to hide skipped work. Record waived Highs prominently.

No aggregate score can override this order. A dependency warning is not automatically
a Blocker; assess severity/reachability and the actual policy threshold. A high
test coverage number does not waive a tenant leak. An agent's recommendation is
not permission to activate, release, deploy, or approve risk on a person's behalf.

## Rollout, Monitoring, and Recovery

Prepare, do not execute unless requested: staged/canary rollout with immutable
artifact IDs, explicit owner/approver, synthetic smoke, critical telemetry,
capacity/error/queue-lag thresholds, observation window and halt criteria.
Check logs, request IDs, metrics, health/readiness and user-safe errors without
exposing tenant content or secrets. Include support/incident ownership.

Define application and schema compatibility separately. Follow the candidate's
approved fresh-install vs upgrade/recovery path, including matching DB and media,
configuration/roles/keys, isolated verified restore, writer fencing and exact
candidate rehearsal. The frozen snapshot expects zero pending migrations;
unplanned migrations are not a routine deployment step. Never assume `migrate:down`,
volume deletion or old-image fallback is safe. Activation and writer resumption
require their own human authorization.

After an authorized rollout, recheck critical journeys/tenant protection and
monitor against pre-agreed limits; rollback/restore only under the approved plan.
Report final evidence and remaining risk. Do not promise "zero bugs" or that a
limited QA pass proves compliance, scalability or universal compatibility.
