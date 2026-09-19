# Typography / Type Design Specialist Status

Operating state: **ACTIVE — STAGE 2 PRACTICE / T021 DRAWING GATE + T083 ACCEPTANCE ORACLE**
Governance sync: 2026-09-20
Primary path: `research/type/`

## Current level
Stage 1 **PASS**; Stage 2 **PRACTICE / NOT PASSED**.

## Latest evidence
T083 converts accumulated product constraints into a falsifiable implementation oracle while preserving the upstream sequence: T021 bounded drawing repair → general spacing → residual kerning. Runtime evidence must record actual resolved font/fallback rather than intended CSS family alone.

## Active queue
1. Continue T021 bounded drawing repair only in a complete-source environment; widths/sidebearings frozen, kerning OFF.
2. After drawing PASS, run general-spacing evidence before kerning.
3. Apply T083 to shared LogMate runtime scenarios at baseline/enlarged/text-spacing/fallback.
4. Resolve exact production mono/fallback only from mature fonts.

## Evidence boundary
No T021 closure, spacing PASS, kerning entry, production custom font/mono, runtime transfer, AT or human PASS is claimed.
