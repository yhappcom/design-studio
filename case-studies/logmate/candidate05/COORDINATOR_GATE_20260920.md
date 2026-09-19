# LogMate Home Candidate 05 — Coordinator Gate — 2026-09-20

Status: **OWNER-REVIEW ELIGIBLE / VISUAL-ONLY CONCEPT / RUNTIME OPEN**

## Scope

Candidate 05 is a visual-design concept on the frozen Home structure.

Frozen:
- Home information architecture;
- order;
- data fixtures;
- action/destination placement;
- product semantics;
- operational comparison geometry.

Sequence preserved:
`Header -> Actions -> Search -> Current Period -> Recent -> Activity -> Totals`

No macro-layout or data-model change is used to create differentiation.

## Isolation

Restore point:
`f992d62a98193629d19346a022a64deef824570c`

Branch:
`design/home-candidate-05-visual-only-20260920`

Excluded during generation:
- sealed Candidate 01;
- rejected Candidate 02;
- rejected Candidate 03;
- rejected Candidate 04;
- Round-1 concepts.

Isolation result: **PASS**.

## Concept

**Ivory Instrument**

Visual-only variables:
- warm ivory canvas;
- one continuous inset work sheet rather than repeated section cards;
- rounded task/search controls;
- soft inset bands for Current Period / Activity / Totals;
- fine cut-lines between canonical sections;
- sentence-case hierarchy;
- bounded operational mono;
- mint selected/focus state;
- matching dark counterpart using the same surface relationships.

## Implementation

Initial Flutter implementation:
`eba943091f52e623025f2f2694151c5454692165`

Viewport-fit refinement:
`c876dda3e927e882139c2457f028cb2afee2783c`

Continuous-sheet refinement:
`dbaab8880194e676b8fbf1c17a61eb4dde4bf282`

Canonical Settings glyph:
`e9fd7793df25735dc39c0a0300fc33f0c1e871bf`

Compile-safety correction:
`bc3dcb47dbd95e7602e36dae053ca5c04d3e0e71`

Primary Flutter source:
`design/prototype/logmate_visual_preview/lib/home_candidate_05_visual.dart`

## Render inspection and corrections

The first deterministic render was inspected before promotion.

Corrections made:
1. repeated small metric boxes were consolidated into shared bands to avoid dashboard/card grammar;
2. light tertiary was darkened from `#777972` to `#70726B` for small-text contrast;
3. month navigation target increased to 44x44;
4. experimental tune/settings icon was rejected and restored to canonical gear;
5. deterministic review icons use vector paths rather than symbol glyphs;
6. invalid Flutter `Container(minHeight: ...)` usage was corrected to `BoxConstraints(minHeight: ...)`.

Final light/dark renders fit the 390x844 review viewport without clipping.

## Specialist-domain review

- Type: **PASS FOR OWNER AESTHETIC REVIEW**
- Color: **PASS FOR OWNER AESTHETIC REVIEW**
- Layout / Spatial: **PASS FOR OWNER AESTHETIC REVIEW**
- Interaction: **PASS FOR OWNER AESTHETIC REVIEW**
- Content: **PASS FOR OWNER AESTHETIC REVIEW**
- Web / Runtime: **PASS FOR OWNER AESTHETIC REVIEW ONLY / RUNTIME PASS PROHIBITED**

No domain has a remaining static-owner-review blocker.

## Runtime boundary

GitHub Actions run `35477358734` terminated before any runner step:
- runner_id = 0;
- steps = [].

No claim is made for:
- Flutter analyze/test/golden;
- native/PWA/browser equivalence;
- enlarged/text-spacing;
- forced-colors;
- physical device;
- representative-pilot usability/preference.

## Coordinator verdict

**OWNER-REVIEW ELIGIBLE.**

This means Candidate 05 may be shown to the owner as a visual comparison candidate.

It does not mean:
- preferred direction;
- final baseline;
- production-ready UI;
- Masterpiece.
