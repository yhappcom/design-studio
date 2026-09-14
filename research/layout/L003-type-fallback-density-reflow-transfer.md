# L003 — Type Fallback as a Layout Variable: Density, Reflow, and Spatial Priority

Status: **PRACTICE + CRITIQUE / TYPE→LAYOUT TRANSFER VALIDATION — controlled Chromium evidence established; human, cross-browser, production-font, and real-product validation remain OPEN**

Owner: Layout, Spatial & Interaction Specialist  
Canonical path: `research/layout/`  
Primary purpose: test whether Type's measured Latin/Korean fallback differences materially change Layout density/reflow decisions, and determine when Layout should absorb variance versus hand the problem back to Type.

Reproducible artifacts:

- `research/layout/L003-type-layout-transfer-playwright.py`
- `research/layout/L003-type-layout-transfer-results-summary.json`

## Question

When the same semantic content is rendered with different valid Latin/Korean fallback stacks, can a nominally identical density/responsive layout cross different wrap and row-height thresholds — and if so, what should Layout preserve, adapt, or return to Typography as a dependency?

This study extends:

- `research/layout/L002-whitespace-density-spatial-rhythm.md`
- `research/layout/L002-density-validation-report.md`
- `research/type/T005-latin-korean-mixed-script-fallback.md`
- `research/type/T004-native-numeral-punctuation-renderer-proof.md`

It is a **TRANSFER VALIDATION** study. It does not replace Type's canonical ownership of font selection, metrics, fallback suitability, or rendering.

---

## RELATED DOMAIN CHECK

### Typography / Type
- Evidence checked:
  - `progress/TYPE_STATUS.md` through T005;
  - `research/type/T005-latin-korean-mixed-script-fallback.md`;
  - `research/type/T004-native-numeral-punctuation-renderer-proof.md`.
- Reusable finding:
  - equal nominal size does not imply equal Hangul body or line-metric behavior;
  - fallback stack choice can shift the width of the exact L002 long Korean label;
  - font-level FreeType/unshaped measurements are not browser-layout proof;
  - source-equal tabular metrics do not by themselves prove runtime alignment.
- Replication / challenge / transfer opportunity:
  - use T005 control stacks in a real Chromium CSS layout and test wrap/row-height thresholds inside L002 density structures.
- Dependency / overlap:
  - Type owns whether a font pairing is intrinsically acceptable; Layout owns whether the spatial system survives valid typographic variance.

### Color
- Evidence checked:
  - `progress/COLOR_STATUS.md` through C004;
  - C001–C003 handoffs relevant to semantic state and density.
- Reusable finding:
  - apparent density can change through luminance/chroma even when geometry is fixed;
  - semantic meaning should not be repaired by color after structural hierarchy fails.
- Replication / challenge / transfer opportunity:
  - this L003 block deliberately holds color nearly constant so typography/fallback remains the principal variable; later Color transfer can hold L003 geometry constant.
- Dependency / overlap:
  - no Color threshold or environmental conclusion is claimed here.

### Layout / Interaction
- Evidence checked:
  - L002 source study and 216-condition density validation;
  - current `progress/LAYOUT_STATUS.md`;
  - I001 orientation findings where route/workspace labels are interaction-critical.
- Reusable finding:
  - semantic content and required interaction geometry must be preserved before discretionary whitespace;
  - density modes are relational policies rather than fixed pixel identities;
  - wrapping can become an orientation/interaction problem when a critical label changes geometry.
- Replication / challenge / transfer opportunity:
  - test whether the L002 adaptive principle remains robust when actual fallback stacks change text width and vertical ink behavior.
- Dependency / overlap:
  - primary ownership of this transfer decision remains Layout.

### Web Design
- Evidence checked:
  - `progress/WEB_STATUS.md`;
  - `research/web/README.md`.
- Reusable finding:
  - Web owns full production browser/page-system integration, real `@font-face`, loading/failure/script fallback, framework containers, zoom and device/browser matrices.
