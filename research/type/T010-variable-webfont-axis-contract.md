# T010 — Variable Webfont Axis Contract: WOFF2, Subsetting, `avar`, and User-Space Semantics

Status: **PRACTICE + CRITIQUE / VARIABLE-FONT DISTRIBUTION TRANSFER — bounded WOFF2/subset axis-contract evidence established; external broad QA, browser/platform and production-family validation remain OPEN**

Owner: Typography / Type Design Specialist  
Canonical path: `research/type/`

Reproducibility artifacts:

- `research/type/T010-variable-webfont-axis-contract.py`
- `research/type/T010-variable-webfont-axis-contract-results.json`

Generated experimental TTF/WOFF2 binaries are temporary research outputs. They are not product assets or canonical source authority.

---

## Question

T009 proved that a subset can remain parseable while silently losing a required OpenType feature. T010 asks the equivalent variable-font question:

> Can a packaged/subset variable font remain parseable and retain `fvar`, `gvar`, `STAT`, axis ranges and named instances while no longer preserving the intended meaning of a user-space axis coordinate?

This matters because a real product consumes the **shipped artifact**, not the source/designspace or an earlier variable-font build.

---

## RELATED DOMAIN CHECK

### Typography / Type

- Evidence checked:
  - `T007-variable-interpolation-source-compatibility.md`;
  - `T008-production-build-release-qa.md`;
  - `T009-webfont-subset-feature-contract.md`;
  - current `progress/TYPE_STATUS.md`.
- Reusable finding:
  - T007: a variable font can build even when correspondence/intermediate behavior is wrong;
  - T008: parseability is weaker than release QA and generated-binary contracts must be checked explicitly;
  - T009: distribution transformations can preserve readability while dropping a product-required feature.
- Replication / challenge / transfer opportunity:
  - extend the distribution contract from static OpenType features/metrics to variable-font axis metadata **and the effective mapping from user coordinates to variation coordinates**.
- Dependency / overlap:
  - external FontBakery/Fontspector/OTS broad QA remains useful but was unavailable in this execution environment. T010 does not simulate those tools.

### Color

- Evidence checked:
  - `research/color/C009-type-rendering-color-contrast-transfer.md`;
  - `progress/COLOR_STATUS.md`.
- Reusable finding:
  - C009 shows that exact Type weight/fallback/DPR can materially alter rendered text while semantic Color pairs remain fixed.
- Replication / challenge / transfer opportunity:
  - T010 asks whether the **same nominal axis coordinate** can resolve to a different font instance after packaging metadata changes.
- Dependency / overlap:
  - Color remains owner of contrast/color claims; T010 makes no readability or contrast-threshold claim.

### Layout / Interaction

- Evidence checked:
  - `research/layout/L003-type-fallback-density-reflow-transfer.md`;
  - `research/layout/L004-tabular-numerals-dense-comparison-transfer.md`;
  - current `progress/LAYOUT_STATUS.md`.
- Reusable finding:
  - actual delivered font behavior can move wrap, width and dense-column thresholds; font features and axis values are spatial inputs.
- Replication / challenge / transfer opportunity:
  - preserve the exact shipped variable-font axis behavior before Layout performs threshold regression.
- Dependency / overlap:
  - T010 measures a font metric change only. It does not claim that the observed `9u` delta causes a specific product-layout failure.

### Web Design

- Evidence checked:
  - `progress/WEB_STATUS.md`;
  - `research/web/README.md`.
- Reusable finding:
  - Web owns real `@font-face`, CSS axis application, loading/fallback, browser/device, responsive and production integration validation.
- Implementation / application validation opportunity:
  - load the exact T010-style audited WOFF2 and verify CSS `font-weight` / `font-variation-settings`, style matching, axis interpolation, zoom/DPR and target-browser behavior.
- Dependency / overlap:
  - no substantive `W###` evidence existed at this checkpoint. T010 is Type-owned packaging semantics, not Web PASS.

### Other / cross-cutting

Authoritative material checked:

- Microsoft OpenType `fvar` specification: axes define user-space ranges/defaults and named instances;
- Microsoft OpenType `avar` specification: optional axis-variation mapping modifies normalized axis coordinates;
- Microsoft OpenType `gvar` specification: glyph variation data is applied across variation space defined by `fvar` and related variation mechanisms;
- Microsoft OpenType variation documentation: `STAT` is required for variable fonts;
- W3C/CSS Fonts: WOFF2 is a webfont format and variable-font resources can be delivered as WOFF2;
- fontTools `varLib.instancer`: user-space locations are normalized and `avar` mapping is applied when present;
- fontTools subsetter: remaining glyph/table/variation data is transformed during subsetting.

### Overlap decision

**EXTENSION + ADVERSARIAL MUTATION + TRANSFER-VALIDATION PREPARATION.**

T010 deliberately repeats the T009 “parseable but product-contract broken” method on a different semantic layer: variable-axis mapping rather than GSUB feature retention.

