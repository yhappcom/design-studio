# T037 — Repair Regression Attribution Gate

Status: PRACTICE / TRANSFER VALIDATION
Date: 2026-09-18

## Purpose
After compact-layout repair, determine whether remaining failures are truly typographic before any spacing or kerning intervention.

## Gate order
1. Drawing integrity: glyph construction and raster defects first.
2. General spacing: advance widths and repeated rhythm only after drawing is stable.
3. Residual kerning: pair-specific residuals only after drawing and general spacing pass.

Layout overflow, wrapping, truncation, fallback, or container pressure MUST NOT be repaired with tracking/kerning.

## Repair regression matrix
Re-run baseline compact, 200% text-scale stress, long localized strings, signed/zero/large currency values, estimated/final, partial/unavailable, and gross/net qualifiers. For each failure classify: GLYPH, METRICS, GENERAL_SPACING, PAIR_RESIDUAL, FALLBACK, LINE_BREAK, COMPOSITION_PRESSURE, SEMANTIC_TRUNCATION, or RASTER.

## Acceptance
A layout repair passes Type transfer only when meaning-bearing strings remain legible without clipping or semantic truncation and no new fallback/metrics defect appears. Pair tuning is permitted only for reproducible pair-local residuals after the preceding gates pass.

## Related-domain check
- Content owns semantic invariants and protected terminology.
- Layout owns container/reflow pressure.
- Web/runtime evidence establishes whether the failure actually executed.
- Human reading quality remains OPEN until observed; automated fit is not usability evidence.
