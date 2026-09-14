# Color Specialist Status

Operating state: **ACTIVE — RESEARCH MAY RESUME**  
Governance sync: 2026-09-15  
Primary path: `research/color/`  
Next new-study ID: `C014`

This file is maintained by the Color Specialist. The specialist must not update global `progress/STATUS.md` directly.

## Operational mission

Color research exists to improve real app, web, and product decisions. Research volume, palette count, token count, or curriculum speed are not success metrics.

When a project arrives, accumulated evidence must become project-specific guidance on palette systems, semantic color, data-visualization color, colorimetry, luminance/contrast, rendered text-color robustness, visual salience, viewing conditions, gamut, device behavior, accessibility, brand behavior, browser/platform behavior, ICC/color-management pipelines, spectral/device evidence, numerical-source provenance, implementation trade-offs, validation, failure conditions, and uncertainty.

Self-directed research remains ACTIVE. Adjacent Type, Layout/Interaction, Web Design, Accessibility, Human Factors, localization, statistics, display technology, frontend/browser behavior, measurement technology, and implementation knowledge may be studied when it materially improves Color judgment, replication, transfer validation, or project usefulness.

## Current level

Current curriculum stage: **Stage 1 — Foundation with an early bridge into Intermediate Professional Practice**  
Overall state: **CRITIQUE**  
Foundation: **NOT PASSED**

The Color program now spans UI color, luminance/contrast, colorimetry and observer models, chromatic adaptation, ICC/CMM production paths, perceptual spaces/difference, gamut mapping, perceptual ramp authoring, browser/user overrides, semantic token architecture, multi-context semantic transfer, data-visualization color, observer-conditional metamerism, fixed-geometry salience/density transfer, Type→Color rendered-role transfer, high-precision Display-P3→sRGB production validation, forced-colors state/SVG transfer, checksum-aware full-spectrum/spectral-sampling practice, and **artifact-first provenance conflict handling when first-party dataset surfaces disagree**.

Major unresolved gates remain: real human/CVD-observer evidence; exact current CIE 1964/LMS raw-byte identity; verified raw CIE 170-2 cone-fundamental-based tristimulus files and complete observer-model comparison; measured physical SPDs; real device/output profiles; second-CMM proof; browser/OS wide-gamut and real high-contrast transfer; soft-proof/print evidence; physical-display/environmental testing; production webfont/load behavior; and production-fidelity multi-project transfer.

---

## Canonical evidence

### Legacy Color studies
- `research/color/008-color-luminance-contrast-hierarchy.md`
- `research/color/010-color-science-colorimetry-foundations.md`
- `research/color/011-lms-cone-fundamentals-observer-models.md`
- `research/color/012-chromatic-adaptation-white-points.md`
- `research/color/013-perceptual-color-spaces-difference.md`
- `research/color/016-color-gamut-wide-gamut-mapping.md`
- `research/color/017-perceptual-ramp-authoring.md`

