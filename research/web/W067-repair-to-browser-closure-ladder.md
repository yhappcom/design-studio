# W067 — Repair-to-Browser Closure Ladder

Evidence class: **SYSTEMS PRACTICE / REPRODUCIBLE VALIDATION PLAN**

## PURPOSE
Prevent another cycle of isolated micro-tests by defining the shortest evidence path from W066's executed widget failures to actual browser/product transfer.

## CLOSURE LADDER
### Gate A — widget repair regression
Run the exact three existing scenarios after L058/I054 implementation. Required: analyzer warning/error gate passes; 390×844 baseline has no unintended overflow; 390×844 2.0-scale stress has no unintended overflow/semantic loss; 1024×768 workflow has no Material feedback-layer assertion and retains correct navigation/state.

### Gate B — Flutter Web build
Only after Gate A passes, execute the existing Web build. Preserve build SHA, Flutter/Dart version, logs and output identity. Build success is not browser PASS.

### Gate C — browser runtime
Serve the exact built artifact and execute route/navigation, responsive compact/wide, enlarged text/zoom, keyboard/focus, state feedback and locale stress. Capture screenshot + DOM/semantics/accessibility evidence + console/network logs + task result under one scenario manifest.

### Gate D — independent engine
A Chromium result cannot establish cross-browser closure. Repeat the high-risk matrix in an independent engine before any cross-browser claim.

### Gate E — network/state expansion
After minimum smoke, add pending, known failure, ambiguous outcome, verify/reconcile and retry. Preserve distinction between transport failure, unknown commit/outcome and confirmed product failure.

## ACCESSIBILITY BASELINE
WCAG 2.2 remains the current W3C baseline. Reflow/resize and Focus Not Obscured are explicit runtime checks. Human usability and AT comprehension remain separate evidence classes.

## PERFORMANCE PROVENANCE
Local Lighthouse/DevTools traces are LAB evidence. LCP/INP/CLS are called FIELD only when provenance-bearing field telemetry such as CrUX/RUM/equivalent is actually available. No field Core Web Vitals claim is currently permitted.

## CRITIQUE
The current bottleneck is not another Chromium micro-test. W066 already supplies a real product-transfer failure. The next valuable Web evidence is repaired whole-workflow execution, followed by actual built-browser runtime and independent-engine transfer.

## RELATED DOMAIN CHECK
T036 classifies post-repair rendering; C067 checks visible semantic states; L058 repairs compact geometry; I054 repairs feedback ownership; CD073 preserves semantics and opens the real locale pipeline.

## HANDOFFS TO OTHER SPECIALISTS
Every browser discrepancy is returned to its canonical owner with build/scenario identity. Browser wrapping/fallback → Type; visible state/contrast → Color; reflow/geometry → Layout; focus/action/recovery → Interaction; string/locale semantic drift → Content.

## OPEN
No repaired widget run, Web build PASS, browser runtime, independent-engine, screen-reader, physical-device, field performance or human evidence exists yet.