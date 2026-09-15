# Typography / Type Design Specialist Status

Operating state: **ACTIVE — STAGE 1 PASSED / STAGE 2 ENTRY AUDIT NEXT**  
Governance sync: 2026-09-15  
Primary path: `research/type/`  
Next new-study ID: `T020`

This file is maintained by the Typography / Type Design Specialist. The specialist must not update global `progress/STATUS.md` directly.

## Operational mission

Type research exists to improve real app, web and product decisions. Research volume is not the objective. Live-project needs take priority over nonessential self-directed curriculum expansion.

---

## Current level

Stage 1 — Foundations: **PASS**  
Next curriculum step: **Stage 2 — Intermediate Professional Practice / entry audit pending**

T019 re-read the exact `curriculum/MASTER_CURRICULUM.md` gate and corrected the prior stage-boundary problem. The previous status kept broad family proof, native Android/iOS rendering, multilingual production transfer, external QA and human recognition as Foundation blockers even though the Master Curriculum places those requirements primarily in Stages 2–5.

This PASS is narrow. It means each explicit Type Foundation principle is supported by original exercise/critique evidence and peer-domain reuse. It does **not** mean production Type, platform parity, multilingual systems, automated QA, human validation or later curriculum stages are complete.

The coordinator-maintained `progress/STATUS.md` may remain stale until coordinator synchronization; Type does not edit it directly.

---

## Stage 1 closure authority — T019

Canonical:
- `research/type/T019-stage1-foundation-closure-audit.md`

Final gate matrix:

| Stage 1 requirement | Main evidence | Verdict |
| --- | --- | --- |
| character / glyph / font distinctions | Study 001 + T009–T015 | **PASS** |
| anatomy / metrics / UPM / alignment zones | Study 002 + Exercise 001 + T003/T004 | **PASS** |
| stroke / contrast / historical construction logic | Study 003 + Exercise 002 + Study 005 | **PASS** |
| Bézier drawing discipline | Study 003 + Exercise 002 + production-outline audits | **PASS** |
| overshoot / optical correction | Study 003 + Exercise 002 + T002 | **PASS** |
| spacing before kerning | Studies 001/002 + Exercise 001 | **PASS** |
| numeral systems / punctuation | Study 005 + Exercise 003 + T004 + T018 | **PASS** |
| proofing at intended size | Exercise 002 + T002 + T003/T004 + T018 | **PASS** |
| typography as composition / IA | Study 009 + T001/T016/T017/T018 + peer transfer | **PASS** |
| design history / precedent literacy | Studies 001/003/005 | **PASS** |
| original exercises | Exercises 001–003 + reproducible T-series controls | **PASS** |
| peer evidence checked / reused | T-series RELATED DOMAIN CHECKs + Layout/Color/Web transfer | **PASS** |

Key closure evidence:
- Exercise 001: three H/O metric/form hypotheses + critique;
- Exercise 002: construction/curve/optics specimen + critique;
- T002: intended-size 14/24/48px surrogate failure → redraw → new compact failure;
- Exercise 003 + T004: numeral/punctuation system planning advanced into compiled/rendered native outlines;
- T017/T018: live LogMate operational-data transfer, including measured Roboto/Inter/Noto Sans audit.

---

## Canonical evidence

Legacy:
- `001-type-as-system.md`
- `002-metrics-spacing-optical-rhythm.md`
- `003-stroke-contrast-bezier-optics.md`
- `005-numerals-punctuation-systems.md`
- `009-typography-as-information-architecture.md`

T-series:
- T001 Web typography fallback/reflow transfer
- T002 raster proof/redraw cycle
- T003 minimal font renderer matrix
- T004 native numeral/punctuation renderer proof
- T005 Latin/Korean mixed-script fallback
- T006 production outline audit
- T007 variable interpolation/source compatibility
- T008 production build/release QA
- T009 Webfont subset/feature contract
- T010 variable Webfont axis contract
- T011 Layout multiscript release contract
- T012 mark/mkmk anchor release contract
- T013 normalization-sensitive subset contract
- T014 Hangul normalization subset contract
- T015 Hangul browser canonical-cluster transfer
- T016 Webfont loading/fallback metric contract
- T017 LogMate operational-data typography/semantic-geometry transfer
- T018 LogMate conservative font candidate audit
- **T019 Stage 1 Foundation closure audit — PASS**

Reproducibility artifacts remain beside the relevant T-series studies. Generated experimental font binaries/screenshots are runtime outputs, not product assets or canonical source authority.

---

## Latest live-product transfer — LogMate

T017/T018 establish the provisional product contract:

`semantic geometry → role-specific Type behavior → OpenType feature → exceptional treatment`

