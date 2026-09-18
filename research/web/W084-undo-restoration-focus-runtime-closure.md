# W084 — Undo Restoration Focus Runtime Closure

## Purpose
Extend W083 browser closure to I071's inverse transition: an object restored by Undo may not be the active focus owner. Browser evidence must prove both configuration restoration and focus agency.

## RELATED DOMAIN CHECK
I071 owns behavior, L075 geometry, C084 state rendering, CD090 semantics, T053 future type transfer. Web integrates these in served runtime and does not redefine them.

## Closure manifest
For each executable scenario capture build/commit, engine/version, viewport, zoom/text scale, theme/forced-colors, transaction ID, restored semantic object ID, current focus semantic object/action ID, invoking recovery control, projection membership, accessibility identity, focus/restored-object rectangles, scroll offset, obscuration, visible/status payload and runtime exceptions.

Scenarios: middle/end hide→Undo; group collapse→recovery; Reset-hide→Undo; Undo after intervening action where product policy permits; 200% recomposition between mutation and Undo. Repeat each twice.

## Evidence ladder
Widget/runtime evidence → production Web build → served primary engine → independent engine → 200% → forced-colors. A correct final projection does not prove correct focus. A visible focus ring does not prove correct semantic owner. Persistence/offline/Sync remains NOT IMPLEMENTED until product truth exists.

## Accessibility boundary
WCAG 2.2 Focus Visible and Focus Not Obscured are AA floors. Focus Appearance is AAA and may be used as a stronger design critique target, not reported as an AA requirement.

## Performance boundary
Lighthouse, DevTools and CI traces remain LAB. LCP/INP/CLS become FIELD evidence only with provenance-bearing aggregate/RUM from the actual product population/environment.

## Evidence boundary / OPEN
No W084 runtime execution, independent-browser, forced-colors, screen-reader, physical-device, field Core Web Vitals or human UX PASS is claimed.

## HANDOFFS TO OTHER SPECIALISTS
Return focus-policy contradictions to Interaction, displacement to Layout, state-collapse to Color, wording/runtime mismatch to Content and genuine font-loading/raster failures to Type.