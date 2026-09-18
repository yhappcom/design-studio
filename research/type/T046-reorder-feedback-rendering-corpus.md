# T046 — Reorder Feedback Rendering Corpus

Date: 2026-09-18
State: STAGE 2 PRACTICE / TRANSFER SPECIFICATION

## Purpose
CD083 introduces post-move object/position feedback. This creates new text pressure but does not change the T021 gate order. T046 defines the later rendering corpus without using unfinished Type work to solve Layout density.

## Protected gate
T021 remains authoritative: drawing → general spacing → residual pair-specific kerning. R1 drawing loci remain bounded; widths/sidebearings and unrelated glyphs stay frozen during drawing repair. No reorder-control fit problem authorizes font-size, tracking, width or kerning compression.

## Corpus
Pair full professional labels and compact headers with move feedback variables:
- DEP / Departure; ARR / Arrival;
- Aircraft Type; Registration;
- Block; Actual;
- PIC; SIC/FO; PICUS; SPIC;
- Instrument Flight Time; Actual Instrument; Simulated Instrument;
- T/O; L/D;
- positions 1, 9, 10, 19, 20, 34, 35 of 35;
- boundary/no-change and before/after-neighbor feedback.

Critical glyph classes: I/l/1/0, slash, hyphen, parentheses if localized realization uses them, colon, digits, uppercase abbreviations and mixed-case long labels.

## PRACTICE protocol
Once T021 drawing/spacing gates permit transfer, render mature fallback and repaired candidate at realistic control sizes and 200% text. Capture resolved family/fallback, line breaks, clipping, vertical metrics, numeral/punctuation ambiguity and raster evidence. Attribute failures as drawing, metrics/fallback, general spacing, pair residual, or composition pressure.

## CRITIQUE
Position feedback increases repeated digits and short operational abbreviations. That makes numeral differentiation and slash/punctuation clarity more important, not a reason to open kerning early. A candidate that appears compact because of unfinished narrow drawing is not a valid layout advantage.

## RELATED DOMAIN CHECK
Color C076 supplies focus/boundary states but does not change glyph geometry. Layout L068 owns available width and wrapping architecture. Interaction I064 owns move/focus truth. Web W076 owns browser transfer. Content CD083 owns semantic wording and variables.

## HANDOFFS TO OTHER SPECIALISTS
Layout should use mature fallback metrics until T021 closes. Content should preserve full semantic wording and typed variables. Web should capture actual resolved font/fallback in browser evidence. Interaction/Color should not infer focus or move state from typographic styling alone.

## OPEN
T021 R1 mutation/raster remains the upstream blocker. No custom-font product, browser/native, AT or human recognition PASS.