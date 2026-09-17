# L059 — Compact Repair Acceptance Matrix

Status: PRACTICE / TRANSFER VALIDATION
Date: 2026-09-18

## Purpose
Convert the known compact overflow into a finite post-repair acceptance matrix rather than accepting pixel-specific suppression.

## Scenarios
1. Compact baseline viewport.
2. Same viewport at 200% text scaling.
3. Long portfolio/name and long localized qualifiers.
4. Signed/zero/large KRW and USD values.
5. Partial/unavailable and estimated/final states.
6. Wide/tablet workflow to detect regressions introduced by compact recomposition.

## Spatial invariants
Preserve label→value→qualifier, field→error→correction, and state→action→recovery adjacency. Reflow is allowed; clipping, overlap, semantic detachment, avoidable two-dimensional scrolling, obscured focus, and target loss are failures.

## Repair order
Localize the exact offending group; remove avoidable fixed-width competition; prefer Flex/Wrap/vertical recomposition where semantics permit; then re-run all scenarios. Do not solve baseline overflow by shrinking meaning-bearing text or deleting qualifiers.

## WCAG 2.2 transfer
Web transfer must separately verify Reflow, Focus Not Obscured, and Target Size (Minimum) where applicable. Flutter/native platform guidance is recorded separately rather than conflated with CSS-pixel criteria.

## Evidence boundary
Automated geometry proves layout behavior only. Discoverability, workload, and professional-workflow usability remain OPEN pending human observation.
