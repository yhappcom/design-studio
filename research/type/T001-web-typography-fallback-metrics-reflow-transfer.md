# T001 — Web Typography Transfer: Fallback Metrics, Font Loading, Zoom/Reflow, and Data Stability

Status: **FOUNDATION / TRANSFER VALIDATION BASELINE — browser/device proof still required**

Owner: Typography / Type Design Specialist  
Canonical path: `research/type/`  
Primary purpose: establish what Type must specify, what Web must validate, and where font design ends and browser/layout behavior begins.

## Question

When typography moves from a type specimen or static UI composition into a real website or web app, which typographic properties must remain stable, which can be normalized with web-platform mechanisms, and which must be treated as browser/application validation rather than assumed from the font alone?

This study is deliberately **Type-led but Web-facing**. It does not replace Web Design's canonical ownership of page systems, browser behavior, responsive composition, or frontend validation.

---

## RELATED DOMAIN CHECK

### Typography / Type
- Evidence checked:
  - `research/type/002-metrics-spacing-optical-rhythm.md`
  - `research/type/005-numerals-punctuation-systems.md`
  - `research/type/009-typography-as-information-architecture.md`
- Reusable finding:
  - contour, sidebearing, advance, sequence rhythm, and raster result are separate layers;
  - tabular/proportional figure behavior is a task decision, not a stylistic absolute;
  - hierarchy must survive text growth rather than depend on one nominal size.
- Replication / challenge / transfer opportunity:
  - transfer those principles into real web-font loading, fallback, zoom, reflow, and browser feature conditions.
- Dependency or overlap:
  - browser rendering and page reflow require Web Design validation.

### Color
- Evidence checked:
  - `research/color/008-color-luminance-contrast-hierarchy.md`
- Reusable finding:
  - text hierarchy cannot be repaired by low contrast or bold weight alone;
  - small/thin text is particularly vulnerable under high glare and reduced edge definition.
- Replication / challenge / transfer opportunity:
  - future browser proof should combine fallback/zoom tests with representative foreground/background conditions.
- Dependency or overlap:
  - Color owns canonical contrast/viewing-condition evidence.

### Layout / Interaction
- Evidence checked:
  - `research/layout/006-grid-composition-hierarchy.md`
  - `research/004-accessibility-reflow-targets-focus.md`
- Reusable finding:
  - responsive systems preserve semantic relationships rather than exact coordinates;
  - enlarged text and narrow width must not produce clipping or avoidable two-dimensional scrolling.
- Replication / challenge / transfer opportunity:
  - test whether font substitution, metric mismatch, and text growth break those spatial relationships.
- Dependency or overlap:
  - Layout/Interaction owns canonical responsive geometry and task-flow behavior.

### Web Design
- Evidence checked:
  - `progress/WEB_STATUS.md`
  - `research/web/README.md`
- Reusable finding:
  - Web Design explicitly owns actual browser/font-loading/fallback/wrapping/zoom validation and must hand failures back to Type.
- Implementation/application validation opportunity:
  - build real browser proofs for font loading, fallback, line wrapping, localized content, zoom/reflow, and numeric alignment.
- Dependency or overlap:
  - there is not yet a substantive `W###` study, so T001 establishes a Type-side transfer contract rather than duplicating existing Web evidence.

### Other / cross-cutting / future specialist
- Evidence checked:
  - WCAG reflow/resize/text-spacing requirements through W3C accessibility guidance.
- Reusable finding:
  - typographic behavior must remain usable under user-controlled enlargement and spacing changes.
- Dependency or overlap:
  - human reading performance and assistive-technology behavior remain broader than Type alone.

### Overlap decision
- Reuse / deliberate repetition / extension / contradiction review / method comparison / transfer validation / project-specific study:
  - **TRANSFER VALIDATION + EXTENSION**.
- Why:
  - existing Type research is strong at metric/role principles but incomplete at real browser fallback and reflow. Web Design is newly established and needs precise Type-owned requirements it can test rather than a vague request to “check typography.”

