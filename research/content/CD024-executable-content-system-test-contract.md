# CD024 — Executable content-system test contract

Classification: **STAGE 3 PRACTICE / EXECUTABLE VALIDATION DESIGN**

## Purpose
Move CD023 from governance architecture to a bounded executable validation target without claiming translator, runtime or human evidence before execution.

## RELATED DOMAIN CHECK
- Type T022 requires literal identifiers/time/numeric material to remain typed rather than prose-normalized.
- Color C022 reinforces semantic states but external channels may lose product color.
- L014/I009 require certainty, recovery and safe action to survive reflow/recomposition.
- Web W021 provides the first integrated browser surface for pseudo/RTL/status transfer.

## Bounded machine-readable model
Each message record must contain at minimum:
- `message_id` — stable semantic identifier;
- `concept_id` / affected object type;
- authoritative `state_id`;
- `action_id` or explicit none;
- certainty class;
- consequence/recovery requirement;
- surface/channel eligibility;
- typed variables;
- freshness/revalidation policy where external/stale action is possible;
- locale realization key.

## Required executable lint failures
A future CD024 runner must fail on:
1. unknown state/action/concept ID;
2. missing required typed variable;
3. literal operational identifier marked as freely localized prose;
4. outcome-unknown message exposing blind retry;
5. external channel strengthening certainty versus authoritative state;
6. actionable external projection missing freshness/revalidation policy where required;
7. material semantic change silently reusing an incompatible message ID;
8. locale fallback dropping certainty, consequence, recovery or safe action;
9. RTL realization lacking isolation metadata for LTR operational literals;
10. pseudo expansion that is 'fixed' by deleting required semantic qualifiers.

## Pseudo/localization fixtures
Minimum fixtures include:
- +30–40% expanded Latin;
- accented pseudo-Latin;
- RTL wrapper with `KE704`, `HL8301`, `ICN`, `NRT`, `1,284:35` isolated as literals;
- long safe-action labels;
- plural/count/date-time/duration variables as locale-realized types.

## Channel invariance checks
In-app, notification, email and history projections may alter order/detail but must preserve authoritative certainty and may not invent urgency/action. Suppressed channels are a valid result when interruption, sensitivity, freshness or destination constraints are not satisfied.

## W021 transfer
The browser specimen should consume message/state IDs rather than infer state from displayed English. Browser success can prove rendered transfer of a bounded fixture; it cannot prove translator comprehension, notification delivery or human trust.

## Gate decision
CD024 design is ready for serialization/runner implementation. Stage 3 remains OPEN until executable lint output exists and browser/native transfer contradictions are reconciled.

## HANDOFFS TO OTHER SPECIALISTS
- Web: bind W021 fixtures to stable IDs and return rendered pseudo/RTL/status failures.
- Interaction: authoritative state/action registry remains canonical; Content lint must not redefine behavior.
- Layout: do not solve overflow by deleting qualifiers.
- Type: preserve literal operational data types for shaping/metric stress.
- Color: verbal state identity remains sufficient without hue.

## Evidence boundary
No executable lint PASS, production localization, TMS workflow, notification delivery, AT or human comprehension/trust evidence is claimed by this contract alone.