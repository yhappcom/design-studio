# I065 — Reorder Reversibility, Transaction & Recovery Contract

Status: **PRACTICE / OPEN PRODUCT TRANSFER**  
Purpose: **EXTENSION + TRANSFER VALIDATION** of I063/I064 from mutation correctness to reversible professional configuration.

## RELATED DOMAIN CHECK
- **Type T046**: position/status strings create density but may not be solved by Type compression.
- **Color C077**: focus/selection/disabled states remain orthogonal after mutation; transient recovery adds a new state without replacing them.
- **Layout L068**: post-move locus/scroll geometry is protected; recovery UI must not obscure the moved item or destabilize the list.
- **Web W077**: browser evidence already captures mutation identity/focus/status; transaction/recovery evidence can reuse the same scenario identity.
- **Content CD083**: structured move-result truth is the source for consequence feedback; wording cannot invent persistence or reversal guarantees.

## SOURCE
WCAG 2.2 SC 2.5.7 requires a non-drag single-pointer alternative for authored drag functionality. WCAG 4.1.3 requires status messages to be programmatically determinable without taking focus. WAI APG rearrangeable-list examples demonstrate separate move controls and a last-change status, but APG examples explicitly require product/AT testing before production use.

## Problem
A reorder path can preserve final order and focus yet still be operationally brittle if an accidental move cannot be reversed cheaply, if Reset is overloaded as undo, or if the user cannot tell whether a mutation is local, committed, persisted, or merely displayed.

## Transaction model
For a display-configuration mutation, keep these truths separate:
1. `ORDER_BEFORE`
2. `MOVE_REQUESTED`
3. `MOVE_APPLIED_LOCAL`
4. `MOVE_REJECTED_BOUNDARY`
5. `UNDO_AVAILABLE`
6. `UNDO_APPLIED`
7. `SESSION_RESET_REQUESTED`
8. `DEFAULTS_RESTORED`
9. `PERSISTENCE_PENDING` — only when persistence exists
10. `PERSISTENCE_CONFIRMED` / `PERSISTENCE_FAILED` / `PERSISTENCE_AMBIGUOUS` — only when implemented.

`Reset` is not `Undo`: Undo reverses the immediately attributable mutation; Reset restores a defined configuration baseline and may affect many prior choices.

## Reversibility oracle
Given starting order S and valid move M producing S′:
- immediate Undo must return semantic order exactly to S;
- unaffected-item relative order remains invariant;
- hidden items remain hidden and are not deleted;
- focus remains on the same semantic item or on the explicit Undo control only while the user intentionally operates it, then returns coherently;
- boundary-rejected moves create no fake Undo transaction;
- repeated `M → Undo` twice must be idempotent at the semantic-order level;
- Reset must be tested separately and must not be described as Undo.

## Competing interaction architectures
### A. Immediate mutation + contextual Undo
Fast repeated configuration; requires clear transaction scope and non-obscuring recovery surface.

### B. Session draft + Apply/Cancel
Strong batch reversibility but adds mode/state and risk of unsaved-change ambiguity.

### C. Immediate mutation + explicit history/revert
Powerful but excessive unless persistence/history requirements justify it.

No architecture is selected without product implementation and task evidence. For current temporary LogMate Customize, A is the lowest-complexity candidate **only if** product truth confirms immediate mutation semantics.

## Reproducible validation ledger
For each scenario capture:
`scenario_id, build, input_path, order_before, requested_move, order_after, focused_semantic_id, undo_available, undo_action, order_after_undo, focus_after_undo, scroll_before/after, status_payload, runtime_exception`.

Run at least twice for non-drag pointer and keyboard; add drag only as a parallel path, never as the only path.

## CRITIQUE
A green final-order test is insufficient: it can hide accidental-move recovery cost. Conversely, automatically adding Undo without a defined commit model can misrepresent product truth. Reversibility is an Interaction contract first, not a microcopy or snackbar styling decision.

## OPEN
- Actual non-drag pointer reorder implementation.
- Product decision on immediate commit versus session draft.
- Persistence/sync semantics.
- AT announcement behavior and human discoverability/workload.
- Physical touch-device behavior.

## HANDOFFS TO OTHER SPECIALISTS
- **Content**: distinguish moved, undone, reset, persisted and ambiguous states.
- **Layout**: compare inline/contextual recovery placement against focus obscuration and 200% reflow.
- **Color**: recovery availability must not collapse with focus/selection/disabled semantics.
- **Web**: add undo round-trip to the same served-browser mutation manifest.
- **Type**: treat recovery/status strings as transfer corpus only; do not compensate unfinished drawing.