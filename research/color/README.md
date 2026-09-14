# Color Research

This directory is the canonical research home for the **Color Specialist**.

## Primary scope

Research belongs here when its primary question concerns:

- color perception, luminance, contrast, adaptation and viewing conditions;
- CIE colorimetry, observer models, illuminants, XYZ, Lab/LCh, Oklab/OkLCh;
- color difference, gamut, gamut mapping, wide-gamut and HDR-related color questions;
- ICC/color management, white points, chromatic adaptation and device reproduction;
- spectral data provenance, spectral integration and device/measurement color questions;
- palette/ramp systems, semantic color architecture, brand-color behavior, data-visualization color, environmental validation and color accessibility evidence.

## Relationship with other disciplines

- **Layout, Spatial & Interaction** owns spatial grouping, responsive geometry, navigation, state/action semantics, feedback and interaction behavior. Color may encode those states but does not redefine their meaning silently.
- **Typography / Type Design** owns glyph/font systems, text metrics, hierarchy and rendering. Color foreground roles and chart labels must be validated with realistic Type conditions.
- **Web Design** owns complete website/web-app integration and real browser/device validation. Color supplies canonical palette, token, contrast, gamut, data-color, production-color and viewing-condition evidence and consumes Web findings that confirm, limit or contradict it.

These boundaries define canonical ownership, not limits on what Color may study. Cross-domain replication, method comparison, contradiction review, transfer testing, prerequisite learning and project-specific research are allowed when analytically useful.

## Mandatory cross-domain scan

Before new Color work:

1. read `AGENTS.md`, `progress/STATUS.md`, and all four specialist status files;
2. read `research/README.md`, this README, and relevant Color studies;
3. inspect related Type, Layout/Interaction and Web evidence;
4. identify reusable, uncertain, disputed or test-worthy findings;
5. decide whether the work is reuse, extension, replication, contradiction review, transfer validation, implementation validation or project-specific study;
6. record the result under `## RELATED DOMAIN CHECK`;
7. after completion, add `## HANDOFFS TO OTHER SPECIALISTS` when useful;
8. update `progress/COLOR_STATUS.md` before moving to a materially different block.

## Current canonical studies

Legacy IDs remain stable:

- `008-color-luminance-contrast-hierarchy.md`
- `010-color-science-colorimetry-foundations.md`
- `011-lms-cone-fundamentals-observer-models.md`
- `012-chromatic-adaptation-white-points.md`
- `013-perceptual-color-spaces-difference.md`
- `016-color-gamut-wide-gamut-mapping.md`
- `017-perceptual-ramp-authoring.md`

New Color studies use `C###` IDs:

