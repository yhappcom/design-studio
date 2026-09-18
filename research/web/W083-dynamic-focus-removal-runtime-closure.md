# W083 — Dynamic Focus Removal Runtime Closure

## Purpose
Extend W082 from surviving semantic focus identity to browser/runtime evidence when the focused object/action is removed from the active projection. This targets a real Stage 3 closure gap rather than another isolated Chromium micro-test.

## SOURCE / platform transfer
Flutter focus guidance states that unfocus transfers focus elsewhere, recommends explicit focus when destination matters, and warns that falling to root scope can damage traversal. FocusScope retains focus history. WAI-ARIA APG deletion/rearrangement patterns provide implementation examples where a removed current item yields a logical neighbor and repeated moves preserve the moved item; APG examples are guidance, not production compatibility proof.

## RELATED DOMAIN CHECK
T051, C083, I069/I070, L073/L074 and CD089 checked. W083 is implementation/runtime validation; it does not redefine their canonical contracts.

## Runtime manifest
For each build/scenario capture: commit/build identity; engine/version; viewport/zoom/theme/forced-colors; pre/post Flutter semantic object/action ID; FocusNode/FocusScope identity when observable; browser active/focus target; accessibility semantic identity; projection membership; fallback reason; visual ordinal; focus/target rectangles; scroll delta/obscuration; status/accessibility payload; console/runtime exception.

Scenario families: focused middle field→hide; focused end field→hide; action becomes unavailable while object survives; group collapse; Reset hides focused field; Undo restores field; last-visible guard/no-op; navigation after fallback. Execute twice per available path.

## Closure ladder
Widget/runtime → production Web build → served primary engine → independent engine → 200% text/zoom → light/night/forced-colors. A correct final projection, visible ring, or same ordinal alone cannot PASS semantic focus continuity.

Performance remains separate: Lighthouse/DevTools/CI synthetic evidence is LAB. LCP/INP/CLS become FIELD only with provenance-bearing aggregate/RUM evidence.

## OPEN
No W083 LogMate runtime execution, independent-browser, forced-colors, screen-reader, physical-device, field Core Web Vitals, full WCAG or human UX PASS.

## HANDOFFS TO OTHER SPECIALISTS
Return any semantic mismatch to Interaction, geometry/scroll failure to Layout, stale state paint to Color, message/payload mismatch to Content, and only reproduced glyph/metric/fallback/raster faults to Type.