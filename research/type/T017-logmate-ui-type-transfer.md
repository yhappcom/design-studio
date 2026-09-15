# T017 — LogMate UI Type Transfer Sprint: Semantic Geometry, Identifier Legibility, and Platform Contract

Status: **PROJECT-SPECIFIC TRANSFER VALIDATION / READY FOR LOGMATE UI TRANSFER — provisional candidate and implementation contracts established; exact Flutter/platform render validation remains OPEN**

Owner: Typography / Type Design Specialist  
Canonical research path: `research/type/`  
Product evidence source: `yhappcom/logmate` branch `design/design-studio-proposal`  
Design Studio snapshot checked: `fdebf27e5cb78f32a44749d9c4524b9439e50328`  
LogMate design snapshot checked: `e44b048b1ff32c291a05c45ff9befc7c8742b608`  
Measured candidate data: `research/type/T017-logmate-ui-type-candidate-results.json`

## Purpose

This study is not another generic type-design curriculum block. It transfers existing Type evidence into the live LogMate design problem exposed by Opening Screen Draft 01.

The immediate failure is structural: proportional airport-code glyphs produce different text widths, so repeated rows such as `ICN → NRT` and `NRT → ICN` do not create stable semantic anchors even though the time values use tabular figures.

The project question is therefore:

> Which geometry belongs to Layout, which behavior belongs to Type, and what provisional font system is strong enough to begin Opening Draft 02 without hiding layout defects behind monospace typography?

This sprint does **not** authorize a bespoke LogMate typeface, logo design, or a universal font decision for every future LogMate surface.

---

## RELATED DOMAIN CHECK

### Typography / Type
- Evidence checked: T004 numeral/punctuation renderer proof; T005 Latin/Korean mixed-script fallback; T016 webfont loading/failure metric contract; `progress/TYPE_STATUS.md` through T016.
- Reusable finding:
  - `tnum` is a figure-width contract, not a cure for alphabetic identifier geometry;
  - marked zero and disambiguation features are conditional tools for mixed identifiers;
  - mixed-script fallback and downloadable-font state can change geometry and line boxes;
  - source metrics are not final Flutter/browser geometry proof.
- Replication / challenge / transfer opportunity: use real LogMate strings and existing commercial/open-source families rather than a synthetic research font.
- Dependency / overlap: exact Flutter/Android/iOS/PWA rendering remains target-stack validation.

### Color
- Evidence checked: latest Color status through Stage 1 PASS and prior Type→Color transfer conclusions.
- Reusable finding: actual rendered glyph mass is part of the visual result; semantic foreground tokens do not normalize font/fallback differences.
- Replication / challenge / transfer opportunity: Draft 02 should hold Color treatment stable while Type/geometry changes are evaluated.
- Dependency / overlap: Color does not determine semantic columns or font metrics.

### Layout / Interaction
- Evidence checked: L003 fallback→reflow transfer; L004 tabular-numeral dense-comparison transfer; latest Layout status; LogMate Opening Draft 01 review.
- Reusable finding:
  - Layout should absorb acceptable Type variance through semantic priority and geometry before shrinking/clipping text;
  - `tnum` can improve comparison while also increasing intrinsic width;
  - fixed pixel tracks that fit one font state are not robust contracts.
- Replication / challenge / transfer opportunity: define explicit `DEP | arrow | ARR | flexible | time` ownership and stress it across fonts/content.
- Dependency / overlap: Layout owns responsive recomposition; Type defines font/feature requirements and failure conditions.

### Web Design
- Evidence checked: latest Web status through Stage 1 PASS and T016 handoff requirements.
- Reusable finding: downloadable font loading/failure, browser zoom and actual page constraints are runtime states.
- Implementation / application validation opportunity: reproduce the chosen artifact in Flutter Web/PWA under cold load, offline service-worker state and persistent fallback failure.
- Dependency / overlap: no PWA PASS is inferred from the local RAQM measurements in this study.

