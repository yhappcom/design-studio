# CD085 — Undo Scope, Expiry & Interruption Language Contract

Status: **STAGE 3 PRACTICE / OPEN RUNTIME**  
Purpose: **EXTENSION** of CD083–CD084 using I066 transaction truth.

## RELATED DOMAIN CHECK
I066 owns transaction scope/coalescing/interruption. L070 owns recovery placement/lifetime geometry. C078 owns visual state encoding. W078 owns runtime/browser evidence. T047 protects operational strings. Content does not invent persistence or history semantics.

## Semantic contract
Source payload: `transaction_id + semantic_id + operation + before_position + after_position + undo_scope + undo_available + invalidation_reason + persistence_state(if real)`.

Protected distinctions:
- `Undo last move` ≠ `Undo all moves for this field`.
- `Undo unavailable` ≠ `Undo failed`.
- `Superseded` ≠ `Expired` ≠ `Reset cleared history`.
- `Moved` ≠ `Saved`.
- `Reset layout` ≠ `Undo` ≠ erase flight data.
- boundary rejection ≠ successful move.

## Language strategies to test
1. Object + consequence: `PIC moved to position 7 of 35. Undo.`
2. Object + relational consequence: `PIC moved after SIC. Undo.`
3. Coalesced sequence, only if I066 chooses it: `PIC moved to position 9 of 35. Undo these moves.`

These are test fixtures, not final copy. Locale realization must not determine state.

## Localization / accessibility checks
- Do not encode direction only as English `up/down` when order semantics are earlier/later.
- Keep semantic ID separate from localized label and compact ledger header.
- Status payload and visible concise copy may differ while preserving the same transaction truth.
- Test reordered grammar, plural/ordinal behavior, long labels and RTL/layout-direction contexts.

## CRITIQUE
`Undo` alone is familiar but can become ambiguous after several mutations. Over-explaining every transaction can create announcement and visual noise. The correct compression boundary depends on I066 scope plus runtime/human evidence, not English brevity preference.

## OPEN
No multilingual, AT comprehension or human task PASS. Persistence wording remains dormant until implementation exists.

## HANDOFFS TO OTHER SPECIALISTS
Type receives the finalized multilingual/status corpus later; Layout receives worst-case string pressure; Color receives explicit unavailable/failed/superseded distinctions; Web receives semantic payload assertions.
