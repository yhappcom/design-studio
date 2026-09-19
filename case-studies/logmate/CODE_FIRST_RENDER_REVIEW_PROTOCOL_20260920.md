# LogMate Code-First Render Review Protocol — 2026-09-20

Status: OWNER-CONFIRMED PROCESS CORRECTION

## Trigger

An image-only Home Candidate 02 attempt was rejected because it:
- visually mutated Candidate 01 instead of beginning from an independent code exploration;
- was generated from prose rather than from the designated structural restore point;
- had no code-render provenance;
- was shown without post-render specialist analysis.

## Required process

`restore point -> isolated candidate code -> contract tests -> code render/golden -> inspect actual render -> cross-specialist critique -> owner review -> save candidate`

Restore point:
`yhappcom/logmate checkpoint/home-structural-baseline-20260919 @ f992d62a98193629d19346a022a64deef824570c`

## Evidence rules

- Generative imagery is not UI implementation evidence in this phase.
- A render must originate from candidate code.
- No candidate number is promoted merely because code exists.
- A code branch without a successful render is UNRENDERED.
- A render without critique is INCOMPLETE.
- Candidate storage requires explicit analysis of successes, failures, and product/specialist fidelity.
- Candidate alternatives must be materially independent explorations, not cosmetic mutations of the prior candidate.

## Current Candidate 02 exploration

Branch:
`design/home-candidate-02-code-20260920`

Approach:
Index Folio — an asymmetric left index column paired with right-side operational content, deliberately distinct from Candidate 01's full-width vertical section grammar.

Current status:
**UNRENDERED / NOT YET CANDIDATE 02**

GitHub Actions currently creates the design-preview run but terminates before any job step begins, so no Flutter golden artifact exists yet. This runtime fact must not be represented as a design or test PASS.

## Review dimensions after a successful render

1. Asset fidelity.
2. Product semantics and canonical copy.
3. Type roles and operational geometry.
4. Color hierarchy and state salience.
5. Spatial rhythm/density.
6. Interaction affordance/state truth.
7. Content truth.
8. Runtime/render defects.
9. Distinctness from prior candidates.
10. Owner aesthetic judgement.

Only after this review may the exploration be stored as Candidate 02.
