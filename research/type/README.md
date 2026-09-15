# Typography & Type Design Research

This directory is the canonical research home for the **Typography / Type Design Specialist**.

## Primary scope

Type owns font/glyph construction, metrics, spacing/kerning, numerals/punctuation, family/variable-font planning, OpenType behavior, multiscript/fallback, typography systems, rendering, packaging/release integrity and font engineering. Canonical ownership does not prohibit cross-domain replication or transfer validation.

## Mandatory cross-domain scan

Before substantial Type work: read `AGENTS.md`, `progress/STATUS.md`, all four specialist statuses, `research/README.md`, this README and relevant Type studies; inspect materially related peer research; choose reuse/replication/challenge/transfer/extension deliberately; record `RELATED DOMAIN CHECK`; add handoffs when useful; update `progress/TYPE_STATUS.md` after substantial work.

## Current studies

Legacy:
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
- `T012-mark-mkmk-anchor-release-contract.md`
- `T013-normalization-sensitive-subset-contract.md`
- `T014-hangul-normalization-subset-contract.md`
- `T015-hangul-browser-canonical-cluster-transfer.md`
- `T016-webfont-loading-fallback-metric-contract.md`
- `T017-logmate-operational-data-typography-semantic-geometry-transfer.md`
- `T018-logmate-conservative-font-candidate-audit.md`
- `T019-stage1-foundation-closure-audit.md` — exact Stage 1 gate audit; Type Foundations PASS without misclassifying later production/platform/human requirements as Foundation blockers.
- `T020-stage2-entry-audit.md` — exact Stage 2 evidence map; existing bridge evidence is substantial but fragmented, and the main gap is an integrated coherent family/spacing/kerning/figure/weight/small-size comparative exercise.

Reproducibility scripts and measured JSON remain beside relevant studies. Generated experimental font binaries/screenshots are runtime outputs, not product assets or canonical source authority.

## Curriculum state

### Stage 1 — Foundations: PASS

Authority: `T019-stage1-foundation-closure-audit.md`.

This is a narrow curriculum PASS. It does not imply production-font, native-platform, multilingual-system, automated-QA or human-validation completion.

### Stage 2 — Intermediate Professional Practice: ENTRY AUDIT COMPLETE / NOT PASSED

Authority: `T020-stage2-entry-audit.md`.

Strong existing bridge evidence:
- interpolation fundamentals: T007/T010;
- screen proof/small-size failure cycles: T002–T004;
- figure-feature and tabular-numeral behavior: Study 005, T004/T009/T018;
- multi-role product typography: Study 009, T017/T018;
- browser loading/fallback geometry: T016.

Primary missing evidence:
- coherent mini-family system;
- systematic control strings;
- kerning classes/exceptions;
- integrated figure alternatives;
- diacritic/punctuation family coherence;
- design-level weight relationship proof;
- one integrated multiple-solution exercise with explicit selection criteria and peer evidence.

## Current production/transfer model

T006–T018 retain a useful production-aware chain:

1. source/design validity;
2. build/interpolation compatibility;
3. binary/spec sanity;
4. distribution transformation contract;
5. normalization/script-specific structural closure;
6. target cluster matching/shaping;
7. font request/loading/failure state;
8. fallback/glyph selection and attachment completeness;
9. target rendering/layout integration;
10. human/product validation.

These later-stage mechanisms now act as constraints and stress tests for Stage 2 practice rather than substitutes for the Stage 2 family-system gate.

## Highest-value next directions

1. **T021 — coherent mini-family + spacing/control-string system** with at least three materially different hypotheses, intended-size proof, and explicit KEEP/REWORK/REJECT critique.
2. T022 — kerning classes/exceptions + proportional/tabular figure alternatives on the selected T021 direction.
3. T023 — weight/interpolation + diacritic/punctuation coherence on the same system.
4. T024 — multi-role typography-system alternatives, preferably transferred to LogMate if live project timing is suitable.
5. If LogMate Draft 02 becomes executable first, exact shipped-font Flutter transfer outranks nonessential curriculum expansion.
6. External FontBakery/Fontspector/OTS and direct HarfBuzz/native/cross-browser work resume when suitable environments are available.

## Tool / platform OPEN

- external FontBakery/Fontspector/OTS or equivalent broad QA;
- direct HarfBuzz tracing;
- exact shipped LogMate Flutter/native renderer transfer;
- Android/iOS/Firefox/Safari cross-platform evidence;
- production PWA loading/cache/failure transfer;
- larger Korean/complex-script production transfer;
- human recognition/scan/readability evidence at app-validation stage.

## Status authority

Type progress is tracked in `progress/TYPE_STATUS.md`. The specialist does not edit global `progress/STATUS.md` during ordinary research.

Current operating state: **ACTIVE — STAGE 2 ENTRY AUDIT COMPLETE / T021 NEXT**.
