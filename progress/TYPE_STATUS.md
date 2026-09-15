# Typography / Type Design Specialist Status

Operating state: **ACTIVE — STAGE 2 PRACTICE / T021 IN PROGRESS**  
Governance sync: 2026-09-15  
Primary path: `research/type/`  
Next new-study ID: `T022` only after T021 outline/render proof is sufficiently closed

This file is maintained by the Typography / Type Design Specialist. The specialist must not update global `progress/STATUS.md` directly.

## Operational mission

Type research exists to improve real app, web and product decisions. Research volume is not the objective. Live-project needs take priority over nonessential self-directed curriculum expansion.

---

## Current level

Stage 1 — Foundations: **PASS**  
Stage 2 — Intermediate Professional Practice: **PRACTICE / NOT PASSED**

T020 mapped the Stage 2 requirements. T021 has now opened the first integrated comparison exercise rather than returning to fragmented mechanism studies.

The coordinator-maintained `progress/STATUS.md` remains older than specialist evidence and is not edited by Type.

---

## Stage 1 authority

Canonical:
- `research/type/T019-stage1-foundation-closure-audit.md`

Verdict: **PASS** under the exact Master Curriculum Foundation gate.

---

## Stage 2 entry authority — T020

Canonical:
- `research/type/T020-stage2-entry-audit.md`

Main structural gap identified:

`family construction → spacing/control strings → kerning → figures/punctuation/diacritics → weight relationship → intended-size proof → multi-role transfer → critique/selection`

Existing T006–T018 evidence remains a constraint/stress-test layer, not a substitute for this chain.

---

## T021 — current practice state

Canonical:
- `research/type/T021-coherent-mini-family-spacing-comparison.md`
- `research/type/T021-mini-family-comparison-metrics.json`
- `research/type/T021-mini-family-comparison-specimen.svg`

### What is established

Three materially different pre-kerning hypotheses now exist under one 1000-UPM / cap 700 / x-height 500 / 12u round-overshoot contract:

- **A — Compact geometric:** 90u stem, tighter bearings, lowest width cost;
- **B — Balanced text:** 85u stem, explicit straight/round spacing differentiation, moderate width;
- **C — Open screen:** 82u stem, generous bearings, highest white-space reserve and width cost.

Representative calculated unkerned widths:

| String | A | B | C |
| --- | ---: | ---: | ---: |
| `HHOO` | 2420u | 2480u | 2600u |
| `HOHOHO` | 3630u | 3720u | 3900u |
| `nono` | 2100u | 2160u | 2270u |
| `HOnonO` | 3390u | 3480u | 3650u |

C is roughly 5% wider than B on representative controls; A is the compact boundary.

### Current critique

- A: **REWORK** — useful compact control, but least white-space reserve and greatest risk of later exception pressure.
- B: **KEEP AS WORKING DIRECTION** — balanced correction reserve and geometry cost.
- C: **REJECT AS DEFAULT / KEEP AS STRESS CONTROL** — useful openness hypothesis, but width cost is materially higher.

This is a **working selection**, not a visual/raster PASS.

### Evidence boundary discovered

The SVG comparison sheet uses the viewer's sans font and exposes the declared strategies; it is not custom-glyph rendering. Therefore:

`metric hypothesis != coherent outline family != target-size raster proof`.

T021 must not be marked complete on metrics alone.

---

## Stage 2 matrix after first T021 block

| Requirement | Current state |
| --- | --- |
| coherent glyph family | **PARTIAL — hypotheses established, custom outlines OPEN** |
| spacing/control strings | **PRACTICE — systematic strings + metrics established; rendered revision OPEN** |
| kerning classes/exceptions | **OPEN** |
| figure styles | **PARTIAL / STRONG BRIDGE** |
| diacritics/punctuation family coherence | **PARTIAL** |
| weight/width relationships | **PARTIAL / STRONG BRIDGE** |
| interpolation fundamentals | **SUPPORTED FOR ENTRY** |
| screen rendering/small-size compensation | **PARTIAL / STRONG BRIDGE; T021 custom proof OPEN** |
| typography across multiple product roles | **PARTIAL / STRONG BRIDGE** |
| multiple solutions + defended selection | **PRACTICE ESTABLISHED; final rendered selection OPEN** |

