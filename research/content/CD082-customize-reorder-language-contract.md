# CD082 — Customize reorder language contract

## Purpose
Extend CD081's semantic governance into the non-drag reorder alternative required by the current accessibility gap. The objective is a complete content/state contract, not isolated arrow microcopy.

## RELATED DOMAIN CHECK
T045 protects rendering and rejects type compression. C076 separates visual states. L067 compares control-density architectures. I063 defines the actual reorder transition. W076 defines browser evidence. CD081 remains canonical for semantic IDs/full labels/compact headers.

## SOURCE
WCAG 2.2 SC 2.5.7 requires a non-drag single-pointer alternative to dragging where dragging is not essential. Content therefore must name an equivalent action without assuming drag, mouse, touch, color or spatial perception.

## SEMANTIC CONTRACT
For each field use stable `semantic_id` and keep separate:
- full field name;
- compact ledger header;
- action intent: move earlier / move later (or domain-appropriate equivalent);
- current/boundary availability;
- completion/status message when needed;
- Reset consequence.

Protected meanings: Hide ≠ delete; Reset ≠ erase; moving a display column ≠ changing flight data; display order ≠ entry-field order; group label ≠ stored field value.

## PRACTICE
Stress corpus includes long field names, aviation abbreviations, first/last boundary states, hidden fields, one-visible floor, repeated moves and group-heavy projections. Localization QA keys on semantic IDs, never English strings. A compact icon may supplement but not silently replace required accessible naming.

## CRITIQUE
`Up/Down` is spatially concise but can become ambiguous when layout direction, responsive composition or nonvisual access changes. `Move earlier/later` expresses order semantics more directly but is longer. Final wording remains architecture- and localization-dependent; no human comprehension preference is claimed.

## REPRODUCIBLE VALIDATION
For every I063 transition, compare source semantic ID/state → localized action/accessibility name → visible realization → resulting order/status. Flag terminology substitution, semantic deletion, input-specific wording and state collapse. Run multilingual production strings before Content Stage 3 closure.

## OPEN
No multilingual production, linguistic review, AT comprehension or representative-pilot task PASS is claimed.

## HANDOFFS TO OTHER SPECIALISTS
Interaction supplies true availability and transition outcome; Layout must fit meaning without deleting it; Web verifies accessible names/runtime localization; Type validates rendering; Color cannot substitute for verbal state.