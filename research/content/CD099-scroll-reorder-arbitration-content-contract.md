# CD099 — Scroll/reorder arbitration content contract

Status: STAGE 3 PRACTICE / COMPLETE-SYSTEM TRANSFER SPEC
Date: 2026-09-19

## Source truth
User-facing copy is derived from semantic result, not raw pointer/capture/gesture-arena events.

Protected invariants:
- touch/press started != move started
- scrolled != reordered
- previewed destination != committed destination
- arena loss / pointercancel != failure
- boundary no-op != cancellation != failure
- committed reorder != Saved/Synced
- non-drag alternative and drag share the same object/result vocabulary

## Complete-system integration
Forms/state: transient gesture states do not create validation/success copy.
Onboarding/discoverability: drag may be taught as optional direct manipulation only when the non-drag single-pointer path remains discoverable; human discoverability evidence is OPEN.
Retrieval/history: only committed semantic transactions enter movement/recovery history.
Tone: avoid implementation language such as capture, gesture arena or pointercancel unless exposed for diagnostics.
Localization: EN/KO strings must preserve object identity, destination/result and recovery scope; do not freeze literal Korean until runtime + linguistic review.
Accessibility: visible and programmatic status must agree; do not force focus merely to announce a clean cancellation.

## Scenario copy oracle
Scroll-only: no reorder-success message.
Cancelled/arena-loss: normally silent if state returns cleanly; this is a product hypothesis pending human/AT evidence.
Committed move: report object + resolved position/destination from semantic IDs.
Boundary no-op: report only if needed to explain why an invoked action had no effect; do not call it an error.
Undo: report restored configuration truth separately from focus and persistence truth.

## Evidence boundary
No EN/KO linguistic PASS, AT comprehension, discoverability or representative-pilot usability PASS is claimed.