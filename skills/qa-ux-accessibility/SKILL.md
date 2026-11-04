---
name: qa-ux-accessibility
description: "Review web or desktop UI usability, approved design fidelity, responsive behavior, accessibility and privacy-aware search indexing. Use for visual UI QA, WCAG checks, keyboard/touch workflows and related user experience tests; not for imposing an unsolicited redesign."
---

# UI, Usability and Accessibility QA

## Goal
Verify that a feature supports user tasks across its approved states, devices, themes and assistive input. Do not substitute personal design taste for an accepted design system.

## Inputs
Exact build, approved design/reference and terminology, supported breakpoints, themes, audience, feature states, browser/OS/device, a11y target, public versus private route intent and test access.

## Workflow
1. Start from user goals, design tokens, approved screenshots and interaction specification. Compare actual hierarchy, spacing, visibility, contrast and controls; annotate deviations with their authoritative source.
2. Exercise create/edit/review/undo/save, empty/large states, loading, validation, disabled, network failure, stale data, navigation, drawer and dialog lifecycle. Verify durable outcomes after refresh and context changes.
3. Use representative mobile/tablet/desktop sizes and zoom, touch, keyboard-only input, reduced motion and real screen-reader testing when available. Emulation alone does not certify device parity.
4. Check semantics, accessible names and descriptions, focus order/visibility, dialog focus containment/restoration, non-color-only status, keyboard alternative to drag/drop/canvas tasks and announcements for async save/error. Use WCAG 2.2 AA unless the project establishes another target; report applicable exceptions accurately.
5. Capture deterministic screenshots and compare approved baseline/candidate/diff. Hold constant fonts, data, viewport, clock and animations. Do not auto-approve snapshots.
6. Treat SEO as conditional: public indexable routes need appropriate metadata/crawl/navigation; authenticated project/workspace and private documents need non-indexing plus true authorization/cache protections. Robots rules alone do not secure data.
7. Report severity by task impact, accessibility barrier and frequency; distinguish visual mismatch from functional failure and blocked manual screen-reader checks.

## Output contract
Give a route/component state matrix with steps, expected vs actual, screenshot/trace ID, requirement or WCAG criterion, role/device/theme and status; include high-priority interaction fixes and evidence gaps.

## Example
Input: A tool-shelf menu shows text instead of icons; selecting an animation interval shifts the horizontal layout.
Output: Verify icons with accessible names and pointer/keyboard menu behavior; record stable canvas/time ruler coordinates across range switches at several widths; add screenshot and measurable bounding-box regression.

## Safety
No unexpected visual baseline updates, asset overwrites, content publishing or real external user notifications. Private-route indexing and cache checks must not expose confidential user data. See [behavioral evaluations](references/evaluations.md).
