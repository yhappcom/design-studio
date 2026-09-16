# T021 — R4B/R4C Shared Family Grammar Raster Review

Status: **EXECUTED LOCALLY / R4A METHOD REPLACED / SHARED GRAMMAR PROMISING / FULL PROMOTION NOT YET CLAIMED**  
Date: 2026-09-16  
Owner: Typography / Type Design Specialist

## Purpose

R4A falsified the shortcut `more curves → coherent family`. This block therefore tested the revised method required by `TYPE_STATUS.md`: define a shared construction grammar first, transfer it across the dominant failure groups, raster at intended sizes, then repair contradictions before any full 36/36 promotion.

No repertoire breadth was added. Kerning remained OFF.

## SOURCE

Binding evidence before execution:
- R3 exact CI/raster remains the latest full candidate and fails drawing validity.
- R4A local prototype showed mechanical rectangle-to-curve substitution did not establish family coherence.
- Current LogMate main uses proportional Roboto + Noto Sans KR fallback; historical mono experiments are not current product control.

## R4B grammar hypothesis

The prototype used one deliberately restrained, industrial/screen-oriented grammar:

1. **Round control — O/o/0:** vertically biased rounded outer/inner contours, common stroke mass, explicit overshoot, smaller lowercase radius. Zero retained an internal slash as an ambiguity candidate rather than changing global width.
2. **Bowl control — D/B/P/R/8:** shared counter tension and rounded right-side transition rather than independent polygonal recipes.
3. **Aperture control — C/G/S/5:** open forms share terminal mass; S uses a continuous curved spine while 5 retains a flat top/open-upper construction, preserving structural separation.
4. **Shoulder control — n:** one curved shoulder with the same broad tension as the round/bowl system.
5. **U:** bottom join uses the round-system tension rather than a rectangular baseline bar.
6. **Figures:** 0/1/5/8 remain coordinated in advance and stroke mass, but ambiguity-critical internal structure is deliberately non-identical.

Stress strings were held fixed:
- `O o 0  O0 0O 000 OOO`
- `D B P R 8  DBPR8`
- `C G S 5  CGS5 S5 5S`
- `U n o  Uno nono noon`
- `S0B8 5O18`

The prototype was rastered deterministically with Pillow/FreeType at 14, 17 and 24 px.

## R4B critique

### KEEP

The shared round/aperture/shoulder policy materially reduced the R3/R4A impression of unrelated rectangular primitives. O/o/0, C/G/S/5 and U/n/o began to read as one intentionally constrained screen family rather than isolated glyph patches.

### REWORK found in the same block

R4B exposed a new contradiction: B was still too close to 8 because its two rounded lobes retained rounded left edges. P/R also inherited the same overly ring-like bowl construction. This was treated as a **DRAWING** defect, not a spacing or kerning defect.

## R4C repair

R4C kept the R4B round/aperture/shoulder grammar but changed the bowl group:

- B/P/R use a flat stem-side bowl with rounded right transition and explicit counter;
- B uses asymmetric upper/lower bowls rather than two symmetric rings;
- 8 remains stemless and uses two round counters with a pinched waist;
- D remains the broad single-bowl control.

The 17 px raster shows the intended structural consequence: `B` and `8` no longer collapse to the same left-edge topology, while P/R retain the same bowl tension without becoming 8-like.

Representative 17 px stress-line advances from the local R4C artifact:
- round/zero line: 159.3125 px;
- bowl line: 128.1875 px;
- aperture/S5 line: 149.7500 px;
- lowercase/U line: 157.0000 px;
- mixed ambiguity line `S0B8 5O18`: 82.8594 px.

These are geometry records only; they are not readability scores.

## STUDIO JUDGMENT

**R4C is the first R4 prototype in this sequence that is credible enough to promote its shared grammar into the full bounded generator for an exact CI test.** This is not a coherent-family PASS. The judgment is narrower: the primitive grammar survived intended-size designer inspection sufficiently to justify the cost of full transfer.

Remaining visible concerns before T021 closure:
- C/G terminals are intentionally blunt and need comparison in full operational strings;
- P/R bowl/leg joins remain utilitarian and may need optical refinement;
- S/5 distinction is structurally improved but requires full-corpus raster context;
- slashed zero remains only a candidate mechanism, not a final product decision;
- figure-style policy remains separate from drawing validity;
- base spacing has not yet been judged because the full candidate does not exist.

## Gate consequence

- R4A mechanical curve-substitution method: **REJECTED**.
- R4B shared-grammar hypothesis: **PARTIAL KEEP; bowl contradiction found**.
- R4C bowl repair: **KEEP FOR FULL-CANDIDATE TRANSFER**.
- drawing grammar prototype: **SUFFICIENT TO PROMOTE, NOT PASS**.
- full 36/36 R4 exact generator: **NEXT**.
- general spacing: **STILL BLOCKED until full-corpus R4 raster**.
- pair residual / T022 kerning: **BLOCKED**.

## RELATED DOMAIN CHECK

- **Layout/Interaction:** no layout width was loosened to accommodate drawing defects; literal operational strings remain the stress substrate.
- **Web:** no browser-transfer claim; this is local FreeType intended-size evidence.
- **Content:** identifiers/numerics are preserved literally.
- **Color:** all distinctions remain monochrome.

## HANDOFFS TO OTHER SPECIALISTS

- Layout should continue treating current product geometry as reversible until the promoted R4 full candidate is measured.
- Web should wait for exact full-candidate CI before transfer testing.
- Content should retain ambiguity-critical literal tokens rather than rewrite around them.
- Color should not be used to rescue character identity.

## Next executable block

Transfer the R4C shared grammar into the canonical full 36/36 T021 generator, preserve kerning OFF, run exact CI, retain 14/17/24 specimens, inspect the full operational corpus, repair drawing contradictions in the same block where possible, then begin general sidebearing analysis only if drawing validity survives.
