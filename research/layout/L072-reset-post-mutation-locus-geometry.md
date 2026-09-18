# L072 — Reset Post-Mutation Locus Geometry

## Purpose
Spatial transfer of I068: determine whether Reset preserves a visible, operable locus under bulk recomposition rather than merely restoring the correct baseline data.

## RELATED DOMAIN CHECK
Type T021/T049, Color C080, Interaction I067/I068, Web W080, Content CD086 checked. This is TRANSFER VALIDATION, not a new ownership structure.

## PRACTICE
For surviving-focus, hidden-focus, no-op, Reset→Undo and navigation-return scenarios capture: viewport, text scale, focused semantic ID, target/focus bounding boxes, scroll offset, sticky/recovery bounds, wrap count and overlap/obscuration.

Compare L071 architectures (immediate+Undo, consequence preview, confirmation, baseline-summary) using the same mutation vectors. Do not prefer a modal/snackbar from screenshot aesthetics.

## CRITIQUE
A baseline-correct Reset fails spatially when the recovery/focus locus is offscreen, entirely obscured, displaced behind sticky UI, or forces excessive context loss. At 200% text, solve by recomposition/flow before Type compression.

## Validation
Repeat each executable scenario twice at baseline and 200% text. Preserve semantic identity across geometry logs. Hand identical scenario IDs to Web for served-browser/independent-engine transfer.

## OPEN
No rendered L072 evidence yet; no human workload, AT, physical-device or representative-pilot evidence.

## HANDOFFS TO OTHER SPECIALISTS
Interaction owns the focus/recovery rule; Color must keep focus/recovery visible after recomposition; Content must not shorten consequence truth merely to fit; Web must capture actual rectangles/scroll/obscuration.