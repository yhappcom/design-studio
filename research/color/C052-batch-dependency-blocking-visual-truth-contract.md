# C052 — Batch Dependency Blocking Visual-Truth Contract

Evidence purpose: **STAGE 3 PRACTICE / SYSTEMS PRACTICE / TRANSFER VALIDATION**.

## RELATED DOMAIN CHECK
- **Type:** T021 remains provisional; dependency strings use mature fallback.
- **Layout/Interaction:** I039 owns dependency/action truth; L043 owns hierarchy.
- **Web:** W052 supplies runtime dependency and reconciliation evidence.
- **Content:** CD058 verbalizes prerequisite, blocked, skipped and unknown states.
- **UX:** human causal comprehension remains OPEN.

## Problem
A batch can contain operations whose safety depends on another member. Aggregate success/error color or ordinary disabled styling can falsely imply that a dependent member failed, was denied, or is safely retryable when it is merely blocked by unresolved prerequisite authority.

## Visual truth states
Keep at least these meanings distinguishable where the product contract supports them:
- prerequisite confirmed;
- prerequisite outcome unknown;
- dependent blocked awaiting prerequisite reconciliation;
- dependent skipped by known prerequisite failure/policy;
- dependent independently denied/failed;
- dependent eligible for execution/retry;
- dependent confirmed.

Do not encode these meanings by hue alone. Text/status semantics, structure and control state must survive grayscale, forced colors, print/export and loss of background fills.

## Failure conditions
FAIL if:
- aggregate green makes a blocked/unknown dependent appear confirmed;
- aggregate red makes `blocked` appear `failed`;
- disabled appearance implies denial when execution is only suspended;
- selection/focus/accent overrides member certainty;
- prerequisite and dependent rows become indistinguishable after hue/background removal;
- visual ordering implies causal dependency that is not present in authority data.

## Validation matrix
Bind to W052 shared IDs and test mixed prerequisite outcomes under normal theme, grayscale, forced colors, print/export, narrow dense list, 200% text, selection and focus overlays.

## Evidence boundary
No C052 artifact PASS, Color Stage 3 PASS, cross-browser, calibrated display, CVD/low-vision observer or human comprehension PASS is claimed.

## HANDOFFS TO OTHER SPECIALISTS
I039 supplies the dependency oracle; L043 preserves prerequisite/dependent hierarchy; W052 supplies executable artifacts; CD058 supplies non-color meaning.