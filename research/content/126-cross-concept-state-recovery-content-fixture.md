# CD126 — Cross-Concept State/Recovery Content Fixture

## PURPOSE
Convert CD125 semantic invariants into a complete failure/recovery string fixture shared by Candidate 05/07.

## RELATED DOMAIN CHECK
T089 fit discipline, C120 semantic state separation, I107 authority transitions, L111 adaptive geometry and W119 provenance checked. Content does not redefine system truth.

## PRACTICE / CRITIQUE
For each implemented workflow map: object -> current state -> available action -> consequence -> recovery. Preserve distinctions where the implementation exposes them: invalid, pending, failed, unknown outcome, saved locally, synced, offline/degraded, stale and recovered.

Runtime capture must compare visible label/message with accessible name/role/state and actual action/destination. The same product action keeps canonical terminology across Candidate 05/07 unless product semantics genuinely differ.

Failure conditions:
- using `Saved` or `Synced` without corresponding authority;
- offering blind `Retry` after an unknown mutation when duplication is possible;
- collapsing No results with retrieval failure, or offline with save failure;
- geometry-driven abbreviation that changes meaning;
- concept-specific vocabulary churn used only to make the candidates feel different;
- color/position-dependent instructions.

Product-authored LogMate UI remains English-only; source/user Unicode and locale-sensitive dates/numbers remain stress inputs rather than a localization launch commitment.

## EVIDENCE BOUNDARY
No human comprehension, linguistic review, trust or task-performance PASS is claimed.

## HANDOFFS TO OTHER SPECIALISTS
Interaction must confirm authority before copy is accepted; Type/Layout own fit/reflow; Color supplies redundant visual state; Web captures visible+a11y+action parity from exact runtimes.