### Other / cross-cutting / future specialist
- Evidence checked:
  - LogMate `MASTER.md`, `VISUAL_FOUNDATION_V01.md`, Opening Draft 01 review and regional sample policy;
  - Flutter `FontFeature`, custom-font and `fontFamilyFallback` APIs;
  - Inter upstream feature documentation and OFL metadata.
- Reusable finding:
  - Flutter can request `tnum`, `zero` and stylistic sets through `FontFeature` when the selected font supports them;
  - missing declared font weights should not be treated as equivalent to real weight files;
  - fallback order is explicit custom family → ordered custom fallbacks → platform fallback.
- Dependency / overlap: human identifier-confusion rates and cross-platform raster equivalence remain untested.

### Overlap decision
- **PROJECT-SPECIFIC TRANSFER VALIDATION + METHOD COMPARISON + FAILURE ANALYSIS**.
- Why: the Type program already contains the general theory. The high-value work is converting it into an actionable LogMate contract and provisional candidate choice.

---

## Product evidence checked

Current LogMate product authority confirms, among other constraints:

- native iOS/Android and tablet/EFB PWA are first-class targets;
- product-authored UI is currently English-only while user-entered data must remain Unicode/multilingual safe;
- View Logbook uses semantic columns rather than viewport-stretched columns;
- clock display uses `HH:mm`; durations/cumulative values use `H+MM`; cumulative UI must support at least `99,999+59`;
- View Logbook header/body/totals share semantic boundaries and a 36px row rhythm;
- the current View Logbook body has an explicit **monospace/code w400** product contract. T017 does not silently revoke that decision.

Opening Draft 01 currently uses one proportional row with `departure`, custom-painted arrow, `arrival`, `Spacer`, and tabular `time`. There are no fixed semantic DEP/ARR cells. The current theme bundles only Roboto 400/500 while styles request heavier weights in multiple places, so visual review can include synthesized/extrapolated weight behavior unless exact files are added.

---

# 1. Core decision — layout robustness before type refinement

## REJECT

Do not solve airport-code drift by switching the entire route row to a monospace font.

A monospace face can equalize `ICN`, `LHR`, `JFK`, etc., but it would make a font choice responsible for a relationship that belongs to the information structure. It also couples route geometry to a technical aesthetic and creates unnecessary pressure to use monospace for other identifiers.

## STUDIO JUDGMENT

Opening route rows should use this ownership model:

`DEP cell | arrow cell | ARR cell | flexible space | time cell`

- DEP and ARR: equal semantic cells, same start alignment.
- Arrow: independent fixed visual cell; it does not determine the text baseline.
- Time: dedicated right-aligned cell.
- Flexible space: absorbs remaining width.
- Type: optimizes legibility, figure behavior, punctuation, weight and fallback **inside** those cells.

The row therefore remains stable even when `ICN`, `HND`, `JFK`, `LHR`, `CDG` and regional alternatives have different glyph advances.

---

# 2. Candidate comparison method

Four materially different open-source UI sans controls were measured at the current Opening route role size (`17px`) using Pillow RAQM / HarfBuzz on Linux:

- Inter 4.001, Semibold 600 control;
- Roboto 2.138, Medium 500 control;
- Noto Sans 2.004, Semibold 600 control;
- Lato 2.015, Semibold 600 control.

Environment recorded in the companion JSON:

- Pillow 12.3.0;
- RAQM 0.10.5;
- HarfBuzz 14.2.1;
- FreeType 2.14.3;
- fontTools 4.63.0.

This is **not Flutter/Skia/CoreText/PWA approval**. Exact local font hashes are preserved in the JSON so later differences are traceable.

Strings include all requested airport codes, identifiers, times/totals, and ambiguity groups. An additional synthetic A–Z three-letter sweep was used only to size the semantic code cell against a font-independent stress case rather than tune it to `ICN/NRT`.

## Measured geometry summary

