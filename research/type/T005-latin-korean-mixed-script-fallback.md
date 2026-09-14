# T005 — Latin/Korean Mixed-Script Fallback + Vertical-Metric Compatibility

Status: **FOUNDATION / PRACTICE + CRITIQUE — mixed-script metric/raster evidence established; browser/platform/human validation still OPEN**

Owner: Typography / Type Design Specialist  
Canonical path: `research/type/`  
Reproducible source: `research/type/T005-mixed-script-fallback-proof.py`  
Measured data: `research/type/T005-mixed-script-results.json`  
Evidence artifact: `research/type/T005-mixed-script-evidence.svg`

## Purpose

T001 identified script fallback as a distinct failure mode, but the Type program had not yet measured a real Latin/Korean pairing. T005 moves that question from abstract guidance into a controlled mixed-script experiment.

The practical question is:

> When a Latin primary face hands Hangul to a Korean fallback face, which differences are genuinely font-level, which can be normalized safely, and which must remain browser/layout/project validation questions?

This matters to Korean apps and web products because one interface can contain Latin identifiers, Arabic numerals, Hangul labels, punctuation, routes, dense rows and operational data in the same line or component.

T005 does **not** select a production font stack. The tested families are controls chosen to expose different metric relationships.

---

## RELATED DOMAIN CHECK

### Typography / Type
- Evidence checked:
  - `research/type/T001-web-typography-fallback-metrics-reflow-transfer.md`
  - `research/type/002-metrics-spacing-optical-rhythm.md`
  - `research/type/T003-minimal-font-renderer-matrix.md`
  - `research/type/T004-native-numeral-punctuation-renderer-proof.md`
- Reusable finding:
  - loading fallback and script fallback are different states;
  - font source metrics do not by themselves prove final renderer behavior;
  - numerals/punctuation are task-critical in dense operational strings.
- Replication / challenge / transfer opportunity:
  - replace generic fallback advice with real Latin/Korean font-table and raster evidence.
- Dependency / overlap:
  - browser font matching, shaping, line layout and platform rendering remain separate validation layers.

### Color
- Evidence checked:
  - `research/color/008-color-luminance-contrast-hierarchy.md`
  - `research/color/C001-web-color-user-override-resilience.md`
  - `progress/COLOR_STATUS.md`, including C003.
- Reusable finding:
  - apparent hierarchy depends on actual rendered type, not a nominal color value in isolation;
  - small or light marks should later be tested under real foreground/background and viewing conditions.
- Replication / challenge / transfer opportunity:
  - later hold mixed-script geometry constant while testing light/dark and reduced-contrast conditions.
- Dependency / overlap:
  - T005 does not establish contrast or viewing-condition thresholds.

### Layout / Interaction
- Evidence checked:
  - `research/layout/L002-whitespace-density-spatial-rhythm.md`
  - `research/layout/L002-density-validation-specimen.html`
  - `progress/LAYOUT_STATUS.md`, including the I001 running validation cycle.
- Reusable finding:
  - compactness is task-dependent;
  - long localized labels and dense rows are explicit spatial stress cases;
  - route/workspace labels can affect orientation, so fallback/wrapping failures may become interaction failures.
- Replication / challenge / transfer opportunity:
  - T005 measures one exact long Korean label from the L002 density specimen across multiple fallback pairs.
- Dependency / overlap:
  - Type supplies font/run metrics and failure hypotheses; Layout/Interaction owns whether a layout should recompose, wrap, truncate or change density.

### Web Design
- Evidence checked:
  - `progress/WEB_STATUS.md`
  - `research/web/README.md`
- Reusable finding:
  - Web owns actual browser font loading/fallback, CSS metric adjustment, reflow, zoom and page validation.
- Implementation / application validation opportunity:
  - reproduce T005 with actual CSS font stacks and inspect which font renders each cluster, line-box changes, wrap points, zoom and device-pixel behavior.
- Dependency / overlap:
  - no substantive `W###` result existed at T005 start; no browser claim is inferred.

### Other / cross-cutting / future specialist
- Evidence checked:
  - W3C CSS Fonts Module Level 4;
  - W3C CSS 2.2 line-height/leading model;
  - Microsoft OpenType `OS/2` metric specification;
  - W3C Requirements for Hangul Text Layout and Typography.
- Reusable finding:
  - CSS fallback can select different fonts for different characters/clusters;
  - equal CSS `font-size` does not guarantee equal apparent glyph size;
  - glyphs in one inline can come from different fonts and therefore different ascent/descent metrics;
  - Korean line breaking and punctuation have script-specific layout requirements.
