# C033 — Semantic-state cue degradation ladder

Evidence: **SYSTEMS PRACTICE / TRANSFER VALIDATION / OPEN**

## RELATED DOMAIN CHECK
Type T021 can affect textual cue legibility; Layout L023 controls grouping/association; Interaction I019 owns state truth; Web W032 supplies runtime modes; Content CD038 supplies semantic IDs and invariant wording.

## Purpose
C032 established cue independence. C033 tests graceful degradation: remove or transform one visual channel at a time and verify the state still has a non-color semantic path.

## Ladder
For each certainty/recovery state record: normal light → normal dark → authored color removed → icon/shape removed → forced-colors substitution → focus-only navigation → text-only semantic inspection. Each step records which independent cues remain and whether the authoritative state/action is still available without hue.

A pass at one rung cannot infer a pass at another. Contrast, state differentiation, focus visibility, focus obscuration and semantic availability remain separate verdicts. WCAG 2.2 is the baseline; 2.4.11 AA focus-obscuration evidence remains geometry-dependent rather than a palette score.

## Failure policy
If removal of authored hue also removes the only state distinction, classify semantic-cue failure. If text survives but is hidden/occluded, hand to Layout/Web. If text itself is ambiguous, hand to Content. If glyph recognition is ambiguous, hand to Type.

## Execution boundary
The ladder is ready for W032 browser captures. Forced-colors and actual focus/overlay behavior require executed browser evidence; no simulated PASS is claimed.

## HANDOFFS TO OTHER SPECIALISTS
Web records each rung with engine/mode provenance; Layout supplies focus/overlay rectangles; Content verifies semantic IDs survive; Type supplies valid rendered text only after T021; Interaction supplies authoritative state/action truth.