- Implementation / application validation opportunity:
  - reproduce L003 using production font delivery, actual browser zoom, real localized content, CSS font loading, and target devices.
- Dependency / overlap:
  - no substantive W### evidence existed at this checkpoint; L003 is Layout-owned independent browser transfer evidence, not Web canonical proof.

### Other / Cross-cutting / Future Specialist
- Evidence checked:
  - T005's cited CSS Fonts, CSS line-height, OpenType metric and Hangul layout sources;
  - controlled Chromium layout behavior in this study.
- Reusable finding:
  - fallback selection and mixed-script line layout can create different spatial outcomes under the same nominal role.
- Dependency / overlap:
  - human readability/preference and assistive-technology consequences remain untested.

### Overlap decision
- **TRANSFER VALIDATION + INDEPENDENT VALIDATION + FAILURE ANALYSIS**.
- Why:
  - T005 explicitly handed its measured fallback differences to Layout/Web. L003 tests whether those differences cross real spatial thresholds and whether Layout recomposition can absorb them without masking a true Type failure.

---

# 1. Controlled browser transfer

## Environment

- Chromium `144.0.7559.96` on Debian;
- Playwright automation;
- system-installed open-source fonts already used by T005;
- same 12-row long-Korean L002 portfolio dataset;
- no remote font loading;
- no production framework/router.

## Font stacks

The browser test uses the same control families as T005 where practical:

1. `Inter, Noto Sans CJK KR`;
2. `Inter, NanumGothic`;
3. `Inter, NanumBarunGothic`;
4. `Noto Sans, Noto Sans CJK KR`.

These remain **experimental controls, not recommendations**.

---

# 2. Direct long-label width transfer

The exact T005/L002 string was measured in Chromium at 20px:

`국제 분산 커버드콜 수익전략 포트폴리오 / $11,242 +1.8%`

| Stack | Chromium width | Minimum tested width for one line |
| --- | ---: | ---: |
| Inter + Noto Sans CJK KR | ~489.95px | 490px |
| Inter + NanumGothic | ~496.75px | 497px |
| Inter + NanumBarunGothic | ~480.42px | 481px |
| Noto Sans + Noto Sans CJK KR | ~486.95px | 487px |

## TRANSFER VALIDATION — T005 was directionally useful but not browser-identical

T005's simple FreeType/unshaped long-string proof reported approximately:

- Inter + Noto CJK: 486px;
- Inter + NanumGothic: 503px;
- Inter + NanumBarunGothic: 486px.

Chromium does **not** reproduce those values exactly. In particular, Inter + NanumBarun becomes materially narrower in this browser proof.

### SYNTHESIS

Font-level evidence is valuable for identifying risk, but **browser wrap thresholds must be measured in the actual layout stack**.

### STUDIO JUDGMENT

Do not set a production breakpoint from a font-table or standalone advance-sum result alone when a critical localized string is close to the threshold.

---

# 3. Baseline layout failure — same density token, different wrap structure

The L002 mobile/tablet composition initially used:

`name + action` on the first row, followed by status and metric/change lanes.

At **500px viewport / 125% text / intermediate density**:

- Inter + Noto CJK: the transferred long label wrapped to 2 lines;
- Inter + NanumGothic: 2 lines;
- Inter + NanumBarun: 1 line;
- Noto + Noto CJK: 2 lines.

The resulting average row heights also differed, approximately:

- 136.0px;
- 129.3px;
- 129.9px;
- 139.0px.

### Failure classification

This is **not automatically a Type failure**.

All four stacks are intentionally different controls, and the layout placed the critical name in direct competition with an action at a width where fallback variance was already known to be meaningful.

### Why this matters

A product can accidentally create different spatial rhythm, simultaneous comparison capacity, and scroll cost depending on fallback state even though its nominal density token and viewport are unchanged.