### C-series
- `research/color/C001-web-color-user-override-resilience.md`
- `research/color/C002-semantic-color-role-token-architecture.md`
- `research/color/C003-data-visualization-color-systems.md`
- `research/color/C004-spectral-integration-observer-metamerism.md`
- `research/color/C005-icc-cmm-roundtrip-validation.md`
- `research/color/C005-icc-cmm-roundtrip-validation.py`
- `research/color/C005-icc-cmm-results.json`
- `research/color/C006-semantic-token-transfer-two-contexts.md`
- `research/color/C006-semantic-token-transfer-two-contexts.py`
- `research/color/C006-semantic-token-transfer-results.json`
- `research/color/C007-fixed-geometry-color-density-salience.md`
- `research/color/C007-fixed-geometry-color-density-specimen.html`
- `research/color/C007-fixed-geometry-color-density-playwright.py`
- `research/color/C007-fixed-geometry-color-density-results.json`
- `research/color/C008-rendered-data-visualization-color-validation.md`
- `research/color/C008-rendered-data-visualization-specimen.html`
- `research/color/C008-rendered-data-visualization-playwright.py`
- `research/color/C008-rendered-data-visualization-results.json`
- `research/color/C009-type-rendering-color-contrast-transfer.md`
- `research/color/C009-type-color-rendering-specimen.html`
- `research/color/C009-type-color-rendering-playwright.py`
- `research/color/C009-type-color-rendering-results.json`
- `research/color/C010-high-precision-p3-srgb-color-management.md`
- `research/color/C010-high-precision-p3-srgb-color-management.py`
- `research/color/C010-high-precision-p3-srgb-results.json`
- `research/color/C011-forced-colors-semantic-data-resilience.md`
- `research/color/C011-forced-colors-semantic-data-specimen.html`
- `research/color/C011-forced-colors-semantic-data-playwright.py`
- `research/color/C011-forced-colors-semantic-data-results.json`
- `research/color/C012-spectral-provenance-sampling-resolution.md`
- `research/color/C012-spectral-provenance-sampling-resolution.py`
- `research/color/C012-spectral-provenance-sampling-results.json`
- `research/color/C013-authoritative-dataset-identity-conflict.md`
- `research/color/C013-provenance-conflict-gate.py`
- `research/color/C013-provenance-conflict-ledger.json`
- `research/color/C013-provenance-conflict-results.json`

Retained earlier Color exercises remain under `product-design/exercises/`.

---

## Foundation / bridge module status

| Module | Status | Remaining gate |
| --- | --- | --- |
| Luminance / contrast / hierarchy | CRITIQUE | physical-display/environmental validation; representative production contexts; human salience/reading evidence |
| Encoded RGB → linear-light → XYZ | PRACTICE / CRITIQUE | wider production/browser/device transfer |
| Spectral colorimetry / observer models | **PRACTICE / PROVENANCE VALIDATION / CONTRADICTION REVIEW / CRITIQUE** | C004 sparse metamer/1931↔1964 proof + C012 current-1931 checksum reconstruction/full smooth-SPD integration/sampling stress + C013 authority-surface audit complete; current raw 1964/LMS identity, verified raw CFB 2°/10° files, complete same-spectrum observer comparison, measured SPDs/instruments/devices/humans pending |
| Chromatic adaptation / ICC color management | PRACTICE / PRODUCTION-PATH VALIDATION | C005 D50 PCS/`chad` + C010 float/16/8-bit P3→sRGB proof complete; real output/device profiles, second CMM, soft proof/print and physical-output validation pending |
| Perceptual spaces / color difference | CRITIQUE | rendered/device comparison and tighter scope validation |
| Gamut / wide-gamut mapping | PRACTICE / CRITIQUE | C010 destination-gamut/precision separation complete; actual browser/OS/device P3 fallback and product acceptance behavior pending |
| Perceptual ramp authoring | CRITIQUE | rendered/browser/device validation; no PASS from model-space regularity alone |
| Web color override resilience | PRACTICE / CROSS-DOMAIN TRANSFER VALIDATION | C001 + I003 + C011 controlled Chromium evidence; real Windows High Contrast, multi-browser/OS/AT/production-token validation pending |
| Semantic color/token architecture | PRACTICE / TRANSFER VALIDATION | C006 two-context graph/collision/pair-matrix proof complete; production component/theme/browser and real-project transfer pending |
| Color-driven visual density / salience | PRACTICE / CROSS-DOMAIN TRANSFER VALIDATION | C007 + independent Layout L005 compatible findings; human perceived-clutter/search/comparison, cross-browser/device and physical-environment validation pending |
| Data-visualization color systems | PRACTICE / CROSS-DOMAIN TRANSFER VALIDATION | C008 rendered light/dark + C011 forced-colors SVG transfer complete; human interpretation, real CVD observers, production chart library, canvas, multi-browser/device and multi-project validation pending |
| Type-dependent Color rendering / text-role transfer | PRACTICE / CROSS-DOMAIN TRANSFER VALIDATION | C009 weight/fallback/DPR/contrast-margin proof complete; human readability, production webfont loading, broader scripts/platforms/devices/environment pending |

