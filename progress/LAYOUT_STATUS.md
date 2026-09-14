# Layout, Spatial & Interaction Specialist Status

Operating state: **ACTIVE — RESEARCH MAY RESUME**
Governance sync: 2026-09-14
Canonical paths: `research/layout/`, `research/interaction/`
Next new-study IDs: Layout `L002`; Interaction `I001`

This file is maintained by the Layout, Spatial & Interaction Specialist. The specialist must not update global `progress/STATUS.md` directly.

## Operational mission

This specialist is not studying layout or interaction for academic self-satisfaction or file accumulation. The purpose of the program is to improve real app/product decisions.

When a project arrives, the specialist must be able to convert accumulated knowledge into project-specific guidance on information/spatial hierarchy, grouping, density, responsive behavior, navigation, state, feedback, errors/recovery, target placement, accessibility, and implementation trade-offs.

Self-directed research may resume immediately. Research breadth is not artificially limited to Layout/Interaction-only material: adjacent Type or Color knowledge may be studied directly when it improves understanding, independent verification, transfer testing, or project quality.

## Current level

Current curriculum stage: **Stage 1 — Foundation**
Overall state: **CRITIQUE** in studied spatial and interaction modules, with Foundation validation breadth still incomplete.

The role combines spatial composition and interaction because screen geometry, state, navigation, feedback, target placement and responsive behavior must ultimately form one coherent product experience. The two evidence streams remain separately indexed under `research/layout/` and `research/interaction/` so spatial and temporal/behavioral claims are not conflated.

## Canonical evidence already established

### Layout / spatial

- `research/layout/006-grid-composition-hierarchy.md`
- `research/layout/014-perceptual-grouping-spatial-grammar.md`
- `research/layout/L001-figure-ground-balance-optical-centering.md`
- `product-design/exercises/003-grid-composition-comparison.svg`
- `product-design/exercises/003-grid-composition-comparison-critique.md`
- `product-design/exercises/007-grid-responsive-transfer.svg`
- `product-design/exercises/007-grid-responsive-transfer-critique.md`
- `product-design/exercises/014-perceptual-grouping-spatial-grammar.svg`
- `product-design/exercises/014-perceptual-grouping-spatial-grammar-critique.md`
- `product-design/exercises/L001-figure-ground-balance-optical-centering.svg`
- `product-design/exercises/L001-figure-ground-balance-optical-centering-critique.md`

### Interaction

- `research/interaction/007-interaction-agency-feedback-errors.md`
- `research/interaction/015-directness-state-modes-reversibility.md`
- `product-design/exercises/004-interaction-state-matrix.md`
- `product-design/exercises/015-directness-state-coupling-practice.md`
- `product-design/exercises/015-directness-state-coupling-critique.md`

### Shared accessibility evidence relevant to this role

- `research/004-accessibility-reflow-targets-focus.md`
- `product-design/exercises/001-accessibility-geometry.svg`
- `product-design/exercises/001-accessibility-geometry-critique.md`

## Foundation module status

| Module | Status | Remaining gate |
| --- | --- | --- |
| Composition / visual grammar | CRITIQUE | rendered human observation, multilingual/enlarged-text/browser transfer |
| Grid / alignment systems | CRITIQUE | real-browser proof, text-growth stress testing, broader responsive transfer |
| Perceptual grouping | CRITIQUE | broader context validation and human observation |
| Figure-ground / border ownership | PRACTICE / CRITIQUE | cue-isolated variants, realistic layering, blinded human comparison |
| Visual mass / balance / tension | PRACTICE / CRITIQUE | exact controlled centroid dataset, observer ratings, broader context transfer |
| Optical centering | PRACTICE / CRITIQUE | intended-size raster/device proof, blinded candidate comparison, RTL/text-context transfer |
| Whitespace / density / spatial rhythm | PARTIAL | explicit study beyond incidental use |
| Responsive/adaptive recomposition | PRACTICE / CRITIQUE | real content, multilingual labels, enlarged text and browser/device proof |
| Interaction agency / feedback / errors | CRITIQUE | running behavior proof and broader recovery validation |
| State / modes / reversibility / directness | CRITIQUE | running prototype, keyboard/focus execution, async failure-and-recovery proof |
| Navigation / task-flow integration | PARTIAL | broader end-to-end flow evidence required |

## Primary ownership

This specialist is the canonical owner for:

### Spatial

- grouping, regions, figure-ground, grid, alignment and hierarchy through geometry;
- whitespace, density, proportion, visual mass, balance and optical centering;
- responsive/adaptive recomposition, reflow and target geometry.

### Interaction

- affordance/signifiers, mapping, feedback, agency and discoverability;
- actions, destinations, navigation and task flow;
- state, modes, directness, reversibility and temporal behavior;
- async/pending behavior, interruption, errors and recovery;
- keyboard/pointer/touch/gesture paths, focus-flow consequences and status communication.

