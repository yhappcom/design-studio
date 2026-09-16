# W032 — Portable Stage-3 Execution Package

Date: 2026-09-16
Evidence: **IMPLEMENTATION / TRANSFER VALIDATION PLAN / EXECUTION BLOCKED LOCALLY**

## RELATED DOMAIN CHECK
- **Type:** T021 is not production-ready; use mature system/product font and record exact font identity.
- **Color:** C031/C032 require shared semantic IDs plus forced-color/cue-independence captures.
- **Layout/Interaction:** L022/L023 and I018/I019 define geometry, recovery and resumption invariants.
- **Content:** CD037/CD038 provides semantic IDs, localized variants and certainty-preserving strings.
- **UX:** end-to-end evidence must preserve object/task continuity; browser automation is not human usability evidence.

## Purpose
W030 established that the current runtime path cannot produce browser captures. W032 converts W031 closure requirements into a portable package that can be handed to any browser-capable CI or local machine without changing the evidence semantics.

## Required execution lanes
### Lane A — authoritative workflow
Run confirm, known rejection, drop-before-commit and drop-after-commit. Record immediate state, reconciliation result, operation ID and later retrieval/history state.

### Lane B — route/resumption
For an outcome-unknown operation exercise back/forward, reload and later return. Verify I019 correlation/object identity and no certainty inflation.

### Lane C — responsive/accessibility
For the same semantic IDs capture baseline, 320 CSS px reflow, actual 200% zoom, keyboard focus through authored sticky layers, and forced-colors/high-contrast where the engine/platform supports it. Record unsupported conditions explicitly.

### Lane D — localization/content
Execute source locale plus pseudo-expanded/long-content condition with the same semantic IDs. Record wrap, action reachability, association and any string/resource fallback.

### Lane E — engine breadth
At minimum execute Chromium plus one independent engine before any cross-browser claim. Firefox and WebKit are preferred portable lanes; Safari-specific claims require Safari execution rather than assuming WebKit equivalence.

## Result schema minimum
`runId, commitSha, engine, engineVersion, OS, route, objectId, operationId, semanticStateId, contentRevision, locale, viewport, visualViewport, zoomCondition, forcedColorsCondition, focusedElement, focusedRect, overlayRects, horizontalOverflow, immediateState, reconciledState, historyState, fontIdentity, screenshots/artifactRefs, unsupportedConditions`.

## Accessibility baseline
WCAG 2.2 remains the W3C baseline. Focus Not Obscured (Minimum) is tested independently from contrast or focus appearance. Automated checks may establish deterministic geometry/state facts but do not establish complete WCAG conformance or AT usability.

## Performance boundary
Functional Stage-3 captures may record lab diagnostics, but field LCP/INP/CLS labels require actual field/RUM population evidence. No lab surrogate is renamed as field Core Web Vitals.

## Portable handoff
The existing W029 runner is the starting executable. A browser-capable environment should install pinned Playwright/runtime dependencies, execute the controlled backend locally, preserve raw JSON plus screenshots/logs, and commit or attach immutable artifacts with commit SHA. If a lane cannot execute, record `BLOCKED/UNSUPPORTED` rather than synthesizing PASS.

## Stage-3 closure impact
W032 reduces environment coupling but does not close Web Stage 3. Closure still requires actual artifacts for workflow/network, route/resumption, responsive/zoom, accessibility, localization and independent-engine transfer.

## HANDOFFS TO OTHER SPECIALISTS
All peers consume the same run IDs rather than creating independent unverifiable screenshots. C032, L023/I019 and CD038 should attach their verdicts to this provenance envelope.
