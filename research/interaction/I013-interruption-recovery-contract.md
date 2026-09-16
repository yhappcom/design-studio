# I013 — Interruption and Recovery Contract

Evidence type: SYNTHESIS / PRACTICE / DEPENDENCY / OPEN

## RELATED DOMAIN CHECK
I012 defines six deterministic state→action invariants. CD031 correctly flags two fixture phrases whose truth depends on interruption/network behavior. W024 is deterministic browser evidence, not backend truth. L018 covers disrupted viewport geometry; C027 covers focus/overlay survival.

## Contract
A professional record workflow must distinguish at least: request pending; confirmed completion; known failure before commit; outcome unknown after possible commit; offline/stale local view; and divergent/conflicting versions. Interruption must not automatically map to failure: if commit outcome cannot be known, the safe state is outcome-unknown until authoritative reconciliation.

Recovery actions therefore remain conditional on system capability: retry only when duplicate execution is safe or idempotent; check/reconcile when outcome may have committed; view local when connectivity prevents authoritative refresh; compare versions before destructive conflict resolution.

## Interruption cases for future backend transfer
1. navigation away while pending;
2. app/browser background or refresh while pending;
3. connection loss before request dispatch;
4. connection loss after dispatch but before response;
5. timeout with unknown server outcome;
6. stale local cache after reconnect;
7. concurrent edit conflict.

For each case record: authoritative state source, whether the original action may have committed, allowed action, forbidden action, persistence across reload, and user-visible status update mechanism.

## Current result
**CONTRACT MODEL ADVANCED / BACKEND TRANSFER OPEN.** No fixture is promoted to backend truth. This specifically blocks unconditional use of `Keep this screen open` and `Fix the connection` until the implementation contract supports them.

## HANDOFFS TO OTHER SPECIALISTS
Content revises conditional wording only after behavior is known. Web must test true Fetch/history/reload behavior at an origin. Layout protects recovery controls under disruption. Color preserves state identity without color-only encoding. UX integration treats interruption→recovery as an end-to-end workflow; human trust/comprehension remains OPEN.
