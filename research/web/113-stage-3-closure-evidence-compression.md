# W113 — Web Stage 3 closure evidence compression

Date: 2026-09-20
Purpose: closure planning; replace isolated micro-test accumulation with product/runtime evidence.

## Finding
W108–W112 already define manifests for cross-surface transfer, runtime persistence, reorder, navigation/history and search. The next Web gain is to execute a small representative scenario matrix in the production LogMate PWA, not add another isolated Chromium fixture.

## Minimum executable matrix
A. navigation/history: direct entry, push/replace/traverse, reload, current-page semantics, dirty-state return.
B. search: A→B request supersession, zero/error/offline, result→record→Back restoration.
C. persistence: Add Flight or edit commit → failure → Retry; offline → reconnect → authoritative projection.
D. Customize: non-drag reorder → persistence failure/retry → Undo → reload.
E. responsive/typographic transfer: one dense ledger/search surface under enlarged text, text-spacing and actual font fallback.

## Provenance packet
For every run capture production build/service-worker/data version, served route, browser engine/version and display mode, network state/transition, requested/resolved font, semantic IDs and visible+a11y payload, focus/selection/current state, geometry/scroll/sticky regions, transaction/inverse/projection and persistence/sync evidence.

## Replication ladder
Primary served engine: two reproducible runs per closure scenario. Then independent engine transfer. Add physical mobile/iPad/PWA standalone where platform behavior is material. AT evidence remains separate.

## Performance evidence boundary
Lighthouse, DevTools, CI and synthetic traces are LAB evidence. LCP/INP/CLS become FIELD evidence only when provenance-bearing representative RUM/aggregate field data exists. Do not relabel lab surrogates.

## Cross-domain handoff
Use Type/Color/Layout/Interaction/Content closure fixtures as one shared runtime packet rather than independent screenshots.

## Evidence boundary
No Stage 3 PASS, production runtime closure, independent-engine transfer, physical-device, AT, RUM or human evidence is claimed.