---

## Latest completed block — C013 authoritative dataset identity conflict

`C013-authoritative-dataset-identity-conflict.md` re-opened the provenance assumption behind C012 and found a first-party contradiction rather than a simple mirror problem.

### CIE 1931 control

For `CIE_xyz_1931_2deg.csv`:

- CIE HTML page MD5: `17cca777db64b17170f06f67ce9d3ab7`;
- linked CIE metadata MD5: `17cca777db64b17170f06f67ce9d3ab7`.

The authority surfaces agree. C012 separately supplies stronger pinned-copy checksum reconstruction evidence.

### CIE 1964 contradiction

For `CIE_xyz_1964_10deg.csv`:

- CIE HTML page MD5: `cd6135a724480eb8c5e7668bae914445`;
- linked CIE metadata MD5: `6140e032f9326d88c5a0959b29b4d8f3`.

The nominally same first-party dataset is identified differently by the page and its own linked metadata JSON.

### CIE 2006 LMS contradiction

For `CIE_lms_cf_2deg.csv`:

- CIE HTML page MD5: `27c74cc0f98edecadc02fc71f540b116`;
- linked CIE metadata MD5: `dba2e9d1f5e6667575aa069832159510`.

A separate public run also reported expecting `27c74...` and receiving a file with `dba2...`, independently reproducing the ambiguity.

### C012 interpretation revised

The previous wording “accessible mirror mismatches the current CIE checksum” is now too simple.

The stronger conclusion is:

**CIE currently exposes conflicting first-party checksum claims for the 1964 and 2006-LMS files.**

C013 therefore refuses to choose an authority surface by convenience. Exact raw file bytes remain the decisive missing evidence.

### Cleaner cone-fundamental-based future comparison path

CIE 170-2:2015 cone-fundamental-based spectral tristimulus tables currently show page↔metadata agreement:

- 2° `CIE_cfb_stv_2deg.csv`: `472cc50b14a6cf41ba9f08f8935aedc8`;
- 10° `CIE_cfb_stv_10deg.csv`: `c8504e70d7f4760253a0a4d3a42b7d20`.

These are `390–830 nm`, `1 nm` spectral tristimulus tables and are a promising future observer-comparison path, but they are **not the same dataset as the 2006 raw LMS fundamentals**. The investigations must remain explicitly separate.

### Artifact-first gate

C013 defines reusable states:

- `SURFACE_CONSISTENT_RAW_UNVERIFIED`;
- `RAW_VERIFIED`;
- `AUTHORITY_CONFLICT_RAW_UNAVAILABLE`;
- `RAW_MATCHES_ONE_AUTHORITY_SURFACE`;
- `TRANSFORMED_DERIVATIVE`.

Professional consequence: checksum validates **artifact identity**, not model appropriateness, numerical equivalence, perceptual validity, instrument quality, device reproduction or project relevance.

### Evidence level

**PRACTICE + CONTRADICTION REVIEW / live first-party HTML↔metadata comparison + public mirror triangulation + reproducible provenance gate.**

Not PASS: exact raw CIE 1964/LMS bytes were not retrieved and hashed; no complete verified 1931↔1964↔cone-model same-spectrum calculation was added in this block.

---

## Previous key blocks

### C012 — spectral provenance and sampling resolution

Strengthened CIE 1931 provenance to a pinned-copy checksum reconstruction matching `17cca777...`, integrated four complete 360–830 nm synthetic SPDs, and showed that a simple 5 nm sampling grid was stable for broad/test-display-like spectra but not for an ultra-narrow diagnostic (`Δxy ≈ 0.001920`, max relative Y error ≈ `0.456%`). C013 now refines the unresolved 1964/LMS provenance interpretation.

### C011 — forced-colors semantic/data resilience

