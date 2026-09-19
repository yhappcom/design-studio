# T080 — LogMate Navigation Label Rendering Transfer

Date: 2026-09-20  
Purpose: downstream Type transfer for I098/L102 while T021 drawing remains upstream.

## RELATED DOMAIN CHECK
C110, I098/L102, W110 direction, CD116 and cross-surface studies checked. Mature fallback is mandatory; no provisional custom metric becomes a navigation constraint.

## PRACTICE corpus
Render the actual implemented primary-destination labels when available, plus bounded stress strings: `Home`, `Logbook`, `Add Flight`, `Activity`, `Settings`, `Customize`, `Back to Logbook`, record identifiers, current-page/accessibility status text. Include fallback substitution, enlarged text and WCAG text-spacing.

Capture actual family, font feature settings, label width, wrap/truncation, line box, target geometry and current/focus state coexistence.

## CRITIQUE
Navigation fit must not be achieved through negative tracking, glyph narrowing, semantic abbreviation, changing professional terminology, or kerning before the drawing/general-spacing gates. If a mature fallback label does not fit, hand the failure to Layout/Content before changing Type semantics.

## Gate discipline
T021 remains frozen-width/sidebearing, kerning-OFF bounded drawing repair. Sequence remains **drawing → general spacing → residual kerning**. T080 cannot close T021 and cannot authorize a custom production font.

## Reproducible validation
Run the I098 route fixture at baseline/narrow/enlarged/text-spacing with shipped/fallback Type. Compare current/focus labels and route-return states. Repeat after any eventual T021 drawing+spacing closure before custom-font transfer.

## HANDOFFS TO OTHER SPECIALISTS
L102 receives measured label geometry; C111 should not rely on type weight alone for current state; Web captures actual loaded family; Content retains semantic labels unless evidence supports a terminology change.

## OPEN
Exact production navigation labels, exact production mono/fallback, repaired T021 raster, general spacing, browser/native rendering matrix, human recognition.