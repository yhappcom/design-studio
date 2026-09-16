# CD002 — User Needs, Mental Models, Terminology and Naming

Status: **FOUNDATION — SOURCE STUDY + SYNTHESIS + ORIGINAL TERMINOLOGY PRACTICE / NOT A PASS CLAIM**  
Date: 2026-09-16

## Research question

How should Content Design connect a user's task and existing knowledge to the product's concepts without oversimplifying expert terminology, inventing unsupported mental models, or allowing inconsistent labels to distort the interface?

This study extends CD001 from the semantic truth of one message to the larger problem of **concept formation and terminology systems**.

CD001 established that wording must preserve the real object, state, available action and consequence. CD002 asks what must happen one layer earlier:

> Before choosing a label, what concept is being named, whose task does it serve, what evidence exists about the user's language, and how consistently must the designation survive across the product?

The goal is not to create a style-guide word list. It is to establish a defensible foundation for later labels, forms, errors, onboarding, search, settings and professional-domain products.

---

## 1. Sources and evidence roles

### SOURCE — GOV.UK: user needs are task/outcome based, not solution labels

GOV.UK defines user needs around what people need to do or achieve, and explicitly warns against writing needs as proposed solutions. Its guidance recommends evidence from user research, analytics, support data and prior research and says user needs should be written in language users would recognize and use themselves.

Sources:
- GOV.UK — Identify user needs  
  https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/plan-manage-content/identify-user-needs/
- GOV.UK Service Manual — Learning about users and their needs  
  https://www.gov.uk/service-manual/user-research/start-by-learning-user-needs

Implication:
- `I need an export button` is not yet a stable user need.
- `I need to take my records into another system so that I can continue my work elsewhere` is closer to a task/outcome statement and leaves implementation options open.

This matters to naming because labels should not be derived only from the implementation team's feature vocabulary.

### SOURCE — GOV.UK: use user language, including for specialist users

GOV.UK's interface-writing guidance recommends using the same language as users, choosing intuitive service names, minimizing unnecessary reading and avoiding explanations that compensate for a confusing interface. It also states that specialist users still benefit from clear language.

Source:
- GOV.UK Service Manual — Writing for user interfaces  
  https://www.gov.uk/service-manual/design/writing-for-user-interfaces

Evidence limit:
- this does not prove that every specialist term should be replaced with a general-language synonym;
- it supports clarity and user-recognizable language, not terminology flattening.

### SOURCE — ISO 9241-110: task suitability, self-descriptiveness and conformity with expectations

ISO 9241-110 identifies interaction principles including suitability for the user's task, self-descriptiveness, conformity with user expectations and learnability. Its public preview states that behavior should be predictable from context and accepted conventions and that the system should expose enough information for capabilities and use to be apparent without unnecessary interaction.

Source:
- ISO 9241-110 — Ergonomics of human-system interaction — Interaction principles  
  https://www.iso.org/obp/ui?_escaped_fragment_=iso%3Astd%3Aiso%3A9241%3A-110%3Adis%3Aed-2%3Av1%3Aen

Content consequence:
- naming is not merely linguistic consistency; it contributes to predictability, discoverability and learnability.

### SOURCE — Norman: design model, system image and user's model are distinct

Don Norman's description of conceptual models distinguishes:
- the designer's model;
- the system image presented by the product;
- the user's model formed from interaction with that system image.

The designer does not directly place a model in the user's head. The product and its communication mediate that relationship.

Source:
- Don Norman, “Design as Communication”  
  https://jnd.org/design-as-communication/

Historical source referenced there:
- Norman & Draper, *User Centered System Design* (1986).

Content consequence:
- interface language is part of the **system image**;
- terms, labels, instructions and state messages can reinforce or distort the conceptual model conveyed by the product;
- “match the user's mental model” is too crude if no evidence exists about what users actually believe.

### SOURCE — HCI research: “mental model” is useful but conceptually variable

Hu and Twidale's 2023 scoping review of HCI mental-model research reports broad diversity in definitions, purposes and methods and explicitly notes that the term is used inconsistently across HCI research.

