# T021 — Family Architecture Reset / A–B Method Comparison

Date: 2026-09-16  
State: **EXECUTABLE ARCHITECTURE RESET BUILT / METHOD DEFECT FOUND BEFORE DRAWING PASS**

## Purpose

R4E established that serial local repair is not a sufficient family-building method. This block therefore resets the method before spacing or kerning: define two materially different complete operational-family architectures first, then construct the same bounded LogMate repertoire from those architecture contracts.

This is a **METHOD COMPARISON + CONTRADICTION REVIEW**. It is not R4F.

## RELATED DOMAIN CHECK

- **Type:** T021 R3–R4E evidence was checked. R4E's central finding is binding: local C/G/S/P/R patches cannot integrate an alphabet whose inherited straight/diagonal forms were not designed from one architecture.
- **Color:** Stage 2 PASS; no color mechanism is allowed to repair character identity.
- **Layout/Interaction:** Stage 2 PASS. Literal operational strings and layout geometry remain stable stress inputs; layout widening is not a Type repair.
- **Web:** Stage 2 PRACTICE through W018. Browser font transfer is intentionally deferred until a drawing-valid candidate exists.
- **Content:** Stage 1 PASS / Stage 2 PRACTICE through CD016. Literal airport codes, registrations, flight identifiers, durations and ambiguity strings remain unchanged; semantic deletion is not permitted to rescue geometry.

## Architecture contracts defined before drawing

### A — restrained humanist / technical proportional

Intent: a restrained proportional family whose operational character comes from controlled apertures, modest stroke contrast by construction class, and differentiated widths rather than monospacing.

Contract:
- stem 76;
- round stem 82;
- cap overshoot 12;
- x-height overshoot 10;
- aperture token 132;
- join token 16;
- proportional capital width map;
- figure width 548;
- plain zero at this stage;
- kerning OFF.

### B — engineered operational semi-mono

Intent: stronger repeated rhythm and more explicit ambiguity management without requiring every glyph to occupy one rigid cell.

Contract:
- stem 84;
- round stem 88;
- cap overshoot 10;
- x-height overshoot 8;
- aperture token 160;
- join token 22;
- nominal 600-unit capital rhythm with optical exceptions for I/J/M/T;
- figure width 570;
- slashed zero;
- kerning OFF.

The alternatives therefore differ in proportion strategy, weight, aperture, joining, figure rhythm and zero mechanism. They are not merely two parameter values of the same nominal visual direction.

## Construction-class map

Before further drawing, the bounded repertoire is classified as:

1. straight orthogonal: E F H I L T;
2. diagonal: A K M N V X;
3. closed round/bowl: B D O P R 0 8 o;
4. open round/aperture: C G;
5. compound spine: S 5;
6. curved-bottom: U J;
7. lowercase arch/control: n l o;
8. coordinated figures: 0–9;
9. punctuation: hyphen, colon, comma.

This is a stronger architecture boundary than R4E's glyph-specific patch list.

## Executable artifact

`T021-family-architecture-reset-harness.py` builds both A and B over the same operational corpus, keeps kerning OFF, verifies cmap coverage, and emits deterministic 14/17/24 px specimens.

The harness explicitly preserves the existing ambiguity, airport, identifier, numeric and spacing corpus. It marks general spacing as blocked pending drawing critique and makes no human claim.

## Adversarial implementation review

The reset exposed an important methodological defect before any drawing PASS can be claimed.

Although A and B now have architecture-level contracts, the first executable implementation still reuses the R4D construction for digits 2/3/4/6/7/9. That means the implementation is **not yet a clean architecture reset across the whole family**. The source contract is new, but a subset of figure geometry remains inherited.

This is exactly the kind of hidden inheritance the reset was intended to eliminate. Therefore it would be invalid to interpret a visually promising raster as proof that either A or B is a coherent complete architecture.

### Decision

- **KEEP:** pre-drawing construction-class map;
- **KEEP:** A vs B materially different proportion/weight/aperture/figure hypotheses;
- **KEEP:** same-corpus 14/17/24 deterministic comparison and kerning-OFF boundary;
- **REWORK:** complete figures 2/3/4/6/7/9 under each architecture instead of delegating to R4D;
- **REWORK:** make terminal/corner/diagonal compensation tokens operational in every applicable construction rather than merely declared metadata;
- **REJECT:** any claim that the current first reset implementation has already demonstrated coherent-family drawing validity;
- **REJECT:** opening spacing/T022 from this artifact.

## Why this is progress rather than another failed micro-iteration

R4D/R4E failures occurred after full-family raster inspection because local repair did not control inherited family logic. This reset moves the failure test earlier: architecture completeness is now audited at source/construction level before accepting raster appearance.

That changes the workflow to:

`architecture contract → construction-class completeness → executable full family → exact raster → drawing critique → general spacing → pair residual → kerning`

The new **construction-class completeness** gate is the principal result of this block.

## Next large block

1. eliminate all inherited R4D figure drawing from A and B;
2. make architecture tokens actually drive straight, diagonal, round, aperture, spine, lowercase and figure construction;
3. add an automated provenance/completeness assertion proving every bounded glyph is produced by the reset architecture rather than predecessor delegation;
4. execute both full 36/36 families at 14/17/24;
5. inspect A and B side by side and reject an architecture if local exceptions proliferate merely to create coherence;
6. compare only surviving drawing-valid architecture against current-product proportional Roboto;
7. begin general spacing only after that gate passes.

## Evidence boundary

No human recognition, readability, scan-speed, preference or error-rate evidence is claimed. No Flutter/native/browser/physical-device transfer is claimed. Human validation remains deferred to app-development validation.

## HANDOFFS TO OTHER SPECIALISTS

- **Web:** no custom-font browser transfer yet; wait for construction-complete drawing candidate.
- **Layout/Interaction:** preserve the same operational strings and layout substrate for later transfer.
- **Content:** literal identifiers remain invariant across A/B.
- **Color:** ambiguity must remain structurally legible without hue.
