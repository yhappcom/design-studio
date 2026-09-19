# W115 — LogMate Home first production-transfer plan

Date: 2026-09-20
Purpose: **TRANSFER VALIDATION / STAGE-CLOSURE EXECUTION PLAN**

## RELATED DOMAIN CHECK
T084, C115, I102, L106, CD121 and W114 reviewed. This extends W114 with the first concrete white-canvas Home fixture rather than adding another isolated browser micro-test.

## Why this is the next Web step
The latest Home review is explicitly static evidence only. W115 defines the minimum promotion packet required before any browser/PWA/runtime claim can be made.

## Production packet
For the coded Home capture together:
- commit/build identifier;
- service-worker/data version where applicable;
- served route and history entry mode;
- engine/version and browser/PWA display mode;
- viewport, DPR and input modality;
- network state/transition;
- requested and actual resolved font/fallback;
- visible text plus accessibility payload;
- focus/current/selection/status semantic IDs;
- L106 protected geometry rectangles and scroll/sticky regions;
- I102 action/query/projection authority;
- persistence/sync evidence only when those states actually exist.

## Execution matrix
A. served primary engine, baseline Home fixture;
B. same build REPLICATION;
C. narrow + enlarged text + WCAG text-spacing;
D. forced fallback font;
E. light/night/forced-colors/reduced-motion where implemented/material;
F. route-out → Back/Forward → Home restoration;
G. independent engine TRANSFER VALIDATION;
H. physical mobile/iPad/PWA standalone when environment is available.

Inject consequence-bearing states only when the implementation has real state authority; otherwise use clearly labelled test fixtures and do not claim runtime semantics.

## Acceptance boundary
Static screenshot approval does not establish responsive, browser, accessibility, offline, history, performance or human usability PASS. Lighthouse/DevTools/CI/synthetic measurements remain LAB. LCP/INP/CLS become FIELD evidence only with provenance-bearing representative RUM/aggregate.

## Falsifiers
Reject promotion if actual font differs without being recorded, reflow breaks protected relationships, visible/a11y semantics diverge, route restoration loses context, forced-colors removes necessary state identity, or a synthetic metric is labelled field evidence.

## HANDOFFS
All peers consume one shared packet rather than independent screenshots: Type gets resolved-font/wrap evidence; Color gets semantic-state/non-color evidence; Layout/Interaction gets geometry/focus/history evidence; Content gets visible+a11y semantic evidence.

## OPEN
Coded Home runtime, independent engine, physical device/PWA, screen reader, representative RUM and human usability evidence.