# Synthetic Film Production Fixtures and Execution Boundary

These fixtures are **proposals for test setup**, not evidence that seeds, services, or accounts exist. Confirm actual schema, permissions and application interfaces before populating any disposable target.

## Fixture model

- Organization A: a film studio with Production A1 (episodic EP01/EP02), A2 (creator content).
- Organization B: an unrelated film studio with Production B1 and its own people/files.
- Identities: A owner, producer, coordinator/AD, director, editor, guest/viewer, custom permission member; B-only member; dual-member identity for context switching.
- Script: 3–5 scenes with numbering variants 12A / 12.1, INT/EXT, DAY/NIGHT, multilingual text and a revision that renumbers or moves one Scene. Use synthetic text, not a real Yekermo Sew episode.
- Characters: Person/Character A with a formal name and a nickname used consistently, Character B, one background/unnamed figure; test ambiguous nicknames separately.
- Elements: a reusable prop referenced in two scenes with different per-scene notes, plus an alias collision intentionally meant not to match.
- Schedule: overlapping cast availability, location conflicts, two Shoot Days, changes that should invalidate a draft call sheet, safe fake contact destination and confirmation event.
- Shot Designer: one common room plus Shot 01 and Shot 02 with overlapping coverage, a short interval, a deliberately uncovered interval, one camera per Shot and one alternate; lighting, actor placement and a wall opening. If newer Road Designer is delivered, include a two-lane curve and an intersection.
- Assets: inert PNG/SVG, allowed and disallowed synthetic format metadata, one version-pinned reference, one follow-current reference; never use live malware or copyrighted client footage.
- Optional AI: local fake provider returning valid proposal, malformed schema, rate limit, timeout and adversarial screenplay text; do not send private screenplay to external providers.

## Execution prerequisites

Record exact application SHA/build, tested branch, test process IDs and ports, test-service containers, host and database identity, storage root, browser profile, synthetic accounts, configuration version and data-deletion ownership. Inspect current Playwright config, reset scripts, file-writing behaviors, provider integrations and mail setup. A database named *uat* or *test* is not sufficient isolation. Verify target is disposable independently.

For screenshots, keep deterministic data, viewport, zoom, fonts, scale and animation; include before/after only for changed UI. A visual-only run is not durable state verification: read/reload persisted records or validate a suitable API response.

## Teardown and traceability

Cleanup only test-created resources in the approved target. Record fixture IDs, seed/cleanup version and failed cleanup. Redact email addresses, tokens, private scripts, signed URLs and tenant identifiers from shared artifacts. Do not commit generated private screenshots or raw DB dumps.

Attach a ledger row per test: requirement ID, fixture ID, scope/role, exact expected business result, actual response/persisted state, command/log/trace, time and candidate SHA. Distinguish attempted tests, selected-but-unrun tests and policy-mandatory suites.
