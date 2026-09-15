# Typography / Type Design Specialist Status

Operating state: **ACTIVE — STAGE 2 PRACTICE / LOGMATE TYPE IDENTITY LIVE-PROJECT PRIORITY / T021 METHOD CALIBRATED, OPERATIONAL BREADTH NEXT**  
Governance sync: 2026-09-16  
Primary path: `research/type/`  
Next new-study ID: `T022` only after T021 family/spacing/operational evidence is sufficiently stable

## Current level
Stage 1 — Foundations: **PASS**  
Stage 2 — Intermediate Professional Practice: **PRACTICE / NOT PASSED**

Authority: T019 for Stage 1; T020 for Stage 2 entry.

## LIVE PROJECT PRIORITY — LogMate Type identity

Canonical incoming directive: `research/type/LOGMATE_TYPE_IDENTITY_LIVE_PROJECT_DIRECTIVE.md`.

The live LogMate project identified a transfer mismatch: T017–T020 solved conservative implementation safety but did not sufficiently answer the original product objective of developing a more distinctive LogMate typographic identity while preserving or improving operational alignment, scan rhythm and identifier legibility.

The current product controls are now more precise than the earlier status wording:

- **Control A — exact airport-only `LogMateRobotoMono` interim control.** The LogMate branch bundles a specific Roboto Mono artifact, labels the role `INTERIM_CONTROL_NOT_FINAL_TYPE_CONTRACT`, validates the asset in CI and has Flutter widget evidence for equal rendered width across airport samples. It is a deterministic temporary control, not the final identity.
- **Control B — proportional Roboto product baseline.** This remains the conservative general-UI reference from T017–T020.

Future T021–T024 work must demonstrate why a proposed system belongs to LogMate and why it is at least as good operationally as these controls. The live-project need pre-empts nonessential curriculum expansion.

## T021 current state

Canonical evidence now includes:

- original A/B/C mini-family comparison;
- actual outline/raster proof;
- lowercase `n` contour redraw;
- broader A/V/T/L/I transfer;
- shared-cap metric-model falsification;
- shape-sensitive pre-kerning metrics;
- pair/scanline geometry diagnostics;
- **mature-font pair-gap method validation / contradiction review**;
- **LogMate operational glyph-coverage audit**.

Three pre-kerning hypotheses remain A Compact, B Balanced and C Open. B remains only a working direction; no candidate is selected for product transfer.

### Executed evidence chain

The first custom-outline run exposed and corrected a cubic→TrueType build defect. Target-size rendering then exposed B's lowercase `n` drawing defect. A contour-only redraw changed raster output while preserving advances, correctly classifying that defect as drawing rather than kerning.

The broader A/V/T/L/I transfer exposed a second model-level defect: all new capitals originally shared one `cap_aw/cap_lsb`, forcing shape-different strings to identical advances. Per-glyph metrics removed that pathological equality while keeping kerning OFF.

A subsequent pair-gap diagnostic measured B `AV` gaps around `270–300u / 1000 UPM` and strong `LI/IL` height/order asymmetry. The earlier status over-interpreted those values as sufficient proof that A/V/T/L/I primitives themselves were defective.

### T021 method correction — CONTRADICTION REVIEW + INDEPENDENT VALIDATION

`T021-pair-gap-method-validation.md` independently applied the same conceptual kerning-off scanline geometry to mature controls.

Representative normalized `AV` ranges:

- Inter: about `318.4`;
- Noto Sans: `256.0–277.8`;
- Lato: `292.5–298.0`;
- DejaVu Sans: `293.9–294.4`;
- Liberation Mono: `250.0–252.0`;
- T021 B: `270.0–300.0`.

Mature controls also showed large `LI/IL` directional/height asymmetry.

Therefore:

> **pair-gap geometry is a useful descriptive signal, but the absolute `270–300u AV` magnitude is not a calibrated drawing-defect threshold.**

The automatic next step “redraw A/V/T/L/I until the scanline number shrinks” is withdrawn. This does not prove B is optically correct; it removes an unsupported defect rule.

Current evidence chain:

`metric alternatives → actual outlines → build correction → raster proof → drawing defect → contour redraw → broader transfer → shared-cap model failure → shape-sensitive base metrics → pair-gap diagnostic → mature-control method validation → absolute-gap threshold rejected → LogMate operational glyph breadth → target-size control comparison → kerning eligibility`

### T021 live-product breadth audit

`T021-logmate-operational-glyph-coverage-audit.md` compared the actual built mini-family (`H O n o A V T L I + space`) with the bounded LogMate corpus.

Measured bounded coverage:

- airport uppercase: **5/16 = 31.25%**;
- identifier uppercase: **4/11 = 36.36%**;
- identifier digits: **0/10**;
- numeric punctuation `, :`: **0/2**;
- ambiguity set `0 1 5 8 B I O S l`: **2/9 = 22.22%**;
- all bounded corpus characters: **6/33 = 18.18%**.

The present blocker is therefore much clearer: the candidate does not yet have enough real operational glyph breadth to support a credible LogMate identity/operational comparison.

## Stage 2 matrix