- Dependency / overlap:
  - human reading/recognition and actual platform/browser rendering remain outside this controlled FreeType experiment.

### Overlap decision
- **EXTENSION + TRANSFER VALIDATION + METHOD CHALLENGE**
- Why:
  - T001 already defined the problem. T005 tests it with real Korean fonts and specifically challenges the tempting assumption that Latin x-height matching is a general mixed-script optical solution.

---

## 1. SOURCE — fallback is a character/cluster selection process

CSS Fonts Level 4 defines `font-family` as a prioritized list. The user agent iterates through the list until it finds an available face that can render the character or cluster. The result can vary across user agents because installed fonts and fallback behavior differ.

Source:
- https://www.w3.org/TR/css-fonts-4/

### SYNTHESIS

A mixed-script line is not necessarily one typographic object rendered by one face. It can be a sequence of runs selected from different faces with different:

- em geometry;
- cap/x-height;
- Hangul body size;
- ascender/descender tables;
- advance widths;
- punctuation forms;
- hinting/raster behavior.

Therefore a project-level statement such as “Inter 16px” is incomplete when the Korean text is actually rendered by another family.

---

## 2. SOURCE — equal `font-size` does not mean equal apparent size

CSS Fonts Level 4 explicitly notes that individual fonts can have different apparent visual sizes at the same `font-size`, because the CSS size scales the font em rather than forcing glyphs to occupy the same portion of that em.

The same specification defines `font-size-adjust` around a chosen font metric, historically x-height. Its motivating examples concern preserving apparent lowercase size when fallback occurs in bicameral scripts such as Latin.

Source:
- https://www.w3.org/TR/css-fonts-4/#font-size-adjust-prop

### SYNTHESIS

`font-size-adjust` can be useful for **same-script loading/failure fallback**, but x-height is not a direct measurement of Hangul body size.

A Korean fallback family may contain Latin glyphs with one x-height ratio and Hangul glyphs occupying a very different vertical fraction of the em. Matching the Latin x-height of the fallback does not prove that the Hangul becomes optically better matched.

This becomes a central T005 test rather than an assumption.

---

## 3. SOURCE — vertical metrics are not one universal font number

The OpenType `OS/2` table distinguishes:

- `sTypoAscender` / `sTypoDescender` / `sTypoLineGap`;
- Windows clipping metrics;
- `hhea` ascent/descent/line gap.

Microsoft states that `sTypo*` values are intended for typographically correct and portable line layout, while legacy metrics remain subject to implementation history. It also states that CJK fonts intended for vertical layout use `sTypoAscender` and `sTypoDescender` to describe the top and bottom of the ideographic em-box.

Source:
- https://learn.microsoft.com/en-us/typography/opentype/spec/os2

CSS 2.2 notes that glyphs in a single inline can come from different fonts and therefore need not share the same ascent and descent. It recommends using `sTypoAscender` / `sTypoDescender` for OpenType/TrueType where available, while also acknowledging implementation behavior.

Source:
- https://www.w3.org/TR/CSS22/visudet.html#line-height

### SYNTHESIS

Mixed-script line behavior cannot be approved by checking only one table or only the primary font.

At minimum, Type should inspect:

1. the primary font's typographic and hhea spans;
2. the Korean fallback's corresponding spans;
3. actual Hangul ink extents relative to the Latin baseline;
4. the target renderer/browser's line-box behavior.

---

## 4. SOURCE — Korean text has layout behavior that differs from Latin

The W3C Hangul layout requirements document records that Korean horizontal text may break on character or word boundaries, and that horizontal Korean writing commonly uses half-width comma/period rather than the full-width punctuation used in vertical writing.

Source:
- https://www.w3.org/International/klreq/

### Project consequence

A fallback study cannot stop at glyph shape. Long Korean labels have different legal/typical break opportunities from English labels, and punctuation behavior can interact with the fallback font's metrics and spacing.

T005 does not implement a browser line-break engine. It hands measured font behavior to Layout/Web for that next layer.

---

## 5. Controlled experiment

### Installed-font controls

The experiment resolved these local open-source fonts through Fontconfig and records the exact file SHA-256 in the companion JSON:

- Inter Regular — version `4.001`;
- Roboto Regular — version `2.138`;
- Noto Sans Regular — version `2.004`;
- Noto Sans CJK KR Regular — version `2.004`;
- NanumGothic Regular — version `3.021`;
- NanumBarunGothic Regular — version `1.000`.

No font binaries are copied into the repository.

### Pair matrix

The controlled pairs are:

1. Inter + Noto Sans CJK KR;
2. Inter + NanumGothic;
3. Inter + NanumBarunGothic;
4. Noto Sans + Noto Sans CJK KR;
5. Roboto + Noto Sans CJK KR.

These are **controls**, not recommendations.

### Rendering method

- nominal size: `20 ppem` for the primary comparison;
- renderer: FreeType;
- target: light grayscale;
- Hangul codepoints are explicitly handed to the Korean fallback;
- other codepoints prefer the Latin primary when available;
- exact font tables, glyph bounds and raster metrics are recorded;
- sample strings include identifiers, numerals, English/Korean labels and one long label transferred from the L002 density specimen.

### Scope limit

The renderer is deliberately simple. It does **not** use HarfBuzz/CoreText/DirectWrite/Skia/browser shaping and does not claim browser line layout. The proof isolates font metrics and basic raster relationships before higher-level transfer.

---

## 6. Measured metric relationships

Normalized spans are expressed in em units.

| Pair | x-height primary / fallback | x-height match scale for fallback | Typo span primary / fallback | hhea span primary / fallback |
| --- | ---: | ---: | ---: | ---: |
| Inter + Noto Sans CJK KR | 0.5459 / 0.5430 | 1.0053 | 1.210 / 1.000 | 1.210 / 1.448 |
| Inter + NanumGothic | 0.5459 / 0.5000 | 1.0918 | 1.210 / 1.000 | 1.210 / 1.150 |
| Inter + NanumBarunGothic | 0.5459 / 0.5000 | 1.0918 | 1.210 / 1.150 | 1.210 / 1.149 |
| Noto Sans + Noto Sans CJK KR | 0.5360 / 0.5430 | 0.9871 | 1.362 / 1.000 | 1.362 / 1.448 |
| Roboto + Noto Sans CJK KR | 0.5283 / 0.5430 | 0.9730 | 1.319 / 1.000 | 1.172 / 1.448 |

### Finding A — family-name or stylistic kinship does not imply vertical-metric parity

Even `Noto Sans + Noto Sans CJK KR` does not expose identical vertical spans in these font tables:

- typographic span: `1.362em` vs `1.000em`;
- hhea span: `1.362em` vs `1.448em`.

This does not mean the pair is bad. It means the project cannot infer line-box equivalence from naming or visual resemblance alone.

### Finding B — one CJK font can expose radically different candidate metric spans

Noto Sans CJK KR in this environment reports:

- `sTypoAscender = 880`;
- `sTypoDescender = -120`;
- `sTypoLineGap = 0`;
- normalized typographic span = `1.000em`;
- hhea ascent/descent = `1160 / -288`;
- normalized hhea span = `1.448em`.

That is a large table-level difference inside one font. It reinforces T001: actual application behavior must be measured rather than reconstructed from a preferred metric table.

---

## 7. Raster relationship at the same nominal size

At nominal `20 ppem`:

### Inter control

- `H`: 15 raster rows above the baseline;
- `x`: 11 rows.

### Noto Sans CJK KR Hangul

- `가`: 20 raster rows, top `18`, extending about 2 raster rows below the Latin baseline in this FreeType proof;
- `한`: 19 rows, top `18`;
- `글`: 19 rows, top `17`.

### NanumGothic Hangul

- `가`: 19 rows, top `17`;
- `한`: 18 rows, top `16`;
- `글`: 18 rows, top `16`.

### NanumBarunGothic Hangul

- `가`: 19 rows, top `17`;
- `한`: 18 rows, top `16`;
- `글`: 17 rows, top `15`.

### STUDIO JUDGMENT

A Latin cap-height comparison alone is not a sufficient mixed-script fit test. At the same nominal em size, Hangul body ink can occupy a taller and differently baseline-positioned region than Latin capitals.

That may be entirely appropriate. The design question is whether the relation is coherent in the **actual role**: navigation title, body copy, table row, identifier, button, readout or dense status line.

---

## 8. METHOD CHALLENGE — blind x-height matching can make Korean optical balance worse

The clearest result in T005 is the Inter + NanumGothic pair.

Their stored x-height ratios are:

- Inter: `0.5459em`;
- NanumGothic: `0.5000em`.

