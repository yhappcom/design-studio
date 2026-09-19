# W096 — Served Scroll-Anchor / Focus Transfer

Date: 2026-09-19
Stage: Stage 3 PRACTICE / NOT PASSED
Related: I083/L087/C096/CD102/T065

## Why this is a closure problem
CSS Scroll Anchoring can adjust viewport position after layout changes. A July 2026 CSSWG issue reports that suppression-window behavior does not match the current draft in tested browsers, so isolated spec reading or one Chromium micro-test cannot establish parity.

Sources:
- https://drafts.csswg.org/css-scroll-anchoring/
- https://lists.w3.org/Archives/Public/public-css-archive/2026Jul/0346.html
- https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum

## Promotion ladder
Actual LogMate implementation → production Web build → served primary engine → independent engine → 200% → forced-colors. Replicate each scenario family twice.

## Manifest
Record build/route/browser/version, scenario ID, semantic source/focus IDs, active focus identity where observable, scrollOffset before/after and time series when relevant, focus/source/sticky rectangles, anchor-related CSS/configuration, transaction/branch/inverse, projection hash, visible/a11y status and whether movement came from app logic, browser anchoring or unresolved interaction.

## Scenario bundle
Reorder commit/cancel, status insertion/removal above focus, source-offscreen rebuild, Undo/Reset, 200% reflow and sticky/overlay interaction. Compare primary and independent engines before any parity claim.

## Performance evidence boundary
Lighthouse/DevTools/CI remain LAB. Scroll-anchor/focus correctness is not Core Web Vitals evidence. Only provenance-bearing RUM/aggregate may support FIELD LCP/INP/CLS claims.

## RELATED DOMAIN CHECK
I083 owns semantic authority; L087 geometry; C096 visual state; CD102 language truth; T065 rendering transfer. W096 returns any browser divergence to those owners.

## Evidence boundary
No served runtime, independent-engine, field CWV, screen-reader, physical-device, full WCAG or human UX PASS is claimed.