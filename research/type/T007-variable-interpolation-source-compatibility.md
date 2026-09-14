# T007 — Multi-master Interpolation Compatibility: Point Structure, Correspondence, and Silent Failure Modes

Status: **FOUNDATION / PRACTICE + CRITIQUE — two-master interpolation failure→revision→adversarial correspondence proof complete; broader variable-family/build/platform validation still OPEN**

Owner: Typography / Type Design Specialist  
Canonical path: `research/type/`  
Reproducible source: `research/type/T007-variable-interpolation-build-proof.py`  
Measured data: `research/type/T007-variable-interpolation-results.json`  
Evidence artifact: `research/type/T007-variable-interpolation-evidence.svg`

## Purpose

T006 established that a clean single-master source is not enough: editable source, generated binary and raster output are separate QA layers.

T007 asks the next production question:

> When two individually valid masters are combined into a variable family, what must remain compatible, what can fail silently, and what evidence is required before an intermediate instance can be trusted?

The experiment deliberately uses a tiny original `H O n o` family on one `wght` axis (`300 → 700`) so that point structure and interpolation behavior remain auditable.

This is a research family, not a product font.

---

## RELATED DOMAIN CHECK

### Typography / Type
- Evidence checked:
  - `research/type/003-stroke-contrast-bezier-optics.md`;
  - `research/type/T003-minimal-font-renderer-matrix.md`;
  - `research/type/T006-production-outline-audit.md`;
  - current `progress/TYPE_STATUS.md`.
- Reusable finding:
  - source topology, generated outline representation and raster behavior are distinct gates;
  - technically valid individual masters do not by themselves prove multi-master compatibility.
- Replication / challenge / transfer opportunity:
  - reproduce a real incompatible-master failure, then challenge the weaker rule “same point count = compatible”.
- Dependency / overlap:
  - broader family spacing, kerning, components, hinting, CFF2, STAT/avar, optical size and release QA remain outside this bounded study.

### Color
- Evidence checked:
  - current `progress/COLOR_STATUS.md`, now beyond C007;
  - C006/C007 transfer findings already consumed in T006.
- Reusable finding:
  - rendered glyph mass can affect practical foreground behavior while nominal color values remain unchanged.
- Replication / challenge / transfer opportunity:
  - later place weight-axis instances into fixed Color role/background conditions.
- Dependency / overlap:
  - **Not materially relevant to master-compatibility acceptance itself after checking.**

### Layout / Interaction
- Evidence checked:
  - current `progress/LAYOUT_STATUS.md`;
  - `research/layout/L004-tabular-numerals-dense-comparison-transfer.md`.
- Reusable finding:
  - Type changes can alter intrinsic width or rendered comparison geometry even when Layout policy is unchanged;
  - production Type changes therefore need regression tests at known Layout thresholds.
- Replication / challenge / transfer opportunity:
  - T007 explicitly varies `O` advance from `600 → 620`; later production regression should verify that interpolated metrics remain intentional near constrained columns/wrap thresholds.
- Dependency / overlap:
  - Layout owns the spatial policy; T007 owns font-source/interpolation correctness.

### Web Design
- Evidence checked:
  - `progress/WEB_STATUS.md`;
  - `research/web/README.md`.
- Reusable finding:
  - Web owns delivered webfont/browser/page validation.
- Implementation / application validation opportunity:
  - test the actual variable font in browser `font-variation-settings` / `font-weight`, zoom/DPR, fallback and real page constraints once W work exists.
- Dependency / overlap:
  - no substantive `W###` evidence exists at T007 start; no browser claim is inferred.

### Other / cross-cutting / future specialist
- Evidence checked:
  - OpenType Font Variations / `gvar` specification;
  - FontTools `varLib` implementation/documentation;
  - FontTools `cu2qu` / `Cu2QuMultiPen` documentation.
- Reusable finding:
  - TrueType variable glyph variation data are point-coordinate deltas;
  - FontTools can skip an incompatible glyph while still producing a variable font;
  - multi-font cubic→quadratic conversion exists specifically to preserve interpolation compatibility.
- Dependency / overlap:
  - commercial editor behavior and other build toolchains may report or repair incompatibilities differently.

### Overlap decision
- **PRACTICE + FAILURE ANALYSIS + ADVERSARIAL REVIEW + METHOD COMPARISON**.
- Why:
  - T006 proved single-master source/build discipline. T007 deliberately tests the next failure boundary and then attacks an overly weak compatibility heuristic.

---

## 1. SOURCE — variable TrueType outlines depend on point deltas

The OpenType `gvar` table stores glyph-variation data for TrueType outlines. Variation data adjusts X/Y coordinates for glyph points; point numbers therefore have structural meaning within interpolation.

Sources:
- https://learn.microsoft.com/en-us/typography/opentype/otspec/gvar
- https://learn.microsoft.com/en-us/windows/win32/directwrite/opentype-variable-fonts

### SYNTHESIS

A variable family cannot be approved by checking each master in isolation.

For corresponding masters, production compatibility must include at least:

