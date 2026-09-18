# CD098 — Pointer interruption feedback source truth

Status: PRACTICE / RUNTIME + LOCALIZATION OPEN

## Question
What should the content system say when a reorder preview is interrupted by pointer cancellation, layout recomposition, capture loss, or a later valid action?

## CONTENT CONTRACT
User-facing feedback resolves from semantic result, not raw pointer events. Source payload:
`semantic_object_id`, `action`, `candidate_destination`, `transaction_result`, `committed_destination`, `recovery_scope`, `current_focus_object/action`, `persistence_truth`.
Browser-only evidence such as `gotpointercapture`, `lostpointercapture`, hit target, or boundary-event reason remains diagnostic unless it changes what the user can do or must recover from.

Protected distinctions:
- captured ≠ moved;
- candidate shown ≠ destination committed;
- interrupted/cancelled ≠ failed;
- layout changed ≠ user moved pointer;
- lost capture ≠ mutation failed;
- boundary no-op ≠ cancellation ≠ failure;
- committed locally ≠ Saved/Synced.

No success/recovery announcement is generated for a preview that never committed. If cancellation returns cleanly to the pre-action state and no user decision is required, silence may be preferable to announcing implementation mechanics; actual AT/human validation remains required before making a universal claim.

## COMPLETE-SYSTEM TRANSFER
Carry the payload through forms/state/recovery/onboarding/retrieval/tone/localization. English/Korean strings must derive from the same semantic result. At 200%, visible copy may be concise while accessibility payload can be richer, but neither may fabricate transaction or persistence truth.

## RELATED DOMAIN CHECK
Type T060/T061: string fit is downstream and cannot justify semantic shortening. Color C091/C092: visual interruption cues must match this result truth. I079 owns lifecycle/capture semantics. L083 owns geometry. W092 supplies served event evidence but does not author user-facing state.

## HANDOFFS TO OTHER SPECIALISTS
Interaction must expose a resolved result independent of raw browser capture events. Web should provide event provenance for debugging while exposing semantic payload to content. Type/Layout must test necessary EN/KO strings rather than shorten them solely for fit.

## OPEN
Actual EN/KO runtime, linguistic review, screen-reader comprehension and representative-pilot task evidence remain OPEN.