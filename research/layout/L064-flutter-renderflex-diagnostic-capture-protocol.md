# L064 — Flutter RenderFlex Diagnostic Capture Protocol

Date: 2026-09-18
Stage: 3 PRACTICE
Purpose: TRANSFER VALIDATION / failure localization for MintTap whole-app runtime

## Question
How should the studio preserve enough Flutter layout diagnostics to identify the actual overflow owner and width claimants before attempting responsive repair?

## SOURCE
Flutter's framework routes build/layout/paint errors through `FlutterError.onError`. The default handler presents a detailed diagnostic; `FlutterError.dumpErrorToConsole(details, forceReport: true)` can force verbose output even after earlier errors. Flutter's common-error guidance shows that a RenderFlex diagnostic normally includes the error-causing widget, orientation and overflow context. Therefore the current evidence loss at a shared `tester.takeException()` boundary is a harness-observability problem, not a reason to infer the owner from source proximity.

Official sources:
- https://docs.flutter.dev/testing/errors
- https://docs.flutter.dev/testing/common-errors
- https://api.flutter.dev/flutter/foundation/FlutterError/onError.html
- https://api.flutter.dev/flutter/foundation/FlutterError/dumpErrorToConsole.html

## PRACTICE — capture contract
For each scenario, install a temporary `FlutterError.onError` interceptor before the first pump and restore the previous handler in `finally`. The interceptor must preserve every `FlutterErrorDetails`, call the previous/default presentation path, and emit a stable scenario marker before the full diagnostic. Do not silently consume the error.

Minimum artifact fields:
- repository/commit/run/build identity;
- scenario ID;
- viewport, device-pixel ratio, text scaler, locale/theme;
- `exceptionAsString` and `summary`;
- full diagnostics tree/string and stack where present;
- relevant error-causing widget / creator chain;
- RenderFlex axis, constraints, actual size and overflow amount when reported;
- direct-child claimant measurements from targeted post-localization probes;
- owner-domain classification and confidence.

The first pass captures the framework diagnostic without modifying geometry. Only after the owner is reproduced should a second targeted probe add keys/finders or render-object measurements around that owner. This avoids instrumenting a guessed AppBar and accidentally confirming the hypothesis by construction.

## CRITIQUE
`takeException()` is useful for asserting that an exception occurred but is insufficient as the sole provenance record when it collapses diagnostics needed for causal repair. Conversely, dumping the entire render tree on every pump creates noise and makes comparison brittle. The preferred method is event-triggered full diagnostics plus targeted measurements after owner localization.

## REPRODUCIBLE VALIDATION
Run the same baseline and 200% text scenarios twice without repair. Localization is accepted only when both runs identify the same owner/creator-chain class and materially consistent constraint/overflow signature. Mark this `REPLICATION`, not repair PASS.

After localization, record claimant widths and verify the budget equation against the RenderFlex max constraint. A structural repair may then be evaluated under baseline, 200% text, long strings, signed/large values and wide layout.

## WCAG 2.2 TRANSFER
The diagnostic itself is not accessibility evidence. It enables repair validation for Resize Text/Reflow conditions. Accessibility PASS still requires actual rendered behavior and, where relevant, browser/AT/human evidence.

## RELATED DOMAIN CHECK
- Type: T041 requires no font/spacing/kerning intervention until a Type-owned cause is reproduced.
- Color: C072 depends on post-repair visible state surfaces, not this layout diagnostic.
- Interaction: I059 owns Material paint/feedback repair separately from RenderFlex localization.
- Web: W072 needs exact failing-widget/creator-chain provenance before browser promotion.
- Content: CD078 requires stable semantic strings/state flags across diagnostic and repair runs.

Reusable conclusion: diagnostic preservation must precede geometry repair. The AppBar claimant set remains a hypothesis until the captured framework diagnostic identifies it.

## HANDOFFS TO OTHER SPECIALISTS
Web should carry the scenario/diagnostic identity into its evidence manifest. Type and Content should record context without changing strings or typography during localization. Interaction/Color should remain independent unless the localized owner overlaps their state surface.

## Evidence boundary
No RenderFlex owner has been newly captured in this study. No repair or runtime PASS is claimed. Human/AT evidence remains OPEN.