Source:
- Xinhui Hu & Michael Twidale (2023), *A Scoping Review of Mental Model Research in HCI from 2010 to 2021*  
  DOI: 10.1007/978-3-031-48038-6_7
- University of Illinois publication record:  
  https://experts.illinois.edu/en/publications/a-scoping-review-of-mental-model-research-in-hci-from-2010-to-202/

Evidence role:
- **CONCEPTUAL CAUTION**, not a content-writing rule.

Studio consequence:
- do not use “mental model” as an unmeasured explanation for why a label is supposedly intuitive;
- when evidence exists, specify what was actually observed: terminology used, grouping behavior, predictions, task strategy, navigation expectation, causal explanation, etc.

### SOURCE — ISO terminology standards: concept and designation are not the same thing

ISO 704:2022 establishes terminology-work principles around relationships among objects, concepts, definitions and designations. ISO terminology vocabulary defines a concept independently from the linguistic designation used to represent it.

Sources:
- ISO 704:2022 — Terminology work — Principles and methods  
  https://www.iso.org/standard/79077.html
- ISO Online Browsing Platform material using ISO 1087 terminology definitions  
  https://www.iso.org/obp/

Reusable distinction:
- **concept**: the unit of knowledge being distinguished;
- **designation/term/name**: a sign or linguistic expression used to represent a concept or object.

Content consequence:
- changing a label does not necessarily change the underlying concept;
- using one label for multiple distinct concepts can hide structural ambiguity;
- using many labels for one concept can create unnecessary relearning unless the variation is deliberate and contextual.

### SOURCE — W3C: consistent identification and clear labels reduce avoidable ambiguity

WCAG 2.2 Success Criterion 3.2.4 requires components with the same functionality to be identified consistently across a set of pages. W3C's supporting material explains that inconsistent labels for identical functions make interfaces harder to predict and can increase cognitive load.

W3C cognitive-accessibility guidance additionally recommends clear visible labels, common/familiar terms and consistent conventional patterns while explicitly noting that human usability claims still require appropriate user testing.

Sources:
- W3C — Understanding SC 3.2.4 Consistent Identification  
  https://www.w3.org/WAI/WCAG22/Understanding/consistent-identification.html
- W3C — G197: Using labels, names, and text alternatives consistently  
  https://www.w3.org/WAI/WCAG22/Techniques/general/G197
- W3C — Use Clear Visible Labels  
  https://www.w3.org/WAI/WCAG2/supplemental/patterns/o4p06-clear-labels/
- W3C — Use Clear Words  
  https://www.w3.org/WAI/WCAG2/supplemental/patterns/o3p01-clear-words/

Important boundary:
- WCAG 3.2.4 is about consistent identification of repeated functionality, not a universal demand that every similar-looking thing receive the same wording.
- different functions or concepts may require different labels even when visual similarity is high.

### SOURCE — Microsoft: familiar words and audience knowledge constrain terminology choice

Microsoft's current style guidance advises against giving common words unusual new meanings and recommends understanding the audience before using industry-specific terminology. If a specialized meaning is necessary for a general audience, it should be explained in context.

Source:
- Microsoft Style Guide — Don't use common words in new ways  
  https://learn.microsoft.com/en-us/style-guide/word-choice/dont-use-common-words-in-new-ways

Content consequence:
- product-created neologisms and implementation metaphors are not neutral; they impose learning cost;
- domain-native vocabulary can be valid when the target audience genuinely uses it and the term carries useful precision.

---

## 2. Foundation correction — “mental model” is not a synonym for “familiar wording”

### SYNTHESIS

A user can recognize a familiar word while still misunderstanding the product's structure or consequences. Conversely, an expert may correctly understand a specialized term that is unfamiliar to a general audience.

Therefore these are separate questions:

1. **User need** — what outcome or task is the person trying to achieve?
2. **Domain concept** — what thing, state, relation or action actually exists in the product/domain?
3. **User knowledge/model evidence** — what does the intended audience already appear to know, expect, group or predict?
4. **Designation** — what term or label should represent that concept here?
5. **System consistency** — does the same concept/function remain recognizable across surfaces and states?

