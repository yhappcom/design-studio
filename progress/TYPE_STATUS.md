# Typography / Type Design Specialist Status

Operating state: **ACTIVE — RESEARCH MAY RESUME**
Governance sync: 2026-09-14
Primary path: `research/type/`
Next new-study ID: `T005`

This file is maintained by the Typography / Type Design Specialist. The specialist must not update global `progress/STATUS.md` directly.

## Operational mission

Type research exists to improve real app, web, and product decisions. Research volume or curriculum speed is not the objective.

When a project arrives, this specialist must convert accumulated knowledge into project-specific guidance on font choice, hierarchy, metrics, spacing, numerals, density, localization, fallback, scaling, rendering, accessibility, implementation trade-offs, validation, and failure conditions.

Self-directed research remains ACTIVE. Adjacent Color, Layout/Interaction, Web, Accessibility, Human Factors, or implementation knowledge may be studied when it materially improves Type judgment, replication, transfer validation, or project usefulness.

## Current level

Current curriculum stage: **Stage 1 — Foundation**
Overall state: **PRACTICE / CRITIQUE**

Foundation is not passed. The Type program now includes reproducible compiled research fonts, FreeType renderer experiments, a complete original research `0–9`/punctuation system, proportional/tabular metrics, zero alternatives, and documented failure→redraw evidence. Production curve quality, manual/native hinting, multi-engine/browser/device validation, broader family coherence, human recognition evidence, and multilingual/fallback proof remain incomplete.

## Canonical evidence already established

### Research
- `research/type/001-type-as-system.md`
- `research/type/002-metrics-spacing-optical-rhythm.md`
- `research/type/003-stroke-contrast-bezier-optics.md`
- `research/type/005-numerals-punctuation-systems.md`
- `research/type/009-typography-as-information-architecture.md`
- `research/type/T001-web-typography-fallback-metrics-reflow-transfer.md`
- `research/type/T002-raster-proof-redraw-cycle.md`
- `research/type/T003-minimal-font-renderer-matrix.md`
- `research/type/T004-native-numeral-punctuation-renderer-proof.md`

### Type-owned evidence / reproducibility artifacts
- `research/type/T002-raster-proof-redraw-cycle.svg`
- `research/type/T003-minimal-research-font-renderer-matrix.py`
- `research/type/T003-minimal-font-renderer-matrix.svg`
- `research/type/T004-numeral-punctuation-research-font.py`
- `research/type/T004-numeral-punctuation-results.json`
- `research/type/T004-numeral-punctuation-evidence.svg`

### Earlier practice evidence retained outside the ordinary Type write area
- `type-design/exercises/001-ho-metrics-three-hypotheses.svg`
- `type-design/exercises/001-ho-metrics-critique.md`
- `type-design/exercises/002-construction-curve-optics.svg`
- `type-design/exercises/002-construction-curve-optics-critique.md`
- `type-design/exercises/003-numeral-punctuation-system-brief.md`
- `product-design/exercises/006-typography-information-architecture-practice.md`
- `product-design/exercises/008-typography-enlarged-proof.svg`
- `product-design/exercises/008-typography-enlarged-proof-critique.md`

## Latest completed block — T004

`T004-native-numeral-punctuation-renderer-proof.md` executes the previously open numeral/punctuation brief as a compiled research font rather than another abstract study.

### Original construction and feature system

T004 builds a 1000-UPM low-contrast constructed/hybrid research set containing:

- original `0–9` proportional lining figures;
- fixed-cell tabular alternates;
- `O I l S B` ambiguity controls;
- `: + , . / -` plus mathematical minus `−`;
- unmarked, slashed and internal-dot zero strategies;
- GSUB features `tnum`, `zero`, and research `cv01`.

Default figures are proportional. Tabular alternates use the same figure identities translated inside a common `620`-unit cell; they are not horizontally stretched to fill it.

### Renderer-aware tabular result

All ten `.tnum` glyphs have source advance `620`, but FreeType raw hinted advances are mode-dependent:

- 14ppem: no-hint all `8.6875px`; normal auto-hint splits `8/9px`; light auto-hint remains all `9px`;
- 20ppem: no-hint all `12.40625px`; normal auto-hint splits `12/13px` with digit `6` at `13px`; light auto-hint remains all `12px`;
- 48ppem: no-hint all `29.765625px`; normal auto-hint splits `29/30px`; light auto-hint remains all `30px`.