| Candidate | Airport sample width range @17px | Sample spread | Max synthetic 3-cap string | `00:45` with `tnum` | `9,999:59` with `tnum` | x-height/em |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Inter 600 | 28.672–37.859px | 9.187px | `WWW` 52.781px | 48.562px | 75.125px | 0.5459 |
| Roboto 500 | 27.141–35.281px | 8.140px | `WWW` 44.906px | 43.125px | 66.188px | 0.5283 |
| Noto Sans 600 | 25.391–38.859px | 13.468px | `WWW` 48.609px | 43.625px | 67.812px | 0.5360 |
| Lato 600 | 27.234–39.016px | 11.782px | `WWW` 53.203px | 43.750px | 67.391px | 0.5065 |

All four tested controls support `tnum`; all had zero measured digit-width spread when that feature was enabled. Inter's default figures are proportional in the tested build, so comparative numeric roles must request `tnum` explicitly. The other three measured controls happened to use equal default digit advances, but the product should still request the semantic feature rather than depend on a family default.

### Finding A — airport-code drift is real in every proportional candidate

Among the requested airport codes, the measured spread ranges from about 8.14px to 13.47px at only 17px type. Font substitution can reduce or enlarge the symptom but does not remove the structural cause.

### Finding B — Inter costs more numeric width

Inter's tabular digit cell is wider in this control: `00:45` is about 48.56px versus roughly 43–44px in the other candidates. That is a real density trade-off.

Disposition: do not reject Inter merely to fit a pre-existing narrow numeric slot. L004 already established that numeric tracks should be sized **after** the approved numeric feature is active.

---

# 3. Font Candidate Comparison

## Inter — **PROVISIONAL BASELINE FOR OPENING DRAFT 02**

Strengths:

- designed for screen/UI use with tall x-height;
- `tnum` and `pnum`;
- `zero` slashed-zero feature;
- official `ss02` “Disambiguation (with zero)” and `ss04` “Disambiguation without slashed zero” sets;
- measured `mark` + `mkmk` support in the control build;
- real 400/500/600/700+ weights and variable forms are available upstream;
- SIL OFL 1.1 in measured/upstream metadata.

Project advantage:

One family can serve ordinary UI, route codes, numbers and mixed alphanumeric identifiers with **role-specific OpenType features**, avoiding an unnecessary second “technical” font.

Trade-off:

Inter is not the most compact numeric candidate. Its `WWW` stress string and tabular figures require honest geometry. That is acceptable because the product needs robustness more than one-font screenshot compactness.

## Roboto — **CONTROL / CURRENT TEMPORARY BASELINE**

Strengths:

- currently bundled in LogMate;
- compact airport/numeric geometry among this set;
- `tnum` is available in the measured control;
- mature platform use and small current LogMate static assets.

Limits:

- current LogMate bundle declares only 400 and 500 while UI styles request 600/700/800 in places;
- the measured control does not provide Inter's explicit project-relevant `zero` + named disambiguation system;
- the existing Draft 01 alignment failure persists because the row has no semantic columns.

Roboto remains a valid comparison control, not the recommended Draft 02 baseline.

## Noto Sans — **MULTISCRIPT/FALLBACK-ECOSYSTEM CONTROL**

Strengths:

- strong open-source multilingual ecosystem;
- `tnum` and `zero` in the measured control;
- useful comparison with the existing Noto Sans KR fallback direction.

Limits:

- the tested airport-code sample had the largest width spread of the four controls;
- Noto naming/ecosystem does not imply metric parity with Noto CJK/Korean faces: T005 already measured materially different vertical-metric relationships.

Noto remains a strong fallback/ecosystem reference, not the current main-UI winner.

## Lato — **HUMANIST CONTROL, NOT SHORTLIST LEADER**

Strengths:

- materially different humanist texture;
- `tnum` support and OFL licensing;
- useful control against the more neutral UI families.

Limits:

