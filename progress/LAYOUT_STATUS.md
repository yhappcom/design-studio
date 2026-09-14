# Layout, Spatial & Interaction Specialist Status

Operating state: **ACTIVE — RESEARCH MAY RESUME**
Governance sync: 2026-09-14
Canonical paths: `research/layout/`, `research/interaction/`
Next new-study IDs: Layout `L003`; Interaction `I002`

This file is maintained by the Layout, Spatial & Interaction Specialist. The specialist must not update global `progress/STATUS.md` directly.

## Operational mission

This specialist is not studying layout or interaction for academic self-satisfaction or file accumulation. The purpose of the program is to improve real app, web and product decisions.

When a project arrives, the specialist must be able to convert accumulated knowledge into project-specific guidance on information/spatial hierarchy, grouping, density, responsive behavior, navigation, state, feedback, errors/recovery, target placement, accessibility, implementation trade-offs, validation strategy and failure conditions.

Self-directed research may resume immediately. Research breadth is not artificially limited to Layout/Interaction-only material: adjacent Type, Color, Web Design, Accessibility, Human Factors or implementation knowledge may be studied directly when it improves understanding, independent verification, transfer testing, or project quality.

## Current level

Current curriculum stage: **Stage 1 — Foundation**
Overall state: **CRITIQUE** in studied spatial and interaction modules, with Foundation validation breadth still incomplete.

The role combines spatial composition and interaction because screen geometry, state, navigation, feedback, target placement and responsive behavior must ultimately form one coherent product experience. The two evidence streams remain separately indexed under `research/layout/` and `research/interaction/` so spatial and temporal/behavioral claims are not conflated.

## Four-specialist collaboration sync

The Design Studio operates with four official peer specialists:

1. Typography / Type Design
2. Color
3. Layout, Spatial & Interaction
4. Web Design

Web Design is not a downstream implementation service. It is an independent design specialist and a major application/validation partner for this role.

Layout/Interaction provides canonical spatial and behavioral evidence. Web Design integrates that evidence into complete websites/web apps and stress-tests it under actual page architecture, intrinsic sizing, responsive reflow, browser-native controls, mouse/trackpad/keyboard/touch input, browser history, loading/network behavior, localization, zoom, text enlargement and real content conditions.

When Web evidence confirms, limits, contradicts or changes a Layout/Interaction conclusion, that result should be treated as transfer/implementation evidence and fed back into future Layout/Interaction research rather than ignored as an implementation anomaly.

No substantive `W###` study was listed at the latest synchronization point. `progress/WEB_STATUS.md` and `research/web/README.md` establish the role and expected validation interface; future work blocks must check for new Web evidence before starting substantial research.

## Canonical evidence already established

### Layout / spatial

- `research/layout/006-grid-composition-hierarchy.md`
- `research/layout/014-perceptual-grouping-spatial-grammar.md`
- `research/layout/L001-figure-ground-balance-optical-centering.md`
- `research/layout/L002-whitespace-density-spatial-rhythm.md`
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
- `research/interaction/I001-navigation-history-focus-restoration-interruption.md`
- `product-design/exercises/004-interaction-state-matrix.md`
- `product-design/exercises/015-directness-state-coupling-practice.md`
- `product-design/exercises/015-directness-state-coupling-critique.md`

### Shared accessibility evidence relevant to this role

- `research/004-accessibility-reflow-targets-focus.md`
- `product-design/exercises/001-accessibility-geometry.svg`
- `product-design/exercises/001-accessibility-geometry-critique.md`

## Latest completed block — I001

`I001-navigation-history-focus-restoration-interruption.md` establishes a project-facing navigation-state model instead of treating navigation as menus, arrows, or transition animation.

Key additions:

- separates semantic location, traversal history, hierarchy, task/work state, presentation state, focus/selection state, transient-layer state and data/commitment state;
- distinguishes Back/history traversal, Up/hierarchy traversal, Close/dismissal, top-level switching and Home/start rather than collapsing them into generic “back” behavior;
- makes deep-link/context-poor entry a required navigation test;
- defines a focus-restoration contract for entry, dismissal and removed invokers;
- integrates interruption/resumption evidence and warns that immediate resume is not always safest for high-cost tasks;
- treats state restoration as a validity/safety policy, not a technical default;
- extends Study 015's commitment model into unsaved-work navigation decisions;
- defines a reusable navigation-state contract and controlled validation scenarios for list/detail/edit/modal, deep links, top-level switching, async interruption and keyboard/assistive-technology traversal.