Standing decisions:
- Roboto remains the provisional main family;
- do not use monospace merely because data is technical;
- operational identifiers remain proportional by default with semantic columns;
- use explicit tabular figures for comparison-critical numeric roles;
- do not use tracking to fake equal airport-code width;
- replace blanket generic monospace in View Logbook;
- ship real declared weights rather than relying on missing-weight synthesis;
- preserve multilingual fallback seams;
- no bespoke LogMate font is justified without a demonstrated mature-font failure.

Measured T018 highlights:
- 17px airport-code width variance: Roboto 25.9%, Inter 27.3%, Noto Sans 41.5%;
- all tested controls fit current 56px airport cells at 100%;
- explicit `tnum` digit spread: 0px for all three controls;
- all three fail current fixed Opening/Ledger cell geometry under the controlled 200% type-size stress.

Exact Flutter/native Draft 02 validation remains OPEN.

---

## Stage-boundary policy after Foundation PASS

### Stage 2 — Intermediate Professional Practice

True next Type requirements include:
- coherent glyph families;
- spacing systems/control strings;
- kerning classes/exceptions;
- proportional/tabular and lining/oldstyle figure systems where relevant;
- diacritic/punctuation family coherence;
- weight/width relationships;
- interpolation fundamentals;
- screen rendering/small-size compensation;
- typography systems across multiple roles;
- multiple solutions to the same problem with explicit selection criteria.

Existing early bridge evidence: T002–T010, T017/T018. Stage 2 is **not passed**.

### Stage 3+

Still OPEN at the appropriate later stages:
- family planning/character-set strategy;
- mixed-script/fallback systems;
- GSUB/GPOS/GDEF depth;
- variable-font architecture/axis discipline;
- vertical metrics/cross-platform behavior;
- hinting/rasterization depth;
- reproducible production pipeline and automated QA;
- browser/device/platform comparison;
- human recognition/reading/scan evidence;
- research-grade experimental/statistical evidence.

---

## Current OPEN / blockers

### Tool / production
- FontBakery/Fontspector/OTS or equivalent external broad QA;
- direct HarfBuzz glyph/cluster tracing;
- complete naming/style-linking and production family coherence;
- broader hinting strategy;
- three-master/multi-axis/CFF2/component/diacritic coverage.

### Platform
- exact shipped LogMate font binaries inside Flutter;
- Android/iOS physical renderer transfer;
- Firefox/Safari/native cross-platform shaping;
- PWA production loading/cache/failure/fallback;
- actual Flutter 200% text scaling with final responsive layout.

### Multilingual
- exact Roboto + Korean fallback line metrics/rendering;
- Arabic/RTL and other complex scripts;
- larger production Korean corpus/line breaking;
- mixed-script user-data line boxes.

### Human / app-stage validation
Deferred until app-development validation as instructed:
- identifier recognition/error rates;
- `0/O`, `1/I/l`, `5/S`, `8/B` task evidence;
- dense-ledger scan speed/error;
- real low-light/device/readability evidence.

No human evidence is fabricated or marked complete.

---

## Four-specialist balance after T019

- **Type:** Stage 1 PASS; Stage 2 entry audit next.
- **Color:** Stage 1 PASS; Stage 2 entry audit next.
- **Layout / Interaction:** Stage 1 PASS; Stage 2 entry audit next.
- **Web:** Stage 1 PASS; Stage 2 entry audit next.

All four specialists now have narrow Foundation PASS under the same Master Curriculum gate model. Future balance decisions should therefore compare actual Stage 2 gaps and project utility rather than assuming Web or Type is behind from older status summaries.

---

## Active next queue

1. **T020 — Stage 2 entry audit** against the exact Master Curriculum; map existing early bridge evidence and identify only genuine Intermediate-practice gaps.
2. If LogMate Draft 02 becomes executable first, prioritize exact shipped-font Flutter transfer because live-project needs outrank nonessential curriculum expansion.
3. Resume external QA/sanitizer and direct HarfBuzz/native/cross-browser work when environments are available.
4. Keep human validation deferred to app/project stage rather than simulating it.

---

## HANDOFFS TO OTHER SPECIALISTS

### Color
Type now uses the same narrow Foundation closure logic as Color C014/C015. Later text/color validation still requires exact shipped Type artifacts.

### Layout / Interaction
L003/L004 reuse valid canonical Type Foundation evidence. T018 confirms enlarged-text fixed-cell failures remain a spatial recomposition problem at later transfer stages.

### Web Design
W009's reuse of Type Study 009/T016 is consistent with Type Foundation PASS. Browser evidence does not substitute for native production Type validation.

---

## Latest checkpoint

- **T019 completed: exact Master Curriculum Stage 1 closure audit.**
- **Type Stage 1 — Foundations: PASS.**
- Later production/platform/multilingual/human gaps remain explicit and active at their correct stages.
- Next new Type study ID: **T020**.
- Next action: **Stage 2 entry audit**, unless a live-product transfer need takes priority.
