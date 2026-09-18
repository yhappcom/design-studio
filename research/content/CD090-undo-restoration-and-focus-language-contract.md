# CD090 — Undo Restoration and Focus Language Contract

## Purpose
Extend CD089 to the inverse recovery edge: Undo may restore a field/group without moving focus to it. Content must describe product-state consequence, not invisible focus mechanics unless those mechanics are themselves necessary instructions.

## RELATED DOMAIN CHECK
I071 owns Undo/focus behavior; L075 geometry; C084 state encoding; W083 runtime; T052 rendering. Content does not invent focus restoration to make feedback sound complete.

## Semantic source model
`transaction_id + restored_object_id + restoration_result + current_focus_object_id/action_id + recovery_scope + persistence_truth`.

Protected invariants:
- restored ≠ focused;
- visible again ≠ selected;
- Undo applied ≠ Saved/Synced;
- Undo restored configuration ≠ returned you to that field;
- focus stayed on recovery control ≠ restoration failed.

## Practice / critique
Prefer consequence-first feedback such as restoration of the display configuration; do not narrate `Focus moved...` unless the movement itself is required to understand or continue the workflow. Visible concise feedback and richer accessibility payload may differ in detail while sharing the same semantic source.

Reject messages that claim `Returned to <field>` when only visibility/order was restored, or `Saved` when persistence truth is absent. Avoid direction-only wording that breaks under layout direction/localization.

## Reproducible validation
Run CD090 payloads through middle/end hide→Undo, group recovery, Reset→Undo and 200% recomposition. Check English source, expansion stress, layout-direction neutrality, object naming, status-role payload and consistency with actual I071 focus owner. Multilingual production execution remains required before PASS.

## Evidence boundary / OPEN
No multilingual runtime, linguistic review, screen-reader comprehension or representative-pilot task PASS is claimed.

## HANDOFFS TO OTHER SPECIALISTS
Type receives protected strings/expansion stress; Layout receives unavoidable wrapping; Color must not encode `restored` as `focused`; Web verifies visible/accessibility payload; Interaction resolves any ambiguous recovery scope before wording is finalized.