# T021 — Pair-Gap Method Validation Against Mature Font Controls

Status: **EXECUTED — CONTRADICTION REVIEW + INDEPENDENT VALIDATION + METHOD COMPARISON**  
Scope: kerning-off same-y scanline geometry used by T021; mature production-font controls; LogMate live-project consequence.  
Companion artifacts:
- `T021-pair-gap-method-validation.py`
- `T021-pair-gap-method-validation-results.json`

## Question

T021's prior pair-gap diagnostic correctly showed that whole-string advance equality was too coarse, but it then made a stronger inference:

> B's `AV` same-y gap of roughly `270–300u / 1000 UPM` is large enough to treat the primitive A/V construction or base spacing as defective, so kerning should remain blocked until those primitives are redrawn.

Before spending more live-project time redrawing LogMate-facing glyphs, this study asks whether that **absolute gap magnitude** is actually unusual relative to mature production fonts measured with the same conceptual geometry.

The objective is not to approve T021 B. It is to validate the diagnostic method so the studio does not turn one uncalibrated measurement into an experimental redesign loop.

---

## RELATED DOMAIN CHECK

### Type

Checked:
- `T021-pair-gap-geometry-diagnostics.md`;
- `T021-shape-sensitive-prekerning-spacing-revision.md`;
- current `progress/TYPE_STATUS.md`;
- `LOGMATE_TYPE_IDENTITY_LIVE_PROJECT_DIRECTIVE.md`;
- T017–T020 LogMate transfer chain.

Reusable evidence:
- spacing must precede kerning;
- whole-string advances cannot diagnose shape-specific pair geometry;
- target-size raster evidence and product role evidence are separate from analytic geometry;
- T017–T020 remain valid as conservative implementation controls, but do not resolve LogMate identity.

Reason for repetition: **CONTRADICTION REVIEW + INDEPENDENT VALIDATION + METHOD COMPARISON**. The previous pair-gap study introduced an implicit quality threshold without a mature-font reference distribution. This study tests the threshold itself.

### Color

Checked current Color status: Stage 2 PASS. Color is held constant and does not determine glyph construction or sidebearing quality in this geometry-only experiment.

No Color conclusion is claimed.

### Layout / Interaction

Checked current Layout/Interaction status and the existing L003/L004 transfer logic.

Reusable finding:
- Type metrics are spatial inputs, but Layout does not define what an acceptable glyph-sidebearing or scanline-gap value is;
- exact product columns should not be frozen around an unstable Type experiment.

This study therefore qualifies a Type diagnostic; it does not redefine LogMate column geometry.

### Web Design

Checked current Web status through W016. Browser transfer remains necessary after a stable font artifact exists, but Chromium/control behavior cannot establish whether a primitive Type drawing is intrinsically correct.

This experiment is local outline geometry, not browser/runtime proof.

### LogMate live project

Checked latest `yhappcom/logmate` `design/design-studio-proposal` work.

The UI team now uses a **specific, bundled `LogMateRobotoMono` airport-only interim control**, not an uncontrolled platform-generic monospace. The runtime contract explicitly labels it `INTERIM_CONTROL_NOT_FINAL_TYPE_CONTRACT`; Flutter widget tests assert equal rendered width for `ICN / NRT / SIN`, and CI validates the exact added font artifact.

That control is therefore suitable as a temporary product baseline while Type research proceeds. It must not be promoted to final identity merely because it removes width drift.

---

## Method

Five mature local control fonts were selected to span proportional UI sans and mono behavior:

- Inter Regular 4.001;
- Noto Sans Regular 2.004;
- Lato Regular 2.015;
- DejaVu Sans 2.37;
- Liberation Mono Regular 2.1.5.

For each font:

1. read exact outlines and metrics with FontTools;
2. flatten quadratic/cubic curves at high subdivision (`64` samples per curve);
3. sample the same conceptual cap-height fractions used by T021 (`0`, `85/700`, `350/700`, `615/700`, `1.0` of cap height);
4. with kerning OFF, compute:

`gap(X,Y,y) = advance(X) + leftBoundary(Y,y) - rightBoundary(X,y)`;

5. normalize the result to `1000 UPM`.

Pairs:

`AV VA TA AT LI IL`

This is an outline-geometry approximation. It is deliberately independent of raster antialiasing and default shaping/kerning. It is still not a perceptual score.

The companion JSON records font version, SHA-256, UPM, cap height, scanline values and normalized pair-gap ranges.

---

## Result A — T021 B's AV magnitude is not anomalous by itself

Prior T021 B `AV` values:

`300.0 / 296.4 / 285.0 / 273.6 / 270.0`

Normalized mature-control ranges:

| Control | `AV` gap / 1000 UPM |
| --- | ---: |
| Inter | `318.4` |
| Noto Sans | `256.0–277.8` |
| Lato | `292.5–298.0` |
| DejaVu Sans | `293.9–294.4` |
| Liberation Mono | `250.0–252.0` |
| **T021 B** | **`270.0–300.0`** |

### CONTRADICTION

The prior inference that `270–300u / 1000 UPM` is, by its magnitude alone, evidence of a primitive A/V construction/base-spacing defect is **not supported**.

T021 B overlaps the same scale found in multiple mature proportional fonts. Inter is wider by this diagnostic; Noto Sans and Liberation Mono are narrower; Lato and DejaVu occupy nearly the same range.

This does **not** prove that B's A/V drawings are good. It proves only that the absolute same-y gap value is not a calibrated defect threshold.

---

