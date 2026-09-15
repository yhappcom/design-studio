# Typography / Type Design Specialist Status

Operating state: **ACTIVE — LIVE-PRODUCT TRANSFER IN PROGRESS**  
Governance sync: 2026-09-15  
Primary path: `research/type/`  
Next new-study ID: `T019`

This file is maintained by the Typography / Type Design Specialist. The specialist must not update global `progress/STATUS.md` directly.

## Operational mission

Type research exists to improve real app, web and product decisions. Research volume is not the objective. Live-project needs take priority over nonessential curriculum expansion.

The specialist must translate evidence into project-specific decisions on font choice, hierarchy, metrics, spacing, numerals, identifiers, localization, fallback, Unicode/text normalization, OpenType behavior, rendering, accessibility, implementation trade-offs, validation and failure conditions.

---

## Current level

Current curriculum stage: **Stage 1 — Foundation**  
Overall state: **PRACTICE / CRITIQUE + LIVE-PRODUCT TRANSFER**  
Foundation: **NOT PASSED**

Type now has controlled evidence from source/glyph construction through browser font loading, plus a real LogMate transfer chain:

`font/glyph system → metrics/features → packaging/fallback → runtime rendering → semantic geometry → product role → live UI decision`

T017/T018 do **not** close the Foundation gate by themselves. They add strong project-transfer evidence while native Android/iOS, exact shipped-font and human recognition gaps remain explicit.

---

## Canonical evidence

### Legacy

- `research/type/001-type-as-system.md`
- `research/type/002-metrics-spacing-optical-rhythm.md`
- `research/type/003-stroke-contrast-bezier-optics.md`
- `research/type/005-numerals-punctuation-systems.md`
- `research/type/009-typography-as-information-architecture.md`

### T-series

- `T001-web-typography-fallback-metrics-reflow-transfer.md`
- `T002-raster-proof-redraw-cycle.md`
- `T003-minimal-font-renderer-matrix.md`
- `T004-native-numeral-punctuation-renderer-proof.md`
- `T005-latin-korean-mixed-script-fallback.md`
- `T006-production-outline-audit.md`
- `T007-variable-interpolation-source-compatibility.md`
- `T008-production-build-release-qa.md`
- `T009-webfont-subset-feature-contract.md`
- `T010-variable-webfont-axis-contract.md`
- `T011-layout-multiscript-release-contract.md`
- `T012-mark-mkmk-anchor-release-contract.md`
- `T013-normalization-sensitive-subset-contract.md`
- `T014-hangul-normalization-subset-contract.md`
- `T015-hangul-browser-canonical-cluster-transfer.md`
- `T016-webfont-loading-fallback-metric-contract.md`
- `T017-logmate-operational-data-typography-semantic-geometry-transfer.md`
- `T018-logmate-conservative-font-candidate-audit.md`

### Reproducibility artifacts

T016:
- `T016-webfont-loading-fallback-metric-contract.py`
- `T016-webfont-loading-fallback-metric-contract-results.json`

T018:
- `T018-logmate-conservative-font-candidate-audit.py`
- `T018-logmate-conservative-font-candidate-results.json`

Generated font binaries/screenshots remain runtime outputs, not product assets or canonical source authority.

---

# Latest completed live-product block — T017/T018 LogMate transfer

## T017 — operational data typography + semantic geometry

T017 converted prior Type research into a product contract for LogMate Opening and View Logbook.

Core model:

`semantic geometry → role-specific Type behavior → OpenType feature → exceptional treatment`

Type roles were separated into:

1. **General UI Typography** — proportional;
2. **Operational Alphanumeric Identifiers** — proportional/high-legibility by default with semantic columns;
3. **Numeric Operational Data** — tabular figures where repeated comparison matters.

Key standing decisions:

- do not use monospace merely because data is technical;
- do not use tracking to fake equal airport-code width;
- keep `DEP | arrow | ARR | flexible | TIME` as semantic geometry;
- use `tnum` for time/duration/totals/counts and deliberate numeric sub-zones;
- preserve multilingual/Unicode fallback seams for user-entered data;
- bespoke LogMate font work is not justified without evidence that mature fonts cannot satisfy a concrete requirement.

## T018 — conservative candidate audit

T018 compared mature installed control families using the actual LogMate corpus:

- Roboto;
- Inter;
- Noto Sans.

Strings included airport codes, flight/aircraft/registration identifiers, operational times/totals/counts, punctuation and ambiguity groups `0/O`, `1/I/l`, `5/S`, `8/B`.

Environment:

- Chromium `144.0.7559.96`;
- Playwright;
- FontTools;
- exact control-file hashes and versions recorded;
- explicit `@font-face` control with browser font synthesis disabled.

### Measured airport-code width behavior at Opening-like 17px

| Candidate | width range | range / mean |
| --- | ---: | ---: |
| **Roboto** | **8.125px** | **25.9%** |
| Inter | 9.203px | 27.3% |
| Noto Sans | 13.453px | 41.5% |

