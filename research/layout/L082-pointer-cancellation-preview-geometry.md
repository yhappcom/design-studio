# L082 — Pointer cancellation preview and commit geometry

Status: PRACTICE / TRANSFER VALIDATION OPEN

## Question
Once I078 defines the semantic commit boundary, does the interface make press/preview, abort, valid drop and committed position spatially legible without target ambiguity, clipping, obscuration or excessive displacement?

## Geometry protocol
Capture viewport, text scale, pointer type, semantic object/action ID, source rectangle, current pointer point, candidate-destination rectangle, activation target rectangle, preview rectangle, committed rectangle, scroll before/after, sticky/safe-area intersections and final focus locus.

Run baseline and 200% for: down-inside→up-outside cancellation, drag→origin cancellation, valid drop, boundary no-op, adjacent/multi-position moves and system groups. Repeat each scenario twice.

## Accessibility floor and stronger critique
WCAG 2.2 SC 2.5.2 is the cancellation floor; SC 2.5.8 remains the AA target-size floor for the non-drag controls. Geometry must not turn an otherwise valid abort path into an impractical one. A preview that visually crosses rows is not a committed order change.

Studio critique is stronger than conformance: cancellation should not cause unexplained scroll jumps, hide the surviving focus owner behind sticky UI, or leave a ghost preview that appears committed. At 200%, an abort area or origin return path must remain reachable and comprehensible if the implementation relies on it.

## Dependency
I078 owns mutation/commit truth. C091 owns state rendering, CD097 owns wording, and W091 must prove actual browser/runtime event order. L082 cannot declare semantic PASS from clean animation alone.