Evidence level: source-grounded Foundation study and project-decision framework. No PASS or CRITIQUE promotion is claimed from I001 alone because running multi-input history/focus behavior, deep-link tests, browser/platform behavior, async recovery and observed resumption evidence remain open.

## Previous completed block — L002

`L002-whitespace-density-spatial-rhythm.md` established a project-facing density model rather than a universal “more whitespace is better” rule.

Key additions:

- separates information density, visual density, interaction density, and navigation/temporal density;
- treats whitespace as a structural resource with explicit jobs rather than a premium aesthetic default;
- distinguishes local from global density and element count from perceptual clutter;
- records evidence that sparse regions may attract search first while not always producing the fastest target extraction;
- frames compact, standard-adaptive, and spacious strategies as task-dependent alternatives;
- explicitly prices progressive disclosure as an exchange of spatial density for interaction/navigation cost;
- defines project inputs, failure modes, stress variants, task metrics, and peer dependencies required before density recommendations are generalized.

Evidence level: source-grounded Foundation study and project-decision framework. No PASS or CRITIQUE promotion is claimed from this note alone because controlled rendered variants, task measures, localization/zoom stress and human observation remain open.

## Foundation module status

| Module | Status | Remaining gate |
| --- | --- | --- |
| Composition / visual grammar | CRITIQUE | rendered human observation, multilingual/enlarged-text/browser transfer |
| Grid / alignment systems | CRITIQUE | real-browser proof, text-growth stress testing, broader responsive transfer |
| Perceptual grouping | CRITIQUE | broader context validation and human observation |
| Figure-ground / border ownership | PRACTICE / CRITIQUE | cue-isolated variants, realistic layering, blinded human comparison |
| Visual mass / balance / tension | PRACTICE / CRITIQUE | exact controlled centroid dataset, observer ratings, broader context transfer |
| Optical centering | PRACTICE / CRITIQUE | intended-size raster/device proof, blinded candidate comparison, RTL/text-context transfer |
| Whitespace / density / spatial rhythm | IN STUDY | L002 source/project framework complete; controlled rendered density variants, task-performance evidence, multilingual/zoom/browser transfer and human validation pending |
| Responsive/adaptive recomposition | PRACTICE / CRITIQUE | real content, multilingual labels, enlarged text and browser/device proof |
| Interaction agency / feedback / errors | CRITIQUE | running behavior proof and broader recovery validation |
| State / modes / reversibility / directness | CRITIQUE | running prototype, keyboard/focus execution, async failure-and-recovery proof |
| Navigation / task-flow integration | IN STUDY | I001 source/project framework complete; running history/focus/deep-link/multi-stack prototype, interruption recovery evidence and real platform/browser validation pending |

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

The Layout/Interaction specialist may study Type, Color, Web Design, Accessibility, Human Factors, frontend/browser behavior or other adjacent subjects when needed to validate spatial or interaction behavior, reproduce or challenge peer evidence, understand prerequisites, compare methods, test transfer, or answer a cross-domain question.

When doing so, link to peer canonical evidence and state whether the work is reuse, replication, independent validation, contradiction review, transfer validation, implementation validation, or project-specific research.

## Incoming dependencies

Current known recurring needs:

- Type needs realistic responsive/dense spatial contexts for text-growth, long-label and scaling stress tests.
- Color needs realistic surfaces, navigation/current-location states, focus contexts and interaction flows for hierarchy, status and environmental validation.
- Web Design needs canonical Layout/Interaction evidence for grouping, hierarchy, density, responsive logic, navigation, history, focus restoration, state, feedback, recovery, target geometry and input behavior when designing actual websites/web apps.

These are collaboration opportunities, not permission to edit the other specialists' files during ordinary work.

## Useful external findings

### From Type

Use canonical Type evidence for font metrics, line wrapping, numerals, localized labels, text scaling and typographic hierarchy whenever those affect geometry or control labels. L001 reuses Type's distinction between measurable geometry and optical judgment. L002 confirms that density decisions must use real text metrics rather than placeholder geometry.

`T001` adds a direct navigation dependency: fallback/vertical metrics can change wrapping, row height, navigation label width and control geometry. I001 therefore treats Type failure as a possible cause of navigation/reflow breakage rather than automatically diagnosing every failure as Layout.

### From Color

