# CD023 — Content Tokens, Message Schema, and Governance Contract

Status: **STAGE 3 PRACTICE — MACHINE-READABLE SYSTEM CONTRACT / NOT PASSED**  
Date: 2026-09-16

## Question
What should a machine-readable Content system expose so engineering, localization, analytics, QA and multiple surfaces can consume language without making English strings the source of product state?

CD020 established concepts/state architecture; CD021 structured message inventory; CD022 channel continuity/governance. CD023 turns those principles into a bounded schema and lintable governance contract. This is architecture practice, not a production framework recommendation.

## RELATED DOMAIN CHECK

- **Type:** T022 mature-font role work needs literal identifier/numeric roles to remain typed; schema exposes those distinctions rather than encoding them in display strings.
- **Color:** C022 state aliases remain visual reinforcement. Content schema uses semantic state IDs, never color names, as message selectors.
- **Layout/Interaction:** I008 remains source of state/action/recovery truth; L013 owns recomposition. Schema references those truths but does not create them.
- **Web:** W021 is the executable integration target. CD023 can later be serialized into a browser fixture; no browser evidence is claimed here.
- **Content:** CD020–CD022 are direct prerequisites. This is an extension, not duplicate study.

---

## 1. Content token is not a sentence token

### SYNTHESIS
A mature content token identifies a semantic role/contract, not merely a reusable phrase.

Bad abstraction:
- `common.ok = "OK"`
- `common.error = "Error"`
- `common.failed = "Failed"`

These maximize textual reuse while destroying object, state, consequence and action context.

Better abstraction identifies intent:
- `record.save.pending.status`
- `record.save.outcome_unknown.status`
- `record.save.known_failure.status`
- `record.conflict.review.action`

Exact naming convention is implementation-dependent; semantic separation is the invariant.

---

## 2. Proposed message schema v0.1

```text
message_id
concept_id
state_id
event_id?
role
surface
channel
intent
certainty
scope
consequence_class
recovery_class
allowed_action_ids[]
variables[]
localizer_context
accessibility_intent?
tone_profile
freshness_policy?
sensitivity_class?
owner
status: active | deprecated | experimental
supersedes?
```

Variable schema:

```text
name
type
required
literal_policy
format_policy
example
sensitivity
```

Possible variable types include `literal_identifier`, `localized_count`, `date`, `time`, `duration`, `currency`, `percentage`, `localized_enum`, `user_text`, and `product_name`.

### STUDIO RULE
Schema fields exist only when they constrain a real downstream decision. Metadata accumulation without consumer/value is rejected.

---

## 3. Message ID design principles

A stable ID should:
- identify semantic purpose, not current English wording;
- remain stable through copy-only revisions;
- change/deprecate when state/consequence meaning materially changes;
- avoid locale names in the canonical semantic ID;
- avoid visual placement (`red_banner_text`) as semantic identity;
- avoid transient product implementation details unless they define meaning.

### REJECT
- `error1`, `error2`;
- `red_warning`;
- `long_error_text`;
- `english_save_failed`;
- one `generic_error` key populated from many unrelated states.

---

## 4. Content token layers

Do not collapse all language assets into one token class.

Proposed layers:
1. **concept registry** — canonical product/domain concepts and definitions;
2. **action registry** — action identity, object, consequence and safety class;
3. **state/event registry** — authoritative semantic states/events from product/Interaction;
4. **message family** — communication intent tied to state/event;
5. **surface/channel projection** — in-app, history, notification, email variants;
6. **locale realization** — translated/localized messages and formatting rules;
7. **runtime binding** — component/route/status invocation and variables.

This layering prevents a translation string from becoming a product concept definition or state-machine constant.

---

## 5. Semantic inheritance versus duplication

### STUDIO JUDGMENT
Inheritance is safe only for invariants, not prose fragments.

A channel variant may inherit:
- certainty;
- state ID;
- safe action set;
- sensitivity;
- variable types.

It should not automatically inherit:
- sentence order;
- punctuation;
- title/body split;
- pronouns;
- truncation strategy;
- grammatical fragments.

