---
name: uat-business-acceptance
description: "Design and facilitate user acceptance testing using realistic roles, production-like scenarios, observable business outcomes and human sign-off. Use for UAT plans, tester scripts, acceptance sessions and evidence review; not for replacing owners' approval with automated CI."
---

# Human Business UAT

## Objective
Prove that intended users can accomplish specified real-world work with the candidate, not merely that automated tests pass. UAT is role- and task-oriented, preferably observed on representative supported devices and a safe synthetic environment.

## Inputs and setup
Identify accepted requirement version, tested release/feature SHA or build, personas, business owner, UAT facilitator, environment, test data, capability flags, device support, accessibility needs, known issues, and explicit entry/exit criteria. Mark missing human acceptance owner or inaccessible UI; do not invent sign-off.

## Workflow
1. Translate accepted requirements into **job stories** with a clear actor, business starting state and finished outcome. Write instructions in user terminology, avoiding implementation hints that artificially improve usability scores.
2. Prepare synthetic but credible records. Include new and returning users, restricted guest, conflicting editor, error/recovery cases, cross-organization boundaries and realistic workload size where relevant.
3. Build a session script: scenario ID, scenario goal, role/account, data prerequisites, task shown to participant, allowed assistance, observable success, time/friction notes, accessibility/device, evidence and cleanup.
4. Separate **functional acceptance** from usability observations. Track discovery failures, excessive steps, wrong mental models, inaccessible actions, failed persistence and broken critical paths as distinct observations.
5. Capture tester, date, exact build, task outcome, screenshot/video/log reference (redacted), severity, issue link, retest and explicit accept/reject/defer by accountable humans.
6. Reconcile requirement gaps and approved deferrals; block acceptance for security, integrity and unapproved material failures. Automation may be referenced as supporting evidence but cannot impersonate a tester or owner.
7. Produce an owner-ready report with cases passed, failed, blocked, deferred, open defects, residual risks and the **actual** approval state.

## Output contract
Deliver UAT charter, script and result ledger. Use PASS only if the task was genuinely performed and observed. Missing participants or product owner => NOT_RUN / sign-off NOT OBTAINED. Clearly distinguish a proposed UAT plan from an executed session.

## Example
Task shown to a production coordinator: Move a scene to a different shoot day, check resulting cast/location conflict, review the draft call sheet and publish only after obtaining the right approval. Success requires the affected dependent views and persisted records to agree.

## Safety
Never send a real call sheet, alert real cast, delete shared media, spend provider credits or sign on behalf of an owner. Use approved synthetic data and controlled outbound channels. See [behavioral evaluations](references/evaluations.md).