---

# 1. SOURCE — variable-font axis identity is more than the `fvar` min/default/max tuple

`fvar` exposes variation axes, user-space ranges/defaults and named instances. `gvar` contains TrueType glyph variation data. `STAT` carries style attributes used to describe variable-font design-space positions and is required for variable fonts under the OpenType variation model.

`avar` is different: it is **optional**, but when present it remaps normalized axis coordinates. In other words, two files can expose the same visible `wght` minimum/default/maximum while resolving an intermediate user-space value to different normalized variation positions if their `avar` behavior differs.

### SYNTHESIS

For a font whose design intentionally uses non-linear axis mapping, the release contract is not merely:

`fvar present + gvar present + STAT present + same min/default/max`

It also includes the intended mapping from user-space coordinate to effective variation location.

### STUDIO JUDGMENT

If a production font intentionally contains `avar`, preserving that mapping is a **product contract**, even though `avar` is not universally required by the OpenType specification.

A general sanitizer may legitimately accept a font without `avar`; that does not prove that the font still represents the designer's intended axis semantics.

---

# 2. Controlled research font

Environment:

- fontTools `4.63.0`;
- TrueType variable outlines;
- one `wght` axis: `300 / default 300 / 700`;
- named instances: `300`, `500`, `700`;
- explicit `STAT` values for Light / Medium / Bold;
- explicit non-linear `avar` control: normalized `+0.5 → +0.35` (serialized as approximately `0.3499755859375`);
- source glyph set: `.notdef`, `space`, `H`, `O`;
- subset target: Unicode `U+0048 H`.

The two master H advances are:

- `wght 300`: `620u`;
- `wght 700`: `680u`.

Because the positive half of the axis is deliberately remapped by `avar`, the intended `wght 500` H advance is not the linear midpoint.

Artifacts tested:

1. source variable TTF;
2. source variable WOFF2;
3. H-only subset variable TTF;
4. H-only subset variable WOFF2;
5. adversarial H-only subset WOFF2 with `avar` deliberately removed.

---

# 3. Bounded acceptance contract

For this experiment, the **product-specific** acceptance contract requires:

1. `fvar`, `gvar`, `STAT`, and the intentionally authored `avar` all remain present;
2. `wght` remains `300 / 300 / 700`;
3. named instances remain `300 / 500 / 700`;
4. the non-linear mapping remains `+0.5 → approximately +0.35`;
5. representative instance metrics remain equivalent at `300`, `500`, and `700`;
6. subsetting removes unused glyph variation data without changing the surviving glyph's axis behavior.

The requirement for `avar` in item 1 is **study/product-specific**, not a claim that every valid variable font must contain `avar`.

---

# 4. RESULT A — normal WOFF2 packaging preserved the variable-axis contract

Source variable TTF and its WOFF2 package both retained:

- `fvar`;
- `gvar`;
- `STAT`;
- `avar`;
- `wght 300 / 300 / 700`;
- all three named instances;
- the same non-linear `avar` mapping.

Measured H advances were identical:

| Artifact | wght 300 | wght 500 | wght 700 |
| --- | ---: | ---: | ---: |
| Source VF TTF | 620u | 641u | 680u |
| Source VF WOFF2 | 620u | 641u | 680u |

### TRANSFER VALIDATION

In this bounded fontTools path, WOFF2 packaging itself preserved the tested variable-font semantics.

This is not a universal WOFF2/browser result; it is a reproducible local transformation result.

---

# 5. RESULT B — normal subsetting pruned glyph closure while preserving axis semantics

After subsetting to `H`:

- glyph order reduced to `.notdef`, `H`;
- `gvar` coverage reduced to `.notdef`, `H`;
- `fvar`, `gvar`, `STAT`, `avar`, and `HVAR` remained;
- axis range and named instances remained;
- H advances remained `620 / 641 / 680` at `300 / 500 / 700`.

The same result survived packaging of the subset as WOFF2.

### SYNTHESIS

A correct variable-font subset operation may intentionally change glyph closure while needing to preserve the semantic behavior of the surviving variation space.

Therefore “binary equality” is not the right acceptance criterion after subsetting. The correct question is whether the **surviving product contract** remains equivalent.

---

# 6. FAILURE — a parseable WOFF2 retained `fvar/gvar/STAT` but changed the meaning of `wght 500`

The adversarial artifact removes only `avar` from the otherwise working H-only variable subset, then packages the result as WOFF2.

It remains parseable and still retains:

- `fvar`;
- `gvar`;
- `STAT`;
- the same visible `wght 300 / 300 / 700` axis range;
- named instances at `300 / 500 / 700`;
- the same endpoint H advances: `620u` and `680u`.

But the intermediate result changes:

| Artifact | H advance @ wght 500 |
| --- | ---: |
| Intended subset WOFF2 with `avar` | **641u** |
| Adversarial subset WOFF2 without `avar` | **650u** |
| Delta | **+9u** |

