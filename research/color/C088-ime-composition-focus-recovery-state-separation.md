# C088 — IME composition, focus and recovery-state separation

## Purpose
Transfer I075/L079 into Color systems practice without letting color define command ownership.

## RELATED DOMAIN CHECK
Checked T021/T056, C087, I074/I075, L078/L079, W087 and CD093. This is `TRANSFER VALIDATION` of existing semantic-state rules into provisional IME text.

## SYNTHESIS
At minimum the rendered system may simultaneously contain: active keyboard focus, provisional composing text, text selection/caret, eligible configuration recovery, configuration restoration feedback, validation state and disabled/superseded recovery. These are independent semantic axes. A single accent treatment cannot safely stand for all of them.

## PRACTICE
Build a state matrix for light/night/forced-colors once executable:
- focused editor + active composition + configuration recovery eligible;
- focused editor + composition committed + text Undo eligible;
- recovery control focused while editor text history remains;
- recovery superseded while editor remains focused;
- validation error during/after composition.

For each, trace `semantic state → token → paint owner → rendered surface → non-color cue → accessible meaning`.

## CRITIQUE / FAIL
FAIL if composition underline/highlight is visually indistinguishable from validation error or selection; configuration recovery appears to own editor Undo solely through shared accent; stale recovery retains actionable paint; forced colors removes the only distinction between focused owner and recovery availability.

## VALIDATION
Use I075 scenario IDs and L079 geometry. Capture normal/light/night and forced-colors where supported, then repeat in an independent engine. Do not claim observer/calibrated-display/human comprehension evidence from screenshots.

## OPEN
No rendered C088 evidence yet; forced-colors, independent engine, physical device, calibrated display and human recognition remain OPEN.

## HANDOFFS TO OTHER SPECIALISTS
Content must verbalize state without color references; Web must expose actual forced-colors/browser evidence; Layout must preserve cue ownership under reflow; Type must not treat composition styling as a glyph-spacing problem.