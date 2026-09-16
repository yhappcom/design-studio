# CD015 — Voice & Tone as Controlled Functional Modulation

Status: **STAGE 2 PRACTICE — SYSTEM MODEL + CROSS-STATE COMPARATIVE PRACTICE / NOT PASSED**  
Date: 2026-09-16

## Question

How should an English-first global product preserve a coherent voice while modulating tone across routine work, warnings, failures, uncertainty, consequential actions and meaningful success—without allowing personality to distort product truth, patronize professional users, or damage localization/accessibility?

This study treats voice/tone as a constrained product system, not an adjective list or marketing exercise.

## RELATED DOMAIN CHECK

### Type
Necessary wording and semantic distinctions remain primary. Tone is not permission to shorten consequential language to fit one line or weak geometry. Professional identifiers remain literal operational content.

### Color
Color can reinforce urgency/severity but does not determine tone. A calm sentence paired with a danger color does not repair semantic understatement; expressive copy paired with neutral color does not create a valid warning hierarchy.

### Layout / Interaction
Interaction owns consequence, reversibility, certainty, agency, timing and recovery. These are inputs to tone modulation. Content must not manufacture urgency or reassurance that the state machine cannot justify.

### Web
Runtime delivery changes perceived force: persistent banner, inline field message, modal interruption, toast and live announcement are not tone-neutral. Web/native transfer must test the combined content + presentation effect.

### Content
CD001–CD014 supply semantic fidelity, plain language, action/state/consequence, global English, forms, state taxonomy, lifecycle, onboarding and retrieval/configuration contracts. CD015 adds controlled expressive modulation only after those functional contracts exist.

### External evidence
Current Microsoft Writing Style guidance distinguishes relatively stable voice from context-sensitive tone and emphasizes getting to the point, clear action and concise human language. Microsoft global-writing guidance recommends conventional grammar, simple sentence structures and consistent terminology to support localization/machine translation. W3C cognitive-accessibility guidance emphasizes clear/common words, short/simple sentences, literal/unambiguous content and clear instructions/error messages. These support clarity and context-sensitive modulation; they do not prove one brand personality or exact wording is universally optimal.

Overlap classification: **SYSTEM EXTENSION + ACCESSIBILITY/LOCALIZATION TRANSFER + CROSS-STATE CONTRADICTION REVIEW**.

---

## 1. Voice and tone are different layers

### SYNTHESIS

**Voice** is the relatively stable linguistic character of the product across contexts.  
**Tone** is controlled contextual modulation of that voice in response to the task/state and the user's situation.

### STUDIO MODEL

Stable voice constraints for an English-first professional product should be expressed as operational rules rather than adjectives alone:

- semantic truth before personality;
- direct before decorative;
- specific before generic;
- respectful of existing domain expertise;
- consistent terminology;
- calibrated claims rather than certainty theater;
- useful action before reassurance;
- globally intelligible source English;
- no dependence on jokes, idioms or cultural references for meaning.

A brand may later choose warmer, more formal or more energetic expression, but it must remain inside these functional constraints.

### CONTRADICTION

`Friendly` is not a sufficient voice rule. It does not tell a writer whether `Oops!` is acceptable after lost work, whether humor belongs in a safety warning, or whether a routine save needs praise.

---

## 2. Tone modulation requires state inputs

### STUDIO MODEL — modulation vector

Before writing, classify:

1. **Consequence** — trivial / recoverable / consequential / potentially irreversible.
2. **Urgency** — none / time-sensitive / immediate action required.
3. **Certainty** — known / probabilistic / unknown outcome.
4. **User agency** — can act now / can wait / cannot self-recover.
5. **Reversibility** — easy / costly / unavailable / unknown.
6. **Responsibility** — user-correctable / product-service / external / mixed / unknown.
7. **Emotional load** — routine / frustrating / potentially stressful or sensitive.
8. **Frequency** — routine repeated / occasional / exceptional milestone.
9. **Domain criticality** — convenience / financial-operational / safety-regulatory or other high-consequence context.
10. **Audience expertise** — product novice/expert and domain novice/expert separately.

Tone is a function of these variables, not a lookup from component color.

---

## 3. Functional priority ordering

