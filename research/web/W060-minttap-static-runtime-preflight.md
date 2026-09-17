# W060 — MintTap Static Runtime Preflight

Status: PRODUCT TRANSFER PREFLIGHT; W059 execution still BLOCKED in this environment.

## Purpose
Reduce W059 execution uncertainty using actual MintTap source, without pretending source inspection is browser/native runtime evidence.

## RELATED DOMAIN CHECK
T029, C060, L051/I047 and CD065 define the shared acceptance oracles. W059 remains the runtime authority.

## Actual product source inspected
`yhappcom/yieldmax_tracker`, branch `design-lab/minttap-1.0.29`.

Confirmed statically:
- Flutter production entry exists and initializes localization, auth/Firebase and app theme.
- compact native iOS <=375 shortest-side applies a 1.10 text-scale cap.
- localization is implemented through project Dart infrastructure (`app_locale.dart`, large `app_strings.dart`, display-name/date helpers), not a conventional ARB-only structure.
- locale-dependent signed trend color mapping exists.
- isolated Design Lab contains `lab_foundation.dart`, `minttap_home_lab_v2.dart`, and `minttap_whole_app_lab.dart`.
- the lab foundation already separates brand, polarity and availability/certainty and includes KRW/USD, long-name, negative-return and partial-data scenarios.

## Important correction to prior queue
CD059/CD065 should not assume MintTap's current production localization mechanism is ARB. The transfer target is the actual Dart localization pipeline; ARB/TMS may remain a method comparison or future migration path, not a prerequisite falsely attributed to the product.

## W059 executable preflight matrix
Identity must record product commit/branch, entrypoint (`main.dart` vs `main_design_lab.dart`), target platform/browser, viewport/device, locale, currency, actual text scaler, theme, network/data fixture and scenario flags.

Required first run order:
1. Design Lab deterministic scenarios without Firebase/auth/ad dependencies.
2. Production mobile/web smoke with actual localization and route state.
3. Accessibility stress: max text/zoom, semantics, keyboard/focus, target checks, grayscale/high contrast where available.
4. Independent browser engine before cross-browser claim.
5. Production async/network ambiguity and history/deep-link scenarios.

## Evidence artifacts
Screenshot/video as needed; Flutter semantics or browser accessibility tree; focus/history trace; console/runtime logs; automated accessibility result; exact scenario state; failure taxonomy from peer domains. Preserve raw evidence before summary.

## Performance boundary
Local Flutter/profile traces, Lighthouse or DevTools remain LAB. Only provenance-bearing CrUX/RUM/equivalent measurements may support field LCP/INP/CLS claims.

## Blocker
This execution environment exposes GitHub source and write operations but no Flutter/browser binary runner. Therefore W059 runtime PASS remains OPEN. The preflight is nevertheless real product-transfer evidence because it corrects target assumptions and binds the runbook to actual source paths.

## HANDOFFS
Content: validate the real Dart localization pipeline first. Layout/Type: explicitly compare current iOS clamp against unclamped diagnostic behavior. Color: bind locale-dependent trend mapping into the runtime matrix. Interaction: run complete workflow traces, not isolated screenshots.