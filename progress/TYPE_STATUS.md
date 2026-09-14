# Typography / Type Design Specialist Status

Operating state: **ACTIVE — RESEARCH MAY RESUME**  
Governance sync: 2026-09-15  
Primary path: `research/type/`  
Next new-study ID: `T015`

This file is maintained by the Typography / Type Design Specialist. The specialist must not update global `progress/STATUS.md` directly.

## Operational mission

Type research exists to improve real app, web and product decisions. Research volume is not the objective. Live-project output must translate evidence into project-specific guidance on font choice, hierarchy, metrics, spacing, numerals, localization, fallback, Unicode/text normalization boundaries, source/build quality, package/release integrity, OpenType behavior, variable axes, rendering, accessibility, implementation trade-offs, validation and failure conditions.

## Current level

Current curriculum stage: **Stage 1 — Foundation**  
Overall state: **PRACTICE / CRITIQUE**  
Foundation: **NOT PASSED**

The program now has controlled evidence across source construction, raster behavior, numerals/punctuation, mixed-script fallback, production outline QA, two-master interpolation, variable-font binary QA, static/variable WOFF2 subset semantics, `kern`/`locl` package contracts, `mark`/`mkmk` anchor-chain release QA, Unicode normalization-sensitive subset closure, and **Hangul NFC↔NFD package transfer with deterministic rebuild proof**.

Major unresolved gates remain: external broad QA/sanitizers; HarfBuzz/browser/platform shaping; production Korean and complex-script systems; normalization/fallback behavior on real product stacks; vertical writing; three-master/multi-axis/CFF2 work; components/diacritics/family coherence; complete naming/style linking; hinting strategy; mixed-script line layout; and human reading/recognition evidence.

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

T014 reproducibility artifacts:

- `research/type/T014-hangul-normalization-subset-contract.py`
- `research/type/T014-hangul-normalization-subset-contract-results.json`

Generated experimental font binaries remain local outputs, not product assets or source authority.

---

## Latest completed block — T014 Hangul normalization-sensitive subset contract

T014 was selected after rechecking the top queue item, external broad QA/sanitizer integration. `fontbakery`, `fontspector`, `ots-sanitize`, and `hb-shape` remain unavailable. No external QA, sanitizer or shaping PASS is claimed.

The highest-value executable fallback was to transfer T013's normalization finding to production-relevant Hangul rather than assume the Latin combining-mark specimen generalizes.

### SOURCE

- Unicode UAX #15 defines NFC/NFD and special algorithmic canonical decomposition for Hangul syllables.
- OpenType `cmap` maps character codes to default glyph indices; package validity does not imply coverage of every canonical representation that might reach shaping.
- T013 established the generic normalization/subset boundary with Latin combining marks.

### Controlled Hangul cases

Python Unicode data `15.1.0`:

- `가` NFC `U+AC00` ↔ NFD `U+1100 U+1161`;
- `각` NFC `U+AC01` ↔ NFD `U+1100 U+1161 U+11A8`.

A synthetic source contains the two precomposed syllables and the three required conjoining Jamo. Three WOFF2 packages were produced:

1. NFC-only;
2. NFD-only;
3. dual-form.

### Failure A — NFC-only

The NFC-only WOFF2 remained parseable and contained U+AC00/U+AC01, but omitted U+1100/U+1161/U+11A8.

Result: both selected syllables passed NFC coverage and failed canonically equivalent NFD coverage.

SHA-256: `a13f632702b25230fe16164dc337b38a45349af7a59a711bad1b39cdf528e344`.

### Failure B — NFD-only

The NFD-only WOFF2 remained parseable and contained U+1100/U+1161/U+11A8, but omitted U+AC00/U+AC01.

Result: both selected syllables passed NFD coverage and failed NFC coverage.

SHA-256: `fb9514bc55ec557217c2a1659c36c032a666d374b382c40f7ab6e3705c0edfac`.

### Revision — dual package

The dual WOFF2 retained U+AC00/U+AC01/U+1100/U+1161/U+11A8 and passed both bounded structural coverage contracts.

SHA-256: `769b9fa37bf8ad2a62d9063c9eba5708eca5c6de357fdbe20b7d0b36d82b0702`.

This is not a universal requirement that every font duplicate every representation. Required closure follows the actual product normalization boundary.

### Reproducibility failure → revision

The first harness run produced correct semantic results but different WOFF2 hashes on repeated builds because font timestamps were not fully fixed. The revised harness pins `head.created`/`head.modified`, disables timestamp recalculation, rebuilds in an independent directory, and compares hashes.

Final result:

- NFC-only rebuild identical;
- NFD-only rebuild identical;
- dual rebuild identical;
- `all_rebuild_hashes_identical = true`.

### SYNTHESIS

T014 independently confirms T013 on Hangul:

`canonical equivalence ≠ identical codepoint sequence ≠ identical font subset closure`.

The practical chain is now:

`content normalization boundary → required codepoint representation → subset closure → shaping/fallback → layout/rendering → human/product result`.

### STUDIO JUDGMENT