All ten tested airport codes fit the current 56px Opening airport cell at 100%.

**Finding:** switching among conservative proportional sans families does not remove alphabetic identifier-width variance. In this control set, Roboto is already the most stable.

### Numeric behavior

At 15px with explicit `tnum`, digit-width spread was `0px` for all three controls.

Representative `02:18` widths:

- Roboto `37.359px`;
- Noto Sans `38.344px`;
- Inter `42.938px`.

Representative `9,999:59` widths:

- Roboto `57.172px`;
- Noto Sans `59.531px`;
- Inter `66.422px`.

**Finding:** numeric alignment can be solved with role-specific tabular figures without turning the full ledger into monospace.

### 200% enlarged-text stress

Keeping current LogMate fixed cell widths while doubling type size caused failures for every candidate:

- Opening airport cells;
- Opening time cell;
- View Logbook DEP/ARR cells;
- registration cells;
- long total cells.

**Finding:** no candidate makes current fixed geometry 200%-safe. Enlarged-text behavior is a Layout/UI recomposition requirement, not a reason to choose condensed/mono/smaller Type.

### Current View Logbook monospace finding

Current LogMate View Logbook forces generic `fontFamily: 'monospace'` across most ledger values.

T018 verdict: **REWORK**.

Reasons:

- numeric comparison already has `tnum`;
- semantic columns already own alignment;
- registrations/aircraft/airport identifiers do not need every character to share one cell;
- generic monospace does not name an exact shipped family and therefore varies by platform/runtime;
- it creates a second Type/fallback/baseline system without demonstrated product benefit.

### Candidate disposition

#### Roboto — **KEEP / PROVISIONAL LOGMATE BASELINE**

Why:

- lowest measured airport-width variance;
- compact operational numerics;
- supports `tnum`;
- already integrated, minimizing migration risk;
- current mobile-portrait hierarchy was already broadly satisfactory.

Required correction:

- LogMate currently bundles only Roboto 400/500 while requesting 600/700/800 in styles;
- Flutter documentation warns against relying on synthesized/extrapolated missing weights;
- normalize tokens to shipped weights and add a real Bold 700 or validate an appropriate variable package before production.

#### Inter — **KEEP AS ALTERNATE**

- strong screen-oriented family;
- tested `tnum` and `zero` support;
- airport variance close to Roboto;
- but operational strings/totals are generally wider and no measured route-alignment advantage justifies a product-wide switch.

#### Noto Sans — **KEEP AS FALLBACK ECOSYSTEM / REWORK AS MAIN**

- strong multilingual ecosystem and tested `tnum`/`zero` support;
- but highest airport-code width variance in this corpus;
- related Noto family names do not prove mixed-script metric parity (T005).

### Identifier ambiguity

Designer inspection only; no human performance claim.

- none of the three default controls decisively eliminates `1/I/l` similarity;
- Inter and Noto Sans controls expose OpenType `zero` and rendered an explicit slashed-zero alternate;
- Roboto control did not expose `zero`;
- no measured LogMate user-error evidence currently justifies global slashed zero.

`FontFeature.slashedZero()` therefore remains **OPEN for a narrow high-risk identifier role**, not a Draft 02 default.

---

## LogMate provisional Type contract after T018

### Main family

**Roboto — provisional baseline.**

Do not switch families merely to fix airport-code alignment.

### Weight direction

Prefer real shipped weights rather than simulation:

- 400 Regular;
- 500 Medium;
- 700 Bold where strong hierarchy is actually required;

or a validated variable package.

Do not rely on requested 600/800 if the shipped family does not supply them.

### Operational identifiers

Use the main proportional family by default:

- airport code;
- aircraft type;
- registration;
- carrier designator;
- whole mixed identifiers.

Keep tracking neutral unless role-specific optical evidence says otherwise.

### Numeric roles

Use explicit `FontFeature.tabularFigures()` for:

- time/duration;
- Block / PIC / SIC / Night / Instrument values;
- totals and counts;
- comparison-critical date/numeric columns;
- deliberate numeric sub-zones such as a separately modeled flight-number zone.

### View Logbook

Replace blanket generic monospace with:

`Roboto proportional identifiers + semantic columns + right-aligned tabular numeric roles`.

### Multilingual / fallback

Product-authored UI remains English-only, but user-entered/imported data is Unicode-safe by product requirement.

Current LogMate contains `NotoSansKR-wght.ttf` (~10.4MB), but T018 does not infer that this alone closes mixed-script line metrics or platform behavior.

Preserve a `fontFamilyFallback` seam. Exact Roboto + Korean fallback runtime validation remains OPEN before a global fallback contract is frozen.

---

## Foundation module state

