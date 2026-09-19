# L091 — Review, Confirmation, and Recovery Geometry

Date: 2026-09-19
Stage: Stage 3 PRACTICE
Evidence purpose: TRANSFER VALIDATION from I087

## RELATED DOMAIN CHECK
I087 owns mutation/reversal truth; CD106 owns consequence language; C100 owns semantic visual state; T069 owns rendering stress; W100 owns served runtime provenance. Layout owns placement, reading order, target/focus geometry, reflow and obscuration.

## SOURCE / SYNTHESIS
WCAG 2.2 SC 3.3.4 permits reversible, checked, or confirmed approaches for covered data-changing submissions; geometry must therefore support the chosen interaction contract rather than forcing every action into a modal confirmation. Existing Studio WCAG 2.2 focus-obscuration, target-size and 200% reflow constraints remain independent acceptance axes.

## PRACTICE
Measure baseline and 200% for: inline review-before-commit; destructive confirmation; cancel; validation error; post-commit Undo; failed recovery; long EN/KO object names; sticky header/footer; software keyboard-safe viewport where executable. Capture trigger, heading/object, consequence, primary/secondary action, error/recovery, focus and sticky rectangles plus scroll displacement.

## CRITIQUE / FAILURE CONDITIONS
FAIL if material consequence is below the action or outside the visible review region; 200% separates object from consequence/action ambiguously; sticky surfaces fully obscure focused recovery controls; destructive and cancel targets become spatially confusable; focus returns to a recycled/removed object; or a transient Undo surface overlaps essential task controls.

## REPRODUCIBLE VALIDATION
Run each executable family twice with identical semantic IDs. Geometry is evidence of spatial integrity, not human comprehension or error prevention. Forced-colors, independent engine, physical-device keyboard, AT and representative-human evidence remain OPEN.

## HANDOFFS TO OTHER SPECIALISTS
C100 receives state adjacency/overlap risks; CD106 receives available text width/order constraints; T069 receives actual string boxes only after T021 permits; W100 records rectangles in the served scenario manifest.