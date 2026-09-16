# CD021 — Structured message inventory and localization stress contract

Classification: **SYSTEMS PRACTICE + TRANSFER PREPARATION**

## RELATED DOMAIN CHECK
T021 requires literal operational identifiers to remain intact. C021 requires verbal state identity independent of hue. L013/I008 supply spatial/state truth. W020/W021 is the browser implementation-transfer surface.

## Structured message model
A message instance is data, not an arbitrary prose blob:

`message_id + object_id + lifecycle_state + certainty + available_action + consequence + recovery + persistence_scope + channel + locale + typed_variables`

### Typed variables
- `flight_number`: literal operational identifier; bidi-isolated when embedded in RTL text.
- `registration`: literal identifier; never locale-number formatted.
- `airport_code`: literal identifier.
- `count`: locale-formatted quantity.
- `date_time`: locale-realized temporal value with explicit timezone/context when operationally material.
- `duration`: locale-realized presentation backed by canonical duration data.

## Core inventory
| Message ID | State | Required semantic payload | Safe action |
|---|---|---|---|
| `record.save.pending` | pending | object + action in progress | wait/cancel only if contract supports cancel |
| `record.save.confirmed` | confirmed | object + completion | continue |
| `record.save.failed_known` | known failure | failed action + known non-commit + recovery | retry when safe |
| `record.save.outcome_unknown` | outcome unknown | request sent + result unverified + consequence of duplicate | verify/reconcile; no blind retry |
| `record.edit.offline_local` | offline/local | local edit state + remote-sync limitation | continue locally / sync later |
| `record.conflict.detected` | conflict | affected object + competing state + resolution need | review/resolve |

## Surface/channel variation rule
Phone, EFB/tablet, web, notification and email may alter ordering/detail, but may **not** alter:
- lifecycle state;
- certainty;
- whether an action is safe;
- consequence;
- affected scope.

A notification may shorten context, but it must deep-link or otherwise provide access to the missing recovery context rather than imply certainty it does not have.

## Pseudo-localization stress
Executable transfer should test at least:
- 30–40% expansion;
- accented/expanded Latin characters;
- RTL wrapper text with LTR operational identifiers isolated;
- long action labels;
- date/time and count expansion;
- narrow phone width and 200% text/zoom.

String truncation is not an acceptable fix when it removes state, certainty or safe action.

## RTL/bidi strategy
Operational identifiers are typed literals and should be isolated from surrounding directional context using platform-appropriate bidi isolation. This is an implementation requirement to be verified in Web/native transfer, not a claim that this document proves browser behavior.

## Gate result
**STRUCTURED INVENTORY CONTRACT PASS; EXECUTABLE LOCALIZATION TRANSFER OPEN.**
Human comprehension/trust, translator workflow quality, notification delivery and screen-reader behavior remain OPEN.

## HANDOFFS TO OTHER SPECIALISTS
- Web W021: implement these IDs as data-driven messages; stress expansion/RTL/zoom/status exposure.
- Layout L013: permit vertical growth rather than semantic deletion.
- Interaction I008: remains source of truth for safe actions.
- Type T021: proof corpus keeps literal identifiers unchanged.
- Color C021: hue is reinforcement, not the message selector.