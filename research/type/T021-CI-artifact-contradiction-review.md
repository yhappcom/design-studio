# T021 — CI artifact contradiction review

Date: 2026-09-16
Purpose: **CONTRADICTION REVIEW / EXECUTED-EVIDENCE RECLASSIFICATION**

## RELATED DOMAIN CHECK
Type remains authoritative for drawing/spacing/kerning. Color cannot repair glyph ambiguity; Layout/Web must not freeze production metrics from an unaccepted candidate; Content supplies operational strings; Interaction owns action truth. This review changes only Type evidence classification.

## Contradiction found
The current status says T021 is blocked on establishing an executable editable source package and repeats an older 6/33 coverage figure. Latest-main repository evidence is stronger and materially newer than that description:

- `T021-family-architecture-reset-complete-harness.py` is executable procedural glyph source, not a raster-only specimen. It constructs all ten digits directly with FontTools pens, keeps kerning OFF, builds fonts, renders 14/17/24 px specimens and emits structured results.
- GitHub Actions already contains reproducible T021 proof workflows with pinned Python major/minor and declared `fonttools`/`pillow` dependencies.
- Executed Actions run `35048673549` (`Type T021 Normalized Proof`) completed successfully on commit `21f9bc8470403716cbf2b45ab3f8338db18c3323`.
- Artifact `t021-normalized-proof`, digest `sha256:4b381da129b470879e7b3339847dfaa88a16dd4c8791f6d2a957927e80e539ab`, was downloaded and inspected during this review.

## Executed artifact result
`T021-normalized-architecture-results.json` reports:
- kerning: false;
- required unique non-space corpus: 36;
- Architecture A coverage: 36, missing: [];
- Architecture B coverage: 36, missing: [];
- specimens at 14/17/24 px for both A and B;
- next gate: semantic sensitivity audit then drawing critique.

The same artifact includes `T021-normalized-semantic-sensitivity-results.json`. Eleven architecture tokens (`stem`, `round_stem`, `cap_overshoot`, `x_overshoot`, `aperture`, `diag_comp`, `terminal_policy`, `bowl_join`, `shoulder_tension`, `figure_width_mode`, `zero_treatment`) all pass their declared mandatory/protected perturbation gates. The result explicitly sets `drawing_claim:false` and `human_claim:false`.

## Correct classification
**The executable-source and bounded-coverage blockers are closed for the normalized procedural A/B candidate lineage.** The older 6/33 figure must not be used as the current blocker for that lineage.

This does **not** close T021. The new blocker is the next gate already named by the executed artifact: **drawing critique of the normalized A/B candidates with kerning OFF**, followed by general spacing critique. Semantic sensitivity proves token wiring, not drawing quality. Generated procedural source is valid editable source for this research lineage, but it is not automatically a production font recommendation.

## Gate discipline
1. Drawing critique first: construction consistency, counters/apertures, joins, terminal logic, ambiguity controls, apparent weight and raster behavior at 14/17/24 px.
2. General spacing second with kerning OFF.
3. Only after drawing/general spacing defects are repaired may pair-specific residuals be enumerated for T022.
4. Human pilot recognition/task performance remains OPEN.

## HANDOFFS
Web/Layout may use the artifact only as a bounded research candidate, not frozen production metrics. Content strings remain unchanged for stress testing. Color treats ambiguity as Type failure. UX integration should test candidate transfer only after Type drawing critique reaches a defensible result.
