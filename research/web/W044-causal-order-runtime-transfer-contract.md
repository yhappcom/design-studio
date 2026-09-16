# W044 — Causal Order Runtime Transfer Contract

## PURPOSE

Advance W043 toward Stage-3 closure by making causal order executable rather than adding another isolated browser micro-test.

## RUNTIME PROVENANCE

Each event record must preserve: `runId`, `objectId`, `eventId`, raw instant(s), clock source, locale/timezone, formatted text, authority revision, order/sequence token when available, ordering basis, certainty, displayed position, action enablement, semantic resource revision, focus, and geometry.

## REQUIRED END-TO-END RUN

Create r1 snapshot/history → inject skewed client event → create newer authoritative r2 → upload earlier offline event later → render history under locale/zone change → recheck live authority → attempt consequential action → export/print → reload/deep-link reconstruction.

Oracle: display sorting may change according to an explicit user-selected basis, but action enablement and current-authority presentation must remain bound to I031 authoritative evidence. Unknown cross-object ordering must not be fabricated.

Run in Chromium plus an independent engine before cross-browser claims; Safari requires Safari execution. Preserve raw artifacts, browser/engine/version, commit SHA and hashes.

## PERFORMANCE BOUNDARY

Execution timing is lab/functional diagnostic. LCP/INP/CLS are field evidence only with actual field/RUM population context.

## RELATED DOMAIN CHECK

Type: use mature fallback until T021 repair/spacing gates pass. Color: C044 visual oracle. Layout/Interaction: I031/L035 ordering and geometry oracle. Content: CD050 semantic/order labels. WCAG 2.2 remains accessibility baseline.

## HANDOFFS TO OTHER SPECIALISTS

Return shared run/event/artifact IDs so C044, I031/L035 and CD050 can independently accept/reject the same evidence.

## EVIDENCE BOUNDARY

Executable contract, not executed evidence. No W044 runtime, cross-browser, Safari, AT, physical print/device, field CWV, or human UX PASS.