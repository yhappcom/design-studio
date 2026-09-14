# Typography / Type Design Specialist Status

Operating state: **ACTIVE — RESEARCH MAY RESUME**
Governance sync: 2026-09-14
Primary path: `research/type/`
Next new-study ID: `T004`

This file is maintained by the Typography / Type Design Specialist. The specialist must not update global `progress/STATUS.md` directly.

## Operational mission

Type research exists to improve real app, web, and product decisions. Research volume or curriculum speed is not the objective.

When a project arrives, this specialist must convert accumulated knowledge into project-specific guidance on font choice, hierarchy, metrics, spacing, numerals, density, localization, fallback, scaling, rendering, accessibility, implementation trade-offs, validation, and failure conditions.

Self-directed research remains ACTIVE. Adjacent Color, Layout/Interaction, Web, Accessibility, Human Factors, or implementation knowledge may be studied when it materially improves Type judgment, replication, transfer validation, or project usefulness.

## Current level

Current curriculum stage: **Stage 1 — Foundation**
Overall state: **PRACTICE / CRITIQUE**

Foundation is not passed. The Type program now includes a reproducible compiled research-font and real FreeType renderer experiment, but broader native outlines, manual/native hinting, multi-engine/browser/device validation, numerals/punctuation, family coherence, and multilingual/fallback evidence remain incomplete.

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

### Type-owned evidence / reproducibility artifacts
- `research/type/T002-raster-proof-redraw-cycle.svg`
- `research/type/T003-minimal-research-font-renderer-matrix.py`
- `research/type/T003-minimal-font-renderer-matrix.svg`

### Earlier practice evidence retained outside the ordinary Type write area
- `type-design/exercises/001-ho-metrics-three-hypotheses.svg`
- `type-design/exercises/001-ho-metrics-critique.md`
- `type-design/exercises/002-construction-curve-optics.svg`
- `type-design/exercises/002-construction-curve-optics-critique.md`
- `type-design/exercises/003-numeral-punctuation-system-brief.md`
- `product-design/exercises/006-typography-information-architecture-practice.md`
- `product-design/exercises/008-typography-enlarged-proof.svg`
- `product-design/exercises/008-typography-enlarged-proof-critique.md`

## Latest completed block — T003

`T003-minimal-font-renderer-matrix.md` moves the T002 R0/R1 lowercase-`n` question from SVG raster surrogate into actual compiled TrueType + FreeType rendering.

### Reproducible research font

The study builds a minimal 1000-UPM quadratic TTF with:

- x-height `500`, cap height `700`;
- `.notdef`, `space`, `H`, `O`, `n`, `n.alt`, `o`;
- R0 normal `n` and R1 research alternate mapped to private-use U+E000;
- identical R0/R1 source advance `560`;
- no authored manual TrueType instructions.

The build is reproducible through `T003-minimal-research-font-renderer-matrix.py` and inspectable through FontTools/TTX workflows.

### Renderer matrix result

R0/R1 were rendered through FreeType at `14 / 16 / 24 / 48 ppem` using:

- no hinting;
- forced auto-hint normal;
- forced auto-hint light.

Key result: **T002's compact-fragility conclusion is not renderer-invariant.**

Examples:

- at 14ppem, no-hint strong pixels change `13 → 11`, while autohint-normal gives `15 → 15`;
- at 16ppem, autohint-normal amplifies the R0/R1 coverage difference to about `-12.1%` while no-hint is about `-6.7%`;
- at 24ppem, identical `560` source advances produce `14px` vs `13px` hinted advances under normal auto-hinting;
- at 48ppem, FreeType delta-aware integer positioning can normalize a raw hinted-advance difference back to equal repeated origins.

### Professional conclusion

The approval unit is not an outline in isolation. For compact custom type, the meaningful unit is:

**outline + source metrics + hinting strategy + renderer + positioning behavior + actual product context**.

T003 therefore **limits** T002 rather than accepting or rejecting R1. R1 remains a plausible join-relief direction, but no R0/R1/optical-size winner is selected.

Evidence level: **PRACTICE + TRANSFER VALIDATION / real font-engine evidence**. Not platform/browser/device PASS.

## Foundation module status

| Module | Status | Remaining gate |
| --- | --- | --- |
| Type anatomy / metrics | PRACTICE / CRITIQUE | broader family/role proof and platform validation |
| Stroke / contrast / construction | PRACTICE / CRITIQUE | T002/T003 control-form cycle exists; extend coherently across family |
| Bézier / outline discipline | PRACTICE | real editable source audit across more glyphs; extrema/topology/overlap/export QA |
| Optical correction | PRACTICE / CRITIQUE | T002/T003 show size/renderer interaction; target-platform proof and redraw decision still open |
| Rasterization / rendering | PRACTICE / CRITIQUE | compiled TTF + FreeType matrix complete; manual/native hinting and CoreText/DirectWrite/browser/device matrix open |
| Spacing before kerning | PRACTICE | broader repeated-string and family validation |
| Numerals / punctuation | IN STUDY | native 0–9/punctuation outlines, ambiguity alternatives, pnum/tnum proof |
| Typography as information architecture | CRITIQUE | real platform/browser scaling/reflow and localized long-label validation |
| Web fallback / metric transfer | IN STUDY / TRANSFER BASELINE | actual browser/device tests for loading/failure/script fallback, metric overrides, zoom/reflow, data stability |
| Mixed-script / fallback | OPEN | systematic Latin/Korean and broader script/fallback proof |

