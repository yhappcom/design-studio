# T021 — R2 Exact Raster Critique

Status: **EXECUTED / DRAWING VALIDITY FAIL / T021 REMAINS OPEN**  
Date: 2026-09-16  
Owner: Typography / Type Design Specialist

## Evidence provenance

Canonical GitHub Actions run `35041942223` (`Type T021 Proof`, run #4) completed `success` on commit `eeb618682ba56b8bb762669f1fb401806e3eecef`.

The job executed, in order:
1. the exact repository R2 family generator;
2. the deterministic raster proof;
3. measured-result display;
4. artifact upload.

Artifact `10425870809`, digest `sha256:43304420f417126c883309248f04bd63b66af9b1e1920d2788ebe2e94658c765`, contains:
- `T021-LogMate-Balanced-Expanded-R2.ttf`;
- `T021-logmate-operational-family-expansion-R2-results.json`;
- `T021-R2-specimen-14px.png`;
- `T021-R2-specimen-17px.png`;
- `T021-R2-specimen-24px.png`.

The specialist downloaded and visually inspected the exact 17px and 24px specimen PNGs. This is designer inspection, not human-recognition testing.

## SOURCE

The R2 generator intentionally uses highly simplified polygonal/stroke primitives. It does not claim curve-finished production outlines. Kerning is OFF.

## Direct raster findings

### 1. Family texture is too rectangular and mechanically modular

At both 17px and 24px, many capitals and figures read as squared construction modules rather than a coherent text family. O/0, bowls and multiple figures have near-rectangular counters. This makes the candidate visually closer to a construction/debug alphabet than a credible LogMate identity direction.

**Classification: DRAWING.** Do not attempt to solve this with sidebearings or kerning.

### 2. Round-family logic is not yet optically round

`O`, `0`, and bowl-derived forms raster as box-like rings. C/G are structurally open now, which fixes the earlier invalid pseudo-erasure method, but their terminal/curve vocabulary remains mechanically rectangular. The structural repair is real; optical form quality is not yet sufficient.

**Classification: DRAWING.**

### 3. Figure system exposes severe recognition-shape weaknesses

The equal-advance property is geometrically useful, but the raster shows that figure construction is not mature enough to evaluate figure-style selection. `1` has a narrow/stem-heavy form and unusual top/base behavior; `8` is two rectangular rings; several figures rely on seven-segment-like modules. In operational strings such as `BA117`, `HL8301`, `N12345`, times and totals, this produces a machine-display texture inconsistent with the current proportional Roboto product baseline unless such a display identity were explicitly intended and validated.

**Classification: DRAWING first. Figure-style comparison is premature.**

### 4. Ambiguity corpus is present but not yet a recognition proof

`0O`, `1Il`, `5S`, `8B` all render without fallback. Their mere visual difference in designer inspection cannot establish recognition accuracy. In particular, the candidate currently achieves some differentiation by construction extremity rather than by a mature shared family grammar.

**Classification: DRAWING / HUMAN VALIDATION DEFERRED.**

### 5. Lowercase controls remain disconnected from the capital system

`nono` and `noon` render, but the lowercase n/o system is sparse and does not yet provide enough evidence for a coherent text-family relationship. The lowercase is useful as a spacing control, not as evidence that the family is complete.

**Classification: DRAWING / FAMILY COHERENCE.**

### 6. Spacing evidence must not be over-read

The raster contains `HHOO`, `HOHOHO`, `AVAVA`, `TOTO`, `LITIL` and operational strings, but drawing defects dominate perceived rhythm. Adjusting sidebearings now would risk compensating for contour defects. Therefore general-spacing revision remains deliberately blocked.

**Classification: DRAWING before GENERAL SPACING.**

## What did improve from R1

KEEP:
- exact-source CI reproducibility;
- explicit construction dispatch;
- no silent generic uppercase placeholder;
- 36/36 bounded corpus coverage;
- deterministic 14/17/24 raster evidence;
- C/G are genuinely open rather than pseudo-erased;
- operational corpus is now inspectable from one exact binary;
- equal-advance figure behavior is measurable.

REWORK:
- round/bowl contour vocabulary;
- S and figure curvature/terminal logic;
- `1`, `8`, and other seven-segment-like figure constructions;
- lowercase n/o relationship;
- optical joins and terminal treatment;
- family-wide balance between straight, diagonal and round glyphs.

REJECT:
- promoting R2 as a product identity candidate;
- starting kerning merely because coverage/build/raster generation pass;
- interpreting 36/36 coverage as family coherence;
- using generic mono as a substitute for a product control.

## Current LogMate product-control audit

A fresh recursive-tree audit of current `yhappcom/logmate` `main` found only these font binaries under `assets/fonts/`:
- `NotoSansKR-wght.ttf`;
- `Roboto-Medium.ttf`;
- `Roboto-Regular.ttf`.

Current `pubspec.yaml` declares `LogMateNotoSansKR` and `LogMateRoboto`; it does not declare `LogMateRobotoMono`. Therefore the latest-main product baseline is proportional Roboto plus Noto Sans KR fallback, not a bundled Roboto Mono control. Any historical mono experiment remains historical unless deliberately restored.

## T021 gate decision

T021 **does not close**.

The gate now fails for a stronger reason than before: not because raster evidence is missing, but because the exact canonical raster has been produced and inspected and the drawing system is visibly insufficient for coherent-family practice.

Next work should not add more glyph breadth. The bounded repertoire is enough. The next iteration must improve **quality within the existing repertoire**:

`round/bowl redraw → figure redraw → n/o coherence → rerender 14/17/24 → drawing gate → only then sidebearings → residual pairs`.

## Human-validation boundary

No claim is made about pilot recognition speed, error rate, preference, fatigue, or operational safety. Those require later human/product validation.

## RELATED DOMAIN CHECK

- Layout/Interaction: keep column geometry reversible; R2 should not set product widths.
- Web: exact binary/raster reproducibility is useful, but browser evidence is still separate.
- Content Design: corpus tokens remain literal and unchanged.
- Color: held constant.

## Verdict

**R2 succeeds as a reproducible falsification instrument and fails as a coherent family direction. This is useful Stage 2 evidence: the team can now distinguish structural completeness from optical type-design quality using the exact same artifact.**
