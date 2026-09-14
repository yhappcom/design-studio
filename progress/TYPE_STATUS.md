# Typography / Type Design Specialist Status

Operating state: **ACTIVE — RESEARCH MAY RESUME**  
Governance sync: 2026-09-15  
Primary path: `research/type/`  
Next new-study ID: `T012`

This file is maintained by the Typography / Type Design Specialist. The specialist must not update global `progress/STATUS.md` directly.

## Operational mission

Type research exists to improve real app, web and product decisions. Research volume or curriculum speed is not the objective. Live-project output must translate accumulated evidence into project-specific guidance on font choice, hierarchy, metrics, spacing, numerals, localization, fallback, source/build quality, package/release integrity, OpenType behavior, variable axes, rendering, accessibility, implementation trade-offs, validation and failure conditions.

## Current level

Current curriculum stage: **Stage 1 — Foundation**  
Overall state: **PRACTICE / CRITIQUE**  
Foundation: **NOT PASSED**

The Type program now has controlled evidence across source construction, raster behavior, numerals/punctuation, mixed-script fallback, production outline QA, two-master interpolation, generated-variable-font binary release QA, static WOFF2/subset feature QA, variable-axis package semantics, and **GPOS/language-bound GSUB/multi-script cmap/line-metric release contracts**.

Major unresolved gates remain: external broad QA/sanitizers; HarfBuzz/browser/platform shaping; marks/anchors/combining marks; production Korean and broader scripts; vertical-writing metrics/features; three-master/multi-axis/CFF2 work; family coherence/components/diacritics; complete naming/style-linking metadata; hinting strategy; mixed-script line layout; and human reading/recognition evidence.

---

## Canonical evidence

Legacy research:

- `001-type-as-system.md`
- `002-metrics-spacing-optical-rhythm.md`
- `003-stroke-contrast-bezier-optics.md`
- `005-numerals-punctuation-systems.md`
- `009-typography-as-information-architecture.md`

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

T002–T011 retain reproducibility/evidence artifacts beside their canonical studies. T011 adds:

- `research/type/T011-layout-multiscript-release-contract.py`
- `research/type/T011-layout-multiscript-release-contract-results.json`

Generated experimental font binaries remain local outputs, not product assets or source authority.

---

## Latest completed block — T011 layout / multi-script release contract

T011 extends T009/T010 distribution QA into four additional product-semantic properties:

1. requested Latin + Hangul cmap closure;
2. GPOS `kern` pair behavior;
3. language-system-bound GSUB `locl` plus non-cmap alternate closure;
4. exact horizontal line metrics across `hhea` and `OS/2`.

### SOURCE

- OpenType registers `kern` for pair spacing and `locl` for localized forms.
- `hhea` contains horizontal-layout ascender, descender and line-gap values and the OpenType specification advises target-application testing because applications may use `hhea`/`OS/2` fields differently.
- `OS/2` contains separate typographic and Windows ascent/descent metrics.
- fontTools subset documentation states that retained layout features pull dependent glyphs into closure; dropping layout features removes those semantics.

### Controlled contract

1000-UPM seven-glyph research TTF:

- cmap: `A`, `V`, `i`, `한`;
- GPOS `kern`: `A V = -80u`;
- GSUB `locl`: `latn/TRK`, `i → i.loclTRK`;
- source and localized `i` advances: `380u`;
- `hhea`: `820 / -220 / 20`;
- `OS/2`: `sTypo 800 / -200 / 0`, `usWin 900 / 250`.

The Hangul glyph is a simple subset-closure probe only, not evidence of Hangul design/shaping quality.

### Result A — normal package path

Source WOFF2 preserved the complete bounded contract.

Feature-aware `AVi한` subsetting also preserved the complete contract. The non-cmap localized alternate survived through GSUB closure even though its glyph name changed to `glyph00004`.

This independently reinforces T009: **glyph-name identity is not a reliable post-subset semantic contract**.

### Result B — cmap success with layout-semantic failure

An adversarial subset with layout features removed remained parseable and retained all requested codepoints `A/V/i/한`, but lost:

- the `A V = -80u` kerning pair;
- `latn/TRK locl` binding;
- localized alternate closure.

Line metrics remained intact.

**Consequence:** Unicode/glyph coverage QA can pass while required typography behavior has already failed.

### Result C — layout features survive while line metrics drift

A second adversarial artifact retained requested cmap, `kern`, `locl`, alternate closure and `OS/2` metrics, but changed only:

`hhea.ascender: 820u → 900u` (**+80u**).

TTF and WOFF2 remained parseable.

This is a separate failure class: feature semantics can survive while line-metric identity changes.

T011 does not claim a universal +80u browser line-box effect. Target shaping/layout remains a later evidence layer.

### SYNTHESIS

T009–T011 now support:

`character closure ≠ layout-feature closure ≠ language-system binding ≠ metric identity ≠ shaping/rendering integration`.

A shipped-artifact contract must therefore cover product-required behavior, not just file validity and requested Unicode presence.

### STUDIO JUDGMENT

Production subset/package QA should, when relevant, assert:

- required Unicode/script coverage;
- required GSUB/GPOS tags **and script/langsys binding**;
- dependent non-cmap glyph closure;
- representative substitution/pair behavior;
- horizontal/vertical metric identity;
- variable-axis semantics from T010;
- exact artifact provenance/hash;
- target shaping/browser/app integration as a separate gate.

### OPEN

`fontbakery`, `fontspector`, `ots-sanitize` and `hb-shape` were unavailable. No external broad-QA or shaping-engine PASS is claimed.

