# W069 — Product Repair Evidence Promotion Gate

Date: 2026-09-18
Stage: Stage 3 PRACTICE
Purpose: TRANSFER VALIDATION / STAGE CLOSURE

## Goal
Prevent a local widget repair from being promoted prematurely to browser or product-transfer PASS.

## Promotion ladder
1. SAME-BUILD WIDGET: repaired 390×844 baseline, enlarged-text contradiction scenario and 1024×768 workflow all execute without framework/layout assertions.
2. WEB BUILD: production Flutter Web build succeeds. This is build evidence only.
3. SERVED RUNTIME: load the built artifact through an HTTP server; capture console, network, screenshot, focus/keyboard and route/history evidence.
4. INDEPENDENT ENGINE: repeat critical workflow in a second browser engine before any cross-browser claim.
5. NETWORK/STATE: pending, known failure, ambiguous outcome, verify/reconcile and retry.
6. PERFORMANCE: lab traces remain LAB. LCP/INP/CLS are FIELD only when provenance identifies field collection such as CrUX/RUM.

## Accessibility baseline
Use WCAG 2.2 as the W3C baseline. Reflow, focus visibility/not-obscured, target geometry, semantics and keyboard operation remain required. Automated evidence does not replace human usability or assistive-technology comprehension.

## Failure vocabulary
EXECUTED-PASS, EXECUTED-FAIL, NOT-EXECUTED and BLOCKED must remain distinct at every rung.

## Handoff
Do not start isolated Chromium micro-tests while rung 1 remains red; repair closure has priority.