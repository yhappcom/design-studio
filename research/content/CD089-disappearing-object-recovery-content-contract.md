# CD089 — Disappearing-Object Recovery Content Contract

## Purpose
Extend CD088 to mutations where the previously focused semantic object/action disappears from the active projection. Content must describe transaction truth without pretending that focus location, visual index, persistence or deletion semantics are the same thing.

## RELATED DOMAIN CHECK
T051, C082/C083, I069/I070, L073/L074 and W082 checked. Interaction owns the fallback state machine; Content owns its user-facing semantic realization.

## Semantic contract
Source payload: `transaction_id + changed_object_id + action/result + projection_result + fallback_focus_object/action + recovery_scope + persistence_truth`.

Protected invariants:
- hidden ≠ deleted;
- object removed from active projection ≠ record/data removed;
- changed object ≠ fallback-focused object;
- focus moved ≠ mutation succeeded;
- Undo restored object ≠ Saved/Synced;
- no-op/boundary rejection ≠ disappearance.

Visible feedback should normally foreground the mutation consequence, not narrate implementation focus mechanics. Accessibility payload may require richer position/context, but must remain bound to semantic IDs and actual state. Do not say “Moved to the next item” merely because focus moved there if the changed field was hidden.

## Localization/system practice
Keep object IDs and state enums locale-neutral. Localize full labels/actions/status separately from compact aviation headers. Test longer localized object names and action/result strings without allowing English word order or visual row index to select product state.

## Validation
Run hide-focused-object, group-collapse, Reset-hide, Undo-restore and no-op families through W083 runtime evidence. Compare concise visible feedback with richer accessibility payload. Static wording critique/string length does not equal AT comprehension or human task evidence.

## OPEN
No multilingual production runtime, linguistic review, screen-reader comprehension or representative-pilot task PASS.

## HANDOFFS TO OTHER SPECIALISTS
I070 supplies state truth; L074 owns placement/reveal; C083 renders focus; Type protects required strings; Web verifies actual semantic/accessibility payload.