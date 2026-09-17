# W068 — Post-Repair Browser Closure Protocol

Status: PRACTICE / TRANSFER VALIDATION
Date: 2026-09-18

## Purpose
Prevent widget-test repair from being mistaken for Web Stage closure.

## Closure ladder
1. Same-build widget matrix: compact baseline, 200% text scale contradiction, wide workflow.
2. Flutter Web production build succeeds.
3. Serve the built artifact and exercise real route/runtime behavior.
4. Capture screenshot, semantics/accessibility evidence, focus trace, console/network logs, and task result under one build/scenario identity.
5. Repeat critical path in an independent browser engine before any cross-browser claim.
6. Expand to pending/failure/ambiguous/reconcile/retry and route/network interruption.

## Evidence vocabulary
EXECUTED-PASS, EXECUTED-FAIL, NOT-EXECUTED, BLOCKED. A skipped downstream step is never a product failure and a successful build is never a browser PASS.

## Performance provenance
Lighthouse/DevTools/local traces are LAB evidence. LCP/INP/CLS are FIELD evidence only when backed by field provenance such as CrUX or appropriately instrumented RUM; lab surrogates must not be relabeled as field results.

## Accessibility baseline
WCAG 2.2 is the current W3C baseline for this program. Browser closure includes reflow, focus visibility/not-obscured behavior, target behavior, semantic state, and non-color redundancy as applicable.

## Blockers
Human usability, AT comprehension on physical devices, and calibrated-display evaluation are outside automated browser closure and remain OPEN.