The file opens. It is still recognizably a variable font. The axis tuple still looks correct. Yet the same user coordinate no longer resolves to the same intermediate geometry/metric state.

### IMPORTANT SCOPE DISTINCTION

This mutation is not automatically an OpenType-invalid font merely because `avar` is absent. `avar` is optional.

The failure is instead:

> the delivered artifact no longer satisfies the **authored product axis contract** of this font.

This distinction is central to T010.

---

# 7. SYNTHESIS — external validators and studio release contracts solve different problems

T008–T010 now separate at least three QA classes:

1. **binary/spec/sanitizer QA** — is the font structurally valid and compatible with relevant standards/tool policies?
2. **distribution transformation QA** — did packaging/subsetting preserve required tables, glyph/feature closure and variation data?
3. **product semantic QA** — does the shipped artifact still produce the intended features, metrics, axis mappings and representative instances?

A broad validator can catch many important structural problems but cannot infer every intentional product semantic contract.

Conversely, a studio-specific checker can prove a bounded product contract while missing broad spec/vendor issues.

### STUDIO JUDGMENT

Production release gates should combine, not substitute:

`external broad QA + studio/product-specific semantic assertions + exact shipped-artifact integration tests`

For variable fonts with intentional axis mapping, representative coordinates should be regression-tested after every transformation that can rewrite or drop variation metadata.

---

# 8. External broad QA attempt

The current execution environment was checked for:

- `fontbakery`;
- `fontspector`;
- `ots-sanitize`.

None was available. A network installation attempt could not resolve package hosts.

### OPEN

T010 does **not** claim or simulate results from FontBakery, Fontspector, OTS, browser sanitizers, or vendor release profiles.

External broad QA remains a high-priority follow-up as soon as an executable environment is available.

---

# 9. What T010 establishes — and what it does not

## Established in this bounded practice

- WOFF2 packaging preserved the controlled variable-font tables and measured axis behavior;
- fontTools subsetting pruned unused glyph/gvar closure while preserving the controlled axis contract;
- `avar` removal can leave a parseable variable WOFF2 with intact `fvar/gvar/STAT` while changing the result at an intermediate user-space coordinate;
- release QA therefore needs product-semantic assertions beyond mere parseability/table presence.

## OPEN

T010 does not establish:

- FontBakery/Fontspector/OTS/sanitizer PASS;
- browser CSS `font-weight` or `font-variation-settings` behavior;
- WOFF2 cross-toolchain equivalence;
- multi-axis or three-master behavior;
- `avar` v2;
- CFF2 variable outlines;
- GPOS/kerning/mark/`locl` preservation;
- components/diacritics/multi-script closure;
- full naming/style-linking/family metadata quality;
- CoreText/DirectWrite/Skia/Flutter behavior;
- visual/raster equivalence;
- human reading or recognition performance;
- production-family release readiness.

Evidence level remains **PRACTICE + CRITIQUE**, not PASS.

---

## HANDOFFS TO OTHER SPECIALISTS

### Color

- Useful finding: the exact shipped variable-font artifact can change the effective Type state at a nominal axis coordinate if authored axis mapping is lost.
- Canonical section: T010 sections 6–7.
- Transfer note: strengthens C009's requirement to pin exact Type/render conditions; “wght 500” alone is insufficient if the shipped artifact's axis mapping differs.
- Scope limit: T010 makes no Color/readability threshold claim.

### Layout / Interaction

- Useful finding: Layout regression should identify the exact delivered variable-font artifact **and its axis mapping**, not only the axis tag/value.
- Canonical section: T010 sections 5–7.
- Transfer note: complements L003/L004; the observed `+9u` H advance is proof of font-semantic drift, not proof of a specific layout failure.
- Scope limit: Layout remains owner of wrap/track/density policy and product-threshold validation.

### Web Design

- Useful finding: a WOFF2 may remain parseable and expose the expected variable axis while an optional mapping table that is part of the product contract has been lost.
- Web application consequence: test the **exact shipped WOFF2** with CSS `font-weight` / `font-variation-settings`, representative axis positions, style matching, zoom/DPR and target browser/device matrices.
- Transfer note: T010 supplies the Type-side package contract; Web must independently verify browser integration.
- Scope limit: T010 is not browser or Web Design PASS.

---

## Next research implications

Highest-value follow-ups:

1. execute external FontBakery/Fontspector/OTS or equivalent broad QA when available and classify structural/spec/vendor-policy findings separately from product-semantic assertions;
2. extend distribution QA into GPOS/kerning, marks/anchors, `locl`, vertical metrics and multi-script closure;
3. broaden variable-family proof to three masters, multiple axes, components/diacritics, overlap strategy, `avar` complexity and CFF2;
4. transfer T001–T010 to actual browser/platform/app stacks using the exact shipped artifact.

Foundation remains **NOT PASSED**.
