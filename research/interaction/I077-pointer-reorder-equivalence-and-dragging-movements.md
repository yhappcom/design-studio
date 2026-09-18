# I077 — Pointer reorder equivalence and Dragging Movements closure

Status: PRACTICE / TRANSFER VALIDATION OPEN

## Problem
The Customize workflow cannot treat drag as the only pointer path for reordering. WCAG 2.2 SC 2.5.7 requires functionality that uses a dragging movement to be achievable by a single pointer without dragging unless dragging is essential or determined by the user agent. This is an accessibility floor, not proof that the alternative is equally efficient or understandable.

## Contract
For one semantic object and one destination, drag and non-drag pointer paths must resolve through the same mutation contract:

`semantic_object_id + source_position + destination_position + scope_id -> transaction_id -> resulting projection -> recovery eligibility -> status payload`

Input mechanics may differ; transaction meaning may not.

## Practice bundle
Run these families against the same 35-item Customize model: adjacent move, multi-position move, first↔middle, middle↔last, system-group projection, hidden-item boundary, no-op destination, repeated move, move→Undo, move→Reset. Compare drag with an explicit single-pointer alternative such as Move Up/Down or a destination picker; do not prescribe the product control until implementation evidence exists.

## Critique / fail conditions
FAIL when drag can reach a state the alternative cannot; the alternative mutates a different semantic object; ordinal labels are used as identity; recovery differs without product rationale; a no-op is reported as success; focus follows stale row index; or the alternative is technically present but hidden behind an undiscoverable state that has no product rationale.

## Evidence ladder
SOURCE → model practice → deterministic mutation tests → actual Flutter product → production Web build → served primary engine → independent engine → 200% → forced-colors → physical-device/human evidence.

Two identical repetitions are required before replication claims. Human discoverability, efficiency and workload remain OPEN until observed.

## Related-domain handoff
Layout owns target geometry/reflow; Color owns action/disabled/focus semantics; Content owns action/destination/status wording; Type protects label rendering without compensating for immature drawing; Web owns served-runtime pointer/browser evidence.

## Sources
- W3C WCAG 2.2 SC 2.5.7 Dragging Movements and Understanding 2.5.7 (current WCAG 2.2 baseline).
