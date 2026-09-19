# I097 — Non-drag reorder authority and recovery

## PURPOSE
Close the highest-value executable design gap left by I096: define a single-pointer, non-drag reorder contract for LogMate Customize without pretending that keyboard support substitutes for WCAG 2.2 SC 2.5.7.

## RELATED DOMAIN CHECK
- Type: T078/T021 checked; control labels and ordinal/position strings must use mature fallback while T021 is open.
- Color: C109 checked; selected/moving/committed/recovered states cannot rely on color alone.
- Layout: L100 checked; local action ownership and focus visibility remain protected.
- Web: W109 checked; runtime evidence must be served-product evidence, not static mockup evidence.
- Content: CD115 checked; action/result/recovery wording must follow actual transaction truth.

## SOURCE
WCAG 2.2 SC 2.5.7 requires functionality using dragging to be achievable with a single pointer without dragging unless an exception applies. W3C technique G219 gives stepwise up/down controls or a destination-selection control as sufficient-pattern examples. Keyboard equivalence alone does not satisfy this pointer requirement. SC 2.5.8 separately requires pointer targets to meet 24×24 CSS px or an applicable spacing/equivalent/inline/user-agent/essential exception.

## SYNTHESIS — authority model
`item identity ≠ selected item ≠ proposed destination ≠ previewed order ≠ committed order ≠ persisted order ≠ recovered order`.

A non-drag path must operate the same underlying reorder function as drag, not a visually similar but semantically different copy.

### Candidate A — stepwise move
1. Activate item action.
2. Expose Move up / Move down as applicable.
3. Each activation commits one deterministic position change.
4. Preserve focus on the moved item's action context.
5. Announce position result without forcing focus to a status message.

### Candidate B — destination selection
1. Activate Move.
2. Choose an explicit destination/position.
3. Review destination if consequence is materially ambiguous.
4. Commit once.
5. Preserve item identity and expose recovery.

Both can satisfy the single-pointer principle; neither is promoted before product execution.

## CRITIQUE / FAILURE CONDITIONS
FAIL if:
- drag is the only pointer path;
- keyboard arrows are offered but no click/tap alternative exists;
- controls appear only after hover;
- position is conveyed only by animation/color;
- the moved item loses identity or focus unpredictably;
- a disabled boundary action remains presented as available;
- visual order changes while persisted order does not, without an explicit pending/unsaved state;
- Undo restores appearance but not canonical order;
- target geometry fails SC 2.5.8 without a valid exception.

## REPRODUCIBLE VALIDATION
Fixture: 7 named LogMate fields with stable IDs; move first/middle/last items; repeated step moves; destination jump; cancel; Undo; save; route away/back; reload; offline/persistence failure.

For each run capture: item IDs/order before and after, action invoked, focus owner, visible/accessibility status, target rectangles, transaction/inverse ID, persistence result. Run baseline, enlarged text, text-spacing, narrow reflow, primary engine twice, then independent engine.

## UX BOUNDARY
This is non-human structural/accessibility analysis. It does not establish discoverability, preference, speed, workload, error rate, or pilot comprehension.

## HANDOFFS TO OTHER SPECIALISTS
- Layout: provide geometry for stepwise and destination candidates without hiding controls or losing item/action ownership.
- Content: provide position/action/result/recovery semantics.
- Color: distinguish selected/moved/pending/error/recovered states without color-only meaning.
- Type: stress `Move up`, `Move down`, `Move to position`, `3 of 7`, long field names.
- Web: execute both candidates in served runtime and collect provenance.

## OPEN
Actual LogMate implementation; independent-engine/physical-device/AT/human evidence; final choice between candidate A/B; persistence behavior.