# C092 — Pointer capture/interruption semantic-state separation

Status: PRACTICE / RENDERED TRANSFER OPEN

## Question
Can visual state survive pointer capture, layout-under-pointer changes and stream interruption without implying a committed reorder or confusing focus/selection?

## SYNTHESIS
Extend C091 with an orthogonal `stream ownership/interruption` axis. Keep independent: keyboard focus, selection, pressed/preview, candidate destination, captured/active pointer stream, cancelled/interrupted, committed, boundary no-op, recovery eligibility, failure/supersession and hidden/disabled.

Capture is primarily event-routing provenance and normally should not require a unique user-facing color. If a visible drag-active cue is useful, it must represent the semantic operation, not DOM capture mechanics. Interruption clears preview/candidate cues unless the actual Interaction contract retains a valid operation.

## PRACTICE / CRITIQUE
Test light/night, 200%, then forced-colors and independent engine when W092 is executable. FAIL if layout-driven boundary events make a new destination look selected/committed, interrupted preview retains success/recovery styling, focus and drag-active collapse into one indistinguishable accent, or forced-colors removes the non-color distinction between active candidate and committed result.

## RELATED DOMAIN CHECK
Type T060/T061 supplies rendering stress only. I079 owns stream/capture semantics. L083 owns recomposition geometry. W092 owns browser provenance. CD097/CD098 verbalizes only resolved state.

## HANDOFFS TO OTHER SPECIALISTS
Web should expose actual event/capture state only as evidence; Content should not name capture mechanics unless user action/recovery changes; Layout should clear ghost candidate visuals after recomposition/cancel.

## OPEN
Rendered forced-colors, independent-engine/device, calibrated-display, observer and representative-human evidence remain OPEN.