# T089 — Cross-Concept Stress Fixture: Type Contract

## PURPOSE
Convert T088 invariants into an executable stress fixture for Candidate 05/07 without bypassing T021.

## RELATED DOMAIN CHECK
- Type: T021 drawing gate; T088 invariant review.
- Color: C119 semantic-rank invariants.
- Layout/Interaction: I106/L110 authority and protected relationships.
- Web: W119 shared production provenance.
- Content: CD125 semantic invariance.
- Reuse: same strings, same semantic roles and same stress conditions across both candidates; visual recipes remain independent.

## PRACTICE / CRITIQUE
The shared fixture SHALL include baseline, maximum supported platform text scaling, mature fallback, narrow width and long-but-semantically-valid operational strings. Capture actual resolved family, size, weight, line metrics, wrapping/clipping and role ownership. Candidate-specific size/weight/density may differ.

Failure conditions:
1. text scaling is suppressed to preserve the mockup;
2. negative tracking, glyph narrowing or semantic shortening is introduced as geometry repair;
3. a mono role is expanded merely to make the candidates look alike;
4. fallback changes information ownership or makes operational strings ambiguous;
5. T021 drawing defects are compensated with spacing/kerning.

## EVIDENCE BOUNDARY
This is an implementation-ready fixture, not runtime evidence. T021 remains upstream: drawing -> general spacing -> residual kerning. No spacing/kerning gate advancement is claimed.

## HANDOFFS TO OTHER SPECIALISTS
Layout should record recomposition caused by the exact corpus; Content should reject wording changes made only for fit; Web should capture resolved-font provenance; Color should repeat state tests after reflow because cue adjacency can change.
