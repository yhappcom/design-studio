# L108 — Candidate 05 adaptive-geometry transfer

Status: **STAGE 3 PRACTICE / TRANSFER VALIDATION / RUNTIME OPEN**

## Question
Does Candidate 05 preserve professional relationships when the 390×844 owner-review composition is stressed by real SafeArea, narrow width, nonlinear text scaling and font fallback?

## RELATED DOMAIN CHECK
T086 actual scaling/fallback, C117 semantic boundaries, I104 action authority, W116 production provenance and CD122 string parity checked.

## Protected relationships
Do not preserve screenshot coordinates. Preserve:
- header identity ↔ Settings;
- Add Flight / View Logbook ↔ destination meaning;
- Current Period control ↔ period values;
- Recent record identity ↔ Date/Flight/Route/Block values;
- Activity range ↔ selected state ↔ values;
- Totals labels ↔ totals values;
- runtime error/recovery ↔ owning object/action when injected.

## PRACTICE matrix
Run exact coded Candidate 05 at baseline, representative narrow width, maximum supported platform text scaling, forced mature fallback and representative SafeArea/insets. Measure target rectangles, text boxes/line counts, clipping/overflow, section order, action-owner distance, focus occlusion and vertical scroll requirement.

Adaptation order:
1. intrinsic growth;
2. local redistribution;
3. row growth/wrap;
4. secondary-detail transfer/disclosure when semantics permit;
5. local scrolling where the data relationship requires it;
6. recoverable truncation only as a last resort.

## CRITIQUE / failure conditions
- FAIL if text/targets are shrunk to preserve 390×844 fit.
- FAIL if the continuous sheet causes unrelated sections to merge semantically under reflow.
- FAIL if a period/action control becomes visually detached from its values/state.
- FAIL if focus or recovery controls are obscured by sticky/system regions.
- FAIL if semantic reading/action order changes accidentally during recomposition.

The 44×44 month target is a product/platform choice; it must not be mislabeled as the WCAG 2.2 AA minimum. WCAG 2.2 Target Size (Minimum) uses 24×24 CSS px or specified spacing/exceptions for web conformance.

## Evidence boundary
No physical-device, AT, human workload/discoverability or Stage 3 PASS is claimed.

## HANDOFFS TO OTHER SPECIALISTS
T086 supplies real text geometry; I104 supplies ownership; C117 rechecks state boundaries after reflow; CD123 may change wording only after layout adaptation is exhausted; W117 records the same-build geometry.