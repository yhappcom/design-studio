# W095 — Served Reorder Focus Closure

Date: 2026-09-19
Stage: Stage 3 PRACTICE / NOT PASSED
Related: I082/L086/C095/CD101/T064

## Closure target
Do not add another isolated Chromium micro-test. Execute the actual LogMate implementation through: production Web build → served primary engine → independent engine → 200% → forced-colors.

## Manifest
For each I082 family and each of two replications record: build/commit, route, browser/engine, viewport, zoom, color mode, input modality, semantic source/destination IDs, active/focused semantic ID before/during/after, source/proxy/focus/sticky rectangles, scrollOffset(t), reorder callback/result, transaction/branch/inverse, projection hash, visible status, accessibility payload and recovery eligibility.

Distinguish `onReorderEnd`/gesture completion from application mutation. Framework feasibility is SOURCE only. Product PASS requires served evidence.

## Acceptance
- stable semantic focus ownership across rebuild/autoscroll;
- no author-created content entirely obscures focused component under WCAG 2.2 SC 2.4.11 test conditions;
- drag and non-drag paths resolve to equivalent semantic mutation;
- cancel/no-op never masquerades as commit;
- 200% and forced-colors retain operability and state clarity;
- independent engine reproduces the critical family before closure.

## Performance evidence boundary
Lighthouse, DevTools and CI synthetic measurements remain LAB. LCP/INP/CLS become FIELD evidence only with provenance-bearing RUM/aggregate data.

## Evidence boundary
No independent-engine, screen-reader, physical-device, field Core Web Vitals, full WCAG conformance or human UX PASS is claimed until executed.