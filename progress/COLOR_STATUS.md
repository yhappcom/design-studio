# Color Specialist Status

Operating state: **ACTIVE — RESEARCH MAY RESUME**  
Governance sync: 2026-09-14  
Primary path: `research/color/`  
Next new-study ID: `C007`

This file is maintained by the Color Specialist. The specialist must not update global `progress/STATUS.md` directly.

## Operational mission

Color research exists to improve real app, web, and product decisions. Research volume, palette count, token count, or curriculum speed are not success metrics.

When a project arrives, this specialist must convert accumulated knowledge into project-specific guidance on palette systems, semantic color, data-visualization color, colorimetry, luminance/contrast, viewing conditions, gamut, device behavior, accessibility, brand behavior, browser/platform behavior, implementation trade-offs, validation, failure conditions, and uncertainty.

Self-directed research remains ACTIVE. Adjacent Type, Layout/Interaction, Web Design, Accessibility, Human Factors, localization, statistics, display technology, or implementation knowledge may be studied when it materially improves Color judgment, independent validation, transfer testing, or project usefulness.

## Current specialist-team awareness

Design Studio has four official peer roles:

1. Typography / Type Design Specialist;
2. Color Specialist;
3. Layout, Spatial & Interaction Specialist;
4. Web Design Specialist.

Color owns canonical color science, color systems, color accessibility, gamut/color management, palette/ramp/semantic systems, data-visualization color, and device/viewing-condition questions. Type owns typography structure/rendering; Layout/Interaction owns spatial hierarchy and state/action semantics; Web Design owns complete web integration and real browser/device validation.

Before substantial work, Color reads all four specialist statuses and materially related peer evidence. New research includes `RELATED DOMAIN CHECK`; useful results are recorded under `HANDOFFS TO OTHER SPECIALISTS`.

## Current level

Current curriculum stage: **Stage 1 — Foundation with an early bridge into Intermediate Professional Practice**  
Overall state: **CRITIQUE**

The Color program now spans UI color, colorimetry/observer models, chromatic adaptation, ICC/CMM production-path validation, perceptual spaces/difference, gamut mapping, ramp authoring, web override behavior, semantic token architecture, two-context semantic transfer practice, data-visualization color, and controlled observer-conditional metamerism practice.

Foundation is **not passed**. Full checksum-verified spectral datasets, current cone-fundamental numerical validation, higher-precision/real-profile/cross-CMM production proof, browser/device evidence, physical-display/environmental tests, CVD/human-task evidence, and production-fidelity project transfer remain incomplete.

## Canonical evidence already established

- `research/color/008-color-luminance-contrast-hierarchy.md`
- `research/color/010-color-science-colorimetry-foundations.md`
- `research/color/011-lms-cone-fundamentals-observer-models.md`
- `research/color/012-chromatic-adaptation-white-points.md`
- `research/color/013-perceptual-color-spaces-difference.md`
- `research/color/016-color-gamut-wide-gamut-mapping.md`
- `research/color/017-perceptual-ramp-authoring.md`
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
- retained product-design Color exercises 005, 009, 010, 012, 013, and 016.

## Foundation / bridge module status

| Module | Status | Remaining gate |
| --- | --- | --- |
| Luminance / contrast / hierarchy | CRITIQUE | physical-display/environmental validation; representative production contexts |
| Encoded RGB → linear-light → XYZ | PRACTICE / CRITIQUE | production-path and wider-space cross-checks; device/browser transfer |
| Spectral colorimetry / observer models | PRACTICE / CRITIQUE | C004 1931 integration/scaling/metamer + 1931↔1964 proof complete; full smooth/measured spectra, independently hash-verified current files, current CIE 2006 LMS/cone comparison, physical-device validation pending |
| Chromatic adaptation / ICC color management | PRACTICE / CRITIQUE | C005 v4 profile `chad`/colorant reconstruction and actual CMM comparison complete; float/16-bit transforms, real device/output profiles, cross-CMM, soft proof and physical-output validation pending |
| Perceptual spaces / color difference | CRITIQUE | rendered/device comparison and tighter scope validation |
| Gamut / wide-gamut mapping | CRITIQUE | browser/device validation and production fallback behavior |
| Perceptual ramp authoring | CRITIQUE | rendered/browser/device validation; no PASS from model-space regularity alone |
| Web color override resilience | IN STUDY / TRANSFER VALIDATION | real browser forced-colors/theme/system-color tests; browser/device differences |
| Semantic color/token architecture | **PRACTICE / TRANSFER VALIDATION** | C006 two-context graph/collision/pair-matrix practice complete; rendered components, CVD/grayscale, multi-theme/platform/browser and real-project transfer pending |
| Data-visualization color systems | IN STUDY / NUMERICAL PRACTICE | rendered categorical/sequential/diverging examples; CVD/human-task evidence; light/dark, browser/device and multi-project validation |

