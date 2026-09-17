# I058 — MintTap Recovery Observability Contract

Date: 2026-09-18
Purpose: **TRANSFER VALIDATION / SYSTEMS PRACTICE**
Stage: Stage 3 PRACTICE.

## QUESTION
Once the primary Material feedback failure is repaired, what observable evidence is required to distinguish known failure from ambiguous outcome and make retry safe?

## STATE MODEL
Two families must remain separate.

### Known failure
`idle → submit → pending → known_failure → correction/retry → pending → success`

Required observables: action accepted, pending state, failure cause at the product's known level, retained user input where safe, available correction/retry, success confirmation.

### Ambiguous outcome
`idle → submit → pending → ambiguous → verify/reconcile → known outcome → safe next action`

Required observables: do not assert failure or success prematurely; prevent unsafe duplicate action where material; provide verification/reconciliation path; expose the resolved outcome before normal retry.

## PRACTICE — evidence ledger
For each transition capture:
- triggering action;
- system truth/state ID;
- enabled/disabled actions;
- visible feedback surface;
- focus destination and keyboard reachability;
- content message key/variables;
- persistence/retrieval/history consequence;
- retry idempotency or duplicate-risk assumption;
- screenshot/semantics/log evidence.

## CRITIQUE
Removing splash/focus/selected feedback to silence a Material assertion is not a valid repair because it reduces observability. Likewise, wording an ambiguous state as `Failed` manufactures certainty the interaction model does not possess.

## ACCESSIBILITY / UX BOUNDARY
WCAG 2.2 Focus Not Obscured (Minimum) requires a focused component not be entirely hidden by author-created content; Target Size (Minimum) sets a 24×24 CSS-pixel baseline for pointer targets on the web, subject to stated exceptions.

- https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/

These are conformance constraints, not proof that people understand the recovery flow. Human discoverability, workload, trust and professional-task performance remain OPEN.

## RELATED DOMAIN CHECK
- Type: labels/status text must render without width-compensation hacks.
- Color: C071 validates visible/non-color state distinction.
- Layout: L062 must preserve focus, target and recovery-action geometry after recomposition.
- Web: must execute keyboard/focus/network ambiguity in served runtime after widget smoke.
- Content: owns exact pending/failure/ambiguous/reconcile wording, not state truth.
- UX: end-to-end recovery coherence is reviewed non-human first; human evidence remains separate.

## HANDOFFS TO OTHER SPECIALISTS
Content receives explicit state IDs and allowed assertions. Web receives network ambiguity scenarios. Color receives state combinations. Layout receives focus/recovery action geometry requirements.

## EVIDENCE BOUNDARY
No product recovery flow has been executed by this study. No Material repair PASS, network ambiguity PASS, AT or human usability PASS is claimed.
