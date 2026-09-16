# W038 — Compensation race runtime transfer contract

Date: 2026-09-16
Evidence purpose: **STAGE 3 TRANSFER VALIDATION CONTRACT / EXECUTION OPEN**

## RELATED DOMAIN CHECK
T021 remains pre-product; C038 owns computed visual truth; I025 owns compensation semantics; L029 owns geometry; CD044 owns correction language. Web owns browser/runtime integration and provenance.

## Stage-closure value
W037 covered concurrent mutations. W038 adds the next product-relevant failure class: a mutation appears successful but newer authority requires rollback or a compensating operation, whose response may itself be delayed/lost.

## Runtime fixture sequence
`rev1 → opA dispatch → optimistic success presentation → rev2/conflict → late opA response → reconcile → rollback/compensation decision → opC dispatch → optional response loss → opC reconcile → stable deep-link/history retrieval`.

## Required provenance per run
commit SHA; fixture/backend revision; browser engine/version; viewport and zoom class; locale/resource revision; object/opA/opC IDs; base/presented/authoritative revisions; network event ordering; I025 state/action verdict; actual enabled/disabled controls; CD044 semantic IDs; C038 computed visual state; L029 rectangles/focus order; final retrieval revision.

## Assertions
- late opA response cannot silently overwrite newer authority;
- compensation has independent operation identity/certainty;
- response loss during compensation yields outcome-unknown until reconciliation;
- rendered action availability matches I025;
- stale success styling does not survive as current semantic truth;
- deep-link/history restoration retrieves authoritative final state, not merely cached presentation;
- actual 200% zoom and forced-colors are separate executed modes, not inferred from narrow viewport or static CSS.

## Performance boundary
Functional/lab timings may diagnose implementation. LCP/INP/CLS are labeled field evidence only with actual field/RUM population context; no lab surrogate is promoted to field evidence.

## Execution boundary
No multi-engine W038 artifact exists in this run. Chromium plus an independent engine are required before cross-browser claims; Safari claims require Safari execution. WCAG 2.2 remains the accessibility baseline.

## HANDOFFS TO OTHER SPECIALISTS
Executed run IDs are the shared evidence key for C038, I025/L029 and CD044. Type transfer waits for T021 drawing/general-spacing closure.