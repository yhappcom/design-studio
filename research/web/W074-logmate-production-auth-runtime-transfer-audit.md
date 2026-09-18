# W074 — LogMate Production Auth Runtime Transfer Audit

Date: 2026-09-18  
Purpose: `TRANSFER VALIDATION` + stage-closure evidence audit

## PRODUCT EVIDENCE
LogMate run `35293644138` at commit `11cbe36f…` used Flutter 3.47.4 / Dart 3.13.3. Production-auth browser tests executed in Chrome and passed wide-PWA flow, phone-landscape composition, 200% recovery reachability, keyboard-height reflow, compact 24px target floor, Night textual error identity, restored-unverified gating and short-height action reachability. Functional and production golden suites also passed broad auth state coverage.

The overall render workflow nevertheless failed: its command accidentally concatenated `onboarding_auth_journey_v4_golden_test.dart` with a literal `\n flutter ...`, producing nonexistent `dartn`/`flutter` paths; `widget_test.dart` also referenced a removed `debugInitialHiddenColumns` parameter; and an older auth journey still has three 200% RenderFlex overflows. The newer V4 large-text scenarios pass.

## CRITIQUE
This run demonstrates why workflow conclusion and design conclusion must be separated. Browser/product evidence exists despite a red workflow. Failures belong to three classes: harness command defect, stale unrelated test/API drift, and genuine legacy-layout transfer defect. None may be silently collapsed into `WEB FAIL`.

## STAGE-CLOSURE PRACTICE
Adopt per-scenario evidence promotion:
`SOURCE/BUILD ID → test loaded? → runtime executed? → design assertion result → browser engine → network condition → artifact provenance`.

A red job can contain valid executed PASS evidence. A skipped/unloaded test is NOT EXECUTED. A compile/harness failure is BLOCKED. A RenderFlex assertion after execution is EXECUTED-FAIL.

Chrome evidence is primary-engine only. Cross-browser requires an independent engine. Current performance evidence contains no provenance-bearing field LCP/INP/CLS; FIELD remains OPEN. Lab surrogates must remain LAB.

## WCAG 2.2 APPLICATION
The 200% and keyboard/short-height evidence supports reflow/reachability analysis, while the compact 24px target-floor test aligns with WCAG 2.2 Target Size (Minimum) geometry. These automated checks do not establish full WCAG conformance or AT usability.

## RELATED DOMAIN CHECK
- Type: T043 uses V4 as non-Type causal control.
- Color: C074 uses rendered focus/error/night evidence.
- Layout/Interaction: L065/I061 own recomposition and state/recovery semantics.
- Content: CD080 preserves auth state and enumeration-resistant semantics.

## HANDOFFS TO OTHER SPECIALISTS
Return the three-class failure taxonomy to all peers. Next Web block should repair/partition the harness, rerun the targeted suites, then add independent-engine and delayed/failed/ambiguous network-state transfer rather than more isolated Chromium micro-tests.

## EVIDENCE BOUNDARY
No cross-browser/Safari/Firefox, screen-reader, physical-device, field Core Web Vitals, full WCAG conformance or human UX PASS is claimed.