| Requirement | Current state |
| --- | --- |
| coherent glyph family | **PRACTICE — H/O/n/o + A/V/T/L/I executed; pair-gap magnitude no longer treated as a defect threshold; operational uppercase breadth incomplete** |
| spacing/control strings | **PRACTICE — shared-cap failure corrected; pair-gap diagnostic calibrated against mature controls; full LogMate control strings not yet renderable** |
| kerning classes/exceptions | **OPEN; deliberately blocked until family/operational breadth is sufficient to identify residual pair-specific needs** |
| figure styles | **PARTIAL / STRONG BRIDGE; current T021 candidate has no integrated product numerals yet** |
| diacritics/punctuation coherence | **PARTIAL; one product-relevant accented construction path still needed** |
| weight/width relationships | **PARTIAL / STRONG BRIDGE** |
| interpolation fundamentals | **SUPPORTED FOR ENTRY** |
| screen rendering/small-size compensation | **PRACTICE — intended-size raster/redraw evidence exists; full LogMate corpus candidate render OPEN** |
| typography across product roles | **PARTIAL / STRONG BRIDGE; live product controls established, custom candidate not yet broad enough** |
| multiple solutions + defended selection | **PRACTICE — A/B/C exist; B working only; no mature LogMate identity candidate selected** |

## Four-specialist balance

- **Type:** Stage 1 PASS; Stage 2 PRACTICE; live LogMate identity priority; pair-gap over-interpretation corrected; operational family breadth is the current blocker.
- **Color:** Stage 1 PASS; Stage 2 PASS; Stage 3 entry not yet audited.
- **Layout / Interaction:** Stage 1 PASS; Stage 2 PASS; Stage 3 entry not yet audited.
- **Web:** Stage 1 PASS; Stage 2 PRACTICE through W016; actual Chromium native/custom control transfer exists, network/runtime breadth remains incomplete.

Type and Web remain the two Stage 2 incomplete specialists. The LogMate live-project Type need currently takes precedence over nonessential Type curriculum expansion.

## Active next queue

1. **Expand T021 coherently toward the actual LogMate airport uppercase repertoire.** Missing airport letters are `B C D F G J K N R S X`; do not redraw A/V/T/L/I merely to chase a lower scanline-gap number.
2. Add identifier-specific uppercase still missing after the airport set, especially `E U`.
3. Add digits `0–9`, core operational punctuation `- : ,`, lowercase `l` for ambiguity inspection, and one accented construction path while preserving one family logic.
4. Rerender at actual LogMate target sizes and compare the same corpus against both controls: proportional Roboto and exact airport-only `LogMateRobotoMono`.
5. Use pair-gap geometry only as a descriptive diagnostic alongside raster proof, control strings, compactness and residual pair behavior.
6. Only after sufficient family breadth exists, open T022 for kerning classes/exceptions + proportional/tabular figure systems where product evidence justifies them.
7. T023 weight/interpolation + diacritic/punctuation coherence; T024 multi-role Type alternatives remain the likely LogMate identity integration path if evidence matures.

## OPEN / dependencies

Stage 2:
- coherent operational uppercase expansion;
- integrated digits/punctuation/accent breadth;
- target-size rendering across real LogMate airport/identifier/time strings;
- residual kerning model after base spacing is broad enough;
- integrated figure systems;
- design-level weight/width proof;
- final defended family selection;
- direct product-facing comparison showing whether a new system improves on proportional Roboto and the exact airport-only mono control.

Individual A/V/T/L/I outlines remain open to normal raster/family critique, but **absolute pair-gap magnitude alone is no longer a blocker**.

Later:
- FontBakery/Fontspector/OTS;
- direct HarfBuzz;
- naming/style linking;
- hinting;
- multi-axis/CFF2/components;
- Android/iOS/browser matrix;
- production PWA;
- larger complex scripts.

Human/app-stage validation remains deferred; no simulated human PASS.

## RELATED DOMAIN / HANDOFF state

### Layout / Interaction
Preserve semantic geometry and keep the airport Type seam replaceable. The exact mono control stabilizes current UI work but must not become immutable final geometry merely because it is deterministic.

### Web Design
Delay exact custom-family Web transfer until the candidate can render the bounded operational corpus without extensive fallback. When breadth is sufficient, test exact loading/fallback and responsive consequences.

### Color
Hold Color constant during Type identity comparisons; no Color contradiction was introduced by the pair-gap method review.

### LogMate UI
The current exact airport-only Roboto Mono implementation may continue as a **temporary validated control**. Do not spread mono automatically to aircraft type, registration, flight number, crew names or prose, and do not promote the interim airport control to final Type identity without comparison evidence.

## Latest checkpoint

- Stage 1: **PASS**.
- T020: **COMPLETE as conservative implementation evidence, not final LogMate identity resolution**.
- T021 actual outline/raster: **EXECUTED**.
- T021 lowercase `n` contour redraw: **EXECUTED**.
- T021 broader A/V/T/L/I transfer: **EXECUTED**.
- Shared-cap spacing parameterization: **FALSIFIED / REPLACED**.
- Shape-sensitive A/V/T/L/I base metrics: **EXECUTED**.
- Initial pair-gap diagnostic: **EXECUTED; useful descriptively**.
- Pair-gap defect-threshold interpretation: **CONTRADICTED / WITHDRAWN** after mature-control validation.
- Forced primitive A/V/T/L/I redraw as automatic next step: **CANCELLED**; revise only if specific raster/family evidence exposes a real defect.
- LogMate operational glyph coverage: **AUDITED — 18.18% of bounded corpus characters currently proven**.
- Operational uppercase family expansion: **NEXT**.
- Numerals/punctuation/accent breadth: **OPEN**.
- B direction: **WORKING, NOT FINAL**.
- T022: **NOT OPEN**.
- Stage 2: **NOT PASSED**.
