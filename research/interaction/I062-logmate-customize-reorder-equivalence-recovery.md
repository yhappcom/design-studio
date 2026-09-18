# I062 — LogMate Customize Reorder Equivalence & Recovery

Date: 2026-09-18
Mode: **TRANSFER VALIDATION**
Stage: 3 PRACTICE / NOT PASSED

## Question
Does LogMate Customize preserve agency and semantic safety when configuration applies immediately, especially for reorder, hide/show and Reset?

## SOURCE
The current LogMate configuration contract says visible items are reorderable, hidden items retain stable catalog order, switches and reorder apply immediately, Back does not roll back, there is no Apply/Save/Cancel, Reset restores Standard without deleting record values or Custom Field definitions, and at least one top-level item remains visible.

Current widget tests exercise live reorder before pointer-up, reversal within the same gesture, semantic total alignment, visibility-driven overflow changes and Reset. This is executed interaction evidence in a temporary session shell, not persisted production configuration.

WCAG 2.2 SC 2.5.7 requires functionality using dragging to be achievable by a single pointer without dragging unless dragging is essential. Column order is not intrinsically a spatial-value input, so the product should provide an equivalent non-drag path rather than treating drag as essential. SC 2.5.8 also sets the 24×24 CSS-pixel target-size baseline for pointer targets, subject to its exceptions.

## PRACTICE — state machine
`STANDARD → CUSTOMIZED_SESSION → {SHOW/HIDE, REORDER, GROUP_TOGGLE}* → RESET_STANDARD`

Critical invariants:
- hidden ≠ deleted;
- reorder ≠ semantic remap;
- group move ≠ child split;
- Back ≠ rollback;
- Reset ≠ record deletion;
- at least one top-level item remains visible;
- presentation configuration ≠ Add Flight entry-field configuration.

## NON-DRAG EQUIVALENCE CONTRACT
Every reorderable visible item needs an operable alternative that can express the same ordering without a dragging movement. Candidate implementations may include Move earlier/later controls or an accessible reorder action menu. The study does not prescribe the UI; it prescribes equivalence.

Acceptance evidence must show:
1. same semantic order result as drag;
2. keyboard operability and visible focus;
3. no loss of group identity;
4. announced/visible confirmation of the new position where appropriate;
5. targets meeting the applicable WCAG 2.2 target-size requirement;
6. no dependency on color or motion alone.

## IMMEDIATE-CHANGE RISK
Because changes commit immediately, the absence of Save is not itself a defect. The risk is a mismatch between the user's mental model and actual persistence. Once persistence exists, navigation away, app restart, offline state, sync arrival and cross-device conflict must all make the committed state predictable. If undo is introduced later, it must reverse presentation metadata only.

## CRITIQUE
The current live drag evidence is strong for direct manipulation fidelity, but it cannot establish accessibility or recoverability by itself. A visually excellent insertion indicator does not satisfy non-drag equivalence. Likewise, Reset must not become a destructive-looking action if its scope is only presentation configuration.

## RELATED DOMAIN CHECK
- **Type:** reorder controls and position announcements must survive enlarged text without shrinking typography.
- **Color:** drag lift/insertion/focus/selected states need non-color redundancy.
- **Layout:** alternate reorder controls must fit the Customize surface without creating a second dense interaction plane.
- **Web:** verify pointer, keyboard and touch paths in real browsers.
- **Content:** action labels must distinguish Hide, Remove, Reset and Delete; only the first/third are relevant here.

## HANDOFFS TO OTHER SPECIALISTS
Web should make SC 2.5.7 a browser closure gate for Customize. Content should define presentation-safe Reset/Hide language. Layout should reserve space for an equivalent reorder mechanism. Color should validate focus/selection/insertion states.

## OPEN
Persistence, sync conflict, non-drag reorder implementation, screen-reader announcement, touch-device evidence, representative-pilot discoverability/workload.

## Conclusion
I062 makes non-drag reorder equivalence a required product-transfer gate. Current drag tests are positive direct-manipulation evidence, not Interaction Stage 3 closure.