- widest measured `WWW` stress string in this set;
- lower x-height than the other controls;
- no `zero` feature in the measured control;
- no measured `mkmk` feature in this specific build.

No product reason found in this sprint to prefer it over Inter/Roboto/Noto Sans.

### Candidate decision

**Use Inter as the provisional Opening Draft 02 main UI family. Do not create a separate identifier font at this stage.**

The final product-wide family decision remains conditional on exact Flutter artifact rendering and broader screens. Draft 02 is the correct next place to validate that provisional choice.

---

# 4. Identifier Legibility Audit

Requested strings:

- airports: `ICN NRT SIN JFK LHR CDG HND DXB FRA LAX`;
- flights/types/registration: `KE704 BA117 AF264 B737-900 B737-8 A320-200 HL8301 N12345 G-EUOH`;
- ambiguity: `0/O`, `1/I/l`, `5/S`, `8/B`.

## Inter default

Designer inspection at the compact role size shows acceptable `5/S` and `8/B` structural differences, but default `0/O` and especially `I/l` can be stronger for operational identifiers.

## Inter `ss02`

In the measured control, `ss02` introduces a slashed zero and more differentiated `I/l` forms while retaining the same family voice. This is the strongest project-relevant ambiguity control among the tested candidate configurations.

**Important evidence limit:** this is designer inspection and font-feature evidence, not a measured pilot recognition/error-rate study.

## Recommended feature policy

- Airport codes: proportional Inter, uppercase, **no `tnum`**, default forms for Draft 02; geometry solves alignment. `ss04` may be compared later if an `I`-specific issue appears.
- Flight number / registration / aircraft type: proportional Inter; test `FontFeature.stylisticSet(2)` (`ss02`) as the provisional high-disambiguation variant.
- Time / duration / totals: Inter with `FontFeature.tabularFigures()`; **do not slash zero by default** because there is no alphabetic `O` in the numeric-only role.
- Prose, labels, crew names, remarks: ordinary proportional forms; no identifier stylistic set.

If the slashed zero is judged visually too technical in a specific identifier role, compare `ss04` (disambiguation without slashed zero) and enable `FontFeature.slashedZero()` only where `0/O` consequence justifies it. Do not invent a second font merely to get this behavior.

---

# 5. LogMate Type Role Matrix

Sizes are **provisional starting values**, not product-wide immutable tokens. Exact line boxes require the actual selected Flutter artifact.

| Role | Priority | Provisional behavior | Alignment / figures | Case / tracking | Fallback / unresolved |
| --- | --- | --- | --- | --- | --- |
| Product name / temporary wordmark | identity | Inter 17–18, 700 | start | authored case; restrained tracking | logo decision separate; exact mark OPEN |
| Screen title | high hierarchy | Inter 20–24, 700 | start | sentence/title case; no all-caps default | localized/title growth later |
| Section heading | hierarchy | Inter 15–17, 600 | start | authored case; tracking 0 | actual screen density validation |
| Body UI text | primary prose | Inter 15–16, 400 | natural/start | sentence case; tracking 0 | normal fallback chain |
| Airport code | operational identifier | Inter 17, 600 on Opening; proportional | fixed semantic DEP/ARR cells; start | uppercase; tracking 0 | no monospace; no `tnum` |
| Flight number | operational identifier | Inter 15–17, 500/600 | fixed semantic field/column | preserve canonical uppercase; tracking 0 | provisional `ss02`; parsing semantics remain data-owned |
| Aircraft type | operational identifier | Inter 15–17, 500/600 | semantic field/column | preserve source case convention | provisional `ss02` for mixed A–Z/0–9 |
| Registration | high-consequence identifier | Inter 15–17, 500/600 | semantic field/column | preserve source uppercase/hyphen | prefer `ss02`; human error evidence OPEN |
| Date | structured data | Inter proportional outside ledger | column-defined; use `tnum` when repeated numeric format is compared | no decorative tracking | locale/format belongs product spec |
| Time / duration | comparison data | Inter 15–17, 500/600 | right; `tnum` | numeric format contract | Opening uses `HH:mm`; ledger duration semantics from MASTER |
| Career total | primary numeric value | Inter 18–22, 600 where prominent | right/end; `tnum` | no tracking | must fit at least `99,999+59` where cumulative contract applies |
| Landing count | numeric count | Inter 15–17, 500 | `tnum` in repeated/comparison contexts; proportional acceptable when isolated | no tracking | task/context decides feature |
| Metadata | secondary | Inter 13–15, 400 | start/natural | preserve content case | avoid over-compression |
| Ledger header | current product contract | preserve MASTER base ledger size, w500 | shared semantic boundaries | compact labels | exact family role remains View Logbook work |
| Ledger body | current product contract | **monospace/code w400 per MASTER** | fixed ledger semantics | preserve data | T017 does not revoke canonical mono ledger decision |
| Ledger totals | current product contract | same base size; w500/w600 per MASTER | shared numeric boundaries | `tnum` if proportional layer is ever introduced | exact family OPEN |
| Crew name | user-entered text | Inter 15–16, 400 primary run | natural; wrap | preserve entered case | multilingual fallback; no `ss02`/mono |
| Remark / free text | user-entered prose | Inter 15–16, 400 primary run; line height ~1.4 | natural; wrap | preserve user text; no forced tracking/case | Unicode/RTL/combining fallback; avoid clipping |