A strict Latin x-height match would scale NanumGothic by:

`0.5459 / 0.5000 = 1.0918`

At a nominal 20px role this implies roughly 21.84px, rounded to 22ppem in the raster check.

### Before x-height normalization — 20ppem

Hangul raster rows:

- `가`: 19;
- `한`: 18;
- `글`: 18.

Inter `H` at the same nominal role is 15 raster rows high.

### After x-height normalization — rounded 22ppem

NanumGothic Hangul becomes:

- `가`: 22 rows;
- `한`: 21;
- `글`: 20.

### Disposition

**REJECT: “match Latin x-height” as a generic script-fallback optical method.**

This does not reject CSS `font-size-adjust`. It limits its use.

### Revised method

- For **same-script loading/failure fallback**, x-height matching can be a useful input when lowercase apparent size drives the mismatch.
- For **Latin→Korean script fallback**, first measure Hangul body size, baseline relation, stroke/color, punctuation, numerals and line-box behavior directly.
- Only then decide whether any size adjustment is beneficial.

A metric tool should solve the metric problem it actually measures.

---

## 9. Long localized label transfer from L002

T005 includes this L002 specimen string:

`국제 분산 커버드콜 수익전략 포트폴리오 / $11,242 +1.8%`

At nominal 20ppem in the controlled unshaped advance-sum proof:

- Inter + Noto Sans CJK KR: `486px`;
- Inter + NanumGothic: `503px`;
- Inter + NanumBarunGothic: `486px`;
- Noto Sans + Noto Sans CJK KR: `474px`;
- Roboto + Noto Sans CJK KR: `472px`.

Within the three Inter-primary cases, fallback choice changes this controlled width from `486px` to `503px`, about `3.5%`.

### Scope limit

These are not browser-shaped widths, and 3.5% is not declared universally important. The design consequence depends on container width and reflow policy.

### HANDOFF consequence

Layout/Web should include fallback state when a long localized label sits close to a wrap/truncation threshold. A layout that passes only with one Korean fallback is not robust merely because the Latin primary has not changed.

---

## 10. Mixed-script approval protocol

### A. Identify the fallback condition

Name whether the project is testing:

- loading fallback;
- permanent/failure fallback;
- script fallback;
- user/browser substitution.

Do not combine them into one “fallback” test.

### B. For script fallback, compare script-specific evidence

Measure:

- Hangul body height and width;
- baseline relation to Latin caps/lowercase;
- apparent stroke/color at target size;
- punctuation and numeral integration;
- line-box/vertical-metric behavior;
- long-label widths and legal break opportunities;
- dense-row behavior;
- enlarged text/zoom behavior.

### C. Do not normalize by one metric automatically

Possible strategies include:

1. no size adjustment — preserve each font's designed em relation;
2. x-height adjustment — mainly appropriate when Latin lowercase matching is the real problem;
3. script-specific fallback sizing — potentially useful but must be justified by Hangul evidence and platform feasibility;
4. choose a better-matched fallback family rather than compensating a weak pair;
5. use one multiscript family when its Latin/Korean relationship meets the product need;
6. assign different families intentionally by semantic role instead of pretending one stack is universal.

### D. Reject fixed-height assumptions early

If controls or rows depend on one exact Latin line box, insert Korean fallback before approving height. Do not wait for localization QA to discover clipping or unwanted row growth.

---

## 11. Project Readiness Test

### When should T005 be applied?

Use this method when a product:

- mixes Korean and Latin;
- uses a Latin-focused brand/custom family with Korean fallback;
- contains dense operational rows or tables;
- uses route/navigation titles where wrapping affects orientation;
- has identifiers and numerals adjacent to Hangul;
- uses web fonts or platform-dependent fallback;
- has fixed or tightly constrained control/row heights.

### When should it not be over-applied?

Do not engineer script-specific scaling when a well-designed multiscript/system family already satisfies the product at target sizes.

Do not create a custom Korean fallback strategy only to achieve screenshot-level visual sameness if it increases implementation fragility.

### Required project inputs

1. target platforms/browser/OS versions;
2. primary and fallback families actually available;
3. primary languages and content mix;
4. representative Korean/Latin/numeric strings;
5. minimum and typical text sizes;
6. row/control height constraints;
7. wrapping/truncation/reflow policy;
8. accessibility enlargement/zoom requirements;
9. loading/performance constraints;
10. whether fallback can be explicitly controlled or is partly system-selected.

