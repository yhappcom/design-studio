# T008 — Production Build / Release QA Baseline: Required Tables, Variable Metrics, and Reproducible Checks

Status: **FOUNDATION / PRACTICE + CRITIQUE — binary/table/metric release-check baseline established with failure→revision→mutation proof; broad external sanitizer/foundry/platform validation still OPEN**

Owner: Typography / Type Design Specialist  
Canonical path: `research/type/`  
Reproducible source: `research/type/T008-production-build-qa.py`  
Measured data: `research/type/T008-production-build-qa-results.json`  
Evidence artifact: `research/type/T008-production-build-qa-evidence.svg`

## Purpose

T006 established editable-source and export QA. T007 established multi-master correspondence and intermediate-instance QA.

T008 asks the next production question:

> What must a release check verify in the generated variable font binary so that source/build success is not confused with a shippable font?

The goal is not to invent a complete foundry release pipeline. The goal is to establish a **minimum reproducible studio QA layer** that catches real binary/metadata failures before browser/device testing.

The experiment reuses the T007 `H O n o` research family and explicitly does not promote it to a product font.

---

## RELATED DOMAIN CHECK

### Typography / Type
- Evidence checked:
  - T006 single-master source/build audit;
  - T007 interpolation compatibility and `gvar` coverage;
  - current `progress/TYPE_STATUS.md`.
- Reusable finding:
  - editor/source correctness, variable-build compatibility, binary validity and renderer behavior are separate gates.
- Replication / challenge / transfer opportunity:
  - audit the actual T007-emitted binary against current OpenType requirements rather than assuming varLib output plus visual proof is release-ready.
- Dependency / overlap:
  - FontBakery/OTS, full naming/family strategy, hinting, GSUB/GPOS, components, marks, CFF2 and platform QA remain later layers.

### Color
- Evidence checked:
  - current `progress/COLOR_STATUS.md`.
- Reusable finding:
  - exact rendered font build/instance must be controlled when Color behavior is being evaluated.
- Replication / challenge / transfer opportunity:
  - T008 makes the binary identity/instance explicit before later Color transfer.
- Dependency / overlap:
  - **Not materially relevant to required-table or LSB/xMin compliance itself after checking.**

### Layout / Interaction
- Evidence checked:
  - current `progress/LAYOUT_STATUS.md`;
  - L003/L004 Type→Layout transfer principles.
- Reusable finding:
  - metrics and actual generated Type behavior can move wrap/column thresholds.
- Replication / challenge / transfer opportunity:
  - release QA should detect unexpected metric behavior before Layout regression testing.
- Dependency / overlap:
  - Layout owns spatial acceptance, not font-binary compliance.

### Web Design
- Evidence checked:
  - current `progress/WEB_STATUS.md`;
  - `research/web/README.md`.
- Reusable finding:
  - Web owns final delivered-font/browser/device validation.
- Implementation / application validation opportunity:
  - consume a release-checked binary rather than editor/source previews for browser tests.
- Dependency / overlap:
  - no substantive `W###` evidence exists yet.

### Other / cross-cutting / future specialist
- Evidence checked:
  - OpenType 1.9.1 font-file required-table rules;
  - OpenType `head` variable-font requirements;
  - OpenType Font Variations table model;
  - FontTools `varLib` / STAT generation behavior.
- Reusable finding:
  - base OpenType tables are required;
  - `STAT` is required for variable fonts;
  - TrueType variable fonts require `head` bit 1 set and bit 5 clear, with each glyph's left sidebearing equal to xMin;
  - binary checksums and axis metadata are machine-checkable release properties.
- Dependency / overlap:
  - broad sanitizer ecosystems and OS-specific acceptance remain external validation.

### Overlap decision
- **EXTENSION + FAILURE ANALYSIS + RELEASE-GATE PRACTICE**.
- Why:
  - T007 validated interpolation behavior but did not audit the resulting binary against release-level structural requirements.

---

## 1. SOURCE — required OpenType and variable-font tables

OpenType 1.9.1 identifies the base tables required for a functioning OpenType font:

- `cmap`
- `head`
- `hhea`
- `hmtx`
- `maxp`
- `name`
- `OS/2`
- `post`

TrueType outline fonts additionally use `glyf` and `loca`.

For variable fonts, the specification identifies variation tables including `fvar`, `gvar`, HVAR/MVAR as applicable, and states that **`STAT` is required for variable fonts**.

Source:
- https://learn.microsoft.com/en-us/typography/opentype/spec/otff

### STUDIO JUDGMENT

A release checker should distinguish:

1. spec-required tables;
2. tables required by this particular outline/variation architecture;
3. project-specific tables/features expected by the design contract.

Do not make every possible OpenType table mandatory.

---

## 2. SOURCE — TrueType variable-font LSB/xMin contract

The OpenType `head` specification states that for a variable font with TrueType outlines:

- the left side bearing for each glyph must equal `xMin`;
- `head.flags` bit 1 must be set;
- bit 5 must be clear.

