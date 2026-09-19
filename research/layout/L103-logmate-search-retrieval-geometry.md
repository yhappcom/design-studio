# L103 — LogMate Search/Retrieval Geometry

Date: 2026-09-20

## RELATED DOMAIN CHECK
I099 defines search authority; T081/C112/W112/CD118 supply rendering, salience, runtime and language constraints. L103 does not choose product IA or a visual style.

## SOURCE → PRACTICE
WCAG 2.2 SC 2.4.3 requires focus order that preserves meaning/operation; SC 2.4.11 prevents author-created content from entirely obscuring focused components. APG combobox/listbox patterns inform geometry only if those semantics are actually implemented.

Sources:
- https://www.w3.org/WAI/WCAG22/Understanding/focus-order
- https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum
- https://www.w3.org/WAI/ARIA/apg/patterns/combobox/
- https://www.w3.org/WAI/ARIA/apg/patterns/listbox/

## Protected relationships
Protect `query → status → result identity → result metadata → available action → selected/opened record → return context`, not a fixed search-bar/result-card rectangle.

Measure at baseline, narrow/reflow, enlarged text and WCAG text-spacing:
- query control, clear/filter actions and focus rectangles;
- status/result-count ownership and separation from results;
- result row/card bounds, operational identifiers and target bounds;
- popup/list geometry if autocomplete exists;
- sticky header/footer occlusion and scroll restoration;
- selected/active result versus page-local focus;
- return position after record detail/edit.

## Adaptation order
Allow intrinsic growth → local redistribution → row/card growth → metadata disclosure/detail → local scroll only when professional comparison requires it. Do not shrink semantic labels, hide error/recovery, or detach actions from their result merely to preserve density.

## Failure conditions
Status overlay obscures query/result focus; popup clips active option; responsive reordering separates record identity from its action; stale result geometry remains interactive; return loses task context; target density forces ambiguous icon-only actions; visual order contradicts meaningful focus order.

## EVIDENCE BOUNDARY
This is a geometry contract, not rendered closure. Physical mobile/iPad safe-area, browser chrome, AT, and representative-human search workload remain OPEN.