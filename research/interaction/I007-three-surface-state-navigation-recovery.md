# I007 — Three-surface State, Navigation & Recovery System

Classification: **SYSTEMS PRACTICE + UX BEHAVIOR CONTRACT**

## RELATED DOMAIN CHECK
- L012 owns the spatial compositions; I007 owns temporal/action truth.
- C020 reinforces states without redefining them.
- CD019 supplies semantic message architecture and preserves certainty.
- Web W019 has partial history/runtime proof; actual network outcome ambiguity remains OPEN.
- Type T021 cannot constrain interaction geometry yet.

## Canonical state machine
For one professional record:
`idle → edited → commit-requested → pending → {confirmed | known-failure | outcome-unknown}`

Orthogonal conditions: `offline/stale`, `conflict`, `selection`, `navigation context`, `transient overlay`.

These are not interchangeable states. In particular, outcome-unknown is not known failure.

## Action contract
- `idle`: inspect/navigate/edit where permitted.
- `edited`: save/commit or discard/revert where supported.
- `pending`: prevent duplicate consequence-changing commit unless operation is explicitly idempotent and product contract permits it.
- `confirmed`: expose completed state and next task.
- `known-failure`: retry only when retry is known safe; preserve edits/context.
- `outcome-unknown`: do not blind-retry; provide verification/reconciliation path.
- `offline/stale`: distinguish local editability from remote freshness/confirmation.
- `conflict`: require explicit resolution when automatic merge cannot preserve truth.

## Navigation/context invariant
Navigation state consists of destination + selected record + task phase + recoverable edit context. Closing a transient overlay must restore the prior meaningful context. Back/history must not silently discard uncommitted consequential edits.

Phone may serialize list/detail; tablet may preserve master/detail; desktop/web may expose multiple regions. These are presentation differences, not different action consequences.

## Interruption and recovery
A recoverable interruption records enough state to answer: what object, what was edited, what commit certainty exists, what action is safe now. Recovery is defined as return to meaningful task context, not merely returning to the same route/screen.

## Motion/reduced-motion equivalence
Animation may indicate continuity but cannot be required to know whether a record moved, saved, failed or needs verification. Reduced-motion mode must preserve state text, focus destination and structural change without depending on transition trajectory.

## Accessibility/UX static checks
WCAG 2.2 remains the web conformance baseline, while I007 treats keyboard/focus/target behavior as interaction contracts across surfaces. Conformance alone is not a human-usability PASS. Focus must follow meaningful task progression; pointer-only dragging cannot be the sole path for consequential reordering where the web criterion applies.

## Gate result
**I007 BEHAVIOR MODEL: PASS FOR DETERMINISTIC CONTRACT / Stage 3 remains PRACTICE.**

Open: native/router implementation, real network ambiguity, cross-device sync conflicts, AT announcements, physical device interruption, human error/recovery performance.

## HANDOFFS TO OTHER SPECIALISTS
- Layout: L012 regions must preserve this context model.
- Content: CD020 may derive messages from these exact states but not merge them.
- Color: C020 status roles map to these states.
- Web: W020 should implement/transfer focus, history and status behavior where executable.
- Type: consequential strings remain proof material.