Source:
- https://learn.microsoft.com/en-us/typography/opentype/spec/head

This requirement matters because TrueType variable outlines use phantom points and variation data to represent sidebearing/advance behavior consistently.

---

## 3. Controlled audit

The T008 checker verifies the research VF for:

### Required binary structure
- base required tables;
- `glyf`/`loca`;
- `fvar`, `STAT`, `gvar`;
- valid `head.magicNumber`;
- full-font checksum equals `0xB1B0AFBA`.

### Variable-family contract
- expected `wght` axis `300 / 300 / 700`;
- STAT axis tags correspond to `fvar`;
- required name IDs exist and axis name ID resolves;
- critical `H O n o` each have variation data;
- endpoint/intermediate static instances can be generated.

### Variable TrueType metrics
The OpenType requirement applies to the TrueType variable font default metrics. T008 checks that invariant at the default and also instantiates `wght 500` and `700` as **regression probes** to verify that the generated static instances preserve the same normalized sidebearing/bounds relationship in this pipeline.

For each sampled `H O n o` instance it:

- reads actual glyph `xMin`;
- reads actual `hmtx` left sidebearing;
- verifies `LSB == xMin`.

The non-default-instance checks are a studio pipeline regression test, not a claim that the variable-font `hmtx` specification stores separate non-default LSB values there.

### Research-build reproducibility
The corrected source is built twice with fixed source/toolchain/timestamps and SHA-256 compared.

This is a bounded checker, not a substitute for FontBakery, OTS, a production foundry toolchain, or target OS/browser validation.

---

## 4. Real failure discovered in the T007 research builder

T007's interpolation logic was valid after shared conversion, but the master builder had used:

`LSB = 0`

for all research glyphs while the actual contour `xMin` was:

`50`

The emitted variable font therefore had:

`head.flags = 1`

meaning bit 0 set, **bit 1 not set**.

At each of `wght 300`, `500`, `700`, all four critical glyphs failed the study's `LSB == xMin` probes.

Examples:

| wght | glyph | advance | LSB | xMin | result |
| ---: | --- | ---: | ---: | ---: | --- |
| 300 | H | 580 | 0 | 50 | FAIL |
| 300 | O | 600 | 0 | 50 | FAIL |
| 500 | O | 610 | 0 | 50 | FAIL |
| 700 | O | 620 | 0 | 50 | FAIL |

Across `H O n o × 3 instances`, the checker records **12 LSB/xMin failures**, plus `head_bit1_not_set`.

### Finding

T007 could be correct as an **interpolation experiment** while still being non-compliant as a **release binary**.

This is exactly why evidence levels must remain separate.

---

## 5. Revision — normalize master metrics and head flags before variable build

The revised build:

1. recalculates each contour glyph's `xMin`;
2. writes the master `hmtx` LSB to that `xMin`;
3. sets `head.flags` bit 1;
4. clears `head.flags` bit 5;
5. rebuilds the VF;
6. re-audits instances at 300/500/700.

Revised `head.flags`:

`3` (`0b11`)

All tested critical glyphs now report:

`LSB = 50` and `xMin = 50`

at all three sampled weights.

The revised audit also confirms:

- required base/variable tables present;
- `wght` axis `300 / 300 / 700`;
- STAT/fvar axis correspondence;
- name IDs `1,2,3,4,6,256`;
- one `gvar` tuple for each `H O n o`;
- valid full-font checksum `0xB1B0AFBA`;
- zero release-check failures in this bounded test.

### Evidence disposition

The revised build **passes T008's local QA contract**.

It does not become production PASS.

---

## 6. Deliberate mutation — a readable font can still violate the variable-font table contract

The corrected VF is copied and the `STAT` table deliberately removed.

The resulting font:

- remains parseable by FontTools;
- still has `fvar`, `gvar`, HVAR and working tested instances;
- still satisfies the whole-font checksum;
- still has correct LSB/xMin behavior.

Yet T008 reports:

`missing_required_table:STAT`

### Finding

“Font opens” or “instances render” is not equivalent to “binary satisfies the release contract.”

Different QA layers catch different failure classes.

---

## 7. Reproducible build check — and a failed first assumption

The first implementation assigned fixed `head.created` / `head.modified` values and observed equal hashes for two builds made close together. A later independent rerun produced a different hash. That exposed a methodological error: **assigning a timestamp value is not sufficient when the font-writing library is still configured to recalculate it on save.**

T008 therefore added an explicit control probe. With requested `head.modified = 3800000000`:

- normal FontTools timestamp recalculation saved a different current-time value;
- setting `TTFont.recalcTimestamp = False` preserved `3800000000`.

The corrected bounded build now controls both the field value **and the serializer behavior**, then builds the same source twice. Both outputs produce:

`e3354d493cba74f03c857f022d529f8d03e7ae91c948beb79b32b126f1213119`

The companion JSON records `binary_identical = true`. An additional separate process rerun during the study produced the same revised hash after the serializer fix.

### STUDIO JUDGMENT

