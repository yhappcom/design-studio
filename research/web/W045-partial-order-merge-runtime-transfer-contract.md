# W045 — Partial-Order Merge Runtime Transfer Contract

## PURPOSE
Stage-3 runtime closure target extending W044 from causal sequence to concurrent, non-comparable branches and authoritative merge.

## END-TO-END RUN
Execute one shared run: r1 loaded → device/session A edits offline → device/session B edits from r1 → B reaches authority → A arrives later but remains concurrent/incomparable under the product ordering contract → UI exposes conflict without choosing by wall clock → authorized merge/reconciliation → merge response delayed/lost variant → authority recheck → merged current consequence → reload/deep-link/history → export/print snapshot.

## REQUIRED PROVENANCE
Capture commit SHA, browser/engine/version, viewport/input, `runId`, `objectId`, branch/event IDs, causal/ordering tokens, raw instants and clock source, receive times, authority revision, comparison verdict, merge operation ID, merge certainty, enabled actions, semantic resource IDs/revision/locale, computed visual states, focus, geometry/reading order, route/history state, network ordering and artifact hashes.

A PASS cannot be inferred from DOM order or later timestamps. The runtime oracle must agree with I032. C045 visual precedence, L036 geometry and CD051 semantics must be evaluated against the same IDs.

## BROWSER / PERFORMANCE BOUNDARY
Chromium plus an independent engine is required before cross-browser claims; Safari claims require Safari. WCAG 2.2 remains baseline. Synthetic timings are lab/functional diagnostics. LCP/INP/CLS become field evidence only with actual RUM population/context.

## RELATED DOMAIN CHECK
Type remains on mature fallback pending T021 repair. C045, I032/L036 and CD051 are direct dependencies. Production backend merge/idempotency/deduplication semantics must be supplied by the product/engineering authority rather than invented by Web.

## HANDOFFS TO OTHER SPECIALISTS
Return runtime contradictions to the owning specialist. Preserve raw artifacts and shared IDs so visual, spatial, interaction and content verdicts are reproducible.

## EVIDENCE BOUNDARY
Runtime contract ready; no executed W045 artifact, cross-browser/Safari, AT, physical-device/print, production-backend integrity, field Core Web Vitals, or human UX PASS.