- same intended contour structure;
- stable contour order;
- stable point ordering;
- meaningful start-point correspondence;
- compatible on/off-curve structure after conversion;
- compatible component structure where composites are used;
- intentional metric interpolation;
- acceptable intermediate geometry and raster behavior.

---

## 2. SOURCE — independent cubic→quadratic conversion can destroy compatibility

FontTools documents that `Cu2QuMultiPen` and multi-font `cu2qu` conversion convert corresponding curves together to keep the resulting quadratic splines interpolation-compatible. Converting one font at a time can be more economical, but does not provide the same compatibility guarantee.

Sources:
- https://fonttools.readthedocs.io/en/latest/pens/cu2quPen.html
- https://fonttools.readthedocs.io/en/latest/cu2qu/index.html

### STUDIO JUDGMENT

Optimization and family compatibility are different objectives.

A master-local conversion that minimizes points for one outline may create a different quadratic topology from another master. For a variable family, **shared compatibility takes precedence over local point-count economy**.

---

## 3. Controlled experiment

Environment recorded in the companion JSON:

- UPM: `1000`;
- FontTools: `4.63.0`;
- FreeType: `2.13.2`;
- cubic→quadratic tolerance: `2.0` font units;
- axis: `wght 300–700`, default `300`;
- instance checks: `300`, `500`, `700`;
- raster check: FreeType no-hint grayscale, `20 ppem`.

Three build conditions are compared.

### A — independent conversion

Each master converts its cubic outlines separately with `Cu2QuPen`.

### B — shared conversion

Corresponding master curves convert together through `Cu2QuMultiPen`.

### C — adversarial equal-count correspondence failure

The masters keep equal quadratic point counts, but the Bold `O` counter's start point is deliberately rotated by 180° before shared conversion. This preserves build-level point-count compatibility while corrupting semantic point correspondence.

---

## 4. Failure A — the variable font can build while one glyph silently stops varying

Under independent conversion, the master contour-point counts are:

| Glyph | wght 300 | wght 700 |
| --- | --- | --- |
| H | `[12]` | `[12]` |
| O | `[16, 16]` | `[16, 12]` |
| n | `[20]` | `[20]` |
| o | `[16, 12]` | `[16, 12]` |

Only `O` becomes structurally incompatible.

In the tested FontTools `4.63.0` `varLib` build, the tool logs:

`glyph O has incompatible masters; skipping`

but still produces a variable font.

Measured `gvar` tuple counts:

- `H`: 1
- `O`: **0**
- `n`: 1
- `o`: 1

The generated `O` therefore remains frozen at the default master:

| wght | advance | black area | 20ppem coverage |
| ---: | ---: | ---: | ---: |
| 300 | 600 | 104,025.67 | 41.17 |
| 500 | 600 | 104,025.67 | 41.17 |
| 700 | 600 | 104,025.67 | 41.17 |

### CONTRADICTION REVIEW

The weak acceptance rule:

> “The variable font built successfully, therefore the family is compatible.”

is false in this tested toolchain.

### STUDIO RULE

A successful binary build is not sufficient QA.

At minimum, inspect:

1. build warnings/errors;
2. expected `gvar` coverage per variable glyph;
3. endpoint and intermediate instances;
4. metric variation;
5. raster or application behavior.

---

## 5. Revision — shared conversion restores `O` interpolation

When corresponding cubic curves are converted together with `Cu2QuMultiPen`, both `O` masters become:

`[16, 16]`

and all four research glyphs receive variation data.

Measured `O` instances:

| wght | advance | black area | 20ppem coverage |
| ---: | ---: | ---: | ---: |
| 300 | 600 | 104,025.67 | 41.17 |
| 500 | 610 | 176,096.37 | 69.67 |
| 700 | 620 | 230,545.65 | 91.24 |

The `500` instance lies between the endpoint black areas, and advance interpolates `600 → 610 → 620`.

### TRANSFER VALIDATION

This validates the **method**, not the shape quality of the research `O`.

Joint conversion establishes compatible generated topology, but compatibility only means interpolation can proceed. It does not prove that the interpolation path is perceptually desirable.

---

## 6. Adversarial failure — equal point counts are necessary but not sufficient

The third condition deliberately rotates the Bold `O` counter's start point by 180°.

Both masters still report:

`[16, 16]`

and `varLib` creates one `gvar` tuple for `O` without an incompatibility warning.

Thus the simple checks:

- same contour count;
- same point count;
- variable build succeeds;
- `gvar` exists;

all pass.

Yet the intermediate is wrong.

Measured `O`:

| wght | advance | black area | 20ppem coverage |
| ---: | ---: | ---: | ---: |
| 300 | 600 | 104,025.67 | 41.17 |
| 500 | 610 | **274,626.45** | **108.74** |
| 700 | 620 | 230,545.65 | 91.24 |

At `wght 500`, the malformed midpoint exceeds the Bold endpoint by:

- black area: **+19.12%**;
- 20ppem coverage: **+19.18%**.

### FINDING

**Point-count compatibility is a necessary structural check, not a sufficient interpolation proof.**

Corresponding point indices must represent corresponding structural locations.

A family can be “compatible” to the build system while still producing unacceptable intermediate geometry.

