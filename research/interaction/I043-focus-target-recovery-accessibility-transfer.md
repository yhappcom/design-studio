# I043 — Focus, Target and Recovery Continuity under Recomposition

Status: TRANSFER VALIDATION / PRACTICE
Date: 2026-09-17

## SOURCE
WCAG 2.2 adds AA Focus Not Obscured (Minimum) and Target Size (Minimum), the latter using a 24×24 CSS px baseline with defined exceptions. Flutter's own release checklist recommends 48×48 tappable targets, intelligible screen-reader descriptions, undo/correction for important actions and usability at large scale factors.

## PRACTICE CONTRACT
When L047 recomposes a workflow, preserve logical focus order, visible/non-obscured focus, target operability, state announcement, error correction and recovery. A visual move must not silently alter task order. Destructive or financially consequential actions require explicit consequence and recovery where the product supports it.

## CRITIQUE
A screen can satisfy static spacing while failing interaction because a sticky surface covers focus, a compact icon remains visually present but too small to operate, or an error moves away from its correction after reflow.

## VALIDATION
For each W055 identity traverse keyboard focus and primary task path at default/max scaling and narrow/wide layouts. Record target geometry, obscuration, skipped/reordered focus, state feedback, error correction, cancellation/undo and history restoration. Human discoverability/comprehension remains OPEN.

## RELATED DOMAIN CHECK
T025 scaling drives recomposition; C056 prevents color-only feedback; L047 owns geometry/order; W056 captures runtime evidence; CD062 owns labels/consequence/recovery wording.

## Gate effect
No Stage 3 PASS; this is executable-target preparation, not a runtime or human usability claim.