### Line-height policy

- compact operational single-line values: approximately 1.15–1.25 as a starting range;
- body/free text: approximately 1.35–1.5;
- large Opening statement: keep the current tight display relationship only if the exact Inter render survives all widths/scales;
- ledger: current 36px row rhythm remains product authority; do not infer a new ledger line height from this sprint.

Never use a tighter line height to hide fallback or enlarged-text failures.

---

# 6. Geometry Contract

## Opening sample route

Required invariant:

`DEP | arrow | ARR | flexible | time`

Recommended Draft 02 implementation contract:

1. DEP and ARR use equal semantic widths.
2. Their width is derived from the **selected route style under the current TextScaler**, not hardcoded from `ICN` or `NRT`.
3. Use `WWW` as an adversarial three-cap stress sentinel for the current shortlist, or measure the supported uppercase alphabet/current regional sample set with `TextPainter`; add small safety, then freeze the result for that rendered role.
4. Time width is measured after `tnum` is active, using `00:00` for the Opening clock specimen.
5. Time is right anchored.
6. Arrow owns its own fixed visual cell and optical centering; it does not change DEP/ARR widths.
7. No code is horizontally scaled, fitted, or letterspaced to fill its cell.
8. If the minimum semantic widths no longer fit, **recompose** rather than shrink type.

For Inter 600 at 17px, the measured A–Z three-cap maximum was `WWW ≈ 52.781px` (`3.105em`) and `00:45` with `tnum ≈ 48.562px`. A practical first render can therefore start around a `~3.2–3.25em` code cell, but the implementation should measure the actual chosen artifact rather than fossilize these Linux-control numbers as Flutter constants.

## 200% enlarged-text stress

At 200% text enlargement, the same semantic system remains valid but the one-line composition may not.

Preferred failure-safe order:

- reduce discretionary gaps first;
- preserve DEP/ARR/time content and target geometry;
- if necessary, recompose route/time into two semantic lines or a wider orientation layout;
- allow page scrolling;
- never use `FittedBox`, font-size reduction or code truncation to force the original one-line row.

## Dense ledger

Keep current LogMate semantic columns (`Date | Type | Reg | Flight | DEP | ARR | Block | Night | Inst | Remark`) and shared header/body/total boundaries. Font choice must not become the column-definition mechanism.

If future ledger typography changes away from the currently canonical monospace body, re-run L004-style numeric/intrinsic-width regression before changing widths.

---

# 7. Fallback / Platform Contract

## Main UI

