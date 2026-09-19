# I103 — LogMate Candidate 03 Runtime Preflight — 2026-09-20

Status: **TRANSFER VALIDATION PLAN / HUMAN EVIDENCE OPEN**

## Purpose
Candidate 03 now has real control affordances in the static concept, but static review does not establish runtime authority. Convert those controls into an executable interaction preflight.

## SOURCE
Flutter recommends that active interactions perform real actions, that screen-reader behavior be inspected with TalkBack and VoiceOver, that important actions support recovery where appropriate, and that user context not change unexpectedly during input.

Sources:
- https://docs.flutter.dev/ui/accessibility
- https://docs.flutter.dev/ui/accessibility/accessibility-testing

## PRACTICE
Verify independently:
- month previous/next changes only the implemented period projection;
- Search remains a shell until SEARCH-001 behavior exists;
- Recent row preserves record identity through record route and Back;
- Activity period selection remains distinct from focus and pressed state;
- Add Flight performs only its implemented route transition;
- View Logbook preserves route and Back/Forward restoration.

For each action capture accessible role/name/state, focus before/after, route/history state, scroll restoration, selected/current state and async authority where present.

## CRITIQUE / failure conditions
FAIL if a no-op control appears complete; Search implies retrieval that does not exist; focus is lost or jumps without task rationale; Back restores a semantically different Home state; or selected/current/focus collapse into one state.

## Reproducible validation
Run the same action/route fixture twice in the real runtime, then transfer to an independent platform/engine where applicable. Keep structural accessibility evidence separate from human screen-reader comprehension.

## RELATED DOMAIN CHECK
- Type: T085 scaling may change geometry, not action identity.
- Color: C116 owns visual salience, not state authority.
- Layout: L107 protects focus/target/relationship geometry.
- Web: W116 owns Flutter Web/browser runtime provenance.
- Content: CD122 owns visible/accessibility wording but cannot invent behavior.

## HANDOFFS TO OTHER SPECIALISTS
Web should capture accessibility structure and history in one provenance packet. Content should compare visible labels with accessible names. Color/Layout should validate focus/current separation after scaling.

## OPEN
No Search implementation, route runtime, screen-reader comprehension, representative-pilot discoverability or workload PASS is claimed.