## Result B — LI/IL directional asymmetry is also not a standalone defect signal

Prior T021 treated the strong `LI` vs `IL` height/order difference as additional evidence that primitive geometry remained suspect.

Mature controls also show large directional differences:

| Control | `LI` range | `IL` range |
| --- | ---: | ---: |
| Inter | `135.7–472.7` | `175.8` |
| Noto Sans | `65.0–461.0` | `138.0–222.0` |
| Lato | `107.0–417.0` | `183.0` |
| DejaVu Sans | `103.5–458.5` | `196.3` |
| Liberation Mono | `161.6–644.0` | `215.3–369.6` |

The asymmetry is explainable in part by the very different ink occupancy of `L` and `I` at different scanlines. Therefore the direction/height asymmetry remains diagnostically descriptive, but not automatically defective.

### SYNTHESIS

`pair-gap geometry = useful descriptive signal != universal optical-quality score`.

---

## Result C — TA/AT confirm why one scalar threshold is structurally weak

The mature `TA/AT` controls span very different gaps by height because `T`'s top bar and `A`'s diagonal geometry occupy different horizontal regions.

For example:
- Noto Sans `TA`: about `233–477 / 1000`;
- Lato `TA`: about `250–501 / 1000`;
- DejaVu Sans `TA`: about `264–508 / 1000`;
- Inter `TA`: about `301–533 / 1000`.

A single same-y gap target would therefore penalize legitimate shape geometry and encourage Type to “normalize” silhouettes that should remain different.

### STUDIO JUDGMENT

Do not optimize T021 toward a target scanline number.

Use pair-gap diagnostics to locate where space originates, then judge the result together with:
- intended-size raster proof;
- control strings;
- repeated operational strings;
- advance/compactness needs;
- actual residual pair problems after base spacing is credible;
- comparison against mature controls.

---

## Correction to the current T021 decision

### KEEP
- per-glyph metrics instead of the falsified shared-cap model;
- kerning OFF while base family coverage is still incomplete;
- pair/scanline diagnostics as a **descriptive** tool;
- A/B/C alternatives as research hypotheses;
- target-size raster proof;
- explicit separation of geometry from human-performance evidence.

### REWORK
- the **interpretation** of pair-gap magnitude;
- the next-step rationale: do not redraw A/V/T/L/I simply to force smaller scanline gaps;
- LogMate transfer should now prioritize actual operational glyph breadth and control comparison rather than an uncalibrated gap target.

### REJECT
- `270–300u AV gap => drawing defect` as a general rule;
- using mature-font scanline values as a new universal target;
- deriving kerning values directly from same-y scanline gaps;
- declaring T021 B selected or production-ready from this contradiction review.

---

## LogMate consequence

This method correction materially reduces the risk of an unnecessary bespoke-Type detour.

The current safe product state is:

1. **general UI:** exact controlled Roboto remains the implementation baseline;
2. **airport codes:** exact bundled Roboto Mono role may remain as the explicit interim control because the UI has now verified equal-width behavior in Flutter;
3. **time/duration:** continue comparison-oriented tabular numerics;
4. **do not spread mono automatically** to aircraft type, registration, flight number, names or prose;
5. **do not call the interim mono final identity**;
6. custom/LogMate-specific Type research must beat both the Roboto proportional control and airport-only Roboto Mono control on explicit product criteria before transfer.

### What T021 must do next

The current custom family is too narrow to answer the live-product question. It does not yet provide the full airport/identifier/numeral corpus needed for a direct LogMate comparison.

The next safe Type work is therefore:

1. broaden the T021 uppercase set toward the actual airport corpus (`ICN NRT SIN JFK LHR CDG HND DXB FRA LAX`), preserving family logic rather than drawing only convenient letters;
2. add the numerals and punctuation needed for operational controls;
3. rerender at actual LogMate target sizes;
4. compare advance consistency, compactness and ambiguity geometry against:
   - proportional Roboto control;
   - exact airport-only Roboto Mono interim control where the product harness provides evidence;
5. only then determine whether residual pair-specific problems justify T022 kerning work.

T022 remains **NOT OPEN** from this study alone. The reason is now **family breadth / operational evidence maturity**, not the absolute AV pair-gap magnitude.

---

## Evidence boundary

This study does not establish:
- that T021 B is optically balanced;
- a final LogMate custom family;
- a final airport-code treatment;
- human identifier-recognition performance;
- Flutter rendering of the experimental T021 font;
- Android/iOS/PWA parity;
- screen-reader or low-light task evidence.

Human/app-stage validation remains deferred and is not simulated.

---

## HANDOFFS TO OTHER SPECIALISTS

### Layout / Interaction

Do not freeze columns around current experimental T021 metrics, but the previous Type warning should also be narrowed: current A/V scanline magnitude is not independently proven defective. Preserve semantic geometry and keep the airport-only mono control replaceable.

### Web Design

No custom experimental font is ready for exact Web transfer yet. When T021 gains operational breadth, compare the chosen candidate with the same product corpus under browser loading/fallback and responsive constraints rather than reproducing an abstract A/V test alone.

### Color

No Color contradiction. Keep Color fixed during Type identity comparison so weight/ink/spacing differences are not confounded with salience changes.

---

## Current verdict

**NOT READY — KEEP INTERIM CONTROL**

Narrow blocker:

> No LogMate-specific candidate yet has enough operational glyph breadth and target-size product evidence to outperform or replace the exact airport-only Roboto Mono control while also improving product identity.

The next work is broader operational family proof, not blind A/V gap reduction.
