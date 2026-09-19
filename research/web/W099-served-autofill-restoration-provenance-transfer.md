# W099 — Served Autofill, Restoration, and Validation Provenance Transfer

Date: 2026-09-19
Stage: Stage 3 PRACTICE
Evidence purpose: INDEPENDENT VALIDATION + TRANSFER VALIDATION

## RELATED DOMAIN CHECK
I086 owns task/state authority; L090 owns geometry; C099 owns visual states; CD105 owns content; Type owns rendering. Web owns served browser/runtime evidence.

## RUNTIME CONTRACT
Record separately: HTML/framework field identity; `autocomplete`/input-purpose metadata where applicable; browser-filled/restored value; application-restored value; user edit; validation result; dirty branch; commit transaction; persistence/sync truth. Presence of a browser-filled value is not application validation, commit or save evidence.

Sources: https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#autofill ; https://www.w3.org/WAI/WCAG22/Understanding/redundant-entry.html ; https://www.w3.org/WAI/WCAG22/Understanding/identify-input-purpose.html

## CLOSURE LADDER
Use actual LogMate implementation → production Web build → served primary engine → independent engine → 200% → forced colors. Do not add an isolated Chromium micro-test as substitute.

For each scenario ID record build/route/document identity, field semantic ID, browser/app provenance, DOM/control value, validation state, dirty/checkpoint branch, focus identity, visible+a11y result, L090 geometry, commit/projection hash and recovery eligibility. Replicate executable families twice.

## SCENARIOS
Repeated valid value; invalidated prior value; browser autofill then overwrite; app-restored draft; Back/Forward restoration; Reset; reload/new document; review-before-commit; EN/KO; 200%; forced colors. Keep password-manager/vendor heuristics separate unless the product actually uses those field classes.

## FAILURE CONDITIONS
Browser fill treated as Saved; restored value bypasses validation; inconsistent semantic IDs across engines; Reset leaves hidden stale value; forced-colors erases focus/error distinction; same-process repeated information has no selection/auto-population path without a documented WCAG exception.

## PERFORMANCE EVIDENCE
Lighthouse/DevTools/CI synthetic remains LAB. Only provenance-bearing field/RUM aggregate may support field LCP/INP/CLS; this form study does not create field Core Web Vitals evidence.

## OPEN EVIDENCE
Independent-engine runtime, physical mobile keyboard/autofill, screen reader, representative-human comprehension/workload and actual field performance remain OPEN until executed.