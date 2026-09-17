# W064 — Second CI API drift and repair

Date: 2026-09-18
Purpose: TRANSFER VALIDATION / EXECUTION TRIAGE

## RELATED DOMAIN CHECK

This continues W063 and shares one execution identity with T032, C063, L054/I050 and CD069. It does not create a new UX owner.

## Evidence

MintTap Actions run `35243795007` executed on product commit `8f5e7c1285057de505859d60db8b6e2a738d6e22` using Flutter 3.47.4 / Dart 3.13.3 on Ubuntu 24.04. Checkout, Flutter setup, identity capture and dependency resolution passed. `flutter analyze` then failed because `debugDumpSemanticsTreeInTraversalOrder()` is not defined in that SDK. Widget matrix, Web build and manifest generation were skipped. Artifact upload succeeded.

The prior repair therefore changed the unsupported symbol but did not remove the unstable debug-helper dependency. This is a second harness/API-drift failure, not a product-design failure.

## Repair

Product branch `design-lab/minttap-1.0.29` was repaired again at commit `27ad199db553b75b7067852a902c7d39c7784587`: the unsupported semantics debug helper and now-unused rendering import were removed. The behavioral assertions remain intact. A semantics artifact must later be captured with an SDK-supported, deliberately versioned mechanism rather than an analyzer-blocking debug helper.

## Classification

- CI substrate: EXECUTED / PASS through dependency resolution.
- Analyzer: EXECUTED / FAIL — harness API drift.
- Type/Color/Layout/Interaction/Content runtime fixtures: NOT EXECUTED.
- Flutter Web build: NOT EXECUTED.
- Browser/cross-browser/AT/physical-device/human UX: OPEN.
- Field LCP/INP/CLS: OPEN; no field evidence exists.

## Critique

Two consecutive failures at semantics-dump helpers show that evidence collection itself must not be allowed to block the primary behavioral transfer matrix. Evidence capture should be layered: first execute stable behavioral assertions and build; then collect optional diagnostics with explicit version compatibility and `always()` preservation. A diagnostic failure must remain distinguishable from a product assertion failure.

## Next executable block

1. Observe the run for `27ad199...` and classify every stage.
2. If analyzer passes, consume the 390×844 baseline, 390×844 / 2.0 contradiction, and 1024×768 workflow results before adding adjacent Web theory.
3. Only after the minimum matrix runs, add stable semantics/focus artifacts and actual MintTap locale execution.
4. Require an independent browser engine before cross-browser claims.

## Evidence boundary

No runtime, browser, accessibility, Core Web Vitals, or human PASS is claimed by this note.
