# T018 — LogMate Conservative Font Candidate Audit

Status: **PROJECT TRANSFER / PRACTICE + CRITIQUE — controlled FontTools + Chromium evidence established; provisional LogMate baseline selected; exact shipped Flutter/native-platform and human recognition validation remain OPEN**

Owner: Typography / Type Design Specialist  
Canonical path: `research/type/`  
Transfer target: `yhappcom/logmate`, branch `design/design-studio-proposal`  
Parent transfer study: `T017-logmate-operational-data-typography-semantic-geometry-transfer.md`

## Purpose

T017 established the LogMate operational-data contract:

`semantic geometry → role-specific Type behavior → OpenType feature → exceptional treatment`

T018 answers the next product question without opening a bespoke-font or experimental-typeface project:

> Among mature, conservative UI sans families available in the validation environment, which family is the best provisional baseline for LogMate Opening + View Logbook, and which alignment problems should Type solve through features/role rules rather than a second or monospaced family?

This is **TRANSFER VALIDATION + CONTROLLED CANDIDATE COMPARISON**, not a universal typeface ranking.

The product objective is to make Draft 02 safer and easier to implement. If two candidates are materially close, the decision favors the more ordinary, mature and already-integrated solution.

---

## Current LogMate implementation checked

Canonical product evidence checked on `yhappcom/logmate` / `design/design-studio-proposal`:

- `lib/main.dart`
- `lib/theme/logmate_theme.dart`
- `lib/screens/view_logbook_screen.dart`
- `pubspec.yaml`
- `design-studio/02-onboarding/USER_REVIEW_OPENING_01.md`
- `design-studio/02-onboarding/OPENING_SAMPLE_ROUTE_POLICY_01.md`

Important current facts:

1. The main UI family is `LogMateRoboto`.
2. `pubspec.yaml` currently bundles Roboto Regular `400` and Medium `500` only.
3. The theme nevertheless requests `600`, `700`, and `800` in several roles.
4. Opening route values are approximately `17sp`, requested at `w600`; DEP/ARR use explicit `56px` cells, arrow `36px`, time `68px`, and time uses `FontFeature.tabularFigures()`.
5. View Logbook currently forces `fontFamily: 'monospace'` for most ledger values and its flight identifier, while numeric flight subfields also request `tnum`.
6. View Logbook uses fixed column widths including DEP/ARR `50px`, registration `84px`, numeric total columns `96px`, and a `36px` row rhythm.
7. The Opening review already records that proportional airport-code widths shifted the earlier row rhythm and that `tnum` does not solve alphabetic airport identifiers.

### Product risk exposed before candidate comparison

The current ledger does **not** use a specific bundled monospace family; it requests the generic family name `monospace`. That makes the exact glyph design and metrics platform/runtime dependent.

For a product whose Type research treats exact shipped artifacts as part of QA, generic monospace is therefore a weak long-term contract even if it produces equal-width characters on one device.

---

## RELATED DOMAIN CHECK

### Typography / Type

Evidence checked:

- `T004-native-numeral-punctuation-renderer-proof.md`
- `T005-latin-korean-mixed-script-fallback.md`
- `T016-webfont-loading-fallback-metric-contract.md`
- `T017-logmate-operational-data-typography-semantic-geometry-transfer.md`

Reusable findings:

- `tnum` is an equal-advance numeric contract, not a general fixed-width text solution;
- `zero`/slashed-zero is conditional ambiguity treatment, not a universal default;
- mixed-script fallback changes font runs/metrics and requires target-runtime proof;
- exact preferred/fallback artifacts and loading state can affect geometry;
- product roles should be selected by task and data semantics, not by “technical-looking” styling.

Decision: **TRANSFER VALIDATION + PRODUCT-SPECIFIC EXTENSION**.

### Color

Evidence checked:

- current Color Stage 1 PASS status;
- C015 perceptual-context/low-light stress conclusions.

Reusable finding:

- nominal type weight does not alone establish cockpit/night readability; actual rendered stroke/color/environment remain a later product validation problem.

