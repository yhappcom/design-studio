# C071 — MintTap State Visibility Independence Matrix

Date: 2026-09-18
Purpose: **TRANSFER VALIDATION / CONTRADICTION REVIEW**
Stage: Stage 3 PRACTICE.

## QUESTION
After Material/layer repair, can MintTap preserve independent financial, certainty, availability and interaction meanings on the actual visible surface rather than merely in token declarations?

## SOURCE
WCAG 2.2 is the studio baseline. Relevant requirements include Use of Color, Non-text Contrast, Focus Visible/Not Obscured and Target Size. W3C's WCAG 2.2 update explicitly adds Focus Not Obscured (Minimum) and Target Size (Minimum).

- https://www.w3.org/WAI/standards-guidelines/wcag/
- https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/

Flutter accessibility testing exposes guideline checks for contrast and tappable targets, but those checks are partial evidence and do not prove semantic comprehension.

- https://docs.flutter.dev/ui/accessibility/accessibility-testing

## PRACTICE — orthogonal state matrix
Validate each axis separately and in contradiction pairs:

| Axis | Required distinction | Stress combination |
| --- | --- | --- |
| financial polarity | positive / zero / negative | positive income + negative total return |
| certainty | estimated / final | final negative + estimated positive nearby |
| availability | complete / partial / unavailable | unavailable must not resemble numeric zero |
| accounting basis | gross / net | both visible without color-only distinction |
| interaction | idle / focus / pressed / selected / disabled | selected + negative; focus + unavailable |
| recovery | pending / known failure / ambiguous | color must not collapse behavioral truth |

For every cell record: semantic token, actual paint owner, visible surface, foreground/background pair, non-color cue, accessible name/state, and screenshot/raster evidence.

## CRITIQUE
A token can be numerically correct while its visual state is hidden by an intervening painted layer. Therefore `TOKEN_PASS / RENDER_FAIL` is a product failure. Conversely, a visible color difference without text/icon/state redundancy is insufficient where meaning must survive forced colors or nonvisual access.

## REPRODUCIBLE VALIDATION
Promotion requires all of:
1. state reaches visible surface;
2. applicable contrast requirement passes;
3. interaction state does not overwrite financial/certainty/availability meaning;
4. meaning survives removal/transformation of color through another cue;
5. focus remains visible and not entirely obscured in the web transfer;
6. same scenario identity is shared with Layout/Interaction/Web/Content.

## RELATED DOMAIN CHECK
- Type: signed values, punctuation and fallback must remain legible; no Type compression for Color fit.
- Color: extends C070 from contract to finite execution ledger.
- Layout/Interaction: owns state truth and paint/feedback behavior.
- Web: validates forced-colors/browser/runtime transfer.
- Content: supplies non-color wording and semantic distinctions.
- UX: no human comprehension claim from contrast/token checks.

## HANDOFFS TO OTHER SPECIALISTS
Interaction must expose distinct states; Content must verbalize them; Web must test actual browser focus/forced-color behavior. Layout must not hide focus/state surfaces behind decorative layers.

## EVIDENCE BOUNDARY
No repaired runtime Color PASS, calibrated-display/observer evidence, cross-browser/device PASS or representative-human comprehension PASS is claimed.
