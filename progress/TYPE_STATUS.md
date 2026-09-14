# Typography / Type Design Specialist Status

Operating state: **ACTIVE — RESEARCH MAY RESUME**  
Governance sync: 2026-09-15  
Primary path: `research/type/`  
Next new-study ID: `T016`

This file is maintained by the Typography / Type Design Specialist. The specialist must not update global `progress/STATUS.md` directly.

## Operational mission

Type research exists to improve real app, web and product decisions. Research volume is not the objective. Live-project output must translate evidence into project-specific guidance on font choice, hierarchy, metrics, spacing, numerals, localization, fallback, Unicode/text normalization boundaries, source/build quality, package/release integrity, OpenType behavior, variable axes, rendering, accessibility, implementation trade-offs, validation and failure conditions.

## Current level

Current curriculum stage: **Stage 1 — Foundation**  
Overall state: **PRACTICE / CRITIQUE**  
Foundation: **NOT PASSED**

The program now has controlled evidence across source construction, raster behavior, numerals/punctuation, mixed-script fallback, production outline QA, two-master interpolation, variable-font binary QA, static/variable WOFF2 subset semantics, `kern`/`locl` package contracts, `mark`/`mkmk` anchor-chain release QA, Unicode normalization-sensitive subset closure, Hangul NFC↔NFD structural package transfer, and **bounded Chromium canonical-equivalent Hangul cluster matching/render transfer**.

Major unresolved gates remain: external broad QA/sanitizers; direct HarfBuzz trace; Firefox/Safari/native platform shaping; production Korean and complex-script systems; real product normalization/loading/fallback behavior; vertical writing; three-master/multi-axis/CFF2 work; components/diacritics/family coherence; complete naming/style linking; hinting strategy; mixed-script line layout; and human reading/recognition evidence.

---

## Canonical evidence

Legacy:

- `research/type/001-type-as-system.md`
- `research/type/002-metrics-spacing-optical-rhythm.md`
- `research/type/003-stroke-contrast-bezier-optics.md`
- `research/type/005-numerals-punctuation-systems.md`
- `research/type/009-typography-as-information-architecture.md`

T-series:

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

T015 reproducibility artifacts:

- `research/type/T015-hangul-browser-canonical-cluster-transfer.py`
- `research/type/T015-hangul-browser-canonical-cluster-transfer-results.json`

Generated experimental font binaries/screenshots remain runtime outputs, not product assets or source authority.

---

## Latest completed block — T015 Hangul canonical-equivalent browser cluster transfer

T015 was selected only after rechecking the top queue item. `fontbakery`, `fontspector`, `ots-sanitize`, `hb-shape`, and Python `uharfbuzz` were unavailable. No external QA, sanitizer or direct HarfBuzz PASS is claimed.

Chromium `144.0.7559.96` + Playwright were available, so the highest-value executable next gap was the browser/shaping transfer that T014 explicitly left OPEN.

### SOURCE

- Unicode UAX #15 defines NFC/NFD and Hangul algorithmic canonical decomposition/composition.
- CSS Fonts Module Level 4 separates ordinary character-map matching from cluster matching. Its canonical-equivalent cluster rule allows a decomposed multi-codepoint sequence to use a supported canonically equivalent single-character glyph.
- T014 established structural package closure only; it did not establish browser failure.

### Controlled specimen

Synthetic 1000-UPM WOFF2 controls:

1. NFC-only: U+AC00/U+AC01, advances 420u/680u;
2. NFD-only: U+1100/U+1161/U+11A8, advances 260u/310u/370u;
3. dual: both sets.

The deliberately different advance systems make runtime path selection observable:

- NFC path at 40px = `44px` expected;
- NFD/Jamo path at 40px = `60.4px` expected.

Matrix:

- 16px + 40px;
- DPR1 + DPR2;
- NFC/NFD `가각`;
- mixed Latin+Hangul `AB가각12` / `AB가각12`;
- unsupported NFD `간` control.

### Result A — NFC-only package did not fail NFD rendering

The NFC-only font structurally lacks U+1100/U+1161/U+11A8, exactly as T014 predicts. Yet Chromium rendered NFD `가각` identically to NFC `가각` in all four size/DPR conditions.

At 40px:

- NFC width = `44px`;
- NFD width = `44px`;
- PNG raster = byte-identical;
- changed pixels = `0`.

### Result B — NFD-only package also rendered NFC identically

The NFD-only font omits U+AC00/U+AC01 but Chromium rendered NFC and NFD through the same bounded Jamo path.

At 40px:

- NFD width = `60.40625px`;
- NFC width = `60.40625px`;
- PNG raster = byte-identical;
- changed pixels = `0`.