Controlled Chromium HTML/SVG/focus testing produced 21/21 bounded assertions. Default inline SVG preserved authored paint under `preserve-parent-color`; explicit `forced-color-adjust:auto` changed raster used colors while computed stroke still exposed authored values. Structural labels/patterns/markers survived color removal; global `forced-color-adjust:none` was rejected.

### C010 — high-precision Display-P3→sRGB

35,937 P3 samples were tested through LittleCMS float/16-bit/8-bit paths. In-gamut float output agreed with independent colorimetry to about `10^-8`; extended float reversibility was separated from bounded destination delivery; cross-profile differences were measured without mislabeling them as cross-CMM/device proof.

### C009 — Type→Color rendered-role transfer

Same foreground/background pair can produce materially different raster mass under weight/fallback/DPR. Korean fallback can change width, coverage and wrap while Color remains unchanged. Contrast conformance and rendered robustness remain separate gates.

### C008 — rendered data visualization

Categorical identity/selection, sequential ordering, diverging midpoint/missing-data, light/dark remapping and CVD diagnostics have controlled rendered failure→revision evidence. C011 adds forced-colors SVG transfer.

### C007 / C006 / C005 / C004 / C001–C003

C007 covers fixed-geometry salience/density; C006 two-context semantic-token transfer; C005 ICC v4 D50 PCS/CMM diagnostics; C004 observer-conditional metamerism; C001 browser/user color override resilience; C002 semantic token architecture; C003 data-visualization source semantics.

---

## Peer evidence currently affecting Color

### Typography / Type

Type is through **T014**, next ID T015.

Relevant consequences:

- T005/C009 establish fallback/raster dependence beneath fixed Color roles;
- T013/T014 add normalization-sensitive Latin/Hangul package closure;
- T014 deterministic rebuild/provenance discipline is methodologically compatible with C013's artifact-first dataset gate;
- C011 direct labels still require production Type/fallback/normalization proof.

Color does not own font construction, shaping, fallback, normalization policy or release QA.

### Layout / Interaction

Layout/Interaction is through **L006/I004** at the latest synchronization.

Relevant consequences:

- I003 is directly confirmed and extended by C011;
- L005 independently confirms C007's separation of spatial density, feature variability and semantic collision;
- L006 shows visual appearance and behavioral ownership can diverge, reinforcing layer-specific diagnosis;
- I004 adds conflict/merge/recovery semantics that Color may encode but not redefine;
- C013 extends the same layer-specific discipline to numerical-source identity: upstream evidence conflicts are not repaired downstream by Color styling or interaction changes.

### Web Design

Web still lists **W001** as next and has no substantive W### evidence at this checkpoint. **Do not invent Web PASS.**

C009–C013 now provide future Web transfer contracts for font-dependent Color rendering, P3/sRGB color management, forced-colors/SVG behavior, device/spectral risk screening, and exact upstream artifact identity.

---

## Active next queue

Research remains ACTIVE. Priorities are expected-value guidance, not hard sequencing:

1. **C014 candidate — verified cone-fundamental-based observer comparison:** obtain and hash exact CIE 170-2:2015 CFB 2°/10° raw tables; if verified, compare the same complete spectra against the verified CIE 1931 path while naming model differences explicitly. Keep the 2006 raw-LMS investigation separate.
2. Retry exact raw CIE 1964/LMS retrieval and search for an authoritative revision/corrigendum explaining the HTML↔metadata checksum conflicts; do not choose a winner without evidence.
3. Acquire at least one measured display/LED/projector SPD and instrument metadata, then replace C012's mathematical subsampling diagnostic with a real measurement-resolution/bandwidth case when available.
4. Extend C011 into real Windows High Contrast/Edge and additional browser/OS conditions; include production SVG/canvas chart libraries and localized labels.
5. Extend C010 with a measured/device or independently sourced Display-P3/output profile, second CMM, browser/OS wide-gamut path, and soft-proof/print evidence.
6. Extend C007/C008/C009/C011 with human tasks when participants are available: search, comparison, series identification, text-role recognition, missing/reference interpretation; keep performance separate from preference/workload.
7. Validate non-text/focus/ramp/chart/Type transfer on physical displays under controlled bright/low-light conditions.
8. Compare Bradford/CAT02/CAT16 only on explicitly bounded datasets; do not declare a universal winner.
9. Transfer C001–C013 and Studies 016/017 into real Web/browser validation when substantive W### evidence becomes available.
10. Continue advanced data visualization only when it outranks the current physical/human/browser evidence gaps.