For consequential UI copy, optimize in this order:

1. truth/certainty;
2. consequence/scope;
3. required or available action;
4. preserved data/intent when material;
5. timing/urgency when real;
6. concise explanatory context;
7. personality/brand expression.

### STUDIO JUDGMENT

When personality conflicts with an earlier item, personality loses.

This is the core CD015 constraint.

---

## 4. Tone matrix by state

| State | Tone target | Avoid |
|---|---|---|
| routine action | compact, neutral, task-forward | praise/noise after every action |
| low-risk validation | direct, specific, repair-focused | blame, scolding, vague `Invalid` |
| warning | explicit, sober, consequence-first | playful hedging, generic `Are you sure?` |
| destructive/irreversible | restrained, precise, scope + consequence | humor, euphemism, urgency without basis |
| known system failure | factual, supportive through recovery | blaming user, theatrical apology |
| outcome unknown | calibrated uncertainty | false failure/success, false reassurance |
| waiting/pending | calm, status-specific | unsupported time promises |
| offline/degraded | factual about availability/freshness | false absence, melodrama |
| routine success | proportional confirmation | `Awesome!`, `Great job!` by default |
| meaningful milestone | warmer expression may be justified | forcing celebration on routine work |
| permission/business block | objective, next-step oriented | moralizing or implying incompetence |

The matrix constrains direction; it does not prescribe one sentence.

---

## 5. Professional users: respect is not formality

### SYNTHESIS

A professional product can use plain language without sounding simplistic. Domain expertise should not be confused with preference for bureaucratic prose.

### STUDIO JUDGMENT

For pilots, investors, clinicians, engineers or other specialist audiences:

- retain established domain terms when they are the precise shared vocabulary;
- do not replace precise professional terms with vague everyday synonyms merely to sound casual;
- do not reteach obvious domain concepts unless the product introduces a nonstandard meaning;
- explain product-specific behavior, ambiguity or consequences;
- avoid congratulatory coaching for routine expert work;
- distinguish product novice from domain novice.

Example:

Weak professional tone: `Great job! You successfully added your flight!`  
Stronger functional direction: `Flight added.`

But a major completed import/migration may justify more explanation because the consequence and next state are not self-evident.

---

## 6. Error language: empathy is not apology volume

### SOURCE/SYNTHESIS

Microsoft guidance emphasizes helpful alternatives and avoids blame; W3C guidance emphasizes clear, actionable error information. CD010–CD012 already establish specific repair and state truth.

### STUDIO JUDGMENT

Empathy in product language is primarily demonstrated by:

- preserving the user's work;
- explaining what happened accurately;
- giving a real recovery path;
- not blaming the user for service failures;
- not making the user repeat unnecessary work;
- acknowledging uncertainty when uncertainty exists.

`We're so sorry!` does not compensate for missing recovery.

Apology can be appropriate when the product/service caused meaningful disruption, but it should not displace the fact/action contract.

### REJECT

- apology as the only useful information;
- emotional language that overstates a minor inconvenience;
- minimizing a serious loss with cheerful language;
- `You did something wrong` framing for neutral validation;
- anthropomorphic excuses for system behavior.

---

## 7. Warning tone: consequence beats fear

Warnings should make the decision legible, not make the product sound alarmed.

### Comparative practice

Fixed truth: deleting 12 imported records is irreversible.

A — theatrical: `Warning! This is a dangerous action! Are you absolutely sure?`  
**REJECT:** high affect, low information.

B — casual: `Remove these? You can always add them again later.`  
**REJECT** if restoration is not guaranteed; minimizes consequence.

C — consequence-led: `Delete 12 imported records? This removes them from this logbook. You can't undo this action.`  
**KEEP as architecture** if the product truth is accurate.

The useful seriousness comes from explicit scope/reversibility, not exclamation marks.

---

## 8. Uncertainty requires calibrated language

CD011 distinguishes known failure from outcome unknown. Tone must preserve this epistemic boundary.

Known failure: `The record wasn't saved. Your entries are still here.`  
Unknown outcome: `We couldn't confirm whether the record was saved.`

### STUDIO JUDGMENT

Do not soften uncertainty into reassurance such as `Don't worry—your record is probably safe` unless the product has evidence and such probability communication is appropriate.

