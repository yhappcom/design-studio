# W080 — Reset Baseline & Navigation Browser Closure

Status: **STAGE 3 PRACTICE / OPEN RUNTIME**  
Purpose: **TRANSFER VALIDATION** of I067/L071/CD086/C080 in served Web runtime.

## RELATED DOMAIN CHECK
Type T049 defines protected rendering evidence; Color C080 state integrity; L071 geometry; I067 transaction/baseline truth; CD086 semantic payload. UX remains cross-cutting.

## Closure manifest
For every scenario record build/commit, engine/version, viewport, zoom/text scale, theme/forced-colors, `baseline_id/kind/version`, semantic order/visibility before and after, active semantic ID, focus/target rectangles, scroll/obscuration, visible and accessibility status payload, console/runtime exceptions.

## Required scenarios
- modified → Reset → exact declared baseline;
- already-at-baseline → Reset/no-op;
- move → Undo → Reset;
- move → Reset → Undo attempt according to declared policy;
- Reset → navigate away/back;
- 200% text/zoom and short viewport;
- light/night/forced-colors;
- primary served engine then independent engine.
Future only after implementation truth: reload persistence, offline, sync/version conflict.

## Evidence ladder
Widget/runtime → production Web build → served primary engine → independent engine → accessibility-mode/network transfer. A green widget test does not prove browser closure. Synthetic Lighthouse/DevTools/CI remains LAB; only provenance-bearing aggregate/RUM may support FIELD LCP/INP/CLS.

## Acceptance
Reset reaches the declared semantic baseline, no-op does not fabricate a change, navigation does not silently retarget the baseline, focus/scroll remain usable, accessible state matches visible consequence, and no runtime exception is present.

## OPEN
No W080 execution, independent-engine, persistence, screen-reader, physical-device, field Core Web Vitals or human UX PASS is claimed.

## HANDOFFS TO OTHER SPECIALISTS
Return any browser contradiction to the owning domain: font/fallback→Type, paint/forced-colors→Color, geometry/focus→Layout/Interaction, semantic mismatch→Content/Interaction.