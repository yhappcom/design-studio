# L030 — Correction-chain escalation layout contract

Date: 2026-09-16
Evidence class: **SYSTEMS PRACTICE / responsive transfer specification**

## RELATED DOMAIN CHECK
I026 owns correction-chain termination; C039 owns terminal-state visual precedence; W039 owns runtime geometry; CD045 owns intervention language; Type metrics remain provisional behind T021.

## Spatial invariant
When an automatic correction chain terminates or escalates, the layout must keep the following in one recoverable information neighborhood without implying that history is the current state:
`affected object → current authoritative consequence → correction-chain status → reason automation stopped → safe next action → history/detail`.

## Stress cases
Validate baseline, 320 CSS px reflow, actual 200% zoom, localized expansion, sticky layers, focus transition after escalation, and reduced visual viewport where executable.

History may collapse behind disclosure, but current consequence and safe action may not be pushed below stale optimistic-success material. Repeated correction cards must not accumulate indefinitely; historical operations belong in durable history while the current surface summarizes the chain.

## Geometry verdicts
Record rectangles for current consequence, escalation explanation, primary safe action, focus target and authored sticky/overlay layers. PASS requires logical reading order, no horizontal overflow at the declared reflow case, reachable safe action, no complete focus obscuration under WCAG 2.2 AA baseline, and no stale success region retaining greater spatial dominance than the terminal state.

## HANDOFFS TO OTHER SPECIALISTS
C039 consumes dominance/overlay captures; W039 records actual rectangles and viewport provenance; CD045 supplies bounded terminal strings; Type later supplies accepted metrics.

## Evidence boundary
320px reflow is not evidence of actual 200% browser zoom. DOM geometry is not human salience evidence. No human discoverability/workload claim is made.
