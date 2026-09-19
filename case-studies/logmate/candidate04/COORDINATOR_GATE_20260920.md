# LogMate Home Candidate 04 — Coordinator Gate — 2026-09-20

Status: **OWNER-REVIEW ELIGIBLE / VISUAL-ONLY CONCEPT / RUNTIME OPEN**

## Scope check

Candidate 04 was rebuilt after the owner clarified that the current task is visual-design concept exploration, not data or macro-layout redesign.

Frozen across this candidate:
- Home information families;
- Home order;
- canonical data fixtures;
- product semantics;
- action/destination set;
- operational comparison geometry.

Canonical sequence preserved:
`Header -> Actions -> Search -> Current Period -> Recent -> Activity -> Totals`

The earlier Route Journal branch is excluded from this candidate's lineage.

## Isolation

Generation inputs:
- restore point `f992d62a98193629d19346a022a64deef824570c`;
- canonical LogMate product contracts;
- current assets;
- owner-wide visual direction;
- Design Studio foundation principles and current specialist criteria.

Excluded:
- sealed Candidate 01;
- rejected Candidate 02;
- rejected Candidate 03;
- rejected Round-1 concepts;
- contaminated Route Journal Candidate 04 branch.

Isolation result: **PASS**.

## Implementation

Branch:
`design/home-candidate-04-visual-only-20260920`

Corrected Flutter implementation:
`d6d46d014b10ea6ff905991a95e9b586450bc5a5`

Primary source:
`design/prototype/logmate_visual_preview/lib/home_candidate_04_visual.dart`

Concept:
**Graphite Editorial**

Visual-only variables:
- dark-first graphite atmosphere with a light paper counterpart;
- low-radius square action/search surfaces;
- uppercase editorial section and micro labels;
- flat tonal depth instead of card shadow;
- fine rules;
- bounded operational mono;
- proportional tabular summary numerics;
- appearance-calibrated mint accent.

## Render evidence

Deterministic 390×844 dark/light review renders were generated from the same tokens, spacing, content and geometry as the Flutter implementation.

GitHub Actions run `35475783670` again failed before any runner step executed. The job contains zero executed steps.

Therefore:
- no Flutter analyze PASS;
- no Flutter contract-test PASS;
- no Flutter golden PASS;
- no runtime/native/PWA PASS.

Static aesthetic review remains valid as code-origin concept evidence only.

## R1 specialist blockers

Type / Layout / Interaction / Content passed the visual concept path.

Color raised two blockers:
1. light mint text contrast;
2. tertiary text/placeholder contrast in both appearances.

Additional code inspection found and corrected:
- unsupported intermediate Flutter font-weight values;
- target sizing for Settings/month controls;
- redundant Block Time labeling.

## R2 specialist gate

- Type: **PASS FOR OWNER AESTHETIC REVIEW**
- Color: **PASS FOR OWNER AESTHETIC REVIEW**
- Layout / Spatial: **PASS FOR OWNER AESTHETIC REVIEW**
- Interaction: **PASS FOR OWNER AESTHETIC REVIEW**
- Content: **PASS FOR OWNER AESTHETIC REVIEW**
- Web / Runtime: **PASS FOR OWNER AESTHETIC REVIEW ONLY / RUNTIME PASS PROHIBITED**

No R2 specialist has an unresolved CHANGES REQUIRED blocker for static owner review.

## Contrast corrections

Appearance-specific calibration:
- dark accent `#00A693` on `#11120F` ≈ 6.15:1;
- light accent `#007C70` on `#F3F1EC` ≈ 4.52:1;
- dark tertiary `#80827B` on `#11120F` ≈ 4.83:1;
- light tertiary `#6B6E67` on `#F3F1EC` ≈ 4.59:1.

These are static concept checks, not full accessibility conformance claims.

## Remaining OPEN

- production font families/fallback;
- Flutter/native/PWA runtime;
- narrow/enlarged/text-spacing;
- forced-colors/reduced-motion;
- route/focus/Search behavior;
- physical-device/glare/night;
- representative-pilot usability and aesthetic preference.

## Verdict

**OWNER-REVIEW ELIGIBLE.**

This means the concept has completed the pre-owner visual gate.

It does not mean:
- preferred direction;
- final baseline;
- production palette;
- production-ready UI;
- Masterpiece;
- superiority to any sealed comparison candidate.