A breakpoint such as `500px` is therefore not a complete spatial contract.

---

# 4. Revision — recompose by semantic priority instead of tuning one stack

The revised narrow/enlarged-text composition does **not** add a font-specific breakpoint.

Instead it changes semantic lane ownership:

Baseline:

`name | action`

then status, metric/change.

Revised:

`name | name`

then `status | action`, then metric/change.

The name receives the full first-line width because it is the primary object identity; the action remains available but moves to the next semantic lane.

## Re-proof at 500px / 125%

Under intermediate density, all four stacks now keep the transferred long label to one line.

Average row heights remain different because the font stacks have different vertical/rendered behavior, but the **fallback-specific wrap bifurcation disappears**.

Under spacious density, the same revision reduces long-name wrapping from 4–8 wrapped names across stacks to zero for this controlled condition.

### SYNTHESIS

When typography variance causes a critical label to compete with a secondary control near a wrap threshold, the strongest fix may be **spatial reprioritization**, not a narrower font, smaller type, clipping, or a breakpoint tuned to one fallback stack.

---

# 5. Extreme stress — variance remains even after robust recomposition

At **390px / 200% text / compact density**, the baseline long label ranged from roughly **3 to 5 lines** depending on stack.

After the revised semantic-lane composition, all four controlled stacks bring that label to **2 lines**.

Average row-height spread also decreases, although it does not disappear.

### Important limit

Layout cannot and should not normalize every font difference.

If a fallback family produces materially inappropriate:

- line-box height;
- script body scale;
- weight/color mismatch;
- punctuation/numeral inconsistency;
- extreme width expansion;
- clipping risk;

then the correct response may be a **Type dependency**, not more layout compensation.

---

# 6. Layout-vs-Type decision boundary

## Layout should usually absorb the variance when

- the font pair is otherwise acceptable in the semantic role;
- the difference mainly changes wrapping near a spatial threshold;
- content can be reprioritized or recomposed without hiding meaning;
- target geometry and hierarchy can remain intact;
- one robust layout rule works across multiple valid font states.

## Return to Type when

- fallback pairing is intrinsically mismatched;
- vertical metrics cause persistent clipping or unusable row height;
- Hangul/Latin apparent scale is materially incoherent;
- numeral/punctuation behavior breaks task-critical comparison;
- fallback produces excessive width/weight differences that spatial recomposition cannot reasonably absorb;
- fixing Layout would damage every other valid typography state merely to accommodate one poor font stack.

## Shared Type + Layout decision when

- a product-specific compact density target is essential;
- localization is near a wrap threshold;
- the brand typeface has incomplete script coverage;
- tabular data requires exact numeric alignment;
- enlarged text and fallback interact with a fixed operational viewport.

---

# 7. Project decision protocol

Before approving a dense mixed-script surface, collect:

1. actual primary and fallback font families;
2. real languages/scripts;
3. critical object names, route labels and data strings;
4. representative long localization;
5. minimum supported width;
6. text enlargement/zoom requirement;
7. density mode and simultaneous-comparison requirement;
8. whether adjacent actions can move without damaging workflow;
9. task-critical numeric alignment requirements;
10. target browser/platform rendering stack.

Then test at least:

- preferred + script fallback state;
- known failure/loading fallback where applicable;
- long localized label;
- enlarged text;
- minimum container width;
- compact and normal density;
- one recomposition option that changes semantic lane priority rather than only font size/padding.

---

# 8. Failure modes

Reject or rework when:

- a breakpoint is tuned to the preferred font only;
- compact mode clips or truncates the localized primary object to preserve a secondary action;
- Layout hides a bad fallback pairing by adding arbitrary whitespace everywhere;
- Type is blamed for every wrap difference even though spatial priority is the real problem;
- Layout shrinks type to keep one-line labels rather than permitting meaningful reflow;
- one fallback state changes row structure enough to damage comparison, but the product never tests that state;
- `font-size-adjust` or metric normalization is assumed to solve Hangul body/line layout without direct evidence;
- numeric columns are considered stable because source metrics are equal even though runtime alignment has not been tested.

