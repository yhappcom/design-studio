# I056 — Material Feedback Repair Transfer Spec

Date: 2026-09-18
Stage: Stage 3 PRACTICE
Purpose: TRANSFER VALIDATION

## Source localization
The MintTap lab Settings destinations are tappable `ListTile` rows. Recent runtime evidence detected a Material/decoration ownership assertion in the wide workflow. The repair must restore the expected interaction layer rather than suppress feedback.

## State contract
For each destination verify idle → hover where applicable → focus → pressed → activation → destination/outcome. For async product flows retain separate contracts for pending → known failure → correction/retry and ambiguous outcome → verify/reconcile → safe retry.

## Repair rules
- Ensure the interactive tile has an appropriate Material paint owner for ink/state feedback.
- Do not remove `onTap`, splash, focus or selected feedback merely to make the assertion disappear.
- Decorative backgrounds must not occlude feedback or accessible focus indication.
- Geometry and hit target must remain stable under enlarged text and localization.

## Evidence
Capture widget-test result plus rendered pressed/focus evidence where the runtime supports it. Browser evidence must later repeat keyboard focus and pointer activation in an actually served build.

Human discoverability, comprehension and professional-workflow efficiency remain OPEN.