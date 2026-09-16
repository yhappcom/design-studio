# T021 — R3 Exact CI Raster Critique

Status: **EXACT CI EXECUTED / ARTIFACT RETAINED / AMBIGUITY SEPARATION IMPROVED / COHERENT DRAWING GATE STILL FAIL**  
Date: 2026-09-16  
Owner: Typography / Type Design Specialist

## Scope

This block followed the R2 structural-collision audit with an executable R3 redraw. It changed the ambiguity-critical construction, emitted deterministic 14/17/24px specimens, repaired the independent raster-proof path, repaired the workflow artifact path, ran the exact repository source on GitHub-hosted CI, downloaded the retained artifact and visually inspected the exact 17px specimen.

This is source + CI + raster critique. It is not human recognition evidence or production approval.

## RELATED DOMAIN CHECK

- **Type:** T021 R2 structural collision review and prior raster critique define the gate order: drawing → intended-size raster → general spacing → pair residual → kerning.
- **Color:** held constant; no glyph distinction depends on color.
- **Layout / Interaction:** literal operational strings remain the stress substrate; layout is not used to conceal glyph defects.
- **Web:** browser transfer remains downstream of a stable drawing candidate.
- **Content Design:** identifiers/times remain literal; no wording substitution hides ambiguity.

## R3 construction changes

### `5/S`

R2 used the same normalized five-element recipe. R3 keeps digit `5` rectilinear but changes `S` to top/middle/bottom bars connected through diagonal transition shoulders. Therefore the source-level collision is resolved: `S` and `5` no longer share the same normalized construction recipe.

### `0/O`

Uppercase `O` remains a ring. R3 digit `0` adds an internal diagonal slash. The pair now has an explicit internal structural distinction rather than depending mainly on width/stem differences.

### retained controls

`1/I/l` and `8/B` retain their prior distinct construction logic.

Kerning remains OFF.

## Exact execution chain

Commit `1c7fff7e2f87e83c98ed2f398f4b12199db8c3ca` introduced the R3 generator. Its first workflow run correctly exposed stale downstream R2 paths: the R3 generator itself succeeded with 36/36 coverage and emitted three specimen names, but the old raster-proof script still requested the R2 binary and artifact upload still targeted the old directory. That run therefore failed and is retained as useful integration-failure evidence.

Commit `10164f7ba7c723ce8424651522d40af94bb28eda` aligned the independent raster proof with R3. The generator and independent raster steps then both passed, while upload still failed because the workflow itself retained the old directory.

Commit `672d22420e82ca58c82ab7bcd36f49409340ea51` aligned the workflow result and artifact paths with R3. Workflow run `35042035613` then executed:

- dependency installation: PASS;
- exact R3 generator: PASS;
- independent raster proof: PASS;
- measured-result display: PASS;
- artifact upload: PASS.

Artifact `t021-logmate-operational-proof-r3` (artifact id `10425721703`) retained the R3 TTF, JSON and both specimen sets.

This is a complete exact-source → CI → retained-raster chain, not an equivalent local reconstruction.

## Engineering results

R3 exact CI reported:

- revision: `R3-ambiguity`;
- kerning: OFF;
- required distinct non-space characters: 36;
- covered: **36/36**;
- missing: `[]`;
- deterministic specimens: 14px / 17px / 24px.

The existing metric model remains stable. Representative 17px values include `ICN` 28.1406px, `B737-900` 74.3438px, `00:45` 43.1562px, `5S` 19.5469px and `0O` 20.0625px.

## Exact 17px raster critique

The downloaded CI artifact was inspected directly.

### Improvement — ambiguity mechanisms now survive rasterization

The R3 source changes are not merely dead code. The 17px specimen shows a visible internal distinction between `0` and `O`, and `5/S` no longer consists of byte-equivalent/normalized-equivalent construction recipes. This closes the specific R2 structural-collision defect.

### FAIL — `S` is still not a mature family drawing