Use canonical Color evidence for luminance, contrast, focus/state color, color-vision independence and gamut/device behavior whenever interaction feedback or spatial hierarchy depends on color. L001 deliberately held hue out of the first proof; L002 warns that apparent visual density can be a contrast/feature-variability problem rather than an element-count problem.

`C001` adds a navigation-state constraint: forced-colors can remove or replace authored fill, shadow, border and SVG color channels, so I001 requires current location, selection and focus meaning to survive without color-only encoding.

### From Web Design

Current reusable finding is structural rather than empirical: Web Design is the canonical owner of complete web page/system application and actual browser/device validation. Future Layout/Interaction work intended for web deployment must check `research/web/` for evidence from intrinsic sizing, responsive browser reflow, native controls, keyboard/focus/pointer/touch behavior, browser history, loading/network states, localization, zoom, content expansion and design-to-code fidelity.

At the latest synchronization point there was still no substantive `W###` result to import. Do not invent Web evidence. Re-check `progress/WEB_STATUS.md` and `research/web/` before every substantial block.

## Dependencies and cross-domain opportunities

### Type

Responsive and dense layouts require real font metrics, text growth, line wrapping, numeral alignment, localized labels and enlarged text. L001's optical-centering protocol should later be tested next to real Latin/Korean/RTL labels rather than only standalone shapes. L002 should use Type evidence to compare compact data rows against spacious explanatory surfaces without changing text quality accidentally.

I001 specifically needs Type transfer tests for navigation titles, tabs, breadcrumbs, hierarchical labels and route controls under fallback font, mixed Latin/Korean, long localization and text enlargement.

### Color

State cues, focus indicators, hierarchy and environment-sensitive feedback depend on contrast, luminance, gamut and semantic-color behavior. A useful Layout transfer test is whether luminance/chroma changes perceived visual mass, clutter or border ownership while geometry remains fixed.

I001 specifically needs Color transfer tests showing that current-location, selected-navigation and focus cues remain distinguishable under forced-colors, grayscale and theme substitution.

### Web Design

High-value Web transfer targets from existing work:

1. `006` / Exercise 007 — test whether semantic alignment and responsive recomposition survive real CSS intrinsic sizing, actual font metrics, localization, browser zoom and narrow content containers.
2. `014` — test proximity/common-region/connectedness and over-containerization inside real page/component systems rather than isolated SVG composition.
3. `L001` — test border ownership, visual mass and optical centering at intended browser/device sizes while keeping semantic/hit geometry stable.
4. `L002` — compare compact/intermediate/spacious density strategies on real dashboards, forms, settings, lists and tables; measure task performance separately from preference.
5. `015` — implement directness/state/mode/reversibility in a real web interaction with browser focus, pointer + keyboard equivalence, pending network state and failure recovery.
6. `I001` — test browser Back/Forward, push/replace/traverse behavior, deep-link entry, modal Close/Escape, route focus placement/restoration, scroll/filter restoration, independent top-level work areas and interruption during pending async work.
7. Accessibility geometry — verify target/focus behavior with browser-native semantics rather than static geometry alone.

Web findings should be classified as confirmation, limitation, contradiction or transfer failure. A browser constraint is not automatically a reason to weaken the canonical Layout/Interaction principle; determine whether the principle, implementation technique, platform convention or project-specific application failed.

### Shared Accessibility / human factors

Target geometry, input modality equivalence, focus behavior, motion, cognitive load and assistive-technology consequences are legitimate research inputs. L001 separates visual-child offsets from hit/semantic geometry; L002 requires objective task measures where density claims affect search/comparison/activation risk; I001 adds focus restoration, current-location orientation, interruption/resumption and deep-link context as explicit human-factors concerns.

## Active next queue

Research may resume now. Priorities are guidance, not hard constraints:

1. Build a running Interaction validation specimen combining Study 015 + I001: list → detail → edit → modal, deep-link entry, top-level switch, Back/Up/Close semantics, focus restoration, pending async work and at least one failure/recovery path.
2. Validate the specimen with keyboard/focus/status-message behavior and at least one interruption/resumption scenario; separate speed, correctness, focus-loss events and subjective orientation.
3. Convert L002 from source/project framework into controlled practice: matched-content compact/intermediate/spacious variants; known-item search and comparison tasks; separate subjective preference from objective performance; include localized/enlarged-text and narrow-container stress.
4. Convert L001 into stronger evidence: exact centroid-controlled variants, cue-isolated border-ownership comparisons, intended-size raster proofs, and blinded human judgments before considering PASS.
5. Test existing responsive/grid work in a real rendering environment with long labels, multilingual expansion and enlarged text using Type evidence; for web conditions, use Web Design results or an explicitly Layout-owned transfer-validation experiment rather than assuming browser behavior.
6. Use future Web `W###` findings to stress-test responsive composition, density, browser-native interaction, history/focus and real-content assumptions; independently reproduce Web findings when the Layout/Interaction claim is high-risk or foundational.
7. Pursue useful Type/Color/Web replication, transfer validation, contradiction review, or adjacent learning when it materially strengthens professional judgment.
8. Open `L003` or `I002` for the next substantial new research question after current validation work, or earlier if a live project/dependency has higher value.