## Latest completed block — C006

`C006-semantic-token-transfer-two-contexts.md` transfer-tests C002 rather than creating another abstract token taxonomy.

### Controlled contexts

Two deliberately different product archetypes were used:

- **Context F — finance analytics / portfolio tracking**, light appearance, dense numerical data, positive/negative values, chart/status semantics, and brand emphasis;
- **Context O — operational record/logbook**, dark appearance, dense records, strong active/current/focus requirements, and caution/critical operational states.

These are transfer specimens, not final MintTap or LogMate palette decisions.

### Failure → revision evidence

Both contexts first used an intentionally overloaded architecture where one strong accent family carried too many jobs.

Rejected collisions included:

- brand = primary action = selected = success = positive data = focus;
- negative data = destructive action = validation error = critical alert;
- dark-product accent = current row = action = focus = information = success.

The revision keeps distinct semantic roles even when two roles currently alias the same primitive value. This preserves reversibility when brand, platform, locale, domain conventions, or product requirements change.

### Pair-contract evidence

C006 adds reproducible relative-luminance checks for explicit foreground/background/focus/boundary contracts.

Finance specimen examples:

- primary content / canvas: `15.67:1`;
- secondary content / canvas: `6.06:1`;
- primary action content / action surface: `5.41:1`;
- focus / white surface: `6.70:1`;
- strong boundary / canvas: `3.28:1`.

Operational-dark examples:

- primary content / canvas: `16.95:1`;
- secondary content / canvas: `8.88:1`;
- on-active content / active surface: `8.40:1`;
- focus / canvas: `14.18:1`;
- strong boundary / raised surface: `3.19:1`;
- critical status / raised surface: `4.68:1`.

All declared bounded numeric contracts pass in the controlled script.

### Transfer conclusion

C002's **method** transfers; its literal values and final mappings do not.

Confirmed transferable principles:

- semantic-job inventory before palette assignment;
- primitive values separate from semantic roles;
- pair contracts rather than isolated “accessible swatches”;
- domain status separate from interaction state;
- brand separate from status by default;
- focus as its own role;
- redundant non-color cues for important meaning;
- component tokens only when justified;
- theme/environment resolution as a separate axis;
- semantic tokens may share a current primitive without becoming the same concept.

Not established as universal:

- one company-wide action hue;
- one fixed success/positive hue;
- one light/dark strategy;
- one fixed token depth;
- one rule that brand and action must always differ;
- one rule that selection/action may always share a family.

Evidence level: **PRACTICE + TRANSFER VALIDATION / semantic architecture and numeric pair evidence**. No rendered/browser/CVD/human/device PASS.

## Previous completed block — C005

C005 validates Study 012 through a real LittleCMS-managed profile path. It reconstructs the generated sRGB profile's D50 colorants from its D65→D50 `chad`, compares 4,913 sRGB colors against independent D65→D50→Lab calculation, and documents why an 8-bit Lab round trip can produce substantial RGB code error even when the CMM itself agrees with the hand calculation within the observation buffer's quantization envelope.

Professional rule retained: compare profile/white/precision/gamut assumptions before blaming a CMM or chromatic-adaptation transform.

## Previous completed block — C004

C004 supplies controlled CIE 1931 spectral integration, scaling, a constructed CIE 1931 metamer pair, CIE 1931↔1964 observer comparison and dataset-provenance audit.

Professional conclusion retained: a colorimetric match is conditional on the observer/system defining it; this does not predict individual observers and does not replace the observer model embedded in production standards.

## Peer evidence currently affecting Color

### Typography / Type

Type is through **T004**. T003/T004 provide compiled-font and raster/alpha evidence, including compact numeral/punctuation failure cases.

Color consequences:

- C006 foreground roles should later be tested with real Type rasterization rather than placeholder text;
- chart labels/numeric readouts remain high-value transfer cases;
- Color should distinguish nominal contrast from actual compact-rendering behavior.

### Layout / Interaction

Layout's L002 now provides a **216-condition Chromium density/reflow matrix**. I001 provides running navigation/state/focus evidence with a failure→revision cycle.

Color consequences:

- use L002 fixed geometry to isolate color-driven visual density/salience;
- use I001 current/focus/pending/error/success semantics as controlled Color targets;
- do not use color to repair unclear layout or state architecture.

### Web Design

At the latest synchronization, Web remains Stage 1 / not yet baselined and no substantive `W###` study is available. **Do not invent Web evidence.**

C001–C006 now provide concrete future browser validation contracts for user overrides, semantic tokens, data color, wide gamut, ICC-tagged assets and role-resolution behavior.

## Incoming dependencies

