# W039 — Bounded correction-chain runtime contract

Date: 2026-09-16
Evidence class: **TRANSFER VALIDATION specification / browser execution OPEN**

## RELATED DOMAIN CHECK
I026 supplies chain termination truth; L030 supplies responsive/focus geometry; C039 supplies terminal visual precedence; CD045 supplies semantic resources; Type remains on mature fallback until T021 closes.

## Product-like runtime sequence
Implement and execute:
`op A → optimistic success → authority conflict → compensation B → B response loss → reconcile B not-applied → authority changes → automatic C prohibited → intervention-required → history/deep-link reload`.

The fixture must persist `correctionChainId`, operation IDs, predecessor relation, presented/authoritative revision, transport observation, reconciliation result, terminal/escalation reason and semantic resource ID.

## Shared run evidence
Each capture records commit SHA, engine/version, viewport and zoom mode, route/history state, network ordering, operation/chain IDs, authoritative/presented revisions, enabled/disabled actions, CD045 resource revision/locale, C039 computed styles/forced-colors state, L030 rectangles/focus/overlay geometry.

Run baseline and 320px reflow. Actual 200% zoom and forced-colors are separately labeled only when actually executed. Chromium plus an independent engine is required before cross-browser claims. WebKit is not Safari evidence; Safari claims require Safari execution.

## Stage-3 relevance
This closes a product-transfer gap that static state contracts cannot: bounded recovery must survive asynchronous ordering, reload/history and responsive/accessibility modes without silently launching unsafe follow-up mutations.

## Performance boundary
Functional timings are lab diagnostics. LCP/INP/CLS are field evidence only when collected from an actual field/RUM population with context; this fixture does not manufacture field Core Web Vitals.

## HANDOFFS TO OTHER SPECIALISTS
Return actual run IDs to C039, I026/L030 and CD045. Type later receives real browser rendering stress only after its drawing/general-spacing gates close.

## Evidence boundary
No browser-runtime PASS, cross-browser, Safari, AT, physical-device, field performance or human UX PASS is claimed until executed artifacts exist.
