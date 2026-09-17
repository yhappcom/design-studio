# T033 — Second CI non-execution classification

Date: 2026-09-18
Purpose: TRANSFER VALIDATION

## RELATED DOMAIN CHECK
Consumes W064 run `35243795007`; Layout/Content own composition and semantic fit, not Type.

## Finding
The repaired MintTap run again stopped in analysis, this time on undefined `debugDumpSemanticsTreeInTraversalOrder()`. Therefore T031 typography fixtures did not execute. No glyph, numeral/punctuation, spacing, kerning, fallback, wrap, clipping or raster conclusion can be drawn.

## Gate discipline
T021 remains drawing-first. Neither CI helper drift nor later composition pressure may be compensated by kerning before drawing/spacing gates close.

## Repair dependency
Product commit `27ad199db553b75b7067852a902c7d39c7784587` removes the unstable debug helper while preserving behavioral assertions.

## Next
Consume the first executed matrix. Classify genuine font/metric defects separately from layout reflow and semantic truncation. Keep browser/native breadth, AT and human evidence OPEN.