Current audit therefore does not choose a heavier family merely because Night mode exists.

### Layout / Interaction

Evidence checked:

- `L004-tabular-numerals-dense-comparison-transfer.md`;
- current Layout/Interaction Stage 1 PASS status;
- LogMate Opening route and View Logbook geometry.

Reusable findings:

- `tnum` can improve numeric comparison while changing intrinsic width;
- numeric feature selection and column allocation form a joint contract;
- typography is a spatial input, but Layout must survive realistic metric variation;
- semantic columns should not be replaced by spaces or by incidental glyph widths.

T018 explicitly stress-tests the current LogMate fixed cells at 100% and 200% text size.

### Web Design

Evidence checked:

- Web Stage 1 PASS status through W009;
- T016 Web-font loading/fallback handoff.

Reusable finding:

- browser rendering is a transfer layer, not proof of Flutter/Android/iOS parity.

T018 Chromium results are therefore bounded renderer evidence, not production Web/PWA PASS.

### Other / platform evidence

Current Flutter documentation checked:

- `FontFeature.tabularFigures()` maps to OpenType `tnum`;
- `FontFeature.slashedZero()` maps to OpenType `zero` when the font supplies it;
- `fontFamilyFallback` is an ordered glyph-fallback list;
- Flutter custom-font guidance explicitly warns against requesting a weight/style without the corresponding font file because the engine may simulate/extrapolate it;
- Flutter supports TTF/OTF/TTC broadly, while WOFF/WOFF2 are not supported on every Flutter platform.

Authoritative references:

- https://api.flutter.dev/flutter/dart-ui/FontFeature/FontFeature.tabularFigures.html
- https://api.flutter.dev/flutter/dart-ui/FontFeature/FontFeature.slashedZero.html
- https://api.flutter.dev/flutter/painting/TextStyle/fontFamilyFallback.html
- https://docs.flutter.dev/cookbook/design/fonts
- https://api.flutter.dev/flutter/painting/TextStyle-class.html

---

# 1. Candidate policy

The sprint deliberately excludes:

- bespoke LogMate type design;
- new/experimental families;
- decorative/display families as the main UI system;
- a second family solely to create a “technical” mood;
- stylistic-set-dependent core layout;
- generic monospace as the default ledger language.

Three mature candidates available as exact local controls were tested:

1. **Roboto** — current LogMate baseline/control;
2. **Inter** — mature screen-oriented neutral UI sans;
3. **Noto Sans** — mature multilingual ecosystem-oriented sans.

Source Sans 3 remained a legitimate future candidate but was not added merely to increase candidate count when its exact test binary was not locally available. Three materially useful controls satisfy the planned 3–5 candidate range.

Licensing/distribution references:

- Roboto official Google Fonts repository: Apache 2.0;
- Inter official repository: SIL OFL 1.1;
- Noto Latin/Greek/Cyrillic official repository: SIL OFL 1.1.

No license or distribution blocker was identified for the three controls.

---

# 2. Method

## Product corpus

Airport codes:

`ICN NRT SIN JFK LHR CDG HND DXB FRA LAX`

Identifiers:

`KE704 BA117 AF264 B737-900 B737-8 A320-200 HL8301 N12345 G-EUOH`

Time / totals / counts:

`00:45 02:18 09:55 12:40 1,284:35 9,999:59 1 11 111 8 88 888`

Ambiguity groups:

`0/O · 1/I/l · 5/S · 8/B`

## Controlled faces

Environment-local open-source controls were resolved and SHA-256 recorded in the result artifact.

- Roboto Regular + Medium, version `2.138`;
- Inter Regular + SemiBold, version `4.001`;
- Noto Sans Regular + SemiBold, version `2.004`.

The Roboto Opening control deliberately uses Medium outlines as the closest bundled-role proxy because current LogMate bundles only `400/500` while requesting `600`.

**Evidence limit:** these local Roboto files are not byte-identical proof of LogMate's repository font assets. Exact shipped-font Flutter validation remains OPEN.

## Renderer / probes

