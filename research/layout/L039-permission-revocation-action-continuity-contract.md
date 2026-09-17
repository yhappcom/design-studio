# L039 Permission Revocation Action Continuity Contract

Evidence mode: **STAGE 3 SYSTEMS PRACTICE / TRANSFER VALIDATION**.

## Goal
Preserve spatial and informational continuity when an action that was previously available becomes unauthorized while the underlying object/history may remain visible.

## RELATED DOMAIN CHECK
I035 owns authorization/action truth. C048 owns visual-state precedence. W048 supplies runtime permission/recheck evidence. CD054 supplies semantic labels. Type custom metrics remain provisional.

## Information spine
For a recoverable object with changed authorization, preserve:
`object → current recoverability → current authorization consequence → evidence/certainty → available safe action or recheck → history`.

Do not place a stale enabled Restore affordance in the dominant action position while a remote permission check is pending. If the control must disappear after authoritative denial, the consequence/explanation must remain near the former action locus so the layout does not look like an arbitrary UI failure.

## Focus and reflow
- If focused mutation control becomes unavailable, move focus only to a logical surviving target that preserves meaning/operability; do not reset to page top by default.
- At 200% text, narrow width and localization expansion, permission explanation and safe next action must remain adjacent enough to preserve causal relation.
- Read-only history must not collapse merely because mutation permission was revoked.
- A disabled-looking control is not itself sufficient explanation of authorization state.
- Responsive ordering must not make a stale cached action appear before the current authorization verdict.

## Stress matrix
1. permission revoked while action has keyboard focus;
2. permission revoked while a confirmation layer is open;
3. offline cached enabled action → reconnect denial;
4. authorization service unavailable → recheck state;
5. read access retained, mutation access revoked;
6. permission restored after object state changed;
7. forced-colors, 200% text, long locale and export/history view.

## Acceptance
PASS for deterministic geometry requires that object identity, current permission consequence, safe next step and history remain reachable and correctly ordered through each transition. Human discoverability/comprehension remains OPEN.

## HANDOFFS TO OTHER SPECIALISTS
C048 must preserve permission-state distinction without color-only meaning; W048 records focus/geometry after server verdict; CD054 must not force geometry-preserving euphemisms that hide authorization truth.