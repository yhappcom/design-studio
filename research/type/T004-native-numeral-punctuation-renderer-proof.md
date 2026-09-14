# T004 — Native Numeral / Punctuation System + Renderer-Aware Metric Proof

Status: **FOUNDATION / PRACTICE + CRITIQUE — original 0–9/punctuation outlines and compiled-font evidence established; human/browser/device validation still OPEN**

Owner: Typography / Type Design Specialist  
Canonical path: `research/type/`  
Reproducible source: `research/type/T004-numeral-punctuation-research-font.py`  
Evidence artifact: `research/type/T004-numeral-punctuation-evidence.svg`

## Purpose

The Type program already established the conceptual rule that figures and punctuation are systems rather than isolated decorative glyphs, but the Foundation gate remained open because no complete native `0–9` system had been drawn and tested.

T004 asks:

> Can one coherent figure/punctuation construction survive proportional and tabular metrics, ambiguity stress, compact rasterization, and renderer-dependent spacing without prematurely choosing a product typeface style?

This is a **research font**, not LogMate/MintTap/Design Studio brand typography and not a production candidate.

---

## RELATED DOMAIN CHECK

### Typography / Type
- Evidence checked:
  - `research/type/005-numerals-punctuation-systems.md`
  - `type-design/exercises/003-numeral-punctuation-system-brief.md`
  - `research/type/T003-minimal-font-renderer-matrix.md`
- Reusable finding:
  - tabular figures are an advance-width contract, not a contour recipe;
  - zero marking is a conditional ambiguity solution, not a universal default;
  - T003 established that source-equal advances can become different hinted advances depending on renderer/mode.
- Replication / challenge / transfer opportunity:
  - execute the complete figure/punctuation brief in an actual compiled font and explicitly re-test the tabular contract through FreeType.
- Dependency / overlap:
  - production Bézier quality, manual/native hinting, browser shaping and platform renderers remain separate gates.

### Color
- Evidence checked:
  - `research/color/008-color-luminance-contrast-hierarchy.md`
  - `research/color/C001-web-color-user-override-resilience.md`
  - latest `progress/COLOR_STATUS.md`, including C002.
- Reusable finding:
  - small marks that are marginal in grayscale coverage can become less reliable under changed contrast/viewing conditions;
  - semantic hierarchy cannot be judged from geometry alone.
- Replication / challenge / transfer opportunity:
  - later composite the exact T004 alpha masks under representative light/dark/reduced-contrast conditions.
- Dependency / overlap:
  - T004 measures raster coverage only; it does not establish contrast or viewing-condition thresholds.

### Layout / Interaction
- Evidence checked:
  - `research/layout/L002-whitespace-density-spatial-rhythm.md`
  - latest `progress/LAYOUT_STATUS.md`, including I001 running validation.
- Reusable finding:
  - compactness is task-dependent;
  - dense comparison/monitoring surfaces may legitimately need stable numeric alignment;
  - typography must be tested in real density and navigation contexts.
- Replication / challenge / transfer opportunity:
  - place proportional and tabular T004 figures into matched compact/standard/spacious data surfaces.
- Dependency / overlap:
  - Layout owns whether a table/readout needs simultaneous density; Type owns whether the figure system supports it.

### Web Design
- Evidence checked:
  - `progress/WEB_STATUS.md`
  - `research/web/README.md`
- Reusable finding:
  - Web owns actual CSS/browser/page validation.
- Implementation / application validation opportunity:
  - test `font-variant-numeric: tabular-nums`, zero alternates, browser zoom/DPR, font loading/fallback and real table alignment.
- Dependency / overlap:
  - no substantive `W###` study was available at T004 start, so no browser result is inferred from this FreeType experiment.

### Other / cross-cutting / future specialist
- Evidence checked:
  - Microsoft OpenType feature registry and `tnum` / `zero` definitions;
  - FreeType glyph loading/rendering documentation already used in T003.
- Reusable finding:
  - proportional and tabular figure behavior is an OpenType feature-level concern;
  - slashed zero is an established discretionary alternate;
  - hinted metrics can differ from source metrics.
- Dependency / overlap:
  - human recognition performance is not established by a raster contact sheet.

### Overlap decision
- **EXTENSION + PRACTICE + METHOD COMPARISON + TRANSFER-VALIDATION PREPARATION**
- Why:
  - Study 005 supplied the conceptual model; T004 supplies missing original outlines, a compiled font, a failure→redraw cycle, and a renderer-aware tabular metric test.

---

## 1. SOURCE — figure style and width behavior are independent decisions

OpenType defines independent figure features including lining/oldstyle and proportional/tabular behavior.

