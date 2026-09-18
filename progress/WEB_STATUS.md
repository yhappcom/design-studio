# Web Design Specialist Status

Operating state: **ACTIVE — STAGE 3 PRACTICE / W093 SERVED SCROLL-REORDER ARBITRATION CLOSURE**
Governance sync: 2026-09-19
Primary path: `research/web/`

## Current level
Stage 1 **PASS**; Stage 2 **PASS**; Stage 3 **PRACTICE / NOT PASSED**.

## Latest evidence
W093 extends W092 into served scroll-versus-reorder arbitration. Pointer Events `touch-action` and Flutter gesture-arena documentation establish SOURCE feasibility only; actual UA pan suppression, recognizer outcome, scroll displacement and semantic transaction result require product/browser runtime evidence.

## Active queue
1. Execute I077–I080/W090–W093 once the non-drag reorder path exists, preserving I063–I076 transaction/focus/Undo/IME invariants.
2. Run production Web build → served primary engine → independent engine with identical scenario IDs; replicate each executable family twice.
3. Add row-body scroll, affordance-start→scroll/arena-loss, valid reorder, pointercancel/UA suppression, stationary-pointer 200% reflow, boundary no-op, non-drag equivalent, light/night/forced-colors and geometry evidence.
4. Keep persistence/offline/sync dormant until implemented.
5. Keep Lighthouse/DevTools/CI synthetic LAB; only provenance-bearing aggregate/RUM may support field LCP/INP/CLS.
6. Keep screen-reader, physical-device/input and representative-human UX evidence OPEN.

## Evidence boundary
No cross-browser/Safari/Firefox, non-drag reorder or scroll/reorder arbitration runtime, persisted configuration, screen-reader, physical-device, field Core Web Vitals, full WCAG conformance or human UX PASS is claimed.