# T011 — Layout / multi-script release contract through packaging and subsetting

Status: **PRACTICE + CRITIQUE / bounded structural release QA**  
Date: 2026-09-15  
Foundation: **NOT PASSED**

## Question

After T009 proved that a parseable subset can lose a required `tnum` feature, and T010 proved that a parseable variable WOFF2 can retain a visible axis while losing authored axis semantics, what additional product contracts can disappear while glyph coverage still looks superficially correct?

T011 tests three release-sensitive contracts together:

1. **GPOS kerning** — `A V = -80u`;
2. **localized GSUB closure** — `latn/TRK locl` maps `i` to a Turkish alternate while retaining the intended 380-unit advance;
3. **line-metric identity** — exact `hhea` and `OS/2` values survive packaging/subsetting.

The bounded character set also includes `한` to prove that requested Latin + Hangul cmap coverage can survive while layout behavior does not.

## RELATED DOMAIN CHECK

### Typography / Type
- Evidence checked: T005 mixed-script fallback; T008 binary release QA; T009 `tnum` packaging/subsetting contract; T010 variable-axis package contract.
- Reusable finding: parseability, table presence, glyph coverage, feature semantics and target behavior are different approval layers.
- Extension: T011 expands the package contract from one GSUB numeral feature to GPOS pair positioning, language-system binding, localized alternate closure and horizontal line metrics.

### Color
- Evidence checked: C009 Type→Color rendering transfer in `progress/COLOR_STATUS.md`.
- Reusable finding: exact Type weight/fallback/render condition can change practical rendered prominence even when semantic Color roles remain fixed.
- Transfer opportunity: T011 establishes that the exact shipped package must also preserve layout features and line metrics before Color-role rendering is considered stable.
- Scope: no Color threshold or readability claim is made here.

### Layout / Interaction
- Evidence checked: L003 fallback/reflow and L004 tabular-numeral dense-comparison transfer from `progress/LAYOUT_STATUS.md`.
- Reusable finding: Type widths/features can cross wrap/column thresholds; delivered font behavior is a Layout input.
- Transfer opportunity: T011 adds kerning and line-metric integrity as release properties that should be pinned before layout regression.
- Scope: no browser line-box or product threshold is inferred from structural table inspection.

### Web Design
- Evidence checked: `progress/WEB_STATUS.md`; no substantive `W###` study exists at this checkpoint.
- Application opportunity: Web should validate the exact T011-style shipped WOFF2/subset in real shaping/browser conditions, including language selection, font loading, line boxes, zoom/DPR and fallback.
- Dependency: browser/HarfBuzz shaping remains open; Type does not invent Web evidence.

### Other / cross-cutting
- OpenType registered feature definitions were checked for `kern` and `locl`.
- OpenType `hhea`/`OS/2` metric specifications and fontTools subset behavior were checked.

### Overlap decision
- **EXTENSION + ADVERSARIAL RELEASE VALIDATION**.
- This intentionally overlaps T009's subsetting method because the analytical question is different: whether cmap survival can coexist with loss of pair positioning, language-specific substitution and line-metric identity.

## SOURCE

Authoritative/source-level inputs:

1. OpenType registers `kern` for kerning and `locl` for localized forms. `kern` adjusts spacing between glyphs where pair-specific correction is needed; `locl` provides language/locality-specific glyph forms.
   - https://learn.microsoft.com/en-us/typography/opentype/spec/featurelist
   - https://learn.microsoft.com/en-us/typography/opentype/otspec182/features_ko
2. The OpenType `hhea` table carries horizontal-layout ascender, descender and line-gap values; the current specification explicitly advises testing target applications because applications may use `hhea` or `OS/2` fields differently.
   - https://learn.microsoft.com/en-us/typography/opentype/spec/hhea
3. The OpenType `OS/2` table separately contains typographic and Windows ascender/descender metrics; variable-font guidance further stresses consistency between typographic metrics and `hhea`.
   - https://learn.microsoft.com/en-us/typography/opentype/spec/os2
4. fontTools subset documentation states that preserved layout features pull their referenced glyph variants into subset closure, while `--layout-features=''` drops layout features.
   - https://fonttools.readthedocs.io/en/latest/_modules/fontTools/subset.html

These sources establish table/feature roles and transformation behavior. They do **not** establish that every application uses metrics identically or that this seven-glyph research font models production shaping.

## Controlled research font

1000 UPM static TrueType, seven glyphs:

- `.notdef`, `space`;
- Latin `A`, `V`, `i`;
- non-cmap `i.loclTRK` alternate;
- Hangul `한` (`U+D55C`) research glyph.

Declared contracts:

- cmap includes `A`, `V`, `i`, `한`;
- GPOS `kern`: `A V = -80u`;
- GSUB `locl`: `latn/TRK`, `i → i.loclTRK`;
- `i` and its localized alternate both retain 380u advance;
- `hhea = 820 / -220 / 20`;
- `OS/2 sTypo = 800 / -200 / 0`, `usWin = 900 / 250`.

The Hangul outline is intentionally a simple research rectangle. It proves cmap/subset retention only; it is not evidence about Hangul design, composition or shaping quality.

## Method

Artifacts generated and audited:

