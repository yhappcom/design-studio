# T021 — Batch-System No-Scope-Creep Review

Evidence purpose: **CONTRADICTION REVIEW / GATE PROTECTION**. Reviews whether W051/CD057 batch terminology creates a valid reason to expand the currently frozen T021 R1 drawing repair.

## RELATED DOMAIN CHECK
- C051, I038/L042, W051 and CD057 introduce batch/member/outcome/retry strings and numeric counts.
- None provides repaired-raster evidence for T021 or a new glyph defect proven to precede the existing `I/l/1` and candidate-B `0` repair.

## Finding
It does **not** justify R1 scope expansion. Batch labels, counts, operation IDs and localized messages must use mature fallback while R1 is unresolved. Adding new glyphs, spacing exceptions or kerning to satisfy systems-study strings would violate the current drawing→general-spacing→kerning gate order and confound the existing repair experiment.

## Frozen R1 remains
- mutable: `I`, `l`, `1`, candidate-B `0` slash geometry only;
- kerning: OFF;
- widths/sidebearings: frozen;
- unrelated glyphs: frozen;
- acceptance evidence: inspectable source diff + build/font/raster hashes + 14/17/24px before/after critique against the already accepted corpus.

## OPEN
Actual mutation/raster execution remains the next valid evidence. This review is not drawing evidence and does not advance the gate.

## HANDOFFS TO OTHER SPECIALISTS
C051/L042/W051/CD057 must not constrain layout or wording around provisional custom metrics; use mature fallback until T021 drawing and spacing gates pass.