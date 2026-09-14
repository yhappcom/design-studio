# Typography / Type Design Specialist Status

Operating state: **ACTIVE — RESEARCH MAY RESUME**  
Governance sync: 2026-09-15  
Primary path: `research/type/`  
Next new-study ID: `T013`

This file is maintained by the Typography / Type Design Specialist. The specialist must not update global `progress/STATUS.md` directly.

## Operational mission

Type research exists to improve real app, web and product decisions. Research volume is not the objective. Live-project output must translate evidence into project-specific guidance on font choice, hierarchy, metrics, spacing, numerals, localization, fallback, source/build quality, package/release integrity, OpenType behavior, variable axes, rendering, accessibility, implementation trade-offs, validation and failure conditions.

## Current level

Current curriculum stage: **Stage 1 — Foundation**  
Overall state: **PRACTICE / CRITIQUE**  
Foundation: **NOT PASSED**

The program now has controlled evidence across source construction, raster behavior, numerals/punctuation, mixed-script fallback, production outline QA, two-master interpolation, variable-font binary QA, static/variable WOFF2 subset semantics, `kern`/`locl` package contracts, and **`mark`/`mkmk` anchor-chain release QA**.

Major unresolved gates remain: external broad QA/sanitizers; HarfBuzz/browser/platform shaping; production combining-mark/complex-script systems; vertical writing; three-master/multi-axis/CFF2 work; components/diacritics/family coherence; complete naming/style linking; hinting strategy; mixed-script line layout; and human reading/recognition evidence.

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

T002–T012 retain reproducibility/evidence artifacts beside their studies. T012 adds:

- `research/type/T012-mark-mkmk-anchor-release-contract.py`
- `research/type/T012-mark-mkmk-anchor-release-contract-results.json`

Generated experimental font binaries remain local outputs, not product assets or source authority.

---

## Latest completed block — T012 `mark` / `mkmk` anchor release contract

T012 was selected after rechecking the top queue item, external broad QA/sanitizer integration. `fontbakery`, `fontspector`, `ots-sanitize`, and `hb-shape` were unavailable; a FontBakery installation attempt failed because the environment could not resolve the package index. No external QA/shaping PASS is claimed.

The highest-value executable fallback was the next open gap: combining marks, anchors and chained GPOS semantics.

### SOURCE

- OpenType registers `mark` for Mark Positioning and `mkmk` for Mark to Mark Positioning.
- GPOS LookupType 4 represents mark-to-base attachment; LookupType 6 represents mark-to-mark attachment.
- Mark arrays carry mark classes and anchors; corresponding base/mark arrays carry target attachment anchors.
- fontTools subsetting retains `mark`/`mkmk` by default but permits explicit feature removal.

### Controlled contract

1000-UPM static research font:

- `A` U+0041, advance `600u`;
- U+0301 COMBINING ACUTE, advance `0u`;
- U+0307 COMBINING DOT ABOVE, advance `0u`;
- `latn/dflt` `mark` binding;
- `latn/dflt` `mkmk` binding;
- mark-to-base: acute `[100,0] → A [300,700]`;
- mark-to-mark: dot `[100,0] → acute [100,220]`.

### Normal package/subset result

Source WOFF2 and a feature-aware `A + U+0301 + U+0307` subset both preserved the bounded contract.

The subset renamed `dotabovecomb` to `uni0307`. The first checker incorrectly treated this as failure. The checker was revised to resolve glyph identity from cmap and then inspect actual GPOS coverage/anchors.

This independently reinforces T009: **source glyph names are not a safe default post-subset semantic key**.

### Adversarial result A — drop `mark`, retain `mkmk`

The WOFF2 remained parseable and retained:

- all requested codepoints;
- both zero-width combining marks;
- `mkmk` binding and mark-to-mark anchors.

It lost `mark` binding and the mark-to-base attachment.

**Consequence:** the stacked-mark stage can survive while the first mark has no base attachment.

### Adversarial result B — retain `mark`, drop `mkmk`

The WOFF2 retained cmap, zero advances and mark-to-base semantics but lost `mkmk` and mark-to-mark attachment.

**Consequence:** base→mark can survive while mark→mark fails.

### Adversarial result C — drop all layout features

Every requested codepoint and both zero advances survived, but all mark attachment semantics were gone.

### SYNTHESIS

T009–T012 now support:

`character closure ≠ metric identity ≠ feature binding ≠ anchor identity ≠ complete attachment chain ≠ shaping/rendering integration`.

Unicode coverage and zero-width marks do not certify mark support. Partial retention of one attachment stage does not certify a sequence requiring the full chain.

### STUDIO JUDGMENT

For products that require combining marks, exact shipped-artifact QA should, where relevant, assert:

- required codepoints and normalization-sensitive sequences;
- intended mark advances;
- script/langsys feature binding;
- required GPOS lookup types/classes;
- mark classes and anchor coordinates/tolerances;
- complete `base → mark → mark` or equivalent chain;
- subset/package preservation;
- separate shaping-engine/browser/platform validation.

### OPEN

- HarfBuzz/browser/platform shaping;
- Unicode normalization/content-path testing;
- ligature mark attachment;
- multiple mark classes/collision behavior;
- Arabic/Indic and other complex scripts;
- production diacritic design quality;
- variable anchor interpolation/CFF2;
- external FontBakery/Fontspector/OTS broad QA;
- human evidence.

