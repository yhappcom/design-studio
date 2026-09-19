# Web Design Specialist Status

Operating state: **ACTIVE — STAGE 3 PRACTICE / W096 SERVED SCROLL-ANCHOR + FOCUS TRANSFER**
Governance sync: 2026-09-19
Primary path: `research/web/`

## Current level
Stage 1 **PASS**; Stage 2 **PASS**; Stage 3 **PRACTICE / NOT PASSED**.

## Latest evidence
W096 extends W095 into browser/application scroll stabilization. Current CSS Scroll Anchoring draft behavior cannot be treated as parity evidence because a July 2026 CSSWG issue reports suppression-window behavior differing across implementations. Served primary + independent-engine evidence is therefore required.

## Active queue
1. Execute I077–I083/W090–W096 once the non-drag reorder path exists, preserving I063–I082 invariants.
2. Run production Web build → served primary engine → independent engine with identical scenario IDs; replicate each family twice.
3. Add scroll-anchor/app-scroll provenance, source-offscreen rebuild, focus identity, sticky/overlay obscuration, 200% reflow, non-drag equivalent, light/night/forced-colors and geometry evidence.
4. Keep persistence/offline/sync dormant until implemented.
5. Keep Lighthouse/DevTools/CI synthetic LAB; only provenance-bearing aggregate/RUM may support field LCP/INP/CLS.
6. Keep screen-reader, physical-device/input and representative-human UX evidence OPEN.

## Evidence boundary
No cross-browser/Safari/Firefox, non-drag reorder or scroll-focus runtime, persisted configuration, screen-reader, physical-device, field Core Web Vitals, full WCAG conformance or human UX PASS is claimed.