Professional consequence: **equal source tabular metrics are necessary but do not by themselves prove final rendered column alignment**. Runtime client/renderer/positioning behavior remains part of the approval contract.

### Failure → redraw evidence

The first colon used 50-unit dots. It produced zero strong-coverage pixels (`alpha >= 128`) at both 14 and 20ppem. The redraw increased dot diameter to 84 units and restores:

- 14ppem: `0 → 2` strong pixels;
- 20ppem: `0 → 4`;
- 48ppem: `8 → 26`.

`colon.v0` is rejected for this compact research system; the redraw is kept for further validation, not PASS.

### Zero-strategy result

- unmarked zero remains a viable default where ambiguity cost is low; it is proportionally narrower than `O`, but no human error-rate claim is made;
- slashed zero produces the strongest compact internal signal in this construction and remains a conditional alternate, not the global default;
- the current dotted/internal-mark alternate adds no strong pixels at 14 or 20ppem under light auto-hint and is rejected for compact use in its current form.

### Evidence level

**PRACTICE + CRITIQUE / compiled TrueType + FreeType transfer evidence.**

T004 does not prove production Bézier topology, browser feature application, human recognition, CoreText/DirectWrite/Skia/device behavior, or final product suitability.

## Foundation module status

| Module | Status | Remaining gate |
| --- | --- | --- |
| Type anatomy / metrics | PRACTICE / CRITIQUE | broader family/role proof and platform validation |
| Stroke / contrast / construction | PRACTICE / CRITIQUE | T002/T003 control cycle plus T004 numeral construction exist; broader coherent family extension required |
| Bézier / outline discipline | PRACTICE | T004 procedural outlines are research geometry, not production topology; editable curve/extrema/overlap/export QA remains open |
| Optical correction | PRACTICE / CRITIQUE | T002/T003 show size/renderer interaction; target-platform/family decisions remain open |
| Rasterization / rendering | PRACTICE / CRITIQUE | compiled TTF + FreeType matrices exist; manual/native hinting and CoreText/DirectWrite/Skia/browser/device matrix open |
| Spacing before kerning | PRACTICE / CRITIQUE | T004 broadens sequence evidence; full alphabet/family spacing and runtime shaping still open |
| Numerals / punctuation | **PRACTICE / CRITIQUE** | complete research 0–9/punctuation/ambiguity/tnum proof exists; production curves, browser feature use, human recognition and broader punctuation/language coverage remain open |
| Typography as information architecture | CRITIQUE | real platform/browser scaling/reflow and localized long-label validation |
| Web fallback / metric transfer | IN STUDY / TRANSFER BASELINE | actual browser/device tests for loading/failure/script fallback, metric overrides, zoom/reflow, data stability |
| Mixed-script / fallback | OPEN | systematic Latin/Korean and broader script/fallback proof |

## Primary ownership

Type is the canonical owner for font/glyph/type-system questions, metrics, spacing, construction, hierarchy, text roles, numerals/punctuation, multiscript/fallback, rendering and font engineering.

This is primary ownership, not a research prohibition. Cross-domain validation is allowed and encouraged when it materially strengthens project judgment.

## Peer evidence currently affecting Type

### Color

- `008-color-luminance-contrast-hierarchy.md` and C001/C002 establish that foreground/background context, user/browser overrides and semantic color systems affect apparent typography and hierarchy.
- T003/T004 grayscale alpha evidence must later be tested under representative Color conditions rather than generalized from black-on-white rendering.
- T004 colon-v0 and dotted-zero failures provide controlled compact marks for future Color viewing-condition transfer tests.

### Layout / Interaction

- L002 establishes compact/standard/spacious density as task-dependent rather than aesthetic defaults.
- T004 therefore does not treat tabular figures or marked zero as default styling; they must answer a concrete comparison/ambiguity task.
- I001 now includes a running Chromium prototype with a documented failure→revision→re-proof cycle and 14/14 controlled assertions. Its route titles, Up/Back/Close labels, workspace identity, focus and status contexts are high-value future Type stress cases for fallback, wrapping and localization.

### Web Design

Web Design remains the canonical integration/validation owner for actual websites/web apps. At the latest synchronization, `W001` was still open and no substantive W study was available.

Type currently offers three explicit Web transfer contracts:

- **T001** — loading/failure/script fallback, metrics, zoom/reflow, numeric stability;
- **T003** — compiled-font compact rendering/metric behavior under different hinting modes;
- **T004** — actual `tnum`/zero-feature research font, numeric proof strings, punctuation failures and renderer-aware tabular alignment risk.

Do not invent Web evidence until a real W study or browser validation exists.

## Active next queue

Research may resume immediately. Expected-value priorities:

1. **T005 mixed Latin/Korean fallback and vertical-metric compatibility** — move beyond Latin-only research: apparent-size/stroke balance, baseline/line-box behavior, long localized labels, dense rows, fallback scenario classification and platform implications.
2. **Browser transfer of T001/T003/T004** — when Web evidence becomes available, load actual research fonts and test fallback/loading, CSS feature application (`tnum`, zero), zoom, DPR, wrapping and table alignment.
3. **Production-outline audit** — replace procedural/polygonal research outlines with a small manually auditable source subset and evaluate extrema, curve economy, overlap handling and export QA without pretending the full family is ready.
4. **T003/T004 target-renderer extension** — add new contour variants only after a real minimum-size/rendering contract exists; avoid endless glyph tuning without project conditions.
5. **Color transfer** — composite actual renderer alpha masks under representative light/dark/reduced-contrast/viewing conditions.
6. **Layout transfer** — place renderer-tested type into L002 compact/standard/spacious contexts and measure task-relevant alignment/search/comparison behavior.
7. **Typography information architecture** — validate hierarchy under text enlargement, localization, route labels, dense data and real reflow.
8. Pursue replication, contradiction review, method comparison, or project-specific research when it materially increases decision reliability.
9. Open `T005` for the next substantial new Type question.

## Open research-quality gaps

- systematic Latin/Korean fallback and mixed-script vertical-metric proof;
- production-quality editable curve topology and broader glyph-family audit;
- manual/native TrueType hinting or justified hintless strategy;
- CoreText, DirectWrite, Android/Skia and browser transfer evidence as project needs require;
- actual Web validation of T001/T003/T004, including `tnum` and zero-feature application;
- human recognition/reading evidence for ambiguity claims;
- broader punctuation and localization-sensitive glyph coverage;
- broader family coherence beyond H/O/n/o plus the research numeral/ambiguity controls;
- reproducible build/QA tooling suitable for later production stages;
- Color/reading-condition and Layout/density transfer evidence.

## Current handoffs to other specialists

### Layout / Interaction

- T003 demonstrates that compact density must be tested with actual renderer output and hinted metrics.
- T004 adds that even fixed source tabular advances can split under a strong auto-hint mode; exact column behavior must be validated in the actual stack.
- Useful contexts: L002 compact/standard/spacious variants, data tables, dense rows, navigation/workspace identifiers, localization and text enlargement.
- Scope limit: Type does not select the product's density strategy.

### Color

- T003 supplies controlled renderer alpha evidence for join corrections.
- T004 supplies compact punctuation/zero cases with measurable weak/strong raster signals; these can be transfer-tested while geometry remains fixed.
- Scope limit: no contrast, glare, dark-mode or environmental threshold is established by Type.

### Web Design

- T001 defines fallback/loading/reflow requirements.
- T003 provides a reproducible compact-font renderer method.
- T004 adds a complete numeric/punctuation research system with actual OpenType `tnum` and zero alternates plus proof strings and renderer-dependent alignment risk.
- Web should test actual browser/CSS feature application, font loading/fallback, zoom/DPR, table alignment and localized content, then return confirmation, limitation, contradiction or transfer failure.
- Scope limit: FreeType evidence is not browser PASS.

## Handoff rule

When another specialist requests Type evidence, answer with canonical Type evidence or new investigation as appropriate. Do not silently replace peer-domain ownership or edit peer canonical files without authorization.

## Latest checkpoint

- `T002`: surrogate failure → redraw → re-proof cycle completed.
- `T003`: reproducible compiled TrueType + FreeType renderer matrix completed.
- `T004`: complete original numeral/punctuation research system, proportional/tabular metrics, zero alternatives, compiled font, colon redraw and full-set renderer-aware tabular stress completed.
- Numerals / punctuation advanced from `IN STUDY` to **PRACTICE / CRITIQUE**, not PASS.
- Next Type study ID: `T005`.
- Overall Type state remains **Stage 1 / PRACTICE + CRITIQUE / Foundation NOT PASSED**.