---

## 1. Four different fallback conditions must not be conflated

**STUDIO JUDGMENT**

A project should distinguish at least four conditions because they produce different design risks.

### A. Loading fallback

The preferred web font exists but has not finished loading. The user may temporarily see another face depending on `font-display` and browser behavior.

Primary risks:
- line-wrap change;
- navigation width change;
- button/control width change;
- row-height change;
- cumulative layout shift;
- visible hierarchy change if x-height/weight perception differs strongly.

### B. Failure fallback

The preferred resource fails or is unavailable and the fallback becomes permanent.

Primary risks:
- persistent hierarchy drift;
- persistent wrapping and density change;
- ambiguous numerals/identifiers if the fallback is structurally weaker;
- line-height or clipping problems in mixed-script content.

### C. Script fallback

The primary family does not cover every character, so another family renders unsupported scripts or symbols inside the same interface.

Primary risks:
- baseline and apparent-size mismatch;
- inconsistent stroke color/weight;
- line-box growth;
- punctuation mismatch;
- Korean/Latin or other mixed-script hierarchy becoming visually uneven.

### D. User/browser substitution

User styles, accessibility settings, browser behavior, unavailable local fonts, or other user-agent conditions may replace or alter the intended typographic result.

Primary risks:
- assumptions based on exact font metrics no longer hold;
- fixed-height controls clip or overflow;
- hierarchy that depended on a narrow width or exact cap/x-height ratio collapses.

**Project consequence:** “We have a fallback font” is not a sufficient specification. The fallback **scenario** must be named.

---

## 2. SOURCE — OpenType vertical metrics are not one universal line-height number

Microsoft's current OpenType `OS/2` specification distinguishes typographic ascender/descender/line-gap values from Windows clipping metrics and legacy platform metrics. It states that `sTypoAscender`, `sTypoDescender`, and `sTypoLineGap` are intended for typographically correct, portable line layout and describes `USE_TYPO_METRICS` as the flag selecting those typographic values for default line spacing.

Source:
- https://learn.microsoft.com/en-us/typography/opentype/spec/os2

It also notes that values should be appropriate for the primary languages a font is designed to support rather than mechanically forced to equal UPM.

### SYNTHESIS

The Type specialist must treat vertical metrics as part of the product contract, not merely font-source metadata.

For a project using a custom family, document:
- intended ascender/descender behavior;
- whether marks/accents exceed common Latin bounds;
- expected line-gap strategy;
- script coverage and likely fallback scripts;
- clipping-risk glyphs;
- whether the font is designed for stable UI line boxes or more generous editorial composition.

### OPEN

Actual browser engines may obtain or apply font metrics through platform/font-stack behavior that must be tested. The font table alone does not prove identical line-box output across browsers and OSes.

---

## 3. SOURCE — the web platform can override fallback metrics

CSS Fonts Module Level 4 defines `ascent-override`, `descent-override`, and `line-gap-override` descriptors for `@font-face`. The specification explicitly states that user agents can otherwise draw metric values from different places in a font file, which can lead to different text layouts.

Source:
- https://www.w3.org/TR/css-fonts-4/#font-metrics-override-desc

MDN documents `size-adjust` as an `@font-face` descriptor that scales glyph outlines and associated metrics for a specific face, including advances and baseline-related metrics.

Source:
- https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/size-adjust

MDN also documents `font-size-adjust` as a property intended to preserve a chosen font metric such as x-height across font substitutions, with `ex-height` as the default metric basis.

Source:
- https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size-adjust

### SYNTHESIS — three different tools, three different jobs

1. **`size-adjust`** changes the rendered scale of one defined font face and its metrics.
2. **metric overrides** (`ascent-override`, `descent-override`, `line-gap-override`) control line metrics for that face.
3. **`font-size-adjust`** helps maintain a chosen apparent metric relationship, commonly x-height, when different fonts are used.

These are not interchangeable and none makes two typefaces optically identical.

