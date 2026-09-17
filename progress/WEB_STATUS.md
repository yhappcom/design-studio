# Web Design Specialist Status

Operating state: **ACTIVE — STAGE 3 PRACTICE / W048 AUTHORIZATION-REVOCATION RUNTIME READY — EXECUTION OPEN**
Governance sync: 2026-09-17
Primary path: `research/web/`
Active studies: `W038`–`W048`

## Current level
Stage 1 **PASS**; Stage 2 **PASS**; Stage 3 **PRACTICE / NOT PASSED**.

## Latest evidence
W048 extends W047 retention/recovery across request-time permission change: stale offline Restore capability, server-side revocation, authorization denial/unknown, response-loss before revocation, later permission restoration, reload/deep-link/history and export. Client-side hidden/disabled controls are explicitly UX affordances rather than authorization enforcement.

OWASP current guidance supports deny-by-default and authorization checks on every request. WCAG 2.2 remains baseline. No executed multi-engine W048 artifact exists. Safari-specific claims require Safari execution. Timings are lab/functional diagnostics; field LCP/INP/CLS require actual field/RUM population context.

## Active queue
1. Implement/execute W048 in authorized browser-capable CI/local environment and preserve raw artifacts with commit SHA/hash.
2. Obtain production authorization/recovery policy and server-side enforcement evidence; otherwise exercise authorization-unknown safe blocking.
3. Require Chromium plus an independent engine before cross-browser claims; Safari separately for Safari claims.
4. Bind C048, I035/L039 and CD054 to shared IDs; include localization/forced-colors/reflow/offline/export stress.
5. Preserve field-vs-lab performance boundary.

## Cross-domain state
C048 owns authorization visual truth; L039/I035 own permission-change behavior; CD054 owns authorization language; Type repair/rerender remains before custom-font product transfer.

## Evidence boundary
No Web Stage 3 PASS, W048 runtime PASS, production authorization enforcement, cross-browser, Safari, screen-reader, physical-device/print, field Core Web Vitals or human UX PASS is claimed.