# T026 — Accessibility Runtime Acceptance Matrix

Status: PRACTICE / TRANSFER VALIDATION SPEC

## PURPOSE
Convert T025 from a general scaling contract into executable acceptance criteria shared with W056. This does not advance T021 drawing/spacing/kerning gates.

## SOURCE
- Flutter Android 14 nonlinear text scaling: scaling is nonlinear up to 200%; do not model it as one global multiplier.
- Flutter accessibility guidance: large scale factors must remain legible/usable; automated guideline tests cover target labels, contrast and platform target sizes.
- WCAG 2.2 remains the web accessibility baseline; reflow/text-spacing evidence is applicable to web surfaces.

## PRACTICE MATRIX
For each W056 build/scenario identity capture default scale and maximum supported accessibility scale for: KRW/USD, signed positive/negative/zero, large values, long localized labels, estimated/final ROC, partial/unavailable.

Accept only when: truth-bearing qualifiers remain present; no ellipsis changes financial meaning; numeral sign/currency/unit remain associated; fallback does not create missing glyphs; hierarchy survives wrapping; geometry pressure is handed to Layout rather than solved by shrinking/deleting content.

## CRITIQUE
A screenshot that merely fits is insufficient. A compact card can visually pass while separating a qualifier from its value or making polarity ambiguous. Raster evidence therefore needs semantic/content pairing from CD062 and group geometry from L047.

## RELATED DOMAIN CHECK
- Type: T021 drawing gate remains prior to spacing/kerning closure.
- Color: C056 polarity/certainty cannot rely on hue when strings wrap.
- Layout/Interaction: L047/I043 own recomposition, target and focus continuity.
- Web: W056 owns runtime identity/artifacts.
- Content: CD062 supplies immutable truth-bearing strings.

## HANDOFFS TO OTHER SPECIALISTS
W056 should record text-scale state and raw screenshot/semantics artifacts. L047 should treat any lost label-value-qualifier association as failure. CD062 should log any proposed shortening that changes semantic dimensions.

## OPEN
No Flutter/browser/native runtime artifact, AT, physical-device or human task evidence is produced by this note.