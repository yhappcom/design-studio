# L067 — Customize control-density recomposition

## Purpose
Extend L066 from projection density into control density created by an accessible non-drag reorder path. This is TRANSFER VALIDATION, not a claim that such controls are already implemented.

## RELATED DOMAIN CHECK
T045 forbids Type compression as a density fix. C076 requires independent visible states. I062 owns reorder equivalence. W075 owns browser closure. CD081 owns full/compact label separation.

## SOURCE
WCAG 2.2 SC 2.5.7 requires a simple single-pointer alternative to dragging when dragging is not essential. SC 2.5.8 adds a 24×24 CSS-pixel target-size/spacing constraint with defined exceptions. Therefore adding tiny adjacent arrows merely to satisfy drag equivalence can create a second accessibility failure.

## PRACTICE — spatial alternatives
Compare three architectures under the same 35-field catalog:
A. persistent inline earlier/later controls per row;
B. selected-row action rail revealed after a single pointer selection;
C. item selection followed by a dedicated reorder mode with large previous/next controls.

Measure row height, target geometry/spacing, label width, 200% text reflow, scroll distance, group adjacency and action reachability. Preserve semantic order and one-visible minimum in every architecture.

## CRITIQUE
A minimizes steps but increases persistent density. B reduces clutter but creates discoverability/state-signifier dependency. C provides generous targets and clearer mode boundaries but adds mode cost and recovery requirements. No architecture is selected without runtime evidence; human discoverability/workload preference remains OPEN.

## REPRODUCIBLE VALIDATION
Use identical field IDs and Standard/minimum/group-heavy projections. At default and 200% text, record viewport, row/target bounding boxes, overlaps, clipping/overflow, focus order and before/after semantic order. Reject any solution that changes order without an observable state transition or that shrinks text to preserve row height.

## OPEN
No architecture PASS, physical-device, AT or representative-pilot evidence is claimed.

## HANDOFFS TO OTHER SPECIALISTS
Interaction should test mode/reversibility differences among A/B/C. Web should execute the selected candidate in browser. Type/Content should preserve full semantic labels while Layout owns recomposition.