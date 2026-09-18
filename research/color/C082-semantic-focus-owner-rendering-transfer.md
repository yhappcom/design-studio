# C082 — Semantic Focus-Owner Rendering Transfer

## Purpose
Extend C081 from post-Reset state orthogonality to a stricter rule: visual focus treatment must follow the semantic focus owner established by I069, not stale row index, selection, insertion or hover state.

## RELATED DOMAIN CHECK
I069/L073, Type T050, Web W081 and Content CD087 checked. This is TRANSFER VALIDATION of Interaction identity into Color rendering.

## SOURCE
WCAG 2.2 SC 2.4.11 requires focused components not be entirely obscured at AA. SC 2.4.13 provides an AAA focus-appearance size/contrast criterion. These do not replace the studio requirement to render focus on the correct semantic object.

## State matrix
Cross `semantic_focus_owner × selected × shown/hidden × move-boundary enabledness × recovery availability × hover/pressed × insertion destination × theme/forced-colors`.

Failure conditions include: focus ring remains at an old visual index after reorder; selected styling is mistaken for focus; hidden/disabled opacity erases focus identity; drag insertion color persists after mutation and looks like focus; Reset recovery receives accent while actual keyboard focus is elsewhere without a distinct cue.

## PRACTICE / validation
Once I069 is executable, capture before/after semantic focus ID plus rendered focus owner in light/night/forced-colors. Test reorder, hide/show, Reset, Undo and 200% recomposition. Use non-color cues and accessible meaning; color-only state identity is insufficient.

Classify `OWNER-MATCH`, `OWNER-MISMATCH`, `CUE-COLLISION`, `BLOCKED`, `NOT-EXECUTED`. Forced-colors emulation remains browser transfer evidence, not human perception evidence.

## OPEN
No rendered C082 runtime evidence, independent engine, calibrated display, observer or representative-human evidence yet.

## HANDOFFS TO OTHER SPECIALISTS
Interaction supplies semantic focus truth; Layout supplies geometry; Web proves actual browser paint/state; Content avoids color-dependent wording; Type supplies text rendering only after its own gate.