The diagonal-shoulder R3 `S` is distinguishable from `5`, but it still reads as a highly angular segmented form rather than a coherent S compatible with the rest of the family. Distinction alone is not sufficient. The drawing gate asks for coherent glyph design, not only pair separation.

**REWORK:** retain structural separation but redesign the S spine/shoulders/terminals so the form is recognizably S-like at 14/17/24px without collapsing back into the digit-5 recipe.

### FAIL — broad family remains over-schematic

The exact specimen confirms the larger limitation already exposed by the first raster critique: many glyphs are still built from coarse rectangular/polygonal primitives. `B`, `D`, round forms, several figures and lowercase `n` do not yet constitute a mature coherent text/operational family. The R3 block intentionally did not redesign every glyph, so this is expected but remains a gate failure.

### REWORK — slashed zero is effective but not yet selected product identity

The slash gives `0/O` strong structural differentiation in the specimen. However, this block does not establish that a slashed zero is the correct LogMate identity choice. It may create visual density or clash with product tone. Keep it as a viable ambiguity solution for comparison, not as a final default.

### KEEP — `1/I/l` and `8/B` remain useful controls

Their distinct structures remain visible enough to continue into the next drawing iteration. No human error-rate claim is made.

## Spacing consequence

General spacing is **still blocked**. The specimen contains enough unresolved drawing geometry that sidebearing judgments would conflate shape and whitespace. The prior rule remains binding: do not use spacing or kerning to repair drawing defects.

The equal-advance figures continue to be measurable, but proportional-vs-tabular selection remains T022 work only after T021 drawing/base-spacing closure.

## KEEP / REWORK / REJECT

- **KEEP:** exact CI/artifact chain; 36/36 coverage; deterministic 14/17/24 specimen method; literal ambiguity controls; kerning OFF; explicit `0/O` differentiation as one candidate; distinct `1/I/l` and `8/B` logic.
- **REWORK:** S construction; B/D/round-family joins and counters; lowercase n shoulder; several figures; punctuation optical placement; then reraster before base spacing.
- **REJECT:** treating structural distinction alone as coherent-family PASS; opening T022 merely because R3 CI is green.

## Gate decision

- exact-source reproducibility: **PASS**;
- bounded coverage: **PASS 36/36**;
- deterministic intended-size raster generation: **PASS**;
- R2 `5/S` normalized collision: **RESOLVED**;
- R2 weak `0/O` structure: **RESOLVED at mechanism level / product choice still OPEN**;
- coherent family drawing: **FAIL**;
- general spacing: **BLOCKED**;
- pair-specific residual/kerning: **BLOCKED**;
- T021 closure: **NO**;
- T022 opening: **NO**.

## Next large block

Do not return to source summaries. Use the exact R3 specimen as the failure substrate and execute a broader R4 family redraw in one block: S first, then B/D/O/C/G consistency, lowercase n, deficient figures and punctuation. Rerun exact 14/17/24 CI specimens, critique them, revise within the same block where feasible, and only if drawing validity becomes credible begin general sidebearing analysis.

## HANDOFFS TO OTHER SPECIALISTS

### Layout / Interaction

The literal operational controls remain valuable. Do not compensate for current drawing immaturity with global layout expansion.

### Web

R3 now has a reproducible retained font+raster artifact chain, but browser transfer should wait until the coherent-family drawing gate is materially stronger.

### Content Design

Continue preserving literal identifiers and numeric strings; Type must solve the ambiguity rather than rewrite domain content.

### Color

No change. Character identity remains independent of color.

## Verdict

**R3 is a substantive advance: the exact repository path now produces and retains 14/17/24px raster evidence, the R2 `5/S` source collision is removed, and `0/O` receives an explicit structural distinction. Direct inspection of the exact CI raster nevertheless rejects a coherent-family PASS. T021 remains open at drawing validity, and spacing/kerning remain blocked until a broader R4 redraw succeeds.**
