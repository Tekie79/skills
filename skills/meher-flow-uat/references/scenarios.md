# Meher Flow Business UAT Charters

Select only delivered capabilities or explicit signed candidate requirements. Use synthetic names like Film A, EP01 and Character A. Replace technical instructions with understandable tasks in facilitator handouts; the expected outcomes below are for evaluation, not participant coaching.

| ID and persona | Participant-facing business goal | Expected outcome for observer | Negative/interruption |
| --- | --- | --- | --- |
| MF-UAT-01 indie producer | Start a short film production and invite a coordinator with the right access | Appropriate template, production metadata, invitation and role-specific view | Incorrect invite/expired link; unrelated production cannot be opened |
| MF-UAT-02 coordinator | Import a screenplay, correct a mistaken scene boundary and continue editing | Preserved original/current revision, corrected Scene, readable error/recovery | Unsupported PDF, ambiguous revision and reload |
| MF-UAT-03 script supervisor | Find a character called by a nickname and assign the same prop throughout relevant scenes | One canonical Character/Element, linked occurrences, distinct scene usage details | False alias match, deleted/moved line, duplicate assignment attempt |
| MF-UAT-04 1st AD | Schedule scenes across shoot days, move a scene and see effects on cast and location | Correct Stripboard, availability/DOOD, conflict feedback, draft/version state | Time-zone/day boundary, concurrent edits and rollback to a draft |
| MF-UAT-05 production coordinator | Prepare a call sheet from an approved day, revise it and see who confirmed | Correct calls/location/notes, revision history and sandbox confirmation state | Missing crew data, bounce/expiry; no live send |
| MF-UAT-06 director/DP | Build a top-down set, place character, camera and light, plan two Shots | Intuitive creation and selection; no manual binding/rig hunt; saved plan reopens | Accidental Scene vs Shot edit, undo/redo, changing tool tabs |
| MF-UAT-07 director/editor | Check coverage, choose a short interval and view planned storyboard | Other-shot coverage distinguishable from fully uncovered gaps; viewport stable; only selected range plays | Overlapping/adjacent Shots, gaps, selecting an alternate camera |
| MF-UAT-08 department head | Find a reusable prop/reference asset, attach it and work with approved version | Correct asset rights, preview, current vs pinned use and return to scene | Outdated/trashed version or denied rights |
| MF-UAT-09 post supervisor | Review edit/VFX/sound/color tasks and approve a version if released | Correct scene/shot/version association, notes/approval and QC follow-up | Outdated timecode, unauthorized approval, missing media |
| MF-UAT-10 client guest | Open only assigned approval/review/call-sheet context | No internal finance, personnel, producer notes or unrelated project access | Revoked, expired and forwarded guest link |
| MF-UAT-11 creator/solo producer | Create a short-form content project, track review and required variants | Appropriate lightweight template/terminology without film-only workflow burden | No active AI provider or external storage connection |
| MF-UAT-12 filmmaker on tablet/mobile | Continue an existing plan or call-sheet check at supported width and input modality | Find key actions, readable layout, accessible interactions, accurate save state | Network interruption or session expiry; offline editing only if supported |

## End-to-end showcase

A producer can create Film A, import a revised episode, reuse scene elements, plan and schedule a shooting day, publish an approved sandbox call sheet, and connect shot coverage to storyboard and assets. After refresh/switching devices (supported platforms only), the identity and current versions remain correct. A guest sees only explicitly shared resources.

Use this journey for human UAT **only after all constituent functions are delivered**. Otherwise test smaller implemented segments and record dependencies as NOT_RUN or deferred.

## What to observe without coaching

- Can a first-time filmmaker identify the next action without knowing database terms?
- Does the current active project/scene/shot/schedule revision remain obvious?
- Can a user finish with accessible keyboard/touch methods and understandable controls?
- Are errors recoverable without losing work, and are save/publish/approval states truthful?
- Do nontechnical users understand change consequences across scripts, schedules and shots?
- Are public demo and production-private data clearly separated?

Do not count screenshots of empty states as successful task completion. Capture errors, workarounds and actual duration only when observed, never invented.
