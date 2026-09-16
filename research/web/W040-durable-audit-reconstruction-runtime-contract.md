# W040 — Durable Audit Reconstruction Runtime Contract

Evidence purpose: **STAGE 3 TRANSFER VALIDATION specification**.

## RELATED DOMAIN CHECK
I027 defines event truth; L031 defines current-vs-history spatial priority; C040 defines terminal/history visual encoding; CD046 owns durable event language; Type remains behind T021 repair. Web integrates and records runtime provenance.

## Runtime target
Extend W039 beyond terminal intervention into durable later retrieval. Fixture sequence: mutation A → conflict → compensation B → B response loss → reconciliation → changed authority → automatic chain termination → intervention-required → reload → deep link to object → open history → select prior event → return to current truth.

## Required provenance
Per run record commit SHA, browser engine/version, viewport/zoom, route/history transitions, object/correctionChain/operation/event IDs, presented and authoritative revisions, event certainty, semantic resource ID/locale, computed visual state, focus target, current-truth/history/action rectangles, overflow/occlusion, and network ordering.

Reload or deep-link success is not audit reconstruction PASS unless the event chain can be reconstructed from durable state rather than retained component memory. Browser back/forward must not manufacture or erase events.

## Accessibility/performance boundary
WCAG 2.2 remains baseline. Actual 200% zoom and forced-colors require executed captures. AT/physical-device evidence remains separate. Functional/lab timings are diagnostics; LCP/INP/CLS are field evidence only with an actual field/RUM population.

## Gate
W040 is ready for browser-capable execution. No runtime, cross-browser, Safari, AT, physical-device, field-performance or human UX PASS is claimed.

## HANDOFFS TO OTHER SPECIALISTS
C040/L031/CD046 consume the same run/event IDs; I027 compares reconstructed history to authoritative event truth; mature fallback remains required until T021 closes.