- Type may require measured contrast/luminance/viewing-condition and downstream asset-pipeline evidence for real text, numerals and chart labels.
- Layout & Interaction may require state/focus color contracts, luminance hierarchy, color-vision independence, chart-density evidence and environmental constraints.
- Web Design may require semantic token, chart palette, forced/system-color, gamut/fallback, ICC asset/export and device/viewing-condition guidance.

## Active next queue

Research remains ACTIVE. Priorities are expected-value guidance, not hard sequencing:

1. **C007 candidate:** use L002-style fixed geometry for a Color-driven density/salience transfer study; vary luminance/chroma/semantic emphasis while keeping content/geometry constant.
2. Convert C003 into rendered practice: categorical + sequential + diverging visualizations in light/dark conditions with grayscale/CVD/small-mark/state critique and at least one failure→revision cycle.
3. Render the C006 finance/operational token systems with realistic Type roles; test selected + focused + status combinations and hue-removal/CVD resilience.
4. Extend C005 with float/16-bit transforms, independently sourced/real output profiles, P3→sRGB and display→print paths, soft proof and a second CMM/toolchain where practical.
5. Extend C004 from sparse lines to complete smooth/measured spectra with independently hash-verified current CIE datasets; complete current CIE 2006 LMS/cone comparison only after provenance is verified.
6. Compare Bradford/CAT02/CAT16 only on explicitly bounded datasets; do not declare a universal winner.
7. Validate non-text/focus/ramp and T003/T004 transfer evidence on physical displays under controlled bright/low-light conditions.
8. Transfer C001–C006 and Studies 016/017 into real browser validation when substantive Web evidence becomes available.
9. Continue advanced data visualization later into cyclic scales, uncertainty, bivariate systems, heatmaps and multi-color gamut optimization.
10. Build automated Color QA only when tied to real product acceptance criteria.

## Open research-quality gaps

- fixed-geometry Color→Layout density/salience transfer using L002;
- C006 rendered/CVD/human-task and real-project validation;
- C003 rendered/CVD/human-task evidence;
- float/high-bit-depth ICC/CMM validation and actual source/destination profiles;
- P3→sRGB, display→print, soft-proof and cross-CMM evidence;
- full checksum-verified spectral integration on complete smooth/measured spectra;
- current CIE 2006 LMS/cone-fundamental numerical comparison and broader observer-diversity evidence;
- real browser implementation evidence for modern CSS color, gamut mapping, forced/system colors, token resolution and ICC-tagged assets;
- physical-display/environmental testing;
- cyclic/uncertainty/bivariate/advanced data visualization;
- automated Color QA tied to product acceptance criteria;
- cultural/localization evidence beyond generic color folklore;
- production-fidelity multi-project transfer evidence.

## Current handoffs to other specialists

### Typography / Type

- C006 supplies two explicit foreground/surface systems ready for real T003/T004/T005 rendering transfer.
- Validate numeric/status/secondary roles with actual compact glyph coverage, fallback and enlargement.
- Scope limit: Color does not define font construction, metrics or hinting.

### Layout / Interaction

- C006 keeps action, selection/current, focus and domain status semantically separate; this is consistent with I001's state-first model.
- L002 remains the next high-value fixed-geometry Color transfer matrix.
- Scope limit: Color does not redefine navigation/state/task semantics.

### Web Design

- C006 supplies explicit semantic graphs and pair contracts for future CSS/design-token implementation.
- C001/C002/C006 should be tested under forced colors, system colors, native/custom controls, light/dark resolution and real focus behavior.
- C003 and Studies 016/017 remain chart/gamut browser-transfer targets; C005 adds profile-tagged asset/export validation.
- Return browser/device/framework confirmations, limitations, contradictions or transfer failures explicitly.

## Handoff rule

If another specialist requests Color evidence, answer with canonical Color evidence or new investigation as appropriate. Cross-domain work is allowed when useful; do not silently claim peer ownership or edit peer canonical files without authorization.

## Latest checkpoint

- `C001`: Web color override resilience and validation matrix.
- `C002`: semantic color/token architecture and project-readiness method.
- `C003`: data-type-driven visualization color systems and numerical scale practice.
- `C004`: CIE 1931 spectral integration/scaling/metamer practice, 1931↔1964 observer comparison, and dataset-provenance audit.
- `C005`: actual v4 ICC profile/CMM D65→D50 validation and precision failure diagnosis.
- `C006`: two-context semantic-token transfer, collision rejection, pair matrices, and method-vs-palette separation.
- `Semantic color/token architecture` advances to **PRACTICE / TRANSFER VALIDATION**, not PASS.
- Next Color study ID: `C007`.
- Overall Color state remains **CRITIQUE / Foundation NOT PASSED**.
