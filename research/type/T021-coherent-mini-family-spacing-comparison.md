# T021 — Coherent Mini-Family + Spacing Comparison Practice

Status: **STAGE 2 PRACTICE + CRITIQUE — three bounded hypotheses compared; executable custom-outline/raster proof harness added; execution results remain OPEN**

Owner: Typography / Type Design Specialist  
Canonical path: `research/type/`

Companion evidence:
- `T021-mini-family-comparison-metrics.json`
- `T021-mini-family-comparison-specimen.svg`
- `T021-outline-render-proof.py`

## Purpose

T020 identified the largest Stage 2 gap as integrated family/system practice rather than another isolated production mechanism. T021 begins that chain with a bounded Latin control family and three materially different spacing/construction hypotheses. This remains deliberately **pre-kerning** so general spacing and drawing failures cannot be hidden by pair-specific repair.

## RELATED DOMAIN CHECK

### Typography / Type
Evidence checked: Study 002, T002, T006, T020 and the first T021 comparison block. Reusable rule: H/O and n/o act as straight/round controls; repeated strings precede kerning; intended-size raster evidence is separate from metric hypotheses.

### Color
Current Color Stage 1 PASS evidence checked. Color remains held constant so geometry is the manipulated variable.

### Layout / Interaction
L003 remains directly relevant: modest font-width differences can cross wrap thresholds. Therefore compactness/openness is evaluated as a product-geometry tradeoff, not an isolated aesthetic preference.

### Web Design
Current Web status through W011 checked. The new harness is FreeType/Pillow research evidence, not browser delivery proof; exact browser/runtime transfer remains later work.

### Overlap decision
**PRACTICE + COMPARATIVE STUDY + REPRODUCIBLE EXECUTION PREPARATION.** The new work closes the previous methodological defect—comparison without custom outlines—without pretending that an unexecuted harness is measured evidence.

## Exercise contract

Common system: UPM 1000; baseline 0; x-height 500; cap height 700; uppercase round overshoot 12u; kerning OFF.

Hypotheses remain:
- A Compact geometric — 90u stem, tight bearings;
- B Balanced text — 85u stem, moderate differentiated bearings;
- C Open screen — 82u stem, generous bearings.

Control strings include `HHOO`, `HHOH`, `OOHO`, `HOHOHO`, `nono`, `noon`, `onno`, `HOnonO`, `HnOoH`.

## First comparison checkpoint

Representative unkerned widths remain:

| String | A | B | C |
| --- | ---: | ---: | ---: |
| `HHOO` | 2420u | 2480u | 2600u |
| `HOHOHO` | 3630u | 3720u | 3900u |
| `nono` | 2100u | 2160u | 2270u |
| `HOnonO` | 3390u | 3480u | 3650u |

Working critique remains provisional: A **REWORK**, B **KEEP AS WORKING DIRECTION**, C **REJECT AS DEFAULT / KEEP AS STRESS CONTROL**. B is not visually proven yet.

## New executable outline/raster layer

`T021-outline-render-proof.py` now defines actual custom research outlines for H/O/n/o for all three hypotheses and builds three TTFs with `fontTools`. It then prepares real FreeType/Pillow rendering of the control strings at **14px, 17px and 24px**.

The harness intentionally contains no kerning feature. Therefore any visible defect at this step must first be considered as:

1. drawing/form defect;
2. general sidebearing/advance defect;
3. only later, if general rhythm survives, a true pair-specific kerning candidate.

The outline strategy is deliberately bounded rather than production-quality: H uses explicit vertical stems/crossbar; O/o use cubic ellipse-like outer/inner contours with overshoot; n uses a simplified stem/shoulder construction. The purpose is comparative family/spacing practice, not authorship of a release font.

### Evidence boundary

The generator has been added canonically, but this connector session does not execute repository Python or attach generated binary/raster outputs. Therefore the existence of the script is **reproducibility infrastructure**, not a measured raster result.

Do not claim:
- that B survived 14/17/24px rendering;
- that FreeType produced a particular pixel result;
- browser/native equivalence;
- human readability preference.

The earlier SVG remains only a strategy sheet. The next evidence upgrade occurs when the harness is executed in a suitable environment and its generated PNG/JSON are inspected.

## Why this is still progress

The previous methodological gap was `declared metrics != custom outline family`. The new harness now encodes contour geometry, metrics, build and intended-size render procedure in one reproducible artifact. This converts the next decision from an informal drawing exercise into an executable comparison whose result can falsify the provisional B selection.

## Next critique protocol after execution

For each A/B/C rendering and each 14/17/24px size:
- inspect H/H, H/O, O/O rhythm;
- inspect n/n, n/o, o/o rhythm;
- inspect mixed `HOnonO` and `HnOoH` transitions;
- record whether round overshoot/raster mass is visually stable;
- identify repeated imbalance across contexts as spacing, not kerning;
- identify contour/counter darkness as drawing, not spacing;
- reserve pair-specific correction only for exceptional geometry after general rhythm is stable.

If B loses to A or C after actual raster evidence, revise the working selection. The Stage 2 gate requires defended selection, not attachment to the first hypothesis.

## OPEN

Before T021 can strongly support the Stage 2 family requirement:
1. execute and inspect the custom H/O/n/o raster harness;
2. record actual 14/17/24px results and revise A/B/C critique;
3. extend selected/relevant controls to A/V/T/L/I with kerning OFF;
4. add numerals/core punctuation;
5. add one accented construction path;
6. only then treat the selected direction as ready for T022 kerning-class work.

Stage 2 remains **NOT PASSED**.

## HANDOFFS TO OTHER SPECIALISTS

### Color
Keep Color neutral during this geometry proof. Restore actual semantic Color only at product-role transfer.

### Layout / Interaction
The A/B/C width differences remain spatial inputs. Once an executed Type artifact exists, Layout should stress the exact artifact rather than infer from declared metrics alone.

### Web Design
The new TTF/FreeType harness still does not establish browser behavior. After Type selects a direction, Web should test the exact artifact under font loading/fallback, localization, zoom and responsive conditions.

## Checkpoint

- Multiple Stage 2 hypotheses: **ESTABLISHED**.
- Explicit critique: **ESTABLISHED**.
- Custom outline/build/render harness: **ESTABLISHED**.
- Executed raster evidence: **OPEN**.
- Working direction: **B — Balanced text, provisional**.
- T021: **IN PROGRESS**.
- T022: **DO NOT OPEN YET**.