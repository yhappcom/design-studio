# T021 — Operational Corpus Proof Manifest

Date: 2026-09-16
Evidence: PRACTICE SPECIFICATION / CRITIQUE CONTRACT / OPEN

## RELATED DOMAIN CHECK
- **Color:** C030/C031-style state evidence cannot compensate for ambiguous `I/l/1` or `O/0` drawings.
- **Layout/Interaction:** L021/I017 require truthful action geometry and recovery semantics; Type must expose real string widths only after base metrics are valid.
- **Web:** W029/W030 runtime work must continue with mature system fonts until this gate closes.
- **Content:** CD034–CD036 supply operational and recovery strings; Type may not shorten semantic content to make an immature candidate fit.

## Purpose
T021 is blocked by operational breadth, not kerning. This manifest converts the bounded 33-character target into a reproducible proof corpus and failure ledger so the next drawing session can produce gate evidence rather than isolated glyphs.

## Mandatory proof families — kerning OFF
1. **Ambiguity:** `I1l`, `O0`, `IO10`, `LO1`, `NO0`.
2. **Airport/identifier:** dense uppercase clusters using the bounded repertoire, including `ICN`, `LAX`, `SFO`, `NRT`, `KIX`, `SIN`, `LHR` where supported by the declared corpus.
3. **Time/duration:** `01:05`, `11:11`, `17:40`, `23:59`, repeated-zero and repeated-one cases.
4. **Totals:** `0`, `10`, `100`, `1000`, `11:11`, repeated figures and mixed `0/1` sequences.
5. **Punctuation:** hyphen and comma in identifier/list contexts; colon vertically aligned in time strings.
6. **Accent path:** `É` beside `E`, with clipping/vertical-metric check.
7. **Operational sentence fragments:** use exact Content semantic strings when character coverage permits; otherwise record fallback rather than silently substituting wording.

## Sizes and comparison
Render every supported proof at 14/17/24 CSS-equivalent px with kerning disabled. Compare against proportional Roboto and the exact declared mono control only when the exact control artifact is available. Do not infer a universal spacing threshold from one control.

## Failure ledger
Each observation receives exactly one primary class before repair:
- D — drawing/contour;
- S — general sidebearing/spacing;
- R — raster/size-specific rendering;
- F — fallback/notdef/coverage;
- P — pair-specific residual after D/S/R/F are cleared.

Only P observations may enter T022. A visually improved pair produced by compensating D/S defects with kerning is a gate failure.

## T021 closure evidence package
Closure requires: bounded repertoire coverage; no unintended fallback/notdef; 14/17/24px proof captures; before/after critique for D/S/R failures; explicit residual-P list; exact source/build identity; and a statement of remaining browser/native/human evidence. Glyph count alone is insufficient.

## UX integration
Operational typography is a recognition and error-prevention dependency, but this non-human proof cannot establish pilot recognition speed, workload or task performance. Those remain HUMAN EVIDENCE OPEN until executable product validation.

## HANDOFFS TO OTHER SPECIALISTS
- **Content:** preserve semantic wording and provide stable semantic IDs for proof strings.
- **Layout/Web:** consume measured widths only after T021 closure; until then use mature production fonts.
- **Color:** do not treat color differentiation as remediation for glyph ambiguity.