Do not intensify uncertainty into `Save failed` merely to sound decisive.

Calibrated uncertainty is part of trustworthy tone.

---

## 9. Success and celebration need proportionality

### Success ladder

- invisible/self-evident completion → no extra copy;
- routine consequential confirmation → concise factual result;
- non-obvious result → result + consequence;
- meaningful user milestone → optional warmer recognition;
- exceptional achievement → richer celebration only if culturally/product appropriate.

### CONTRADICTION

A uniformly enthusiastic voice can reduce signal quality: if every save is `Amazing!`, genuine milestones lose differentiation and professional workflows accumulate noise.

### STUDIO JUDGMENT

Celebration is an information-hierarchy resource. Spend it selectively.

---

## 10. Urgency must be evidence-backed

Urgency language (`now`, `immediately`, `required`, countdowns, `urgent`) changes decision pressure.

Only use it when the underlying timing constraint exists and matters.

Reject:

- urgency for engagement/marketing inside functional workflows;
- `Act now` when no deadline exists;
- countdown language that does not map to an actual deadline;
- `Required` for optional configuration.

Professional tools particularly need separation between operational urgency and product-engagement urgency.

---

## 11. Humor, idiom and anthropomorphism boundary

### STUDIO JUDGMENT

Humor/idiom can be considered only when:

- the state is low consequence;
- meaning remains complete without the joke;
- repetition will not become irritating;
- localization can replace rather than literally translate it;
- it does not trivialize frustration or loss;
- it does not create false system agency.

Avoid as default in warnings, data loss, financial consequences, permission blocks, uncertain outcomes, safety/regulatory contexts and accessibility-critical instructions.

Examples of source-English risk:
- `Hang tight`;
- `Oops`;
- `We hit a snag`;
- `You're all set` when actual readiness is partial;
- product anthropomorphism such as `I couldn't find your flights` unless a deliberate conversational-agent contract exists.

---

## 12. Global English and localization-ready tone

### SOURCE TRANSFER

Microsoft global-writing guidance favors conventional grammar, simple structures and consistent terminology to support localization/machine translation. W3C cognitive guidance favors literal, common and unambiguous language.

### STUDIO RULES

- semantic proposition survives removal of personality words;
- avoid idiom as state information;
- avoid sarcasm/irony;
- keep terminology stable across tone states;
- avoid synonym variation purely for stylistic freshness;
- do not encode politeness through fragile English word order or fragments;
- allow locale teams to adapt warmth/politeness without changing consequence, certainty, agency or recovery;
- provide localizer metadata for state, severity, audience, consequence and variable meaning;
- separate brand-expression guidance from semantic string keys.

### TRANSFER VALIDATION

Later locale transfer should test whether translators can preserve the same functional proposition while adapting culturally appropriate politeness/formality. Korean may be one such later transfer locale but is not the universal reference model.

---

## 13. Voice invariants vs tone variables

### Voice invariants v0.1

Always preserve:

- truthful certainty;
- domain terminology consistency;
- user-respecting agency;
- explicit material consequence;
- actionable recovery where available;
- plain/global English architecture;
- non-blaming system-failure framing;
- no unsupported promise.

### Tone variables v0.1

May change:

- sentence compression;
- warmth;
- degree of acknowledgement;
- salience/explicitness;
- formality within product bounds;
- amount of context;
- celebration;
- urgency language when evidence-backed.

This separation makes voice governance testable.

---

## 14. Tone contract schema v0.1

For a consequential string/pattern record:

- `state_class`
- `object`
- `known_fact`
- `certainty`
- `consequence_level`
- `urgency_basis`
- `user_agency`
- `reversibility`
- `responsibility_class`
- `preserved_work`
- `recovery`
- `domain_criticality`
- `audience_domain_expertise`
- `audience_product_expertise`
- `voice_invariants`
- `allowed_tone_range`
- `disallowed_expressions`
- `localizer_context`
- `runtime_surface`

Tone review should inspect this contract before editing surface wording.

---

## 15. Cross-state comparative practice

Fixed professional-record product; same voice invariants, different state truth.

### Routine save
`Record saved.`

