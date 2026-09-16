# C044 — Causal Order vs Clock Recency Visual Contract

## PURPOSE

Extend C043 from multi-clock provenance to causal-order truth. A visually newer wall-clock timestamp must not outrank an authoritative revision, sequence, or dependency relation.

## SYNTHESIS

Professional interfaces can contain valid timestamps that disagree with causal order because of clock skew, offline capture, delayed upload, timezone conversion, or later reconciliation. Color hierarchy must encode semantic state and consequence, not infer truth from the largest/latest-looking time.

Visual precedence: current authoritative consequence → action safety/intervention → causal/order evidence → time-role metadata → history → focus/selection/brand emphasis.

## ADVERSARIAL MATRIX

Test: client clock ahead; offline event uploaded later; DST/zone display change; reconciliation time later than event time; event time unknown but authority revision known; two events with equal formatted time but distinct sequence. Repeat under light/dark, grayscale, hue removal, background removal, forced-colors, print, and focus/selection.

FAIL if recency styling makes a causally older event appear authoritative/current, or if focus/selection is mistaken for causal priority.

## RELATED DOMAIN CHECK

Type: T021 provisional glyphs cannot carry causal distinction alone. Layout/Interaction: I031/L035 must own ordering and chronology structure. Web: W044 must capture raw instant plus ordering basis. Content: CD050 must name sequence/authority semantics without saying “latest” when only display time is latest.

## HANDOFFS TO OTHER SPECIALISTS

C044 supplies the visual acceptance oracle for W044; I031/L035 and CD050 remain canonical for behavior/semantics.

## EVIDENCE BOUNDARY

Deterministic visual contract only. No executed W044 artifact, observer salience, CVD/low-vision, physical print/display, or human task PASS.