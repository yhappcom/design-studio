# T021 — Coherent Mini-Family + Spacing Comparison Practice

Status: **STAGE 2 PRACTICE + CRITIQUE — three bounded hypotheses compared; B selected as working direction for T022; custom-outline/raster proof remains OPEN**

Owner: Typography / Type Design Specialist  
Canonical path: `research/type/`

Companion evidence:
- `T021-mini-family-comparison-metrics.json`
- `T021-mini-family-comparison-specimen.svg`

## Purpose

T020 identified the largest Stage 2 gap as integrated family/system practice rather than another isolated production mechanism. T021 begins that chain with a bounded Latin control family and three materially different spacing/construction hypotheses.

This is deliberately **pre-kerning**. The purpose is to force global sidebearing and family decisions before pair-specific repair.

---

## RELATED DOMAIN CHECK

### Typography / Type

Evidence checked:
- `002-metrics-spacing-optical-rhythm.md`;
- Stage 1 H/O construction/spacing exercises;
- T002 intended-size failure/redraw logic;
- T006 source/metric audit;
- T020 Stage 2 entry audit.

Reusable finding:
- H/O and n/o are useful straight/round controls;
- sidebearings and contours must be judged as coupled systems;
- repeated strings expose rhythm defects better than isolated pairs;
- spacing should be pushed as far as possible before kerning;
- intended-size proof is a separate evidence layer.

### Color

Evidence checked:
- `progress/COLOR_STATUS.md` through C015.

Reuse decision:
- hold Color constant during spacing comparison. Chroma must not become an accidental preference variable while Type geometry is being compared.

### Layout / Interaction

Evidence checked:
- `research/layout/L003-type-fallback-density-reflow-transfer.md`;
- current Layout status.

Reusable finding:
- width differences become product geometry differences near wrapping thresholds. Therefore the widest hypothesis is not automatically more readable, and the narrowest is not automatically more efficient.

### Web Design

Evidence checked:
- current Web status through W011;
- T016 browser font-loading transfer remains the Type-owned loading baseline.

Reuse decision:
- actual browser delivery is not part of this first family-design exercise. Final selected artifacts must later be transferred to browser/runtime conditions.

### Overlap decision

**PRACTICE + COMPARATIVE STUDY.** This intentionally reuses Foundation spacing principles because Stage 2 requires multiple solutions and defended selection, not another source summary.

---

## SOURCE

OpenType separates visible outline geometry from horizontal layout metrics. `hmtx` supplies advance widths and left sidebearings; right sidebearing follows from advance, left sidebearing and glyph bounds. A metric value therefore has meaning only relative to UPM and contour geometry.

Canonical source already recorded in Study 002:
- Microsoft OpenType `head`: https://learn.microsoft.com/en-us/typography/opentype/spec/head
- Microsoft OpenType `hmtx`: https://learn.microsoft.com/en-us/typography/opentype/spec/hmtx

Study 002 also records the Glyphs spacing workflow: establish H/O and n/o controls, inspect repeated strings, judge at intended size, and solve general spacing before kerning.

---

## Exercise contract

Common coordinate system:
- UPM: 1000;
- baseline: 0;
- x-height: 500;
- cap height: 700;
- round overshoot target: 12;
- kerning: OFF.

Initial control family:
- repeated-form controls: `H O n o`;
- stress forms prepared for the next pass: `A V T`;
- later T021/T022 extension target: `L I`, numerals, punctuation and one accented construction path.

Control strings:
- `HHOO HHOH OOHO HOHOHO`;
- `nn oo nono noon onno`;
- `HOnonO HnOoH`;
- `AVAVA TOTO LALO`;
- `00112233445566778899`;
- `010101 808080 111888`;
- `1+05 12+40 999+59`.

The last three strings are retained as future data-centric transfer controls; they do not replace H/O/n/o spacing proof.

---

# Hypothesis A — Compact geometric

Intent:
- minimize horizontal footprint;
- keep straight/round bearings close;
- use a comparatively strong 90u stem.

Representative metrics:
- H: 600 advance, 55/55 bearings;
- O: 610, 45/45;
- n: 520, 48/42;
- o: 530, 42/42.

Calculated unkerned control widths:
- `HHOO`: 2420u;
- `HOHOHO`: 3630u;
- `nono`: 2100u;
- `HOnonO`: 3390u.

### Critique

**Strength:** lowest space cost of the three hypotheses.

**Risk:** compactness plus the heaviest stem leaves the least white-space reserve. It is the direction most likely to tempt later pair-specific negative kerning to recover openness around diagonals/rounds.

**Verdict: REWORK.** Keep as the compact boundary/control, not the working family direction.

---

# Hypothesis B — Balanced text

Intent:
- moderate width;
- explicitly differentiate straight and round spacing;
- preserve enough white space for text rhythm without maximizing footprint.

Representative metrics:
- H: 620, 65/65;
- O: 620, 55/55;
- n: 540, 58/52;
- o: 540, 50/50;
- stem: 85u.

Calculated unkerned control widths:
- `HHOO`: 2480u;
- `HOHOHO`: 3720u;
- `nono`: 2160u;
- `HOnonO`: 3480u.