Also open: `mark/mkmk`, anchors/combining marks, complex scripts, real Korean shaping, `vhea/vmtx/vert/vrt2`, variable/CFF2 integration, target browser/OS/app behavior and human evidence.

### Evidence level

**PRACTICE + CRITIQUE / static TTF + WOFF2 + Latin/Hangul cmap subset + GPOS kern + language-bound GSUB locl + adversarial feature loss + adversarial line-metric drift.**

T011 is **not PASS**.

---

## Foundation module status

| Module | Status | Remaining gate |
| --- | --- | --- |
| Type anatomy / metrics | PRACTICE / CRITIQUE | broader family/role and target-platform validation |
| Stroke / contrast / construction | PRACTICE / CRITIQUE | broader coherent family extension and role transfer |
| Bézier / outline discipline | PRACTICE / CRITIQUE | diagonals/complex curves/components/diacritics and family proof |
| Multi-master / interpolation | PRACTICE / CRITIQUE | three-master/multi-axis/CFF2/components/richer avar/overlap |
| Optical correction | PRACTICE / CRITIQUE | broader family/axis/platform intended-size proof |
| Rasterization / rendering | PRACTICE / CRITIQUE | CoreText/DirectWrite/Skia/browser/device + hinting strategy |
| Spacing / kerning / GPOS | **PRACTICE / CRITIQUE** | T011 package-level pair proof exists; broader classes/GPOS/shaping/browser proof open |
| Numerals / punctuation | PRACTICE / CRITIQUE | production figures, browser shaping, localization, human evidence |
| Typography as information architecture | CRITIQUE | production reflow/localization/enlarged-text transfer |
| Web fallback / metric transfer | IN STUDY / TRANSFER BASELINE | real loading/failure/script fallback, metric overrides, zoom/reflow |
| Mixed-script / fallback | PRACTICE / CRITIQUE | T011 adds cmap/locl package contract; real shaping/line boxes/Korean breaking/human evidence open |
| Source/build/release pipeline | **PRACTICE / CRITIQUE** | T006–T011 span source→interpolation→binary→static/variable package semantic QA; external broad QA and target integration remain open |

---

## Peer evidence currently affecting Type

### Color

C009 shows fixed semantic Color pairs do not normalize Type weight/fallback/rendered mass. T010/T011 add a provenance requirement: the exact packaged artifact, axis mapping, features and metrics must be known before Type-dependent Color rendering is treated as stable.

### Layout / Interaction

L003/L004 show fallback and numeral behavior can cross wrap/column thresholds. T011 adds kerning, language-specific substitutions and line metrics as shipped-artifact inputs. Structural drift is evidence of a Type contract change, not proof of a particular browser layout failure.

### Web Design

At this checkpoint `W001` is still next and there is no substantive `W###` evidence. Web should independently validate the exact package under real `@font-face`, `lang`, kerning/localized-form shaping, line boxes, fallback, zoom/DPR and target browsers/devices.

---

## Active next queue

Choose by expected project value, not study count.

1. **T012 — external broad QA + sanitizer integration** when FontBakery/Fontspector/OTS or equivalent executables are available; separate universal/spec/vendor-policy checks from studio semantic assertions.
2. Extend package/shaping QA into `mark/mkmk`, anchors, combining marks, richer `locl`, production multi-script closure and HarfBuzz/browser shaping.
3. Study vertical-writing release semantics: `vhea`, `vmtx`, `vert`, `vrt2` where project relevance justifies it.
4. Broaden variable-family compatibility: three masters, multiple axes, richer `avar`, components/diacritics, overlap strategy and CFF2.
5. Browser/platform transfer of T001–T011 with substantive Web/live target stack.
6. Type→Layout regression against exact shipped artifacts at known thresholds.
7. Type→Color transfer with exact package/build/axis/render condition.
8. Broader family coherence and human reading/recognition evidence after target rendering/layout stabilizes.

---

## Open research-quality gaps

- FontBakery/Fontspector/OTS and exception policy;
- HarfBuzz shaping integration;
- `mark/mkmk`, anchors, combining marks and complex scripts;
- production Korean/multi-script feature closure;
- vertical metrics/writing features;
- complete naming/style-linking/STAT/avar metadata;
- three-master/multi-axis/CFF2/interpolation expansion;
- components/diacritics and broad family coherence;
- hinting strategy;
- cross-machine/toolchain WOFF2/reproducibility/provenance;
- CoreText/DirectWrite/Android/Skia/Flutter/browser transfer;
- mixed-script line-box construction and Korean line breaking;
- human recognition/reading evidence;
- release-artifact regression against Layout and Color contracts.

---

## HANDOFFS TO OTHER SPECIALISTS

### Color

- T011 adds feature/metric provenance to C009's Type-dependent rendering problem.
- Use exact shipped artifact after Type semantic QA; no Color threshold is inferred from T011.

### Layout / Interaction

- L003/L004-style regression should use exact shipped subset after verifying kerning, localized forms and line metrics.
- Cmap coverage alone cannot certify text width, pair spacing, localized-form behavior or line-metric identity.

### Web Design

- Validate exact WOFF2/subset with real `lang`, CSS/font loading and browser shaping.
- Test kerning/localized-form activation, line boxes, fallback, zoom/DPR and responsive thresholds.
- T011 is not Web PASS.

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
- **T011: GPOS `kern` + `latn/TRK locl` + Latin/Hangul cmap + line-metric package contract; cmap-only QA and feature-only QA each shown insufficient through separate adversarial failures.**
- Next Type study ID: `T012`.
- Overall Type state remains **Stage 1 / PRACTICE + CRITIQUE / Foundation NOT PASSED**.
