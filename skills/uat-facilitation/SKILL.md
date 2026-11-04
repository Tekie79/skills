---
name: uat-facilitation
description: "Prepare and facilitate business-oriented user acceptance testing for any product: real-user scenarios, persona charters, test sessions, usability findings, evidence logs and sign-off records. Use when users ask for UAT plans, scripts, acceptance decisions or pilot feedback. For Meher Flow-specific UAT prefer meher-flow-uat. Not an engineering regression suite and never signs for the product owner."
---
# UAT Facilitation

User Acceptance Testing asks whether intended people can accomplish their real work in the product, under the approved requirements. It is distinct from engineering QA and from publication/release authorization.

## Scope

Obtain the release candidate identifier and environment, current requirements, supported capabilities, target users, agreed scenarios, business risks, expected outcome and accountable approver. Do not test roadmap-only features as if shipped. Distinguish scripted UAT, exploratory observation and pilot feedback. Do not use developer shortcuts or seed hidden navigation hints for the participant.

## Build realistic scenarios

For each scenario provide: business objective, persona and permission, starting state, synthetic input data, self-contained user task (not click-by-click coaching), expected observable outcome, allowed completion criteria, negative/interruptions, evaluator observations and artifact capture. Include novice/expert perspectives when relevant. Test a whole journey and context transitions, not just isolated fields.

Include graceful failures: offline/error recovery where supported, stale records, ambiguous terminology, empty data, denied access and changed requirements. Check whether participants can find the action, understand consequences, recover without data loss, and complete efficiently. Separate functional acceptance failure from usability friction and feature requests.

## Run and document

- Use an approved sandbox with synthetic accounts/projects and avoid real personal data, messages, paid provider use or production changes.
- Run a short pilot of the script for ambiguity; then record actual participant actions and task completion without inventing observations.
- A facilitator or automation may prepare, monitor and gather evidence. It cannot impersonate human product-owner sign-off.
- Record candidate SHA/build, task, participant role (not unnecessary identifiers), actual result, defects, severity, evidence, date and accountable decision owner.
- When user testing cannot occur, supply a ready-to-run UAT pack and mark actual execution NOT_RUN; do not represent proposed scenarios as accepted results.

## Outcome

Classify scenario as PASS, FAIL, BLOCKED, NOT_RUN, or NOT_APPLICABLE. PASS requires observed business outcome and attributable evidence. Track workarounds, assistance needed, usability issues, blocked requirements, and residual risk. Owner sign-off is a separate recorded decision: approved, rejected, or NOT_OBTAINED; never self-approve. Do not treat automated Playwright smoke as completed human UAT.

Use the [UAT session template](assets/uat-session.md), and check [behavior evaluations](references/evaluations.md) when maintaining this skill.
