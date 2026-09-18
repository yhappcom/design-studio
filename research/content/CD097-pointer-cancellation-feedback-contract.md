# CD097 — Pointer cancellation and commit feedback contract

Status: PRACTICE / RUNTIME + LOCALIZATION OPEN

## Question
Can visible and accessibility content distinguish preview, cancellation, no-op, committed movement and recovery without narrating pointer mechanics as product truth?

## Source-of-truth payload
Content may be generated only after resolution from: `semantic_object_id/name`, `action`, `candidate_destination`, `result`, `committed_destination`, `tx_id`, `recovery_scope/eligibility`, `current_focus_owner`, and `persistence_truth`.

Protected invariants:
- `pressed/preview ≠ moved`;
- `cancelled ≠ failed`;
- `boundary no-op ≠ cancelled ≠ failed`;
- `destination previewed ≠ destination committed`;
- `move committed ≠ Saved/Synced`;
- `moved object ≠ focused object`.

## Complete-system integration
Forms/state: do not emit success on pointer-down or preview. Onboarding/help: describe the stable action and available alternative, not fragile drag choreography. Retrieval/history: only committed transactions enter movement history. Tone: cancellation is neutral unless the user needs actionable explanation. Localization: EN/KO strings must preserve result distinctions and object identity; do not freeze literal Korean wording before runtime and linguistic review.

Visible feedback can remain concise while accessibility status may include object + resulting position when needed. Neither may fabricate a committed move after I078 reports cancellation.

## Closure protocol
For I078 scenarios capture visible copy, accessibility payload, transaction result, focus owner, and recovery eligibility at preview/cancel/commit. Re-run at baseline/200%, EN/KO, primary/independent engine when implementation exists.

## Evidence boundary
No multilingual runtime, linguistic-review, AT-comprehension or representative-human PASS is claimed.