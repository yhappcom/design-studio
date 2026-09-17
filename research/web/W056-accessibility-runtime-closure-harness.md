# W056 — Accessibility Runtime Closure Harness

Status: EXECUTION TARGET / PRACTICE
Date: 2026-09-17

## Problem
W053/W055 are blocked by missing executable breadth. More isolated browser theory will not close Stage 3. The next useful Web artifact is a shared runtime harness contract that every specialist can consume.

## SOURCE
WCAG 2.2 is the baseline. Current W3C guidance includes AA Focus Not Obscured (Minimum) and 24×24 CSS px Target Size (Minimum); reflow remains evaluated around 320 CSS px. Flutter provides Accessibility Guideline API tests for contrast, target size and labels, browser semantics inspection, and recommends testing very large scaling. Flutter also documents Android 14 nonlinear scaling up to 200%.

## HARNESS CONTRACT
Each run records: repository+commit/build ID; route/task; scenario ID; runtime/platform/browser engine; viewport/device pixel ratio; locale/currency; text scaling/zoom; theme/high-contrast state; data state. Artifacts: screenshot, semantics/accessibility tree where available, focus traversal trace, overflow/console logs, task result, and automated accessibility results.

Minimum scenario family: positive/negative/zero; estimated/final; complete/partial/unavailable; KRW/USD; long localization; narrow/wide; default/max text scaling. Browser claims require Chromium plus an independent engine; Safari/WebKit is separate when relevant.

## PERFORMANCE EVIDENCE BOUNDARY
Local traces, Lighthouse and synthetic timing are lab evidence only. LCP/INP/CLS become field evidence only when collected from an appropriate real-user field source; no field Core Web Vitals claim is inferred from this harness.

## RELATED DOMAIN CHECK
T025 supplies typography pressure; C056 semantic redundancy; L047 protected-group reflow; I043 focus/target/recovery; CD062 semantic/localization assertions.

## Gate effect
No W053/W055/W056 PASS is claimed. This intentionally stops contract expansion and points the next cycle toward actual execution.