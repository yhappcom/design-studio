# L036 — Concurrent Branch / Merge Spatial Contract

## PURPOSE
Spatial companion to I032. A list sorted into one dimension must not imply that incomparable branches have an authoritative winner.

## INFORMATION SPINE
For a conflicted object preserve: object/current authority → branch comparison verdict → branch A provenance/consequence → branch B provenance/consequence → merge/reconciliation state → safe actions → durable history.

When branches are incomparable, do not use vertical position alone as semantic priority. Reflow may stack branches, but each branch keeps identity and provenance. After merge, historical branches remain inspectable while the merged authoritative consequence is visually/spatially separated as current truth.

## STRESS MATRIX
Validate narrow mobile, tablet split view, desktop table/detail, 200% text, long localization, RTL, zoom/reflow, page break/print, keyboard focus movement, one branch expanded and the other collapsed. A branch label, its consequence and its action must not become detached during recomposition.

## RELATED DOMAIN CHECK
- I032 owns branch comparability and action safety.
- C045 owns state cue precedence.
- W045 owns browser geometry/runtime evidence.
- CD051 owns branch/merge wording and localization expansion.
- Type metrics remain provisional until T021 drawing/spacing gates.

## HANDOFFS TO OTHER SPECIALISTS
W045 should record bounding boxes/reading order/focus for branch provenance, consequence and merge action. Content may expand but must not be shortened to preserve a preferred two-column layout.

## EVIDENCE BOUNDARY
Static/deterministic spatial contract only; no executed browser/native geometry, AT reading order, physical-device, or human scanning/workload PASS.