# T086 — Candidate 05 runtime Type transfer

Status: **PRACTICE / TRANSFER VALIDATION / RUNTIME OPEN**

## Question
Can Candidate 05 `Ivory Instrument` preserve its bounded operational typography when Flutter applies real platform text scaling, fallback and adaptive layout, without using unfinished custom metrics or spacing/kerning as compensation?

## RELATED DOMAIN CHECK
- Type: T021 drawing gate and T085 Flutter scaling transfer checked. T021 remains upstream: drawing → general spacing → residual kerning.
- Color: C116 requires state boundaries to survive scaling/reflow.
- Layout/Interaction: I103/L107 protect semantic relationships rather than 390×844 coordinates.
- Web: W116 requires exact-build native/Web provenance.
- Content: CD122 requires visible/accessibility-string parity without geometry-driven abbreviation.
- Candidate evidence: Candidate 05 is owner-review eligible only; production type, fallback, enlarged text and runtime remain OPEN.

## SOURCE
Flutter's current platform scaling model is `TextScaler`; Android 14 nonlinear scaling can reach 200%, and Flutter recommends testing the UI at maximum font size. A scalar `fontSize × factor` assumption is therefore not a valid general runtime model. Flutter accessibility guideline tests can separately check target labels, target sizes and text contrast; they do not prove typographic usability.

## PRACTICE contract
Use Candidate 05's existing role split as the immutable-first fixture:
- product-authored UI: proportional;
- Date / Flight / Route / Block repeated operational rows: bounded mono candidate;
- Current Period / Activity / Totals values: proportional tabular figures;
- section titles: sentence case.

For the exact coded build capture at baseline and maximum supported platform scaling:
1. requested and resolved font family per role;
2. fallback occurrence;
3. actual scaled text size via platform `TextScaler` behavior;
4. line count, clipping, ellipsis and overflow;
5. operational-column geometry and comparison alignment;
6. visible strings unchanged from Content authority.

Repeat with production-like fallback forced. Candidate 05 passes this transfer only if the role distinction survives without changing semantic strings or using negative tracking, glyph narrowing, artificial scale clamping, or provisional custom-font metrics to rescue the 390×844 composition.

## CRITIQUE / failure conditions
- FAIL if layout is frozen around provisional T021 metrics.
- FAIL if unfinished drawing is compensated by spacing/kerning.
- FAIL if `Current Period`/Activity/Totals are switched to mono merely to stabilize geometry.
- FAIL if strings are shortened to preserve the screenshot.
- FAIL if maximum scaling is declared passed from a synthetic linear multiplier when the target platform uses nonlinear scaling.

## Gate consequence
No T021, spacing, kerning, production-font, Candidate 05 runtime or human-recognition PASS is created here. Candidate 05 can use mature fallback while T021 remains open.

## HANDOFFS TO OTHER SPECIALISTS
Layout/Web should record actual resolved family and text geometry in the same runtime packet. Content owns any wording change after recomposition is exhausted. Color must recheck state salience after text-induced reflow.