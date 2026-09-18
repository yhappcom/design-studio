# I071 — Undo Restoration Focus Agency Contract

## Purpose
Extend I070 from disappearance fallback to the inverse transition: an Undo can restore a hidden/removed semantic object without implying that keyboard focus should automatically jump back to it. This is TRANSFER VALIDATION of agency and recovery, not product-runtime PASS.

## SOURCE
WCAG 2.2 remains the accessibility baseline. Focus Visible and Focus Not Obscured constrain the focused destination, but do not prescribe that undoing a visibility mutation must restore focus to the restored object. WAI-ARIA patterns provide pattern-specific focus movement, not a universal Undo algorithm. Therefore restoration policy remains an Interaction/product contract.

## RELATED DOMAIN CHECK
T052, C083, L074, W083 and CD089 checked. I070 owns fallback when an object disappears. I071 adds the inverse recovery edge. Layout owns resulting geometry, Content owns consequence wording, Color owns visible state, Web owns runtime proof. No separate UX owner is created.

## Core distinction
Configuration restoration and focus restoration are independent state transitions.

For `O visible/focused → Hide O → fallback F → Undo`:
- Undo MUST restore the declared configuration state if the transaction is eligible.
- Undo MUST NOT silently infer `focus → O` merely because O reappears.
- If Undo is invoked from a dedicated recovery control `U`, default studio hypothesis is to preserve focus on `U` when it remains operable; moving to O requires an explicit workflow rationale.
- If Undo is invoked by a keyboard command while focus remains on fallback `F`, preserve `F` unless product evidence establishes a stronger continuation rule.
- If the current focus owner becomes invalid as a consequence of Undo, run the same declared fallback machinery rather than ordinal inheritance.

This is a studio hypothesis to test, not a WCAG requirement.

## Reproducible sequences
Execute twice per available input path:
1. middle field O focused → Hide O → fallback next F → Undo from recovery control;
2. last field O focused → Hide O → fallback previous F → Undo;
3. group child O focused → collapse group → group/neighbor fallback → Undo/expand recovery;
4. Reset hides O → fallback F → Undo Reset;
5. Hide O → fallback F → user performs another action on F → Undo earlier mutation where supported;
6. 200% recomposition between disappearance and Undo.

Capture transaction ID, restored semantic object ID, current focus semantic object/action ID, invoking control ID, focus scope/history, projection membership, traversal successor, status payload, scroll/reveal delta and whether the recovery control remains operable.

## Failure conditions
FAIL if configuration restoration is mistaken for focus restoration; Undo steals focus without a declared rationale; focus returns to a stale ordinal rather than semantic owner; focus lands on a hidden/disabled target; or a recovery announcement requires focus theft to be perceivable.

## Evidence boundary / OPEN
No LogMate Undo-focus runtime, non-drag reorder, AT, physical-device or representative-pilot PASS is claimed. Whether pilots prefer focus return to the restored field is a human-workflow question and remains OPEN.

## HANDOFFS TO OTHER SPECIALISTS
Layout measures whether preserving the recovery/fallback locus prevents disruptive scroll. Color distinguishes restored object visibility from actual focus. Content separates `restored` from `focus moved`. Web must prove active semantic identity before/after Undo. Type must accommodate recovery strings without compensating for behavioral ambiguity.