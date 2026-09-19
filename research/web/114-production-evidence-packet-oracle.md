# W114 — Production evidence-packet acceptance oracle

Date: 2026-09-20
Purpose: PRACTICE / Stage-3 closure instrumentation design after W113; no isolated Chromium micro-test.

## RELATED DOMAIN CHECK
T082/T083, C113/C114, I100/I101, L104/L105 and CD119/CD120 checked. W114 is the integration capture contract for their falsifiers, not ownership of their domain conclusions.

## Minimum provenance packet
For each shared scenario/run record: production build and service-worker/data version; URL/route/history entry; engine/version/display mode; viewport/input; network transition; requested/resolved fonts; semantic IDs and visible+a11y payload; focus/current/selection/state; element/target/sticky/scroll geometry; transaction ID/state/inverse; persistence and sync evidence; screenshots/traces only as supporting artifacts.

## Execution ladder
1. served production-equivalent primary engine, same scenario twice (REPLICATION);
2. independent engine (TRANSFER VALIDATION);
3. enlarged text and WCAG text-spacing;
4. applicable light/night/forced-colors/reduced-motion;
5. offline/reconnect and service-worker update/reload where the workflow can be interrupted;
6. physical mobile/iPad/PWA standalone when platform behavior is material.

A service-worker update is itself a state transition: immediate activation/takeover strategies can change control of open clients and therefore must not be treated as invisible plumbing when dirty drafts or pending mutations exist.

## Accessibility evidence boundary
WCAG 2.2 is the baseline. Individual techniques, ACT rules, automated checks or isolated success-criterion tests do not establish full conformance. Screen-reader/AT support and human usability remain separate evidence classes.

## Performance evidence boundary
Lighthouse, DevTools, CI and synthetic traces remain LAB. LCP/INP/CLS become FIELD evidence only with provenance-bearing representative RUM/aggregate.

## HANDOFFS TO OTHER SPECIALISTS
Return actual font failures to Type, semantic-state rendering to Color, focus/transaction failures to Interaction, geometry/reflow failures to Layout and visible/a11y semantic divergence to Content.

## Evidence boundary
No production runtime closure, Stage 3 PASS, WCAG conformance, independent-engine/device, AT, field Core Web Vitals or human UX PASS is claimed.