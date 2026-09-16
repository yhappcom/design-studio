# T021 — Executable architecture-token operationality review

Classification: **INDEPENDENT VALIDATION + CONTRADICTION REVIEW**

## Question
Does the current A/B family-architecture reset actually consume its declared architecture tokens in outline/metric construction, rather than merely storing them as metadata?

## RELATED DOMAIN CHECK
- **Type:** checked the T021 operational architecture gate, token-consumer matrix, construction-complete harness, and the new executable sensitivity audit.
- **Color:** C020 keeps character identity independent of hue; no Color result can rescue Type ambiguity or drawing failure.
- **Layout/Interaction:** L012/I007 explicitly keep geometry flexible until T021 is valid; no fixed UI geometry is assumed here.
- **Web:** W020 waits for a drawing-valid custom family before custom-font runtime transfer.
- **Content:** CD020 preserves literal airport, registration, flight and numeric identifiers; these remain unchanged proof strings.

## Evidence levels
### SOURCE / executable method
`T021-token-sensitivity-audit.py` performs single-token perturbation against architecture A, rebuilds the bounded family, fingerprints `glyf + hmtx`, and checks whether at least one declared consumer changes.

This is materially stronger than the prior static consumer matrix because a metadata-only token cannot pass merely by appearing in an architecture dictionary.

### CONTRADICTION / method limitation
The current audit's `operational` predicate is intentionally weak: **one changed glyph inside the required consumer set is sufficient**. It does not prove that:
1. every required consumer uses the token;
2. only intended consumers use it;
3. the magnitude/direction of change is appropriate;
4. architecture A and B are materially coherent alternatives;
5. drawing quality improved.

Therefore `all_declared_tokens_operational=True`, if obtained, is not equivalent to the stronger architecture gate described by the consumer matrix.

### Boundary correction
A workflow was added outside the ordinary Type writing boundary. `AGENTS.md` restricts ordinary Type writes to `research/type/` and `progress/TYPE_STATUS.md`. The workflow was removed. No exact CI PASS is claimed from it; commit-associated workflow lookup returned no run.

## Gate decision
The executable audit is **KEEP as a diagnostic**, but its present boolean must be treated as **minimum sensitivity evidence**, not complete consumer operationality PASS.

Before drawing critique can be reopened, the executable gate should require:
- per-token expected-consumer coverage, not any-hit;
- unexpected-consumer reporting;
- explicit exceptions where a token is class-level but not universal;
- A/B geometry-delta proof for tokens whose values differ;
- zero predecessor delegation;
- kerning OFF;
- full 36/36 bounded repertoire and identical 14/17/24 corpus after the stronger gate.

## Decision boundary
Do **not** open spacing or T022. Do **not** claim that the latest sensitivity harness closes architecture operationality. The next Type implementation should strengthen the audit itself, then rebuild/reraster A/B. If both genuinely operational complete architectures still fail drawing, execute the already-declared bespoke-vs-proportional-Roboto method comparison rather than another local-patch sequence.

## HANDOFFS TO OTHER SPECIALISTS
- **Layout/Web:** continue using flexible/current-product geometry; no custom Type metric freeze.
- **Content:** keep literal identifiers/numerics unchanged in stress corpora.
- **Color:** no color compensation for glyph ambiguity.

## Evidence boundary
No custom-family drawing, readability, recognition, preference, spacing, kerning, browser/native, physical-device or human PASS is claimed.