- Chromium `144.0.7559.96`;
- custom `@font-face` data-URI loading from exact control files;
- `font-synthesis:none` inside the browser specimen;
- FontTools inspection of OpenType feature tags, cmap coverage, weight metadata, versions and hashes;
- Opening airport probes at `17px`;
- ledger probes at `15px`;
- explicit `tnum` numeric probes;
- 200% size stress by doubling relevant type sizes while retaining current LogMate fixed cell widths.

Companion artifacts:

- `T018-logmate-conservative-font-candidate-audit.py`
- `T018-logmate-conservative-font-candidate-results.json`

Runtime screenshots are inspection artifacts, not canonical font assets.

---

# 3. Finding A — changing among conservative proportional sans families does not remove airport-width variance

At Opening-like `17px` identifier size:

| Candidate | narrowest | widest | mean | range | range / mean |
| --- | ---: | ---: | ---: | ---: | ---: |
| Roboto | 27.156px | 35.281px | 31.341px | **8.125px** | **25.9%** |
| Inter | 28.672px | 37.875px | 33.728px | 9.203px | 27.3% |
| Noto Sans | 25.406px | 38.859px | 32.438px | 13.453px | 41.5% |

All three candidates fit all ten airport codes inside the current `56px` Opening airport cell at 100% size.

### TRANSFER VALIDATION

This confirms T017's central premise: **a mature proportional family can reduce or increase width variance, but it does not turn alphabetic identifiers into fixed-width objects.**

In this measured set, Roboto is actually the most width-stable of the three controls. Switching to Inter or Noto Sans merely to “fix airport width” is therefore unsupported.

### STUDIO JUDGMENT

Do not replace Roboto with a more distinctive family in an attempt to solve a geometry problem that the candidate data does not solve better.

Keep semantic DEP/ARR anchors and treat family geometry as refinement inside those anchors.

---

# 4. Finding B — current 200% text scaling fails the fixed cells regardless of candidate

The current fixed geometry was stress-tested without enlarging the cells.

## Opening

At 100%:

- all tested airport codes fit the `56px` airport cell for all three candidates;
- `00:45 / 02:18 / 09:55 / 12:40` fit the `68px` time cell for all three.

At 200%:

- every candidate produced airport-code failures;
- all four tested time strings overflowed the `68px` time cell for every candidate.

Roboto was marginally more compact, but still failed most airport strings.

## View Logbook

At 100%:

- all tested airports fit the `50px` DEP/ARR column after current horizontal padding;
- tested registrations `HL8301 / N12345 / G-EUOH` fit the current registration content width;
- tested totals fit the current numeric content width.

At 200%:

- all tested airport codes failed the current ledger content width for every candidate;
- all tested registrations failed;
- both long totals `1,284:35 / 9,999:59` failed.

### SYNTHESIS

No conservative font candidate can make the current fixed cells inherently 200%-safe.

`font choice ≠ enlarged-text layout strategy`

### HANDOFF implication

Layout/UI must recompose, expand tracks, wrap/move secondary information, or otherwise adapt under large text. Type should not disguise that requirement with condensed, mono, tracking or smaller-than-requested text.

This is **not a reason to reject Draft 02**; it is an explicit enlarged-text acceptance criterion for the implementation pass.

---

# 5. Finding C — tabular numerics work without making the whole ledger monospaced

Digit advance spread at `15px`:

| Candidate | default digit spread | `tnum` digit spread |
| --- | ---: | ---: |
| Roboto | 0px | **0px** |
| Inter | 3.594px | **0px** |
| Noto Sans | 0px | **0px** |

For Inter, explicit `tnum` materially changes the numeric system from proportional to equal-advance digits. Roboto and Noto Sans controls already expose equal default digit advances in this test, but explicit `tnum` remains the correct semantic contract because a future family/subset/package may differ.

Representative `tnum` time width at `15px`:

- Roboto `02:18` — `37.359px`;
- Noto Sans `02:18` — `38.344px`;
- Inter `02:18` — `42.938px`.

Long total `9,999:59`:

- Roboto — `57.172px`;
- Noto Sans — `59.531px`;
- Inter — `66.422px`.

