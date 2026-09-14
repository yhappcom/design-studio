# Learning Status

Status vocabulary:

- `NOT STARTED` — not yet studied
- `IN STUDY` — source study underway
- `PRACTICE` — exercises underway
- `CRITIQUE` — work exists and is being evaluated
- `PASS` — evidence satisfies the gate
- `REVISIT` — later work exposed a foundational gap

## Stage 1 — Foundations

| Domain | Status | Evidence |
| --- | --- | --- |
| Composition / visual grammar | CRITIQUE | `research/006-grid-composition-hierarchy.md`; `product-design/exercises/003-grid-composition-comparison.svg`; `product-design/exercises/003-grid-composition-comparison-critique.md`; `product-design/exercises/007-grid-responsive-transfer.svg`; `product-design/exercises/007-grid-responsive-transfer-critique.md`; narrow recomposition, forced-compression failure, and unrelated editorial transfer complete; multilingual/enlarged-text/browser proof pending |
| Grid / alignment systems | CRITIQUE | `research/006-grid-composition-hierarchy.md`; three structural hypotheses in Exercise 003; `product-design/exercises/007-grid-responsive-transfer.svg`; `product-design/exercises/007-grid-responsive-transfer-critique.md`; semantic vs disposable alignments documented across breakpoint and second context; real-browser/multilingual proof pending |
| Color / luminance / contrast | CRITIQUE | `research/008-color-luminance-contrast-hierarchy.md`; `research/010-color-science-colorimetry-foundations.md`; `research/011-lms-cone-fundamentals-observer-models.md`; `research/012-chromatic-adaptation-white-points.md`; `product-design/exercises/005-color-luminance-cross-context-practice.md`; `product-design/exercises/009-color-nontext-focus-proof.svg`; `product-design/exercises/009-color-nontext-focus-proof-critique.md`; `product-design/exercises/010-srgb-linear-xyz-practice.md`; `product-design/exercises/012-d65-d50-bradford-practice.md`; cross-context grayscale/state critique, representative text probes, measured non-text boundary, focus geometry, primary-source colorimetry foundation, encoded-sRGB → linear-light → XYZ bridge, LMS/observer-model foundation, and D65↔D50 chromatic-adaptation practice complete; official spectral integration/observer comparison, broader CAT comparison, ICC-tool validation, and physical-display bright/low-light/interactive-focus validation pending |
| Typography as information architecture | CRITIQUE | `research/009-typography-as-information-architecture.md`; `product-design/exercises/006-typography-information-architecture-practice.md`; `product-design/exercises/008-typography-enlarged-proof.svg`; `product-design/exercises/008-typography-enlarged-proof-critique.md`; three hypotheses, dense-table adaptation, distinction-removal critique, second-context transfer, and enlarged-text failure → revision cycle complete; real platform scaling/reflow validation pending |
| Type anatomy / metrics | PRACTICE | `research/001-type-as-system.md`; `research/002-metrics-spacing-optical-rhythm.md`; `type-design/exercises/001-ho-metrics-critique.md` |
| Stroke / contrast / construction | PRACTICE | `research/003-stroke-contrast-bezier-optics.md`; `type-design/exercises/002-construction-curve-optics.svg`; critique documents limits and required family extension |
| Bézier drawing discipline | PRACTICE | `research/003-stroke-contrast-bezier-optics.md`; `type-design/exercises/002-construction-curve-optics.svg`; `type-design/exercises/002-construction-curve-optics-critique.md`; real font-source/raster audit still required |
| Optical correction | PRACTICE | overshoot study in `research/002-metrics-spacing-optical-rhythm.md`; construction/optics practice in `research/003-stroke-contrast-bezier-optics.md` and Exercise 002; raster comparison pending |
| Spacing before kerning | PRACTICE | `research/002-metrics-spacing-optical-rhythm.md`; `type-design/exercises/001-ho-metrics-three-hypotheses.svg`; `type-design/exercises/001-ho-metrics-critique.md` |
| Numerals / punctuation | IN STUDY | `research/005-numerals-punctuation-systems.md`; `type-design/exercises/003-numeral-punctuation-system-brief.md`; native 0–9/punctuation drawing not yet complete |
| Interaction foundations | PRACTICE | `research/004-accessibility-reflow-targets-focus.md`; `research/007-interaction-agency-feedback-errors.md`; `product-design/exercises/004-interaction-state-matrix.md`; interactive/navigation proof pending |
| Accessibility foundations | PRACTICE | `research/004-accessibility-reflow-targets-focus.md`; `product-design/exercises/001-accessibility-geometry.svg`; `product-design/exercises/001-accessibility-geometry-critique.md`; static measured focus/non-text evidence added in Exercise 009; interactive/assistive-tech proof pending |
| Design history / precedent literacy | IN STUDY | modernist grid/New Typography and reaction precedent study in `research/006-grid-composition-hierarchy.md`; broader historical comparison still pending |

## Stage 2 — Intermediate

All modules: NOT STARTED.

## Stage 3 — Advanced

All modules: NOT STARTED.

## Stage 4 — Production / authorship

All modules: NOT STARTED.

## Completion rule

No global completion announcement until every stage gate in `curriculum/MASTER_CURRICULUM.md` is `PASS` with evidence links.

The first immediate objective is not to design a font or app. It is to complete Stage 1 with enough rigor that later design decisions are materially better than pre-study work.

## Immediate next study block

1. execute Study 010/011 spectral colorimetry practice with official CIE datasets: spectral integration → CIE 1931 XYZ/xy → spectrum scaling → same-spectrum observer comparison → metamerism evidence;
2. begin perceptual-colour-space study: CIELAB/CIELCh, colour-difference purpose/limits, and later CIEDE2000 before comparing with Oklab/OkLCh;
3. validate Exercise 012 through an actual ICC CMM/profile round trip and compare hand calculation vs managed conversion;
4. compare Bradford/CAT02/CAT16 only on an explicitly defined research dataset; do not convert the comparison into a production recommendation prematurely;
5. raster proof Exercise 002 at multiple sizes and record a failure → redraw cycle;
6. execute Exercise 003 numeral/punctuation brief with native outlines and ambiguity alternatives;
7. test Grid Exercise 007 with long/multilingual labels and enlarged text in an actual rendering environment;
8. validate Color Exercise 009 on physical displays under controlled bright/low-light conditions and with interactive keyboard focus;
9. validate Typography Exercise 008 with real platform text scaling/reflow and localized long labels;
10. extend interaction work into a navigation-model prototype and keyboard/status-message validation.
