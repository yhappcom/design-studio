# T012 — `mark` / `mkmk` Anchor Release Contract

Status: **PRACTICE + CRITIQUE / controlled structural GPOS + subset + WOFF2 evidence; real shaping/browser/platform/human validation OPEN**

Owner: Typography / Type Design Specialist  
Canonical path: `research/type/`

Reproducibility:

- `T012-mark-mkmk-anchor-release-contract.py`
- `T012-mark-mkmk-anchor-release-contract-results.json`

## Question

Can a packaged/subset font retain every requested Unicode codepoint and zero-width combining mark while losing the attachment semantics required to position those marks correctly?

T011 established that cmap coverage can survive while `kern` or `locl` semantics fail. T012 extends that release-contract model to **GPOS mark attachment**, where the critical behavior is not merely glyph closure but feature binding, lookup type, mark class and anchor coordinates.

## Why T012 took this path

The first queue item was external broad QA/sanitizer integration. At this checkpoint `fontbakery`, `fontspector`, `ots-sanitize`, and `hb-shape` were not installed; an attempted FontBakery install could not reach the package index because network name resolution was unavailable. No external-tool PASS is therefore claimed.

The highest-value executable fallback was the next open Type gap: `mark` / `mkmk`, anchors and combining marks.

---

## RELATED DOMAIN CHECK

### Typography / Type

Evidence checked: T009–T011 and current Type status.

Reusable findings:

- T009: post-subset glyph names are not a reliable semantic contract;
- T011: Unicode closure, OpenType layout semantics and metric identity are independent release gates.

T012 deliberately extends those claims from substitution/pair positioning to chained combining-mark attachment.

### Color

Evidence checked: `research/color/C009-type-rendering-color-contrast-transfer.md`.

Reusable finding: the declared color pair does not normalize differences in final rendered Type. Mark attachment failure would change the rendered ink field without any Color-token change.

No Color threshold is inferred here.

### Layout / Interaction

Evidence checked: `research/layout/L003-type-fallback-density-reflow-transfer.md` and current Layout status.

Reusable finding: Type behavior can cross actual layout thresholds; structural Type failures should not be silently repaired by spacing/layout policy.

T012 does not measure reflow. It provides a shipped-font semantic prerequisite for later layout regression.

### Web Design

Evidence checked: current Web status. No substantive `W###` evidence exists yet.

Web should validate the exact shipped artifact under real `@font-face`, Unicode normalization/content, browser shaping, zoom/DPR, fallback and target platforms. T012 is not browser PASS.

### Other / cross-cutting

Authoritative sources checked:

- OpenType 1.9.1 registered feature list: `https://learn.microsoft.com/en-us/typography/opentype/spec/featurelist`
- OpenType GPOS table: `https://learn.microsoft.com/en-us/typography/opentype/spec/gpos`
- fontTools subset documentation: `https://fonttools.readthedocs.io/en/latest/_modules/fontTools/subset.html`

### Overlap decision

**EXTENSION + ADVERSARIAL RELEASE VALIDATION.**

T012 repeats T009–T011's package/subset method because mark attachment introduces a different semantic failure class: a complete Unicode sequence can remain present while its geometric attachment chain is partially or completely removed.

---

# SOURCE

OpenType registers:

- `mark` — Mark Positioning;
- `mkmk` — Mark to Mark Positioning.

The GPOS specification defines mark-to-base attachment as LookupType 4 and mark-to-mark attachment as LookupType 6. Mark arrays associate covered mark glyphs with mark classes and anchor coordinates; corresponding base/mark arrays provide the attachment anchors.

fontTools subset documentation states that `mark` and `mkmk` are in its default retained layout-feature set, and that preserved layout features participate in glyph closure. It also permits explicit feature removal.

These are structural/spec facts. They do not prove that a particular shaping engine will render a sequence correctly.

---

# Controlled specimen

1000-UPM research TTF with four glyphs:

- `.notdef`;
- `A` (`U+0041`, advance `600u`);
- `acutecomb` (`U+0301`, advance `0u`);
- `dotabovecomb` (`U+0307`, advance `0u`).

The controlled contract is:

1. `A`, U+0301 and U+0307 remain in cmap;
2. both combining marks retain `0u` advance;
3. `latn/dflt` binds `mark`;
4. `latn/dflt` binds `mkmk`;
5. LookupType 4 preserves `acutecomb [100,0] → A [300,700]`;
6. LookupType 6 preserves `dotabovecomb [100,0] → acutecomb [100,220]`.

The geometry is deliberately synthetic. This is a release-semantic probe, not a diacritic design-quality specimen.

---

# Practice / validation

## A. Source TTF → WOFF2

