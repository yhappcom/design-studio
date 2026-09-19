# CD101 — Reorder Focus / Result Content Contract

Date: 2026-09-19
Stage: Stage 3 PRACTICE / NOT PASSED
Related: I082/L086/C095

## Protected distinctions
`focused object ≠ moved object`
`drag proxy ≠ focused control`
`drag ended ≠ move committed`
`row rebuilt ≠ object changed`
`ordinal/index ≠ stable object identity`
`cancelled/no-op ≠ failed`
`local commit ≠ Saved/Synced`

## Content source payload
User-visible and accessibility feedback should resolve from: semantic object ID/name, action, committed destination/result, transaction result, focus-restoration result, recovery eligibility/scope and persistence truth. Framework callback names, proxy lifecycle and widget indices are diagnostic data, not user-facing source truth.

## Practice
For drag and non-drag paths, generate visible and accessibility payload candidates for commit, cancel, boundary no-op, unavailable move and Undo/Reset. Exercise EN/KO length at baseline and 200% without freezing literal production wording before runtime fit and linguistic review.

If focus restoration fails or moves to a different semantic object, do not hide that discrepancy with success copy. Accessibility payload may need richer object/result context than visible feedback, but must not claim focus moved when only the reordered object moved.

## Evidence boundary
No multilingual production, linguistic-review, screen-reader comprehension or representative-pilot task PASS is claimed.