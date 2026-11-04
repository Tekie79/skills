# Meher Flow Module QA Charters

This is a **candidate-dependent coverage menu**, not a report of completed tests. Select cases only for delivered functions and affected contracts, with explicit exclusions. Test against synthetic film/episode/creator content; no real production scripts, actors, or guest email delivery.

| Case family | Feature and expected result | Essential negative / boundary |
| --- | --- | --- |
| MF-CORE-01 | Organization/project membership, role-aware nav, permission-filtered search and direct API; no cross-tenant content | Replace Organization A / Production A identifiers with B in path, body, cursor, file link, jobs and export; session after revocation |
| MF-CORE-02 | Stable canonical IDs and links across renumber, archive/restore, import/export, navigation and publish | Stale recordVersion, concurrent edits, retry and duplicate create; no false Saved state |
| MF-SCRIPT-01 | Standard FDX/text-PDF/source import, scene preview/correction, immutable source, current revision and stable Scene ID | Bad formatting, missing headings, 20 MB boundary only if current policy confirms it, conflicting source, cancel/failure recovery |
| MF-SCRIPT-02 | Script revisions reflect exact changed/moved/missing/unchanged/manual matches and downstream impact | Ambiguous match cannot silently overwrite or create duplicate canonical Scenes |
| MF-BREAK-01 | Select script text or use context menu to assign reusable canonical Breakdown element with per-scene details/department | Alias/nickname for a Character finds intended occurrences, avoids false matches and repeated assignment; multi-scene reuse preserves scoped fields |
| MF-BREAK-02 | Collapsible Script and full-width Breakdown sheet, notes/assets/links tabs, printing without script when specified | Selection persists on collapse; editing and right-click menu don't lose unsaved state or duplicate elements |
| MF-LIB-01 | Upload/search/version/rights/preview/reuse/pin/restore as actually delivered | Cross-tenant download, MIME spoof, scanners pending/error, stale links, guarded purge and immutable versions |
| MF-M4-01 | Stripboard, shoot days, boneyard, scheduling constraints, calendar/DOOD, versions and conflict explanations | Change scene/availability/location/time zone/DST; no stale call-sheet publish or duplicate scene placement; simultaneous editors |
| MF-M4-02 | Call sheet accurately inherits approved schedule, cast, crew, location, dates/calls; preview/export and revision rules | Unauthorized guest/private finance access; revision rebroadcast/ack history; no real provider send from test |
| MF-M4-03 | Context drawer/History & options opens/closes by button, outside click, Escape, navigation, focus restoration | No duplicated global Search/Account/Organization controls; nested-dialog Escape, mobile width and keyboard |
| MF-SD-01 | Scene vs current Shot editing scope is explicit; actor placement/Character linking and reset retain canonical identity | Changing tabs doesn't clear selection/pan/zoom; viewing a Shot does not create an override; no duplicate character binding |
| MF-SD-02 | Camera/light placement and adjustment use an intuitive action while retaining underlying rig/setup semantics | Add object vs actual planning device distinction; an unrelated decorative SVG never becomes registered equipment |
| MF-SD-03 | Shot coverage shows this camera's intervals, other cameras' intervals and fully uncovered gaps accurately | Grey for other-shot coverage, red only for no-shot gaps, compact no-congestion layout; overlapping/disjoint ranges and inactive Shots |
| MF-SD-04 | Selecting one exact coverage interval keeps timeline horizontal position and scoped playback; scrubbing is separate from selection | Selecting a short range never forces full-scene playback; zoom/scroll remain stable; adjacent ranges not merged |
| MF-SD-05 | Design tool previews, snapping, floor paths before completion, fully joined/smoothed wall corners, consistent defaults | Undo/redo, double-click finish, Esc/cancel, invalid geometry, browser resizing, zoom and persistence; road/lane builder if implemented |
| MF-SD-06 | Correct asset category/subtype icons, manifest, Simple/Advanced SVG identity, stable pivots and footprints | Reject missing or active-content SVG, broken render/export, duplicate IDs; don't replay unaffected large historical asset suite by default |
| MF-SD-07 | Animations, saved Shot plan, review/approval, storyboard capture and package/export preserve version and source links | Overridden Shot vs Scene state, timecode/rational fps, deleted reference, unauthorized review, failed export or restore |
| MF-AI-01 | AI proposal supports preview, accept/reject, optional provider connection; manual path remains fully available | Provider outage, rate limit, wrong schema, prompt injection, cross-tenant provider ID, revoked permission, no silent write |
| MF-POST-01 | If M7 exists: editorial/VFX/sound/color/review/QC/delivery preserve source scene/shot/version and approval state | Stale approval or timecode, access boundaries, missing media, version mismatch and export fidelity |
| MF-UX-01 | Light-first design, user-friendly icons with accessible labels, responsive/touch/keyboard, Amharic/Unicode and correct print | Drawer focus, state after refresh, animation reduced motion, zoom and screen reader alternatives |
| MF-OPS-01 | If shipped: worker/outbox, search/export, backups and supported self-hosted install/recovery are correct | Retry duplication, partial write, cancelled job, error state, leak via logs/caches and isolated restore consistency |

## Cross-workflow integrity scenario

Create an authorized synthetic episodic Production; import screenplay Scene 12A; identify one Character with two scripted aliases; reuse a prop in multiple scenes; revise/renumber the scene; place it on a Shoot Day; draft/publish the appropriate call sheet in a fake-send environment; link Shot Designer camera and storyboard; reference assets; export the project.

Expected: stable canonical IDs, only intentional new versions, no duplicated Elements/call recipients, accurate audit/outbox, permission-safe view, explicit downstream stale/impact markers and successful read/reopen. Run the portions implemented in the chosen candidate; mark missing dependencies instead of inventing success.

## Change-specific exclusions and protected tests

A local inspector restyle can be scoped to browser visual, focus, state and nearby animation controls; do not replay the 1,231-type asset library automatically. But a change to common SVG serialization, register/pivot metadata or export requires the affected manifest/corpus and linked workflow checks.

Changes to schedule versioning require cross-checking approved call sheet content. Changes to Scene revision or aliases require Breakdown, shot/source, schedule and post reference integrity. Permission changes require full affected direct-API denial matrix regardless of changed-file count. This selection is for feature QA; mandatory release matrix remains independent.