Using “mental model” to skip questions 1–5 produces weak analysis.

### STUDIO JUDGMENT

Content Design will not write claims such as:

> “Users expect this to be called X because it matches their mental model.”

unless evidence establishes what was actually observed.

Prefer statements such as:

> “In five research sessions, participants consistently called this workflow a ‘reconciliation’ task and distinguished it from ‘review’; this supports preserving that terminology for this audience.”

or, when no user evidence exists:

> “`Reconciliation` is the current domain term from the product specification. User recognition is untested.”

This preserves evidence boundaries.

---

## 3. Concept first, label second

### SYNTHESIS from ISO terminology work + HCI/content guidance

A robust terminology decision starts by separating the concept from the word used to represent it.

Example:

- concept: one source file selected by the user;
- concept: one processing event that may create many records;
- concept: one resulting record;
- concept: one suspected duplicate pair requiring review.

If all four are casually called an “import,” the interface may appear concise while the product model becomes harder to explain.

### STUDIO JUDGMENT — terminology diagnostic

For every high-value product term, record at least:

1. **Concept** — what is it, independent of the preferred label?
2. **Boundary** — what nearby concept is it not?
3. **Audience/context** — who needs this distinction and in what task?
4. **Evidence** — user language, domain standard, product contract, analytics/support evidence, or currently only team convention?
5. **Preferred designation** — current user-facing term.
6. **Allowed variants** — abbreviations, locale variants, contextually shorter forms.
7. **Prohibited collisions** — terms that would merge distinct concepts.
8. **Cross-surface locations** — navigation, field, table, notification, help, accessibility name, export, etc.
9. **Localization note** — whether the concept has a stable equivalent or requires explanation in another language.
10. **Validation need** — semantic check only, expert-domain review, localization review, or actual user comprehension/task test.

This is a terminology record, not necessarily a UI artifact.

---

## 4. Default consistency rules — with exceptions

### Rule A — same concept/function → same designation by default

W3C provides a strong accessibility basis for consistently identifying repeated functionality. The broader Content rule is similar but must remain concept-aware.

Use one preferred term when:
- the same concept or function recurs;
- changing wording would create relearning or imply a false distinction;
- there is no contextual reason for a different grammatical form.

### Rule B — different concepts → different designations when the distinction matters to the task

Do not use one convenient word for states or objects whose differences affect:
- action eligibility;
- risk;
- ownership;
- persistence;
- recovery;
- financial/operational interpretation;
- auditability.

This directly extends CD001's rule against collapsing `pending`, `failed` and `unknown outcome` into one generic state label.

### Rule C — consistency does not mean mechanical sameness

A concept may legitimately have:
- a full term on first use;
- a recognized abbreviation after introduction;
- a shorter button label when surrounding context makes the object unambiguous;
- a locale-specific designation;
- a platform-conventional phrasing.

The requirement is **stable meaning and recoverable mapping**, not identical character strings everywhere.

### Rule D — vocabulary precision outranks generic “plainness” when expert meaning would be lost

Plain language is not “remove all jargon.”

A practical classification:

1. **Domain-native, task-critical term**  
   Keep when evidence shows the audience uses it and replacing it would lose precision.

2. **Organization/internal implementation term**  
   Translate unless the user genuinely needs the internal concept.

3. **Common word with a special product meaning**  
   High ambiguity risk. Prefer the common meaning or clearly define the specialized meaning.

4. **Product-created neologism**  
   Treat as a new learning burden. Justify, define and validate rather than assuming memorability.

5. **Abbreviation/acronym**  
   Keep when more recognizable than the expansion for the intended expert audience; otherwise introduce or explain it.

### OPEN

Whether a specific professional audience recognizes a specific term is an empirical question. Expert status does not allow the studio to assume vocabulary knowledge without evidence.

---

## 5. Common terminology failure modes

### 5.1 Implementation leakage

Backend or engineering names become user-facing because they already exist in code.

Failure:
- the term reflects storage/process implementation rather than the user's task.