---

## 7. Production compatibility contract

### STUDIO JUDGMENT

For a variable outline family, use the following layered contract.

### Layer 1 — source correspondence
- same semantic contour set;
- intentional contour order;
- intentional start points;
- corresponding extrema and structural landmarks;
- corresponding node roles;
- component structure compatible where applicable.

### Layer 2 — generated-outline compatibility
- same generated contour/point structure;
- no skipped glyphs;
- expected `gvar`/CFF2 variation coverage;
- no build warnings treated as harmless by default.

### Layer 3 — metric interpolation
- advances and sidebearings interpolate intentionally;
- phantom-point behavior is inspected;
- no unexpected width freeze or overshoot.

### Layer 4 — instance geometry
- inspect endpoints **and intermediates**;
- sample more than the named/default instances when curvature can be non-obvious;
- reject kinks, counter collapse, weight spikes, self-crossing, or non-monotonic appearance that is not intentional.

### Layer 5 — target rendering/use
- compact raster behavior;
- browser/platform/device transfer;
- Layout regression at constrained widths;
- Color/background transfer where relevant;
- human recognition/reading evidence for critical roles.

---

## 8. Project Readiness Test

### When should this knowledge be applied?
- any custom variable-font or multi-master family;
- static families generated from interpolated masters;
- cubic-source families converted to quadratic output;
- any build pipeline where masters can be independently normalized/optimized.

### When is it not enough?
- it does not select the correct number/location of masters;
- it does not decide the artistic weight curve;
- it does not prove kerning interpolation, component behavior, hinting, STAT/avar, CFF2 or production release quality;
- it does not replace browser/device/human validation.

### What project information is required?
- target outline format;
- static vs variable delivery;
- axis definitions and intended range;
- build toolchain;
- target browsers/platforms;
- text roles and minimum sizes;
- whether widths must remain stable for tables/data;
- required scripts/components/diacritics.

### What design decisions can it change?
- whether masters may be converted independently;
- contour/start-point editing policy;
- whether an apparent editor/build success is accepted;
- which intermediate instances enter QA;
- whether width/weight behavior needs Layout regression testing.

### Failure conditions
Reject or hold release when:
- a required glyph is skipped from variation;
- a glyph freezes unexpectedly on an axis;
- corresponding point semantics are unclear;
- an intermediate develops unintended mass/counter/curve behavior;
- metrics vary unexpectedly;
- build warnings are unexplained;
- actual target rendering contradicts source/editor inspection.

---

## OPEN

Still unresolved:

- three or more masters and non-linear design spaces;
- `avar` mapping and deliberately non-linear weight progression;
- multiple axes and corner-master compatibility;
- CFF2 variable outlines;
- components, anchors and diacritics;
- overlap strategy across masters;
- kerning/layout-feature interpolation;
- hinting strategy for variable TrueType;
- `STAT`, naming and release metadata;
- FontBakery/broader binary QA;
- browser/CoreText/DirectWrite/Skia/Flutter validation;
- production Layout/Color regression;
- human recognition/reading evidence.

---

## HANDOFFS TO OTHER SPECIALISTS

### Typography / Type
- Useful finding/context:
  - independent cubic→quadratic conversion can make one glyph incompatible even when both masters are individually valid;
  - equal point counts still do not prove semantic correspondence.
- Canonical section:
  - Sections 4–7.
- Confirmation / contradiction / transfer note:
  - extends T006 from single-master topology to variable-family correspondence;
  - contradicts “successful build” and “same point count” as sufficient QA heuristics.
- Scope limit:
  - small one-axis original research family only.

### Color
- Useful finding/context:
  - intermediate weight can produce unintended black-mass spikes even with unchanged color tokens.
- Canonical section:
  - Section 6.
- Confirmation / contradiction / transfer note:
  - future rendered Color tests must pin the exact font instance/build, not only family name and nominal weight.
- Scope limit:
  - no Color threshold or perceptual salience claim.

### Layout / Interaction
- Useful finding/context:
  - metric interpolation can freeze when glyph variation is skipped, or vary when compatibility is fixed.
- Canonical section:
  - Sections 4–5.
- Confirmation / contradiction / transfer note:
  - reinforces L003/L004's rule that actual Type output is a Layout input near wrap/column thresholds.
- Scope limit:
  - T007 does not choose any responsive/density policy.

### Web Design
- Useful finding/context:
  - a generated variable font can exist while one glyph is non-variable in the tested build;
  - browser QA must verify actual delivered variable instances and critical glyphs, not merely file load success.
- Web application / validation consequence:
  - sample endpoint and intermediate `font-weight`/variation values with production webfonts and real page strings.
- Confirmation / contradiction / transfer note:
  - future browser testing should explicitly catch frozen or malformed glyph interpolation.
- Scope limit:
  - no browser evidence exists in T007.

---

## Evidence level

**PRACTICE + CRITIQUE / reproducible two-master TrueType + varLib + gvar + FreeType evidence.**

T007 establishes a real source/build failure, a compatible-build revision, and an adversarial same-point-count failure. It does **not** establish production family PASS.