### STUDIO JUDGMENT

Use explicit tabular figures for comparison-oriented numeric roles even when the chosen face currently has equal default digit advances.

Use `tnum` for:

- time/duration;
- Block / PIC / SIC / Night / Instrument totals;
- career totals;
- landing counts when vertically compared;
- date columns where stable repeated numeric comparison matters;
- the **numeric sub-zone** of a split flight identifier when the UI intentionally models carrier + flight number separately.

Do **not** apply `tnum` merely because a mixed identifier contains digits:

- airport code;
- registration;
- aircraft type;
- whole unparsed alphanumeric identifiers;
- crew name / remark / prose.

---

# 6. Finding D — full-ledger generic monospace is not justified

The current View Logbook forces generic `monospace` on most value cells.

T018 finds no requirement that justifies that as the default system:

- numeric comparison can be handled with `tnum`;
- airport alignment is protected by semantic columns;
- registration and aircraft type benefit from normal identifier word shape rather than a universal equal character cell;
- the exact generic monospace face varies by platform/runtime;
- a second font system adds fallback, weight, baseline and asset/QA complexity.

### Verdict

**REWORK: remove generic `monospace` as the default View Logbook value family.**

Use the selected main family for ledger identifiers and prose-like fields; preserve semantic columns; enable tabular figures only on numeric comparison roles.

This is not a ban on monospace. A specific bundled mono companion may be reconsidered only if later controlled product evidence shows a meaningful operational advantage that proportional + geometry + `tnum` cannot provide.

---

# 7. Identifier legibility audit

Designer inspection was performed on:

- `0 / O`
- `1 / I / l`
- `5 / S`
- `8 / B`
- `KE704`
- `HL8301`
- `N12345`
- `G-EUOH`
- `B737-8`

## Default forms

All three controls retain visible structural differences for the tested strings at the specimen sizes, but **none provides a decisive universal solution to `1 / I / l` in its default forms**.

No measured human recognition/error-rate claim is made.

## `0 / O`

- Roboto control: default zero differs mainly by proportion/shape; tested control does not expose OpenType `zero`.
- Inter control: exposes `zero`; slashed-zero alternate was visibly explicit in the renderer specimen.
- Noto Sans control: exposes `zero`; slashed-zero alternate was visibly explicit.

Flutter exposes `FontFeature.slashedZero()` for fonts that provide the feature.

### STUDIO JUDGMENT

Do **not** enable slashed zero globally in Draft 02.

Reason:

- the present product evidence establishes ambiguity as a risk to audit, not a measured user-error problem;
- a global marked zero would unnecessarily change ordinary time/total appearance;
- the intervention is available later for a narrow high-risk identifier role if live-product evidence justifies it.

### OPEN

Human identifier-recognition/error testing remains deferred to app-development validation as instructed. Do not convert designer inspection into a human-performance PASS.

---

# 8. Candidate comparison

## Roboto — KEEP / provisional baseline

Strengths in this audit:

- lowest airport-code width variance of the three controls;
- most compact measured time/total system;
- all current 100% fixed-cell probes fit;
- supports `tnum`;
- already integrated into LogMate, minimizing change risk;
- mature, widely deployed UI family;
- current product visual hierarchy was already judged broadly satisfactory in mobile portrait.

Weaknesses / required correction:

- current LogMate bundle declares only 400/500 while product styles ask for 600/700/800;
- tested older Roboto control does not provide `zero`;
- exact LogMate asset binary/native rendering was not measured in T018;
- unsupported scripts still require fallback.

**Disposition: KEEP, but fix the weight/package contract.**

## Inter — KEEP AS ALTERNATE, not selected

Strengths:

- screen-oriented mature UI family;
- strong complete OpenType control set in the tested version, including `tnum` and `zero`;
- airport width variance close to Roboto;
- proper tested SemiBold face available.

Costs in this corpus:

- generally wider operational strings;
- `tnum` times/totals were materially wider than Roboto/Noto controls;
- switching the whole product yields no measured airport-geometry advantage over Roboto;
- introduces unnecessary migration/visual-change cost without a demonstrated product benefit.

