# C077 — Reorder Post-Mutation Focus-State Integrity

Date: 2026-09-18
State: STAGE 3 PRACTICE / TRANSFER SPECIFICATION

## Question
C076 separated reorder state axes. I064 adds a temporal requirement: after a row moves, does the visible state continue to identify the moved/focused object without collapsing focus, visibility, selection or boundary availability into one color treatment?

## SOURCE
WCAG 2.2 is the current studio baseline. Focus Visible is required at AA; WCAG 2.2 also adds Focus Not Obscured (Minimum). Target Size (Minimum) and Dragging Movements constrain the same control family. W3C supplemental cognitive guidance recommends avoiding unexpected movement unless user initiated.

Sources:
- https://www.w3.org/TR/WCAG22/
- https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/

## State matrix
Test combinations rather than isolated tokens:
- SHOWN + focused + movable both directions;
- SHOWN + focused + first-item boundary;
- SHOWN + focused + last-item boundary;
- HIDDEN + focused configuration row;
- focused moved item adjacent to selected/dragged/insertion state;
- focus after move under light, night and forced-colors;
- boundary-disabled control adjacent to enabled move control.

Acceptance chain remains: semantic token → paint owner → visible surface → non-color cue → accessible meaning. `TOKEN_PASS / RENDER_FAIL` is failure.

## PRACTICE / CONTRADICTION REVIEW
A post-move row may change location while retaining focus. If focus indication is implemented as a transient background that is also used for selection or drag insertion, the user can lose state identity after mutation. Likewise opacity-only disabled treatment can collide with HIDDEN semantics. Preserve orthogonal channels: focus geometry/outline, control enabledness, textual/icon signifier, and semantic state.

## REPRODUCIBLE VALIDATION
Use I064 semantic IDs and L068 before/after geometry. Capture rendered screenshots and computed/used styles in primary and independent engines, plus forced-colors. Verify focus remains perceivable after each mutation and is not visually confused with SHOWN/HIDDEN or insertion destination. Do not claim human perception from pixel/contrast checks alone.

## RELATED DOMAIN CHECK
Type T046 protects status/control rendering. Layout L068 owns post-mutation geometry. Interaction I064 owns focus/action state. Web W076/W077 runtime manifests own engine evidence. Content CD083 supplies non-color semantic feedback.

## HANDOFFS TO OTHER SPECIALISTS
Web should capture actual post-mutation paint/focus state, not token declarations. Layout should avoid clipping focus under dense wrapping. Content supplies redundant meaning. Interaction must expose boundary and focus state separately.

## OPEN
Actual non-drag controls, forced-colors runtime, independent engine, calibrated display, observer and human evidence.