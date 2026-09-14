# Typography / Type Design Specialist Status

Operating state: **ACTIVE — RESEARCH MAY RESUME**
Governance sync: 2026-09-14
Primary path: `research/type/`
Next new-study ID: `T002`

This file is maintained by the Typography / Type Design Specialist. The specialist must not update global `progress/STATUS.md` directly.

## Operational mission

This specialist is not studying typography for academic self-satisfaction or file accumulation. The purpose of the Type program is to improve real app, web, and product decisions.

When a project arrives, the specialist must be able to convert accumulated knowledge into project-specific guidance on font choice, hierarchy, metrics, density, numerals, localization, scaling, rendering, accessibility, fallback, and implementation trade-offs.

Self-directed research may resume immediately. Research breadth is not artificially limited to Type-only material: adjacent Color, Layout/Interaction, Web, Accessibility, Human Factors, or implementation knowledge may be studied directly when it improves understanding, independent verification, transfer testing, or project quality.

## Current level

Current curriculum stage: **Stage 1 — Foundation**
Overall state: **PRACTICE / CRITIQUE depending on module**

The Type program has established a meaningful conceptual base but has not passed Foundation. Real rendering, native outline work, platform/browser scaling/reflow proof, broader script/family validation, and repeated failure→revision evidence remain incomplete.

## Canonical evidence already established

- `research/type/001-type-as-system.md`
- `research/type/002-metrics-spacing-optical-rhythm.md`
- `research/type/003-stroke-contrast-bezier-optics.md`
- `research/type/005-numerals-punctuation-systems.md`
- `research/type/009-typography-as-information-architecture.md`
- `research/type/T001-web-typography-fallback-metrics-reflow-transfer.md`
- `type-design/exercises/001-ho-metrics-three-hypotheses.svg`
- `type-design/exercises/001-ho-metrics-critique.md`
- `type-design/exercises/002-construction-curve-optics.svg`
- `type-design/exercises/002-construction-curve-optics-critique.md`
- `type-design/exercises/003-numeral-punctuation-system-brief.md`
- `product-design/exercises/006-typography-information-architecture-practice.md`
- `product-design/exercises/008-typography-enlarged-proof.svg`
- `product-design/exercises/008-typography-enlarged-proof-critique.md`

## Foundation module status

| Module | Status | Remaining gate |
| --- | --- | --- |
| Type anatomy / metrics | PRACTICE | extend beyond narrow proof; validate real font/raster behavior |
| Stroke / contrast / construction | PRACTICE | broader family extension and rendered comparison |
| Bézier drawing discipline | PRACTICE | real font-source/raster audit and redraw cycle |
| Optical correction | PRACTICE | multi-size raster comparison |
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

- Layout & Interaction may require font metrics, text expansion, numeral alignment, label length, scaling and action/status text behavior.
- Color may require realistic type size/weight/role contexts when evaluating text contrast or visual hierarchy.
- Web Design may require canonical Type criteria for font choice, fallback, vertical metrics, line wrapping risk, numeric features, multilingual behavior, and rendering failure conditions.

Respond with canonical Type evidence, a Type-owned study, or an explicitly labeled cross-domain validation when useful. Do not edit the requesting specialist's files during ordinary work.

## Useful external findings

### From Color

Use Color's canonical luminance/contrast and viewing-condition evidence whenever a legibility or hierarchy claim depends on foreground/background color. Independently reproduce or challenge high-impact calculations when confidence or project risk warrants it.

### From Layout & Interaction

Use Layout/Interaction's canonical responsive, density, grouping, task-state and control-context evidence to create realistic typography tests. Type may independently reproduce spatial or interaction conditions when the purpose is to test typographic behavior, but canonical ownership remains explicit.

### From Web Design

Web Design is now the official fourth specialist and the canonical integration/validation owner for actual websites and web apps. It is expected to test Type findings under real font loading, fallback, line wrapping, localization, zoom, responsive composition, browser/device, and implementation conditions.

At the latest synchronization, Web Design remains **Stage 1 / not yet baselined**, with `W001` still open. No substantive Web study was available to reuse yet. Type therefore created `T001` as a Type→Web transfer baseline rather than pretending browser behavior had already been validated.

