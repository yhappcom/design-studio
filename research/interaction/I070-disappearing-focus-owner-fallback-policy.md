# I070 — Disappearing Focus Owner Fallback Policy

## Purpose
Extend I069 from surviving semantic identity to the harder case where the focused semantic object/action ceases to be focusable after hide, group collapse, Reset, or projection change. This is TRANSFER VALIDATION, not a claim that LogMate already implements the required path.

## SOURCE
Flutter's focus guidance states that `unfocus()` always transfers focus somewhere; explicit focus is preferred when the destination matters, and falling to the root scope can damage traversal. `FocusScope` retains focus history. WAI-ARIA APG patterns for deletable tabs and rearrangeable listboxes demonstrate a stronger workflow principle: when the current object disappears, focus moves to a logical surviving neighbor or workflow destination, while repeated move operations keep focus on the moved object.

## RELATED DOMAIN CHECK
T051, C082, L073, W082 and CD088 checked. I069 remains authority while the object survives. L073 owns resulting geometry; Content names the consequence; Color renders the new owner; Web must prove browser/semantics identity. No new UX specialist path is created.

## State model
For mutation `M` on focused semantic object/action `(O,A)`:
1. If `(O,A)` survives and remains operable, preserve that exact semantic owner.
2. If `O` survives but `A` becomes unavailable, choose an explicitly defined operable action on `O`; do not let ordinal index choose accidentally.
3. If `O` becomes hidden/removed from the active projection, choose a deterministic logical survivor: preferred next semantic neighbor, otherwise previous neighbor, otherwise the owning section/control that can continue the workflow.
4. If the active projection becomes empty, move to an explicit workflow destination outside the collection.
5. Boundary rejection/no-op does not create a disappearance and therefore must not trigger fallback.

The exact fallback hierarchy is a product contract, not a WCAG-prescribed algorithm. It must be declared before runtime PASS.

## Reproducible validation matrix
Run each available input path twice: focused row action → hide same field; focused last-visible field → attempted hide; focused child → collapse group projection; focused field → Reset where field becomes hidden; Undo restoring the field; 200% recomposition. Capture pre/post semantic object/action ID, projection membership, chosen fallback reason, focus scope/history, next/previous semantic neighbors, available actions, status/recovery transaction and traversal continuation.

FAIL if focus lands on a different object merely because it inherited the same ordinal index; falls to root/body without a declared workflow reason; targets hidden/disabled semantics; or causes traversal restart unrelated to the mutation.

## Evidence boundary / OPEN
No LogMate non-drag reorder, hide-focused-object, group-collapse, Reset/Undo fallback runtime, AT, physical-device or representative-pilot PASS is claimed. Human discoverability/workload remains deferred.

## HANDOFFS TO OTHER SPECIALISTS
Layout measures reveal/scroll after I070 chooses the semantic destination. Color must follow the chosen owner, not stale paint/index state. Content must distinguish disappearance/recovery from success wording. Web must bind Flutter focus identity to browser accessibility identity. Type must not compress labels to avoid this behavioral problem.