# W116 — LogMate Candidate 03 Flutter Native/Web Promotion Ladder — 2026-09-20

Status: **PRODUCTION-TRANSFER PLAN / STAGE 3 NOT PASSED**

## Purpose
Candidate 03 now has Flutter implementation provenance but no successful runner-based analyze/test/golden or runtime PASS. W116 turns that gap into a promotion ladder that distinguishes Flutter native evidence from Flutter Web/browser evidence.

## SOURCE
Flutter accessibility testing recommends platform scanners/inspectors, Guideline API tests for contrast/target labels/target size, and browser inspection of the Flutter Web semantics host. Flutter Web accessibility is produced by translating the Flutter Semantics tree into accessible HTML; semantics activation/runtime must therefore be recorded rather than inferred from the widget source.

Sources:
- https://docs.flutter.dev/ui/accessibility/accessibility-testing
- https://docs.flutter.dev/ui/accessibility/web-accessibility
- https://docs.flutter.dev/ui/accessibility

## Promotion ladder
1. exact Candidate 03 source + Flutter/Dart/toolchain version;
2. successful analyze + relevant widget/golden/accessibility-guideline tests;
3. native primary runtime baseline with resolved fonts, MediaQuery/TextScaler, SafeArea, semantics/focus/route evidence;
4. same-build REPLICATION;
5. max text scaling + fallback + theme/high-contrast stress;
6. second native platform transfer where product scope requires it;
7. Flutter Web served build: browser/engine, semantics enabled, viewport, DOM accessibility payload, route/history and responsive transfer;
8. independent browser transfer;
9. physical device/PWA standalone where applicable;
10. human/AT validation remains a separate gate.

## Candidate 03 runtime packet
Record build commit, Flutter version, target platform/engine, viewport/window, display/text scale, accessibility settings, resolved fonts, route/history, visible strings, accessibility payload, focus/current/selection state, target/geometry rectangles and implemented transaction authority.

## WCAG 2.2 boundary
WCAG 2.2 remains the studio accessibility baseline. Flutter's 44/48 logical-pixel platform guidance is a stronger design target for many controls than WCAG 2.2 SC 2.5.8's 24 CSS-pixel minimum; do not misstate 44px as the WCAG 2.2 AA minimum. Candidate 03's 44×44 corrections are therefore retained as a product/platform design choice, not mislabeled conformance proof.

## Performance boundary
Analyze/golden/widget tests and DevTools/synthetic measurements are LAB. LCP/INP/CLS become FIELD evidence only with provenance-bearing representative RUM/aggregate. Native Flutter frame metrics are not Core Web Vitals.

## CRITIQUE / failure conditions
FAIL promotion if static SVG/code-mirror evidence is called runtime proof; if native high-contrast is mislabeled CSS forced-colors; if semantics source declarations are called AT proof; if a failed-before-runner CI job is treated as test evidence; or if Flutter Web and native results are merged without platform provenance.

## RELATED DOMAIN CHECK
- Type: T085 supplies scaling/resolved-font requirements.
- Color: C116 supplies semantic-state/high-contrast conditions.
- Interaction/Layout: I103/L107 supply route/focus/geometry invariants.
- Content: CD122 supplies visible/accessibility string parity.

## HANDOFFS TO OTHER SPECIALISTS
All specialists should consume the same W116 runtime packet instead of separate screenshots. Any browser/platform contradiction is handed back to the owning specialist before Stage 3 closure.

## OPEN
Current GitHub Actions failure occurred before runner steps; no analyze/test/golden/runtime/browser/device/AT/human PASS is claimed.