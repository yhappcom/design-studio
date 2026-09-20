# T088 — Candidate 05/07 Type Invariant Contradiction Review

Date: 2026-09-20
State: **CONTRADICTION REVIEW / TRANSFER VALIDATION — PRACTICE, NOT PASS**

## PURPOSE
Separate reusable Type-system invariants from concept-specific styling by comparing materially different LogMate Home Candidate 05 (`Ivory Instrument`) and Candidate 07 (`Linebook`). This review does not select a visual winner and does not bypass T021.

## RELATED DOMAIN CHECK
- **Type:** T021 remains upstream: bounded drawing before general spacing; residual kerning last. T086/T087 define candidate-specific transfer constraints.
- **Color:** C117/C118 show palette atmosphere can change while semantic-state rank remains stable.
- **Layout/Interaction:** I104/L108 and I105/L109 protect semantic relationships rather than screenshot coordinates.
- **Web:** W117/W118 leave resolved-font/TextScaler/runtime evidence OPEN.
- **Content:** CD123/CD124 keep canonical terminology immutable-first across concepts.

## CONTRADICTION REVIEW
Candidate 05 and Candidate 07 differ in atmosphere, density and typographic composition. Treating either candidate's exact font size, weight, line spacing, mono proportion or alignment as a studio-wide rule would therefore overfit one concept.

The comparison supports these **candidate-independent invariants**:
1. semantic product labels remain mature proportional UI unless a representation/comparison requirement justifies another treatment;
2. operational identifiers/numerics may use mono/tabular treatment only for an explicit representation or repeated-comparison need;
3. actual resolved family/fallback and actual platform text scaling are evidence inputs, not implementation trivia;
4. text growth may change geometry; geometry does not authorize semantic shortening;
5. fit pressure does not authorize negative tracking, glyph narrowing, scaling suppression or premature kerning;
6. state meaning must not depend on weight/type treatment alone.

The following remain **concept variables**, not invariants: exact size/weight ladder, editorial vs instrument-like density, capitalization treatment where semantics permit, exact line-height, precise mono/proportional balance and alignment style.

## PRACTICE / CRITIQUE
A false design-system conclusion would be to normalize Candidate 05 and Candidate 07 into one typography recipe. That would erase useful concept diversity and confuse style consistency with semantic/system consistency.

A second false conclusion would be to use Candidate 07's denser ledger as evidence that narrower glyphs or tighter tracking are required. Until T021 drawing and general spacing pass, such changes would be downstream compensation for an immature source.

## REPRODUCIBLE VALIDATION
When both exact runtimes exist, use the same semantic corpus and capture for each candidate at baseline and maximum supported text scaling plus forced mature fallback: source commit, platform, requested/resolved family where observable, line breaks, clipping, row growth, semantic order and any fit intervention. Repeat each build twice. Compare whether the six invariants above survive while concept variables remain materially different.

## RESULT
The cross-candidate evidence narrows the Type system: **role/representation/scaling/fallback/fit rules are reusable; exact visual metrics are not.** No Type gate changes.

## OPEN
T021 drawing PASS; general spacing; residual kerning; exact runtime comparison; AT/human reading evidence; production custom-font decision.

## HANDOFFS TO OTHER SPECIALISTS
Layout/Web may allow different recomposition strategies per candidate while preserving text ownership and semantic order. Content should resist abbreviation solely for fit. Color/Interaction should preserve non-type state cues. Cross-domain comparison should not force the two concepts toward the same visual typography.