Check:
- would the concept still be meaningful if the implementation changed?

### 5.2 Synonym drift

One concept becomes `record`, `entry`, `item`, `log` and `row` across different surfaces without deliberate rationale.

Failure:
- users must determine whether these are the same thing or different things.

Non-human check:
- terminology inventory can detect the drift even though it cannot prove user confusion.

### 5.3 False synonymy

Different concepts are intentionally made to sound the same for simplicity.

Example:
- `Upload`, `Import` and `Sync` all become `Add`.

Failure:
- distinct system consequences disappear from language.

### 5.4 Premature simplification of expert terms

A precise domain term is replaced with a friendly generic word.

Failure:
- familiar wording may become less precise for the intended professional audience.

### 5.5 Product neologism

A team invents a branded or clever label for a common function.

Failure risk:
- discoverability and transfer from prior experience decrease;
- accessibility/cognitive burden may increase;
- translation becomes harder.

### 5.6 Same label, different function

Two controls named `Save` perform materially different operations, such as:
- local draft save;
- publish to shared system.

Failure:
- the designation hides consequence differences.

### 5.7 Different label, same function

`Remove`, `Delete`, `Discard` and `Clear` are used interchangeably for exactly the same destructive operation.

Failure:
- unnecessary prediction/relearning cost;
- possible WCAG 3.2.4 issue in web contexts when the repeated functionality is identical.

---

## 6. RELATED DOMAIN CHECK

### Typography / Type

Evidence checked:
- `research/type/T017-logmate-operational-data-typography-semantic-geometry-transfer.md`
- current `progress/TYPE_STATUS.md`

Reusable finding:
- operational information roles must be defined by task/function rather than by visual appearance alone;
- real strings, identifier repertoires, abbreviations, numerals and punctuation materially affect Type/layout validation.

Content consequence:
- terminology decisions produce actual glyph/width/localization stress and cannot be treated as geometry-free.
- Type's current LogMate work also provides a useful future substrate for expert-domain terminology transfer, but CD002 does not claim aviation vocabulary correctness.

Relationship: **DIRECT REUSE / FUTURE TRANSFER OPPORTUNITY**.

### Color

Evidence checked:
- current `progress/COLOR_STATUS.md` and C017/C018 status summary.

Reusable finding:
- semantic roles should remain stable across alternate visual token strategies.

Content consequence:
- terminology should name the state/concept itself, not depend on a palette-specific nickname or visual color reference.

Relationship: **REUSE; no new Color test required in CD002**.

### Layout / Interaction

Evidence checked:
- CD001's direct reuse of I002/I004 state distinctions;
- current `progress/LAYOUT_STATUS.md`, especially the separation of task architecture, state, recovery and component contracts.

Reusable finding:
- system states and available actions are not interchangeable labels; they are behavioral contracts.

Content consequence:
- a terminology system must not merge concepts whose interaction behavior differs materially.

Relationship: **DIRECT DEPENDENCY**.

### Web Design

Evidence checked:
- current `progress/WEB_STATUS.md`;
- W016 finding that accessible role/name exposure and actual keyboard behavior are distinct contracts.

Reusable finding:
- names/labels in a browser exist together with programmatic accessibility names and actual control behavior.

Content consequence:
- later Web transfer must check visible label ↔ accessible name consistency and whether repeated functionality is named consistently in implemented pages.

Relationship: **TRANSFER VALIDATION LATER**.

### Existing Content evidence

Evidence checked:
- `CD001-language-as-interface-foundations.md`.

Reusable finding:
- object/state/action/consequence semantic fidelity precedes brevity/tone optimization.

CD002 extension:
- semantic fidelity also requires stable concept boundaries and designations across the product.

### Peer-domain search result

A repository-wide search did not reveal an existing canonical study dedicated to mental-model terminology governance or concept↔designation mapping. CD002 therefore fills a genuine Content-specific gap rather than duplicating peer ownership.

---

## 7. Original practice — controlled professional data-import terminology

This is a **synthetic professional-tool scenario**, not a claim about any live project's final vocabulary.

