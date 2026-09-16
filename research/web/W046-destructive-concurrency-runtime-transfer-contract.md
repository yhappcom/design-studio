# W046 — Destructive-Concurrency Runtime Transfer Contract

## PURPOSE
Stage-3 product-transfer target extending W045 partial-order merge into concurrent delete/update, tombstone/retention uncertainty, restore and durable reconstruction. This prioritizes a real runtime closure class rather than another isolated Chromium micro-test.

## END-TO-END RUN
Use one shared run: r1 loaded in sessions A/B → A edits offline → B requests deletion → delete response loss variant → authority recheck → A late update arrives → explicit comparison verdict → conflict/policy resolution from product authority → current existence consequence → optional authorized restore as a new operation → restore response-loss variant → recheck → reload/deep-link/history → export/print.

Do not invent deletion-wins/update-wins/tombstone retention. Those are production dependencies. If unavailable, the correct runtime state is `policy/authority unavailable`, with unsafe actions blocked.

## REQUIRED PROVENANCE
Capture commit SHA, browser/engine/version, viewport/input, `runId`, `objectId`, branch/event IDs, delete/restore operation IDs, authoritative revision/comparison token, tombstone/retention evidence if supplied, network order, raw times/clock source, current existence verdict, enabled actions, semantic resource IDs/revision/locale, computed visual states, focus, geometry/reading order, route/history state and artifact hashes.

## ACCESSIBILITY / TRANSFER
WCAG 2.2 remains baseline. Validate keyboard/focus continuity when a live object disappears, status announcement semantics when executable AT is available, 200% text/reflow, forced-colors, locale expansion and print/export. Chromium plus an independent engine is required before cross-browser claims; Safari claims require Safari execution.

## PERFORMANCE BOUNDARY
Network/reconciliation/export timings in this run are lab/functional diagnostics. LCP/INP/CLS are field evidence only with an actual RUM population and field context.

## RELATED DOMAIN CHECK
T021 custom type remains blocked; use mature fallback. C046, I033/L037 and CD052 are direct dependencies. Production persistence/tombstone/idempotency/retention contracts belong to engineering/product authority.

## HANDOFFS TO OTHER SPECIALISTS
Return any runtime contradiction against I033 to Interaction; removal/recovery geometry to Layout; visual state leakage to Color; semantic/fallback failures to Content. Preserve shared IDs and raw artifacts.

## EVIDENCE BOUNDARY
Runtime contract ready; no executed W046 artifact, production deletion policy, cross-browser/Safari, AT, physical-device/print, field Core Web Vitals or human UX PASS.