This keeps semantic reuse high without forcing English syntax reuse.

---

## 6. Fallback policy

Localization/runtime fallback is a semantic risk, not merely a missing-string concern.

A fallback contract must answer:
- if locale-specific realization is missing, what language may appear?
- can mixed-language UI appear?
- does fallback preserve variables and directionality?
- can a deprecated source message be used as fallback?
- what happens if variable schema differs between source and target?
- does high-consequence content fail closed, show source language, or use another policy?

### OPEN
Exact fallback behavior is product/platform/localization-policy dependent. CD023 does not choose a universal strategy.

### REJECT
Silently rendering a semantically older translation because a key name happens to match.

---

## 7. Structural lint rules v0.1

A machine-readable inventory should be able to fail CI or audit when:

- active `message_id` duplicates exist;
- a state message lacks `state_id`;
- certainty-sensitive states lack `certainty`;
- outcome-unknown exposes an action outside authoritative safe actions;
- external channel lacks freshness/sensitivity policy;
- a variable lacks type/context;
- literal identifier is configured for ordinary numeric localization;
- deprecated message remains referenced by an active projection without explicit compatibility rule;
- message references unknown concept/action/state IDs;
- locale realization has missing required variables;
- a high-consequence message lacks localizer context;
- semantic key contains locale or visual-color identity as its only meaning.

These checks establish internal contract integrity, not copy quality or comprehension.

---

## 8. Change classes and review depth

### Class A — wording-only
Meaning, variables, state, action and consequence unchanged. Content/localization review may suffice depending on process.

### Class B — presentation projection
Same semantic family, new/changed surface/channel. Requires Content + owning surface/channel review.

### Class C — variable/schema
Variable type/addition/removal/format changes. Requires engineering/localization/QA compatibility review.

### Class D — semantic contract
State, certainty, consequence, action, scope or recovery meaning changes. Requires product/Interaction + Content + downstream propagation review.

### Class E — policy
Freshness, sensitivity, notification eligibility, retention or fallback changes. Requires relevant product/privacy/platform owners.

The classification makes “small copy change” an evidence question rather than a visual impression.

---

## 9. Terminology governance

Concept registry entries should distinguish:
- `concept_id`;
- canonical source-English term;
- definition;
- domain/source authority;
- prohibited/ambiguous synonyms where justified;
- related concepts;
- scope;
- literal identifier examples;
- locale terminology notes;
- owner;
- status/version.

### SYNTHESIS
Synonym variation is not automatically good writing in interfaces. For operational concepts, controlled repetition can preserve mapping. Marketing/educational surfaces may allow broader expression only when concept identity remains clear.

---

## 10. Analytics boundary

Analytics should reference semantic event/message IDs rather than parse displayed text.

Benefits at architecture level:
- copy revisions do not fragment metrics;
- locale changes do not create separate semantic events;
- deprecated semantics can be versioned;
- recovery/action outcomes can be linked to authoritative state.

### CAUTION
Analytics correlation does not prove comprehension or causal effect of copy. Experimental design/human research remains separate.

---

## 11. Accessibility binding

Visible message and programmatic status may share a semantic family but are not necessarily one literal string.

Schema may need:
- announcement intent;
- urgency/politeness class as runtime metadata;
- deduplication/suppression dependency;
- focus relationship;
- object context needed for nonvisual interpretation.

Interaction/Web own actual focus/live-region behavior. Content supplies the semantic announcement requirement.

### REJECT
Using punctuation/capitalization in a string as the runtime mechanism for urgency.

---

## 12. Localization package boundary

A production localization handoff should eventually be generated from semantic inventory, not from a blind list of English strings.

Minimum package candidates:
- stable ID;
- English source realization;
- concept definition;
- state/certainty context;
- surface/channel;
- variable types/examples;
- screenshot/reference where available;
- character/preview constraints only when real;
- tone bounds;
- related terminology;
- revision/version.

CD023 defines the information contract but does not claim a production TMS/vendor workflow.

---

## 13. Governance failure modes