Sources:
- https://learn.microsoft.com/en-us/typography/opentype/spec/featurelist
- https://learn.microsoft.com/en-us/typography/opentype/spec/features_pt
- https://glyphsapp.com/learn/figure-sets

Study 005 already established the practical consequence: tabular figures require equal advance widths, but they do not require equal contour widths or horizontal scaling.

### T004 implementation decision

The research font therefore uses:

- **default proportional lining figures**;
- an OpenType `tnum` feature that substitutes fixed-cell alternates;
- no horizontal contour scaling during tabular conversion;
- the same underlying figure identity translated optically inside the fixed cell.

Because the default set is already proportional, T004 does **not** add a redundant `pnum` substitution. This is a research-font architecture decision, not a statement that production families should never expose `pnum`.

---

## 2. Construction hypothesis

T004 uses one explicit **low-contrast constructed / hybrid optical** model.

Shared rules:

- nominal stroke: approximately `82/1000 UPM`;
- lining figure height: approximately `700/1000 UPM`;
- rounded terminals/joins in the procedural construction;
- open `4`;
- `1` uses a top flag and foot;
- `6/9` share loop logic;
- `8` uses two related loops;
- punctuation weight is derived from the numeral stroke but reduced where necessary;
- ambiguity controls `O I l S B` are drawn from the same construction vocabulary.

The outlines are original procedural skeleton-to-outline constructions. They are **not traced from an existing typeface**.

### Scope limit

The procedural source intentionally prioritizes system testing. It creates polygonal research outlines and does not prove production-quality Bézier topology, overlap strategy, interpolation compatibility, or final curve economy.

Therefore T004 advances Numeral/Punctuation practice but does **not** advance Bézier discipline to PASS.

---

## 3. Compiled research font

The reproducible script builds a real quadratic TrueType font using FontTools.

### Character coverage used in the experiment

- `0–9`
- tabular alternates for `0–9`
- `O I l S B` ambiguity controls
- `: + , . / -`
- mathematical minus `−` as an additional semantic control
- zero alternatives:
  - unmarked default;
  - slashed;
  - internal-dot research alternate.

### OpenType features present

The generated GSUB contains:

- `tnum`
- `zero`
- `cv01`

`zero` maps the default zero to the slashed alternate. `cv01` is used only as a research mechanism for the dotted/internal-mark candidate.

Private-use cmap entries also expose alternates directly so FreeType can render them without a shaping engine. Those mappings are **research instrumentation**, not a production encoding strategy.

---

## 4. Proportional versus tabular source metrics

### Proportional source advances

| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 600 | 480 | 570 | 560 | 600 | 560 | 580 | 560 | 590 | 580 |

The ten-figure source total is `5680` units.

### Tabular source advances

Every tabular alternate uses:

`620 units`

The ten-figure source total is therefore `6200` units.

The contours are not stretched to fill the cell. The narrow `1` remains narrow; the fixed-cell conversion changes side-space/positioning.

### STUDIO JUDGMENT

This is the correct order for a tabular experiment:

1. preserve recognizable contour identity;
2. define the equal cell;
3. distribute side space/optical position inside that cell;
4. render repeated sequences;
5. only then decide whether any contour needs a small compensating redraw.

A fixed width alone does not prove a good tabular set.

---

## 5. TRANSFER VALIDATION — equal source advances do not guarantee equal raw hinted advances

T003 exposed this problem with two lowercase `n` variants. T004 deliberately tests the same issue on the **entire tabular 0–9 set**.

All ten `.tnum` glyphs have the same `620` source advance.

FreeType raw hinted advances:

| ppem | no hint | auto-hint normal | auto-hint light |
| ---: | --- | --- | --- |
| 14 | all `8.6875px` | split `8 / 9px` | all `9px` |
| 20 | all `12.40625px` | split `12 / 13px` | all `12px` |
| 48 | all `29.765625px` | split `29 / 30px` | all `30px` |

At `20ppem` under normal auto-hinting, digit `6` receives a raw `13px` advance while most tabular figures receive `12px`.

### SYNTHESIS

`tnum` is fundamentally a source-metric contract, but **rendered table alignment is still a client/rendering-stack behavior**.

Equal `hmtx` does not permit the studio to skip actual runtime validation when exact alignment is operationally important.

### Scope limit

T004 does not claim that a modern browser, CoreText, DirectWrite, Skia, Flutter, or another stack will use these exact FreeType raw advances. T003 already established that positioning algorithms and delta handling can modify the final origin sequence.

The result is therefore a **risk demonstration**, not a universal renderer rule.

---

## 6. Failure → redraw cycle: colon

The first colon candidate used `50-unit` diameter dots (`colon.v0`).

In the compact raster proof, the mark remained only low-coverage antialiasing.