Korean production subset QA must first define where normalization is guaranteed: CMS, API, database, client, or immediately before shaping. If NFC is operationally guaranteed and tested, a narrower NFC-oriented subset may be valid. If decomposed Hangul can reach shaping, either normalize deliberately or validate the exact shipped artifact against that runtime form.

Do not infer visual equivalence from `cmap` coverage. Conjoining-Jamo shaping, fallback-run behavior, Korean line breaking, renderer/platform differences and production font design remain separate gates.

### OPEN

- HarfBuzz shaping of exact T014 artifacts;
- browser fallback-run behavior when one normalization form is absent;
- production Korean font/Jamo shaping and larger corpus coverage;
- compatibility Jamo/NFKC policy where relevant;
- real CMS/API/database/platform normalization observation;
- CoreText/DirectWrite/Skia/Flutter/browser transfer;
- Korean line breaking/mixed-script line boxes;
- external FontBakery/Fontspector/OTS QA;
- human-visible failure evidence.

### Evidence level

**PRACTICE + CRITIQUE / synthetic Hangul TrueType → three WOFF2 subset contracts + two adversarial one-form failures + dual-form revision + deterministic rebuild proof.**

T014 is **not PASS**.

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
| Spacing / kerning / GPOS | PRACTICE / CRITIQUE | broader classes/complex shaping/browser proof open |
| Numerals / punctuation | PRACTICE / CRITIQUE | production figures, browser shaping, localization, human evidence |
| Typography as information architecture | CRITIQUE | production reflow/localization/enlarged-text transfer |
| Web fallback / metric transfer | IN STUDY / TRANSFER BASELINE | real loading/failure/script fallback, metric overrides, zoom/reflow |
| Mixed-script / fallback / normalization | **PRACTICE / CRITIQUE** | T005 + T011–T014 cover structural fallback/package/normalization; real shaping/line boxes/Korean breaking/complex scripts/human evidence open |
| Source/build/release pipeline | **PRACTICE / CRITIQUE** | T006–T014 span source→interpolation→binary→package semantic/normalization QA; external broad QA and target integration remain open |

---

## Peer evidence currently affecting Type

### Color

C009 shows fixed semantic Color pairs do not normalize Type weight/fallback/rendered mass. T014 adds a prior content/package prerequisite: normalization mismatch may alter glyph availability or trigger fallback while Color remains unchanged.

### Layout / Interaction

L003 shows Korean fallback can cross browser wrap thresholds and that standalone font metrics are not enough for production breakpoints. T014 adds normalization representation as another prerequisite before Korean localized width/reflow evidence is treated as stable.

### Web Design

No substantive `W###` evidence exists at this checkpoint. Web should validate actual content normalization, exact shipped WOFF2, browser shaping/fallback, `@font-face` lifecycle, zoom/DPR and target browser/OS/device combinations.

---

## Active next queue

1. **T015 — external broad QA + sanitizer integration** when FontBakery/Fontspector/OTS or equivalent executables are available; keep universal/spec/vendor-policy checks separate from studio semantic assertions.
2. HarfBuzz/browser shaping of T011–T014 exact artifacts, especially Hangul NFC/NFD, combining marks and fallback behavior.
3. Production Korean transfer: real conjoining-Jamo shaping, larger Hangul coverage strategy, Korean line breaking and mixed-script line boxes.
4. Extend attachment QA into ligature marks, multiple mark classes, cursive attachment and production complex scripts.
5. Study vertical-writing release semantics: `vhea`, `vmtx`, `vert`, `vrt2` where project relevance justifies it.
6. Broaden variable-family compatibility: three masters, multiple axes, richer `avar`, components/diacritics, variable anchors, overlap strategy and CFF2.
7. Browser/platform transfer of T001–T014 with substantive Web/live target stack.
8. Type→Layout regression against exact shipped artifacts.
9. Type→Color transfer with exact package/build/axis/render condition.
10. Broader family coherence and human reading/recognition evidence after target rendering/layout stabilizes.

---

## Open research-quality gaps

- FontBakery/Fontspector/OTS and exception policy;
- HarfBuzz shaping integration;
- normalization-sensitive browser/fallback behavior;
- production Hangul/Jamo and larger Korean corpus closure;
- real content-pipeline normalization behavior;
- ligature marks/multiple mark classes/cursive attachment/complex scripts;
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

Use exact shipped artifact after normalization/fallback state is known when evaluating Korean text roles. Normalization mismatch can change glyph output without changing semantic Color tokens. No Color threshold is inferred.

### Layout / Interaction

Treat normalization representation as a Type prerequisite before Korean wrap/density/geometry regression. L003-style browser testing should use exact shipped fonts and realistic NFC/NFD content when the product does not enforce one form.

### Web Design

Validate the actual normalization contract of content sources, then test exact WOFF2/subsets in target browsers with NFC/NFD cases that can really reach rendering, including `@font-face`, fallback, zoom/DPR, OS/device and loading/failure states. T014 is not Web PASS.

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
- **T014: Hangul NFC/NFD transfer with `가/각`; one-form WOFF2 packages fail the canonically equivalent opposite representation; dual-form revision covers both; deterministic rebuild proof completed.**
- Next Type study ID: `T015`.
- Overall Type state remains **Stage 1 / PRACTICE + CRITIQUE / Foundation NOT PASSED**.
