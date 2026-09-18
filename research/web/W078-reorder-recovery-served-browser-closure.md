# W078 — Reorder Recovery Served-Browser Closure

Status: **STAGE 3 PRACTICE / NOT EXECUTED**  
Purpose: **TRANSFER VALIDATION** of I065/L069/CD084/C078 in actual Web runtime.

## RELATED DOMAIN CHECK
Type T047 supplies protected rendering corpus. Color C078 supplies recovery state axes. L069 supplies recovery geometry. I065 supplies transaction/reversal oracle. CD084 supplies semantic payload and persistence-language boundary.

## SOURCE
WCAG 2.2 SC 2.5.7 requires a single-pointer non-drag alternative for drag functionality. SC 4.1.3 requires status messages to be programmatically determinable without receiving focus. WAI APG rearrangeable-list examples use explicit move buttons plus a last-change status; APG warns that example code is illustrative and production use requires browser/AT testing.

## Browser closure sequence
Do not skip evidence levels:
1. widget/runtime semantic transaction test;
2. production Web build;
3. served primary browser;
4. independent browser engine;
5. 200% text/zoom + light/night/forced-colors;
6. delayed/failed persistence only after persistence exists;
7. screen-reader/physical-device/human evidence separately.

## Scenario manifest
For `move → undo`, `boundary reject`, and `reset` capture:
- build/commit, browser/engine/version;
- viewport, zoom/text scale, theme/forced-colors;
- semantic order before/move/undo;
- active/focused semantic ID and focus rectangle;
- scroll offset and obscuration;
- move/Undo target rectangles;
- visible status and accessibility status payload;
- DOM/semantics name/state where available;
- console/runtime exceptions;
- persistence state only if implemented.

## Acceptance
- Move and Undo round-trip semantic order exactly for the defined transaction.
- Status announcement mechanism does not steal focus merely to report the change.
- Recovery control remains operable at 200% and is not obscured.
- Forced-colors preserves understandable focus/recovery state without authored-color dependence.
- Independent-engine execution is required before cross-browser claims.
- A green widget suite or production build is not a browser PASS.

## Performance evidence boundary
Lighthouse, DevTools and CI synthetic traces remain **LAB**. LCP/INP/CLS become **FIELD** only with provenance-bearing aggregate/RUM evidence from the relevant product/runtime population. Recovery UI must not be blamed for field performance without such evidence.

## CRITIQUE
An ARIA live region can satisfy a static implementation check while producing duplicate/noisy announcements in a real browser+AT pair. Therefore 4.1.3-compatible markup is necessary evidence, not screen-reader quality PASS.

## OPEN
Non-drag reorder and recovery implementation, served-browser execution, independent engine, forced-colors runtime, screen-reader, physical device, persistence/sync and field Core Web Vitals.

## HANDOFFS TO OTHER SPECIALISTS
Return browser geometry to Layout, focus/reversal failures to Interaction, state rendering to Color, actual strings/announcements to Content, and resolved-font evidence to Type.