# I063 — Customize reorder equivalence contract

## Purpose
Advance I062 from identifying the WCAG 2.2 dragging gap to a testable equivalence contract for direct manipulation, non-drag pointer and keyboard paths.

## RELATED DOMAIN CHECK
T045 protects labels/rendering. C076 separates visibility/focus/reorder states. L067 compares spatial architectures. W075 owns browser execution. CD081 owns semantic IDs and full action meaning.

## SOURCE
WCAG 2.2 SC 2.5.7 (AA) requires functionality using dragging to be achievable by a single pointer without dragging unless dragging is essential. W3C's explanatory example explicitly describes selecting a list item and using up/down arrows. SC 2.5.8 separately constrains target size/spacing.

## STUDIO JUDGMENT — equivalence means state equivalence, not visual sameness
For a starting semantic order S and requested move M, drag, non-drag pointer and keyboard paths must converge on the same resulting semantic order S'. They may differ in gestures and presentation, but must preserve:
- the moved field identity;
- relative order of unaffected fields;
- hidden-item stability contract;
- group adjacency rules;
- one-visible floor;
- immediate-session commit semantics;
- Reset semantics.

## PRACTICE — transition ledger
For each path capture `scenario_id`, `input_path`, `before_order`, `selected_id`, `requested_move`, `after_order`, `focus_after`, `announcement/status`, `undo/reset availability`, and failure reason. Boundary attempts (first item earlier, last item later) must not silently mutate order.

## CRITIQUE
Adding arrows is insufficient if the user cannot identify which item will move, focus is lost after movement, repeated moves are expensive/unobservable, or the alternative manipulates a different order model from drag. Keyboard support also does not substitute for SC 2.5.7's single-pointer non-drag requirement.

## VALIDATION
REPLICATION: run the same reorder vector through all implemented input paths twice. PASS requires identical semantic order and preserved invariants, with no runtime exception. Accessibility-name/focus/status evidence is required for browser promotion. Human discoverability and workload remain OPEN.

## HANDOFFS TO OTHER SPECIALISTS
Web receives the transition-ledger schema. Layout receives target/row recomposition requirements. Content receives status/action semantics. Color receives focus/disabled/insertion state distinctions.