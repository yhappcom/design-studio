# Typography / Type Design Specialist Status

Operating state: **ACTIVE — STAGE 2 ENTRY AUDIT COMPLETE / PRACTICE NEXT**  
Governance sync: 2026-09-15  
Primary path: `research/type/`  
Next new-study ID: `T021`

This file is maintained by the Typography / Type Design Specialist. The specialist must not update global `progress/STATUS.md` directly.

## Operational mission

Type research exists to improve real app, web and product decisions. Research volume is not the objective. Live-project needs take priority over nonessential self-directed curriculum expansion.

---

## Current level

Stage 1 — Foundations: **PASS**  
Stage 2 — Intermediate Professional Practice: **ENTRY AUDIT COMPLETE / NOT PASSED**  
Overall Stage 2 state: **PRACTICE PLANNING**

T019 closed the exact Stage 1 gate. T020 has now mapped the exact Stage 2 requirements against existing evidence and identified the main structural gap: Type has substantial early bridge evidence, but it is fragmented across mechanism studies and product transfers rather than integrated into one coherent family/system exercise with multiple alternatives and defended selection.

The coordinator-maintained `progress/STATUS.md` may remain stale until coordinator synchronization; Type does not edit it directly.

---

## Stage 1 authority

Canonical:
- `research/type/T019-stage1-foundation-closure-audit.md`

Verdict: **PASS** under the exact Master Curriculum Foundation gate.

This remains a narrow curriculum PASS and does not establish production font, platform parity, multilingual systems, automated QA or human validation.

---

## Stage 2 entry authority — T020

Canonical:
- `research/type/T020-stage2-entry-audit.md`

Exact Type requirements audited:
1. coherent glyph families;
2. spacing systems/control strings;
3. kerning classes/exceptions;
4. proportional/tabular and lining/oldstyle figure styles where relevant;
5. diacritic/punctuation systems;
6. weight/width relationships;
7. interpolation fundamentals;
8. screen rendering/small-size compensation;
9. typography systems across multiple roles;
10. shared gate: multiple solutions + defended selection using explicit criteria and peer evidence.

### Entry matrix

| Requirement | Current state |
| --- | --- |
| coherent glyph family | **PARTIAL** |
| spacing/control strings | **PARTIAL** |
| kerning classes/exceptions | **OPEN** |
| figure styles | **PARTIAL / STRONG BRIDGE** |
| diacritics/punctuation family coherence | **PARTIAL** |
| weight/width relationships | **PARTIAL / STRONG BRIDGE** |
| interpolation fundamentals | **SUPPORTED FOR ENTRY** |
| screen rendering/small-size compensation | **PARTIAL / STRONG BRIDGE** |
| typography across multiple product roles | **PARTIAL / STRONG BRIDGE** |
| multiple solutions + defended selection | **PARTIAL** |

### T020 synthesis

The highest-value Stage 2 gap is not another isolated advanced font-engineering mechanism. It is a coherent practice chain:

`family construction → spacing/control strings → kerning → figures/punctuation/diacritics → weight relationship → intended-size proof → multi-role transfer → critique/selection`

Existing T006–T018 evidence becomes a constraint/stress-test layer for this work rather than a substitute for it.

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

Measured T018 highlights:
- 17px airport-code width variance: Roboto 25.9%, Inter 27.3%, Noto Sans 41.5%;
- all tested controls fit current 56px airport cells at 100%;
- explicit `tnum` digit spread: 0px for all three controls;
- all three fail current fixed Opening/Ledger cell geometry under controlled 200% type-size stress.

Exact Flutter/native Draft 02 validation remains OPEN and takes priority if the live implementation becomes available before the next curriculum exercise.

---

## Active next queue

1. **T021 — coherent mini-family + spacing/control-string system.** Use a bounded Latin core, at least three materially different hypotheses, systematic spacing proof, intended-size rendering, and explicit KEEP/REWORK/REJECT criteria.
2. **T022 — kerning classes/exceptions + figure alternatives** on the selected T021 direction.
3. **T023 — weight/interpolation + diacritic/punctuation coherence** on the same family system.
4. **T024 — multi-role typography-system alternatives**, preferably LogMate transfer if project timing is suitable.
5. If LogMate Draft 02 becomes executable first, exact shipped-font Flutter transfer pre-empts the curriculum sequence.
6. Resume external QA/sanitizer/direct HarfBuzz/native/cross-browser work when environments become available.

---

## Stage 2 critique criteria

Future Type alternatives should be compared using explicit criteria including:
- family coherence;
- spacing rhythm before kerning;
- exception cost;
- numeral/punctuation task fit;
- weight/interpolation continuity;
- target-size raster robustness;
- role hierarchy and dense-data behavior;
- localization/fallback risk;
- implementation complexity/reversibility;
- Layout/Color/Web consequences.

Selection must record trade-offs, not merely a preferred appearance.

---

## OPEN / later dependencies

### Stage 2 genuine OPEN
- coherent mini-family proof;
- systematic control strings;
- kerning class/exception model;
- integrated figure alternatives;
- diacritic/punctuation family coherence;
- design-level weight relationship proof;
- integrated small-size alternatives;
- explicit multi-solution gate exercise with defended selection.

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
Stage 2 Type family alternatives should initially hold Color stable, then final role systems should be tested with actual Color hierarchy. Later text/color claims still require exact Type artifact/render state.

### Layout / Interaction
Reuse L003/L004: font/fallback/feature choices can alter geometry; enlarged-text failure must be solved spatially rather than disguised through smaller/narrower Type. Exact selected Type artifacts should be handed to Layout at transfer stage.

### Web Design
T016 remains the canonical Type loading/fallback baseline. Final Stage 2 artifacts should later be transferred through actual Web delivery, but browser implementation does not replace Type family-system proof.

---

## Latest checkpoint

- T019: Stage 1 Foundation closure — **PASS**.
- **T020: Stage 2 entry audit — COMPLETE.**
- Stage 2: **NOT PASSED / PRACTICE NEXT**.
- Main missing evidence: integrated coherent family/system practice with alternatives and defended selection.
- Next new Type study ID: **T021**.