- `GENERIC_KEY_SEMANTIC_COLLAPSE`
- `DISPLAY_STRING_AS_STATE`
- `VISUAL_NAME_AS_SEMANTIC_ID`
- `LOCALE_NAME_IN_CANONICAL_ID`
- `PROSE_FRAGMENT_INHERITANCE`
- `VARIABLE_SCHEMA_DRIFT`
- `FALLBACK_SEMANTIC_DRIFT`
- `DEPRECATED_ID_ACTIVE`
- `UNKNOWN_CONCEPT_REFERENCE`
- `UNKNOWN_ACTION_REFERENCE`
- `ANALYTICS_PARSE_DISPLAY_TEXT`
- `COPY_CHANGE_MISCLASSIFIED`
- `LOCALIZATION_WITHOUT_CONTEXT`
- `ACCESSIBILITY_URGENCY_IN_PUNCTUATION`
- `METADATA_WITHOUT_CONSUMER`
- `HUMAN_VALIDATION_NEEDED`
- `RUNTIME_TRANSFER_NEEDED`

---

## 14. Bounded machine-readable fixture

Illustrative, not production syntax:

```yaml
message_id: record.save.outcome_unknown.status
concept_id: record
state_id: save_outcome_unknown
role: status
surface: record_editor
channel: in_app
intent: explain_unconfirmed_persistence
certainty: unknown
scope: one_record
consequence_class: duplicate_risk
recovery_class: verify_then_reconcile
allowed_action_ids:
  - verify_record_state
variables:
  - name: flight_number
    type: literal_identifier
    required: true
    literal_policy: preserve
localizer_context: The save request was sent, but authoritative persistence cannot be confirmed. Do not translate this as known failure.
tone_profile: operational_uncertainty
owner: content
status: active
```

### Structural assertion
A notification projection of this family may shorten detail but must retain `certainty: unknown` and cannot add `retry_save` unless Interaction changes the safe-action set.

---

## 15. KEEP / REWORK / REJECT

### KEEP
- semantic IDs independent of English copy;
- layered concept/action/state/message/projection/locale/runtime model;
- typed variables;
- semantic inheritance, not phrase inheritance;
- explicit change classes;
- governed deprecation;
- analytics keyed to semantics, not text;
- localization packages generated with context.

### REWORK
- exact YAML/JSON/ARB/ICU/Flutter/web implementation;
- CI tooling and repository location;
- actual LogMate/MintTap terminology registries;
- TMS/vendor integration;
- fallback policy;
- AT announcement runtime metadata;
- privacy/security ownership.

### REJECT
- generic phrase libraries as primary content architecture;
- English string keys as state identifiers;
- one common `error` token;
- key reuse after semantic change;
- locale-specific grammar embedded in canonical state logic;
- analytics based on rendered-copy parsing.

---

## Stage 3 implication

CD023 gives Stage 3 a machine-readable governance model connecting terminology, states, actions, message families, channels, localization, analytics and accessibility. It makes CD020–CD022 lintable in principle and defines what later production implementation must prove.

Stage 3 remains **PRACTICE / NOT PASSED**. A static schema is not production evidence. The next highest-value block is executable transfer: serialize a bounded inventory, run structural lint/pseudo-localization checks, then reconcile actual W021 browser findings when available. Production translator workflow and human evidence remain separate later gates.

## HANDOFFS TO OTHER SPECIALISTS

- **Interaction:** expose authoritative state/action IDs and safe-action sets; Content schema must reference rather than duplicate behavioral truth.
- **Web:** consume semantic IDs/typed variables in W021-style specimens; report fallback, reflow, bidi, live-status and runtime invocation contradictions.
- **Type:** use typed literal identifiers/numeric values as role-specific stress data; do not infer semantics from formatting.
- **Color:** bind visual aliases to semantic state IDs, never the reverse.

## Evidence level

**SYSTEM ARCHITECTURE + MACHINE-READABLE CONTRACT DESIGN + LINT SPECIFICATION + GOVERNANCE/CHANGE-CLASS SYNTHESIS. No production schema implementation, CI execution, TMS, browser/native, AT, or human PASS claimed.**