Provisional chain:

`Inter → LogMateNotoSansKR (where glyph coverage is needed) → platform fallback`

This is a **role/fallback contract**, not proof that the current Noto KR asset is metrically matched to Inter.

T005 already rejects blind Latin x-height normalization as a generic Korean solution. Exact bundled Inter + current `NotoSansKR-wght.ttf` must be rendered together before claiming mixed-script visual balance.

## User-entered multilingual data

- Korean: use the explicit Korean fallback where available; verify actual body size/baseline/weight.
- accented Latin: main family where covered; combining-mark behavior must remain unclipped.
- Cyrillic: main family where covered by the exact selected artifact; otherwise fallback.
- Arabic/RTL: use script-capable fallback and Unicode bidi behavior; **do not uppercase, force tracking, apply `ss02`, or manually reverse strings**.
- combining marks: avoid overly tight line boxes; do not treat unsupported mark attachment as a layout problem.
- mixed script: wrapping/row height are target-renderer questions, not solved by one nominal font size.

No attempt is made to bundle one universal font for every script.

## Weight files

The current LogMate Roboto declaration includes only 400/500, while the theme requests heavier values. Flutter documentation warns against relying on synthesized/extrapolated weights when the correct face is absent.

For the Draft 02 Inter evaluation, include exact real outlines for the weights actually shown. Minimum likely set for current Opening roles: 400, 600, 700; add 500 and/or 800 only where the product really uses them. A variable file is also viable in current Flutter, but exact artifact size, weight-axis behavior and PWA delivery must be measured before using it as a production optimization.

## Android / iOS / PWA

Use the same bundled primary font artifact when practical to reduce family variance, but do **not** require pixel-identical rasterization across platforms.

Mandatory later validation states:

- Android device/emulator with exact asset;
- iOS device/simulator with exact asset and fallback runs;
- Flutter Web/PWA cold load, warm load, offline cached load and failed-font/fallback state;
- portrait/landscape/tablet compositions;
- text scaling through 200%;
- actual `tnum`, `ss02`/`ss04`, and zero feature behavior.

T016 demonstrates why loaded/fallback/failure states can have different geometry. The current sprint therefore treats PWA loading behavior as **OPEN, non-blocking for Draft 02 but required before production approval**.

---

# 8. Regional sample policy consequence

Regionalized sample routes must not tune Type to Korea or to `ICN/NRT`.

Because airport code geometry is defined by semantic cells, switching sample data among `ICN`, `LHR`, `CDG`, `JFK`, `HND`, etc. should not move the ARR/time anchors.

Type does **not** require city names to repair airport-code alignment.

For Opening Draft 02, code-only rows remain the cleaner Type baseline. If the design team compares code + city metadata, city names should be a subordinate proportional metadata role inside/under the relevant code region and must not drive the primary code anchors. Long regional city names then become a normal layout/localization stress case rather than a new identifier geometry.

---

# 9. Opening Screen Draft 02 Recommendation

## KEEP

- the mobile-portrait macro hierarchy and generous calm spacing as the starting composition;
- proportional route codes rather than converting the whole row to monospace;
- the custom vector direction arrow as an independent visual element;
- tabular time behavior;
- code-only regional sample as the default Type baseline while city metadata remains a design comparison, not a requirement.

## CHANGE

- replace implicit sequential route text with explicit `DEP | arrow | ARR | flexible | time` semantic cells;
- use Inter as the provisional family for Draft 02 candidate rendering;
- use real Inter weight files instead of synthesized heavy weights;
- keep airport codes proportional and cell-aligned;
- test mixed alphanumeric identifiers with Inter `ss02` rather than introducing an identifier monospace;
- size the time anchor after `tnum` is enabled;
- derive code/time minimum widths from actual `TextPainter` metrics under the active TextScaler and recompose when they no longer fit.

## OPEN