1. source TTF;
2. source WOFF2;
3. feature-aware subset TTF for `AVi한`;
4. feature-aware subset WOFF2;
5. adversarial subset TTF with layout features removed;
6. same layout-dropped WOFF2;
7. adversarial preserved-feature subset with `hhea.ascender` mutated `820 → 900`;
8. same metric-mutated WOFF2.

The checker does **not** require the localized alternate to keep its source glyph name after subsetting. It verifies the actual GSUB mapping and the mapped glyph's advance, because T009 already established that subset glyph names may change without a semantic failure.

Environment:

- fontTools `4.63.0`;
- `fontbakery`, `fontspector`, `ots-sanitize`, `hb-shape`: unavailable.

## Results

### A. Normal WOFF2 packaging preserved the complete bounded contract

Source WOFF2 retained:

- requested cmap coverage;
- `A V = -80u` GPOS pair;
- `latn/TRK locl` binding;
- localized alternate closure with 380u advance;
- exact `hhea` and `OS/2` metrics.

**Local contract: PASS.** This is not external-sanitizer or browser PASS.

### B. Feature-aware subsetting preserved the complete bounded contract

The `AVi한` subset kept all four requested codepoints. It also pulled the non-cmap localized alternate into glyph closure and retained:

- `kern`;
- `locl` under `latn/TRK`;
- 380u source/alternate advance agreement;
- exact line metrics.

The alternate was renamed from `i.loclTRK` to `glyph00004`; semantic inspection still passed.

This independently reinforces T009: **glyph names are not a robust release-semantic contract after subsetting**.

### C. Adversarial layout-feature removal remained parseable and retained cmap coverage

The layout-dropped subset WOFF2 still contained:

- `A`;
- `V`;
- `i`;
- `한`.

Yet:

- no surviving `kern` binding/pair;
- no surviving `locl` binding;
- no localized alternate closure.

The file remained parseable and exact line metrics remained unchanged.

**Critical failure:** a QA gate that checks only requested characters would report success while localized and pair-positioning behavior had already regressed.

### D. Adversarial metric mutation remained parseable while layout features stayed intact

A second adversarial artifact retained:

- all requested cmap characters;
- `kern`;
- `locl` and localized alternate closure;
- unchanged `OS/2` values.

Only `hhea.ascender` changed:

`820u → 900u` (**+80u**).

The TTF and WOFF2 both remained parseable.

This proves a different release failure class from feature loss: **feature semantics can remain intact while line-metric identity drifts**.

T011 does not claim that every browser/OS would turn this +80u mutation into the same line-box delta. The OpenType specification itself is why target-application validation remains a separate layer.

## SYNTHESIS

T009–T011 now support a broader package-contract model:

`character closure ≠ layout-feature closure ≠ language-system binding ≠ metric identity ≠ shaping/rendering integration`.

A subset can contain every required user-visible character and still fail typography because a non-cmap alternate, GPOS pair, language binding or metric field changed.

The release manifest therefore needs semantic assertions for behaviors that matter to the product, not merely file-open, table-count or Unicode-coverage checks.

## STUDIO JUDGMENT

For production fonts, define a **shipped-artifact typography contract** before subsetting/package optimization. At minimum, when relevant, record and test:

- required Unicode/script coverage;
- required GSUB/GPOS features;
- language-system bindings (`script/langsys`), not feature tag existence alone;
- feature-dependent non-cmap glyph closure;
- representative pair/substitution behavior;
- horizontal/vertical metric fields used by the product/family contract;
- variable-axis semantics where applicable (T010);
- exact artifact hash/provenance;
- target shaping/browser/app integration separately.

Do not promote a build because it is smaller and parseable if the semantic contract was never checked.

## OPEN

- FontBakery/Fontspector/OTS broad QA remains unexecuted because executables are unavailable.
- HarfBuzz/hb-shape is unavailable, so T011 is structural OpenType inspection, not shaping-engine proof.
- No browser/CoreText/DirectWrite/Skia/Flutter line-box proof.
- No `mark`/`mkmk` anchor closure, combining marks, complex scripts or production Korean shaping.
- No vertical-writing `vhea`/`vmtx`/`vert`/`vrt2` study.
- No variable axes/CFF2 in this block.
- No human reading/recognition evidence.
- The metric mutation is adversarial; it does not claim fontTools normally introduces that change.

## HANDOFFS TO OTHER SPECIALISTS

### Color
- **TRANSFER:** exact font package provenance should include layout/metric contract, not only nominal family/weight/fallback.
- C009 rendering comparisons should use an artifact whose Type release contract is already verified.
- Scope: T011 makes no Color/readability threshold claim.

### Layout / Interaction
- **TRANSFER:** L003/L004 regression tests should run against the exact shipped subset, after required kerning/localized forms and line metrics are verified.
- Cmap presence alone cannot certify text width, pair spacing, localized form behavior or line-metric identity.
- Scope: structural metric drift is not a measured browser line-box failure.

### Web Design
- Independently validate the exact shipped WOFF2 with real `lang`/CSS/font loading and browser shaping.
- Test localized-form activation, kerning, line-height/line boxes, fallback, zoom/DPR and responsive thresholds.
- This is a Type release contract, **not Web PASS**.

## Evidence level

**PRACTICE + CRITIQUE / seven-glyph static TTF + WOFF2 + Latin/Hangul cmap subset + GPOS kern + language-bound GSUB locl + adversarial feature loss + adversarial line-metric drift.**

Foundation remains **NOT PASSED**.
