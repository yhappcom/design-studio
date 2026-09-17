# W070 — Runtime evidence promotion and field-performance boundary

## Purpose
Keep Web work focused on Stage closure: repaired product runtime, route/network behavior and independent-engine transfer, while preventing lab evidence from being mislabeled as field evidence.

## Stage
Stage 3 PRACTICE / NOT PASSED.

## Promotion ladder
Evidence may move upward only in this order for the same build/scenario identity:

1. static/source inspection;
2. Flutter widget/runtime regression;
3. production-mode Flutter Web build;
4. served browser runtime with route, console and network evidence;
5. independent browser-engine replication;
6. realistic network/state transfer;
7. field evidence where provenance exists.

A successful build is not a browser PASS. A Chromium-only run is not cross-browser evidence.

## Served-runtime bundle
For each key workflow collect:
- build SHA and deployment/runtime identity;
- route/deep-link result;
- viewport/text scale/locale;
- screenshot and focus order evidence;
- console errors/warnings;
- failed/cancelled network requests;
- loading, offline, timeout and recovery behavior;
- state persistence/reload result.

## Accessibility baseline
Use WCAG 2.2 as the current W3C baseline. Include reflow, focus visibility/not-obscured, target geometry, semantics/name-role-value and keyboard continuity where applicable. Automated evidence is not equivalent to AT-user or representative-human evidence.

## Performance provenance rule
Keep three classes explicit:
- LAB: Lighthouse, DevTools traces, synthetic local/CI measurements;
- FIELD-AGGREGATE: provenance-bearing CrUX-like real-user aggregate data;
- FIELD-PRODUCT: product-owned RUM with documented sampling, route/device/network context.

LCP/INP/CLS from LAB must never be presented as field performance. If field evidence does not exist, record FIELD = OPEN rather than substituting a surrogate.

## CRITIQUE / failure classes
- BUILD_ONLY_OVERCLAIM
- SINGLE_ENGINE_OVERCLAIM
- ROUTE_TRANSFER_FAIL
- NETWORK_RECOVERY_FAIL
- FOCUS/SEMANTICS_DRIFT
- LAB_AS_FIELD
- PROVENANCE_MISSING

## RELATED DOMAIN CHECK
Consume Content semantic fixtures, Type rendering constraints, Color rendered-state evidence, Layout geometry/reflow and Interaction recovery states under one scenario manifest.

## Next evidence
After the compact and Material repairs pass the widget matrix, immediately build and serve the same SHA, capture the browser bundle, then replicate on an independent engine. Do not accumulate another isolated Chromium micro-test.