The source WOFF2 retained the complete bounded contract.

**Result: local structural contract PASS.**

This is not a broad font-quality or shaping-engine PASS.

## B. Feature-aware subset

A subset containing `A + U+0301 + U+0307` with all layout features retained preserved:

- all three cmap entries;
- zero advances for both combining marks;
- `mark` and `mkmk` bindings;
- exact mark-to-base anchors;
- exact mark-to-mark anchors.

The subsetter renamed `dotabovecomb` to `uni0307`. The first version of the T012 checker incorrectly treated that rename as semantic failure.

### Failure → checker revision

The checker was revised to resolve glyph identity from the subset's cmap and then inspect the actual GPOS coverage/anchor structure.

**SYNTHESIS:** post-subset semantic QA must not depend on original source glyph names when those names are not themselves a product contract.

This independently reproduces T009's glyph-name warning in a new GPOS/anchor context.

## C. Adversarial subset: retain `mkmk`, drop `mark`

The WOFF2 remained parseable and retained:

- `A`, U+0301, U+0307;
- both zero-width combining marks;
- `mkmk` binding;
- the mark-to-mark attachment.

But it lost:

- `mark` binding;
- the LookupType 4 mark-to-base anchor relation.

The second mark could still have a mark-to-mark relation while the first mark had lost its base attachment.

**Result: Unicode sequence intact; attachment chain incomplete.**

## D. Adversarial subset: retain `mark`, drop `mkmk`

The WOFF2 remained parseable and retained the same cmap/zero-width contract plus mark-to-base attachment, but lost:

- `mkmk` binding;
- LookupType 6 mark-to-mark attachment.

**Result: first attachment stage intact; stacked-mark stage incomplete.**

## E. Adversarial subset: drop all layout features

The WOFF2 retained all three requested codepoints and both zero advances, but no `mark`/`mkmk` bindings or attachment lookups remained.

**Result: character coverage alone gives a false sense of completeness.**

---

# SYNTHESIS

T009–T012 now support the stronger separation:

`character closure ≠ advance/metric identity ≠ feature binding ≠ attachment-anchor identity ≠ complete attachment chain ≠ shaping/rendering integration`.

For combining marks, a product can contain every requested Unicode codepoint and still ship broken typography if only one stage of an attachment chain survives packaging/subsetting.

The failure can be partial: preserving `mkmk` does not compensate for loss of `mark`, and preserving `mark` does not compensate for loss of `mkmk` when stacked marks are part of the required repertoire.

---

# STUDIO JUDGMENT

When a product repertoire includes combining marks, release QA should define semantic test sequences and assert, where relevant:

- required codepoints and normalization-sensitive sequences;
- zero/nonzero mark advances as intended;
- required script/langsys feature bindings;
- required GPOS lookup classes/types;
- mark classes and actual anchor coordinates or accepted tolerances;
- complete chain behavior (`base → mark → mark`, or ligature/cursive equivalents);
- subset/package preservation in the exact shipped artifact;
- independent shaping-engine/browser/platform validation after structural QA.

Do not certify mark support from cmap coverage alone.

Do not use source glyph-name identity as the default post-subset semantic key.

---

# OPEN

- HarfBuzz / `hb-shape` execution;
- browser, CoreText, DirectWrite, Skia and Flutter shaping;
- canonical decomposition/composition behavior and normalization handling;
- ligature mark attachment;
- multiple mark classes and collision behavior;
- Arabic/Indic and other complex-script mark systems;
- production diacritic design/optical quality;
- variable-font anchor interpolation;
- CFF2;
- external FontBakery/Fontspector/OTS broad QA;
- human reading/recognition evidence.

T012 does **not** claim PASS for these areas or for Foundation overall.

---

## HANDOFFS TO OTHER SPECIALISTS

### Color

A complete Unicode sequence can render a materially different ink field if mark attachment semantics are missing while the Color pair is unchanged. Use the exact shipped artifact after Type semantic QA when evaluating rendered Type/Color robustness. No Color threshold follows from T012.

### Layout / Interaction

Treat required mark attachment as a Type precondition before measuring localized widths/heights or making spatial repairs. A layout workaround should not mask missing `mark`/`mkmk` semantics.

### Web Design

Use real text sequences containing combining marks against the exact WOFF2/subset. Validate normalization/content paths, browser shaping, fallback, zoom/DPR and target OS/browser combinations. Structural GPOS presence is necessary evidence, not browser PASS.

---

## Evidence level

**PRACTICE + CRITIQUE / synthetic static TrueType + WOFF2 + feature-aware subset + exact structural GPOS anchor audit + three adversarial feature-loss conditions + checker failure/revision.**

Foundation remains **NOT PASSED**.
