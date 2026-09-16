# I008 — Cross-surface state and recovery invariants

Classification: **SYSTEMS PRACTICE + CONTRADICTION PREVENTION**

## RELATED DOMAIN CHECK
L013 defines spatial recomposition; C021 reinforces but does not define state; W020 is runtime transfer owner; CD020 defines messages from state truth; T021 geometry remains flexible.

## State tuple
`object × edit-state × commit-state × certainty × connectivity × selection × overlay × surface`

Canonical commit path remains:
`idle → edited → commit-requested → pending → {confirmed | known-failure | outcome-unknown}`.

## Cross-surface behavioral assertions
- `pending`: duplicate commit action is unavailable unless the underlying operation is explicitly idempotent and product semantics permit it.
- `confirmed`: committed truth is shown and stale pending language is removed.
- `known-failure`: retry may be offered only when the failed operation and retry consequence are known.
- `outcome-unknown`: blind retry remains blocked; user receives a verification/reconciliation path.
- `offline`: local editability and remote commit availability are separate truths; wording/UI must not collapse them.
- `conflict`: both competing versions/scopes remain identifiable until resolution; navigation cannot silently discard the conflict context.
- surface change/recomposition never converts one state into another.

## Navigation/recovery assertions
Recovery returns the user to **object + task + certainty context**, not merely a route or screen. A back action, overlay dismissal, viewport change or list/detail collapse must preserve unsaved/ambiguous state unless the user explicitly resolves/discards it under a defined contract.

## Input/accessibility assertions
Keyboard, touch and pointer may expose different affordance geometry but must provide equivalent task actions. Focus movement is a state transition with observable destination. Motion is optional presentation; reduced-motion mode preserves state and focus meaning.

## Failure-oriented scenarios
1. pending save + viewport recomposition;
2. network loss after request dispatch → outcome unknown;
3. offline local edit + later reconnect;
4. conflicting record update while detail is open;
5. overlay appears while recovery action has focus;
6. pseudo-localized message expands and changes region height;
7. forced colors removes authored hue.

For all seven, safe action and certainty are determined by state truth, never by surface geometry or message wording.

## Gate result
**DETERMINISTIC INVARIANT MODEL PASS; RUNTIME/NETWORK/NATIVE/HUMAN TRANSFER OPEN.**

## HANDOFFS TO OTHER SPECIALISTS
- Web W021 should execute scenarios 1, 5, 6, 7 and attempt 2/3 where network policy permits.
- Content CD021 must preserve certainty/action semantics across channel variants.
- Layout L013 must keep affected object/state/recovery spatially connected.
- Color C021 reinforces states but cannot create them.