# W055 — Flutter Product Lab Accessibility & Runtime Transfer

Status: **TRANSFER VALIDATION / SOURCE-LEVEL PRODUCT ARTIFACT READY / EXECUTION OPEN**  
Date: 2026-09-17  
Stage relevance: Stage 3 systems practice

## Question

What evidence is required before a Flutter mobile/web Product Lab can claim that responsive, semantic and accessibility decisions survived real runtime transfer?

## SOURCE

### Flutter web accessibility

Flutter documents that web accessibility is produced by translating the framework Semantics tree into an accessible HTML DOM. Flutter web accessibility is not automatically equivalent to visual rendering; accessibility mode and the exported semantics tree must be inspected.

Source:
- https://docs.flutter.dev/ui/accessibility/web-accessibility

### Flutter accessibility testing

Flutter recommends platform inspection and its Accessibility Guideline API. Web validation should inspect the accessibility tree; mobile validation should include platform tools such as Accessibility Inspector and screen readers.

Source:
- https://docs.flutter.dev/ui/accessibility/accessibility-testing
- https://docs.flutter.dev/ui/accessibility

### Text scaling

Android 14 nonlinear font scaling reaches 200%, and Flutter recommends testing the maximum setting. A scalar laboratory surrogate is not equivalent to actual nonlinear runtime scaling.

Source:
- https://docs.flutter.dev/release/breaking-changes/android-14-nonlinear-text-scaling-migration

### WCAG baseline

Design Studio uses WCAG 2.2 as the current W3C baseline for web accessibility. Target-size, focus, reflow, contrast and other success criteria must be assessed against the applicable rendered/browser behavior rather than inferred from source intent.

Source:
- https://www.w3.org/TR/WCAG22/

## Product transfer — MintTap

MintTap 1.0.29 is a Flutter application with mobile and web-capable source. The isolated `design-lab/minttap-1.0.29` candidate deliberately bypasses Firebase/auth/ads/user data and provides synthetic workflows spanning activation, portfolio, holding, transaction, insights and settings.

The branch currently has no verified Flutter-capable CI/runtime execution attached to this Product Lab. Therefore source implementation is **not** promoted to browser/device PASS.

## Runtime evidence package

A useful Product Lab artifact must bind all evidence to an exact identity.

### Build identity

Record:

- repository;
- branch;
- commit SHA;
- Flutter/Dart version;
- build mode;
- target platform;
- dependency lock identity where material.

### Scenario identity

Record:

- journey/screen;
- synthetic scenario variant;
- currency;
- gross/net state;
- positive/negative total performance;
- ready/estimated/partial/unavailable data state;
- locale;
- viewport/device profile;
- system text scaling or browser zoom;
- theme/high-contrast/forced-colors mode where applicable.

### Runtime identity

For web:

- browser + version + engine;
- route/path;
- keyboard/pointer/touch mode tested;
- semantics/accessibility mode state;
- network/cache/service-worker conditions where relevant.

For mobile:

- OS/device/simulator;
- text size/accessibility category;
- VoiceOver/TalkBack state where tested;
- orientation and window class.

### Artifact outputs

Capture as appropriate:

- screenshot/render;
- semantics/accessibility-tree snapshot;
- overflow/exception logs;
- automated accessibility checks;
- focus traversal record;
- input/task result;
- test command/log;
- raw performance trace when performance is under study.

## Required transfer matrix

At minimum, the integrated MintTap candidate should eventually cover:

1. normal phone / default text;
2. narrow phone / large text;
3. 200% supported scaling on an appropriate platform;
4. long localized labels;
5. KRW and USD long values;
6. negative-total-return/high-distribution contradiction;
7. partial/unavailable states;
8. keyboard/focus path on web;
9. browser accessibility tree;
10. Chromium + an independent browser engine before a cross-browser claim;
11. Safari/WebKit separately where relevant to the shipping surface.

## Performance evidence rule

Lab timing is diagnostic evidence only.

- synthetic frame/build timing ≠ field performance;
- local browser LCP/INP/CLS ≠ population field LCP/INP/CLS;
- a Lighthouse or lab run can identify regressions but does not become RUM evidence.

Field Web Vitals require actual field/RUM population evidence with appropriate sampling and route/device context.

## PRACTICE

The Product Lab source now avoids the production compact-iOS global text-scale clamp and uses responsive stack/reflow behavior in shared components. It also separates financial status semantics and protects first-value/ad boundaries.

This creates a substantially better **execution target**, but W055 remains OPEN at runtime because the current connected environment does not provide a verified Flutter execution result for the branch.

## CRITIQUE

Source review can detect likely risks but cannot prove:

- actual semantics node order;
- browser DOM/ARIA export;
- focus visibility/restoration;
- no visual overflow;
- touch target physical usability;
- cross-engine layout parity;
- screen-reader phrasing;
- service-worker/offline behavior;
- field performance.

Do not convert implementation intent into runtime claims.

## RELATED DOMAIN CHECK

### Type
T024 defines nonlinear scaling pressure and string corpus. W055 must record the actual runtime scaling mode, not a guessed scalar.

### Color
C055 semantic roles require forced-colors/grayscale/high-contrast transfer checks.

### Layout / Interaction
L046/I042 define workflow order, reflow and owner-review gates. Browser route/focus/history evidence must preserve those contracts.

### Content
CD061 state/financial terminology must survive browser accessibility naming and localization.

### UX integration
End-to-end task evidence is stronger than isolated component screenshots. Owner review should receive a coherent artifact set after internal runtime validation.

## HANDOFFS TO OTHER SPECIALISTS

### Type
Return actual wrap/raster/fallback findings by locale and scale.

### Color
Return authored-versus-forced/high-contrast semantic survival findings.

### Layout / Interaction
Return focus, route, viewport and reflow failures with exact scenario identity.

### Content
Return accessible-name, truncation/wrap and localization findings.

## Gate effect

W055 does not replace or close W053. W053's multi-engine graph-integrity execution remains an independent Stage 3 closure blocker. W055 adds a real-product runtime target and evidence protocol, but Web remains Stage 3 PRACTICE / NOT PASSED until executable evidence supports closure.
