# CD122 — LogMate Candidate 03 Accessible String / Runtime Preflight — 2026-09-20

Status: **TRANSFER VALIDATION PLAN / STAGE 3 NOT PASSED**

## Purpose
Candidate 03's visible English strings passed static owner-review gating. The next Content question is whether visible wording, accessible names, state wording and route meaning remain semantically aligned in the actual Flutter surface.

## SOURCE
Flutter recommends intelligible descriptions for controls under TalkBack/VoiceOver and supports explicit Semantics where standard widget semantics are insufficient. Flutter Web translates its Semantics tree into an accessible HTML structure; this is runtime evidence, not something a static render can prove.

Sources:
- https://docs.flutter.dev/ui/accessibility
- https://docs.flutter.dev/ui/accessibility/web-accessibility
- https://docs.flutter.dev/ui/widgets/accessibility

## PRACTICE — immutable-first fixture
Preserve current canonical visible strings first: Current Period, Search, Recent Flights, Activity, Totals, Add Flight, View Logbook, plus current period/date fixtures. For every interactive element compare:
- visible label;
- accessible name/role/state;
- destination/action meaning;
- current/selected state wording where implemented;
- error/offline/pending/recovery wording only when Interaction authority exists.

Icon-only previous/next controls require an intelligible accessible name even when no visible text is added.

## CRITIQUE / failure conditions
FAIL if accessible names contradict visible wording; Search promises retrieval before SEARCH-001 exists; state copy invents Saved/Synced/offline truth; geometry pressure silently abbreviates canonical terminology; or instructions depend on color/position alone.

## Reproducible validation
Capture visible strings and accessibility payload from the same build/run. Repeat after text scaling, fallback and adaptive reflow. Human comprehension remains a separate evidence class.

## RELATED DOMAIN CHECK
- Type: T085 owns fit/rendering and may not silently shorten semantics.
- Color: C116 cannot be the sole carrier of state meaning.
- Layout/Interaction: I103/L107 own action/state/geometry truth.
- Web: W116 captures browser semantics transfer for Flutter Web.

## HANDOFFS TO OTHER SPECIALISTS
Interaction must supply actual state/action truth before status copy is promoted. Web should diff visible and accessibility payloads in the same provenance packet. Type/Layout should return fit failures before wording changes are considered.

## OPEN
No runtime accessibility payload, linguistic review, screen-reader comprehension or representative-pilot task PASS is claimed.