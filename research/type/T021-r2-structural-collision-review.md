# T021 — R2 Structural Collision Review

Status: **CONTRADICTION REVIEW / STATIC SOURCE AUDIT EXECUTED / DRAWING GATE FAIL / R3 REDRAW REQUIRED**  
Date: 2026-09-16  
Owner: Typography / Type Design Specialist

## Why this block exists

The latest canonical evidence changed materially after the prior status file. Commit `340705130357eed2d715439bec1577ed94d40561` repaired the exact T021 generator and commit `69df4f517d7f1066b7acf984c0d8636ef021e0a5` recorded a successful clean GitHub-hosted CI execution with 36/36 bounded encoded coverage. Therefore the old exact-source `KeyError: M` blocker is no longer current.

The next gate in the canonical evidence chain is drawing validity. This block does not infer visual quality from CI success. It adversarially inspects the R2 source construction itself before spending effort on spacing or kerning.

Reason for repetition: **CONTRADICTION REVIEW + INDEPENDENT VALIDATION**. The question is whether R2's structural repair actually creates distinguishable ambiguity-critical glyph constructions, not merely whether it builds.

## RELATED DOMAIN CHECK

- **Type:** T021 R2 generator, R2 canonical CI/gate review, prior raster critique and operational corpus were checked. Reusable rule: drawing → general spacing → pair residual → kerning.
- **Color:** not materially involved; no distinction in this audit may depend on color.
- **Layout / Interaction:** operational scanning and dense logbook contexts make character ambiguity consequential, but no human recognition result is inferred.
- **Web:** browser transfer remains downstream; a structurally unresolved font candidate should not be promoted merely because browser loading succeeds.
- **Content Design:** literal identifiers/times must not be rewritten to hide glyph ambiguity. The corpus pair `5S` remains an explicit stress case.

## Method

A deterministic source audit was added as `T021-r2-structural-collision-audit.py` with committed results in `T021-r2-structural-collision-audit-results.json`.

The audit removes width and coordinates and compares normalized construction topology for bounded ambiguity/control pairs. This is intentionally narrower than raster or human recognition testing.

It can establish that two characters are generated from the same structural recipe. It cannot establish that users confuse them, nor that different topology is sufficient for recognition.

## Finding 1 — `5` and `S` are the same normalized construction recipe

R2 `S` is built from:

- top bar;
- middle bar;
- bottom bar;
- left upper vertical;
- right lower vertical.

R2 `5` is built from exactly the same five structural elements in the same arrangement.

Their source widths differ (`S` 590u; digit `5` 560u), but width is carrying essentially all of the encoded distinction in this simplified construction.

This is a direct failure against the purpose of the bounded `5S` ambiguity control. A width difference may help at some sizes, but it is not an adequate basis for declaring the drawing gate credible.

**Verdict: REJECT current R2 `5/S` pair for T021 closure.**

## Finding 2 — `D`, `O`, and `0` share rectangular-ring topology

R2 `O` uses `ring()`. Digit `0` also uses `ring()` with different width/stem values. `D` uses `bowl()`, but at this abstraction level its left/top/bottom/right structure also reduces to a rectangular ring.

This does **not** mean the outlines are byte-identical. Their metrics, stem values and overshoot differ. It means the construction system currently provides no internal distinguishing feature among these forms beyond proportion/metric differences.

For `D/O`, shared broad topology is not itself unusual in type design; the relevant question is curve/straight-stem behavior and optical construction. R2's deliberately rectilinear primitives erase much of that distinction.

For `0/O`, the issue is more operational because the corpus explicitly contains `0O`. The current pair is differentiated mainly by width and stem thickness.

**Verdict: REWORK.** This is not a human-confusion claim, but it is insufficient evidence for an ambiguity-sensitive operational candidate.

## Finding 3 — `1/I/l` has materially stronger structural differentiation

The static source audit confirms different construction signatures:

- `1`: centered stem + base + upper flag;
- `I`: top/bottom bars + centered stem;
- `l`: narrow stem + foot.