Do not limit growth merely to avoid overlap. Also do not repeat existing work without a reason that adds analytical value.

## Open research-quality gaps

- controlled human-observation evidence for grouping, figure-ground, balance and optical-centering claims;
- real rendered/device validation of optical corrections;
- controlled density variants with objective task evidence and preference/performance separation;
- responsive transfer under multilingual, enlarged-text and dense-data conditions;
- cross-surface systems across phone/tablet/desktop;
- complete web-context transfer under intrinsic sizing, zoom, localization and real browser reflow;
- running navigation/state prototype with explicit Back/Up/Close, history, deep-link and top-level-stack behavior;
- keyboard focus placement/restoration and assistive-technology validation across route/modal changes;
- browser history/native-control implications where interaction semantics depend on the web platform;
- interruption/resumption evidence on representative product tasks;
- async failure, interruption and recovery evidence;
- integration of spatial and temporal hierarchy without collapsing them into one concept;
- stronger cross-validation with real Type, Color and Web behavior.

## Handoffs to other specialists

### Typography / Type

- L001 geometric-center vs perceived-center method may be useful for symbols/icons paired with text; validate in Type-specific contexts before importing offsets into font metrics.
- Responsive/grid studies can supply realistic narrow/dense/long-label contexts for text scaling, wrapping and numeral alignment validation.
- L002 adds explicit compact/standard/spacious density scenarios where Type can test line height, wrapping, numeral alignment and localization without treating typography independently of page geometry.
- I001 adds navigation titles/tabs/breadcrumbs/deep-link orientation as Type stress contexts; fallback and localization must not silently change the navigation model or hide current location.

### Color

- Hold L001 geometry constant and vary luminance/chroma to test whether perceived mass or ownership shifts.
- Interaction studies provide realistic focus/status/state contexts for semantic color validation.
- L002 adds a transfer test: hold geometry constant while varying luminance/chroma/feature variability to determine how much perceived clutter is color-driven versus spatial.
- I001 extends C001: current location, selected navigation and focus must remain semantically distinguishable when authored colors/shadows are replaced.

### Web Design

Existing Layout/Interaction work offers immediate browser-validation targets:

- responsive semantic alignment and recomposition from Study 006 / Exercise 007;
- grouping, containment and over-containerization from Study 014;
- border ownership, visual mass and optical centering from L001;
- density, whitespace, spatial rhythm and progressive-disclosure trade-offs from L002;
- directness, state, modes, reversibility and async recovery from Study 015;
- history/hierarchy, Back/Up/Close, deep links, focus restoration and interruption recovery from I001;
- target/focus geometry from shared accessibility evidence.

Requested feedback from Web: document actual browser/page conditions that confirm, limit, contradict or expose transfer failure in these findings, especially intrinsic sizing, localization, zoom, browser Back/Forward, route history, mixed input, native controls, modal focus restoration, history/scroll restoration, loading/network behavior and real content stress. For L002, separate task performance from visual preference. For I001, distinguish product hierarchy from browser traversal history rather than forcing them to match.

### Layout / Interaction

Internal rule: Web implementation evidence does not replace spatial/interaction theory automatically. When Web returns a failure, classify whether it exposes a theory limit, platform convention, context dependency, implementation mismatch or project-specific error before revising canonical guidance.

## Handoff rule

If another specialist requests Layout/Interaction evidence, answer with canonical evidence or new investigation as appropriate. Cross-domain work is allowed when useful; do not silently claim canonical ownership of the peer domain and do not edit their files without authorization.

## Latest checkpoint

- `I001` completed as a source-grounded **navigation/history/focus/restoration/interruption** Foundation framework on 2026-09-14.
- Interaction next new-study ID advanced to `I002`.
- No PASS promotion claimed; the next high-value step is a running validation specimen that combines Study 015 and I001.