### Strong-coverage pixels (`alpha >= 128`)

| ppem | colon v0 | colon v1 |
| ---: | ---: | ---: |
| 14 | 0 | 2 |
| 20 | 0 | 4 |
| 48 | 8 | 26 |

Coverage-pixel-equivalent area:

| ppem | v0 | v1 |
| ---: | ---: | ---: |
| 14 | 0.749 | 2.145 |
| 20 | 1.529 | 4.408 |
| 48 | 8.788 | 25.318 |

The final research colon increases dot diameter to `84 units`.

### Disposition

- **v0: REJECT for this compact research system.**
- **v1: KEEP FOR FURTHER VALIDATION, not PASS.**

This is a genuine raster-triggered redraw. The fix changes the punctuation itself rather than increasing surrounding spacing or contrast.

---

## 7. Zero strategies

Study 005 and OpenType's `zero` feature establish that `0/O` ambiguity is a legitimate problem but do not require a slash as the universal default.

Source:
- https://learn.microsoft.com/en-us/typography/opentype/spec/features_uz

T004 tests three forms against the same surrounding system.

### A. Unmarked zero

The default `0` is narrower than `O`.

Under auto-hint-light:

| ppem | `0` advance | `O` advance |
| ---: | ---: | ---: |
| 14 | 8px | 9px |
| 20 | 12px | 13px |
| 48 | 29px | 31px |

This supplies a proportion cue, but a raster contact sheet cannot prove a human error rate.

**Disposition: viable default where ambiguity risk is low; sufficiency remains OPEN.**

### B. Slashed zero

Relative to default zero, the slash adds strong-coverage pixels under auto-hint-light:

- 14ppem: `+5`
- 20ppem: `+8`
- 48ppem: `+55`

The mark remains explicit at compact size in this experiment.

**Disposition: strongest compact ambiguity alternate in this T004 construction, but not selected as the global default.**

### C. Internal-dot alternate

At 14 and 20ppem under auto-hint-light, the internal dot adds measurable low-alpha coverage but **zero additional strong pixels**.

- 14ppem extra coverage: about `1.745` pixel-equivalent, strong-pixel delta `0`
- 20ppem extra coverage: about `2.561` pixel-equivalent, strong-pixel delta `0`
- 48ppem strong-pixel delta: `+8`

**Disposition: REJECT for compact use in its current form.**

A larger dot or pill would be a different design hypothesis and must be re-tested rather than assumed to solve the problem.

### STUDIO JUDGMENT

T004 does not turn “slashed zero wins this raster test” into “all operational products should use a slashed zero.”

The project must first establish:

- whether `0/O` confusion is consequential;
- the minimum size/density;
- surrounding identifiers;
- target renderer;
- whether marked-zero style creates unwanted coding/OCR/technical tone;
- whether an alternate feature can be reliably enabled in the product.

---

## 8. Other ambiguity groups

The research font also constructs:

- `1 / I / l`
- `5 / S`
- `8 / B`

The structural strategy is systematic:

- `1` — top flag + foot;
- `I` — cap bars + central stem;
- `l` — simple ascender with tail;
- `5` — top/vertical/lower-bowl logic;
- `S` — continuous curved spine;
- `8` — paired loops;
- `B` — explicit vertical stem + two bowls.

At 14ppem auto-hint-light the distinctions remain visibly present in the rendered proof.

### Evidence limit

This is **designer inspection**, not a controlled recognition experiment. T004 may state that distinct cues survive rasterization; it may not state a measured reduction in user confusion.

---

## 9. Punctuation system observations

Required contexts were rendered:

- `23:59`
- `1+05`
- `12+40`
- `99,999+59`
- `-12.5`
- `12/34`

Additional minus `−` exists as a semantic control.

### Current critique

- colon required a real redraw and now has stronger compact presence;
- plus is intentionally wider/heavier than colon because it carries operator meaning;
- comma and period remain subordinate to figures at the 20ppem proof size;
- slash is long enough to read as punctuation rather than the internal zero mark;
- hyphen is vertically lower/shorter than the mathematical minus.

These remain construction observations. Full punctuation spacing, language-specific punctuation, mathematical setting and browser text shaping are not complete.

---

## 10. Project-readiness test

### When should this knowledge be applied?

Use it when a product contains:

- changing tabular values;
- dense financial/operational data;
- clocks/times;
- identifiers mixing letters and figures;
- compact tables/readouts;
- user-configurable or custom fonts;
- contexts where `0/O`, `1/I/l`, `5/S`, or `8/B` errors matter.

### When should it not be over-applied?

Do not force tabular figures into running prose or mark every zero merely because the font supports those features.

Do not build a bespoke numeral system when the chosen platform/system font already meets the product's accuracy, density, brand and localization requirements.