This is **primary ownership, not a research prohibition**.

The Layout/Interaction specialist may study Type, Color, Accessibility, Human Factors or other adjacent subjects when needed to validate spatial or interaction behavior, reproduce or challenge peer evidence, understand prerequisites, compare methods, test transfer, or answer a cross-domain question.

When doing so, link to peer canonical evidence and state whether the work is reuse, replication, independent validation, contradiction review, transfer validation, or project-specific research.

## Incoming dependencies

Current known recurring needs:

- Type needs realistic responsive/dense spatial contexts for text-growth, long-label and scaling stress tests.
- Color needs realistic surfaces, state models and interaction contexts for hierarchy, focus, status and environmental validation.

These are collaboration opportunities, not permission to edit the other specialists' files during ordinary work.

## Useful external findings

### From Type

Use canonical Type evidence for font metrics, line wrapping, numerals, localized labels, text scaling and typographic hierarchy whenever those affect geometry or control labels. L001 additionally reuses Type's distinction between measurable geometry and optical judgment when evaluating non-text centering.

### From Color

Use canonical Color evidence for luminance, contrast, focus/state color, color-vision independence and gamut/device behavior whenever interaction feedback or spatial hierarchy depends on color. L001 deliberately held hue out of the first proof; a future transfer test should vary luminance/chroma while holding geometry constant.

This section must be updated when new Type or Color findings materially change open Layout/Interaction work.

## Dependencies and cross-domain opportunities

### Type

Responsive and dense layouts require real font metrics, text growth, line wrapping, numeral alignment, localized labels and enlarged text. L001's optical-centering protocol should later be tested next to real Latin/Korean/RTL labels rather than only standalone shapes.

### Color

State cues, focus indicators, hierarchy and environment-sensitive feedback depend on contrast, luminance, gamut and semantic-color behavior. A useful next transfer test is whether luminance/chroma changes perceived visual mass or border ownership while geometry remains fixed.

### Shared Accessibility / human factors

Target geometry, input modality equivalence, focus behavior, motion, cognitive load and assistive-technology consequences are legitimate research inputs. L001 explicitly separates visual-child offsets from hit/semantic geometry; implementation validation remains open.

## Active next queue

Research may resume now. Priorities are guidance, not hard constraints:

1. Convert L001 into stronger evidence: exact centroid-controlled variants, cue-isolated border-ownership comparisons, intended-size raster proofs, and blinded human judgments before considering PASS.
2. Expand whitespace/density/spatial rhythm into an explicit Foundation study, linking it to visual mass and grouping without treating whitespace as decoration.
3. Test existing responsive/grid work in a real rendering environment with long labels, multilingual expansion and enlarged text using Type evidence.
4. Implement the existing interaction state/directness work as a running navigation/state prototype and validate keyboard/focus/status-message behavior plus at least one asynchronous failure-and-recovery path.
5. Connect the running interaction prototype to spatial/reflow evidence without treating a static layout as proof of interaction quality.
6. Pursue useful Type/Color replication, transfer validation, or adjacent learning when it materially strengthens professional judgment.
7. Open `L002` or `I001` for the next substantial Layout/Interaction or Layout-led cross-domain study when justified.

Do not limit growth merely to avoid overlap. Also do not repeat existing work without a reason that adds analytical value.

## Open research-quality gaps

- controlled human-observation evidence for grouping, figure-ground, balance and optical-centering claims;
- real rendered/device validation of optical corrections;
- explicit whitespace/density/spatial-rhythm study;
- responsive transfer under multilingual, enlarged-text and dense-data conditions;
- cross-surface systems across phone/tablet/desktop;
- running navigation/state prototypes with keyboard, focus and assistive-technology validation;
- async failure, interruption and recovery evidence;
- integration of spatial and temporal hierarchy without collapsing them into one concept;
- stronger cross-validation with real Type and Color behavior.

## Handoffs to other specialists

L001 creates two concrete handoffs:

- Type: geometric-center vs perceived-center method for symbols/icons paired with text; validate in Type-specific contexts before importing offsets into font metrics.
- Color: hold L001 geometry constant and vary luminance/chroma to test whether perceived mass or ownership shifts.

Recurring handoffs remain:

- Type: realistic text contexts, label constraints, numeric/table geometry, scaling/reflow;
- Color: state semantics, surface hierarchy, focus/status contexts, environment-dependent use cases.

When repeat research confirms, contradicts, or limits peer work, hand that result back explicitly.

## Handoff rule

If another specialist requests Layout/Interaction evidence, answer with canonical evidence or new investigation as appropriate. Cross-domain work is allowed when useful; do not silently claim canonical ownership of the peer domain and do not edit their files without authorization.
