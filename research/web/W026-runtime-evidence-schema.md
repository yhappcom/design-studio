# W026 — Integrated Runtime Evidence Schema

Evidence type: SYNTHESIS / TRANSFER VALIDATION / OPEN

## RELATED DOMAIN CHECK
T022 is excluded from product typography. C028 requires focus/occlusion fields. L019 requires geometry fields. I014 requires request/outcome/recovery fields. CD032 requires message ID/revision. W025 remains the execution plan.

## Why
W025 cannot close Stage 3 with screenshots that cannot be joined across state, network, geometry, color and content. W026 defines the minimum evidence record before true-origin execution.

## Record schema
Each run records: capture ID; timestamp; browser/version; OS/device; physical vs simulated; URL/route/history action; viewport and zoom; input mode; semantic state; request/operation ID; dispatch/outcome classification; expected and observed recovery action; focused control; focus/overlay rectangles and occlusion class; forced-colors/theme; message ID + semantic revision + locale; overflow/reflow result; accessibility inspection method; artifact reference.

## Performance boundary
Diagnostic lab timings may be attached to a run but are not field Core Web Vitals. LCP/INP/CLS are labelled field evidence only when sourced from actual field/RUM population data with collection context; otherwise they remain lab/diagnostic evidence.

## Closure rule
A browser/device row is not PASS merely because the page loads. The end-to-end workflow must preserve state classification, safe recovery, focus/geometry, semantics and operability. AT evidence requires actual AT/runtime inspection; DOM structure alone is not AT evidence.

## Current result
**W026 EVIDENCE SCHEMA PASS / TRUE-ORIGIN EXECUTION OPEN.** The next Web work should implement W025 using this schema, not add isolated Chromium fixtures.

## HANDOFFS TO OTHER SPECIALISTS
C028/L019/I014/CD032 join evidence by capture ID. UX integration receives one traceable workflow record instead of disconnected specialist claims.