This is structurally stronger than the `5/S` and `0/O` cases. It remains subject to 14/17/24px raster inspection and later human/product validation.

**Verdict: KEEP for next raster, not PASS.**

## Finding 4 — `8/B` also has different topology

`8` uses stacked upper/lower rings. `B` uses a full left stem with bowl structure. The construction distinction exists before width differences.

**Verdict: KEEP for next raster, not PASS.**

## Gate consequence

The latest CI evidence and this audit must be held simultaneously:

- exact-source reproducibility: **PASS**;
- bounded cmap coverage: **PASS (36/36)**;
- ambiguity-critical drawing construction: **FAIL because `5/S` collapses to one normalized recipe**;
- broader drawing validity: **OPEN pending deterministic R2/R3 raster**;
- general spacing: **BLOCKED by drawing gate**;
- pair-specific residual/kerning: **BLOCKED**;
- T021 closure: **NO**;
- T022 opening: **NO**.

This is a useful falsification: successful font build + complete cmap + measured advances are necessary engineering evidence, but they do not establish a coherent operational type family.

## R3 redraw contract — next executable block

The next revision should be narrow and falsifiable rather than redesigning everything at once.

### Mandatory structural changes

1. **Separate `5` from `S` at construction level.** Width alone is not accepted as the primary distinction. Preserve the literal `5S` control.
2. **Increase `0/O` structural distinction without relying on color or contextual substitution.** Candidate mechanisms may include proportion, counter treatment or a deliberate zero-specific feature; the selected mechanism must be justified against product tone and small-size raster behavior.
3. Preserve the currently distinct `1/I/l` and `8/B` construction logic unless raster evidence contradicts it.
4. Keep kerning OFF.

### Mandatory proof outputs

The canonical proof should emit deterministic specimen images at **14/17/24px** containing at minimum:

- `5S S5 555 SSS`;
- `0O O0 000 OOO`;
- `1Il lI1 111 III lll`;
- `8B B8 888 BBB`;
- airport strings;
- aircraft/flight identifiers;
- time/totals;
- `HHOO HOHOHO nono noon AVAVA TOTO LITIL`.

The specimen should be retained as a CI artifact together with the TTF and JSON measurement output. A build-only green CI run is not sufficient.

### Critique order after R3 execution

1. missing/fallback/placeholder;
2. structural drawing validity;
3. ambiguity-control raster distinction at 14/17/24px;
4. general sidebearing/spacing;
5. pair-specific residuals;
6. only then kerning eligibility.

## Workflow observability note

The latest R2 CI review reported an output-directory display mismatch while artifact upload still succeeded. The current generator source now writes to `/tmp/t021-logmate-expanded`, matching the older path. Because `.github` workflow files are outside the Type specialist writing boundary, this block does not edit workflow governance. Future canonical execution should verify the human-readable result path rather than assuming the previous mismatch persists.

## Evidence boundary

This audit is static source/topology evidence. It does not claim:

- human recognition or readability;
- raster quality;
- optical spacing quality;
- browser/native rendering parity;
- exact LogMate product-font comparison;
- production suitability.

Human observation remains deferred to app-development validation as instructed.

## HANDOFFS TO OTHER SPECIALISTS

### Layout / Interaction

Dense operational interfaces should retain literal ambiguity controls such as `5S`, `0O`, `1Il`, `8B`; layout should not solve a glyph-construction failure by adding unnecessary spacing everywhere.

### Web

Do not treat successful custom-font loading as proof of operational distinction. When R3 is structurally stable, Web can transfer-test actual font loading/fallback/zoom/rendering separately.

### Content Design

Do not rewrite identifiers or abbreviations merely to avoid weak glyph pairs. Necessary domain strings are valid stress inputs for Type.

## Verdict

**R2 materially advances T021 by restoring exact-source CI reproducibility and 36/36 bounded coverage, but it still fails the drawing gate. The decisive new defect is that `5` and `S` use the same normalized construction recipe; `0/O` also remains structurally weak. T021 stays open, spacing/kerning stay blocked, and the next work should be an R3 redraw plus deterministic 14/17/24px raster proof in one block.**
