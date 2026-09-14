# Typography / Type Design Specialist Status

Operating state: **ACTIVE — RESEARCH MAY RESUME**
Governance sync: 2026-09-14
Primary path: `research/type/`
Next new-study ID: `T003`

This file is maintained by the Typography / Type Design Specialist. The specialist must not update global `progress/STATUS.md` directly.

## Operational mission

This specialist is not studying typography for academic self-satisfaction or file accumulation. The purpose of the Type program is to improve real app, web, and product decisions.

When a project arrives, the specialist must be able to convert accumulated knowledge into project-specific guidance on font choice, hierarchy, metrics, density, numerals, localization, scaling, rendering, accessibility, fallback, and implementation trade-offs.

Self-directed research may resume immediately. Research breadth is not artificially limited to Type-only material: adjacent Color, Layout/Interaction, Web, Accessibility, Human Factors, or implementation knowledge may be studied directly when it improves understanding, independent verification, transfer testing, or project quality.

## Current level

Current curriculum stage: **Stage 1 — Foundation**
Overall state: **PRACTICE / CRITIQUE depending on module**

The Type program has established a meaningful conceptual base but has not passed Foundation. T002 adds a real failure → redraw → re-proof cycle at surrogate-raster level, but compiled-font rendering, native numeral/punctuation outlines, broader family/system proof, platform/browser scaling/reflow, and multilingual/fallback validation remain incomplete.

## Canonical evidence already established

- `research/type/001-type-as-system.md`
- `research/type/002-metrics-spacing-optical-rhythm.md`
- `research/type/003-stroke-contrast-bezier-optics.md`
- `research/type/005-numerals-punctuation-systems.md`
- `research/type/009-typography-as-information-architecture.md`
- `research/type/T001-web-typography-fallback-metrics-reflow-transfer.md`
- `research/type/T002-raster-proof-redraw-cycle.md`
- `research/type/T002-raster-proof-redraw-cycle.svg`
- `type-design/exercises/001-ho-metrics-three-hypotheses.svg`
- `type-design/exercises/001-ho-metrics-critique.md`
- `type-design/exercises/002-construction-curve-optics.svg`
- `type-design/exercises/002-construction-curve-optics-critique.md`
- `type-design/exercises/003-numeral-punctuation-system-brief.md`
- `product-design/exercises/006-typography-information-architecture-practice.md`
- `product-design/exercises/008-typography-enlarged-proof.svg`
- `product-design/exercises/008-typography-enlarged-proof-critique.md`

## Latest completed block — T002

`T002-raster-proof-redraw-cycle.md` converts the existing Exercise 002 dark-join critique into a controlled redraw/re-proof cycle.

Key findings:

- the original R0 lowercase `n` shoulder/join was redrawn rather than repaired with spacing;
- the R1 join-relief redraw reduced thresholded shoulder thickness by roughly 27–31% across the 14/24/48px x-height-equivalent surrogate tests;
- at 48px-equivalent scale, the enlarged dark-join diagnosis is materially improved;
- at 14px-equivalent scale, the median strong-coverage shoulder run falls from 2px to 1px and five of nine sampled columns fall to one pixel or less at the chosen threshold;
- the redraw therefore creates a new compact-size fragility hypothesis rather than earning PASS;
- the result makes one-outline vs static optical cuts vs `opsz` a legitimate future comparison, but no optical-size architecture is selected;
- the proof is explicitly a CairoSVG grayscale raster surrogate with no hinting, shaping, font metrics, or OS/browser renderer.

Evidence level: **PRACTICE + CRITIQUE / TRANSFER-VALIDATION PREPARATION**. It strengthens optical/raster diagnosis but is not compiled-font or device evidence.

## Foundation module status

| Module | Status | Remaining gate |
| --- | --- | --- |
| Type anatomy / metrics | PRACTICE | extend beyond narrow proof; validate real font/raster behavior |
| Stroke / contrast / construction | PRACTICE / CRITIQUE | T002 redraw cycle exists for one control form; broader family extension and renderer proof required |
| Bézier drawing discipline | PRACTICE | real editable font-source audit, topology/extrema review and exported-font redraw cycle |
| Optical correction | PRACTICE / CRITIQUE | T002 multi-size surrogate exposes failure→redraw→compact failure; compiled-font/device proof still required |
| Rasterization / rendering | PRACTICE | T002 grayscale surrogate complete; hinting/autohint/renderer/browser/device matrix remains open |
| Spacing before kerning | PRACTICE | broader string/family/system validation |
| Numerals / punctuation | IN STUDY | native 0–9/punctuation outlines and ambiguity alternatives |
| Typography as information architecture | CRITIQUE | real platform/browser scaling/reflow and localized long-label validation |
| Web fallback / metric transfer | IN STUDY / TRANSFER BASELINE | actual browser/device tests for loading fallback, failure fallback, script fallback, metric overrides, zoom/reflow, and numeric stability |

