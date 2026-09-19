# C097 — Route/history state separation

## Purpose
Prevent browser/navigation lifecycle from inventing product semantic color states.

## State model
Independent axes remain: focus, selection, candidate/preview, committed, cancelled/no-op, recovery, unavailable/stale. `history-restored`, `pageshow persisted`, scroll-restored and widget-rebuilt are implementation/lifecycle facts and receive no success/error color semantics by themselves.

## Practice / critique
Test light, night and forced-colors transfer with L088 scenarios. FAIL if a stale restored row inherits focus/selection paint from an ordinal slot; browser-restored form state appears as Saved/Synced; Back/Forward resurrects preview/success styling without current semantic truth; forced-colors collapses focus and stale/unavailable state.

## Accessibility boundary
WCAG 2.2 remains the baseline. Focus Visible and Non-text Contrast remain AA concerns; stronger focus treatment may be a Studio target but must not be mislabeled as the AA floor.

## RELATED DOMAIN CHECK
I084 authority, L088 geometry, CD103 semantics, T066 rendering, W097 served history evidence.

## Evidence boundary
No rendered forced-colors, independent-engine, calibrated-display, observer or human PASS is claimed.

## Sources
- https://www.w3.org/TR/WCAG22/
- https://developer.mozilla.org/en-US/docs/Web/API/Window/pageshow_event
