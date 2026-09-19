# L097 — LogMate Large-Text Ledger Adaptation Modes

Status: **STAGE 3 PRACTICE / SYSTEMS PRACTICE — no gate promotion**

## PURPOSE
Resolve the spatial side of H2 without assuming that a professional ledger must either fully stack or remain a fixed desktop table.

## RELATED DOMAIN CHECK
Type T075, Color C106, Interaction I093, Web W105 and Content CD111 checked. Current W3C WCAG 2.2 Reflow guidance explicitly recognizes data tables/grids as potentially requiring two-dimensional layout while keeping the exception scoped.

## THREE ADAPTATION MODES
### A — Preserved comparison plane
Keep the table/grid as a locally scrollable two-dimensional region. Use when simultaneous column comparison is essential. Surrounding page content reflows; cells must not clip protected text.

### B — Priority-preserving hybrid
Keep high-value comparison fields on stable local axes; move secondary descriptive metadata into row expansion/detail. Use when the core comparison task survives with fewer simultaneous fields.

### C — Record-detail transfer
Use a compact index/list for identification and transfer the complete record to a detail representation. Use when enlarged text makes simultaneous comparison less important than complete per-record inspection.

None is globally preferred. Choice depends on task and evidence.

## OPERATIONAL GEOMETRY CONTRACT
Across all modes preserve:
- stable semantic ordering of Date / Flight / Route / duration where present;
- Flight carrier + number/suffix zoning;
- DEP/ARR relationship;
- duration integrity;
- record identity;
- visible relationship between state/action and affected record;
- complete access to secondary/user/source text.

Stable geometry means stable relationships, not identical coordinates or fixed row height.

## REPRODUCIBLE VALIDATION PLAN
For each mode capture baseline and enlarged/text-spacing conditions:
- viewport and local-scroll-region bounds;
- column/field start/end positions;
- row height distribution;
- wrapping/clipping/ellipsis/reveal state;
- focused component rectangle;
- sticky header/column rectangles;
- horizontal and vertical scroll offsets;
- selected/invalid/recovery boundary rectangles;
- target rectangles.

FAIL if protected content disappears, semantic ordering changes without an explicit representation contract, focus is entirely obscured by author content, or target/action ownership becomes ambiguous.

## CRITIQUE
SC-A Calibrated Axis must not force fixed columns beyond their useful range. At enlarged text, a local axis can move from x-coordinate alignment to repeated label/value alignment or a detail grid. That is still calibrated if comparison relationships remain intentional and predictable.

## SYNTHESIS
H2 should not be solved with one responsive breakpoint. It requires an **adaptation mode decision** based on which simultaneous comparisons are essential. This is the bridge between the Signature Code and actual large-text production behavior.

## OPEN
- Which LogMate ledger comparisons are essential under pilot workflows.
- Exact breakpoint/container thresholds.
- Actual production geometry at 200%/400%-equivalent conditions.
- Human orientation/comparison workload.

## HANDOFFS TO OTHER SPECIALISTS
- Web: implement all candidate modes only as needed to falsify/compare them; do not infer PASS from static layouts.
- Type/Content: identify protected strings that cannot be clipped or semantically shortened.
- Interaction: verify semantic/focus/action continuity across mode changes.
