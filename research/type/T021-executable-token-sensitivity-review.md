# T021 — Executable Architecture Token Sensitivity Review

Status: **EXACT CI EXECUTED / TOKEN OPERATIONALITY FAIL / IMPLEMENTATION TARGET NARROWED**  
Date: 2026-09-16  
Owner: Typography / Type Design Specialist

## SOURCE → EXECUTION

`T021-token-sensitivity-audit.py` perturbs one architecture token at a time, rebuilds the bounded family, and fingerprints each glyph's compiled `glyf` plus `hmtx`. GitHub Actions run `35048091113`, job `104642269401`, completed successfully on Ubuntu 24.04 / Python 3.13.15 / FontTools 4.65.0 / Pillow 12.3.0. Artifact `10427966577` was uploaded.

This is executable geometry evidence. It is not drawing-quality, readability, human, Flutter, browser or device evidence.

## Result

The first audit established the following actual sensitivity in the current constructors:

| token | observed state against required consumer matrix | evidence |
| --- | --- | --- |
| `stem` | FULL for the matrix's required consumers | all named required consumers changed |
| `round_stem` | FULL | all named required consumers changed |
| `cap_overshoot` | PARTIAL | C/G/O/U changed; S/0 did not |
| `x_overshoot` | FULL | o changed |
| `aperture` | PARTIAL | C/G changed; S/5 did not |
| `corner` | NONE | no glyph changed |
| `join` | NONE | no glyph changed |
| `diag_comp` | NONE | no glyph changed |
| `terminal` | NONE | no glyph changed |
| `figure_width` | FULL | 0–9 all changed |
| `zero` | FULL | 0 changed and O did not |

Therefore only 5/11 declared token groups are fully operational against the specified consumer matrix; 2/11 are partial and 4/11 are zero-effect. The architecture is not operationally complete.

The audit source was then tightened so `FULL` requires every required consumer to change; `PARTIAL` and `NONE` are explicit gate failures. This corrects the weaker first-pass boolean rule where any one changed consumer could label a token operational.

## SYNTHESIS

This experiment changes the next task materially. The problem is no longer vaguely 'make parameters real'. Four zero-effect tokens and two incomplete consumer paths are now isolated:

1. `corner`: implement observable corner treatment in C/G/S/5/E/F where the architecture claims it;
2. `join`: drive B/D/P/R/8 bowl joins rather than independent local recipes;
3. `diag_comp`: drive A/V/X/K/N/R and diagonal figures 2/4/7;
4. `terminal`: drive C/G/S/5/E/F endings;
5. `cap_overshoot`: extend only where structurally justified, but reconcile the matrix expectation for S/0 rather than silently claiming full coverage;
6. `aperture`: make S/5 consume the policy or narrow the architecture contract if aperture is not semantically appropriate there.

The last two points matter: a consumer matrix is itself a hypothesis. If a token should not affect a glyph, the correct action is to revise the declared contract with a design rationale, not force a meaningless geometry delta merely to satisfy an assertion.

## STUDIO JUDGMENT

Do not reraster A/B yet. Another 14/17/24 specimen before the four NONE and two PARTIAL groups are resolved would repeat the same invalid method. The next build should first make the sensitivity audit FULL under a defensible consumer contract, then regenerate the full family and inspect drawing.

If a genuinely operational A/B rebuild still fails drawing, execute the already-defined bespoke-vs-current-Roboto method comparison rather than beginning another serial R4-style patch cycle.

## RELATED DOMAIN CHECK

- Layout/Interaction: no A/B metrics become stable from this audit.
- Web: no transfer test is justified yet.
- Content: literal operational corpus remains the proof input.
- Color: ambiguity remains a glyph-identity problem; color is not a compensator.

## HANDOFFS TO OTHER SPECIALISTS

No downstream specialist should freeze geometry around either custom candidate. Current proportional Roboto remains the product control until T021 produces drawing-valid evidence.
