# CD016 — Localization-Ready Cross-Surface Semantic Transfer

Status: **STAGE 2 PRACTICE — CROSS-SURFACE TRANSFER / NOT PASSED**  
Date: 2026-09-16

## Question
Can the Content system built in CD010–CD015 preserve the same product truth when content moves across forms, lifecycle states, onboarding, retrieval/configuration, compact controls, notifications, and future locales without using English surface strings as application logic?

This study is about semantic portability, not translation quality. It does not claim that a locale is good merely because strings can be externalized.

## RELATED DOMAIN CHECK

### Type
Current Type work has advanced beyond the prior R4B/R4C checkpoint into R4D full-family promotion/CI evidence. Content therefore treats text expansion, literal identifiers, numerics, wrapping and fallback as real rendering inputs while preserving the boundary: Type geometry cannot authorize semantic deletion.

### Color
Semantic state must survive loss or transformation of color. Localized content therefore cannot depend on a color adjective or colored badge as the sole carrier of state.

### Layout / Interaction
Interaction owns actual state, persistence, commit timing, retry safety, route/view/transient state, and recovery mechanics. CD016 transfers only the semantic contract across surfaces; it does not redefine behavior.

### Web
Web owns actual DOM/accessibility semantics, URL/history restoration, browser reflow, dynamic announcements, locale loading and network behavior. CD016 specifies content inputs that later browser transfer must test.

### Content
CD007 supplies the Foundation localization-ready baseline. CD010–CD015 supply Stage 2 forms, state, onboarding, retrieval/configuration and voice/tone contracts. CD016 is **INTEGRATION + TRANSFER VALIDATION PREPARATION**, not a repeat of CD007.

---

## 1. Translation readiness is not localization readiness

### SYNTHESIS

Externalizing English strings is necessary but insufficient. A content system is localization-ready only when the product meaning needed to construct each message exists independently of English wording.

A useful hierarchy is:

1. **product truth** — state, object, action, consequence, scope, certainty, recovery;
2. **semantic message contract** — message role, variables, grammatical relationships, priority, context;
3. **locale realization** — wording, morphology, order, punctuation, plural/category selection;
4. **surface realization** — button, field help, status, dialog, notification, compact summary, etc.;
5. **render/runtime realization** — typography, layout, AT semantics, timing, platform behavior.

Defect pattern: application logic inspects an English string such as `Saved`, `No data`, `Default`, or `Active` to infer state. This reverses the hierarchy and makes localization a behavioral risk.

### STUDIO RULE

**State selects message; message text never selects state.**

---

## 2. The semantic atom is not the string

For Stage 2 practice, define a portable content unit as a structured proposition:

- `message_id`
- `role`
- `state_class`
- `object_type`
- `action_or_event`
- `scope`
- `certainty`
- `consequence`
- `user_agency`
- `recovery`
- `variables`
- `literal_data`
- `count_or_quantity`
- `time_reference`
- `tone_profile`
- `surface_context`
- `localizer_context`
- `accessibility_intent`

Not every message needs every field. The point is that material meaning must be represented before English prose is written.

### CONTRADICTION

Two English surfaces can use similar words but require different contracts:

- `Record saved.` — confirmed persistence.
- `Saved filter.` — could name an object rather than report an event.
- `Saved locally.` — persistence scope differs.

String similarity is not semantic equivalence.

---

## 3. One product event may need multiple surface realizations

### SYNTHESIS

Reusing the exact same sentence everywhere is not semantic consistency. Consistency means preserving the same truth while adapting information density and grammar to the surface.

Fixed hypothetical event: authoritative save confirmation for one record.

Possible realizations:
- form status: `Record saved.`
- compact history row: `Saved`
- activity item: `Record saved` + timestamp supplied structurally
- notification, only if notification is justified: object + result + relevant next action

All derive from the same confirmed-save contract. They need not share one literal string key.

### REJECT

- copying a toast sentence into a button label;
- using one `saved` token for event, adjective, noun category and status;
- forcing every surface to include the same amount of context;
- omitting consequence on a high-consequence surface merely because a compact surface omits it.

---

## 4. Cross-surface transfer matrix

| Contract | Form | Inline status | Dialog | Empty/state view | Search/filter | Settings | Notification |
|---|---|---|---|---|---|---|---|
| object identity | usually local context | often needed | needed | needed | dimension/scope | setting name | needed |
| certainty | validation/pending | critical | critical | cause-dependent | result state | commit state | critical |
| consequence | point-of-decision | when material | before commit | sometimes | when constraint changes interpretation | often required | when material |
| recovery | field/action | explicit when blocked | explicit | state-specific | clear/change query/filter | revert/restore | deep link only if real |
| tone | neutral/helpful | restrained | risk-modulated | context-dependent | functional | functional | especially restrained |
| variables | field value | object/count | object/count | scope/query/count | query/filter/count | value/default | object/time/value |

### STUDIO JUDGMENT

