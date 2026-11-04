# Meher Flow Feature QA Charters

Use these as risk seeds and measurable **candidate-specific** acceptance tests, not as evidence that a feature is implemented. First discover the actual routes, source and approved feature specification at the target SHA. Feature names and future milestones cannot be used to claim release gaps unless they are within the accepted candidate scope.

Each suggested ID must be expanded to role/tenant, fixture, preconditions, execution steps, UI/API/DB oracle, teardown, severity, artifacts and owner. Include negative and failure outcomes for every primary path. Reference requirement IDs from the approved specification, not fabricated IDs.

## Platform, identity, permissions, events and export (M0/M1)

| ID | Risk-driven scenario | Observable oracle |
| --- | --- | --- |
| MF-CORE-01 | Create Organization A and B, create productions A1/A2/B1; switch and deep-link | Current context and server-side results are correctly scoped, including counts, search, files and export; no bleed after refresh |
| MF-CORE-02 | Add Person without user account; invite/revoke across productions | Person remains canonical, memberships scoped; revoked session/API cannot access private project; appropriate safe audit event |
| MF-CORE-03 | Concurrent update or stale version on a production record | Conflict surfaced; no false Saved state, lost update or duplicate outbox event |
| MF-CORE-04 | Change role while user is signed in; use direct API ID substitution | Central permissions enforced for list/detail/write/search/download/export regardless of hidden UI |
| MF-CORE-05 | Export a project, archive, unarchive, restore; retry export/job | Stable IDs/relationships preserved, output complete and access-scoped; no duplicate records |
| MF-CORE-06 | Fresh Docker/self-hosted install, supported upgrade and isolated recovery | Authorized test target starts, data/media/config restored consistently, no hidden dependence on cloud subscription |

## Script, import, revisions and canonical Scenes (M2/M2.5)

| ID | Scenario | Oracle |
| --- | --- | --- |
| MF-SCR-01 | Import valid FDX and supported text screenplay; manual scene correction | Immutable original, scene boundaries and source locations; authoritative revision only after permitted confirmation |
| MF-SCR-02 | Malformed/oversized/image-only PDF, invalid encoding and cancel/retry | Recoverable errors, no partial authoritative script; ordinary no-AI path remains functional |
| MF-SCR-03 | Renumber, move, split, merge or ambiguously reconcile existing Scenes | Stable Scene IDs for continuing scenes; ambiguous matches require review; downstream links not silently reassigned |
| MF-SCR-04 | Edit across collapse/expand, reload, concurrent tab and failed autosave | No lost selection/unsaved content; truthfully reported save and revision state |
| MF-SCR-05 | Run optional parser on Amharic/English synthetic screenplay with hostile text | Explicit opt-in/cost/provider disclosure, schema-valid draft, source trace, no instruction execution or unauthorized persistence |

## Scene Breakdown, canonical Elements and character aliases (M3/M3.5)

| ID | Scenario | Oracle |
| --- | --- | --- |
| MF-BRK-01 | Select script line and right-click; create/reuse Element | Context menu available by click/keyboard alternative; correct excerpt/scene/revision provenance and category |
| MF-BRK-02 | Assign an Element once, discover occurrences throughout script | Occurrences found across eligible scenes, ambiguous instances reviewable; no duplicate canonical Element or unwanted bulk assignment |
| MF-BRK-03 | Character uses first name, nickname and alias | All valid mentions resolve to same canonical Character while avoiding unrelated-name false positives |
| MF-BRK-04 | Reuse one Element with different quantity, variant, status or department | Canonical identity shared while scene-specific attributes remain independent |
| MF-BRK-05 | Revise source lines or remove/move text after assignment | Changed/moved/missing/unchanged impact statuses and manual decision paths; earlier provenance retained |
| MF-BRK-06 | Collapse editable script and work in full-width Breakdown Sheet; print | Draft/selection preserved, Notes/Assets/Links contextual tabs function, print excludes screenplay when specified |

## Project Library, versions and rights

| ID | Scenario | Oracle |
| --- | --- | --- |
| MF-LIB-01 | Upload image/audio/video/PDF, corrupt files, MIME mismatch, duplicate and size boundaries | Type/limits and scan behavior match current policy; stable asset and correct immutable version references |
| MF-LIB-02 | Favorite item as User A, inspect as User B | Per-user favorites isolated within correct organization/production |
| MF-LIB-03 | Extract media properties and rational frame rate | Audio/video metadata fields and exact numerator/denominator FPS preserved; no lossy guessed value |
| MF-LIB-04 | PDF text search with no-text or malformed document | Searchable extraction where supported; explicit no-text/diagnostics, not invented OCR result |
| MF-LIB-05 | Link current vs pinned asset versions; apply rights, trash/restore/purge | Pinned links stay pinned, rights not leaked to guests, blocked/quarantined originals not served; purge respects references |

## Shot List, Storyboard, Review and export

| ID | Scenario | Oracle |
| --- | --- | --- |
| MF-SHOT-01 | Create, reorder, duplicate, filter and switch list/card presentations | Same canonical Shot data and order, no loss of view-specific draft or script/scene linkage |
| MF-SHOT-02 | Review and approve a specific storyboard/Shot version; change it afterward | Old approval not shown as current, notes/version/frame references retained |
| MF-SHOT-03 | Create a visual panel and export storyboard or planning package | Asset identity/rights, dimensions, metadata and supported round-trip are valid |
| MF-SHOT-04 | AI-assisted storyboard request with malformed output/cost/disabled provider | Manual path works; proposals permission-scoped, reviewable and not auto-authoritative |

## Shot Designer, 2D layout, camera coverage and timing