Stage 2 remains **NOT PASSED**.

---

## Latest live-product transfer — LogMate

T017/T018 remain active project evidence.

Standing provisional decisions:
- Roboto remains the provisional main family;
- do not use monospace merely because data is technical;
- operational identifiers remain proportional by default with semantic columns;
- explicit tabular figures for comparison-critical numeric roles;
- do not use tracking to fake equal airport-code width;
- replace blanket generic monospace in View Logbook;
- ship real declared weights rather than relying on missing-weight synthesis;
- preserve multilingual fallback seams;
- no bespoke LogMate font without a demonstrated mature-font failure.

T021 is a curriculum/type-design exercise, not a proposal to replace Roboto in LogMate.

---

## Active next queue

1. **Continue T021 before opening T022:** create actual custom H/O/n/o outlines for the hypotheses or at minimum the selected B plus adversarial A/C controls; render real control strings at 14/17/24px.
2. Classify failures as drawing / general spacing / true pair-specific kerning.
3. Extend the selected system to A/V/T/L/I with kerning OFF.
4. Add numerals, core punctuation and one accented construction path.
5. Only then open **T022 — kerning classes/exceptions + figure alternatives**.
6. T023 — weight/interpolation + diacritic/punctuation coherence.
7. T024 — multi-role typography alternatives, preferably LogMate transfer when useful.
8. Exact LogMate Flutter transfer pre-empts curriculum work if live implementation becomes available.

---

## OPEN / dependencies

### Stage 2 genuine OPEN
- actual coherent mini-family outlines;
- rendered control-string revision;
- kerning class/exception model;
- integrated figure alternatives;
- diacritic/punctuation family coherence;
- design-level weight relationship proof;
- integrated small-size alternatives;
- final multiple-solution selection after real rendering.

### Later-stage / production OPEN
- FontBakery/Fontspector/OTS or equivalent external QA;
- direct HarfBuzz tracing;
- complete naming/style-linking and production family coherence;
- broader hinting strategy;
- multi-axis/CFF2/component coverage;
- exact shipped LogMate Flutter binaries;
- Android/iOS/Firefox/Safari/native cross-platform transfer;
- production PWA loading/cache/failure;
- larger Korean/Arabic/complex-script systems.

### Human / app-stage validation
Deferred to app-development validation:
- identifier recognition/error rates;
- `0/O`, `1/I/l`, `5/S`, `8/B` task evidence;
- dense-ledger scan speed/error;
- physical low-light/device readability.

No human evidence is simulated or marked complete.

---

## RELATED DOMAIN / HANDOFF state

### Color
T021 holds Color stable while geometry alternatives are compared. Real Color hierarchy returns at product-role transfer.

### Layout / Interaction
L003 is directly reused: Type width is a spatial input near wrap thresholds. C's ~5% width premium over B is therefore a real transfer risk to test later, not an automatic rejection criterion by itself.

### Web Design
The T021 SVG is not browser font proof. Actual font artifacts should later be tested under the Web loading/fallback/zoom/localization stack; T016 remains the baseline.

---

## Latest checkpoint

- Stage 1: **PASS**.
- T020: Stage 2 entry audit **COMPLETE**.
- T021 first comparison block: **COMPLETE AS METRIC/CRITIQUE PRACTICE, NOT AS OUTLINE/RASTER PROOF**.
- Working direction: **B — Balanced text**.
- Stage 2: **NOT PASSED**.
- Next action: **continue T021 with real outlines and intended-size rendering before T022**.