Surface-specific omission is allowed only when the omitted meaning is reliably available from structure/context and omission does not change the user's interpretation or decision.

---

## 5. Forms transfer

CD010 form content already separates stable label, accepted input, requiredness, guidance, validation and repair. CD016 adds localization transfer requirements:

- label and validation are separate messages;
- placeholder is not the canonical label;
- accepted-format examples are data/locale aware;
- field names are not concatenated into generic English error templates when grammar may require inflection/reordering;
- required/optional status is semantic metadata, not punctuation alone;
- dates, numbers, currencies and units use locale-aware formatting while preserving literal professional identifiers where required.

### REJECT

`{fieldName} is invalid` as the only architecture for all validation simply because it is convenient in English.

---

## 6. Lifecycle-state transfer

CD011–CD012 states remain non-collapsible across locales:

- loading ≠ pending;
- authoritative failure ≠ outcome unknown;
- no data ≠ no match ≠ unavailable;
- confirmed success ≠ optimistic assumption;
- retry ≠ verify/reconcile.

### Critical localization rule

Do not allow a translation catalog to collapse semantic keys because two English source strings happen to be identical today. Separate keys preserve future differences in grammar, context, tone and behavior.

Example classes:
- `empty.first_use.records`
- `empty.filter.records`
- `empty.search.records`
- `unavailable.records.offline`
- `pending.record.save`
- `failure.record.save.confirmed`
- `unknown.record.save.outcome`
- `success.record.save`

---

## 7. Onboarding transfer

CD013's decision-relative disclosure timing is semantic, not English-specific. Localization must preserve:

- what must be known before a decision;
- what can be deferred;
- skip/resume/re-entry meaning;
- progress truth;
- product-delta explanations for domain experts.

### CONTRADICTION

A localized string that expands beyond a tutorial card is not evidence that the instruction should be deleted. The architecture must first consider reflow, sequencing, alternate surface, or decomposition without moving consequence-critical information after the decision it governs.

---

## 8. Search/filter/sort/settings transfer

CD014 requires retrieval semantics to remain structured:

- query scope;
- searchable fields;
- filter dimension;
- operator;
- machine value;
- localized value label;
- combination semantics;
- sort field;
- sort direction;
- setting scope;
- default source;
- persistence.

### REJECT — English concatenation

Do not build phrases from fragments such as:
`Sort by` + `{field}` + `ascending`
or
`No` + `{object plural}` + `found`.

Locale grammar must be able to reorder or replace the entire proposition.

### Literal-data boundary

Flight numbers, registrations, airport codes, tickers and other professional identifiers may need to remain literal even when surrounding grammar, number/date formatting or directionality changes. Their treatment is a data contract, not a translator preference.

---

## 9. Voice/tone transfer

CD015 established that personality yields to truth, consequence, recovery and real urgency. CD016 extends this to localization:

### Rule

Translate the **communication intent and tone constraints**, not personality tokens word-for-word.

Localizer context should distinguish:
- routine confirmation;
- warning before reversible action;
- irreversible consequence;
- service failure;
- user-correctable validation;
- outcome unknown;
- meaningful milestone.

### REJECT

- forcing jokes/idioms to preserve an English brand phrase;
- literal translation of apology frequency;
- translating urgency words without the underlying urgency contract;
- adding celebration to routine professional actions because the target-language marketing voice prefers enthusiasm.

---

## 10. Variables, pluralization, selection and formatting

### STUDIO MODEL

Variables are typed semantic inputs, not arbitrary string replacements.

Possible types:
- user-entered literal;
- professional identifier;
- localized object name;
- count;
- currency amount;
- date/time;
- duration;
- percentage;
- unit-bearing quantity;
- enum/domain value;
- product-generated title/name.

Each type needs a formatting/escaping/bidi/context policy.

### Plural/count rule

Do not encode English `count == 1 ? singular : plural` as the universal language model. Locale-aware message selection belongs to the internationalization layer.

### Numeric rule

Display localization and domain meaning are separate. A currency amount may require localized number formatting while the currency code/symbol and accounting meaning remain explicit. Professional identifiers must not be silently reformatted as ordinary numbers.

---

## 11. Bidirectional-text and literal identifier preparation

### TRANSFER VALIDATION PREPARATION

Future RTL transfer must explicitly test mixed-direction strings containing:
- Latin flight numbers;
- registrations;
- airport codes;
- tickers;
- dates/times;
- signed values;
- currency symbols/codes;
- punctuation around variables.

CD016 does not claim bidi correctness without an executable specimen. It establishes the requirement that literal-data boundaries be represented so the runtime can apply appropriate isolation/directionality mechanisms.

---

## 12. Pseudo-localization as engineering evidence, not linguistic evidence

### STUDIO JUDGMENT

Pseudo-localization can expose:
- hard-coded strings;
- clipping/truncation;
- fixed-width assumptions;
- concatenated fragments;
- missing externalization;
- fragile variable boundaries;
- some bidi/layout failures.

