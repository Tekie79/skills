# Meher Flow Filmmaker UAT Sessions

## Audience and ground rules
UAT must be performed by actual authorized users or human proxies who know the relevant role: director, 1st AD, production coordinator, producer, script supervisor, editor/post supervisor and guest reviewer. The agent may prepare, observe and summarize but **cannot sign UAT** or replace the participant with browser automation.

Do not instruct participants how to operate the UI unless testing guided-mode documentation. Provide the business goal and realistic synthetic context; record steps the participant tried, confusion, accessibility issues, task completion, elapsed time only if measured, and suggestions separately. Default to sandbox production, fake outbound email and fake AI providers.

## Synthetic demonstration production
Use fictional “Harbor Light” (Organization A) and “Valley Studio” (Organization B). In A, create Production One and Production Two, Scene 12 (INT. STUDIO – NIGHT), Scene 13 (EXT. ROAD – DAY), characters Ana/A.J. (alias) and Luis, a camera, one wall/floor, a planning Shot and one synthetic reference asset. Reuse shared canonical Person/Element records where supported. Names, addresses and contacts must be fictional and non-deliverable. Do not depend on any real show data.

## Role-based business scenarios

| ID | Persona | Participant task (no UI hints) | Evidence of business success |
| --- | --- | --- | --- |
| UAT-01 | Producer | Start a production for an episodic shoot and invite a coordinator with limited access | Appropriate template/organization, correct member scope; unrelated organization stays inaccessible |
| UAT-02 | Script supervisor | Import a screenplay, correct a scene boundary and keep a trusted revision | Correct visible scene list, immutable previous version, no lost source/corrections after reload |
| UAT-03 | Coordinator | Identify every scene where Ana appears as “A.J.” and put her in the breakdown | One canonical Character, relevant verified occurrences, no duplicate or false unrelated matches |
| UAT-04 | Department head | Reuse one prop across scenes but change quantities in only one | Reused canonical Element while per-scene Details remain independent |
| UAT-05 | Director | Build a simple room and place an actor, camera and light | Immediate recognizable setup without technical rig/binding detours; save/reload returns matching layout |
| UAT-06 | Director/DP | Find a planned time range with no shot coverage and make a covering Shot | Red only on genuinely uncovered scene interval; other-camera coverage neutral gray; selected interval and ruler remain stable |
| UAT-07 | Director | Create an alternate angle, adjust blocking for only that Shot and preview its range | Scene layout unchanged; Shot-only overrides correct; playback doesn't force entire-scene selection |
| UAT-08 | Director | Draw a floor and two connected walls, then round a corner | Preview visible before completion, continuous corners, intentional smoothing and successful undo |
| UAT-09 | 1st AD | Re-plan two shoot days and identify an unavailable cast member | Correct stripboard/day plan/DOOD conflict and version state; no unapproved publication |
| UAT-10 | Production coordinator | Prepare a revised call sheet and request acknowledgements | Canonical schedule/crew fields correct; fake-channel deliveries, confirmations and version history accurate |
| UAT-11 | Editor/post supervisor | Attach notes to the correct source Shot and approved version | Version-specific notes; new edit does not inherit stale approval as current |
| UAT-12 | Guest reviewer | Review assigned media or plan without accessing unrelated materials | Scoped visibility, ability to perform allowed task and denial on direct URL/API to private content |
| UAT-13 | Producer | Export essential production data and reopen an archived project | Usable, accurate export with stable IDs; archive not destructive; allowed restore |
| UAT-14 | Any user | Continue a partially edited task after network interruption and session expiry | No false Saved notification; recoverable changes or clear conflict/error as specified |
| UAT-15 | Director | Use key Shot Designer tasks on narrow/touch and keyboard input | Essential actions discoverable and operable without hover/right-click-only dependence |

Only run scenarios **available and included in the candidate's agreed scope**. UAT-09/10 and post/AI/3D extensions may be planned but not release-scoped. Never mark an unimplemented future milestone FAIL merely for not existing; mark NOT_APPLICABLE with rationale outside scope.

## Facilitation script
1. Verify build/SHA, synthetic environment and scope; have owner approve scenario and roles.
2. Give the participant the **task**, not click-by-click instructions. Ask them to think aloud; observer logs facts rather than guiding.
3. Record task completion, errors, recovery, time if measured, assistance and UX friction. Save redacted screenshot/video with case ID, device/theme and timestamp.
4. Reconcile business outcome with persistent API/DB evidence where authorized. Don't mistake a toast or screenshot for durable state.
5. Triage: Blocker for tenant leak/corruption, High for blocked core task, Medium for workaround/repeated friction, Low for non-blocking polish; verify against project classification.
6. Record actual tester and accountable owner accept/reject/defer, issue ID, mitigation, target retest and an approval timestamp. Absence of owner => **NOT OBTAINED**.

## UAT report questions
- Could a first-time indie filmmaker complete the primary action without a tutorial?
- Was the user forced to understand internal rigs, bindings, source revisions or permissions architecture?
- Did data persist and remain coherent through downstream views?
- Did UI reflect what the user intended rather than silently editing another Shot or production?
- Were errors and recovery intelligible? Did the UI avoid congestion as data grew?
- Can the user complete the same essential outcome on supported narrow/touch/keyboard surfaces?

Use [UAT session ledger](../assets/uat-session-ledger.md) to record actual evidence. A plan is never a passed UAT.
