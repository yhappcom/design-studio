# T029 — MintTap Static Product-Transfer Audit

Status: TRANSFER VALIDATION / STATIC EVIDENCE; runtime execution remains OPEN.

## Question
What can be learned from the actual MintTap Flutter source before W059 runtime execution, without violating the T021 drawing → spacing → kerning gate?

## RELATED DOMAIN CHECK
- Color C059: state meaning must not collapse into one hue role.
- Layout L050 / Interaction I046: truth-bearing strings must survive reflow and workflow state changes.
- Web W059: source inspection is not runtime/browser PASS.
- Content CD065: financial qualifiers must not be shortened merely to preserve geometry.

## Product evidence inspected
Repository `yhappcom/yieldmax_tracker`, branch `design-lab/minttap-1.0.29`.

1. Production `lib/main.dart` wraps compact native iOS in `MediaQuery.withClampedTextScaling`.
2. `lib/widgets/ios_compact_adapt.dart` defines `kIosCompactWidthMax = 375.0` and `kIosCompactTextScaleCap = 1.10`.
3. The isolated product lab defines explicit financial strings including signed KRW/USD, long portfolio names, gross/net and partial-data stress.

## SOURCE
Flutter's current accessibility guidance requires UI to remain usable at very large text/display scale factors. Flutter's Android 14 migration material documents nonlinear font scaling up to 200%. WCAG 2.2 remains the studio web accessibility baseline.

## PRACTICE / CRITIQUE
The production 1.10 compact-iOS clamp is a concrete product-transfer risk: it reduces the chance of observing wrapping and composition failures precisely where T028/T027 need them exposed. This is not classified as a Type defect by itself; it is a product composition policy that can mask Type/Layout/Content failures.

The product lab is directionally stronger because it contains finite stress strings rather than compensating through kerning or custom-font metrics. While T021 R1 drawing remains open, mature fallback remains the only defensible font for MintTap transfer evidence.

## Failure routing
- glyph ambiguity or malformed shape → T021 drawing;
- broad spacing defect after drawing closure → general spacing;
- residual pair-specific defect after spacing closure → kerning;
- wrap/overflow under necessary wording → Layout/Web;
- semantic shortening/truncation → Content;
- source-level text-scale suppression → Layout/Interaction/Web accessibility policy.

## Reproducible next validation
Use exact W059 identity and compare at minimum: unclamped platform scaling versus current compact-iOS policy, narrow/wide viewports, KRW/USD signed large values, long portfolio label, estimated/final and partial/unavailable qualifiers. Capture actual fallback font, line breaks, clipping/overflow and semantic text.

## Evidence boundary
STATIC SOURCE TRANSFER evidence only. No raster, native, browser, AT, human-recognition, T021 closure, spacing closure or kerning-entry PASS.

## HANDOFFS TO OTHER SPECIALISTS
Layout/Web should treat the 1.10 clamp as an explicit audit item rather than a neutral implementation detail. Content must keep truth-bearing qualifiers intact. Color must not use visual state as a substitute for text removed by fit pressure.