# CD036 — Action-enablement content contract

Evidence type: **SYSTEMS PRACTICE / CONTENT CRITIQUE**

## RELATED DOMAIN CHECK
I017 owns which recovery action is safe/enabled; CD036 owns its label, explanation and consequence wording. W029 supplies runtime transfer; L021 owns reachability; C030 ensures state meaning is not color-only; Type T021 must accommodate truthful strings rather than force shortening.

## Content model
Every recoverable state binds:
`semantic_message_id → certainty → primary_action_id → primary_action_label → consequence → optional secondary action → revision → locale`.

The action label must describe the actual safe action:
- outcome unknown → **Check outcome**, not Retry;
- confirmed → **View record** / Continue as product context requires;
- known rejection → correction-specific action when known;
- conflict → **Compare versions** before destructive resolution;
- offline/stale → **View local record** or reconnect/reconcile language supported by product truth.

## Disabled/withheld action language
Do not present an unsafe retry as the visually dominant action and explain the risk only in helper text. If retry is not permitted by I017, omit/disable it according to the interaction contract and make the safe action primary. Content cannot use reassuring tone to weaken an uncertainty boundary.

## Localization contract
Semantic IDs and action IDs remain stable even when localized wording changes. Expansion is a Layout/Web stress input, not a reason to merge materially different states. Locale review must verify that certainty terms do not become stronger or weaker in translation.

## Current result
**CONTENT CONTRACT ADVANCED / TOOLCHAIN + HUMAN REVIEW OPEN.** CD033 localization tooling, real locale review, AT wording behavior and human comprehension remain unexecuted.

## HANDOFFS
I017 supplies action truth; W029 binds rendered IDs; L021 tests long-string reachability; C030 verifies non-color state survival; Type receives full operational strings inside T021 proof corpus.