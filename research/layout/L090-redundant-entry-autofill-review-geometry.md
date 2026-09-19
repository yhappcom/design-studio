# L090 — Redundant Entry, Autofill, and Review Geometry

Date: 2026-09-19
Stage: Stage 3 PRACTICE
Evidence purpose: TRANSFER VALIDATION

## RELATED DOMAIN CHECK
I086 owns provenance/validation authority; CD105 owns semantics; C099 owns visual-state separation; W099 owns served browser evidence; Type owns text rendering.

## SPATIAL CONTRACT
Autofill or app restoration must not change the semantic field identity, hide the opportunity to inspect/change a value, or cause validation/recovery controls to become obscured. At 200%, value provenance must not be conveyed by spatial position alone. Repeated information that can be selected must remain reachable without forcing a drag gesture.

## PRACTICE MATRIX
Measure baseline and 200% for: empty→browser fill; empty→app restored; repeated value available as selection; overwritten restored value; invalidated prior value; inline validation; Reset; Back/Forward return; review-before-commit. Record field/control/focus/error/recovery/sticky rectangles, scroll displacement, wrapping, target size and whether focus is fully obscured by author-created content.

WCAG 2.2 reference points: SC 3.3.7 Redundant Entry, SC 2.4.11 Focus Not Obscured (Minimum), SC 2.5.8 Target Size (Minimum), and SC 1.4.10 Reflow where applicable.

Sources: https://www.w3.org/TR/WCAG22/ ; https://www.w3.org/WAI/WCAG22/Understanding/redundant-entry.html

## FAILURE CONDITIONS
FAIL if an autofilled/restored value pushes its label or recovery off-screen without a reachable path; validation inserts content that fully obscures keyboard focus; 200% creates horizontal two-dimensional reading for ordinary form content; repeated selection becomes pointer-drag-only; or layout makes restored and committed values indistinguishable by removing necessary semantic text.

## REPRODUCIBLE VALIDATION
Replicate each executable scenario twice at baseline and 200%; then forced colors and independent engine. Geometry is non-human evidence. Discoverability, confidence in restored values, cognitive load and representative-pilot performance remain OPEN.

## HANDOFF
C099 tests state visibility; CD105 supplies actual payloads; T068 tests wrapping after drawing gate; W099 returns served geometry/provenance.