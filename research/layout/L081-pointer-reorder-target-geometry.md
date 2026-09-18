# L081 — Pointer reorder target geometry and adaptive reflow

Status: PRACTICE / TRANSFER VALIDATION OPEN

## Question
Once I077 defines semantic move equivalence, can drag and single-pointer alternatives remain operable at baseline and 200% without target ambiguity, clipping, sticky-surface obstruction or excessive displacement?

## Geometry protocol
Capture viewport, text scale, semantic object/action ID, source/destination rectangles, actionable target rectangles, scroll offset before/after, sticky/safe-area intersections, wrap count, and resulting locus. Test first/middle/last positions, long localized labels, system groups and recovery surfaces.

WCAG 2.2 SC 2.5.8 Target Size (Minimum) is the AA floor: pointer targets are at least 24×24 CSS px or satisfy a listed exception such as spacing/equivalent/inline/user-agent/essential. Do not convert this into a blanket 24×24 visual-control rule; record which clause establishes PASS. Studio critique is stronger: neighboring move controls must remain distinguishable and the destination model must remain spatially comprehensible.

## 200% transfer
Repeat the identical semantic scenario at 200% text. A layout that passes only by horizontal clipping, target overlap, focus obstruction, or unexplained large scroll displacement fails transfer even if the final order is correct.

## Dependency
Semantic correctness is decided by I077 before geometry. L081 must not use a visually clean animation to excuse a wrong object/destination mutation.
