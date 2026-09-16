# T021 — Successor semantic architecture contract

Classification: **CONTRADICTION RESOLUTION + METHOD DESIGN**

## Purpose
Freeze the semantic contract for the successor A/B harness before further outline construction. Historical harnesses remain evidence and are not mutated.

## RELATED DOMAIN CHECK
Color C021 cannot compensate glyph ambiguity. L013 keeps geometry flexible. W021 blocks custom-font transfer until drawing validity. CD021 preserves literal operational strings.

## Normalized architecture vocabulary
`stem`, `round_stem`, `cap_overshoot`, `x_overshoot`, `aperture`, `diag_comp`, `terminal_policy`, `bowl_join`, `shoulder_tension`, `figure_width_mode`, `zero_treatment`.

`corner` is not a successor token unless later evidence establishes an independent reusable corner system.

## Consumer semantics
### Mandatory
A mandatory consumer must exhibit the intended outline/metric delta when the token changes.
- `stem`: straight-stem construction classes.
- `round_stem`: round/bowl stroke-mass classes.
- `cap_overshoot`: designated cap-round classes.
- `x_overshoot`: lowercase round proof class (`o`) where present.
- `diag_comp`: actual diagonal stroke structures, not merely glyph names containing diagonals conceptually.
- `bowl_join`: bowl-to-stem/junction structures in B/D/P/R and homologous 8 junction where construction shares it.
- `shoulder_tension`: `n` shoulder; other consumers only after homologous construction is demonstrated.
- `figure_width_mode`: all figures through one width policy.
- `zero_treatment`: zero only.

### Conditional
- `aperture`: C/G are mandatory open-form consumers; S/5 participate only if their construction uses the same aperture parameter rather than a separate terminal/counter decision.
- `terminal_policy`: only structures whose terminal shape is actually controlled by the shared policy.

### Protected
Operational identifier characters unrelated to a perturbed token should remain invariant where the architecture contract says they are unrelated. Unexpected deltas are diagnostics, not harmless noise.

## A/B material-difference rule
A and B are not valid alternatives merely because token dictionaries differ. Every declared A/B difference must produce an observable outline or metric difference in its intended consumer class. A difference that never reaches geometry is metadata, not architecture.

## Successor audit result categories
For each token:
- `FULL`: all mandatory consumers show intended delta; protected set remains invariant; conditional behavior is documented.
- `PARTIAL`: at least one mandatory consumer fails or an unexplained protected consumer changes.
- `NONE`: no intended mandatory effect.
- `INVALID_CONTRACT`: consumer expectation itself is not semantically defensible.

Only all-`FULL`/documented-conditional architecture reopens raster critique.

## Gate result
**SEMANTIC SUCCESSOR CONTRACT PASS; EXECUTABLE SUCCESSOR OPEN.**
No drawing/spacing/kerning gate changes.

## HANDOFFS TO OTHER SPECIALISTS
Layout/Web continue with current flexible/product font metrics. Content keeps literal identifiers intact. Color remains non-compensatory.