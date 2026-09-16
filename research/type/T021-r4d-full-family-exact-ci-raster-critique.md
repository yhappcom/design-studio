# T021 — R4D Full-Family Exact CI / Raster Critique

Status: **EXACT CI EXECUTED / 36-OF-36 COVERAGE PASS / 14-17-24PX ARTIFACTS RETAINED / DRAWING GATE FAIL**  
Date: 2026-09-16  
Owner: Typography / Type Design Specialist

## Purpose

Promote the bounded R4C shared grammar into the full T021 operational repertoire and test the exact artifact rather than continuing local grammar prototypes. This is **TRANSFER VALIDATION + CONTRADICTION REVIEW** of the R4C judgment that the bounded grammar was credible enough for full promotion.

## RELATED DOMAIN CHECK

- **Type:** R3 remains the prior exact full candidate; R4A was rejected; R4B defined shared constraints; R4C survived bounded intended-size critique sufficiently for promotion.
- **Color:** not materially causal; character identity remains monochrome.
- **Layout/Interaction:** operational strings and density are held fixed; layout is not widened to hide glyph defects.
- **Web:** browser transfer remains downstream of a stable exact drawing candidate.
- **Content:** literal airports, identifiers, times and ambiguity strings are preserved; wording is not changed around Type defects.

## Executed proof

Canonical harness: `T021-r4d-full-family-promotion-harness.py`.  
Exact GitHub Actions workflow: `Type T021 R4D Proof`, run `35044374385`.

Environment recorded by CI:
- Ubuntu 24.04.5 runner;
- Python 3.13.15;
- fontTools 4.65.0;
- Pillow 12.3.0;
- kerning OFF.

The workflow built `T021-LogMate-R4D.ttf`, generated deterministic specimens at 14/17/24 px, emitted JSON measurements and retained all five files as artifact `t021-r4d-full-family-proof`.

Machine result:
- required unique non-space operational characters: **36**;
- covered: **36**;
- missing: **0**;
- intended sizes generated: **14, 17, 24 px**.

This establishes exact build/coverage/raster reproducibility. It does not establish drawing quality.

## Exact artifact inspection

The retained 17 px CI specimen was downloaded and inspected directly after the workflow succeeded.

### KEEP

- Full bounded operational strings now render from one exact R4 artifact with no fallback/notdef in the tested corpus.
- R4C's B/8 topology correction survives full promotion: B retains a stem-side construction while 8 remains stemless.
- Figure advances remain coordinated; repeated numeric strings preserve regular horizontal accumulation.
- The family is no longer blocked by repertoire breadth or inability to produce exact intended-size artifacts.

### REWORK / FAIL

The full specimen exposes drawing defects that were not sufficiently visible in the bounded R4C grammar test:

1. **C/G aperture construction is too mechanically open and angular at 17 px.** In operational strings such as `ICN`, `CDG` and `G-EUOH`, the open-round vocabulary does not yet integrate naturally with the straighter uppercase system.
2. **S remains structurally awkward at small size.** The opposing shoulder construction creates an artificial segmented/spine impression rather than a controlled continuous S rhythm. S/5 distinction exists, but distinction alone is not a quality gate.
3. **Round-to-straight family rhythm remains uneven.** O/0/o are visibly rounded while several inherited R3 straight glyphs retain coarse rectangular construction. Full promotion therefore reveals a family-level grammar discontinuity that a failure-cluster-only prototype could not prove away.
4. **P/R and some bowl joins remain utilitarian.** Their exact raster is operationally renderable but not yet credible as a coherent authored family.
5. **The slashed zero remains unresolved.** It creates explicit O/0 separation, but exact product-context suitability has not been established and must not be treated as final merely because it survives rasterization.

Therefore the exact R4D artifact **fails coherent-family drawing validity**. General spacing must not begin yet; kerning must not be used to mask these defects.

## Contradiction result

R4C's bounded conclusion was correctly narrow: the grammar was *promotable*, not passed. R4D confirms the value of that distinction. The full-family transfer reveals discontinuities that were impossible to judge from the limited R4C cluster alone.

The contradiction is not `R4C was wrong`; it is:

> **A grammar that survives bounded cluster critique can still fail after transfer into inherited full-family forms. Full-family context is a separate gate.**

## Revised next method

Do not return to isolated glyph patching and do not start spacing. The next drawing block should be an **R4E integration pass**:

1. classify all 36 operational glyphs by construction grammar, including the inherited straight/diagonal forms rather than only the R4 failure cluster;
2. define shared terminal, corner, join and stroke-ending rules for straight/diagonal glyphs so they relate to the round/bowl/aperture system;
3. redraw C/G/S and P/R under that integrated grammar;
4. retain B/8 structural separation and coordinated figures;
5. test slashed-zero and non-slashed-zero alternatives as a product decision without changing other geometry;
6. rebuild the complete 36/36 artifact with kerning OFF;
7. reraster the same airports/identifiers/numeric/ambiguity/spacing corpus at 14/17/24;
8. only if the full specimen survives drawing critique may general sidebearing analysis open.

## Gate consequence

- exact R4D full generator/build: **PASS**;
- bounded operational coverage: **36/36 PASS**;
- exact retained 14/17/24 raster production: **PASS**;
- coherent-family drawing: **FAIL**;
- general spacing: **BLOCKED**;
- pair residual analysis: **BLOCKED**;
- T022 kerning: **BLOCKED**.

## HANDOFFS TO OTHER SPECIALISTS

- **Layout/Interaction:** do not change product density/column geometry to compensate for current Type defects.
- **Web:** exact browser-font transfer should still wait; R4D is reproducible but drawing-invalid.
- **Content:** preserve literal operational identifiers and numeric strings.
- **Color:** no character distinction should depend on hue.

## Evidence boundary

This is exact GitHub CI + FreeType/Pillow raster + designer critique. It is not Flutter/native/browser rendering evidence and not human recognition, scan-speed, readability or preference evidence. Human validation remains deferred to app-development validation.
