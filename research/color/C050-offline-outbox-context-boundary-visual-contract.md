# C050 — Offline Outbox Context-Boundary Visual Contract

Evidence purpose: **PRACTICE / TRANSFER VALIDATION**. Extends C049 from stale read/cache context into queued consequential mutations created under one tenant/workspace and later viewed or synchronized under another.

## RELATED DOMAIN CHECK
- **Type:** T021 remains provisional; queue IDs/context labels use mature fallback and must not trigger custom-metric scope creep.
- **Layout/Interaction:** I037 owns whether a queued operation may execute; L041 owns queue/context spatial continuity.
- **Web:** W050 owns runtime provenance for enqueue, context switch, reconnect and dispatch.
- **Content:** CD056 owns queued/suspended/wrong-context/recheck language.
- **UX:** human comprehension of queue ownership remains OPEN.

## Problem
A queued action can look visually ready because it was valid when created. After tenant/workspace switch, that appearance can falsely imply that the current context owns or may dispatch it.

## Visual truth states
Keep these distinguishable without color-only dependence:
- `queuedContextConfirmed`
- `queuedPriorContext`
- `dispatchSuspendedContextMismatch`
- `dispatchAuthorityUnknown`
- `dispatchRecheckRequired`
- `dispatchDenied`
- `dispatchConfirmed`
- `outcomeUnknown`

A prior green success/accent, current workspace brand color, selected queue row, enabled-looking icon, or chronological recency must never promote `queuedPriorContext` into dispatch authority.

## Acceptance matrix
Test normal color, grayscale, hue removal, icon removal, forced colors, dark/light, print/export and selection/focus overlays. In every condition:
1. current workspace identity remains separable from operation-origin workspace;
2. suspended/mismatch remains separable from failed/denied;
3. unknown remains separable from confirmed;
4. focus/selection indicates navigation only, never authority;
5. current-context brand styling cannot recolor prior-context queued work into apparent ownership.

## Failure conditions
FAIL if an A-origin queued mutation shown while B is current appears actionable solely because B uses the same semantic success/accent token, same object ID, or the row is focused/selected.

## Evidence boundary
This is a deterministic visual contract. No runtime, production isolation, observer, CVD/low-vision, physical-display or human-task PASS is claimed.

## HANDOFFS TO OTHER SPECIALISTS
W050 should capture computed styles and forced-colors evidence with origin/current context IDs. I037/L041 supply dispatch truth and geometry. CD056 must verbalize every non-color state.