- `C001-web-color-user-override-resilience.md` — forced/user colors, semantic resilience, browser-transfer contract.
- `C002-semantic-color-role-token-architecture.md` — base/semantic/component/context architecture, pair contracts, state/status separation, project-readiness method.
- `C003-data-visualization-color-systems.md` — categorical/sequential/diverging scale semantics, numerical monotonicity practice, CVD/redundant coding, interaction/theme transfer and chart failure modes.
- `C004-spectral-integration-observer-metamerism.md` — spectral tristimulus practice, spectrum scaling, constructed CIE 1931 metamer, CIE 1931↔1964 observer comparison, and dataset-provenance audit.
- `C005-icc-cmm-roundtrip-validation.md` — ICC/CMM D65→D50 profile validation, profile-tag reconstruction, 4,913-color CMM-vs-hand comparison, and low-precision round-trip failure analysis.
- `C005-icc-cmm-roundtrip-validation.py` — reproducible Pillow/ImageCms + LittleCMS validation source.
- `C005-icc-cmm-results.json` — measured profile/CMM results and interpretation boundaries.
- `C006-semantic-token-transfer-two-contexts.md` — two-context semantic-token transfer proof, semantic-collision failure analysis, pair matrices, and project-readiness validation.
- `C006-semantic-token-transfer-two-contexts.py` — reproducible contrast-contract validation for the two transfer specimens.
- `C006-semantic-token-transfer-results.json` — measured pair-matrix results and evidence limits.
- `C007-fixed-geometry-color-density-salience.md` — fixed-geometry Color→Layout transfer, salience/clutter literature synthesis, rendered chroma/luminance controls, and failure→revision evidence.
- `C007-fixed-geometry-color-density-specimen.html` — four color conditions with identical content/geometry.
- `C007-fixed-geometry-color-density-playwright.py` — Chromium geometry and Oklab image-analysis harness.
- `C007-fixed-geometry-color-density-results.json` — measured geometry identity and rendered feature statistics.
- `C008-rendered-data-visualization-color-validation.md` — rendered categorical/sequential/diverging validation across light/dark contexts, CVD diagnostic, state-identity failure, midpoint/missing-data critique, and revision method.
- `C008-rendered-data-visualization-specimen.html` — matched SVG chart specimen for failure/revised light/dark conditions.
- `C008-rendered-data-visualization-playwright.py` — Chromium + Oklab + Machado-model diagnostic harness.
- `C008-rendered-data-visualization-results.json` — measured geometry, scale-order, CVD, selection-identity, and midpoint-semantic results.
- `C009-type-rendering-color-contrast-transfer.md` — Type→Color transfer: declared contrast versus rendered raster coverage, weight/fallback/DPR dependence, and project diagnosis method.
- `C009-type-color-rendering-specimen.html` — controlled 14px Inter/Noto/Nanum browser specimen with fixed Color pairs and Korean wrap stress.
- `C009-type-color-rendering-playwright.py` — Chromium screenshot/raster diagnostic harness with explicit non-normative pixel-metric boundaries.
- `C009-type-color-rendering-results.json` — measured results for weight, fallback, DPR, contrast-margin, and wrap-threshold comparisons.
- `C010-high-precision-p3-srgb-color-management.md` — high-precision Display-P3→sRGB production-path validation across float/16-bit/8-bit, in/out-of-gamut semantics, profile differences and delivery boundaries.
- `C010-high-precision-p3-srgb-color-management.py` — reproducible LittleCMS 2.19 float/integer P3→sRGB harness.
- `C010-high-precision-p3-srgb-results.json` — measured 35,937-sample grid, round-trip, quantization, gradient and independent-profile results.
- `C011-forced-colors-semantic-data-resilience.md` — forced-colors state/focus/SVG transfer, computed-vs-used-value distinction, SVG preserve-parent-color behavior, explicit auto-adjust, and opt-out policy.
- `C011-forced-colors-semantic-data-specimen.html` — matched HTML/SVG failure/revision specimen.
- `C011-forced-colors-semantic-data-playwright.py` — Chromium forced-colors + raster verification harness.
- `C011-forced-colors-semantic-data-results.json` — 21-assertion measured state/SVG/focus/opt-out result summary.
- `C012-spectral-provenance-sampling-resolution.md` — current CIE 1931 checksum reconstruction, full 360–830 nm synthetic SPD integration, 5 nm phase/spectral-bandwidth stress, 1964 current-vs-stale provenance separation, and unresolved CIE 2006 LMS identity boundary.
- `C012-spectral-provenance-sampling-resolution.py` — reproducible checksum-gated CIE 1931 full-spectrum/sampling harness; CIE datasets are not redistributed in the repository.
- `C012-spectral-provenance-sampling-results.json` — measured provenance ledger and broad/narrow synthetic SPD sampling diagnostics.

Next new Color study ID is tracked in `progress/COLOR_STATUS.md`.

## Evidence and project-use rule

Research should distinguish as appropriate:

- `SOURCE`
- `SYNTHESIS`
- `STUDIO JUDGMENT`
- `OPEN`
- `DEPENDENCY`
- `REPLICATION`
- `CONTRADICTION`
- `TRANSFER VALIDATION`

A color topic is not project-ready merely because a palette, formula, chart, token file, profile transform, screenshot statistic, simulation, raster metric, spectral checksum, sampling diagnostic, or colorimetric calculation exists. It must be possible to state when the knowledge applies, what decision it changes, what trade-offs/failure modes exist, which peer evidence is required, and how the result will be validated.

Computational salience/clutter proxies, CVD simulations, screenshot-pixel/raster diagnostics, unbounded float round trips, profile-to-profile comparisons, forced-colors emulation and mathematical spectral-subsampling tests are not human-task, perceived-clutter, real-observer accessibility, WCAG-conformance, OS-wide high-contrast, instrument-performance, device-match or physical-appearance evidence unless the relevant method explicitly establishes that role.

## Status authority

Color progress is tracked in `progress/COLOR_STATUS.md`. The Color Specialist does not edit global `progress/STATUS.md` during ordinary work.

Current operating state: **ACTIVE — research may resume immediately**.
