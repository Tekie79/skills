# Design, Accessibility, and SEO

## Design Contract

Refresh `docs/UI_DESIGN_SYSTEM.md`, `docs/THEME_SYSTEM.md`, approved compositions,
and candidate components before judging. This is conformance/usability testing,
not permission to redesign the product according to personal taste.

Verified brand: **Meher Flow**. UI chrome uses Inter and semantic tokens; screenplay
content uses Courier Prime or approved production-scoped language fonts. Test
Amharic/Unicode examples with synthetic text and fallback glyphs. Canonical print
surfaces may deliberately differ from UI theme colors.

Themes at the snapshot: Meher, Studio, Mono, Linen, Frost, each in light/dark;
System is a preference resolving to one mode. Test changed surfaces across the
theme matrix and representative full journeys in all combinations. Include
first-paint flash, invalid/legacy preferences, cross-tab synchronization, OS mode
changes, and persistence. Appearance changes must preserve route, data and layout.
Frost translucency is restricted; dense data surfaces remain readable/opaque.

Check hierarchy, spacing, typography, token usage, information density, consistent
controls, uncluttered authenticated shell and permission-aware navigation. Avoid
flagging domain colors, screenplay/print colors or user asset pixels as token
violations without checking documented exceptions.

## Interaction and Responsive Matrix

| Dimension | Checks |
| --- | --- |
| Layout | Representative mobile (e.g. 360 px), tablet (768 px), laptop (1280 px), desktop (1440+ px); actual supported breakpoints and viewport fit |
| States | Loading, empty, populated, submitting, success, validation, server/network error, permission denial, stale write, session expiry |
| Forms | Explicit labels, input retention on failure, duplicate-submit protection, correct errors; modal close/reset/refresh or settings concurrency-version update on success |
| Dialogs/popovers | Focus containment/restoration, Escape/outside close, stacking, title/description, one active dropdown; no interactive forms nested in menu primitives |
| Navigation | Deep links, back/forward, refresh, current URL selection, context switching, persistent account/sign-out and authorized actions |
| Dense work | Large tables, horizontal data scrollers without page overflow, selection shortcuts/ranges, upload/Designer/Breakdown contextual panels |
| Destruction | Clear consequences, required typed confirmation, valid cancel path, no accidental keyboard-triggered irreversible action |
| Delivery | Browser/PWA install/update/reconnect, native OS chrome/file dialogs if in scope, canonical print and PDF output |

Use deterministic viewport, browser/OS, seeded content, fonts, time, motion, and
network when comparing screenshots. Capture baseline/candidate/diff and associate
each mismatch with an approved design rule. Do not blindly accept new baselines.
Review real devices and touch/zoom when available; emulation does not prove parity.

## Accessibility

Use WCAG 2.2 AA as a proposed review target unless another conformance contract
applies. Automated scans can find issues but cannot certify conformance.

- Keyboard-only primary journeys; logical tab order; no traps; visible focus not
  obscured by sticky/bottom navigation; skip/main/landmark structure as appropriate.
- Accessible names, roles and state; links navigate and buttons act; labels and
  error associations; headings; grouped controls; live announcements for progress,
  async status and actionable errors. Test with a real screen reader where possible.
- Text contrast generally 4.5:1 (3:1 for qualifying large text); applicable UI
  component/non-text contrast 3:1; state not communicated by color alone.
- Touch targets and spacing per WCAG 2.2 criteria (24x24 CSS px minimum or permitted
  exceptions); zoom/reflow at 200%/400%, reduced motion, high contrast, focus order
  and error prevention. Record applicable exceptions rather than arbitrary failure.
- Accessible alternatives/semantics for dense tables, canvas/Designer, uploads,
  drag/drop, charts and visual selection tools; ensure essential outcomes are
  possible without pointer-only gestures. Verify text alternatives in context.

Report criterion, component/route, affected persona, steps, evidence and impact.
Do not use a single automated accessibility score as acceptance evidence.

## SEO: Separate Public and Private Surfaces

Inventory actual public indexable routes, auth/token pages, authenticated workspace,
API/file endpoints, and environment. Establish intended discoverability first.
Do not invent public marketing pages. Snapshot root layout provides Meher Flow
title/description and `lang="en"`; this alone does not prove route-level SEO.

For public indexable pages check server-rendered useful content, descriptive unique
titles/descriptions/headings, crawlable links, canonical scheme/host/URL, redirect
chains/statuses, true 404/410 vs soft-404, sitemap scope/lastmod, robots rules,
mobile usability, HTTPS, image alt text, Open Graph/social previews and performance.
Structured data must describe real visible content and validate against relevant
schemas; never fabricate ratings or use schema markup as a ranking guarantee.
Check locale/hreflang only if multilingual public publishing actually exists.

For private workspace and auth/token pages check intended `noindex`/`X-Robots-Tag`,
canonical behavior, sitemap exclusions, response/cache policy and authorization.
`robots.txt` disallow is not access control, and a blocked crawl may prevent a
bot from seeing `noindex`. Verify sensitive content never appears in unauthenticated
HTML, previews, metadata, error pages, CDN/service-worker caches, shared links or
signed media URLs. Authorization remains mandatory regardless of indexing policy.

Staging should be access-restricted and non-indexable by policy; production public
pages must not accidentally inherit staging `noindex`. Check final HTTP headers
and rendered HTML on the actual approved target. Source-only review cannot prove
deployed indexing behavior or search-engine results. Crawl only approved URLs at
bounded rates; do not index or upload private repository/content to third-party tools.

SEO for an authenticated tenant workspace is privacy-first, not "make every route
rank." Mark genuinely public-only ranking criteria inapplicable with rationale,
but retain the private indexing/data-leak checks.
