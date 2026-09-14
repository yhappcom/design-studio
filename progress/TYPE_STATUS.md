# Typography / Type Design Specialist Status

Operating state: **PAUSED BY OWNER**
Governance sync: 2026-09-14
Primary path: `research/type/`
Next new-study ID: `T001`

This file is maintained by the Typography / Type Design Specialist. The specialist must not update global `progress/STATUS.md` directly.

## Operational mission

This specialist is not studying typography for academic self-satisfaction or file accumulation. The purpose of the Type program is to improve real app/product decisions.

When a project arrives, the specialist must be able to convert accumulated knowledge into project-specific guidance on font choice, hierarchy, metrics, density, numerals, localization, scaling, rendering, accessibility, and implementation trade-offs. Existing evidence should be applied before launching new broad research. Additional study is justified only when a material project decision depends on a genuine evidence gap.

`PAUSED BY OWNER` applies to self-directed curriculum expansion, not to explicit project-support requests.

## Current level

Current curriculum stage: **Stage 1 — Foundation**
Overall state: **PRACTICE / CRITIQUE depending on module**

The Type program has established a meaningful conceptual base but has not passed Foundation. Real rendering, native outline work, platform scaling/reflow proof, broader script/family validation, and repeated failure→revision evidence remain incomplete.

## Canonical evidence already established

- `research/type/001-type-as-system.md`
- `research/type/002-metrics-spacing-optical-rhythm.md`
- `research/type/003-stroke-contrast-bezier-optics.md`
- `research/type/005-numerals-punctuation-systems.md`
- `research/type/009-typography-as-information-architecture.md`
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
| Typography as information architecture | CRITIQUE | real platform scaling/reflow and localized long-label validation |

## Ownership boundary

This specialist owns font/glyph/type-system questions, metrics, spacing, font construction, typographic hierarchy, text roles, numerals/punctuation, multiscript/fallback, rendering and font engineering.

Do not launch research whose primary question is:

- colorimetry, luminance/palette/gamut → Color;
- screen geometry, grid/grouping/recomposition or interaction/state/task-flow semantics → Layout & Interaction.

## Incoming dependencies

Record active requests from other specialists here. Current recurring collaboration needs:

- Layout & Interaction may require font metrics, text expansion, numeral alignment, label length, scaling and action/status text behavior.
- Color may require realistic type size/weight/role contexts when evaluating text contrast or visual hierarchy.

Respond with canonical Type evidence or a Type-owned study; do not edit the requesting specialist's files.

## Useful external findings

### From Color

Use Color's canonical luminance/contrast and viewing-condition evidence whenever a legibility or hierarchy claim depends on foreground/background color. Do not derive independent contrast rules inside Type research.

### From Layout & Interaction

Use Layout/Interaction's canonical responsive, density, grouping, task-state and control-context evidence to create realistic typography tests. Do not infer universal spatial or interaction rules from typographic behavior.

This section must be revisited at the start of each work block after reading the other specialist status files.

## Dependencies to other domains

### DEPENDENCY — Layout & Interaction

Need realistic spatial and behavioral contexts for typography stress testing: narrow widths, dense tables, responsive recomposition, long labels, multilingual expansion, action labels and status messages. Type owns the text system; Layout & Interaction owns geometry and state semantics.

### DEPENDENCY — Color

When legibility or hierarchy depends on foreground/background contrast or chromatic/luminance behavior, use Color's canonical evidence and measured pair results rather than creating a parallel color study.

### DEPENDENCY — Shared Accessibility / Human Factors

Platform text-scaling/reflow behavior and assistive-technology consequences may require cross-cutting evidence. Record unowned gaps and request coordinator triage rather than creating a competing specialty.

## Next queue after explicit restart

1. Raster-proof the existing construction/optics exercise at multiple intended sizes and document at least one failure → redraw → re-proof cycle.
2. Execute the numeral/punctuation brief with native outlines, ambiguity alternatives, tabular/proportional implications where relevant, and proof strings.
3. Validate typography information architecture under real platform text scaling/reflow and localized long labels using Layout/Interaction-owned spatial contexts and Color-owned contrast evidence when needed.
4. Only after those gates, identify the next missing Foundation topic and open `T001` if genuinely new research is required.

Do not start a new study merely to accumulate notes. Prefer closing existing evidence gaps first.

## Open research-quality gaps

- stronger primary-source coverage for rendering/rasterization and platform vertical metrics;
- systematic mixed-script/fallback study;
- broader family coherence evidence rather than isolated glyph exercises;
- reproducible font-source/build and QA evidence for later stages;
- empirical/human reading evidence where a claim exceeds formal type construction.

## Handoffs to other specialists

After substantial Type work, state explicitly whether the result can help:

- Layout & Interaction: metrics, text growth, line wrapping, action/status labels, numeral/table behavior, scaling/reflow;
- Color: realistic text roles/sizes/weights for contrast and hierarchy validation.

Reference the canonical Type file rather than copying source summaries elsewhere.

## Handoff rule

If another specialist requests Type evidence, answer with a canonical Type study or a new Type-only study. Do not edit their files. Split Color- or Layout/Interaction-owned portions into dependencies.