This section must be revisited at the start of each work block after reading the other specialist status files.

## Dependencies and cross-domain opportunities

### Layout & Interaction

Need realistic spatial and behavioral contexts for typography stress testing: narrow widths, dense tables, responsive recomposition, long labels, multilingual expansion, action labels and status messages.

### Color

Legibility and hierarchy often depend on foreground/background contrast and viewing conditions. Reuse Color evidence where sufficient; independently validate when the result is important enough to justify a second check.

### Web Design

`T001` defines an outgoing validation contract for:

- loading fallback;
- permanent/failure fallback;
- script fallback;
- `size-adjust` and vertical metric override use;
- zoom/reflow;
- numeric feature/alignment stability;
- localized/mixed-script wrapping.

Type should consume future `W###` findings whenever browser/page evidence confirms, limits, or contradicts Type assumptions.

### Shared Accessibility / Human Factors

Platform/browser text-scaling/reflow behavior, assistive-technology consequences and human reading evidence are legitimate Type research inputs even if they are cross-cutting.

## Active next queue

Research may resume now. Priorities are guidance, not hard constraints:

1. Raster-proof the existing construction/optics exercise at multiple intended sizes and document at least one failure → redraw → re-proof cycle.
2. Execute the numeral/punctuation brief with native outlines, ambiguity alternatives, tabular/proportional implications where relevant, and proof strings.
3. Convert `T001` from source-grounded transfer baseline into rendered evidence: preferred font vs loading fallback vs permanent fallback, metric normalization, zoom/reflow, and numeric stability in a real browser environment; coordinate with Web Design evidence when available.
4. Run a mixed Latin/Korean fallback specimen with long labels and dense rows, separating font-level findings from layout/browser findings.
5. Validate typography information architecture under real platform/browser text scaling/reflow and localized long labels using Layout/Interaction contexts and Color contrast evidence where needed.
6. Pursue useful cross-domain replication, transfer validation, or adjacent learning when it materially strengthens professional judgment.
7. Open `T002` for the next substantial Type or Type-led cross-domain study when justified.

Do not limit growth merely to avoid overlap. Also do not repeat existing work without a reason that adds analytical value.

## Open research-quality gaps

- stronger primary-source coverage plus real evidence for rendering/rasterization and platform/browser vertical metrics;
- real browser/device validation of `T001` fallback and metric-adjustment claims;
- systematic mixed-script/fallback study, including Latin/Korean stress cases;
- broader family coherence evidence rather than isolated glyph exercises;
- reproducible font-source/build and QA evidence for later stages;
- empirical/human reading evidence where a claim exceeds formal type construction;
- stronger integration with Color, Layout/Interaction, and Web evidence in realistic project conditions.

## Current handoffs to other specialists

### Layout & Interaction

- `T001` shows that wrap, row-height, and reflow failures can originate in font substitution and vertical metrics, not only grid rules.
- Useful validation contexts: narrow responsive widths, dense rows, long labels, multilingual expansion, and text enlargement.

### Color

- fallback and zoom can alter apparent x-height/weight and therefore the perceptual result of a nominally unchanged text color.
- representative Color validation should include typographic states that materially change under substitution/enlargement.

### Web Design

- `research/type/T001-web-typography-fallback-metrics-reflow-transfer.md` is the current Type→Web handoff.
- It defines four fallback conditions, metric/fallback criteria, project inputs, browser validation states, numeric proof strings, and failure conditions.
- Web should return browser/page evidence that confirms, limits, or contradicts these assumptions.
- Scope limit: T001 is not real-browser PASS evidence.

When repeat research confirms, contradicts, or limits peer work, hand that result back explicitly.

## Handoff rule

If another specialist requests Type evidence, answer with canonical Type evidence or new investigation as appropriate. Cross-domain work is allowed when useful; do not silently claim canonical ownership of the peer domain and do not edit their files without authorization.

## Latest checkpoint

- `T001` opened and completed as a **source-grounded Type→Web transfer baseline** on 2026-09-14.
- Web Design specialist recognized as the fourth official peer.
- Next Type study ID advanced to `T002`.
- Foundation remains **not passed** until rendered/browser/source evidence closes the open gates above.
