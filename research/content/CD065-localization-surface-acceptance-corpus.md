# CD065 — Localization & Surface Acceptance Corpus

Status: STAGE 3 PRACTICE / TOOLCHAIN EXECUTION OPEN  
Date: 2026-09-17

## PURPOSE
Make CD064 executable by defining a bounded corpus that must preserve financial meaning across source, locale, visible UI, accessibility, history and export surfaces.

## RELATED DOMAIN CHECK
T028 owns render/fallback pressure; C059 visual redundancy; L050 adjacency/reflow; I046 actual state/action/recovery; W059 runtime packaging. Content does not redefine those contracts.

Analytical purpose: TRANSFER VALIDATION preparation for CD059/CD064.

## CORPUS — truth distinctions that must survive
1. portfolio value vs invested capital;
2. total performance vs cumulative distributions;
3. distribution vs profit;
4. gross vs net / before-tax vs after-tax;
5. estimated ROC vs final ROC;
6. partial data vs unavailable data vs numeric zero;
7. refund vs additional tax adjustment;
8. pending vs known failure vs ambiguous outcome;
9. destructive consequence vs reversible/undoable consequence;
10. source-screen state vs history/export representation.

## SURFACE MATRIX
For each corpus item record:
- semantic message ID;
- source-language realization;
- locale realization;
- variables and formatting ownership;
- visible label/value/qualifier;
- accessible name/description/status announcement where applicable;
- error/recovery message;
- history label;
- export field/header/value;
- truncation/wrap result;
- discrepancy class and canonical owner.

## DISCREPANCY CLASSES
Retain CD064 semantic-collapse failures and add: SURFACE_DRIFT, LOCALE_STATE_COLLISION, VARIABLE_FORMAT_DRIFT, ACCESSIBLE_NAME_LOSS, HISTORY_EXPORT_DRIFT, ACTION_CONSEQUENCE_MISMATCH.

A shorter localized string is acceptable only if semantic distinctions and consequence remain intact. A longer string is not a Content defect merely because a preferred one-line layout fails.

## PRACTICE / CRITIQUE
Use KRW/USD, signed/zero/large values, long labels, estimated/final ROC, partial/unavailable, tax adjustment and ambiguous network outcome. Verify that visible and nonvisual surfaces do not silently convert unknown to zero or ambiguous outcome to failure/success.

## TOOLCHAIN CONTRACT
Actual closure requires Flutter localization/ARB/TMS-equivalent round trip or the project's real localization pipeline. Preserve message IDs, placeholders/types, locale output and runtime screenshots/semantics under W059 identity. Static hand-written translations are preparation, not product localization PASS.

## HANDOFFS
Type receives rendering/fallback issues; Layout receives fit/adjacency; Interaction receives state/consequence mismatches; Color receives missing redundant semantic cues; Web packages runtime/browser artifacts.

## EVIDENCE BOUNDARY
No Content Stage 3 PASS, real Flutter/TMS/ARB round trip, linguistic review, AT comprehension or representative-human task-performance PASS is claimed.