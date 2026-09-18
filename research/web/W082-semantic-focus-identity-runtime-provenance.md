# W082 — Semantic Focus Identity Runtime Provenance

## Purpose
Advance W081 from post-Reset geometry/status capture to served-runtime proof that focus remains bound to the intended semantic object through Flutter/Web recomposition.

## RELATED DOMAIN CHECK
I069 is behavioral authority; L073 owns locus geometry; C082 owns visual focus-state integrity; T051 protects rendering; CD088 owns object/result language. LogMate `b551ce4` remains the product-transfer target. This is browser TRANSFER VALIDATION, not another isolated Chromium micro-test.

## SOURCE
Flutter's current focus guidance says FocusNode/FocusScopeNode are long-lived state objects and warns against creating a new FocusNode on each build because focus can be lost. Focus requests take effect after the current build phase. Flutter Web translates Semantics roles into corresponding ARIA roles, so browser accessibility inspection is a distinct evidence layer rather than an assumption from widget code.

## Runtime manifest
For each mutation record build/commit, engine/version, viewport/zoom, semantic object/action ID, Flutter FocusNode debug identity where instrumentable, browser active/focus target, accessibility/semantics identity, visual index, semantic order, focus/target rectangles, scroll/obscuration, status payload and runtime exceptions.

Scenario family: reorder across neighbors; repeated move; hide/show; system-group projection change; Reset; Undo; no-op/boundary; navigation-return; 200% recomposition.

## Evidence ladder
Widget/runtime instrumentation → production Web build → served primary engine → independent engine → 200% → forced-colors. Repeat each executable family twice. Classify `IDENTITY-PASS`, `RECOVERY-PASS`, `IDENTITY-FAIL`, `BLOCKED`, `NOT-EXECUTED`.

A visible focus ring or correct final list order alone is insufficient. A browser test that locates a row only by ordinal position is insufficient after mutation.

## Performance boundary
Lighthouse/DevTools/CI synthetic remains LAB. Only provenance-bearing aggregate/RUM can support field LCP/INP/CLS; no field evidence is created by this study.

## OPEN
Non-drag reorder is not yet confirmed in the product target. Independent engine, screen reader, physical device, persistence/offline/Sync and human UX remain OPEN.

## HANDOFFS TO OTHER SPECIALISTS
Return semantic identity failures to Interaction, geometry to Layout, rendered cue mismatch to Color, semantic payload mismatch to Content, and reproduced font/fallback/raster defects to Type.