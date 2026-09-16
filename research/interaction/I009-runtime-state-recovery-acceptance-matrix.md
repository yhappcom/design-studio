# I009 — Runtime state and recovery acceptance matrix

Classification: **STAGE 3 PRACTICE / TRANSFER VALIDATION PREPARATION**

## Purpose
Turn I008's cross-surface state invariants into runtime-observable acceptance conditions for W021 and later native transfer.

## RELATED DOMAIN CHECK
Type T022 preserves operational literals; Color C022 reinforces but does not define state; L014 owns spatial preservation; W021 owns browser integration; CD022–CD023 owns semantic projections and channel wording.

## State contract
Authoritative sequence remains:
`idle → edited → commit-requested → pending → {confirmed | known-failure | outcome-unknown}`.
Offline/stale, conflict, selection/navigation context and overlay are orthogonal conditions, not substitutes for lifecycle certainty.

## Runtime assertions
- **pending:** duplicate commit action is unavailable or explicitly guarded; status is exposed without relying on animation/color.
- **confirmed:** confirmation identifies the affected object and does not preserve obsolete retry/recovery controls.
- **known failure:** failure is named and a valid retry/recovery action may be offered only when the underlying state authorizes it.
- **outcome unknown:** blind retry remains blocked; verification/reconciliation is the safe next action.
- **offline/stale:** local availability is not presented as remote confirmation; freshness context remains available.
- **conflict:** competing versions/ownership are exposed before destructive reconciliation.

## Recomposition invariant
Changing viewport, theme, locale direction, zoom or reduced-motion preference must not change lifecycle state, certainty or safe action. If an implementation remount resets state, that is a transfer failure even when the screen looks correct.

## Recovery invariant
Recovery succeeds only when the user can regain:
1. affected object identity;
2. task/edit context where still valid;
3. current certainty/freshness state;
4. a safe authorized next action.

A navigation return alone is insufficient.

## Cross-channel extension
CD022 shows the same semantic family may project to notification/email/history. External copy may not strengthen certainty. Deep-linked actions that can become stale require revalidation before executing consequential behavior.

## Evidence boundary
This is a deterministic acceptance contract, not proof of backend behavior, human trust, interruption cost or native/browser runtime. W021 must execute browser-observable portions; real network ambiguity requires an HTTP/backend-capable environment.

## HANDOFFS TO OTHER SPECIALISTS
- Web: instrument state persistence through recomposition and verification flow.
- Layout: keep state/recovery adjacent under L014 stress.
- Content: bind message IDs to these states; never infer state from prose.
- Color: preserve redundant non-color carriers.
- Type: operational identifiers used in recovery remain literal and legible.