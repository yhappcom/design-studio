# LogMate Home Candidate 06 — Coordinator Gate — 2026-09-20

Status: **OWNER-REVIEW ELIGIBLE / VISUAL-ONLY CONCEPT / RUNTIME OPEN**

## Scope

Candidate 06 is a visual-only concept on the frozen Home product structure.

Frozen:
- information architecture;
- section order;
- data fixtures;
- action/destination placement;
- product semantics;
- operational comparison geometry.

Sequence preserved:
`Header -> Actions -> Search -> Current Period -> Recent Flights -> Activity -> Totals`

## Isolation

Restore point:
`checkpoint/home-structural-baseline-20260919 @ f992d62a98193629d19346a022a64deef824570c`

Branch:
`design/home-candidate-06-visual-only-20260920`

Excluded during generation:
- sealed Candidate 01;
- rejected Candidates 02–05;
- Round-1 concepts.

No prior candidate render, rationale or styling was used as generation input.

Isolation result: **PASS**.

## Concept

**Precision Neutral**

The candidate intentionally removes most decorative surface language.

Visual-only characteristics:
- near-neutral light/dark canvas;
- no section cards;
- Actions defined by shared horizontal rules;
- Search defined by one functional lower boundary;
- Current Period as one measurement region;
- Recent Flights as an open operational table;
- Activity selected state as neutral field + dot geometry + weight + accent;
- Activity/Totals summary values in shared ruled rows;
- operational mono restricted to repeated flight data;
- sparse mint accent.

The concept depends on alignment, spacing and type-role discipline more than on containers.

## Implementation

Initial Flutter implementation:
`8791bb30d7e8ea33d997e2a08608e675e049bb1f`

Light tertiary contrast correction:
`3d47615ff6d3d3d932a7fadb01459a724221d801`

Canonical label restoration:
`218a1a44d591d65daee5e4ef5fcc7be6738b41bd`

Primary source:
`design/prototype/logmate_visual_preview/lib/home_candidate_06_visual.dart`

## Render review

Deterministic 390×844 light/dark renders were generated from the same visual tokens, content and geometry as the Flutter concept.

Before specialist promotion:
1. month chevrons in the review harness were converted from text glyphs to vector icons;
2. light tertiary text was darkened after contrast inspection;
3. `Recent` was restored to `Recent Flights`;
4. Current Period was restored to separate `Block Time`, `This month`, and `This year` labels.

Final render shows no clipping or missing control icon.

## Specialist gate

- Type: **PASS FOR OWNER AESTHETIC REVIEW**
- Color: **PASS FOR OWNER AESTHETIC REVIEW**
- Layout / Spatial: **PASS FOR OWNER AESTHETIC REVIEW**
- Interaction: **PASS FOR OWNER AESTHETIC REVIEW**
- Content: **PASS FOR OWNER AESTHETIC REVIEW**
- Web / Runtime: **PASS FOR OWNER AESTHETIC REVIEW ONLY / RUNTIME PASS PROHIBITED**

No domain has a remaining static-owner-review blocker.

## Runtime boundary

GitHub Actions run `35479321853` again ended before any runner step:
- runner_id = 0;
- steps = [].

Therefore no claim is made for:
- Flutter analyze/test/golden;
- native/PWA/browser equivalence;
- resolved production fonts;
- narrow/enlarged/text-spacing;
- forced colors;
- route/focus runtime;
- physical device;
- representative-pilot usability/preference.

## Coordinator verdict

**OWNER-REVIEW ELIGIBLE.**

This candidate may be shown for visual judgment.

It is not:
- a selected direction;
- a final baseline;
- production-ready;
- a Masterpiece.
