# Typography / Type Design Specialist Status

Operating state: **ACTIVE — RESEARCH MAY RESUME**  
Governance sync: 2026-09-15  
Primary path: `research/type/`  
Next new-study ID: `T014`

This file is maintained by the Typography / Type Design Specialist. The specialist must not update global `progress/STATUS.md` directly.

## Operational mission

Type research exists to improve real app, web and product decisions. Research volume is not the objective. Live-project output must translate evidence into project-specific guidance on font choice, hierarchy, metrics, spacing, numerals, localization, fallback, Unicode/text normalization boundaries, source/build quality, package/release integrity, OpenType behavior, variable axes, rendering, accessibility, implementation trade-offs, validation and failure conditions.

## Current level

Current curriculum stage: **Stage 1 — Foundation**  
Overall state: **PRACTICE / CRITIQUE**  
Foundation: **NOT PASSED**

The program now has controlled evidence across source construction, raster behavior, numerals/punctuation, mixed-script fallback, production outline QA, two-master interpolation, variable-font binary QA, static/variable WOFF2 subset semantics, `kern`/`locl` package contracts, `mark`/`mkmk` anchor-chain release QA, and **Unicode normalization-sensitive subset closure**.

Major unresolved gates remain: external broad QA/sanitizers; HarfBuzz/browser/platform shaping; production combining-mark/complex-script systems; normalization/fallback behavior on real product stacks; vertical writing; three-master/multi-axis/CFF2 work; components/diacritics/family coherence; complete naming/style linking; hinting strategy; mixed-script line layout; and human reading/recognition evidence.

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

T002–T013 retain reproducibility/evidence artifacts beside their studies. T013 adds:

- `research/type/T013-normalization-sensitive-subset-contract.py`
- `research/type/T013-normalization-sensitive-subset-contract-results.json`

Generated experimental font binaries remain local outputs, not product assets or source authority.

---

## Latest completed block — T013 normalization-sensitive subset contract

T013 was selected after rechecking the top queue item, external broad QA/sanitizer integration. `fontbakery`, `fontspector`, `ots-sanitize`, and `hb-shape` remained unavailable in the execution environment. No external QA, sanitizer or shaping PASS is claimed.

The highest-value executable fallback was the next T012 gap: whether a shipped subset remains valid when canonically equivalent text arrives in a different Unicode normalization form.

### SOURCE

- Unicode Standard Annex #15 defines NFC and NFD as standardized normalization forms and canonical equivalence.
- OpenType `cmap` maps character codes to default glyph indices; a valid package may still lack a codepoint required by a runtime representation.
- T012 established that character coverage and attachment semantics are separate release contracts.

### Controlled normalization contract

Controlled input:

`A + U+0301 COMBINING ACUTE + U+0307 COMBINING DOT ABOVE`

Python Unicode data `15.1.0` produced:

- NFD: `U+0041 U+0301 U+0307`;
- NFC: `U+00C1 U+0307`.

The strings are canonically equivalent after NFC normalization but do not have identical codepoint sequences.

The synthetic source contains:

- `A` U+0041, `600u`;
- `Aacute` U+00C1, `600u`;
- U+0301 and U+0307 combining marks at `0u`;
- mark anchors for `A` and `Aacute`;
- mkmk attachment for dot-above to acute.

Feature-preserving WOFF2 subsets were built from NFD-only, NFC-only and the union of both forms.

### Failure A — NFD-only package

NFD-only WOFF2 remained parseable and preserved:

- U+0041/U+0301/U+0307;
- zero advances;
- `acute → A` mark attachment;
- `dot → acute` mkmk attachment.

It omitted U+00C1, therefore the bounded NFD structural contract passed while the canonically equivalent NFC contract failed.

SHA-256: `e1d54762761c710b6e2a5ca102716354d6d7805fcb953fd8c49195b6569dc53f`.

### Failure B — NFC-only package

NFC-only WOFF2 remained parseable and preserved:

- U+00C1/U+0307;
- zero-width dot;
- `dot → Aacute` mark attachment.

It omitted U+0041/U+0301, therefore the bounded NFC structural contract passed while the canonically equivalent NFD contract failed.

SHA-256: `2e9793f2f0b5af988ced4c0409351f6498d4f67a092402b5d559341513071518`.

### Revision — dual-normalization package

The dual subset retained U+0041/U+00C1/U+0301/U+0307 and both required attachment paths. It passed both bounded structural contracts.

SHA-256: `d23fe5c3a84dc2b320520e6c48a269fa6eabc9a732963ab5819bfbf307833795`.

### SYNTHESIS

T013 adds:

`canonical text equivalence ≠ identical codepoint sequence ≠ identical subset closure`.

T009–T013 now support:

`character closure ≠ normalization-form closure ≠ metric identity ≠ feature binding ≠ anchor identity ≠ complete attachment chain ≠ shaping/rendering integration`.

A package may be parseable and semantically correct for the representation used at build time while failing canonically equivalent runtime text.

### STUDIO JUDGMENT

