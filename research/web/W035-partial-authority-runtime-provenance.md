# W035 — Partial-Authority Runtime Provenance

Date: 2026-09-16
Evidence class: **TRANSFER VALIDATION PROTOCOL / EXECUTION OPEN**

## RELATED DOMAIN CHECK
T021 keeps mature-font fallback; C035 defines visual degradation; I022 defines authority evidence/action safety; L026 defines spatial association; CD041 owns partial-authority wording.

## Stage-3 purpose
W034 distinguishes restored presentation from authority reconciliation. W035 extends the product-like fixture to authority checks that succeed fully, time out, return partial evidence, conflict, or become unavailable after a previously confirmed revision.

## Runtime scenarios
For stable object/operation IDs execute:
1. restored last-known presentation → full authority confirmation;
2. restored presentation → authority timeout/unavailable;
3. partial authority response with action-critical field unknown;
4. conflicting local/remote revision;
5. later successful reconciliation after prior unavailability;
6. deep link directly into each state;
7. history traversal/reload without falsely upgrading freshness.

## Provenance bundle
Record commit SHA, engine/version/platform, route/lifecycle, request ID, request start/end/timeout observation, object/operation ID, presented revision, authoritative revision where known, known/unknown fields, semantic state/action IDs, locale, viewport/visualViewport, actual zoom method/result where executable, forced-colors state, focus/overlay rectangles and raw network trace.

## Browser breadth
Chromium plus an independent engine is required before cross-browser claims. WebKit execution is not Safari evidence; Safari claims require Safari. Headless execution is not physical-device evidence.

## Accessibility baseline
WCAG 2.2 is the current W3C baseline used by the studio. Focus visibility and focus obscuration remain separate verdicts.

## Performance boundary
Scenario timings are functional/lab diagnostics only. LCP/INP/CLS are labeled field evidence only when derived from an actual field/RUM population with context.

## Current blocker
No browser-capable W035 execution artifact exists in the current connector runtime. This protocol reduces ambiguity in the next executable environment; it does not claim runtime PASS.

## HANDOFFS TO OTHER SPECIALISTS
C035/L026 consume shared run IDs; I022 evaluates action safety; CD041 binds semantic resources; Type remains mature fallback until T021 closes.
