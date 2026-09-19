# L101 — Non-drag reorder geometry

## PURPOSE
Transfer I097 into spatial rules that survive dense Customize lists, reflow, enlarged text and pointer-target constraints.

## RELATED DOMAIN CHECK
T078, C109, I097/I096, W109 and CD115 checked. This is TRANSFER VALIDATION of I097, not a second interaction-state model.

## SYNTHESIS
Protected relationship: `item identity → current position → available move action → resulting position → recovery`.

Stable geometry means this relationship remains legible; it does not require fixed coordinates.

### Stepwise candidate
- Keep move controls in the item's owned action region.
- Boundary items expose only applicable actions; do not reserve misleading active-looking targets.
- After movement, keep the item's action region visually and focus-wise attached to the same item ID.
- At narrow widths, actions may stack or enter a disclosed action region, but must not become hover-only.

### Destination candidate
- Destination chooser must identify the moved item and destination independently.
- Overlay/popover placement must not obscure the item context or focused control.
- Long labels and enlarged text may grow the chooser; clipping is not a density strategy.

## WCAG 2.2 GEOMETRY CHECK
Author-created pointer targets should meet SC 2.5.8's 24×24 CSS-px minimum or a valid exception/spacing path. Reorder density is not itself an `essential` justification. Focus must remain visible under sticky regions and overlays.

## PRACTICE FIXTURE
Seven rows: Date, Flight number, Aircraft registration, Departure, Arrival, Block time, Remarks. Test first/middle/last; 320 CSS-px-equivalent width; 200% text; WCAG text spacing; long labels; pointer rectangles and nearest-target spacing.

Capture item/action rectangles before/after each move, focus rectangle, viewport/sticky rectangles, reading/action order and scroll displacement.

## CRITIQUE
Reject geometry that:
- detaches controls from the moved item;
- causes target overlap/ambiguity after text growth;
- uses tiny icon handles as the only non-drag path;
- scroll-jumps so the moved item/recovery disappears without necessity;
- changes visual order without preserving semantic/action order.

## HANDOFFS TO OTHER SPECIALISTS
Web executes rectangles in real engines; Type stresses labels/position numerals; Color preserves state salience; Content protects explicit action/destination semantics.

## OPEN
Rendered production geometry, physical touch evidence, AT/human task evidence.