It cannot prove:
- translation quality;
- cultural appropriateness;
- terminology acceptance;
- naturalness;
- human comprehension.

Therefore pseudo-localization belongs to production-transfer verification, not human-language PASS.

---

## 13. Cross-surface practice — one semantic contract

Hypothetical professional-record save with ambiguous network outcome.

### Product truth
- user submitted one record;
- local request was issued;
- authoritative persistence cannot currently be confirmed;
- duplicate retry may be unsafe;
- verification/reconciliation is the valid recovery.

### Form/status realization
`We couldn’t confirm whether the record was saved.`
Recovery: verify/reconcile if the product provides that action.

### Compact activity realization
`Save not confirmed`
Only valid where record identity and recovery are structurally adjacent.

### Notification realization
A notification should exist only if the product has a legitimate asynchronous reason to notify. If used, it must preserve uncertainty; it must not become `Save failed` merely for brevity.

### CONTRADICTION TEST

If a compact surface cannot fit the certainty distinction, the solution is not to change `outcome unknown` into `failure`. Recompose the surface, provide structural context, or use a less compact treatment.

---

## 14. Semantic integrity audit v0.1

Flag:
- `STRING_AS_STATE`
- `SHARED_KEY_FALSE_EQUIVALENCE`
- `ENGLISH_CONCATENATION_LOGIC`
- `SURFACE_COPY_PASTE`
- `CONTEXT_LOSS_ON_COMPACT_SURFACE`
- `CERTAINTY_LOST_IN_TRANSFER`
- `CONSEQUENCE_LOST_IN_TRANSFER`
- `RECOVERY_LOST_IN_TRANSFER`
- `CRITICAL_COPY_DELETED_FOR_EXPANSION`
- `UNTYPED_VARIABLE`
- `IDENTIFIER_REFORMATTED_AS_NUMBER`
- `ENGLISH_BINARY_PLURAL_LOGIC`
- `MISSING_LOCALIZER_CONTEXT`
- `TONE_TOKEN_LITERALISM`
- `RTL_LITERAL_BOUNDARY_UNMODELED`
- `PSEUDOLOCALIZATION_OVERCLAIM`
- `HUMAN_VALIDATION_NEEDED`
- `RUNTIME_TRANSFER_NEEDED`

---

## 15. KEEP / REWORK / REJECT

### KEEP
- product truth → semantic contract → locale realization → surface realization → runtime hierarchy;
- state selects message, never reverse;
- typed variables and literal-data boundaries;
- separate keys for semantically distinct states even when English strings coincide;
- surface adaptation with semantic invariants;
- decision-relative onboarding information preserved through localization;
- tone intent/context rather than word-for-word personality transfer.

### REWORK
- exact message-format technology in Stage 3/production practice;
- real pseudo-localization harness;
- actual RTL/bidi isolation;
- native/web string-resource architecture;
- translator workflow, screenshots/context tooling and terminology QA;
- live MintTap/LogMate contracts once implementation truth is available.

### REJECT
- one English string as both UI and application state;
- universal fragment concatenation;
- deleting meaning to satisfy English-sized geometry;
- one literal sentence reused across unrelated surfaces;
- translation success inferred from externalized strings;
- pseudo-localization treated as proof of linguistic quality.

---

## Stage 2 implication

CD016 integrates the previously separate Stage 2 systems and demonstrates a coherent localization-ready semantic architecture at specification/practice level. The major remaining Stage 2 gap is now an **integrated multiple-solution capstone** that applies forms, lifecycle states, onboarding, retrieval/configuration, voice/tone and localization transfer to one fixed professional-product problem and critiques materially different complete content systems.

Stage 2 remains **PRACTICE / NOT PASSED** until that capstone and a separate closure audit satisfy the explicit gate.

## OPEN

- executable message-format and pseudo-localization transfer;
- real RTL/bidi specimen;
- production translator/localization workflow;
- native/web resource and fallback behavior;
- live-project semantic contracts;
- screen-reader/AT behavior across locales;
- human comprehension and terminology validation by locale/domain;
- telemetry linking localized state/recovery content to task outcomes.

## HANDOFFS

### Type
Use CD016 typed variables, literal identifiers, long state propositions and pseudo-localized expansion as future rendering stress. Never request semantic deletion solely to preserve a preferred line count.

### Layout / Interaction
Expose state, scope, persistence, certainty, recovery and decision timing as machine-readable product truth so Content does not infer them from strings.

### Web
Future transfer should verify message loading/fallback, dynamic announcements, URL/state restoration, pseudo-localized reflow, bidi literals, zoom/text expansion and failure behavior.

### Color
Status identity and consequence must survive color removal in every locale/surface.

## Evidence level

**CROSS-SURFACE SYSTEM SYNTHESIS + PEER TRANSFER + CONTRADICTION TESTS + LOCALIZATION-TRANSFER ARCHITECTURE + PRODUCTION-VALIDATION PLAN. No production localization, RTL, AT, human, or live-product PASS claimed.**
