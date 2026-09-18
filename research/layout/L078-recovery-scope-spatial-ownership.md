# L078 — Recovery-scope spatial ownership

## PURPOSE
TRANSFER VALIDATION from I074: test whether spatial placement communicates which subsystem an Undo/recovery control owns without making geometry the source of behavioral truth.

## RELATED DOMAIN CHECK
I074 owns scope routing; C086 owns recovery-state color; T055 keeps Type provisional; W086 owns browser evidence; CD092 owns recovery semantics.

## SYNTHESIS
Recovery placement is an ownership cue, not an ownership definition. A control may be local, sticky-local, page-level or transient. Its `scope_id` must come from Interaction; Layout tests whether position preserves association under reflow.

## PRACTICE
Compare four structures for simultaneous text-edit + display-configuration histories:
1. local recovery adjacent to Customize controls;
2. sticky recovery inside Customize region;
3. page-level recovery rail with explicit scope label;
4. transient status action.

Measure baseline and 200% text/zoom: recovery/control bounding boxes, owning-region bounds, nearest competing editable region, scroll offset, focus rectangle, sticky overlap, safe-area/keyboard collision and wrapping.

## CRITIQUE / FAILURE
FAIL if a configuration Undo visually migrates into another editor's region, if 200% reflow destroys ownership grouping, if removing stale recovery causes destructive locus jump, or if a correct focus target becomes fully obscured. WCAG 2.2 Focus Not Obscured remains the accessibility floor; spatial scope clarity and displacement are stronger Studio criteria.

## REPRODUCIBLE VALIDATION
Run each structure twice at baseline and 200%. Record semantic `scope_id` first, then geometry. Geometry may reject a structure but cannot redefine the scope.

## UX BOUNDARY
Whether users correctly infer recovery ownership from these structures requires human observation and remains OPEN.

## HANDOFFS TO OTHER SPECIALISTS
Web should reproduce the winning/losing geometry in served runtime; Content should qualify scope only when needed; Color must not substitute hue for region ownership; Type must not shorten truthful labels solely to rescue a weak layout.
