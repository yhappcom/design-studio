# W073 — Widget Diagnostic to Served-Browser Closure

Date: 2026-09-18
Stage: 3 PRACTICE
Purpose: product-transfer closure protocol

## New evidence basis
Flutter's official error model routes framework build/layout/paint failures through `FlutterError.onError`; forced verbose diagnostic presentation is available. L064 therefore supplies a concrete way to preserve the exact failing-widget/creator-chain provenance missing from the current MintTap widget run.

Official sources:
- https://docs.flutter.dev/testing/errors
- https://api.flutter.dev/flutter/foundation/FlutterError/onError.html
- https://api.flutter.dev/flutter/foundation/FlutterError/dumpErrorToConsole.html
- https://www.w3.org/WAI/standards-guidelines/wcag/

## Closure ladder
1. `WIDGET_DIAGNOSTIC_REPLICATION`: baseline + 200% text reproduce and localize the same owner without repair.
2. `WIDGET_REPAIR_REGRESSION`: baseline, 200%, long/locale/value contradiction and wide traversal pass under one repaired commit.
3. `WEB_BUILD`: production Flutter Web build completes. This is not browser PASS.
4. `SERVED_PRIMARY`: serve the build over HTTP and capture route/deep-link/reload, viewport/reflow/zoom, keyboard/focus, interaction feedback, console and network evidence.
5. `SERVED_INDEPENDENT_ENGINE`: repeat critical flows in a genuinely independent browser engine before cross-browser claims.
6. `NETWORK_STATE_TRANSFER`: delayed/failed/ambiguous outcomes, verify/reconcile and safe retry.
7. `FIELD`: only provenance-bearing aggregate/RUM evidence may support field LCP/INP/CLS claims.

Each promotion records repository, commit, build/run identity, browser/engine/version, scenario ID and artifact locations. A later stage cannot retroactively convert an earlier NOT EXECUTED stage into PASS.

## WCAG 2.2 transfer
WCAG 2.2 remains the current W3C baseline. Served-runtime checks must include Resize Text/Reflow, keyboard/focus visibility and Focus Not Obscured where applicable, plus target geometry. Automated browser evidence does not equal screen-reader or representative-human evidence.

## Performance evidence
Keep `LAB` (CI synthetic, Lighthouse, DevTools/local traces) separate from `FIELD-AGGREGATE` and `FIELD-PRODUCT`. Report LCP/INP/CLS as field only when provenance demonstrates real-user field collection for the relevant product/population/window.

## CRITIQUE
The current bottleneck is not another Chromium micro-test. It is failure provenance plus repair regression. Browser work before widget repair would mix known product defects with browser-specific findings and reduce diagnostic value.

## RELATED DOMAIN CHECK
- Type T042 supplies font/fallback context without compensation.
- Color C073 supplies rendered-state contradiction matrix.
- Layout L064 supplies exact RenderFlex localization.
- Interaction I060 supplies Material feedback acceptance.
- Content CD078 supplies stable semantic scenario identity and later real localization corpus.

## HANDOFFS TO OTHER SPECIALISTS
Every served-browser contradiction is returned to the canonical owner with same-build evidence. Browser font/fallback issues return to Type; occlusion/reflow to Layout; feedback/focus to Interaction/Color; semantic/localization failures to Content.

## Evidence boundary
Current Web build/browser/independent-engine/field evidence remains OPEN until widget repair is executed. No screen-reader, physical-device or human UX PASS is claimed.
