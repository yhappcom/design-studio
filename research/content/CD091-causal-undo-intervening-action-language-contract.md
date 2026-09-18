# CD091 — Causal Undo and Intervening-Action Language Contract

Date: 2026-09-18
Stage: Stage 3 PRACTICE
Purpose: TRANSFER VALIDATION from I072.

## RELATED DOMAIN CHECK
Interaction I072 owns transaction eligibility and focus agency. Layout L076 owns placement/reflow. Color C085 owns visual-state separation. Type T054 receives protected strings after drawing gates. Web W085 must prove runtime semantics/localization.

## SOURCE
WCAG 2.2 SC 4.1.3 requires qualifying status messages to be programmatically determinable without taking focus. WCAG does not define LogMate's Undo transaction policy or wording.

## CONTENT MODEL
Message source truth:
`transaction_id + inverse_of + changed_object_id + restoration_result + undo_eligibility + current_focus_object/action + intervening_action_present + recovery_scope + persistence_truth`.

Protected invariants:
- restored ≠ focused;
- Undo applied ≠ returned to restored field;
- later focus/action ≠ undone merely because an earlier mutation is reversed;
- unavailable ≠ failed ≠ superseded;
- local change ≠ Saved ≠ Synced;
- hidden ≠ deleted;
- Reset ≠ Undo ≠ erase.

## PRACTICE
Prepare runtime candidates by truth state, not visual position:
- immediate successful Undo: identify what changed when useful;
- successful Undo after later focus/action: report restoration without claiming focus return;
- stale/superseded Undo: explain unavailability only when user action requires feedback;
- no-op guard: do not emit false success;
- Reset supersession: never describe old transaction as still recoverable if Interaction invalidated it.

Visible feedback may be concise while an accessibility payload is richer, but both must derive from the same semantic payload.

## CRITIQUE
Avoid generic `Done`/`Restored` when the object/consequence is ambiguous. Avoid `Returned to X` unless focus actually moved to X by declared Interaction policy. Avoid `Saved`/`Synced` until persistence truth exists. Do not mention color, direction or visual ordinal as the sole locator.

## REPRODUCIBLE VALIDATION
When runtime exists, bind each I072 scenario ID to visible string, accessibility status payload, semantic object ID, locale, text direction, viewport and 200% condition. Compare at least actual English/Korean runtime before broader localization claims. Human linguistic review, AT comprehension and pilot task evidence remain separate OPEN gates.

## HANDOFFS TO OTHER SPECIALISTS
Web integrates strings/status semantics; Layout receives expansion pressure; Type receives corpus; Color must preserve non-color meaning; Interaction remains authority for truth and eligibility.