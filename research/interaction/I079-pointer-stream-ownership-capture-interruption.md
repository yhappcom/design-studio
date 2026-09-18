# I079 — Pointer-stream ownership under capture, interruption, and layout mutation

Status: PRACTICE / TRANSFER VALIDATION OPEN

## Question
I078 separates preview/cancel/commit. The next failure class is ownership: when a drag leaves its original hit target, the layout moves under a stationary pointer, the UA suppresses the stream, or capture is released, which semantic reorder operation still owns the pointer and may commit?

## SOURCE
- W3C Pointer Events Level 3 became a W3C Recommendation on 30 June 2026; the current Level 4 Working Draft (26 August 2026) preserves the capture model while extending the specification.
- While pointer capture is active, subsequent events for that pointer are targeted to the capture target rather than ordinary hit testing. `pointerup` implicitly releases capture.
- Suppressing a pointer stream fires `pointercancel` and then boundary events, and implicitly releases capture. UA viewport manipulation is one specified suppression case; authors use `touch-action` to declare direct-manipulation behavior rather than trying to cancel viewport manipulation after the fact.
- The current draft also specifies boundary events caused by layout changes even when a pointing device is stationary. Therefore DOM/hit-target movement is not equivalent to pointer movement or a user-selected destination.

## SYNTHESIS / PRACTICE CONTRACT
Pointer identity, capture ownership, semantic drag ownership, visual candidate destination, and committed destination are separate fields. Record at least:
`scenario_id`, `semantic_object_id`, `pointer_id/type`, `stream_phase`, `capture_owner`, `semantic_drag_owner`, `hit_target`, `candidate_destination`, `boundary_event_reason`, `cancel_reason`, `commit_event`, `tx_id`, `projection_hash_before/after`, `focus_owner`, `recovery_eligibility`.

Invariant: **capture routes events; it does not authorize mutation.** A candidate exposed only because content reflowed beneath a stationary pointer cannot silently become a committed destination. A `pointercancel`/stream suppression cannot commit the preview transaction. Loss of capture alone is not success or failure; the implementation must resolve the semantic operation from its actual lifecycle.

## REPRODUCIBLE SCENARIOS
1. Start drag, move outside original row while capture/gesture ownership continues, then validly resolve.
2. Start preview, induce 200% recomposition/layout movement while pointer remains stationary; verify no synthetic destination commit.
3. Start drag, trigger viewport pan/UA suppression where executable; expect cancellation/no accidental mutation.
4. Remove/rebuild the visual row during preview; semantic object identity must not be replaced by the new ordinal occupant.
5. Release/cancel, then move pointer over another target; no stale preview owner may commit.
6. Repeat first/middle/last/system-group/boundary cases twice and compare drag with the non-drag single-pointer path.

## CRITIQUE / ACCEPTANCE
FAIL if capture identity is treated as transaction authority, layout-driven boundary changes commit a reorder without a resolved user action, `pointercancel` changes the projection hash, stale capture/preview state survives into a later pointer sequence, or focus/recovery/status claim a committed move that did not occur.

## RELATED DOMAIN CHECK
- Type: T060 transfer corpus remains downstream; pointer ownership is not repaired through typography.
- Color: C091 preview/cancel/commit separation transfers directly; C092 should add capture/interruption without inventing a new semantic truth.
- Layout/Interaction: I077–I078 are prerequisites; L082 geometry must now distinguish pointer movement from layout-under-pointer movement.
- Web: W091 requires event provenance; W092 must test actual served browser capture/suppression rather than infer it from framework docs.
- Content: CD097 consequence truth transfers; interruption/capture mechanics must not leak into user-facing copy unless they materially change available action/recovery.

## HANDOFFS TO OTHER SPECIALISTS
Web should capture browser event order/capture provenance; Layout should record stationary-pointer geometry before/after recomposition; Color and Content should represent only resolved semantic state; Type keeps mature fallback until T021 closes.

## OPEN
Actual LogMate non-drag reorder and drag runtime are not yet available for this closure. Independent-engine, physical touch/pen, AT, motor-error, discoverability, workload and representative-pilot evidence remain OPEN.