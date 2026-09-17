# L063 — Runtime Failure Localization & Width-Claimant Instrumentation

## PURPOSE
**TRANSFER VALIDATION / CRITIQUE.** Convert the MintTap 9.3 px baseline and 47 px enlarged-text RenderFlex failures from anonymous exception totals into evidence that identifies the exact spatial owner before repair.

## RELATED DOMAIN CHECK
- **Type:** T040 forbids Type intervention until a Type-owned cause is reproduced; instrumentation must therefore record text scale/font context without changing metrics.
- **Color:** C071 requires rendered state visibility after Material repair; geometry instrumentation must not remove paint/state behavior.
- **Interaction:** I058 requires feedback/recovery continuity; exact Material ownership is behavioral as well as spatial.
- **Web:** W071 requires same-build evidence identity before browser promotion.
- **Content:** CD077 protects semantic strings from shortening merely to gain width.

## CURRENT EXECUTED EVIDENCE
GitHub Actions run `35255971379`, commit `27b8f3938350ed83e1380511bc357d0929b7f171`, Flutter 3.47.4 / Dart 3.13.3:
- 390×844 baseline: `RenderFlex overflowed by 9.3 pixels on the right`.
- 390×844 enlarged-text contradiction: `RenderFlex overflowed by 47 pixels on the right`.
- The current test catches the exception through `tester.takeException()` at the common `pumpLab` boundary. The log therefore records the amount but not the RenderFlex creator chain or claimant widths.
- Source inspection shows the AppBar title contains `AppBrandWordmark(fontSize: 23)`, a fixed 10 px gap and `_LabBadge`, while the AppBar also reserves a stress-scenario IconButton and trailing 8 px. This is a credible claimant set, but **not yet a proven failure owner**.

## PRACTICE — NEXT EXECUTABLE INSTRUMENTATION
Before spatial repair, capture for each failing scenario:
1. viewport, safe-area insets, text scaler and journey;
2. exact overflowing RenderFlex creator chain / diagnostics;
3. RenderFlex max constraint and actual size;
4. each direct child's size and flex behavior;
5. fixed gaps/padding and reserved AppBar action width where applicable;
6. scenario/build/run identity.

The test harness should preserve the first FlutterError diagnostic before `takeException()` collapses it to a summary. Instrumentation is diagnostic only: it must not alter widget geometry, strings, fonts or interaction feedback.

## CRITIQUE / DECISION RULE
- If the AppBar claimant set is confirmed, repair structurally: flexible allocation or secondary-metadata recomposition before breakpoint/vertical recomposition.
- If another RenderFlex owns the failure, abandon the AppBar hypothesis and repair that owner instead.
- Reject pixel shaving that only clears 9.3 px, Type compression, semantic deletion, or test suppression.
- Re-run baseline + enlarged text + value/locale stress after repair; zero overflow in one fixture alone is insufficient.

## REPRODUCIBLE VALIDATION
`LOCALIZED` requires exact creator chain + constraints + claimant sizes under the failing build. `REPAIRED` requires the same scenario identity to execute without overflow and without semantic/Type/interaction regression.

## OPEN
Exact RenderFlex owner and claimant widths remain OPEN until instrumented execution. Human usability, AT, physical-device and browser evidence remain OPEN.

## HANDOFFS TO OTHER SPECIALISTS
Type receives text-scaler/font context for causal exclusion; Content receives any string pressure without deletion; Interaction/Color receive Material-layer findings; Web receives the localized/repaired scenario manifest for browser promotion.