### Fixed product facts

The product contains these distinct concepts:

- **Source file** — the file selected by the user.
- **Import run** — one processing event performed on a source file.
- **Record** — one normalized data entry produced or updated by the import run.
- **Possible duplicate** — a comparison result indicating that two records may represent the same real-world event but require review.
- **Resolution choice** — the explicit action deciding which record representation to keep.

Assume that:
- one source file can contain many records;
- one import run can partially succeed;
- a possible duplicate is not itself a confirmed duplicate;
- resolving a possible duplicate changes stored record state.

### Candidate terminology system A — one-word simplification

- File: `Import`
- Processing event: `Import`
- Resulting records: `Imports`
- Duplicate review section: `Import issues`

#### Critique

Benefits:
- superficially small vocabulary.

Failures:
- merges object, event and output;
- makes statements such as `Import failed` ambiguous: file invalid, processing failed, or one record failed?
- `12 imports` could mean files, runs or records;
- makes later recovery/error content harder because concept boundaries are already lost.

Verdict: **REJECT** for semantic collision.

No human study is necessary to establish that the labels are unable to uniquely represent the fixed product facts. Human evidence would still be needed to compare the usability of valid alternative systems.

### Candidate terminology system B — concept-preserving

- Source object: `File`
- Processing event: `Import`
- Result object: `Record`
- Review state: `Possible duplicate`
- Review action: `Review duplicates`

#### Critique

Benefits:
- preserves separate object/event/result concepts;
- `Import completed with 3 records needing review` can be expressed without lexical collision;
- possible duplicate remains epistemically distinct from confirmed duplicate.

Risks:
- `Record` may be too generic in a real specialist domain;
- `Possible duplicate` may be longer than a domain-native term;
- actual audience vocabulary is unknown.

Verdict: **KEEP as semantic control**, not proven final wording.

### Candidate terminology system C — friendlier generic vocabulary

- Source object: `Document`
- Processing event: `Add data`
- Result object: `Item`
- Review state: `Match`
- Review action: `Fix matches`

#### Critique

Benefits:
- common words.

Failures/risks:
- `Document` is inaccurate if CSV/XLS/text files are supported and not perceived as documents;
- `Add data` hides replacement/update consequences;
- `Item` removes useful domain specificity;
- `Match` can imply confirmation even though the product knows only that a duplicate is possible;
- `Fix` presupposes an error when the system only requires review.

Verdict: **REJECT / REWORK**.

### Practice result

The exercise demonstrates three Foundation points:

1. vocabulary size minimization is not the same as conceptual simplicity;
2. common words can be semantically worse than specialized terms;
3. terminology quality can be partially validated against fixed product concepts before human testing.

What remains unproven:
- whether users prefer `Record` or a domain-specific alternative;
- whether `Possible duplicate` is understood efficiently;
- whether users naturally conceptualize the processing event as an `Import`;
- whether the labels improve task speed/error rate.

Those require audience/domain evidence.

---

## 8. Reproducible non-human terminology audit — version 0.1

CD002 introduces a bounded audit that can be run before human testing.

### Input

A list of user-facing strings plus a concept inventory and known product behavior.

### Checks

1. **Concept collision check**  
   Does one designation refer to two materially different concepts in the same task context?

2. **Synonym drift check**  
   Does one concept have multiple user-facing terms with no documented contextual reason?

3. **State/action boundary check**  
   Is a state noun being used as though it were an action, or an action label as though it guaranteed an outcome the system cannot guarantee?

4. **Internal-language check**  
   Is the label derived from implementation/storage/team vocabulary with no evidence that the user needs that concept?

5. **Expert-term evidence check**  
   If a specialized term is retained, what evidence establishes that the audience uses or requires it?

6. **Common-word-special-meaning check**  
   Has a familiar word been assigned a product-specific meaning that could conflict with its common meaning?

7. **Cross-surface consistency check**  
   Is the same concept/function recognizable in navigation, forms, tables, notifications, help and accessibility names?

8. **Unknown-evidence flag**  
   Which terminology judgments remain expert hypotheses rather than user-validated facts?