**Disposition: KEEP AS SECONDARY CANDIDATE if later identifier-recognition evidence changes priorities; do not switch for Draft 02 merely to solve route alignment.**

## Noto Sans — REWORK AS MAIN CANDIDATE / KEEP AS FALLBACK ECOSYSTEM

Strengths:

- mature broad Latin/Greek/Cyrillic coverage;
- Noto provides a coherent wider script ecosystem;
- supports `tnum` and `zero` in the tested control;
- numeric widths remain compact.

Costs in this corpus:

- largest airport-code width variance by a substantial margin (`41.5%` range/mean);
- does not remove semantic-column need;
- a broader main package can increase asset cost;
- T005 already warns that related family naming does not prove mixed-script metric parity.

**Disposition: do not select Noto Sans as the primary LogMate family on the evidence of this sprint. Preserve Noto/script-specific families as fallback candidates where coverage justifies them.**

---

# 9. Provisional LogMate Type Role Matrix

| Role | Family / behavior | Weight direction | Alignment / geometry | Numeral behavior | Case / tracking | Fallback / OPEN |
| --- | --- | --- | --- | --- | --- | --- |
| Product name / temporary wordmark | Roboto proportional | 700 only with real 700 asset | normal flow | default | authored case; restrained tracking | logo/wordmark design separate |
| Screen title / main statement | Roboto proportional | 700 with real asset | composition-owned | default | sentence/title case | text scaling/reflow validate |
| Section heading | Roboto proportional | 500–700 by hierarchy | layout-owned | default | avoid decorative tracking | exact token later |
| Body UI | Roboto proportional | 400 | natural | proportional/default | normal | platform/user-data fallback |
| Airport code | Roboto proportional identifier | **500 provisional** | fixed semantic DEP/ARR anchor | none | uppercase code; tracking 0 | no mono by default |
| Flight carrier designator | Roboto proportional identifier | 400/500 | carrier sub-zone | none | uppercase | current split geometry useful |
| Flight numeric sub-zone | Roboto | 400/500 | numeric sub-zone | **tnum** | normal | suffix letter stays proportional |
| Aircraft type | Roboto proportional identifier | 400/500 | semantic column | default | canonical identifier case | no whole-field tnum |
| Registration | Roboto proportional identifier | 400/500 | semantic column | default | canonical identifier case | `zero` treatment OPEN |
| Date | Roboto | 400 | column contract | **tnum when repeated** | locale format owns punctuation | localized width OPEN |
| Time / duration | Roboto | 400–500 | **right anchor** | **tnum** | normal | colon must remain clear |
| Career total | Roboto | 500/600 only with real asset | right anchor | **tnum** | grouping punctuation tested | max-value width contract |
| Landing count | Roboto | 400/500 | right aligned in comparison tables | **tnum** | normal | dynamic width stress |
| Metadata | Roboto proportional | 400 | natural | role-dependent | normal | fallback-aware |
| Ledger header | Roboto proportional | 500 | semantic columns | default | concise labels | 200% recompose |
| Ledger body identifier | Roboto proportional | 400/500 | semantic columns | no global tnum | tracking 0 | **remove generic monospace** |
| Ledger numeric body | Roboto | 400/500 | right aligned | **tnum** | normal | max magnitude/locales |
| Crew name | Roboto + fallback | 400 | natural/wrap | proportional | preserve entered case | multilingual/Unicode |
| Remark / free text | Roboto + fallback | 400 | natural/wrap | proportional | preserve entered text | RTL/combining marks OPEN |

### Weight rule

Do not keep requesting weights that are absent from the bundled family and rely on simulation.

For the conservative Draft 02 baseline, prefer an explicit asset set such as:

- `400` Regular;
- `500` Medium;
- `700` Bold for genuinely strong hierarchy;

or an appropriately validated variable font package.

Do not request `600/800` until the selected shipped artifact actually provides those weights or the product deliberately changes its token system.

---

# 10. Geometry Contract

Typeface changes must not alter these semantic relationships:

## Opening route