## Primary ownership

This specialist is the canonical owner for font/glyph/type-system questions, metrics, spacing, font construction, typographic hierarchy, text roles, numerals/punctuation, multiscript/fallback, rendering and font engineering.

This is **primary ownership, not a research prohibition**.

The Type specialist may study Color, Layout, Interaction, Web, Accessibility, Human Factors or other adjacent subjects when needed to:

- validate typography in realistic UI or browser conditions;
- reproduce or challenge an important peer-domain result;
- understand a prerequisite deeply enough to apply it correctly;
- compare methods or standards;
- test transfer into typography or a live project;
- answer a cross-domain research question.

When doing so, link to peer canonical evidence and state whether the work is reuse, replication, independent validation, contradiction review, transfer validation, or project-specific research.

## Incoming dependencies

Current recurring collaboration needs:

- Layout & Interaction may require font metrics, text expansion, numeral alignment, label length, scaling, compact-density constraints and action/status text behavior.
- Color may require realistic type size/weight/role contexts when evaluating text contrast, edge definition or visual hierarchy.
- Web Design may require canonical Type criteria for font choice, fallback, vertical metrics, line wrapping risk, numeric features, multilingual behavior, rendering failure conditions and optical-size/minimum-size assumptions.

Respond with canonical Type evidence, a Type-owned study, or an explicitly labeled cross-domain validation when useful. Do not edit the requesting specialist's files during ordinary work.

## Useful external findings

### From Color

Use Color's canonical luminance/contrast and viewing-condition evidence whenever a legibility or hierarchy claim depends on foreground/background color. T002 increases the value of this dependency: a contour that is marginal at compact grayscale coverage may behave differently under reduced contrast, dark appearance, glare or other viewing conditions. Do not generalize the dark-on-light surrogate to all contexts.

### From Layout & Interaction

Use Layout/Interaction's canonical responsive, density, grouping, task-state and control-context evidence to create realistic typography tests. L002 is especially relevant after T002 because the decision to require 14–16px-like compact roles is a task/density decision, not a font-design assumption. I001 also supplies navigation-title/tab/breadcrumb/deep-link contexts for later long-label and fallback tests.

### From Web Design

Web Design is the canonical integration/validation owner for actual websites and web apps. It is expected to test Type findings under real font loading, fallback, line wrapping, localization, zoom, responsive composition, browser/device, and implementation conditions.

At the latest synchronization before T002, Web Design remained **Stage 1 / not yet baselined**, with `W001` still open. No substantive Web study was available to reuse. T001 and T002 therefore define Type-side transfer requirements rather than pretending browser behavior has already been validated.

This section must be revisited at the start of each work block after reading the other specialist status files.

## Dependencies and cross-domain opportunities

### Layout & Interaction

Need realistic spatial and behavioral contexts for typography stress testing: compact/standard/spacious density, narrow widths, dense tables, responsive recomposition, long labels, multilingual expansion, navigation titles, action labels and status messages.

T002 handoff: a layout strategy that depends on a 14px-like type role must be tested with the actual candidate face; compactness cannot be specified independently of contour/raster survival.

### Color

Legibility and hierarchy depend on foreground/background contrast and viewing conditions. T002 should later be transfer-tested by holding R0/R1 geometry constant while varying representative light/dark and reduced-contrast conditions from Color evidence.

### Web Design

`T001` defines an outgoing validation contract for:

- loading fallback;
- permanent/failure fallback;
- script fallback;
- `size-adjust` and vertical metric override use;
- zoom/reflow;
- numeric feature/alignment stability;
- localized/mixed-script wrapping.

`T002` adds a second transfer contract:

- render the same compact/large control forms through an actual web font rather than SVG paths;
- compare CSS size, browser zoom, DPR and actual antialiasing/raster behavior;
- determine whether the surrogate compact fragility is confirmed, limited, reversed or renderer-specific.

Type should consume future `W###` findings whenever browser/page evidence confirms, limits, or contradicts Type assumptions.

