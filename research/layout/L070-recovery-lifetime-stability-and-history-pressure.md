# L070 — Recovery Lifetime, Stability & History Pressure

Status: **STAGE 3 PRACTICE / OPEN RUNTIME**  
Purpose: **EXTENSION** of L067–L069 using I066 multi-mutation/interruption sequences.

## RELATED DOMAIN CHECK
I066 supplies transaction lifetime/scope. CD084 supplies semantic distinctions. C078 supplies recovery-state layering. W078 supplies browser geometry manifest. T047 forbids solving recovery density by premature Type compression.

## SYNTHESIS
Recovery placement is a temporal-spatial problem. A surface that is acceptable for one mutation may fail under repeated mutations if it replaces itself, grows into a history stack, shifts targets, obscures focus, or disappears while the manipulated object remains off-screen.

## Architecture stress
Compare L069 architectures under: one mutation; three consecutive same-item moves; two-item interleaving; boundary rejection; Reset; navigation return. Record recovery-surface count, row/viewport displacement, focus and moved-item boxes, scroll offset, target visibility, wrapping and 200% text.

## Acceptance
- Recovery lifetime does not cause cumulative layout shift that moves the next intended reorder target unexpectedly.
- Coalescing, if chosen by Interaction, does not visually imply multiple independent Undo actions.
- History, if chosen, remains reachable without covering the active list or requiring semantic truncation.
- Expired/superseded recovery UI leaves a stable layout and no orphaned focus target.
- Short viewport, keyboard and safe-area conditions remain usable.

## CRITIQUE
Persistent history can maximize reversibility while consuming scarce customization space; transient recovery minimizes density but may disappear before repeated-workflow correction. Geometry cannot select transaction semantics, but it can reject a semantic policy whose presentation is unstable.

## OPEN
No recovery architecture PASS until I066 is implemented. Human discoverability and correction workload remain deferred.

## HANDOFFS TO OTHER SPECIALISTS
Interaction receives spatial feasibility constraints; Web receives repeated-mutation geometry fields; Content receives real available-space evidence only after rendering; Color receives overlapping recovery-layer states; Type receives reproduced rendering defects only.