### Concrete decisions T005 can change

- fallback-family selection;
- whether a custom Latin face should be used in mixed-script compact UI at all;
- whether size/metric overrides are justified;
- minimum line-height/row-height;
- truncation/wrap policy near localized labels;
- whether one family should own all operational text while brand type is restricted to display roles;
- what Web/Flutter/native validation matrix is required before release.

### Failure conditions

Rework when:

1. Korean fallback is evaluated only by family-name similarity;
2. x-height matching is assumed to solve Hangul optical balance;
3. a primary font's vertical metrics are treated as the line's only metrics;
4. fixed-height controls are approved without real Korean fallback;
5. a fallback change moves long labels across a wrap/truncation threshold and the product has no resilient layout policy;
6. browser/platform font selection is assumed from a static FreeType proof;
7. mixed-script quality is judged only at display size;
8. localization is treated as a late content swap rather than part of the typography system.

---

## 12. What T005 establishes and what remains OPEN

### Established

- real font-table comparison across five Latin/Korean fallback pairs;
- exact installed font versions and file hashes;
- mixed-script FreeType raster evidence;
- baseline/ink-height comparison at a common nominal size;
- explicit typographic-vs-hhea span comparison;
- a concrete counterexample to blind x-height normalization;
- a long Korean label transferred from L002 and measured across fallback pairs;
- a project-ready mixed-script approval protocol.

### OPEN

- browser font selection and shaping;
- actual CSS `font-size-adjust`, `size-adjust`, ascent/descent/line-gap override behavior with Korean runs;
- CoreText, DirectWrite, Android/Skia and Flutter behavior;
- real line-box construction and wrap points on target platforms;
- Korean line-breaking behavior in complete layouts;
- human judgment/reading evidence for mixed-script balance;
- weight matching across a full family;
- Korean punctuation and broader localization-sensitive glyph coverage;
- real accessibility zoom/text-scaling tests;
- dark/light and viewing-condition transfer with Color.

**Mixed-script / fallback may advance from OPEN to PRACTICE / CRITIQUE, but not PASS.**

---

## HANDOFFS TO OTHER SPECIALISTS

### Typography / Type
- Useful finding/context:
  - Latin x-height normalization is not a general Hangul optical-matching method;
  - one Korean fallback can expose materially different typographic and hhea spans.
- Canonical section:
  - Sections 6–8.
- Confirmation / contradiction / transfer note:
  - confirms T001's script-fallback risk and adds a concrete method limitation.
- Scope limit:
  - no production stack or Korean family is selected.

### Color
- Useful finding/context:
  - mixed-script fallback can change ink area and apparent mass even when the foreground color token is unchanged.
- Canonical section:
  - Sections 7–8 and evidence SVG.
- Confirmation / contradiction / transfer note:
  - reinforces Color's requirement to validate actual rendered text rather than placeholder typography.
- Scope limit:
  - no contrast threshold or environmental reading result is claimed.

### Layout / Interaction
- Useful finding/context:
  - the L002 long Korean label changes controlled width across fallback choices; route/workspace labels can therefore cross layout thresholds because of Type, not only geometry.
- Canonical section:
  - Section 9.
- Confirmation / contradiction / transfer note:
  - transfers L002/I001 localization and orientation concerns into concrete Type evidence.
- Scope limit:
  - Type does not decide whether to wrap, truncate, stack or recompose the layout.

### Web Design
- Useful finding/context:
  - T005 supplies exact font pairs, file versions/hashes, source metrics, mixed strings and a rejected x-height-normalization heuristic for browser reproduction.
- Web application / validation consequence:
  - test actual `font-family` fallback selection, line boxes, wrap points, CSS metric overrides, zoom, DPR and font loading/failure states.
- Confirmation / contradiction / transfer note:
  - browser evidence should confirm, limit or contradict the FreeType/source-metric findings rather than silently inherit them.
- Scope limit:
  - T005 is not browser PASS evidence.

---

## Next Type priority after T005

Highest-value next directions are:

1. browser/platform transfer of T001/T003/T004/T005 once Web evidence is available;
2. a small production-outline audit with real editable curves/extrema/overlap/export QA;
3. target-platform mixed-script proof in Flutter/CoreText/Skia/DirectWrite as live project needs require;
4. Color viewing-condition transfer and L002 density transfer using the T005 strings;
5. human mixed-script balance/recognition work only after rendered target conditions are stable.

Foundation remains **NOT PASSED**.