### Validation
`Enter the aircraft registration.`

### Known failure
`The record wasn't saved. Your entries are still here.`

### Unknown outcome
`We couldn't confirm whether the record was saved.`

### Destructive warning
`Delete 12 imported records? This removes them from this logbook. You can't undo this action.`

### Pending
`Saving record…`

### First-use empty
`No flight records yet.` + real create/import path if available.

### Meaningful import completion
`128 records imported.` Add conflict/duplicate summary when materially relevant rather than generic praise.

### RESULT

Coherence does not require identical emotional intensity. It requires the same truthfulness, terminology, agency and clarity rules while tone adapts to consequence/certainty.

---

## 16. Audit taxonomy v0.1

Flag:

- `PERSONALITY_BEFORE_TRUTH`
- `TONE_STATE_MISMATCH`
- `FALSE_REASSURANCE`
- `UNSUPPORTED_URGENCY`
- `BLAME_SHIFT`
- `APOLOGY_WITHOUT_RECOVERY`
- `CHEERFUL_DATA_LOSS`
- `ROUTINE_OVERCELEBRATION`
- `EXPERT_PATRONIZING`
- `DOMAIN_TERM_DILUTION`
- `IDIOM_AS_INFORMATION`
- `HUMOR_HIGH_CONSEQUENCE`
- `ANTHROPOMORPHIC_FALSE_AGENCY`
- `UNCERTAINTY_ERASURE`
- `STYLE_SYNONYM_TERMINOLOGY_DRIFT`
- `LOCALIZATION_FRAGILITY`
- `RUNTIME_FORCE_UNCHECKED`
- `HUMAN_VALIDATION_NEEDED`

The audit identifies system defects; it does not measure trust, emotional response, perceived warmth or preference.

---

## 17. KEEP / REWORK / REJECT

### KEEP

- stable voice invariants + variable tone;
- modulation from consequence/urgency/certainty/agency/reversibility/responsibility;
- professional plain language without domain dilution;
- proportional success/celebration;
- consequence-led warning language;
- calibrated uncertainty;
- localization-ready semantic core.

### REWORK

- actual brand-expression range for each live product;
- exact warmth/formality across markets;
- high-stakes domain-specific warning thresholds;
- native/web runtime force and announcement behavior;
- locale transfer with professional terminology corpora.

### REJECT

- adjective-only voice charts;
- one tone for every state;
- `friendly` as permission for humor everywhere;
- apology as recovery;
- enthusiasm as success semantics;
- urgency without a timing contract;
- personality overriding certainty or consequence;
- casual synonym churn in professional terminology.

---

## Stage 2 implication

CD015 closes the major voice/tone-system gap in the Stage 2 map. It adds a reusable model rather than a product-specific brand voice. Stage 2 remains **PRACTICE / NOT PASSED** because broader localization-ready cross-surface transfer and an integrated multiple-solution Stage 2 capstone remain required before closure audit.

## OPEN

- live LogMate/MintTap brand-expression ranges;
- actual high-consequence domain thresholds and terminology review;
- locale-specific politeness/formality transfer;
- browser/native surface-force interaction;
- human trust, comprehension, emotional response and preference;
- production telemetry relating tone variants to recovery/task outcomes without reducing content quality to engagement metrics.

## HANDOFFS TO OTHER SPECIALISTS

### Type
Use real warning/failure/uncertainty strings as wrapping and hierarchy stress. Do not compress away consequence to fit typography.

### Color
Severity and tone are independent channels; test whether semantic seriousness survives color removal and whether visual intensity contradicts wording.

### Layout / Interaction
Provide consequence/certainty/agency/reversibility truth before tone review. Modal interruption or destructive confirmation cannot be decided by wording alone.

### Web
Transfer identical semantic content across inline, banner, toast/dialog and live-status contexts to test whether runtime presentation changes perceived force or accessibility behavior.

## Evidence level

**CURRENT AUTHORITATIVE-GUIDANCE CHECK + PEER-EVIDENCE TRANSFER + SYSTEM SYNTHESIS + CROSS-STATE COMPARATIVE PRACTICE + CONTRADICTION TEST + AUDIT TAXONOMY. No human, locale, production-brand or runtime PASS claimed.**
