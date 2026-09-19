# L092 — Import preview and resolution geometry

Date: 2026-09-19
State: STAGE 3 PRACTICE — TRANSFER VALIDATION SPEC; rendered/human evidence OPEN

## RELATED DOMAIN CHECK
Reuses I088 authority, C100 state separation, W100 provenance, CD106 consequence/recovery semantics and T021/T069 constraints. This is TRANSFER VALIDATION from single-mutation review to dense batch review, not a new ownership model.

## SYNTHESIS
Import review has three simultaneous spatial scales: batch summary, row/object identity and local correction/recovery. Spatial compression must not erase the relationship among `row → classification → consequence → available action`.

## PRACTICE
Deterministic fixture: 28 rows with valid, exact-duplicate, possible-duplicate and invalid classes. Test baseline and 200% at phone/tablet/desktop widths. Measure batch-summary box, row identity, classification text, correction/action target, focused control, sticky header/footer, error summary and recovery/status region.

Required scenarios: initial preview; jump from error summary to row; resolve possible duplicate; expand row detail; bulk exclude exact duplicates; cancel; commit; Undo batch; long filename; long flight identifier; EN/KO stress; 200% reflow; keyboard traversal; non-drag/single-pointer controls.

## ACCEPTANCE / FAILURE
- Focused target must not be fully obscured by author-created sticky content under WCAG 2.2 SC 2.4.11.
- At 200%, row identity, classification and action must remain associated without requiring two-dimensional scrolling for ordinary text content where WCAG reflow applies.
- Batch totals must remain discoverable but must not displace row-level recovery.
- A sticky commit bar must not hide the last unresolved row or its focus indicator.
- Color alone must not encode duplicate/error classes.
- Geometry evidence does not prove human comprehension or efficient scanning.

## OPEN
Actual LogMate component implementation, real iPad viewport/safe areas, AT reading order, pilot scanning/workload and production localization remain OPEN.

## HANDOFFS TO OTHER SPECIALISTS
Web should record rectangles and scroll offsets under the same I088 scenario IDs. Content should keep row/batch messages semantically aligned. Color should verify forced-colors. Type should not shorten required strings to preserve geometry before T021 closes.
