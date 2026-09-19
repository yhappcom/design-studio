# Web Design Specialist Status

Operating state: **ACTIVE — STAGE 3 PRACTICE / W094 SERVED EDGE-AUTOSCROLL REORDER CLOSURE**
Governance sync: 2026-09-19
Primary path: `research/web/`

## Current level
Stage 1 **PASS**; Stage 2 **PASS**; Stage 3 **PRACTICE / NOT PASSED**.

## Latest evidence
W094 extends W093 beyond scroll-versus-reorder arbitration into authored edge-autoscroll after reorder wins. Flutter autoscroll/boundary APIs are SOURCE feasibility only; actual scrollOffset(t), candidate changes and commit require product/browser evidence.

## Active queue
1. Execute I077–I081/W090–W094 once the non-drag reorder path exists, preserving I063–I080 invariants.
2. Run production Web build → served primary engine → independent engine with identical scenario IDs; replicate each family twice.
3. Add edge autoscroll→drop/cancel, stationary pointer, list-end saturation, active-drag 200% reflow, sticky/safe-area collision, non-drag equivalent, light/night/forced-colors and geometry evidence.
4. Keep persistence/offline/sync dormant until implemented.
5. Keep Lighthouse/DevTools/CI synthetic LAB; only provenance-bearing aggregate/RUM may support field LCP/INP/CLS.
6. Keep screen-reader, physical-device/input and representative-human UX evidence OPEN.

## Evidence boundary
No cross-browser/Safari/Firefox, non-drag reorder or edge-autoscroll runtime, persisted configuration, screen-reader, physical-device, field Core Web Vitals, full WCAG conformance or human UX PASS is claimed.