# T009 — Webfont Packaging/Subsetting as a Feature Contract

Status: **PRACTICE + CRITIQUE / controlled TTF→WOFF2 + GSUB-aware subsetting failure→revision proof complete; external sanitizer, shaping/browser, variable-font and production-family validation remain OPEN**

## Why this study exists

T008 established that a font can parse/render yet still fail a release contract. The next release boundary is packaging/subsetting. T004 and Layout L004 already established that `tnum` is not decorative metadata: equal-width figure alternates can change dense numeric comparison geometry.

T009 therefore asks:

> Can a font remain structurally readable after packaging/subsetting while silently losing a product-critical OpenType feature contract?

It also tests whether a QA checker may itself fail when it relies on implementation details such as glyph names rather than semantic lookup outputs and metrics.

Reproducibility artifacts:

- `T009-webfont-subset-feature-contract.py`
- `T009-webfont-subset-feature-contract-results.json`

Generated font binaries remain temporary research outputs and are not product assets.

---

## RELATED DOMAIN CHECK

### Typography / Type
- Evidence checked: T004 numeral/punctuation feature practice; T006–T008 source→interpolation→binary-QA chain; `progress/TYPE_STATUS.md`.
- Reusable finding: release acceptance must preserve intended metrics/features, not merely file readability.
- Extension: move from binary sanity into distribution transformation (subsetting + WOFF2).

### Color
- Evidence checked: C009 Type→Color rendering transfer.
- Reusable finding: downstream rendering evidence depends on the exact font artifact. T009 extends this operationally: packaging/subsetting can produce a different functional artifact even when it still opens.
- Scope: no Color threshold claim.

### Layout / Interaction
- Evidence checked: L004 tabular-numeral transfer.
- Reusable finding: `tnum` equal-width behavior has spatial consequences; removing it can invalidate a dense-comparison layout contract.
- Transfer opportunity: production Layout regression should use the shipped/subset artifact, not only the source font.

### Web Design
- Evidence checked: current Web status; no substantive `W###` evidence exists.
- Reusable finding: Web owns real `@font-face`, browser loading, CSS feature application, zoom/DPR/device validation.
- Dependency: T009 proves table/metric preservation only; browser shaping remains Web validation.

### Other / cross-cutting
- SOURCE: current fontTools subset documentation states that the subset glyph set is affected by preserved OpenType layout features and that glyph variants used by preserved features are added by layout closure.
- SOURCE: OpenType 1.9.1 registers `tnum` as **Tabular Figures**.
- OPEN: FontBakery, Fontspector and OTS executables were unavailable in the execution environment, so external broad QA remains unresolved rather than simulated.

### Overlap decision
- **TRANSFER VALIDATION + FAILURE ANALYSIS + QA-METHOD CORRECTION**.
- Why: T004/L004 establish the semantic/layout value of `tnum`; T009 tests whether the release transformation preserves that contract.

---

# SOURCE

## fontTools subset behavior

The fontTools subsetter documents that the retained glyph set depends on requested characters/glyphs and retained OpenType layout features. With layout closure enabled, glyphs reachable through preserved GSUB features are added to the subset. `--layout-features='*'` retains all features; an empty feature set drops them.

## OpenType `tnum`

The OpenType registered-feature list identifies `tnum` as **Tabular Figures**.

### SYNTHESIS

A subset recipe is part of font behavior, not merely a file-size optimization. If a product relies on a feature, the release contract must explicitly preserve both:

1. the relevant OpenType feature/lookup; and
2. the glyph/metric outputs that make the feature useful.

---

# CONTROLLED EXPERIMENT

Environment:

- fontTools `4.63.0`;
- Brotli/WOFF2 support available;
- external `fontbakery`, `fontspector`, `ots-sanitize`: not available.

Research font:

- static TrueType;
- glyphs `.notdef`, `space`, `one`, `two`, `one.tnum`, `two.tnum`;
- proportional advances: `one=380`, `two=520`;
- tabular alternates: both `600` units;
- GSUB `tnum`: `one→one.tnum`, `two→two.tnum`.

Transform matrix:

1. source TTF;
2. source WOFF2;
3. subset TTF preserving all layout features;
4. subset TTF dropping layout features;
5. feature-preserving subset WOFF2;
6. feature-dropping subset WOFF2.

Acceptance contract:

- `tnum` exists;
- GSUB exposes two substitution outputs;
- those two outputs have equal `600`-unit advances.

The checker intentionally validates semantic lookup outputs and metrics rather than requiring source glyph names to survive.

---

# FAILURE 1 — the first QA checker was wrong

The first checker expected literal glyph names `one.tnum` and `two.tnum` after subsetting. fontTools correctly preserved the `tnum` substitutions but renamed non-Unicode alternates to generated glyph names (`glyph00003`, `glyph00004`) under the chosen subset settings.

