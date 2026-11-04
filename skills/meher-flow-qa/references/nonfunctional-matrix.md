# Meher Flow Nonfunctional Test Matrix

These are test charters, not performance results, a compliance certificate or a promise that all modules are delivered. Read candidate code/config and approved requirements first.

| Domain | What to test and measure | Failure modes and evidence |
| --- | --- | --- |
| Browser responsiveness | Shot Designer canvas with complex but synthetic room/object counts, long script/Breakdown tables, Schedule drag/drop, loaded Storyboard timeline | Frame time distribution, user input latency, unnecessary rerenders, layout shifts, memory after repeated open/close and pan/zoom |
| API/DB scalability | Tenant-scoped search, paginated scenes/elements/assets, schedule conflicts, export and permission filters at increasing synthetic data sizes | p50/p95/p99 with counts and comparable environments; N+1 queries, unbounded sort/count, row-level filter misses, lock waits |
| Worker resilience | Upload scan/retry, script processing, storyboard/AI task, outbox and call-sheet distribution only if shipped | Fail before/after commit, token expiry, duplicated deliveries, lease recovery, bounded queue and visible terminal status |
| Memory and size | Large screenplay revisions, dense Shot layouts/SVG assets, multi-day schedules and media metadata | Heap/RSS, unexpected serialization copies, stalled main thread, out-of-memory, resource cleanup; safe bounded datasets |
| Security and privacy | Tenant and project ID substitution in API/file/export/search/job, guest link expiry/revocation, permission changes mid-session | Direct denied request plus durable state, no unauthorized content/cache, no leaked signed URL or unauthorized success audit; correct scoped security-denial audit permitted |
| AI/agent | Provider disabled/unavailable/over quota, prompt injection in user script, model-response validation, low-confidence suggestions | Source text never becomes instructions, provider creds masked, permission-bound acceptance, no silent canonical updates or tenant crossover |
| Accessible interaction | Keyboard and touch to create/choose actors/cameras/lights, wall/floor/road tools, timeline ranges, modal/drawer and drag/drop alternatives | WCAG 2.2 AA review target if adopted; semantic names, focus, visible indication beyond color, touch targets, screen reader where possible |
| Responsive and themes | Light and charcoal/dark design, supported 360/768/1280/1440+ px examples, zoom/reflow, reduced motion, print and Amharic Unicode text | No panel overflow, hidden action, icon-only ambiguity, unreadable preview or Lost selection on navigation |
| Time and media accuracy | Production local dates/DST, call times, multi-camera overlapping Shot ranges, rational frame rates, export/import and Storyboard | Repeated/omitted hours, off-by-one frame and split interval errors, stale version references |
| Installation/recovery | Clean approved self-hosted installation, supported DB upgrade, restored media and metadata, desktop/browser session lifecycle | Independent isolated restore with correct keys/roles, real measured RPO/RTO against project-approved objectives, no blind downgrade/volume deletion |

## Measurement protocol

Specify immutable candidate SHA, build mode, OS/browser/device, synthetic dataset volume, selected workflow, baseline, warm-up, repeats, concurrency and throttling. Record elapsed timings and failure counts, not just one best run. Distinguish latency of actual user operations from artificial browser sleeps. Run production builds for performance; do not compare development and production as if equivalent.

For performance objectives, use actual approved project budgets. If none exist, *propose* budgets (and require owner decision) without declaring test success against invented thresholds. For web vitals, distinguish field data from a lab score; a Lighthouse score does not establish all users' experience.

Use bounded, explicitly authorized load/stress/soak tests only on isolated staging with named stop thresholds and no expensive real AI calls or external mail.

## Incident and recovery safety

Do not truncate a DB, turn off malware scanning in production, create load against a public URL, enable real call-sheet delivery or run destructive fault injection as a casual QA step. If test target identity or blast radius cannot be verified, mark BLOCKED with a safe alternative.
