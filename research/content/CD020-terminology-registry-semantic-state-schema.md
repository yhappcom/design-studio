# CD020 — Terminology Registry + Semantic State Schema

Classification: **SYSTEMS PRACTICE + CONTENT GOVERNANCE MODEL**

## RELATED DOMAIN CHECK
- I007 is authoritative for state/action/recovery truth.
- L012 allows surface-specific composition without semantic deletion.
- C020 maps visual state roles but verbal meaning must survive hue removal.
- Web W019/W020 is the eventual runtime/localization transfer surface.
- Type T021 remains drawing-invalid; required wording and literal identifiers are not shortened to fit it.

## Concept registry
A product concept receives a stable semantic ID independent of displayed English wording.

Minimum registry fields:
`concept_id, canonical_meaning, object_type, allowed_synonyms, forbidden_ambiguities, literal_data_policy, lifecycle_scope, action_relationships, translator_context, accessibility_context, owner, version`.

Initial professional-record concepts:
- `record.identity` — persistent identity of the operational record;
- `record.edit` — local modification not yet equivalent to confirmed persistence;
- `commit.request` — user request to persist/propagate change;
- `sync.pending` — confirmation not yet established;
- `sync.confirmed` — persistence/propagation confirmed to defined scope;
- `commit.known_failure` — operation known not to have succeeded;
- `commit.outcome_unknown` — final outcome not known;
- `record.offline_stale` — displayed data may not represent remote/current truth;
- `record.conflict` — competing versions require resolution.

Literal flight/operational identifiers, registration, airport codes and similar typed values are data, not translatable prose.

## Semantic message schema
Consequential messages derive from:
`object + lifecycle_state + action_availability + consequence + recovery_certainty + persistence_scope + channel/surface + locale_context`.

Required message fields:
- stable message ID;
- semantic state ID;
- primary assertion;
- consequence where material;
- safe next action(s);
- recovery/verification instruction;
- variables with explicit types;
- surface/channel variant rules;
- translator note;
- accessibility/status-announcement intent.

## Cross-surface realization
Phone may use shorter first-line phrasing with expandable detail; tablet/EFB may keep state and recovery adjacent; desktop/web may expose state in table/detail simultaneously. All variants must preserve certainty, consequence and safe action. Literal sentence sameness is not required.

## Change propagation
Changing a concept/state triggers review of terminology → action labels → form/helper text → lifecycle/recovery messages → search/filter/settings labels → notification/email variants → localization context → accessibility names/status exposure. Display strings never become logic keys.

## Localization architecture
Reject concatenated English fragments. Variables are typed; locale realization owns word order, plural/date/number formatting. Pseudo-localization, RTL/bidi and real locale transfer remain executable future work. Operational identifiers remain isolated from surrounding localized prose so bidi/localization does not mutate their data identity.

## Failure tests
FAIL if pending and outcome-unknown share a semantic ID; notification certainty exceeds in-product certainty; a translated display string becomes a state key; long localization is solved by deleting consequence/recovery; or color/direction/location wording is required to identify an action.

## Gate result
**CD020 SEMANTIC ARCHITECTURE: PASS FOR SCHEMA / Stage 3 remains PRACTICE.**

Open: executable ICU/message-format implementation, pseudo-localization, RTL/bidi, translator workflow, notification delivery, screen-reader transfer, human comprehension/trust.

## HANDOFFS TO OTHER SPECIALISTS
- Interaction: schema directly preserves I007 truth distinctions.
- Layout: L012 must accommodate expanded consequence/recovery strings.
- Color: state labels remain valid without hue.
- Web: implement stable IDs, typed variables and status semantics in W020+.
- Type: preserve operational proof strings and do not shorten around failed geometry.