### STUDIO JUDGMENT

Metric normalization is justified when it reduces harmful layout instability **without damaging the fallback face itself**.

Do not normalize blindly to make screenshots align. Check:
- lowercase and cap apparent size;
- line breaks;
- numeral width;
- accents/diacritics;
- mixed-script lines;
- control heights;
- dense table rows;
- whether the adjusted fallback now appears too large, too dark, or too tight.

---

## 4. SOURCE — font loading is observable state, not an invisible implementation detail

The CSS Font Loading API exposes font loading through `FontFace`, `FontFaceSet`, and `document.fonts`. MDN documents that authors can trigger and observe loading and that `document.fonts.ready` resolves after used fonts are resolved and layout operations complete.

Sources:
- https://developer.mozilla.org/en-US/docs/Web/API/CSS_Font_Loading_API
- https://developer.mozilla.org/en-US/docs/Web/API/Document/fonts

CSS Fonts defines `font-display` values including `block`, `swap`, `fallback`, and `optional`.

Source:
- https://www.w3.org/TR/css-fonts-4/#font-display-desc

### SYNTHESIS

Font loading is a visible product state because text can change geometry or appearance during the transition.

### STUDIO JUDGMENT

Web typography validation should include at minimum:
- first render before preferred font is available;
- post-load render;
- permanent font failure;
- cached/fast-load condition;
- slow-load condition on representative pages;
- critical localized/script-fallback content.

For a dashboard or operational product, also compare whether loading changes:
- numeric column alignment;
- row density;
- timestamp width;
- identifier legibility;
- label truncation;
- action position.

Do not judge only the final loaded screenshot.

---

## 5. SOURCE — resize, reflow, and text spacing are user-controlled stress conditions

WCAG requires text to be resizable up to 200% without loss of content or functionality (SC 1.4.4), and reflow guidance requires vertically scrolling content to work at a width equivalent to 320 CSS pixels without avoidable two-dimensional scrolling except where two-dimensional presentation is essential (SC 1.4.10). WCAG also requires no loss of content/functionality when specified text-spacing adjustments are applied (SC 1.4.12).

Sources:
- https://www.w3.org/WAI/standards-guidelines/act/rules/
- https://www.w3.org/WAI/standards-guidelines/wcag/new-in-21/
- https://www.w3.org/WAI/fundamentals/accessibility-principles/

### SYNTHESIS

Web typography cannot be approved at one nominal `font-size` and one viewport.

A type system must be evaluated as part of a **reflowing content system**.

### STUDIO JUDGMENT

For project validation, test at least:
- default browser text size;
- user zoom / enlarged text conditions;
- narrow viewport or equivalent magnification condition;
- long localized labels;
- increased line/letter/word spacing where applicable;
- fallback-font state under the same stresses.

A typographic role is not robust if its hierarchy survives only when the preferred font is loaded at the nominal size.

---

## 6. Fallback matching should be based on task-critical metrics, not visual resemblance alone

**STUDIO JUDGMENT**

When choosing a fallback stack, compare the characteristics that affect the actual product task.

### For prose/editorial pages

Prioritize:
- comfortable apparent size;
- line length and wrap similarity;
- paragraph color;
- language coverage;
- acceptable line-height behavior.

### For dense UI/navigation

Prioritize:
- label width behavior;
- x-height/cap-height compatibility;
- weight perception;
- compact readability;
- control-height stability.

### For data tables/readouts

Prioritize:
- figure width behavior;
- availability of tabular figures where the product relies on them;
- punctuation placement;
- `0/O`, `1/I/l`, `5/S`, `8/B` distinction where relevant;
- baseline and row-height stability.

### For multilingual products

Prioritize:
- script coverage;
- Latin/non-Latin apparent-size balance;
- baseline relation;
- stroke/color compatibility;
- punctuation and numeral integration;
- line-box behavior.

A fallback can be visually “similar” in a type specimen yet be unsuitable for the product's critical strings.

---