This reverse direction is **observed Chromium implementation evidence**, not a universal standards claim.

### Result C — dual package and mixed-script transfer

The dual package rendered NFC/NFD identically at 44px/40px size, matching the precomposed path. `AB가각12` and its NFD equivalent also had identical width and raster at 16/40px and DPR1/2.

### Adversarial control

NFD `간` includes U+11AB and has canonical equivalent U+AC04; neither is supported by the NFC-only synthetic font. It produced a different width/raster. The harness therefore did not merely normalize every input outside the browser before measurement.

### Bounded assertion result

`40/40` experiment-local assertions were true.

This count is **not** a Foundation PASS metric.

### SYNTHESIS

T013–T015 now require both statements:

`canonical equivalence ≠ identical codepoint sequence ≠ identical cmap/subset closure`

and:

`different cmap/subset closure ≠ automatic target-rendering divergence`.

Updated production chain:

`content representation → binary cmap/feature closure → target cluster matching/shaping → fallback/glyph selection → rendered geometry/raster → layout/color consequence → human/product result`.

### STUDIO JUDGMENT

- Keep structural package QA and target-rendering QA separate.
- T014 remains valid; T015 limits the stronger inference that missing exact input codepoints necessarily cause browser fallback/render failure.
- Do not require dual NFC+NFD packaging solely from structural fear when a product owns and proves a narrower content/runtime contract.
- Do not remove coverage or rely on Chromium's canonical-equivalence behavior without replicating every supported target stack on which the product decision depends.
- Explicit NFC normalization may still be preferable for storage/search/cache/subset consistency even when rendering is robust.

### OPEN

- direct `hb-shape`/`uharfbuzz` glyph/cluster traces;
- Firefox and Safari/WebKit;
- Windows DirectWrite/Edge, macOS/iOS CoreText;
- Android/Skia/Flutter;
- production Korean fonts and larger corpus/Jamo shaping;
- Korean paragraph line breaking/mixed-script line boxes;
- real `@font-face` network loading, `font-display`, cache/failure states;
- real CMS/API/database/client normalization behavior;
- external FontBakery/Fontspector/OTS QA;
- human reading/recognition evidence.

### Evidence level

**PRACTICE + CRITIQUE / asymmetric synthetic Hangul WOFF2 + Chromium 144 browser shaping/rendering + 16/40px × DPR1/2 + mixed-script transfer + unsupported control + width/raster identity; 40/40 bounded assertions true.**

T015 is **not PASS**.

---

## Foundation module status

| Module | Status | Remaining gate |
| --- | --- | --- |
| Type anatomy / metrics | PRACTICE / CRITIQUE | broader family/role and target-platform validation |
| Stroke / contrast / construction | PRACTICE / CRITIQUE | broader coherent family extension and role transfer |
| Bézier / outline discipline | PRACTICE / CRITIQUE | complex curves/components/diacritics and family proof |
| Multi-master / interpolation | PRACTICE / CRITIQUE | three-master/multi-axis/CFF2/components/variable anchors |
| Optical correction | PRACTICE / CRITIQUE | broader family/axis/platform intended-size proof |
| Rasterization / rendering | PRACTICE / CRITIQUE | Chromium bounded evidence exists; CoreText/DirectWrite/Skia/Firefox/Safari/device + hinting strategy open |
| Spacing / kerning / GPOS | PRACTICE / CRITIQUE | broader classes/complex shaping/cross-browser proof open |
| Numerals / punctuation | PRACTICE / CRITIQUE | production figures, browser shaping, localization, human evidence |
| Typography as information architecture | CRITIQUE | production reflow/localization/enlarged-text transfer |
| Web fallback / metric transfer | **PRACTICE / TRANSFER BASELINE** | T015 adds exact embedded-WOFF2 Chromium canonical-cluster proof; real network loading/failure, metric overrides, zoom/cross-browser open |
| Mixed-script / fallback / normalization | **PRACTICE / CRITIQUE** | T005 + T011–T015 cover structural and bounded Chromium normalization transfer; production Korean/line boxes/cross-platform/human evidence open |
| Source/build/release pipeline | **PRACTICE / CRITIQUE** | T006–T015 span source→interpolation→binary→package→bounded browser semantic transfer; external broad QA and production target integration open |

---

## Peer evidence currently affecting Type

### Color

C009 shows fixed semantic Color pairs do not normalize Type weight/fallback/rendered mass. T015 limits a naive extension of that risk: **normalization-form mismatch does not itself prove a changed rendered glyph state** when the target browser resolves canonical equivalence. Color should measure the actual target artifact/runtime state.

### Layout / Interaction

