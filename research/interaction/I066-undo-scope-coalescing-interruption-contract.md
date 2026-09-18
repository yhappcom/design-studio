# I066 — Undo Scope, Coalescing & Interruption Contract

Status: **STAGE 3 PRACTICE / OPEN RUNTIME**  
Purpose: **EXTENSION + CONTRADICTION REVIEW** of I063–I065: reversibility is not defined until Undo scope and interruption behavior are explicit.

## RELATED DOMAIN CHECK
Type T047 protects recovery strings from compression. Color C078 separates recovery availability from focus/selection. L069 compares recovery surfaces. W078 defines browser recovery evidence. CD084 separates Undo, Reset and persistence truth. No separate UX owner exists; end-to-end UX remains cross-cutting.

## SOURCE
WCAG 2.2 is the current W3C baseline. SC 3.3.4 applies when user-controllable stored data is modified/deleted and permits reversibility/checking/confirmation; current LogMate display configuration must not be claimed under that criterion until persistence truth exists. W3C supplemental cognitive guidance recommends predictable back/undo and avoiding data loss, but it is supplemental rather than a conformance requirement.

## Problem
I065 proves that one move can be reversed. It does not answer what happens after repeated moves, a second object mutation, navigation, timeout, Reset, or future persistence. A visible Undo with undefined scope can restore the wrong state while still looking successful.

## Transaction model
For each mutation record: `transaction_id`, `semantic_id`, `before_order`, `after_order`, `input_path`, `timestamp/order`, `undo_eligible`, `superseded_by`, `interruption_reason`.

Test three policies rather than assuming one:
1. **Atomic last-action Undo** — every move is one reversible transaction.
2. **Coalesced object Undo** — consecutive moves of the same semantic item form one transaction returning to its pre-sequence position.
3. **Session history Undo** — multiple mutations form a stack.

## Required sequences
- `S0 → A+1 → Undo`.
- `S0 → A+1 → A+1 → A+1 → Undo`.
- `S0 → A+1 → B-1 → Undo → Undo`.
- move → boundary rejection → Undo.
- move → Reset → Undo attempt.
- move → navigation away/back → Undo attempt.
- future only: move → persistence pending/failure/ambiguous/success → Undo.

## Acceptance
- The product declares one policy; visible wording and behavior match it.
- Undo never targets a different semantic item because list indices changed.
- Boundary rejection creates no fake reversible transaction.
- Reset has an explicit relationship to prior Undo history; no silent resurrection of an unintended configuration.
- Interruption either preserves a valid recovery path or clearly invalidates it without claiming success.
- Focus/status identify the semantic object and resulting state, not merely a visual index.

## CRITIQUE
A single snackbar Undo is not automatically simple: repeated moves can replace the prior message faster than the user can reason about transaction scope. Conversely, a full history stack can add cognitive and implementation complexity unsupported by current product need. Policy must follow workflow risk and evidence.

## OPEN
No policy is selected or passed. Current product persistence/Sync truth is absent; AT, human error frequency, workload and pilot validation remain OPEN.

## HANDOFFS TO OTHER SPECIALISTS
Layout receives lifetime/placement pressure; Content receives exact transaction-scope truth; Color receives expiry/supersession states; Web receives interruption manifest requirements; Type receives only resulting strings after semantics are fixed.
