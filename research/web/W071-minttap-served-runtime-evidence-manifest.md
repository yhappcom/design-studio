# W071 — MintTap Served-Runtime Evidence Manifest

Date: 2026-09-18
Purpose: **TRANSFER VALIDATION / STAGE-CLOSURE INFRASTRUCTURE**
Stage: Stage 3 PRACTICE.

## QUESTION
What evidence must exist before MintTap can promote a repaired Flutter widget result to an actual Web/browser claim?

## SOURCE
WCAG 2.2 is the current studio accessibility baseline. W3C identifies WCAG 2.2 as a published Recommendation and documents Reflow, Focus Not Obscured and Target Size requirements.

- https://www.w3.org/WAI/standards-guidelines/wcag/
- https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/
- https://www.w3.org/WAI/standards-guidelines/wcag/new-in-21/#1410-reflow-aa

Flutter documents web semantics visualization in profile/release mode via `FLUTTER_WEB_DEBUG_SHOW_SEMANTICS=true`; this is diagnostic evidence, not screen-reader or human evidence.

- https://docs.flutter.dev/ui/accessibility/accessibility-testing

## PROMOTION LADDER
No step inherits a PASS from the prior step.

1. **Widget runtime** — exact repaired scenarios execute with no unexpected framework/layout assertions.
2. **Production Web build** — build completes; artifact identity recorded.
3. **Served runtime** — actual built files served over HTTP; startup/route/deep-link/reload tested.
4. **Primary browser** — reflow/zoom, keyboard/focus, pointer, semantics overlay where useful, console/network and state feedback captured.
5. **Independent engine** — repeat critical scenarios in a genuinely independent engine before cross-browser claims.
6. **Network/state transfer** — delayed, failed and ambiguous requests; reload/back/forward/reconciliation where product behavior requires them.
7. **Field evidence** — only provenance-bearing aggregate/RUM product data may be labeled field LCP/INP/CLS.

## REPRODUCIBLE MANIFEST
Every run must record:
- product commit/build SHA;
- Flutter/Dart versions;
- build mode;
- browser name/version/engine;
- OS/runner;
- viewport/DPR/zoom/text scaling;
- locale/currency/scenario fixture;
- route/deep-link;
- network condition;
- console errors/warnings;
- screenshot/semantics/focus artifacts;
- widget/build/browser result separately;
- performance evidence class: `LAB`, `FIELD-AGGREGATE`, `FIELD-PRODUCT`.

## CRITIQUE
`flutter build web` proves compilation, not runtime UX. A Chromium-only pass does not prove Safari/Firefox behavior. Lighthouse or local traces are lab surrogates even when they report LCP/INP/CLS-like metrics; they are not field Core Web Vitals without field provenance.

## ACCESSIBILITY ACCEPTANCE
At minimum, the served-runtime matrix must include 200% text/zoom behavior, constrained-width reflow, visible/non-obscured focus, keyboard reachability and applicable target-size/non-text contrast checks. Automated checks are necessary but not sufficient for AT or human claims.

## RELATED DOMAIN CHECK
- Type: T040 supplies font/fallback causal evidence.
- Color: C071 supplies rendered-state/contrast/non-color matrix.
- Layout/Interaction: L062/I058 supply reflow, focus, target and recovery scenarios.
- Web: extends W070 into a concrete manifest and promotion ledger.
- Content: actual locale strings/message states must be present; synthetic English is not localization closure.
- UX: browser evidence supports end-to-end analysis but not representative-human usability.

## HANDOFFS TO OTHER SPECIALISTS
All specialists should reference the same manifest identity instead of producing incompatible fixture claims. Browser findings that expose font, color, spatial or semantic defects return to the canonical owner.

## EVIDENCE BOUNDARY
No repaired widget PASS, served-browser PASS, independent-engine PASS, field Core Web Vitals, screen-reader or human UX PASS is claimed.