## Primary ownership

Type is the canonical owner for font/glyph/type-system questions, metrics, spacing, construction, hierarchy, text roles, numerals/punctuation, multiscript/fallback, rendering and font engineering.

This is primary ownership, not a research prohibition. Cross-domain validation is allowed and encouraged when it materially strengthens project judgment.

## Peer evidence currently affecting Type

### Color

- `008-color-luminance-contrast-hierarchy.md` and C001/C002 establish that foreground/background context, user/browser overrides and semantic color systems affect apparent typography and hierarchy.
- T003 alpha coverage must later be tested under representative Color conditions rather than generalized from black-on-white rendering.

### Layout / Interaction

- L002 establishes compact/standard/spacious density as task-dependent rather than aesthetic defaults.
- T003 therefore must not choose a minimum type size independently of the actual density/task context.
- I001 adds navigation titles, tabs, breadcrumbs and deep-link orientation as future Type stress contexts for long labels/fallback/scaling.

### Web Design

Web Design remains the canonical integration/validation owner for actual websites/web apps. At the latest synchronization, `W001` was still open and no substantive W study was available.

Type currently offers two explicit Web transfer contracts:

- **T001** — loading/failure/script fallback, metrics, zoom/reflow, numeric stability;
- **T003** — compiled-font compact rendering/metric behavior that should be re-tested under actual CSS/browser/zoom/DPR conditions.

Do not invent Web evidence until a real W study or browser validation exists.

## Active next queue

Research may resume immediately. Expected-value priorities:

1. **Native numeral/punctuation practice** — execute the existing brief as the next major Type construction gap: real `0–9`, `: + , . / -`, ambiguity alternatives, pnum/tnum metrics and raster proof.
2. **T003 extension** — add an R2 compromise contour only after the relevant target-size/rendering contract is explicit; compare repeated `H O n o` strings with delta-aware positioning.
3. **Browser transfer of T001/T003** — when Web evidence becomes available, load an actual research font and test fallback/loading, CSS size, zoom, DPR, wrapping and numeric alignment.
4. **Latin/Korean fallback study** — mixed-script baseline, apparent-size/stroke/line-box compatibility, long labels and dense rows.
5. **Color transfer** — composite actual renderer alpha maps under representative light/dark/reduced-contrast conditions.
6. **Layout transfer** — place renderer-tested typography into L002 compact/standard/spacious contexts instead of evaluating glyph size in isolation.
7. **Typography information architecture** — validate hierarchy under text enlargement, localization and real reflow.
8. Pursue replication, contradiction review, method comparison, or project-specific research when it materially increases decision reliability.
9. Open `T004` for the next substantial new Type question.

## Open research-quality gaps

- native `0–9` and punctuation outlines with ambiguity strategies;
- proportional vs tabular figure metrics and actual rendered alignment;
- real editable source audit across a broader glyph family;
- manual/native TrueType hinting or justified hintless strategy;
- CoreText, DirectWrite, Android/Skia and browser transfer evidence as project needs require;
- actual Web validation of T001/T003;
- systematic Latin/Korean fallback and mixed-script vertical-metric proof;
- broader family coherence beyond `H/O/n/o` and one `n` redraw pair;
- reproducible build/QA tooling suitable for later production stages;
- human recognition/reading evidence where claims exceed formal construction;
- Color/reading-condition and Layout/density transfer evidence.

## Current handoffs to other specialists

### Layout / Interaction

- T003 demonstrates that a compact density target must be tested with actual renderer output and hinted metrics, not source geometry alone.
- Useful contexts: L002 compact/standard/spacious variants; narrow navigation; dense rows; localized labels; text enlargement.
- Scope limit: Type does not select the product's density strategy.

### Color

- T003 supplies exact renderer alpha coverage for a controlled R0/R1 pair.
- Useful next transfer: keep geometry/render mode fixed while varying Color-defined foreground/background/viewing conditions.
- Scope limit: no contrast or environmental threshold is established by Type.

### Web Design

- T001 defines fallback/loading/reflow validation requirements.
- T003 adds a reproducible compiled-font method and a renderer-dependent compact-size failure hypothesis.
- Web should test actual browser/CSS font size, zoom, DPR, loading/fallback and layout behavior and return confirmation, limitation, contradiction or transfer failure.
- Scope limit: T003 is FreeType evidence, not browser PASS.

## Handoff rule

When another specialist requests Type evidence, answer with canonical Type evidence or new investigation as appropriate. Do not silently replace peer-domain ownership or edit peer canonical files without authorization.

## Latest checkpoint

- `T002`: surrogate failure → redraw → re-proof cycle completed.
- `T003`: reproducible compiled TrueType + FreeType renderer matrix completed.
- T003 materially limits the outline-only interpretation of T002 and establishes renderer/size/positioning dependency.
- Next Type study ID: `T004`.
- Overall Type state remains **Stage 1 / PRACTICE + CRITIQUE / Foundation NOT PASSED**.
