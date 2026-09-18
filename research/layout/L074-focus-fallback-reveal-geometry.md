# L074 — Focus Fallback Reveal Geometry

## Purpose
Extend L073 to mutations where I070 determines that the previous semantic focus owner no longer exists in the active projection. Spatial acceptance begins only after Interaction has selected the correct fallback owner.

## RELATED DOMAIN CHECK
I069/I070, T051, C082, W082 and CD088 checked. This is TRANSFER VALIDATION of semantic fallback into spatial continuity, not a new behavioral owner.

## Practice model
Measure three distinct outcomes after hide/collapse/Reset: (A) logical next/previous neighbor already visible; (B) correct fallback requiring minimal reveal; (C) collection disappears and focus moves to owning section/workflow control. For each, capture pre/post focus and target rectangles, viewport, scroll offset/delta, sticky/safe-area overlap, wrapping, 200% text condition and semantic-neighbor relationship.

## Critique criteria
PASS candidate: I070 destination is visible or minimally revealed without unrelated large displacement, remains operable, and does not become obscured by author-created sticky/recovery surfaces. FAIL: geometry looks stable but the semantic owner is wrong; correct owner is fully obscured; reveal causes avoidable context loss; or 200% recomposition places recovery/controls over the new focus locus.

WCAG 2.2 Focus Not Obscured (Minimum) is a floor, not proof of professional workflow continuity. Correct semantic fallback and bounded spatial displacement remain separate acceptance axes.

## Reproducible validation
Execute each I070 disappearance family twice at baseline and 200%: middle field hide, end field hide, group collapse, Reset-hide, Undo-restore. Record semantic destination before interpreting geometry.

## OPEN
No rendered LogMate L074 execution, forced-colors, independent-engine, physical-device or human spatial/workload evidence.

## HANDOFFS TO OTHER SPECIALISTS
Interaction supplies fallback identity/reason. Color follows the new owner. Web captures actual rectangles/scroll. Content must not imply the old object remains active. Type pressure returns here unless reproduced glyph/metric evidence proves a Type fault.