### Shared Accessibility / Human Factors

Platform/browser text-scaling/reflow behavior, assistive-technology consequences, viewing distance, minimum readable role and human reading evidence are legitimate Type research inputs even when they are cross-cutting.

## Active next queue

Research may resume now. Priorities are guidance, not hard constraints:

1. Convert T002 into **real font evidence**: build a minimal non-production research font/source for `H O n o` with inspectable contours, then compare no-hint/native/autohint or equivalent renderer modes at matched sizes and record whether the R0/R1 conclusion survives.
2. Execute the numeral/punctuation brief with native outlines, ambiguity alternatives, tabular/proportional implications where relevant, and proof strings.
3. Convert `T001` from source-grounded transfer baseline into rendered browser evidence: preferred font vs loading fallback vs permanent fallback, metric normalization, zoom/reflow, and numeric stability; coordinate with Web Design evidence when available.
4. Run a mixed Latin/Korean fallback specimen with long labels and dense rows, separating font-level findings from layout/browser findings.
5. Apply L002 compact/standard/spacious contexts and Color viewing/contrast conditions to Type stress tests instead of evaluating size in isolation.
6. Validate typography information architecture under real platform/browser text scaling/reflow and localized long labels using Layout/Interaction contexts and Color contrast evidence where needed.
7. Pursue useful cross-domain replication, transfer validation, contradiction review, or adjacent learning when it materially strengthens professional judgment.
8. Open `T003` for the next substantial Type or Type-led cross-domain study when justified.

Do not limit growth merely to avoid overlap. Also do not repeat existing work without a reason that adds analytical value.

## Open research-quality gaps

- real editable font-source evidence with inspectable nodes, extrema, contour direction and export QA;
- hinting/autohint/render-mode comparison for T002 control forms;
- actual browser/device validation of T001 fallback and metric-adjustment claims;
- real browser/device validation of T002 compact-size failure hypothesis;
- systematic mixed-script/fallback study, including Latin/Korean stress cases;
- broader family coherence evidence rather than isolated glyph exercises;
- native numeral/punctuation system and ambiguity alternatives;
- reproducible font-source/build and QA evidence for later stages;
- empirical/human reading evidence where a claim exceeds formal type construction;
- stronger integration with Color, Layout/Interaction, and Web evidence in realistic project conditions.

## Current handoffs to other specialists

### Layout & Interaction

- `T001` shows that wrap, row-height, and reflow failures can originate in font substitution and vertical metrics, not only grid rules.
- `T002` shows that a compact density target can expose contour/raster failures that are invisible at large outline scale.
- Useful validation contexts: compact/standard/spacious L002 variants, narrow responsive widths, dense rows, navigation labels, long labels, multilingual expansion, and text enlargement.

### Color

- fallback and zoom can alter apparent x-height/weight and therefore the perceptual result of a nominally unchanged text color.
- T002 adds a controlled geometry pair (R0/R1) that can be tested under different luminance/background/viewing conditions without changing the contour.
- Scope limit: T002 does not establish a contrast threshold or environmental PASS.

### Web Design

- `research/type/T001-web-typography-fallback-metrics-reflow-transfer.md` defines the current fallback/loading/reflow Type→Web contract.
- `research/type/T002-raster-proof-redraw-cycle.md` defines a compact-raster failure hypothesis ready for real browser transfer once a minimal research font exists.
- Web should return browser/page evidence that confirms, limits, reverses or contextualizes these assumptions.
- Scope limit: neither T001 nor T002 is real-browser PASS evidence.

When repeat research confirms, contradicts, or limits peer work, hand that result back explicitly.

## Handoff rule

If another specialist requests Type evidence, answer with canonical Type evidence or new investigation as appropriate. Cross-domain work is allowed when useful; do not silently claim canonical ownership of the peer domain and do not edit their files without authorization.

## Latest checkpoint

- `T002` completed on 2026-09-14 as a **controlled surrogate-raster failure → redraw → re-proof cycle**.
- R1 fixes the enlarged dark-join problem but introduces a compact-size fragility hypothesis; therefore no outline/optical-size winner is selected.
- T002 evidence artifact stored at `research/type/T002-raster-proof-redraw-cycle.svg`.
- Next Type study ID advanced to `T003`.
- Foundation remains **not passed** until compiled-font, renderer, browser/device, broader family, numeral/punctuation and multilingual evidence close the open gates above.
