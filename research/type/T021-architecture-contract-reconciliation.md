# T021 — Architecture Contract Reconciliation

Classification: **CONTRADICTION REVIEW + METHOD CORRECTION**

## RELATED DOMAIN CHECK
- Type governance and current T021 status were re-read before this block.
- Color: prior C020 boundary remains applicable; color cannot repair glyph ambiguity.
- Layout/Interaction: current layout evidence must remain tolerant of candidate metric change; no A/B metrics are promoted.
- Web: current product control remains preferable to consuming an unvalidated bespoke family.
- Content: literal airport/identifier/numeric strings remain the operational proof corpus and must not be rewritten to improve typography.

## Trigger
The strict token-sensitivity audit measured the executable `ARCH` dictionary, while `T021-operational-token-consumer-matrix.md` specifies a partly different conceptual architecture. Treating the resulting 5 FULL / 2 PARTIAL / 4 NONE score as the final operational contract would therefore optimize implementation against a stale vocabulary.

## Exact contradiction
Current executable reset dictionary declares:

`stem, round_stem, cap_overshoot, x_overshoot, aperture, corner, join, diag_comp, terminal, figure_width, zero`

Current consumer specification instead defines the semantic obligations:

`stem, round_stem, aperture, cap/lower overshoot, diag_comp, terminal_policy, bowl_join, shoulder_tension, figure_width_mode, zero_treatment`

The differences are material:

1. `corner` exists in executable metadata but has **no canonical consumer obligation** in the consumer matrix.
2. `shoulder_tension` is a canonical consumer obligation for `n` / S-transition logic but has **no executable architecture token**.
3. `join` is too generic relative to the specified `bowl_join` semantics.
4. `terminal` is too generic relative to `terminal_policy`.
5. `figure_width` and `zero` are executable shorthand for the matrix's `figure_width_mode` and `zero_treatment`.
6. the executable split between `cap_overshoot` and `x_overshoot` is useful and should remain explicit rather than collapsing both into one label.

## Method correction
**STUDIO JUDGMENT:** do not make `corner` operational merely to turn a red audit cell green. A parameter belongs in an architecture only if it encodes a defensible, reusable design decision with named consumers.

The next executable architecture therefore uses this normalized vocabulary:

- `stem`
- `round_stem`
- `cap_overshoot`
- `x_overshoot`
- `aperture`
- `diag_comp`
- `terminal_policy`
- `bowl_join`
- `shoulder_tension`
- `figure_width_mode`
- `zero_treatment`

`corner` is removed unless a later drawing hypothesis demonstrates an independent corner-system need.

## Consumer obligations for normalized architecture
| Token | Required consumers | Required observable |
| --- | --- | --- |
| stem | H/I/E/F/L/T and straight segments | straight stroke/crossbar mass |
| round_stem | O/o/0 and B/D/P/R/8 | curve/counter mass |
| cap_overshoot | O/C/G and other genuinely round cap extrema | cap-round extrema |
| x_overshoot | o | lowercase round extrema |
| aperture | C/G plus S/5 only if their construction actually has a homologous opening parameter | opening geometry |
| diag_comp | A/V/X/K/R leg and genuinely diagonal figures | diagonal mass/placement |
| terminal_policy | open-form endings where a terminal exists | cut/shape/position |
| bowl_join | B/D/P/R/8 | bowl-to-stem/counter transition |
| shoulder_tension | n and defensibly homologous shoulder transitions | control-point/tension relationship |
| figure_width_mode | 0–9 | coordinated advance-width policy |
| zero_treatment | 0 only | plain/slashed treatment without O contamination |

### Important refinement
The previous strict audit incorrectly assumed that every token must change every listed consumer. That is valid only when the consumer relation is semantically mandatory. For `aperture`, forcing S and 5 to respond merely because C/G do would conflate different construction grammars. The executable test must therefore encode **mandatory consumers** separately from **conditional/homologous consumers**.

## Revised executable gate
For each token:
1. the token must have at least one mandatory named consumer;
2. perturbation must alter every mandatory consumer's intended outline/metric property;
3. unrelated protected glyphs must remain invariant where specified (`zero_treatment` must not alter O);
4. conditional consumers are tested only after their construction is declared homologous;
5. no predecessor constructor delegation is accepted for bounded glyphs;
6. 0–9 must remain under one figure-width policy;
7. kerning remains OFF.

This changes the audit from a crude "all names must hash differently" test into a **semantic sensitivity contract**.

## Decision
**KEEP** the perturbation/fingerprint method.  
**REWORK** its token vocabulary and mandatory-consumer semantics.  
**REJECT** implementation work whose only purpose is to make obsolete `corner` or non-homologous S/5 rows change.

The prior 5 FULL / 2 PARTIAL / 4 NONE result remains valid evidence about the old executable dictionary, but it is no longer the target score for architecture completion.

## Next executable block
1. introduce normalized architecture names in a successor harness rather than mutating historical evidence;
2. add `shoulder_tension` to lowercase `n` construction;
3. make `bowl_join`, `diag_comp`, and `terminal_policy` observable in their mandatory classes;
4. revise sensitivity audit to mandatory/conditional/protected consumer sets;
5. run CI; only a semantic FULL result reopens 36/36 A/B raster comparison.

## OPEN
- Whether S should share an aperture parameter with C/G is not established.
- Whether 5 should share an aperture parameter with C/G is not established.
- Whether a separate corner-system token is valuable is not established.
- Drawing quality, spacing, human recognition, native/browser transfer remain unpassed.

## HANDOFFS TO OTHER SPECIALISTS
Layout/Web should continue treating bespoke metrics as unstable. Content should preserve the exact operational strings. Color should not compensate ambiguous forms. No peer implementation should depend on the normalized architecture until its executable sensitivity and raster gates pass.