---

## Open research-quality gaps

- exact raw-file identity for current CIE 1964 10° and CIE 2006 2° LMS despite first-party checksum conflict;
- authoritative explanation/revision history for those checksum divergences;
- independent raw-file verification of CIE 170-2:2015 CFB 2°/10° spectral tristimulus tables;
- verified complete-spectra 1931↔1964↔explicit cone-fundamental-based comparison;
- measured display/LED/projector SPDs and instrument bandwidth/calibration evidence;
- real Windows High Contrast / Edge and broader browser forced/user-color evidence;
- assistive-technology behavior;
- production SVG/canvas chart-library transfer;
- human readability/low-vision and real-CVD-observer evidence;
- localized/direct-label stress with production fonts and normalization;
- human perceived-clutter/search/comparison evidence;
- production-fidelity semantic-token real-project transfer;
- real measured display/output ICC profiles;
- second CMM/toolchain and soft-proof/print validation;
- browser/OS CSS P3, tagged-image and screenshot/export color-management evidence;
- physical-display/environmental testing;
- cultural/localization evidence beyond generic color folklore;
- production-fidelity multi-project evidence.

---

## HANDOFFS TO OTHER SPECIALISTS

### Typography / Type

- C013 independently confirms the value of exact artifact identity and reproducibility before downstream visual claims, paralleling T014's deterministic package discipline.
- Korean/text Color validation should still use the exact shipped font artifact after normalization/fallback state is known.
- Scope limit: C013 makes no font-quality or legibility claim.

### Layout / Interaction

- C013 adds a source-layer rule: numerical Color evidence conflicts should be resolved at the data/provenance layer, not hidden by spatial/interaction compensation.
- C011 remains the direct forced-colors state/focus transfer.
- Scope limit: no user task or interaction behavior was tested in C013.

### Web Design

- C013 adds exact upstream profile/dataset/token identity to the acceptance contract for future browser/device Color validation.
- C012 remains the spectral/device risk screen; C011 supplies forced-colors/SVG cases; C010 supplies P3/sRGB color-management cases; C009 supplies Type/fallback/DPR cases.
- Return confirmations, limitations, contradictions or transfer failures when substantive W### work begins.

## Latest checkpoint

- C001: browser/user color override resilience.
- C002: semantic token architecture.
- C003: data-visualization source framework.
- C004: CIE 1931 sparse spectral integration/metamer + 1931↔1964 observer comparison.
- C005: ICC v4 D50 PCS/CMM and low-precision failure diagnosis.
- C006: two-context semantic-token transfer.
- C007: fixed-geometry Color→Layout salience/density transfer.
- C008: rendered categorical/sequential/diverging chart validation.
- C009: Type→Color raster/fallback/DPR transfer.
- C010: float/16-bit/8-bit Display-P3→sRGB CMM validation and delivery-boundary semantics.
- C011: forced-colors HTML state/focus + SVG preserve/auto/opt-out transfer, computed-vs-used-value raster proof, 21/21 bounded assertions.
- C012: current-CIE-1931 checksum reconstruction + complete synthetic-SPD integration + spectral-sampling stress.
- **C013: first-party CIE HTML↔metadata checksum contradictions confirmed for 1964 and 2006-LMS; 1931 and 2015 CFB 2°/10° surfaces consistent; artifact-first provenance gate established; raw conflicted files remain OPEN.**
- Next Color study ID: **C014**.
- Overall Color state remains **Stage 1 + early Intermediate bridge / CRITIQUE / Foundation NOT PASSED**.