Binary reproducibility is useful because unexplained byte changes complicate release review, regression diagnosis and provenance. But a “reproducible” test must control the **actual sources of nondeterminism**, not merely assign values that a build tool may overwrite.

This experiment does **not** establish a universal timestamp policy. A production pipeline may preserve meaningful version/build metadata while still using a reproducible artifact strategy.

---

## 8. Release-gate hierarchy

### Gate A — source/design validity
- clean/intentional contours;
- master correspondence;
- spacing/metrics intent;
- design interpolation intent.

### Gate B — build compatibility
- no skipped required glyphs;
- correct generated topology;
- expected variation tables/data;
- explained warnings.

### Gate C — binary/spec sanity
- required tables;
- head/metrics requirements;
- axis/name/STAT consistency;
- checksum/integrity;
- expected glyph/axis coverage.

### Gate D — design regression
- endpoint/intermediate appearance;
- metrics and widths;
- compact raster;
- fallback/script behavior;
- Layout/Color integration.

### Gate E — target environment
- FontBakery/OTS/foundry QA as applicable;
- browser/OS/device;
- accessibility/localization;
- actual project content;
- human evidence where required.

No earlier gate substitutes for a later one.

---

## 9. Project Readiness Test

### Apply this knowledge when
- building custom static/variable families;
- modifying source masters;
- changing conversion/build tools;
- generating release webfonts/app fonts;
- accepting third-party/custom font builds into a product.

### Do not use it as
- a font-selection criterion by itself;
- a substitute for optical/design critique;
- a guarantee of browser/platform support;
- a complete foundry QA pipeline.

### Information required from a project
- exact delivered format;
- static/variable strategy;
- axes and ranges;
- target platforms/browsers;
- supported scripts/languages;
- required OpenType features;
- minimum text sizes;
- release/update/provenance requirements.

### Decisions this can change
- whether a binary is allowed into integration testing;
- whether a build warning is release-blocking;
- whether metrics must be rebuilt before UI validation;
- which checks become CI gates;
- whether browser/device testing uses the correct artifact.

### Failure conditions
Hold the build when:
- a spec-required table is absent;
- required variable glyphs are missing variation data;
- axis/STAT/name metadata are inconsistent or unresolved;
- TrueType VF LSB/xMin/head flags violate the required contract;
- checksum/integrity is invalid;
- representative instances cannot be generated;
- expected metric behavior is missing;
- reproducibility/provenance changes are unexplained where the project requires them.

---

## OPEN

Still unresolved:

- FontBakery integration;
- OpenType Sanitizer / browser sanitizer transfer;
- complete naming/style-linking/family model;
- named instances and `STAT` AxisValue coverage;
- `avar`;
- three-master/multi-axis build QA;
- CFF2;
- composites/components/anchors/marks;
- GSUB/GPOS/kerning/interpolation QA;
- hinting/instructions;
- WOFF/WOFF2 release artifacts;
- subsetting;
- license metadata and provenance;
- versioning/release packaging;
- cross-machine/toolchain reproducibility beyond this same-environment proof;
- CoreText/DirectWrite/Skia/Flutter/browser validation;
- production project regression.

---

## HANDOFFS TO OTHER SPECIALISTS

### Typography / Type
- Useful finding/context:
  - T007 interpolation PASS did not imply binary/spec PASS; T008 found a real LSB/xMin/head-flags failure.
- Canonical section:
  - Sections 4–8.
- Confirmation / contradiction / transfer note:
  - confirms the studio evidence model: source, build, binary and rendering are separate gates.
- Scope limit:
  - local checker on a tiny research VF, not foundry production certification.

### Color
- Useful finding/context:
  - future rendered Color testing should identify the exact release-checked font binary/instance.
- Canonical section:
  - Gate hierarchy / reproducibility.
- Confirmation / contradiction / transfer note:
  - prevents Color evidence from accidentally using a malformed or non-release-equivalent Type artifact.
- Scope limit:
  - no Color threshold claim.

### Layout / Interaction
- Useful finding/context:
  - release QA can catch metric defects before width/reflow/density regression reaches Layout.
- Canonical section:
  - Sections 4–5.
- Confirmation / contradiction / transfer note:
  - corrected Type metrics become the input for later Layout validation.
- Scope limit:
  - binary compliance does not prove spatial fit.

### Web Design
- Useful finding/context:
  - Web should integrate/test the exact release candidate artifact after required-table/metric/axis checks, not an arbitrary editor or intermediate build.
- Web application / validation consequence:
  - WOFF/WOFF2, browser loading, CSS axes/features and device rendering remain downstream checks.
- Confirmation / contradiction / transfer note:
  - T008 supplies a pre-browser release gate, not Web evidence.
- Scope limit:
  - no browser/device validation was performed.

---

## Evidence level

**PRACTICE + CRITIQUE / actual generated variable TrueType binary + spec-oriented audit + failure→revision→mutation + reproducibility evidence.**

T008 establishes a studio release-QA baseline. It does **not** establish Foundation PASS or a complete font-production pipeline.