The feature remained functional at the table/metric level, but the name-based checker returned a false failure.

### STUDIO JUDGMENT

Do not make release QA depend on non-contractual internal identifiers when the actual product contract is semantic behavior. For an OpenType substitution feature, inspect the retained lookup outputs and their required metrics/behavior.

This is the QA analogue of T007's lesson: equal point counts were too weak there; stable glyph names are too strong and irrelevant here.

---

# REVISION — semantic-output checker

The checker was revised to inspect:

- presence of `tnum` in GSUB FeatureList;
- count of substitution outputs;
- advance widths of the actual output glyphs, whatever their post-subset names.

Revised results:

| Artifact | Parseable | `tnum` | GSUB outputs | Equal 600u outputs | Contract |
| --- | --- | --- | ---: | --- | --- |
| source TTF | yes | yes | 2 | yes | PASS |
| source WOFF2 | yes | yes | 2 | yes | PASS |
| feature-aware subset TTF | yes | yes | 2 | yes | PASS |
| feature-aware subset WOFF2 | yes | yes | 2 | yes | PASS |
| layout-feature-drop subset TTF | yes | no | 0 | no | **FAIL** |
| layout-feature-drop subset WOFF2 | yes | no | 0 | no | **FAIL** |

Observed sizes in this tiny research font:

- source TTF: `1084` bytes;
- source WOFF2: `440` bytes;
- feature-aware subset TTF: `1008` bytes;
- feature-aware subset WOFF2: `436` bytes;
- layout-feature-drop subset TTF: `908` bytes;
- layout-feature-drop subset WOFF2: `400` bytes.

The exact byte savings are not generalizable from this artificial font. The important result is that the smaller feature-dropping artifacts remained readable while violating the intended numeric contract.

### SYNTHESIS

**Parseability + smaller size is not release success.** A release transformation must preserve project-required shaping/metric behavior.

---

# WOFF2 RESULT

WOFF2 packaging by itself preserved the bounded `tnum` contract in both the full research font and the feature-aware subset.

### LIMIT

This is a table/metric round-trip result, not browser proof. It does not establish:

- CSS `font-variant-numeric` application;
- HarfBuzz/CoreText/DirectWrite/Skia shaping equivalence;
- actual `@font-face` loading/fallback;
- cache/CORS/preload behavior;
- variable-font axis retention;
- hinting/rendering equivalence;
- real production-family subsetting.

---

# RELEASE-GATE CONSEQUENCE

T006–T009 now support a more explicit production chain:

1. source/design validity;
2. interpolation/build compatibility;
3. binary/spec sanity;
4. **distribution transformation contract** — subsetting, WOFF2/app packaging, feature/glyph/metric preservation;
5. target shaping/rendering/layout integration;
6. human/product validation.

A PASS at any earlier layer does not imply the next.

### STUDIO JUDGMENT

A production font release should maintain a project-specific manifest of required capabilities, for example:

- required Unicode/script coverage;
- required GSUB/GPOS features (`tnum`, `zero`, `locl`, `kern`, mark positioning, etc. as applicable);
- required variation axes/instances;
- critical metric invariants;
- required names/metadata;
- packaging formats;
- shaping/browser/app regression cases.

The subset/build recipe should be tested against that manifest after every transformation.

---

## HANDOFFS TO OTHER SPECIALISTS

### Color
- Use the exact shipped/subset font artifact in rendered Color validation. A source font and a packaged subset are not automatically behaviorally equivalent.
- Scope limit: T009 makes no readability/contrast threshold claim.

### Layout / Interaction
- L004's tabular-numeral geometry contract can be broken by release subsetting even when the font still opens.
- Regression should test the shipped artifact and required numeric features, not only design-source metrics.

### Web Design
- `@font-face` integration should consume the exact feature-audited WOFF2/subset artifact.
- Reproduce `tnum` through CSS shaping in target browsers and test localization, zoom/DPR, fallback and numeric-column geometry.
- Browser success is not established by T009.

---

# OPEN

- external FontBakery / Fontspector / OTS execution and finding-classification policy;
- HarfBuzz/browser shaping proof of the subset artifacts;
- variable-font WOFF2/subsetting and `fvar`/`gvar`/`STAT`/`avar` retention;
- GPOS/kerning/mark-feature preservation;
- Korean/Latin multi-script subset closure and `locl` behavior;
- production-family Unicode-range partitioning;
- hinting retention/removal policy;
- cross-machine/toolchain reproducibility of subset/package outputs;
- production web loading and device/browser validation;
- human numeric-comparison evidence.

## Evidence level

**PRACTICE + CRITIQUE / original research font + GSUB `tnum` + feature-aware vs feature-dropping subset mutation + WOFF2 packaging + QA-checker failure→revision.**

T009 is **not PASS**.