---

# 9. Evidence level and OPEN

Evidence established:

- actual Chromium mixed-script CSS fallback rendering using the T005 control families;
- exact long-label width and one-line threshold measurements;
- density/reflow matrix under narrow/enlarged-text conditions;
- a documented fallback-specific wrap failure;
- a semantic-lane recomposition revision;
- re-proof showing reduced fallback sensitivity.

Still OPEN:

1. production `@font-face` loading and failure fallback;
2. real browser zoom rather than synthetic root scaling;
3. Safari/Firefox/Android/iOS/Flutter transfer;
4. exact font-run inspection in each browser;
5. Korean line-breaking and punctuation under production content;
6. T004 research font / `tnum` browser application in the same density surface;
7. human search/comparison/readability evidence;
8. screen-reader/assistive-technology behavior;
9. production project font stacks and design tokens;
10. broader scripts beyond Latin/Korean.

No PASS promotion is claimed.

---

## Project Readiness Test

### When should this knowledge be applied?
- mixed-script apps/websites;
- products with incomplete primary-script coverage;
- dense lists/tables/cards near wrap thresholds;
- localized navigation/object labels;
- enlarged-text responsive surfaces.

### When should it not be over-applied?
- do not add complex recomposition rules if the product uses one stable system-font stack and real content has ample width;
- do not treat every one-line/two-line difference as failure when both preserve task performance and hierarchy.

### What concrete design decisions can change?
- lane allocation between primary label and action;
- breakpoint/recomposition policy;
- whether wrapping or truncation is allowed;
- which content has spatial priority;
- whether the problem belongs to Layout, Type, or both;
- which fallback states become mandatory QA cases.

### How should it be validated?
- actual production fonts;
- real localized strings;
- actual browser/platform renderer;
- target widths and zoom/text scaling;
- task observation where row density/comparison performance matters.

---

## HANDOFFS TO OTHER SPECIALISTS

### Typography / Type
- Useful finding/context:
  - T005 successfully predicted that Korean fallback belongs in Layout validation, but its standalone width values were not browser-identical.
  - Chromium one-line thresholds for the transferred long string ranged roughly 481–497px across the four stacks.
- Canonical section:
  - Sections 2–5 of L003.
- Confirmation / contradiction / transfer note:
  - **CONFIRMATION + LIMITATION**: confirms fallback variance matters; limits standalone FreeType/unshaped width as a production wrap predictor.
- Scope limit:
  - Layout does not judge intrinsic font quality or choose the production stack.

### Color
- Useful finding/context:
  - L003 now provides a typography-varied but color-controlled density matrix.
- Canonical section:
  - controlled transfer and revised composition.
- Confirmation / contradiction / transfer note:
  - useful future transfer: hold robust geometry/type state fixed and vary luminance/chroma to separate color-driven density from typography-driven density.
- Scope limit:
  - no Color/environment conclusion is established here.

### Layout / Interaction
- Useful finding/context:
  - primary object identity should receive spatial priority over a secondary action when fallback variance makes both compete near a wrap threshold.
  - viewport width alone is not a complete responsive contract.
- Canonical section:
  - Sections 3–6.
- Confirmation / contradiction / transfer note:
  - extends L002's adaptive-density principle with real mixed-script fallback evidence.
- Scope limit:
  - no human performance claim is made.

### Web Design
- Useful finding/context:
  - reproducible browser matrix and a concrete fallback-sensitive wrap threshold case are now available.
- Web application / validation consequence:
  - reproduce with real `@font-face`, production fallback stack, actual zoom, framework containers, target browsers/devices, and localized page structure.
- Confirmation / contradiction / transfer note:
  - current Chromium result is a transfer baseline, not Web canonical proof.
- Scope limit:
  - no W### result existed at study time.
