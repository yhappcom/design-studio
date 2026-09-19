# W098 — Served Unsaved-Exit and Lifecycle Transfer

Date: 2026-09-19
Stage: Stage 3 PRACTICE
Evidence purpose: PRODUCT TRANSFER + INDEPENDENT VALIDATION

## RELATED DOMAIN CHECK
I085 defines authority; L089 geometry; C098 state encoding; CD104 content truth; T067 downstream rendering corpus. W098 integrates them in actual served browser behavior.

## SOURCE FINDINGS
Current MDN guidance: `beforeunload` is not reliably fired on mobile, requires prior user activation for confirmation, uses browser-controlled generic wording, and can affect Firefox bfcache eligibility. `visibilitychange` is a more reliable application-state checkpoint signal; `pagehide` is bfcache-compatible but still not guaranteed on mobile. `unload` must not be a correctness boundary.

Sources:
- https://developer.mozilla.org/en-US/docs/Web/API/Window/beforeunload_event
- https://developer.mozilla.org/en-US/docs/Web/API/Window/pagehide_event
- https://developer.mozilla.org/en-US/docs/Web/API/Window/unload_event

## CLOSURE LADDER
Do not add an isolated Chromium micro-test. Execute in this order when LogMate implementation exists:
1. production Web build;
2. served primary engine;
3. served independent engine;
4. baseline and 200%;
5. light/night/forced-colors where applicable;
6. physical mobile lifecycle later for process/background cases that desktop automation cannot establish.

## SCENARIO MANIFEST
For each scenario ID and two replications capture: build/route, browser/version, activation state, history/document identity, visibility/pagehide/pageshow/beforeunload observations where available, bfcache evidence, dirty/checkpoint/validation flags, semantic object/focus ID, branch/projection hash, warning shown/not shown, navigation result, and L089 geometry.

Families: clean leave; dirty in-app leave; dirty Back/Forward; reload/new-document return; background/return; bfcache return; Undo/Reset dirty-to-clean; source unavailable; non-drag reorder once implemented.

## CRITIQUE
Capability is not product PASS. Event absence is not save success. Event presence is not persistence. bfcache return is not freshness validation. Browser warning copy is not product-owned. A permanent beforeunload handler is suspect because warning scope and bfcache/performance costs must follow actual dirty state.

## PERFORMANCE EVIDENCE
Keep Lighthouse/DevTools/CI synthetic as LAB. Lifecycle/bfcache observations may explain navigation behavior but do not become field Core Web Vitals. LCP/INP/CLS require provenance-bearing field/RUM evidence before FIELD claims.

## ACCESSIBILITY
WCAG 2.2 is baseline. Distinguish focus-taking dialogs from non-focus status messages. Preserve keyboard/pointer/non-drag equivalence and focus visibility. Screen-reader and human comprehension evidence remain OPEN.

## EVIDENCE BOUNDARY
No cross-browser, mobile process lifecycle, persisted configuration, screen-reader, physical-device, field CWV, full WCAG or human UX PASS is claimed.