`DEP | arrow | ARR | flexible | TIME`

- DEP and ARR have independent semantic anchors;
- arrow has its own slot;
- time has a right anchor;
- airport-code tracking is not used to fake equal width;
- time uses `tnum`;
- the row may need adaptive geometry/recomposition at enlarged text.

## View Logbook

- each field owns a semantic column;
- numeric comparison columns align right and use `tnum`;
- carrier and flight-number sub-zones may remain separate when the product model intentionally exposes that structure;
- identifier columns use the main proportional family by default;
- no spaces are used as layout;
- fixed column widths are validated against actual production strings/features before release;
- at large text scale, column/row geometry must adapt rather than clipping content.

---

# 11. Fallback / Platform Contract

## Product-authored UI

Current scope is English-only. The main UI can therefore remain a single primary family.

## User-entered / imported data

Must remain Unicode-safe. Do not assume the primary Latin family covers:

- Korean;
- Arabic/RTL;
- every Cyrillic extension;
- combining-mark sequences;
- mixed-script names/remarks/imported strings.

Current LogMate already contains a `NotoSansKR-wght.ttf` asset of about `10.4MB`, but T018 does not claim that simply declaring that file solves multilingual line metrics or platform behavior.

Provisional strategy:

1. primary UI/Latin operational family: Roboto;
2. preserve an explicit `fontFamilyFallback` seam for user-data roles;
3. evaluate exact Roboto + Noto Sans KR line metrics/rendering before making the Korean fallback global;
4. use platform/system fallback for unbundled scripts only as an interim compatibility path, not as a typography-fidelity PASS;
5. test Arabic/RTL directionality and script-specific line boxes separately when live data requires them.

Flutter documents `fontFamilyFallback` as ordered glyph fallback, followed by platform fallback if no declared family contains the glyph.

## Platform evidence boundary

T018 measured Chromium/Linux controls. Still OPEN:

- exact LogMate Flutter asset rendering;
- Android device rendering;
- iOS device rendering;
- PWA production font loading/cache/failure;
- exact CoreText/Skia/Flutter paragraph differences;
- device pixel ratio and physical display;
- 200% Flutter text scaling with final responsive geometry;
- screen-reader/AT behavior;
- human identifier-recognition evidence.

No native-platform PASS is claimed.

---

# 12. Opening Draft 02 Recommendation

## KEEP

- current mobile-portrait hierarchy as a reference composition;
- Roboto as the **provisional main family**;
- separate DEP / arrow / ARR / TIME geometry;
- proportional airport identifiers;
- explicit `tnum` for time;
- current principle of regional sample substitution rather than ICN-specific tuning.

## CHANGE

- normalize Type tokens to actually shipped weights; stop relying on missing `600/700/800` assets;
- use `500` as the provisional operational-identifier emphasis if keeping the current Regular/Medium package during Draft 02 exploration;
- add a real Bold `700` asset before treating 700 as production-approved, or adopt a validated variable package;
- keep airport tracking at `0` rather than widening/narrowing individual codes;
- include 200% text-size stress in the Draft 02 render matrix; current fixed cells are not sufficient there.

## OPEN

- exact bundled Roboto artifact/native-device metrics;
- whether future human evidence justifies slashed zero for a narrow identifier role;
- final line-height tokens;
- exact Korean fallback pairing and line metrics;
- Arabic/RTL fallback and layout;
- final enlarged-text recomposition behavior.

---

# 13. View Logbook Recommendation

## KEEP

- semantic column model;
- 36px row rhythm as a 100% baseline subject to scaling validation;
- right alignment for Block/Night/Instrument totals;
- split carrier / flight-number zones where they reflect product structure;
- `tnum` on numeric flight-number sub-zone and numeric comparison roles.

## CHANGE

- remove the blanket `fontFamily: 'monospace'` from ledger values;
- use Roboto proportional identifiers for Date/Type/Registration/DEP/ARR/Flight carrier;
- keep explicit `tnum` for duration/total/count columns;
- verify column widths after the Type change rather than preserving widths by assumption;
- make enlarged-text behavior adaptive rather than expecting a different family to fit fixed tracks.