### Required project inputs

Before recommending figure behavior, collect:

1. representative numeric/identifier strings;
2. whether values change in aligned columns;
3. minimum/typical size;
4. renderer/platform/browser stack;
5. ambiguity cost;
6. languages/scripts/fallback;
7. whether proportional rhythm or tabular comparison matters more per role;
8. expected zoom/text scaling;
9. accessibility/viewing conditions;
10. whether OpenType features can be enabled reliably.

### Decisions this can change

- proportional vs tabular figures by semantic role;
- marked vs unmarked zero;
- minimum approved numeric size;
- punctuation scale and spacing;
- whether custom figures are acceptable in compact roles;
- whether runtime alignment must be validated on each target stack;
- whether a system font should handle dense data while a brand face handles identity roles.

### Failure conditions

Rework or reject when:

1. tabular is claimed merely because source widths are equal;
2. figures are stretched to fill a common cell;
3. punctuation disappears at compact size;
4. ambiguity is “solved” by unrelated novelty marks;
5. slashed zero is imposed without a real ambiguity need;
6. dotted/internal marks disappear in the target renderer;
7. source metrics are assumed to equal final rendered positioning;
8. figure style is approved from large isolated glyphs only;
9. a compact data font is selected without Layout density and Color/viewing-condition tests.

---

## 11. What T004 completes and what remains open

### Established

- original complete `0–9` research construction;
- proportional source metrics;
- tabular fixed-cell alternates;
- real OpenType `tnum`;
- three zero strategies;
- required punctuation subset;
- ambiguity controls;
- compiled TrueType output;
- FreeType compact/normal/display raster proof;
- one actual failure → redraw → re-proof cycle;
- a full-set renderer-aware tabular metric stress test.

### Still OPEN

- production-quality editable curve topology;
- overlap/interpolation/source compatibility;
- manual/native hinting;
- CoreText / DirectWrite / Skia / browser/device behavior;
- HarfBuzz/browser feature application;
- real CSS `tnum`/`zero` behavior;
- human recognition tests;
- Latin/Korean mixed-script relationship;
- broader punctuation/language coverage;
- production QA and build pipeline;
- project-specific selection of zero strategy or figure style.

**Foundation Numeral/Punctuation status may advance from IN STUDY to PRACTICE / CRITIQUE, but not PASS.**

---

## HANDOFFS TO OTHER SPECIALISTS

### Typography / Type
- Useful finding/context:
  - source-equal tabular widths can diverge in raw hinted advances;
  - punctuation and zero alternatives must be judged at target size.
- Canonical section:
  - Sections 5–8.
- Confirmation / contradiction / transfer note:
  - confirms Study 005's system model and extends T003 renderer dependency from one control glyph to a full numeric set.
- Scope limit:
  - no production typeface or final zero policy is selected.

### Color
- Useful finding/context:
  - colon v0 and dotted zero show low compact coverage; they are good controlled inputs for luminance/viewing-condition transfer tests.
- Canonical section:
  - Sections 6–7.
- Confirmation / contradiction / transfer note:
  - supports Color's rule that nominal geometry alone does not prove visual reliability.
- Scope limit:
  - Type supplies alpha/render evidence, not a contrast threshold.

### Layout / Interaction
- Useful finding/context:
  - tabular cells support comparison, but runtime alignment may depend on renderer/client behavior;
  - compact punctuation/ambiguity must be validated in the density that requires it.
- Canonical section:
  - Sections 4–5 and Project-readiness test.
- Confirmation / contradiction / transfer note:
  - transfers L002's task-dependent density principle into numeric typography.
- Scope limit:
  - Type does not decide whether the product should be compact or how many columns should remain visible.

### Web Design
- Useful finding/context:
  - T004 provides a reproducible research font architecture for actual browser `tnum`, zero-alternate, zoom/DPR and table-alignment tests.
- Web application / validation consequence:
  - test actual CSS feature application, loading/fallback, layout alignment and numeric strings in real pages.
- Confirmation / contradiction / transfer note:
  - FreeType proves that equal source advances are not sufficient to infer every rendered client result.
- Scope limit:
  - no browser behavior is claimed by T004.

---

## Status implication

T004 closes a major **practice** gap but deliberately does not close the Foundation gate.

The next high-value Type work should shift from “do figures exist?” to one of two deeper questions:

1. **T005 mixed Latin/Korean fallback and vertical-metric compatibility**, because product-facing typography cannot remain Latin-only; or
2. **browser transfer of T001/T003/T004** once substantive Web evidence or an explicit Type-owned browser experiment is available.

A production numeral redesign is not justified until an actual project supplies its task, renderer, language, density and ambiguity requirements.
