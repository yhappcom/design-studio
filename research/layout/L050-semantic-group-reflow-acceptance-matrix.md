# L050 — Semantic-group Reflow Acceptance Matrix

Status: STAGE 3 PRACTICE / TRANSFER VALIDATION PREPARATION  
Date: 2026-09-17

## PURPOSE
Make L049 executable across the integrated product workflow by defining a finite reflow matrix and observable spatial failures.

## RELATED DOMAIN CHECK
T028 supplies realistic string pressure; C059 separates semantic axes; I046 owns temporal/focus/recovery continuity; W059/W058 package runtime evidence; CD065/CD064 preserve meaning through localization and surfaces.

## SOURCE
WCAG 2.x Reflow requires information/functionality to remain available without avoidable two-dimensional scrolling at the specified narrow presentation, with exceptions for genuinely two-dimensional content. WCAG 2.2 also adds focus-not-obscured requirements. Flutter nonlinear scaling means native composition must be tested rather than extrapolated from a single linear scale.

## PRACTICE MATRIX
Protected groups:
- label → value → qualifier;
- section heading → explanatory state;
- field → helper/error → correction control;
- state → available action → recovery;
- list item identity → primary metric → drill-in affordance.

Stress each group at: compact phone portrait; wider phone/tablet; maximum supported text scaling; long localized content; signed/large financial values; partial/unavailable; empty/error/recovery. Geometry may change from row to stack, but semantic order and ownership must remain legible.

## OBSERVABLE FAILURES
- clipping or inaccessible overflow;
- qualifier detached so it can be read as belonging to another metric;
- action detached from the state/consequence it changes;
- avoidable two-dimensional scrolling for ordinary prose/forms/cards;
- fixed-height container hiding enlarged content;
- promotional/ad content interrupting the first-value group;
- focus target obscured by authored sticky/overlay content;
- visual order contradicting meaningful/interaction order.

## CRITIQUE
A denser one-line composition is not preferred when it requires semantic deletion, tiny targets or ambiguous adjacency. Recomposition is a success when relationships survive, even if the screen becomes taller.

## VALIDATION CONTRACT
Bind screenshots, measured bounds/overflow, semantic order and focus location to the same W058 identity. Mark two-dimensional layouts that are genuinely essential rather than applying the ordinary-card rule mechanically.

## HANDOFFS
Type owns glyph/metric causes; Color owns semantic encoding; Interaction owns focus/action/recovery behavior; Content owns truth-bearing strings; Web owns browser/runtime execution and artifact identity.

## EVIDENCE BOUNDARY
No Stage 3 PASS, physical-device, AT, discoverability or representative-human usability PASS is claimed.