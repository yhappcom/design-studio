# W075 — LogMate Customize Browser Closure

Date: 2026-09-18
Mode: **PRODUCT TRANSFER + WCAG 2.2 CLOSURE DESIGN**
Stage: 3 PRACTICE / NOT PASSED

## Product evidence
LogMate `main` currently implements Customize as a temporary session shell with 35 top-level items, visible reorder, stable hidden order, immediate changes, four renderer-controlled groups, at-least-one-visible enforcement and Reset. Widget tests exercise semantic reorder, shared header/body/totals alignment, visibility-driven overflow and scroll-indicator safety. Persistence, Sync and real FlightRecord projection are not implemented.

## Current authoritative accessibility baseline
WCAG 2.2 is the studio baseline. For this surface the highest-value criteria include:
- 2.5.7 Dragging Movements: drag functionality needs a single-pointer non-drag equivalent unless dragging is essential;
- 2.5.8 Target Size (Minimum): 24×24 CSS px baseline subject to defined exceptions;
- 1.4.10 Reflow: two-dimensional layout may be essential for the ledger, but Customize controls and explanatory UI should not inherit that exception without justification;
- keyboard/focus and non-text contrast requirements remain part of complete browser closure.

## Browser closure matrix
A production-transfer run should use one scenario manifest across:

1. Standard ledger, Customize unopened.
2. Enter Customize by pointer and keyboard.
3. Toggle OFF/ON; verify immediate projection update.
4. Reorder by drag.
5. Reorder to the identical semantic result by non-drag single-pointer path and keyboard path.
6. Toggle/move each system Field Group.
7. Reach one-visible-item floor.
8. Reset to Standard.
9. 200% text / zoom for Customize controls.
10. light/night/forced-colors.
11. narrow/wide landscape and keyboard-up/short-height where relevant.
12. reload/offline/restart only after persistence exists; cross-device conflict only after Sync exists.

Each scenario records build SHA, browser engine/version, viewport, DPR, zoom/text scale, input mode, semantic configuration before/after, screenshot, focus path, console/runtime errors and result class.

## CRITIQUE
Existing Flutter widget tests are valuable component/runtime evidence but cannot prove WCAG 2.2 dragging equivalence, browser focus behavior, forced-colors, independent-engine compatibility or persisted configuration. Conversely, a red CI job should not erase individual executed PASS evidence; preserve scenario-level provenance.

The ledger's horizontal scrolling may be justified by two-dimensional professional meaning. The Customize surface is a separate interaction system and should be tested for ordinary reflow rather than automatically claiming the ledger exception.

## Performance evidence boundary
Customization can increase rendered column count and work, but no field Core Web Vitals evidence exists. Lighthouse, DevTools and CI traces remain **LAB**. LCP/INP/CLS become **FIELD** only with provenance-bearing aggregate/RUM evidence for the product and relevant route/population.

## RELATED DOMAIN CHECK
- **Type:** browser font loading/fallback for compact aviation headers.
- **Color:** forced-colors and actual paint-state evidence.
- **Layout/Interaction:** density, horizontal ledger, reorder equivalence and recovery.
- **Content:** semantic IDs must drive assertions; English labels must not become state logic.
- **UX:** pilot workflow efficiency remains a human-evidence question even if automation passes.

## HANDOFFS TO OTHER SPECIALISTS
Interaction receives non-drag/keyboard reorder results. Color receives forced-colors/rendered-state artifacts. Type receives fallback/zoom evidence. Content receives localization/accessibility-name discrepancies. Layout receives breakpoint/overflow findings.

## OPEN
Production persistence, real record projection, independent engine, forced-colors, screen reader, physical device, real network/sync, field Core Web Vitals, representative-human usability.

## Conclusion
W075 moves Web's next product-transfer target from auth-only runtime toward a complete professional customization workflow. No browser closure is claimed until the matrix executes.