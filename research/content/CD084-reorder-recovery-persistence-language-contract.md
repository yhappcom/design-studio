# CD084 — Reorder Recovery & Persistence Language Contract

Status: **STAGE 3 PRACTICE / OPEN LOCALIZATION + HUMAN EVIDENCE**  
Purpose: **EXTENSION + CONTRADICTION REVIEW** of CD082/CD083.

## RELATED DOMAIN CHECK
I065 owns the actual move/undo/reset/commit contract. L069 owns recovery placement/reflow. C077 owns visual state separation. T046 owns rendering constraints. W077/W078 own browser/runtime realization. Content must not invent persistence or recovery truth.

## SOURCE
WCAG 4.1.3 requires status messages to be programmatically determinable so assistive technologies can present them without receiving focus. WAI APG rearrangeable-list examples include a distinct last-change status, but example patterns are not production proof and require AT/browser testing.

## Semantic source model
`field_semantic_id + mutation_result + old_position + new_position + total + reversibility + persistence_state + optional neighbor/group context`

The rendered sentence never selects these states.

## Protected distinctions
- `Moved` ≠ `Saved`.
- `Undo move` ≠ `Reset layout`.
- `Reset layout` ≠ `Delete flight data`.
- `Hidden` ≠ `Deleted`.
- `Applied locally` ≠ `Persisted across restart`.
- `Persistence failed` ≠ `Move failed`.
- `Persistence ambiguous` ≠ `Persistence failed`.

## Message families
### Move consequence
Must identify enough object/result context to make the mutation attributable. Absolute (`7 of 35`), relational (`after ARR`) and hybrid forms remain alternatives.

### Undo action
The action label should name the consequence being reversed when ambiguity is possible. A generic `Undo` may be acceptable only when the immediately preceding reversible transaction is unambiguous in context; this remains a product/human validation question.

### Undo result
Do not announce a second success merely because a transient surface disappeared. Source truth is `UNDO_APPLIED` plus resulting position/order.

### Reset
State the configuration scope. Never imply flight records are erased when only display configuration returns to defaults.

### Persistence
Do not use `Saved` until the product has a persistence contract and confirmation evidence. Temporary-session behavior should not borrow persistence language.

## Localization architecture
Variables remain typed and reorder semantics remain logical rather than English-word-order dependent. Avoid deriving state from words such as `up`, `down`, `before`, `after`; locale realization chooses grammatical order and directional expression. Professional field IDs remain stable across locale.

## Critique matrix
Reject copy that is shorter but collapses state, including:
- `Done` — object/consequence absent.
- `Saved` after local reorder — unsupported persistence claim.
- `Reset` used as immediate Undo — wrong scope.
- color-referential instructions — not resilient to forced colors/nonvisual access.

## Reproducible evidence
For each I065 scenario store source payload, locale, visible string, accessibility status string, action label, resulting semantic order and persistence truth. Geometry/string-fit checks are not human comprehension evidence.

## OPEN
Actual multilingual runtime, linguistic review, screen-reader announcement quality, representative-pilot comprehension/workload, persistence/sync product truth.

## HANDOFFS TO OTHER SPECIALISTS
Interaction receives wording dependencies that require state truth. Layout receives non-deletable semantic payload. Type receives recovery numeral/punctuation corpus. Color receives non-color meaning requirements. Web receives visible/accessibility message parity checks.