## OPEN

- final column widths after actual Flutter rendering;
- 200% row/track recomposition;
- native Android/iOS comparison;
- human scan/error evidence.

---

# 14. Why no custom LogMate font is justified now

T018 directly tests the product failure that prompted the custom-font question.

Results do **not** show a missing typeface category that only bespoke design can solve:

- Roboto has the lowest measured airport width variance of the tested mature candidates;
- all candidates support the 100% route geometry;
- all candidates still require semantic columns;
- all candidates fail the existing fixed-cell 200% stress;
- numeric alignment is already solved by standard `tnum` behavior;
- the remaining `1/I/l` concern is not solved decisively by another conservative candidate and lacks human-error evidence.

Therefore a bespoke LogMate family would currently add large design, engineering, licensing/QA and platform-validation cost without a demonstrated product requirement.

**Custom typeface work remains out of scope unless later evidence identifies a concrete requirement that mature families cannot satisfy.**

---

# 15. Completion questions

### 1. Opening Draft 02 provisional baseline?

**Roboto — KEEP as provisional baseline.** Do not switch families merely to fix airport alignment.

### 2. How should airport-code width difference be absorbed?

By **semantic DEP/ARR anchors plus proportional Roboto identifiers**. A font family switch does not remove the width variance.

### 3. Where should tabular figures apply?

Time/duration, repeated totals/counts, comparison-critical dates/numbers, and deliberately separated numeric flight-number zones.

### 4. What stays proportional?

General UI, airport code, aircraft type, registration, whole mixed identifiers, crew names, remarks and free text.

### 5. Which tested candidate has the lowest identifier-misread risk?

No human error rate is established. Designer inspection does not justify a universal winner. Inter/Noto provide an optional slashed-zero feature; all three retain some `1/I/l` similarity. **This remains OPEN for live-product validation, not a blocker for Draft 02.**

### 6. Can one type system span mobile portrait / landscape / tablet portrait / tablet landscape?

**Yes at the role/token level.** Exact geometry must recompose by form factor and enlarged-text state; the current fixed cells do not survive 200% unchanged.

### 7. What remains OPEN?

Exact shipped Roboto artifact, proper weight package, Flutter native Android/iOS metrics, PWA loading/failure, multilingual fallback pairing, 200% adaptive geometry, and human identifier recognition.

### 8. Can Draft 02 start?

**Yes.** The remaining items are implementation/validation gates, not a blocking family-selection problem.

---

# Final transfer verdict

## **READY FOR LOGMATE UI TRANSFER**

Provisional Type direction:

> **Roboto main family + real declared weights + proportional operational identifiers + semantic columns + explicit tabular numeric roles + multilingual fallback seam.**

Do not replace the entire ledger with monospace. Do not create a LogMate typeface. Do not switch to a more novel family merely to make the data look technical.

The next validation should use the exact Draft 02 Flutter build and shipped font assets.

---

## HANDOFFS TO OTHER SPECIALISTS

### Layout / Interaction

**TRANSFER + LIMITATION.** The existing semantic-column direction is confirmed. T018 additionally shows that the current fixed Opening/Ledger cells fail a 200% type-size stress for all tested families. Large-text recomposition is now an explicit Layout acceptance criterion; do not solve it by shrinking Type.

### Color

Roboto remains provisional; this creates a stable Type input for Night-theme iterations. No low-light/cockpit readability PASS follows from the family selection. Validate exact rendered weight/color/device later.

### Web Design

PWA must validate exact production font loading/failure/fallback and enlarged text in the real Flutter Web build. Chromium data-URI controls are not production Web evidence.

### LogMate UI / product team

For Draft 02:

1. retain Roboto provisionally;
2. replace blanket ledger monospace with role-specific proportional/`tnum` styles;
3. stop relying on unavailable weights;
4. preserve DEP/ARR/time semantic anchors;
5. add 200% text-size stress to the render matrix;
6. keep slashed zero OPEN rather than enabling it globally;
7. do not start custom-font work.
