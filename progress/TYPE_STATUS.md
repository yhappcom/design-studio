# Typography / Type Design Specialist Status

Operating state: **ACTIVE — STAGE 2 PRACTICE / T021 DRAWING GATE OPEN + T036 REPAIR REGRESSION GATE**
Governance sync: 2026-09-18
Primary path: `research/type/`

## Current level
Stage 1 **PASS**; Stage 2 **PRACTICE / NOT PASSED**.

## Latest evidence
MintTap run `35255971379` passed analysis and executed the widget matrix. Compact baseline overflowed 9.3 px horizontally; 2.0-scale stress overflowed 47 px. T035 classifies both as composition pressure, not kerning/drawing evidence. T036 now defines the post-Layout-repair Type regression gate while preserving T021 drawing→spacing→residual kerning order.

## Active queue
1. Continue T021 bounded R1 drawing repair; no spacing/kerning compensation for unfinished drawing.
2. After L058 repair, execute T036 against the same compact identities: font/fallback, line breaks, clipping, vertical metrics, numerals/punctuation and raster where available.
3. Keep production compact-iOS 1.10 clamp versus unclamped diagnostic differences as composition/accessibility evidence unless a genuine glyph/metric defect is demonstrated.
4. Keep browser/native breadth, AT and human recognition/task evidence OPEN.

## Evidence boundary
No T021 closure, kerning entry, post-repair runtime Type PASS, cross-browser/native, AT or human PASS is claimed.