| ID | Scenario | Oracle |
| --- | --- | --- |
| MF-SD-01 | Use single Design shelf to place wall, opening, prop, character, camera and light | User completes task without hidden rig/actor/light registration; selecting an object shows its correct contextual inspector |
| MF-SD-02 | Draw floor before double-click completion | Preview/path visible and follows cursor from first point; finished geometry persists; Undo/Redo works |
| MF-SD-03 | Construct joined walls and corner smoothing | Structural wall endpoints connect precisely, no visible gap/overlap; smooth/unsmoothed corners valid; default wall color gray if approved |
| MF-SD-04 | Switch tool dropdown, resize, keyboard/touch navigation | Distinct icons and names where specified, correct selected tool, no hidden hover-only requirement or overlay congestion |
| MF-SD-05 | Select different camera coverage ranges | Timeline/x-position/playhead/ruler stable; selection highlights exact interval, not the entire scene; scrubbing alone does not alter selected Shot |
| MF-SD-06 | Calculate planned coverage across simultaneous Shots/cameras | This camera's planned coverage identifiable; neutral gray only where another Shot covers the segment; red only where **no** active planned Shot covers it; no red for simple camera inactivity |
| MF-SD-07 | Alternate/overlapping and disjoint ranges, inactive Shots and unassigned cameras | Correct source-of-truth intervals, no accidental merging/duplication; accessible selection and meaningful gap state |
| MF-SD-08 | Change actor/camera/light in Scene context vs selected Shot | Explicit edit scope, inherited/shared vs override semantics, no implicit override on select; reset to Scene works |
| MF-SD-09 | Animate path and keyframes then preview shot range | Blocking path remains distinct from timed animation; correct selected interval and persisted keyframes |
| MF-SD-10 | Switch Simple/Advanced SVG, import/preview assets, undo and export | Stable IDs/footprints/pivots; no SVG active content or lost scene links; Golden asset baseline not silently altered |
| MF-SD-11 | Large scenes, pan/zoom, timeline resize and browser/inspector switching | Selection and scroll position stable; measurable rendering and memory budget; viewport unchanged on unrelated selection |

**Road Designer (conditional, only after implementation):** Test straight/curved segments, add/remove lanes, bidirectional/single-direction layouts, intersections, curbs/markings and props, junction connectivity, lane continuity, undo/redo, scale alignment and export. Do not report Road Designer as failed solely because an approved future plan exists.

**3D previs / Character Studio (conditional):** Six editable starting templates (adult man, boy, adult woman, girl, older man, older woman); easy non-rigging adjustments/posing/animation for filmmakers; human-editable AI blocking, set, light and camera proposals. Validate editability, script/Shot linkage, source rights and explicit acceptance, not photorealism or professional rigging controls not promised.

## Scheduling, Shoot Day, Availability/DOOD and Call Sheets (M4)

| ID | Scenario | Oracle |
| --- | --- | --- |
| MF-SCH-01 | Drag/reorder Scene strips to Shoot Days; boneyard and undo | Stable Scene and schedule IDs, correct parent Shoot Day hierarchy and saved ordering |
| MF-SCH-02 | Switch scenario/version, clone, compare and publish | Draft vs published history retained; correct authorization, no silent public updates |
| MF-SCH-03 | View Day Plan, calendar modes, availability/DOOD and conflicts | Same canonical schedule; cast/location availability and company move/time zone warnings accurate |
| MF-SCH-04 | Open History & options, close by launcher/Escape/outside/Close, use nested dialog | Focus restored and controls remain contextual; no duplicated global Search, Appearance or Organizations |
| MF-SCH-05 | Generate call sheet, revise/publish and re-distribute in approved fake channel | Latest schedule/cast/location/call times, PDF, delivery/view/confirmation statuses and version history correct |
| MF-SCH-06 | Simultaneous coordinator edits, time zones, DST and conflicting bookings | Stale writes/conflicts visible, correct local call times and audit; no silently overwritten schedule |

## AI providers, agent platform and tools

| ID | Scenario | Oracle |
| --- | --- | --- |
| MF-AI-01 | Admin configures/rotates/disables provider; user without permission invokes it | Server-held secret never in UI/API/logs; tenant/model/capability policy enforced and audited |
| MF-AI-02 | AI unavailable, rate limited, malformed, malicious or over budget | Clear recovery, accurate usage status; manual feature not blocked |
| MF-AI-03 | Accept/reject/retry suggestions from one source revision and a newer one | Proposals remain drafts until authorized confirmation, source revision/concurrency checked, no duplicate canonical updates |
| MF-AI-04 | MCP/agent job replays, cancellation and permission revoked during job | Idempotency and run-scoped permissions; no unauthorized writes or false global rollback claims |

## Conditional future domains (only if release scoped)
- **Budget (M5):** Quantity × rate calculations, decimals/currencies/fringes, versions/approval, schedule-driven dependencies and permission boundaries. Payroll/banking initially integrated, not silently assumed native.
- **Production/on-set (M6):** Crew check-in, shot/take status, continuity, time/meal logs, incident reporting, offline behavior only as actually implemented.
- **Post-production (M7):** Scene/shot lineage through Editorial/VFX/Sound/Color, version-based review, timecode/frame notes, QC and approval audit; no duplicated production graph.
- **Delivery and wrap (M8):** Codec/resolution/audio/captions metadata, rights and master references, package approval, export and archive/recovery. Do not declare an unshipped milestone complete based on a page mock.

## Cross-cutting data and UX corpus
Use synthetic English/Amharic script text, nickname collisions, identical scene headings, 29.97 rational-frame rates where timecode exists, large datasets, revoked users, inactive Shots, concurrent tabs, malformed PDFs/SVGs, 360/768/1280/1440+ widths, light/dark theme variants and interrupted network. Confirm which are supported at the candidate SHA. Never use confidential Yekermo Sew scripts or real actor contact information as fixtures.