### Critique

**Strength:** preserves a clear straight-vs-round bearing model while avoiding both A's compressed reserve and C's large width cost. H/O and n/o also share equal advances inside each case, simplifying early repeated-form comparison without forcing every future glyph into equal width.

**Risk:** equal H/O and n/o advances can become a false symmetry if later contours prove to need different cells. These values are hypotheses, not rules.

**Verdict: KEEP AS WORKING DIRECTION.** Advance B into T022, subject to custom-outline/control-string proof.

---

# Hypothesis C — Open screen

Intent:
- maximize counters/white-space reserve;
- use lighter 82u stems and more generous bearings;
- treat small-screen robustness as the priority hypothesis.

Representative metrics:
- H: 650, 75/75;
- O: 650, 65/65;
- n: 565, 68/62;
- o: 570, 60/60.

Calculated unkerned control widths:
- `HHOO`: 2600u;
- `HOHOHO`: 3900u;
- `nono`: 2270u;
- `HOnonO`: 3650u.

### Critique

**Strength:** greatest white-space reserve and lowest nominal stem mass.

**Risk:** width cost is substantial: `HHOO` is ~4.8% wider than B and ~7.4% wider than A; `HOnonO` is ~4.9% wider than B. L003 shows that modest Type-width differences can cross real layout thresholds, so openness cannot be selected without product geometry consequences.

**Verdict: REJECT AS DEFAULT / RETAIN AS STRESS CONTROL.** C remains useful for small-size experiments but is not the default working direction.

---

## Comparative decision matrix

| Criterion | A compact | B balanced | C open |
| --- | --- | --- | --- |
| horizontal economy | strongest | moderate | weakest |
| white-space reserve | weakest | moderate | strongest |
| straight/round spacing differentiation | limited | explicit | explicit/generous |
| likely exception pressure | higher risk | lowest current risk | moderate, mostly width-driven |
| dense-product geometry risk | lowest width | controlled | highest width |
| small-size openness hypothesis | weakest | balanced | strongest |
| current decision | REWORK | **KEEP** | REJECT default / keep stress control |

### SYNTHESIS

The useful comparison is not `tight vs loose` in isolation. It is:

`black-form mass + sidebearing ownership + sequence rhythm + exception cost + product width consequence`.

A spacing system that looks orderly numerically can still fail once contours are drawn; a visually open system can still be the wrong product choice if its width repeatedly crosses layout thresholds.

### STUDIO JUDGMENT

**B is the correct working direction for the next exercise, not a finished design.**

Why:
- it keeps explicit straight/round spacing logic;
- it preserves more correction reserve than A;
- it avoids C's ~5% control-string width premium over B;
- it provides a neutral middle hypothesis from which later kerning and small-size evidence can move in either direction;
- it minimizes premature optimization for either density or openness.

What B sacrifices:
- it is not as compact as A;
- it is not as open as C;
- equal advances in the initial controls may need to be broken after real outline proof.

---

## Failure discovered in the comparison artifact

The companion SVG intentionally does **not** pretend to be a custom-font raster proof. Its visible sample text uses the viewer's sans font while labels expose the three declared metric strategies.

This creates a useful evidence boundary:

`declared metrics + comparison sheet != custom glyph family != target-size raster proof`.

A prior Stage 2 mistake would be to call a metric table a coherent family. T021 does not do that.

---

## OPEN

T021 is **not complete enough to close the Stage 2 family requirement**.

Still required before this exercise can be considered strong family evidence:
1. actual custom H/O/n/o outlines for A/B/C or at minimum B plus adversarial A/C controls;
2. real control-string rendering from those outlines at 14/17/24px;
3. classification of observed defects as drawing vs spacing vs true kerning;
4. A/V/T/L/I extension with no kerning first;
5. numeral/punctuation extension;
6. accented construction path;
7. proof that B remains preferable after actual rendering.

No browser, native-platform, human-reading or production-font PASS is claimed.

---

## HANDOFFS TO OTHER SPECIALISTS

### Color
- Hold Color constant during Type spacing comparisons; do not let chroma become a preference confound.
- Later role-system transfer should restore real Color hierarchy.

### Layout / Interaction
- C is roughly 5% wider than B on representative control strings. L003 already shows that differences of this kind can matter near wrap thresholds.
- Treat the final Type artifact as an input to layout stress testing rather than forcing Type to one width solely to preserve fixed cells.

### Web Design
- The SVG is not browser font validation. When actual font binaries exist, test exact artifacts under loading/fallback/zoom/localization conditions.
- T016 remains the relevant loading-state baseline.

---

## Checkpoint

- Three materially different Stage 2 hypotheses: **ESTABLISHED**.
- Explicit KEEP/REWORK/REJECT critique: **ESTABLISHED**.
- Working direction: **B — Balanced text**.
- Coherent custom-outline family proof: **OPEN**.
- Actual intended-size raster proof: **OPEN**.
- Stage 2: **NOT PASSED**.
- Next action: continue T021 with real outlines/control-string rendering before opening T022 if the environment permits; otherwise T022 must not treat B as visually proven.