## 7. Numeric stability is a separate web-transfer contract

Existing Type evidence in `005-numerals-punctuation-systems.md` establishes that tabular figures are an advance-width contract, not a contour recipe.

### STUDIO JUDGMENT

For web products that compare changing values in columns, Type should explicitly hand Web:
- whether the intended family supports `tnum`;
- which roles require tabular vs proportional figures;
- required punctuation behavior (`: + , . / -` etc.);
- ambiguity requirements;
- representative proof strings.

Web should validate actual browser application of the chosen CSS feature path and fallback behavior rather than assume font metadata guarantees application.

Recommended test strings:

```text
00112233445566778899
010101 808080 111888
0O 1I 5S 8B
23:59
1+05 12+40 999+59 99,999+59
-12.5 / 12-34
```

### OPEN

Browser-specific feature application, fallback mixing, variable-font axis behavior, and script-specific numeral substitution still require actual Web validation.

---

## 8. Type-versus-Web responsibility boundary

### Typography / Type owns

- intended text roles;
- family/face suitability;
- glyph distinction and numeral/punctuation architecture;
- spacing and metric quality;
- OpenType feature meaning;
- vertical-metric intent;
- fallback-compatibility criteria;
- test strings and typographic failure conditions.

### Web Design owns

- actual `@font-face` loading strategy in the product context;
- page/component behavior before, during, and after load;
- real fallback stack application;
- responsive line wrapping and intrinsic sizing;
- browser zoom/reflow behavior;
- native/browser constraints;
- real browser/device validation;
- implementation-aware choice among available CSS mechanisms.

### Shared decision

A project should not approve web typography until both sides agree that:
- the type choice is intrinsically suitable;
- the page system survives fallback and loading;
- hierarchy survives reflow and enlargement;
- numeric/data behavior survives real browser use;
- localization does not create a different visual system by accident.

---

## 9. Project decision protocol

Before recommending a web type system, collect:

1. primary languages/scripts;
2. content types: prose, navigation, forms, tables, identifiers, readouts;
3. critical numeric strings and alignment needs;
4. minimum and typical viewport/context density;
5. accessibility text-enlargement expectations;
6. loading/performance constraints;
7. whether brand typography is essential or optional;
8. acceptable fallback behavior if the preferred font never loads;
9. whether line-height/row-height is fixed by product constraints;
10. target browser/device range.

Then classify the recommendation:

- **SAFE TO TRANSFER** — typography remains acceptable across preferred/fallback and expected scaling conditions;
- **CONDITIONAL** — acceptable only with measured metric normalization or specific layout adaptation;
- **DO NOT TRANSFER AS-IS** — font choice or hierarchy depends on conditions the web product cannot reliably preserve.

---

## 10. Failure modes

Reject or rework when:

- the preferred face looks strong only after load but fallback causes major structural shift;
- navigation/control sizing depends on exact label widths with no growth path;
- a fallback matches x-height but produces materially different line length or weight color;
- line boxes are tuned so tightly that diacritics/script fallback collide or clip;
- tabular-data alignment disappears under fallback with no acceptable degradation strategy;
- `font-display` is chosen only for speed metrics without evaluating the visible typographic transition;
- brand display type is forced into small operational roles where fallback/legibility cost is high;
- zoom/reflow is treated as a Layout-only problem even though font metrics and hierarchy materially contribute;
- metric overrides are used to force screenshot parity while harming reading quality.

---

## 11. Project Readiness Test

### When should this knowledge be applied?
- any site/app using web fonts, custom fonts, multilingual fallback, dense data, or a typography hierarchy sensitive to wrapping/row height.

### When should it not be over-applied?
- simple content where system fonts are accepted and font substitution does not materially change task success; do not add metric-override complexity without a demonstrated problem.

### What project inputs are required?
- language/script set, content roles, target browsers/devices, critical strings, loading constraints, density, accessibility requirements, and brand priorities.

