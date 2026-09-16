# CD050 — Causal Order / Sorting Language System

## PURPOSE

Extend CD049 so language does not convert display-time recency into authoritative or causal truth.

## SEMANTIC CONTRACT

Keep distinct resources/concepts for: event occurred, observed, received/uploaded, authority confirmed, reconciled, snapshot generated, live rechecked, and authoritative sequence/order when exposed. `Latest` is forbidden unless its basis is explicit and correct for the task.

Sorting labels must name the basis where ambiguity matters: e.g. event time, received time, or authoritative sequence. If cross-object order is unknown/non-comparable, wording must not imply a total order.

Relative time may support scanning but cannot replace durable absolute/provenance time in audit/recovery surfaces. Localization may change field order, 12/24-hour form, and zone display without changing ordering semantics.

## TEST VECTORS

Clock skew; offline late upload; equal formatted timestamps/different sequence; missing event time with revision; non-comparable revisions; DST/zone change; pseudo-expansion; missing-resource fallback; snapshot/current co-display.

## RELATED DOMAIN CHECK

Type: T021 repaired glyphs must survive unchanged strings; wording is not shortened to hide ambiguity. Color: C044 cannot encode order alone. Interaction: I031 owns actual order/action truth. Layout: L035 owns role/value locality. Web: W044 supplies runtime/resource evidence.

## HANDOFFS TO OTHER SPECIALISTS

W044 should record semantic resource ID/revision with ordering basis. I031 remains source of truth if wording and state disagree.

## EVIDENCE BOUNDARY

Semantic/localization contract only. No real Flutter/TMS/ARB round trip, linguistic review, AT, or human comprehension/task PASS.