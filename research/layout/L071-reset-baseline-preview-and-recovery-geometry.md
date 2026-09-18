# L071 — Reset Baseline Preview & Recovery Geometry

Status: **STAGE 3 PRACTICE / OPEN RUNTIME**  
Purpose: **EXTENSION** of L067–L070 for I067 baseline-aware Reset.

## RELATED DOMAIN CHECK
I067 defines baseline provenance; CD086 owns consequence wording; C080 owns changed/no-op/recovery state visibility; T049 protects resulting strings; W080 owns browser closure.

## Spatial problem
Reset may affect many visible/hidden rows at once. The surface must preserve orientation before, during and after a potentially large recomposition without treating a dense ledger as permission to obscure controls.

## Architecture comparison
Compare four evidence-backed options: immediate Reset + Undo; compact consequence preview; explicit confirmation sheet/dialog; baseline-summary surface with Reset action. Do not select by screenshot preference.

Measure at baseline, modified, reset and recovered states: viewport/safe area, active semantic ID, focus box, reset/undo target boxes, scroll offset, first/last affected semantic item, wrapping, sticky overlap, keyboard collision, 200% text and target geometry.

## Acceptance
- consequence information and recovery action remain reachable at 200% text;
- Reset-triggered recomposition does not strand focus on a removed/reordered visual index;
- the user can recover orientation to the same semantic field where feasible;
- no dialog/sheet is added merely because Reset sounds destructive: consequence scope governs architecture;
- hidden≠deleted and display configuration≠flight data remain spatially legible.

## CRITIQUE
Confirmation can reduce accidental activation but also creates repetitive modal friction; Undo can preserve flow but may be too transient for large changes. Geometry evidence and actual workflow risk must decide.

## OPEN
No architecture selected. Runtime, independent engine, AT, physical-device and representative-pilot evidence remain OPEN.

## HANDOFFS TO OTHER SPECIALISTS
I067 supplies transaction truth; CD086 must name exact baseline/consequence; C080 must preserve state distinctions; W080 must capture focus/scroll before and after Reset; Type must not compress wording to preserve a preferred layout.