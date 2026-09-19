# W108 — Cross-surface production transfer manifest

Date: 2026-09-20
Status: Stage 3 PRACTICE / PRODUCT-TRANSFER DESIGN

## Goal
Close the gap between a signature that works in one concept and a signature demonstrated across real LogMate routes/runtime states.

## Promotion ladder
explicit invariant → implemented Home + at least two materially different surfaces → production build → served primary engine → independent engine → enlarged text/text-spacing → applicable light/night/forced-colors/reduced-motion → real route/history/network/font fallback → physical mobile/iPad when platform behavior matters.

Static renders can falsify obvious failures but cannot prove runtime transfer.

## Shared provenance manifest
For each scenario capture:
- build/commit and browser/engine;
- route/history/document identity;
- viewport/DPR and accessibility mode;
- actual loaded font/fallback and relevant font features;
- semantic object/state/action IDs;
- visible and accessibility payload;
- focus/selection/validation/recovery state;
- L099 protected geometry and scroll/sticky regions;
- transaction/inverse/projection hashes when mutation occurs;
- network/offline/service-worker state where relevant.

Run Home→ledger edit/return, Add Flight validation/commit, import mapping/preview/Undo, and Customize reorder/save as TRANSFER VALIDATION; repeat deterministic scenarios twice per primary and independent engine when implementation exists.

## Accessibility/runtime boundary
WCAG 2.2 is the current W3C baseline for this work. Focus visibility/obscuration, reflow, text spacing, target/input alternatives, programmatic state, and status communication are tested as separate axes; visual similarity does not satisfy them.

## Performance evidence boundary
Lighthouse, DevTools, CI and synthetic traces are LAB evidence. LCP/INP/CLS become FIELD evidence only when provenance-bearing representative RUM/aggregate data exists; no current signature-transfer test changes that rule.

## Blockers
Implemented multi-route production surfaces, independent-engine runs, real route/network/font fallback, physical iPad/mobile where applicable, non-drag reorder, NAV-001 and SEARCH-001 remain open.