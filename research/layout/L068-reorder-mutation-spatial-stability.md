# L068 — Reorder Mutation Spatial Stability

Date: 2026-09-18
State: PRACTICE / TRANSFER VALIDATION

## Question
L067 compares control architectures. I064 exposes the next spatial risk: after each reorder mutation, can the moved item, its controls and focus remain visible and spatially intelligible under dense 35-field lists, scrolling and 200% text?

## SOURCE
WCAG 2.2 SC 2.4.11 requires a keyboard-focused component not be entirely hidden by author-created content. SC 2.5.8 establishes a 24×24 CSS px minimum pointer-target rule with defined exceptions. W3C supplemental cognitive guidance recommends avoiding unexpected movement unless initiated by the user.

Sources:
- https://www.w3.org/TR/WCAG22/
- https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/
- https://www.w3.org/WAI/WCAG2/supplemental/patterns/o4p01-unexpected-movement/

## PRACTICE — mutation geometry ledger
For each I064 vector capture before/after:
- viewport and text scale/zoom;
- row semantic ID and bounding box;
- active reorder target bounding box;
- visible viewport intersection;
- sticky header/footer overlap;
- scroll offset;
- nearest preceding/following semantic IDs;
- target-to-target spacing;
- row height and wrapped-line count.

Three architecture candidates from L067 remain live: persistent inline controls, selected-row action rail, dedicated reorder mode. L068 adds a new criterion: mutation stability. A compact architecture that passes static density but causes repeated viewport jumps after every move is not preferred merely because it fits.

## CRITIQUE
Index-based visual anchoring is dangerous. When the moved row changes index, keeping the same pixel slot while focus semantically moves elsewhere can create an apparent no-op or wrong-object action. The spatial system should follow semantic identity, not stale list index. Auto-scroll is acceptable when needed to keep the user-initiated moved item/control visible, but the cause and magnitude should be bounded and reproducible.

## REPRODUCIBLE VALIDATION
Run Standard, long-label, 200% text, top-boundary, bottom-boundary, hidden-neighbor and group-boundary scenarios. Compare architectures by:
- zero unintended focus loss;
- focused target remains at least partially visible;
- no overlap by author-created sticky surfaces;
- target-size/spacing evidence retained after wrap;
- no unrelated list jump;
- semantic neighbor relationship matches the new order.

This is non-human geometry/runtime evidence. Perceived stability and workload remain OPEN.

## RELATED DOMAIN CHECK
Type T045: action/status strings may wrap and cannot be shrunk to preserve row height. Color C076: focus/boundary state must survive recomposition. Interaction I064 supplies the temporal oracle. Web W076 supplies browser evidence provenance. Content CD082 supplies stable semantic IDs and input-neutral action language.

## HANDOFFS TO OTHER SPECIALISTS
Interaction should treat semantic identity as the post-mutation focus anchor. Web should log before/after scroll offsets and target rectangles. Content should not encode positional truth only as visual “up/down”. Type should test wrapped action/status strings after the spatial architecture is selected.

## OPEN
No architecture winner is declared before actual runtime measurements. No human stability/workload claim.