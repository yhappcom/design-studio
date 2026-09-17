# C058 — Runtime semantic-state oracle

Status: PRACTICE / TRANSFER VALIDATION PREPARATION

## PURPOSE
Convert C057 from a scenario list into an unambiguous runtime oracle so a rendered result can be classified without treating color presence as success.

## RELATED DOMAIN CHECK
T027 supplies text/render failure ownership; L048/I044 protect adjacency/action/recovery; W057 owns runtime identity; CD063 supplies explicit state language.

## ORACLE
For each financial state, test four independent dimensions: brand emphasis, outcome polarity, certainty/finality, availability/integrity.

A state passes only when:
- its required distinction is present in normal rendering;
- the same distinction remains available without hue/chroma (grayscale/color-loss condition);
- state meaning is not carried by brand mint alone;
- positive/negative outcome does not imply estimated/final or available/unavailable;
- text/icon/structure provides a redundant carrier where state meaning is consequential;
- foreground/background pairs used for required text/non-text information meet applicable WCAG 2.2 criteria in the rendered context.

Required contradiction cases include high distribution + negative total performance, zero, estimated vs final ROC, partial vs unavailable, and positive/negative tax adjustment.

## FAILURE CLASSES
COLOR_ONLY, AXIS_COLLISION, BRAND_AS_SUCCESS, POLARITY_AS_CERTAINTY, AVAILABILITY_AS_ZERO, CONTRAST, FORCED/HIGH_CONTRAST_LOSS, ADJACENCY_BREAK.

## EVIDENCE BOUNDARY
This is an executable oracle, not execution. It does not establish calibrated-display, cross-browser/device, CVD-observer or human-recognition PASS.

## HANDOFFS TO OTHER SPECIALISTS
W057 should store the oracle outcome beside each screenshot; CD063 supplies the non-color semantic carrier; L048 protects adjacency; T027 ensures the carrier survives rendering.