### What concrete decisions can it change?
- family/fallback selection;
- whether to use a brand face for body/UI roles;
- vertical metrics and line-height strategy;
- `font-display` strategy;
- use of size/metric adjustment;
- tabular-figure policy;
- responsive component allowances;
- acceptance criteria for implementation.

### Alternatives and trade-offs
- system font: highest local availability and lower loading complexity, weaker bespoke identity;
- custom family + raw fallback: strongest identity, higher transition/layout risk;
- custom family + metric-tuned fallback: reduced shift, added implementation/testing complexity;
- role-separated system: custom identity/display plus robust operational/system text, less typographic uniformity but often lower risk.

### Failure modes
- layout shift, clipping, wrap drift, density drift, numeral ambiguity, mixed-script mismatch, lost hierarchy, feature loss, excessive implementation tuning.

### Which peer evidence is required?
- Color for actual contrast/viewing contexts;
- Layout/Interaction for responsive/reflow/task geometry;
- Web Design for real browser/font-loading/input/device behavior.

### How does the recommendation change under different constraints?
- higher performance pressure favors smaller/subset/system-font strategies;
- stronger brand mandate may justify more custom typography but raises fallback validation burden;
- data-dense products raise numeral/metric stability priority;
- multilingual products raise script/fallback/vertical-metric priority;
- accessibility-heavy environments raise reflow/enlargement resilience priority.

### How should it be validated?
- real browser prototype with preferred font, loading fallback, permanent fallback, localized text, zoom/reflow, numeric strings, and representative Color/Layout conditions.

**Result:** T001 is project-useful as a decision framework, but it is **not PASS evidence for browser behavior** until Web Design or a Type-led browser experiment records real rendered results.

---

## OPEN / NEXT VALIDATION

1. real browser comparison of at least two fallback strategies using `size-adjust` and metric overrides;
2. browser/OS comparison of line-box behavior for the same font files;
3. mixed Latin/Korean fallback specimen with long labels and dense rows;
4. numeric column test with preferred font, fallback font, and font-loading transition;
5. user zoom / 320-CSS-pixel-equivalent reflow proof;
6. at least one failure → adjustment → re-test cycle;
7. determine which findings are stable enough to become a reusable Type→Web handoff checklist.

---

## HANDOFFS TO OTHER SPECIALISTS

### Typography / Type
- Useful finding/context: fallback is four distinct conditions; Type must specify metric/feature/fallback criteria, not only a font family name.
- Canonical section: §§1–3, 6–9.
- Confirmation / contradiction / transfer note: extends Studies 002/005/009 from static/type-system logic into web-transfer requirements.
- Scope limit: no real-browser PASS yet.

### Color
- Useful finding/context: fallback and zoom can change apparent weight/x-height, so text contrast tests should include representative fallback and enlarged-text states when typography changes materially.
- Canonical section: §§3, 5, 11.
- Confirmation / contradiction / transfer note: confirms that numeric contrast alone does not prove readable hierarchy.
- Scope limit: Color remains canonical owner of luminance/contrast evidence.

### Layout / Interaction
- Useful finding/context: wrap/row-height/layout shift can originate in font substitution and vertical metrics, not only grid rules.
- Canonical section: §§1, 5, 8–10.
- Confirmation / contradiction / transfer note: extends existing reflow principles with font-loading/fallback causes.
- Scope limit: Layout/Interaction remains canonical owner of responsive and behavioral design.

### Web Design
- Useful finding/context: T001 defines concrete browser validation states and Type-owned acceptance inputs for web typography.
- Web application / validation consequence: test loading fallback, permanent fallback, script fallback, metric adjustment, zoom/reflow, and numeric-feature behavior on complete pages/components rather than isolated text samples.
- Confirmation / contradiction / transfer note: this is an outgoing Type→Web validation contract; Web should return any browser findings that confirm, limit, or contradict these assumptions.
- Scope limit: no `W###` study existed at the start of T001; actual browser evidence remains Web-owned unless independently reproduced as Type-led transfer validation.
