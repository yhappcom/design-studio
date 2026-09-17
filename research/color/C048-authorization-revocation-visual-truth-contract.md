# C048 Authorization Revocation Visual Truth Contract

Evidence mode: **STAGE 3 SYSTEMS PRACTICE / TRANSFER VALIDATION**.

## Goal
Prevent stale permission styling from masquerading as current authority when recovery capability and subject authorization diverge.

## RELATED DOMAIN CHECK
I035 owns the authorization/action oracle. L039 owns spatial continuity. W048 supplies runtime evidence. CD054 supplies non-color semantics. Type remains provisional.

## Semantic states
At minimum distinguish:
- `recoveryAuthorizedConfirmed`;
- `authorizationCheckPending`;
- `authorizationUnknown`;
- `recoveryNotAuthorizedConfirmed`;
- `permissionChangedSinceView`;
- `priorOperationOutcomeUnknown`.

These are not interchangeable with recoverability states from C047. An object can be recoverable yet unauthorized for the current subject.

## Visual precedence
Current authorization consequence outranks stale enabled-control styling, prior success color, cached role badge, selection, focus and retention countdown emphasis. Color may reinforce the state but cannot be the only cue.

## Adversarial matrix
1. cached green/primary Restore remains after server denial;
2. permission revoked while focus ring remains on former action;
3. hue removed / grayscale;
4. forced-colors mapping collapses custom fills;
5. disabled styling collides with `authority unavailable`;
6. permission restored but object no longer recoverable;
7. print/export shows historical permission without implying current permission.

## Acceptance
A reviewer must be able to identify which visual evidence is historical, which is current authorization consequence, and which action is safe after hue/background/icon removal. `notAuthorized` and `authorizationUnknown` must not collapse into the same visual truth when their safe next steps differ.

## Evidence boundary
No executed W048 artifact, observer salience, CVD/low-vision human study, calibrated display or Color Stage 3 PASS is claimed.

## HANDOFFS TO OTHER SPECIALISTS
W048 should capture computed styles/forced-colors with the same authorization verdict IDs; L039/I035/CD054 own geometry, behavior and wording respectively.