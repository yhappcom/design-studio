# T021 — Repair Implementation Handoff

Evidence purpose: **PRACTICE / EXECUTION HANDOFF**. This closes the gap between the accepted repair decision and the next executable source change without pretending that a repair has been rendered.

## RELATED DOMAIN CHECK
- **Color:** C041 cannot compensate for glyph ambiguity and must not be used as a discrimination crutch.
- **Layout/Interaction:** I028/L032 need stable identifiers but must continue mature fallback while metrics are provisional.
- **Web:** W041 should not embed this candidate until drawing and general-spacing gates pass.
- **Content:** CD047 preserves exact operational identifiers and therefore supplies unchanged stress strings.
- **UX:** human recognition/error-rate evidence remains OPEN.

## Source locus verified
The current normalized executable source is `T021-normalized-architecture-harness.py`. Its present constructions make the repair locations explicit: `upper('I')`, `lower('l')`, `digit('1')`, and candidate-B `digit('0')` slash geometry. This means the next Type step is not blocked by source discovery.

## Bounded source-change contract
Kerning remains OFF and sidebearings are frozen during the first repair iteration. Only silhouette-producing geometry may change.

1. `I`: preserve bilateral capital terminals and increase their survival margin at 14–17 px without changing sidebearings.
2. `l`: replace the current base-only distinction with a structurally different lowercase silhouette; the distinction must survive without color or contextual guessing.
3. `1`: retain numeral top-entry/base identity while preventing convergence with `l`.
4. B `0`: retain slash semantics while reducing slash dominance by changing slash geometry only; O outline and figure sidebearings stay fixed for this iteration.

## Acceptance matrix
The rerender must include `Il1 I1l lI1 111 lll III`, `O0 00 OO 00:45 B737-900`, and the bounded operational corpus at 14/17/24 px. Record source SHA, build hash, raster hash, size, defect class and before/after verdict. A repair is rejected if a synthetic ambiguity row improves while airport/identifier/numeric strings degrade materially.

## Gate discipline
This handoff does **not** authorize general spacing or kerning. After repaired raster critique, only drawing defects may be repaired. General spacing opens only when drawing is defensible; T022 kerning opens only after general spacing.

## OPEN
This connector run can inspect and write repository text but cannot execute the Python/font raster toolchain or safely replace the full harness from a partial source fetch. Therefore no source mutation, rerender or drawing PASS is claimed.

## HANDOFFS TO OTHER SPECIALISTS
Web/Content/Layout should keep exact operational strings and mature fallback. Color must treat character identity as an independent channel. The next executable environment should modify only the four bounded constructions above, rerender, and return hashes/artifacts for direct critique.