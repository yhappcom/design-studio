# W117 — Candidate 05 production promotion packet

Status: **STAGE 3 PRACTICE / PRODUCTION TRANSFER PLAN / RUNTIME OPEN**

## Question
What exact evidence promotes Candidate 05 from visual owner-review eligibility to defensible Flutter native/Web runtime evidence without confusing static renders, CI setup, synthetic checks or platform recommendations with production proof?

## RELATED DOMAIN CHECK
T086, C117, I104, L108 and CD123 checked. Candidate 05 coordinator gate reports final 390×844 light/dark render fit, but its Actions run ended before runner steps (`runner_id=0`, `steps=[]`). Therefore analyze/test/golden/runtime claims remain OPEN.

## SOURCE
Flutter recommends accessibility testing with platform scanners/inspectors and its Accessibility Guideline API; the API can check Android/iOS target recommendations, target labels and text contrast. Flutter Web exposes semantics into an accessibility structure that can be inspected in browser tooling. Android 14 nonlinear font scaling is supported through `TextScaler`, and Flutter recommends testing at the maximum font size. These sources support a test method, not a Candidate 05 PASS.

## Promotion ladder
1. **Exact-source identity** — commit/source hash, Flutter/Dart versions, dependencies, build mode.
2. **Runner evidence** — successful `flutter analyze`, relevant widget tests, golden tests and accessibility-guideline tests. A job that never starts is no evidence.
3. **Primary native runtime REPLICATION ×2** — same build, same fixture; record device/OS, viewport/insets, TextScaler, resolved fonts, semantics IDs, focus, route/state and L108 geometry.
4. **Stress transfer** — max supported platform text scaling, forced mature fallback, narrow/SafeArea, light/dark and supported accessibility modes.
5. **Second native platform** — same semantic fixture, platform-specific evidence kept distinct.
6. **Flutter Web transfer** where product scope applies — served build, semantics enabled/inspectable, browser focus/route behavior, CSS forced-colors kept distinct from native high-contrast.
7. **Independent browser** — repeat material web assertions in a second engine.
8. **Physical device/PWA** — installation/display-mode/update/offline behavior where applicable.
9. **AT + representative human** — screen reader and pilot comprehension/workload/preference remain separate final evidence classes.

## Shared provenance packet
Every run records build/SW/data version as applicable, engine/platform, display mode, viewport/insets/input, network state, actual resolved fonts, visible + semantics payload, focus/current/selection state, route/history, geometry, and transaction/persistence evidence if the fixture reaches those systems.

## Candidate 05 first fixtures
- month previous/next;
- Recent row → record → Back;
- Add Flight → return;
- View Logbook → return;
- Activity range selection;
- Search remains shell until SEARCH-001 is implemented.

## Performance evidence boundary
Lighthouse, DevTools, CI timing and synthetic traces are **LAB**. LCP/INP/CLS become **FIELD** only from provenance-bearing representative RUM/aggregate; no field Core Web Vitals claim is made here.

## CRITIQUE / failure conditions
- FAIL promotion if exact source cannot be tied to the run.
- FAIL if only static/golden appearance is available for behavioral claims.
- FAIL if native high-contrast is substituted for Web forced-colors or vice versa.
- FAIL if accessibility guideline tests are presented as WCAG conformance.
- FAIL if one primary-engine run is promoted as independent transfer.

## HANDOFFS TO OTHER SPECIALISTS
W117 is the shared execution envelope: T086 supplies type assertions, C117 state-color assertions, I104 action/state assertions, L108 geometry assertions and CD123 semantic/accessibility assertions. Contradictions return to the owning specialist rather than being patched silently in Web.