L003 shows browser font selection can cross wrap thresholds and standalone font measurements are not enough for production geometry. T015 directly confirms that methodological principle: structural `cmap` difference alone did not predict Chromium width/raster divergence.

### Web Design

No substantive `W###` evidence exists at this checkpoint. T015 supplies a concrete future Web transfer contract: exact WOFF2 + actual normalization + `@font-face` lifecycle + cross-browser/OS/device + zoom/loading/failure must be tested before subset minimization is treated as safe.

---

## Active next queue

1. **T016 — external broad QA + sanitizer integration** when FontBakery/Fontspector/OTS or equivalent executables are available; keep universal/spec/vendor-policy checks separate from studio semantic assertions.
2. Direct HarfBuzz glyph/cluster trace and cross-browser/platform replication of T015: Firefox/Safari/Windows/macOS/Android/Flutter.
3. Production Korean transfer using a real Korean font and larger corpus: conjoining Jamo, fallback, line breaking and mixed-script line boxes.
4. Real `@font-face` network loading/failure/`font-display`/cache/zoom transfer, ideally with substantive Web/live-product work.
5. Extend attachment QA into ligature marks, multiple mark classes, cursive attachment and production complex scripts.
6. Study vertical-writing release semantics: `vhea`, `vmtx`, `vert`, `vrt2` where project relevance justifies it.
7. Broaden variable-family compatibility: three masters, multiple axes, richer `avar`, components/diacritics, variable anchors, overlap strategy and CFF2.
8. Type→Layout regression against exact shipped artifacts.
9. Type→Color transfer with exact package/build/axis/render condition.
10. Broader family coherence and human reading/recognition evidence after target rendering/layout stabilizes.

---

## Open research-quality gaps

- FontBakery/Fontspector/OTS and exception policy;
- direct HarfBuzz shaping trace;
- cross-browser/native canonical-equivalent shaping behavior;
- production Hangul/Jamo and larger Korean corpus closure;
- real content-pipeline normalization and webfont-loading behavior;
- ligature marks/multiple mark classes/cursive attachment/complex scripts;
- vertical metrics/writing features;
- complete naming/style-linking/STAT/avar metadata;
- three-master/multi-axis/CFF2/variable-anchor expansion;
- components/diacritics and broad family coherence;
- hinting strategy;
- cross-machine/toolchain provenance;
- CoreText/DirectWrite/Android/Skia/Flutter/Safari/Firefox transfer;
- mixed-script line-box construction and Korean line breaking;
- human recognition/reading evidence;
- release-artifact regression against Layout and Color contracts.

---

## HANDOFFS TO OTHER SPECIALISTS

### Color

T015 limits the inference from T014: a normalization-form package mismatch does not automatically create different rendered Type/Color conditions in Chromium. Pin exact artifact + target runtime, then measure. No Color threshold is inferred.

### Layout / Interaction

L003's browser-first geometry rule is directly reinforced. Do not predict localized wrap/density from structural `cmap` coverage alone; measure exact shipped font + normalization + shaping/browser state near real thresholds.

### Web Design

Reproduce T015 with production `@font-face` delivery, exact content-source normalization, target browsers/OSes/devices, zoom/DPR and loading/failure/cache states. Chromium/Linux 40/40 bounded assertions are not Web PASS or cross-platform package approval.

## Handoff rule

Answer peer requests with canonical Type evidence or new investigation as appropriate. Do not silently replace peer ownership or edit peer canonical files without authorization.

---

## Latest checkpoint

- T002: raster failure→redraw.
- T003: compiled TrueType renderer matrix.
- T004: research numeral/punctuation + tabular proof.
- T005: Latin/Korean fallback transfer.
- T006: production outline audit + CFF/TTF transfer.
- T007: two-master interpolation compatibility/adversarial correspondence.
- T008: generated-variable-font release QA.
- T009: static WOFF2/subset `tnum` semantic contract.
- T010: variable WOFF2/subset axis-semantic contract.
- T011: `kern` + language-bound `locl` + multi-script cmap + line-metric package contract.
- T012: `mark`/`mkmk` + exact anchor-chain package contract.
- T013: Latin NFC/NFD normalization-sensitive subset closure.
- T014: Hangul NFC/NFD structural package transfer + deterministic rebuild proof.
- **T015: Chromium canonical-equivalent Hangul cluster transfer; asymmetric NFC-only/NFD-only/dual WOFF2 all produced NFC↔NFD width+raster identity across 16/40px × DPR1/2; mixed-script identity held; unsupported control differed; 40/40 bounded assertions true.**
- Next Type study ID: `T016`.
- Overall Type state remains **Stage 1 / PRACTICE + CRITIQUE / Foundation NOT PASSED**.