### Evidence level

**PRACTICE + CRITIQUE / synthetic static TrueType + WOFF2 + feature-aware subset + structural GPOS anchor audit + three adversarial feature-loss conditions + checker failure/revision.**

T012 is **not PASS**.

---

## Foundation module status

| Module | Status | Remaining gate |
| --- | --- | --- |
| Type anatomy / metrics | PRACTICE / CRITIQUE | broader family/role and target-platform validation |
| Stroke / contrast / construction | PRACTICE / CRITIQUE | broader coherent family extension and role transfer |
| Bézier / outline discipline | PRACTICE / CRITIQUE | complex curves/components/diacritics and family proof |
| Multi-master / interpolation | PRACTICE / CRITIQUE | three-master/multi-axis/CFF2/components/variable anchors |
| Optical correction | PRACTICE / CRITIQUE | broader family/axis/platform intended-size proof |
| Rasterization / rendering | PRACTICE / CRITIQUE | CoreText/DirectWrite/Skia/browser/device + hinting strategy |
| Spacing / kerning / GPOS | **PRACTICE / CRITIQUE** | T011/T012 cover pair positioning and mark chains structurally; broader classes/shaping/browser proof open |
| Numerals / punctuation | PRACTICE / CRITIQUE | production figures, browser shaping, localization, human evidence |
| Typography as information architecture | CRITIQUE | production reflow/localization/enlarged-text transfer |
| Web fallback / metric transfer | IN STUDY / TRANSFER BASELINE | real loading/failure/script fallback, metric overrides, zoom/reflow |
| Mixed-script / fallback | PRACTICE / CRITIQUE | real shaping/line boxes/Korean breaking/complex scripts/human evidence open |
| Source/build/release pipeline | **PRACTICE / CRITIQUE** | T006–T012 span source→interpolation→binary→package semantic/anchor QA; external broad QA and target integration remain open |

---

## Peer evidence currently affecting Type

### Color

C009 shows fixed semantic Color pairs do not normalize Type weight/fallback/rendered mass. T012 adds another provenance condition: attachment semantics in the exact shipped artifact can alter the rendered ink field without any Color-token change.

### Layout / Interaction

L003/L004 show Type behavior can cross wrap/column thresholds. T012 adds mark attachment as a Type precondition before layout regression; Layout should not compensate for a broken shipped-font attachment contract.

### Web Design

No substantive `W###` evidence exists at this checkpoint. Web should validate exact WOFF2/subsets with real text normalization/content, shaping, fallback, zoom/DPR and target browser/OS combinations.

---

## Active next queue

1. **T013 — external broad QA + sanitizer integration** when FontBakery/Fontspector/OTS or equivalent executables are available; keep universal/spec/vendor-policy checks separate from studio semantic assertions.
2. HarfBuzz/browser shaping of T011/T012 exact artifacts, especially combining-mark and normalization-sensitive sequences.
3. Extend attachment QA into ligature marks, multiple mark classes, cursive attachment and production complex scripts.
4. Study vertical-writing release semantics: `vhea`, `vmtx`, `vert`, `vrt2` where project relevance justifies it.
5. Broaden variable-family compatibility: three masters, multiple axes, richer `avar`, components/diacritics, variable anchors, overlap strategy and CFF2.
6. Browser/platform transfer of T001–T012 with substantive Web/live target stack.
7. Type→Layout regression against exact shipped artifacts.
8. Type→Color transfer with exact package/build/axis/render condition.
9. Broader family coherence and human reading/recognition evidence after target rendering/layout stabilizes.

---

## Open research-quality gaps

- FontBakery/Fontspector/OTS and exception policy;
- HarfBuzz shaping integration;
- normalization-sensitive mark behavior;
- ligature marks/multiple mark classes/cursive attachment/complex scripts;
- production Korean/multi-script feature closure;
- vertical metrics/writing features;
- complete naming/style-linking/STAT/avar metadata;
- three-master/multi-axis/CFF2/variable-anchor expansion;
- components/diacritics and broad family coherence;
- hinting strategy;
- cross-machine/toolchain provenance;
- CoreText/DirectWrite/Android/Skia/Flutter/browser transfer;
- mixed-script line-box construction and Korean line breaking;
- human recognition/reading evidence;
- release-artifact regression against Layout and Color contracts.

---

## HANDOFFS TO OTHER SPECIALISTS

### Color

Use the exact shipped artifact after Type semantic QA when evaluating rendered Type/Color robustness. Mark attachment failure can change the rendered ink field while Color remains unchanged. No Color threshold is inferred.

### Layout / Interaction

Treat required mark attachment as a Type prerequisite before localized geometry/reflow measurements. Do not mask missing `mark`/`mkmk` semantics with layout fixes.

### Web Design

Validate exact WOFF2/subsets using real combining-mark sequences, normalization/content paths, browser shaping, fallback, zoom/DPR and target devices. T012 is not Web PASS.

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
- **T012: `mark`/`mkmk` + exact anchor-chain package contract; cmap/zero-width survival shown insufficient, partial attachment-chain loss reproduced, and checker revised to avoid source glyph-name dependence.**
- Next Type study ID: `T013`.
- Overall Type state remains **Stage 1 / PRACTICE + CRITIQUE / Foundation NOT PASSED**.