| Module | Current evidence state | Main remaining gate |
| --- | --- | --- |
| Type anatomy / metrics | PRACTICE / CRITIQUE | broader family/role + target-platform validation |
| Stroke / contrast / construction | PRACTICE / CRITIQUE | coherent family extension / role proof |
| Bézier / outline discipline | PRACTICE / CRITIQUE | complex curves/components/diacritics/family proof |
| Multi-master / interpolation | PRACTICE / CRITIQUE | three-master/multi-axis/CFF2/components/anchors |
| Optical correction | PRACTICE / CRITIQUE | intended-size/family/platform proof |
| Rasterization / rendering | PRACTICE / CRITIQUE | native Android/iOS/CoreText/Skia/Firefox/Safari/device |
| Spacing / kerning / GPOS | PRACTICE / CRITIQUE | broader classes/complex shaping/cross-platform |
| Numerals / punctuation | **PRACTICE / CRITIQUE + LOGMATE TRANSFER** | exact production font/native/human validation |
| Typography as information architecture | **CRITIQUE + LOGMATE TRANSFER** | production reflow/localization/enlarged-text transfer |
| Web fallback / metric transfer | PRACTICE / CRITIQUE | real delivery/cache/cross-browser/zoom |
| Mixed-script / fallback / normalization | PRACTICE / CRITIQUE | production Korean/complex scripts/native/human |
| Source/build/release pipeline | PRACTICE / CRITIQUE | external broad QA + exact production integration |

Foundation remains **NOT PASSED** until a separate exact gate audit says otherwise.

---

## Current OPEN / blockers

### Tool / production Type

- FontBakery/Fontspector/OTS or equivalent external broad QA;
- direct HarfBuzz glyph/cluster tracing;
- complete naming/style-linking and production family coherence;
- broader hinting strategy;
- three-master/multi-axis/CFF2/component/diacritic coverage.

### Platform

- exact shipped LogMate font binaries inside Flutter;
- Android physical/device renderer transfer;
- iOS physical/device renderer transfer;
- Firefox/Safari/native cross-platform shaping;
- PWA production loading/cache/failure/fallback;
- actual Flutter 200% text scaling with final responsive layout.

### Multilingual

- exact Roboto + Noto Sans KR line metrics/rendering;
- Arabic/RTL and other complex scripts;
- larger production Korean corpus and line breaking;
- mixed-script user-data line boxes.

### Human / app-stage validation

Deferred until app-development validation as instructed:

- airport/registration/flight identifier recognition and error rates;
- `0/O`, `1/I/l`, `5/S`, `8/B` task evidence;
- dense-ledger scan speed/error;
- real low-light/device/readability evidence.

No human evidence is fabricated or marked complete.

---

## Active next queue

1. **T019 — exact LogMate Draft 02 Flutter Type transfer**, once the revised UI/font package is available: inspect exact shipped Roboto assets, real declared weights, ledger removal of generic monospace, `tnum`, fallback, 100%/200% text scaling and target form factors.
2. If Draft 02 is not yet executable, perform an exact **Type Stage 1 closure audit** against `curriculum/MASTER_CURRICULUM.md` before opening more unrelated theory; distinguish true Foundation gaps from later production/research gaps.
3. Resume external QA/sanitizer integration when executables become available.
4. Direct HarfBuzz and native/cross-browser replication when environments become available.
5. Production Korean/mixed-script transfer with exact project fonts.

---

## HANDOFFS TO OTHER SPECIALISTS

### Layout / Interaction

T018 confirms the semantic-column model and adds a concrete limitation: no tested family preserves current fixed Opening/Ledger cells at 200% text size. Enlarged-text recomposition must be solved spatially; do not shrink Type or add monospace to hide it.

### Color

Roboto is now the provisional stable Type input for LogMate visual work. Night/cockpit readability still requires exact rendered weight/color/device validation; family selection does not imply low-light PASS.

### Web Design

PWA should later transfer-test the exact production font package, cache/loading/failure states and enlarged text. T018's data-URI Chromium control is not production Web PASS.

### LogMate UI / product

Draft 02 may proceed under:

**Roboto main family + real declared weights + proportional operational identifiers + semantic columns + explicit tabular numeric roles + multilingual fallback seam.**

Do not create a LogMate font and do not keep blanket generic monospace in View Logbook without new evidence.

---

## Latest checkpoint

- T016: downloadable-font lifecycle / fallback metric contract.
- T017: LogMate operational-data typography + semantic-geometry transfer contract.
- **T018: conservative Roboto/Inter/Noto Sans product audit with measured LogMate corpus; Roboto retained as provisional baseline; blanket ledger monospace REWORK; 200% fixed-cell failure demonstrated across all three controls.**
- LogMate Type transfer verdict: **READY FOR LOGMATE UI TRANSFER**, with exact Flutter/native implementation validation still OPEN.
- Next Type study ID: **T019**.
- Overall Type state remains **Stage 1 / PRACTICE + CRITIQUE + live-product transfer / Foundation NOT PASSED**.
