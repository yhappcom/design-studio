# C099 — Autofill, Restored Value, and Validation State Separation

Date: 2026-09-19
Stage: Stage 3 PRACTICE
Evidence purpose: TRANSFER VALIDATION

## RELATED DOMAIN CHECK
I086 owns value provenance and validation authority; L090 owns geometry; CD105 owns language; W099 owns browser/runtime evidence; Type owns rendering.

## STATE MODEL
Keep `focus`, `browser autofill/restored`, `application-restored draft`, `user-edited dirty`, `valid`, `invalid`, `committed`, `saved/synced`, and `disabled/readonly` as separate axes. Browser autofill styling is implementation/browser evidence, not product validation or success semantics.

## PRACTICE
For light/night/forced-colors candidates, compare empty, browser-filled, app-restored, user-overwritten, invalidated, validated and committed fields at baseline/200%. Every meaningful product state must retain a non-color semantic channel. Focus must remain distinguishable from invalid/warning/restored state.

WCAG 2.2 reference points remain SC 1.4.1 Use of Color, SC 1.4.11 Non-text Contrast, SC 2.4.7 Focus Visible and the applicable form/error criteria.

Source: https://www.w3.org/TR/WCAG22/

## FAILURE CONDITIONS
FAIL if browser autofill highlight is interpreted as product success; restored value receives Saved styling; invalid state is color-only; forced colors merges focus and invalid state; stale success paint survives Reset/Back/Forward; or recycled field/ordinal receives another object's dirty state.

## VALIDATION BOUNDARY
No rendered C099, forced-colors, independent-engine, calibrated-display, observer or human PASS is claimed until actual runtime evidence exists.

## HANDOFF
L090 measures focus/error geometry; CD105 keeps provenance out of copy unless action/recovery changes; W099 captures actual browser styling/runtime; Type must not compress strings to preserve color-chip geometry.