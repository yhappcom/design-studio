# L048 / I044 — End-to-End Accessibility Acceptance

Status: STAGE 3 PRACTICE / TRANSFER VALIDATION SPEC

## PURPOSE
Join L047 protected semantic groups and I043 focus/target/recovery into one workflow-level acceptance model.

## SOURCE
WCAG 2.2 adds Focus Not Obscured (Minimum) and Target Size (Minimum) 24 CSS px with exceptions. Flutter's product guidance is stronger for Flutter tappable targets: 48×48 logical pixels on Android and its release checklist recommends 48×48 tappable targets. WAI reflow guidance requires information/functionality to survive enlarged text/small viewports without two-dimensional scrolling in applicable web conditions.

## PRACTICE
Run Start → Portfolio → Holding → Add Transaction → Insights/ROC/Tax → Settings with default/max text, narrow/wide viewport, long localization, keyboard/focus where supported, error/recovery, partial/unavailable and negative/ambiguous financial states.

Failures include: label/value/qualifier separation; field/error/correction separation; state/action/recovery separation; focus obscured by sticky/overlay content; visual order diverging from focus/semantic order; undersized Flutter targets; first-value path interrupted by promotional content; recovery losing prior context; avoidable two-dimensional scrolling.

## CRITIQUE
Passing isolated screens does not establish workflow coherence. Recomposition may change columns to stacks, but semantic and temporal adjacency must survive.

## RELATED DOMAIN CHECK
T026 supplies immutable string pressure. C057 supplies redundant state carriers. W056 supplies runtime identity. CD062/CD063 semantics govern visible/nonvisual state truth.

## HANDOFFS TO OTHER SPECIALISTS
Web should capture focus trace and semantics order. Content should ensure recovery actions describe actual state. Type should flag raster/fallback failures separately from spatial failures.

## OPEN
No AT, physical-device, discoverability or representative-user evidence is simulated.