A production subset contract should explicitly define the product text-normalization boundary.

If one normalization form is guaranteed before shaping, QA may intentionally target that form. If unnormalized or differently normalized content can reach shaping, exact shipped-artifact regression should include materially relevant canonically equivalent forms and their required cmap/OpenType behavior.

Do not inflate package requirements blindly: the correct closure follows the real product content contract, not a universal rule that every font must duplicate every representation.

### OPEN

- HarfBuzz/browser shaping of the exact NFC/NFD packages;
- browser fallback when one form is missing;
- canonical combining-class reorder stress;
- Hangul normalization/decomposition transfer;
- Arabic/Indic normalization and shaping interactions;
- real CMS/database/API/framework normalization behavior;
- production complex-script diacritic design;
- external FontBakery/Fontspector/OTS QA;
- human-visible failure evidence.

### Evidence level

**PRACTICE + CRITIQUE / synthetic TrueType + feature-preserving WOFF2 subset + Unicode NFC/NFD transformation + structural cmap/GPOS audit + two one-form failures + dual-form revision.**

T013 is **not PASS**.

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
| Spacing / kerning / GPOS | PRACTICE / CRITIQUE | pair/mark chains structurally covered; broader classes/complex shaping/browser proof open |
| Numerals / punctuation | PRACTICE / CRITIQUE | production figures, browser shaping, localization, human evidence |
| Typography as information architecture | CRITIQUE | production reflow/localization/enlarged-text transfer |
| Web fallback / metric transfer | IN STUDY / TRANSFER BASELINE | real loading/failure/script fallback, metric overrides, zoom/reflow |
| Mixed-script / fallback / normalization | **PRACTICE / CRITIQUE** | T005 + T011–T013 cover fallback/package/normalization structurally; real shaping/line boxes/Korean breaking/complex scripts/human evidence open |
| Source/build/release pipeline | **PRACTICE / CRITIQUE** | T006–T013 span source→interpolation→binary→package semantic/anchor/normalization QA; external broad QA and target integration remain open |

---

## Peer evidence currently affecting Type

### Color

C009 shows fixed semantic Color pairs do not normalize Type weight/fallback/rendered mass. T013 adds a prior package/content condition: normalization-form mismatch can change or remove rendered glyph output without any Color-token change.

### Layout / Interaction

L003/L004 show Type behavior can cross wrap/column thresholds. T013 extends the Type prerequisite: normalization-form coverage/fallback must be known before localized geometry/reflow measurements are treated as Layout evidence.

### Web Design

No substantive `W###` evidence exists at this checkpoint. Web should validate exact WOFF2/subsets with the normalization behavior of actual CMS/API/database/client content, browser shaping/fallback, zoom/DPR and target browser/OS combinations.

---

## Active next queue

1. **T014 — external broad QA + sanitizer integration** when FontBakery/Fontspector/OTS or equivalent executables are available; keep universal/spec/vendor-policy checks separate from studio semantic assertions.
2. HarfBuzz/browser shaping of T011–T013 exact artifacts, especially combining-mark, normalization and fallback behavior.
3. Extend attachment QA into ligature marks, multiple mark classes, cursive attachment and production complex scripts.
4. Transfer normalization/subset QA into production-relevant Hangul and other scripts rather than generalizing the Latin specimen.
5. Study vertical-writing release semantics: `vhea`, `vmtx`, `vert`, `vrt2` where project relevance justifies it.
6. Broaden variable-family compatibility: three masters, multiple axes, richer `avar`, components/diacritics, variable anchors, overlap strategy and CFF2.
7. Browser/platform transfer of T001–T013 with substantive Web/live target stack.
8. Type→Layout regression against exact shipped artifacts.
9. Type→Color transfer with exact package/build/axis/render condition.
10. Broader family coherence and human reading/recognition evidence after target rendering/layout stabilizes.

---

## Open research-quality gaps

- FontBakery/Fontspector/OTS and exception policy;
- HarfBuzz shaping integration;
- normalization-sensitive browser/fallback behavior;
- canonical combining-class reorder stress;
- Hangul normalization/decomposition transfer;
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

Use the exact shipped artifact after Type semantic and normalization-closure QA when evaluating rendered Type/Color robustness. Normalization mismatch can change glyph output while Color remains unchanged. No Color threshold is inferred.

### Layout / Interaction

Treat required normalization-form coverage, fallback and mark attachment as Type prerequisites before localized wrap/density/geometry measurement. Do not mask missing package coverage with Layout compensation.

### Web Design

Validate the normalization contract of actual content sources and then test exact WOFF2/subsets using NFC/NFD cases that can really reach the browser, including shaping, fallback, zoom/DPR and target devices. T013 is not Web PASS.

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
- **T013: NFC/NFD normalization-sensitive subset closure; one-form subsets shown structurally correct for their build form yet failing the canonically equivalent runtime form; dual-form revision passed both bounded contracts.**
- Next Type study ID: `T014`.
- Overall Type state remains **Stage 1 / PRACTICE + CRITIQUE / Foundation NOT PASSED**.