### Output categories

- `SEMANTIC PASS` — designation is consistent with the known product concept/contract;
- `COLLISION` — one term merges concepts that need distinction;
- `DRIFT` — one concept has unexplained multiple terms;
- `INTERNALISM` — internal implementation language leaks into user-facing copy without justification;
- `AUDIENCE EVIDENCE NEEDED` — expert/domain term may be appropriate but recognition is unverified;
- `LOCALIZATION REVIEW NEEDED` — concept/term mapping may not survive language transfer;
- `HUMAN VALIDATION NEEDED` — semantic candidates are all valid but comprehension/preference/task effect cannot be determined non-humanly.

### Evidence boundary

This audit can detect terminology-architecture defects relative to known product facts. It **cannot** measure:
- comprehension rate;
- recall;
- perceived clarity;
- preference;
- trust;
- task time;
- error rate.

Those remain human-study outcomes.

---

## 9. HANDOFFS TO OTHER SPECIALISTS

### Layout / Interaction

CD002 adds a linguistic rule to Interaction's semantic-contract model:
- if two concepts have different behavior, consequence or recovery, Content should not merge them under one convenience label unless the distinction is truly irrelevant in that context.

This **extends** rather than redefines Interaction ownership.

### Type

A terminology ledger can provide Type with realistic stress strings, abbreviations, capitalization, punctuation and multilingual equivalents earlier in product work. Type should not optimize a font/layout around placeholder copy if high-value terms are still unresolved.

### Web Design

Future Content→Web transfer should test:
- repeated function naming across routes/components;
- visible label ↔ accessible-name mapping;
- long/localized terminology in actual controls;
- terminology consistency across responsive variants.

### Color

State terminology should remain meaningful without color-specific references. If a state requires a verbal distinction, changing palette/theme must not alter that semantic distinction.

---

## 10. OPEN questions after CD002

1. Which research methods are best for eliciting expert-domain terminology without simply asking users what labels they “like”?
2. How should card sorting, tree testing, concept mapping, interview coding and corpus analysis be divided between Content, UX Research and IA responsibilities?
3. What is the best terminology-governance structure for bilingual Korean/English professional products?
4. When should an abbreviation become the preferred term rather than a shortened variant?
5. How should terminology systems represent partial synonymy, audience-specific terms and locale-specific non-equivalence?
6. How should a content system distinguish a conceptual term from its grammatical surface forms in strings?
7. What quantitative consistency checks are useful without overclaiming comprehension?
8. How should expert-domain terms be introduced for novice or occasional users without degrading expert efficiency?

---

## 11. Current conclusion

`SOURCE`:
- GOV.UK grounds content in evidenced user needs and user-recognizable language;
- ISO 9241-110 connects interaction quality to task suitability, self-descriptiveness and user expectations;
- Norman's conceptual-model framing separates design model, system image and user's model;
- HCI literature cautions that “mental model” is not one uniformly operationalized construct;
- ISO terminology work separates concepts from their designations;
- W3C requires consistent identification for repeated functionality and provides cognitive-accessibility guidance for clear labels;
- Microsoft cautions against giving familiar words unfamiliar product meanings without audience justification.

`SYNTHESIS`:
- the Content problem is not “find the simplest word.” It is **map the right concept to a recognizable designation for a specific audience and preserve that mapping across the product**.

`STUDIO JUDGMENT`:
- adopt a concept-first terminology record and the CD002 non-human terminology audit as provisional Content Foundation methods;
- use “mental model” only when the underlying observed/assumed representation is specified rather than as a generic intuition claim;
- treat precise expert vocabulary and plain language as compatible when the terminology is genuinely audience-native and task-critical.

`OPEN`:
- actual audience terminology, comprehension, efficiency and bilingual transfer remain empirical questions;
- no human evidence is claimed.

Stage 1 remains **IN STUDY / PRACTICE — NOT PASSED**.

Next recommended study: **CD003 — action labels, command grammar and consequence clarity**, building on CD001 object/state/action/consequence and CD002 concept/designation discipline.