- final company/product font family;
- exact Inter release/artifact and static-vs-variable packaging;
- exact Flutter Android/iOS/Web metrics and rasterization;
- Inter + current Noto Sans KR optical/line-box fit;
- whether `ss02` is used globally for all mixed identifiers or only high-consequence roles;
- human recognition/error rate for identifier alternates;
- city metadata inclusion;
- final large-statement size/copy after Draft 02 render;
- production PWA font loading/cache/failure behavior;
- exact View Logbook mono family — current mono role itself remains canonical.

---

# 10. Completion questions

### 1. What provisional font candidate should Opening Draft 02 use?

**Inter.** It offers the strongest controllable identifier-disambiguation system in the tested set while retaining a neutral UI voice and robust OpenType figure features. It is provisional until the exact bundled asset is rendered in Flutter.

### 2. How should airport-code width differences be absorbed?

By **equal DEP/ARR semantic cells and fixed anchors**, not by monospace. The cell width is measured from a stress-safe three-cap specimen/current font under active text scaling.

### 3. Where should tabular figures be applied?

Repeated/comparison numeric roles: route time, durations, cumulative totals, repeated counts, ledger/table numeric fields where column comparison matters. Do not apply `tnum` to alphabetic airport codes or to prose.

### 4. What remains proportional?

UI prose, headings, airport codes, mixed identifiers, crew names, remarks/free text and most metadata. Mixed identifiers use geometry + optional disambiguation features, not full monospacing.

### 5. Which candidate has the lowest current identifier-ambiguity risk?

**Inter with `ss02` is the strongest tested configuration by available structural cues and feature control.** This is designer/feature evidence, not measured human error-rate evidence.

### 6. Can one type system span mobile portrait/landscape/tablet portrait/tablet landscape?

**Yes at the semantic-role level.** Keep roles/features stable and change layout/recomposition, not the family per device class. Exact render/breakpoints remain Draft 02 validation work.

### 7. What remains OPEN?

Exact Flutter/platform rendering, 200% reflow proof, selected artifact packaging/size, Korean fallback fit, PWA loading/failure, final product-wide family, human recognition, and exact View Logbook mono family.

### 8. Can Draft 02 start?

**Yes.** The remaining questions are validation targets for Draft 02 and production hardening, not blocking uncertainties in the route/type architecture.

---

## HANDOFFS TO OTHER SPECIALISTS

### Color
- Useful finding/context: candidate/font-feature changes can alter glyph mass and width while the semantic color system remains unchanged.
- Confirmation / transfer note: keep Color stable during Draft 02 Type comparison; later re-run critical low-luminance states with the exact chosen font.
- Scope limit: T017 establishes no contrast threshold.

### Layout / Interaction
- Useful finding/context: Opening rows now have an explicit Type→Layout contract: equal DEP/ARR semantic cells, independent arrow, right-anchored tabular time, and recompose-before-shrink at text enlargement.
- Confirmation / transfer note: confirms L003/L004 — geometry absorbs valid type variance; numeric tracks are sized after features are active.
- Scope limit: Layout owns exact breakpoint/recomposition and tablet composition.

### Web Design
- Useful finding/context: Inter is provisional, but exact PWA font loading/fallback states are not approved.
- Web application / validation consequence: test exact bundled artifact under cold/warm/offline/failed load, real service worker/cache, zoom/text enlargement and regional samples.
- Scope limit: RAQM measurements are not Web production evidence.

### Typography / Type
- Reusable project lesson: identifier alignment and identifier legibility are separate problems. Semantic columns solve the former; font/form/OpenType features refine the latter.
- Do not generalize Inter as a universal Design Studio default from this project-specific result.

---

# Final disposition

**READY FOR LOGMATE UI TRANSFER**

No blocking Type issue prevents Opening Draft 02. The next correct action is to implement the semantic route geometry and exact provisional Inter artifacts in the Draft 02 Flutter specimen, then validate the OPEN platform/fallback/enlarged-text conditions rather than extending abstract font research first.
