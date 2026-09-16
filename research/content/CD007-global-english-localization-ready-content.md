# CD007 — Global English and Localization-Ready Content Architecture

Status: **FOUNDATION — SOURCE STUDY + INTERNATIONALIZATION TRANSFER + ORIGINAL PRACTICE / NOT A PASS CLAIM**  
Date: 2026-09-16

## Research question

How should an English-first app intended for global release write and structure its source content so that the English experience is clear on its own while the product remains localizable into other languages and regions without semantic drift, broken grammar, hidden platform assumptions or layout-driven rewriting?

This study supersedes the earlier plan to make Korean-specific transfer a Foundation blocker.

Design Studio product context is now explicit:

> **Default product language: English. Distribution target: global. Other locales are transfer/localization cases, not the primary source-language curriculum.**

Korean may be tested later because it is useful to the studio, but it is not privileged over other target locales in the Content curriculum.

---

## 1. Internationalization and localization are different contracts

### SOURCE — W3C Internationalization

W3C distinguishes:
- **internationalization (i18n):** design/development work that removes barriers to localization or international deployment;
- **localization (l10n):** adaptation of a product/content to the language, cultural and other requirements of a specific locale.

W3C explicitly includes string concatenation, language identification, bidirectional text, dates, numbers, calendars, sorting, names and other locale-dependent behavior within the internationalization problem.

Source:
- W3C — Localization vs. Internationalization  
  https://www.w3.org/International/questions/qa-i18n

### SYNTHESIS

English source copy can be linguistically excellent and still be **architecturally hostile to localization**.

Examples:
- a sentence assembled from separately translated fragments;
- plural logic hard-coded to English singular/plural;
- meaning that depends on left/right screen position;
- dates/numbers/currencies embedded as literal English-formatted text;
- ambiguous strings with no translator context;
- an interface geometry that assumes English string length.

### STUDIO JUDGMENT

Content Design therefore owns two separate questions:

1. **Source-language semantic quality** — Is the English wording accurate, clear, sufficient and consistent?
2. **Localization readiness** — Is that meaning represented in a form that another locale can express correctly without reconstructing hidden context or breaking the UI contract?

A string must satisfy both before it is considered globally project-ready.

---

## 2. English-first does not mean English-grammar-dependent architecture

### SOURCE — Microsoft global-content guidance

Microsoft’s global writing guidance recommends clear sentence structure and warns against idioms, colloquial expressions, culture-specific references and modifier stacks because they can confuse global readers and complicate localization/translation.

Source:
- Microsoft Writing Style Guide — Writing tips for global content  
  https://learn.microsoft.com/en-us/style-guide/global-communications/writing-tips

### SYNTHESIS

For an English-first global product, source English should prefer:
- explicit agents/objects where ambiguity would affect translation;
- stable terminology;
- ordinary, literal wording over idiom when no product value is gained by idiom;
- short logical sentences when complexity can be reduced without losing necessary meaning;
- unambiguous references rather than culture-specific shorthand.

### Critical boundary

This does **not** mean “write robotic translation English.”

Natural English remains the shipped source experience. The requirement is to remove **gratuitous ambiguity and culture dependence**, not personality or fluency.

Tone may remain human and distinctive where the meaning is stable and the phrase does not create avoidable localization debt.

---

## 3. Never encode sentence grammar by string concatenation

### SOURCE — W3C

W3C explicitly lists care over string concatenation as an internationalization concern.

Source:
- https://www.w3.org/International/questions/qa-i18n

### SOURCE — Unicode CLDR

CLDR demonstrates that grammatical form can vary by quantity and that languages may use different plural categories. It explicitly advises against literal English transfer in plural minimal-pair work.

Sources:
- Unicode CLDR — Plural Rules  
  https://cldr.unicode.org/index/cldr-spec/plural-rules
- Unicode CLDR — Plurals & Units  
  https://cldr.unicode.org/translation/getting-started/plurals

### SOURCE — Apple

Apple’s current localization system supports plural variants because languages differ in grammatical rules. Xcode string catalogs are the current recommended mechanism.

Sources:
- Apple — Localizing and varying text with a string catalog  
  https://developer.apple.com/documentation/xcode/localizing-and-varying-text-with-a-string-catalog
- Apple — Localizing strings that contain plurals  
  https://developer.apple.com/documentation/xcode/localizing-strings-that-contain-plurals

### STUDIO JUDGMENT

Reject architectures such as:

`"Delete " + count + " " + objectName + "?"`

when translators need control over the complete phrase.

Prefer one semantic message with named variables/placeholders whose relationship is visible to the localizer.

The localizable unit is the **complete semantic proposition**, not whichever fragments happen to be convenient in code.

---

## 4. Plural, number, date, currency and unit behavior are content-system concerns

### SOURCE — Unicode CLDR

CLDR provides locale-sensitive conventions for plurals, numbers, currencies, dates/times, units and many other language/region behaviors. Its current release describes these data as building blocks used by major software systems for internationalization/localization.

Sources:
- Unicode CLDR — release overview  
  https://cldr.unicode.org/downloads/cldr-49
- Unicode CLDR — definitions / locale data  
  https://cldr.unicode.org/index/cldr-spec/definitions

### SOURCE — Apple

Apple states that supporting multiple languages/regions is more than translating text and includes plural behavior and locale-sensitive display.

Source:
- Apple — Localization  
  https://developer.apple.com/documentation/xcode/localization

### SYNTHESIS

Content specifications should distinguish:
- **semantic value**: e.g. duration = 90 minutes;
- **presentation template**: e.g. `1 hr 30 min`;
- **locale formatting**: selected by platform/locale rules;
- **terminology choice**: e.g. `Block time`, if that is a domain concept rather than a generic duration label.

Do not bake locale formatting into the semantic data contract.

### Example

Product fact:
- `count = 1`
- object concept = imported record

English source:
- `1 record imported`

Another locale may require different word order, morphology or plural category. Content should preserve the event semantics, not insist on English syntax.

---

## 5. Translator/localizer context is part of the content architecture

### SOURCE — W3C localization notes

W3C localization requirements identify the need for authors to provide localizers with context such as:
- meaning of ambiguous text;
- what a variable refers to;
- where/how a UI string is used;
- why a segment should remain untranslated;
- relationships among content items.

Source:
- W3C — Internationalization and Localization Markup Requirements, localization notes  
  https://www.w3.org/TR/itsreq/

### SOURCE — Apple

Apple’s current string-catalog workflow supports comments/context, and its localization tooling uses contextual information about where strings appear and terminology consistency.

Sources:
- Apple — Preparing your app’s text for translation  
  https://developer.apple.com/documentation/xcode/preparing-your-apps-text-for-translation
- Apple — Localizing your app using agents  
  https://developer.apple.com/documentation/xcode/localizing-your-app-using-agents

### STUDIO JUDGMENT

Each high-risk string should be able to carry metadata such as:
- stable string ID;
- English source;
- screen/workflow context;
- object/state/action/consequence;
- variable definitions;
- character/geometry sensitivity if real;
- approved terminology references;
- whether a product/domain token must remain unchanged;
- screenshot/context link where useful;
- accessibility role/name relationship where applicable.

A translation vendor or tool should not have to infer product behavior from an isolated word like `Open`, `Close`, `Apply`, `Record`, `Current` or `Sync`.

---

## 6. Same English word may need different localization keys when meanings differ

### SOURCE — Apple

Apple’s localization documentation notes that where the same source phrase has multiple meanings, unique keys can be used for distinct uses to avoid collisions.

Source:
- Apple — `NSLocalizedString`  
  https://developer.apple.com/documentation/foundation/nslocalizedstring

### SYNTHESIS

String reuse should follow **semantic identity**, not character equality.

Example:
- `Record` = noun meaning one imported flight entry;
- `Record` = verb meaning begin recording.

They must not be forced through one translation unit merely because English spelling is identical.

This directly extends CD002’s concept-before-designation rule into localization architecture.

---

## 7. Avoid layout-driven semantic truncation

### SOURCE — Apple

Apple’s localization guidance explicitly requires preparing interfaces for translated text and testing each supported language/region.

Source:
- https://developer.apple.com/documentation/xcode/localization

### SOURCE — W3C

W3C Internationalization maintains guidance specifically on text expansion and why translated text can break layout.

Index:
- https://www.w3.org/International/articlelist

### CROSS-DOMAIN TRANSFER — Type/Web

Design Studio Type and Web already establish that necessary labels must survive enlargement/reflow rather than be deleted simply to preserve geometry.

### STUDIO JUDGMENT

If localization causes fit pressure, review in this order:

1. Is every semantic distinction necessary?
2. Can the component/layout reflow?
3. Can the local wording be naturally more compact without losing meaning?
4. Is an accepted domain abbreviation available for that locale/audience?
5. Is an alternate layout/presentation required?

Do **not** begin with “shorten the translation until it fits.”

---

## 8. Directionality and position are not stable global semantics

### SOURCE — W3C

W3C documents failures that occur when strings move between left-to-right and right-to-left contexts and provides specific internationalization guidance for bidirectional content.

Sources:
- W3C — Strings and bidi  
  https://www.w3.org/international/articles/strings-and-bidi/
- W3C — Authoring HTML for right-to-left scripts  
  https://www.w3.org/International/docs/bp-html-bidi/

### SYNTHESIS

CD005 already rejects `the button on the right` as a primary semantic identifier. Global localization makes that rule stronger: visual direction itself can change by locale.

Content should identify controls by semantic name/role first, leaving position only as an optional supplemental cue when genuinely useful.

---

## 9. Global English is a source-language strategy, not a locale

`Global English` in this study is an internal Design Studio shorthand, not a standards-defined locale.

It means:
- English is the source/development language;
- source content is written for an international audience where possible;
- idiom/cultural assumptions are deliberate rather than accidental;
- strings preserve full semantic propositions;
- localization metadata is available;
- locale-sensitive formatting is delegated to appropriate platform/data systems;
- future languages can restructure grammar and word order without violating the product contract.

It does **not** mean:
- one simplified English variant must serve all English-speaking locales forever;
- all culture-specific product decisions disappear;
- translators must mirror English sentence structure;
- English terminology automatically becomes globally understood professional terminology.

---

## 10. Product-domain terminology — preserve concepts, not English words

For specialist apps, many terms may be English-origin professional vocabulary.

Examples from Design Studio live-project domains include concepts such as:
- import / duplicate / sync / conflict;
- flight record / block time / PIC / SIC;
- distribution / ROC / cost basis / split.

### STUDIO JUDGMENT

For every high-value professional term, record:
1. canonical product concept;
2. English source designation;
3. whether the English token itself is domain-standard internationally;
4. allowed abbreviations;
5. terms that must not be merged;
6. locale-specific translation decision status;
7. whether local professionals normally retain the English term;
8. evidence source for any locale-specific decision.

Do not translate a specialist concept merely because a dictionary equivalent exists.

Do not preserve English merely because the development team is accustomed to it.

Both choices require audience/domain evidence when stakes are material.

---

## 11. Original practice — one English-first import workflow

This is a non-human semantic/localization-readiness exercise.

### Product facts

- user selects one or more files;
- parser identifies records;
- some records are possible duplicates;
- user reviews them before import;
- confirmation imports selected records;
- import count varies;
- an ambiguous network outcome can occur after confirmation;

### Candidate A — English-centric fragments

Strings:
- `Review ` + count + ` duplicate(s)`
- `Import ` + count + ` record(s)`
- `Click the button on the right`
- generic key `Record` reused for noun and verb

Verdict: **REJECT**.

Reasons:
- concatenated grammar;
- English pseudo-plural `(s)`;
- sensory/position dependency;
- semantic key collision.

### Candidate B — natural English but weak localization metadata

Strings:
- `Review possible duplicates`
- `Import 12 records`
- `Select Import records`

Semantics are substantially better, but translation units have no object/state/variable context.

Verdict: **REWORK**.

### Candidate C — semantic message units + context

Example source entries:

`import.review_duplicates.title`
- English: `Review possible duplicates`
- context: heading shown after parser flags records whose identity is uncertain
- concept: review task, not confirmed duplicates

`import.confirm.count`
- English one: `Import 1 record`
- English other: `Import {count} records`
- variable: `{count}` = number of selected records to commit
- consequence: starts import; does not assert completion

`import.status.outcome_unknown`
- English: `We couldn’t confirm whether the import finished.`
- context: request outcome unknown; retry safety controlled by Interaction

Verdict: **KEEP AS ARCHITECTURE CONTROL**.

This does not prove that these exact English phrases are optimal for users. It proves that the content architecture preserves distinctions needed by localization and Interaction.

---

## 12. Localization-readiness audit v0.1

For every important source string, check:

### Semantic
- `CONCEPT IDENTITY` — is the underlying concept explicit?
- `STATE FIDELITY` — does wording match actual state?
- `ACTION FIDELITY` — does the command match actual behavior?
- `SCOPE / CONSEQUENCE` — is important scope preserved?

### Source English
- `IDIOM / CULTURE DEPENDENCY`
- `AMBIGUOUS PART OF SPEECH`
- `AMBIGUOUS REFERENT`
- `UNNECESSARY MODIFIER STACK`
- `ENGLISH-ONLY ABBREVIATION ASSUMPTION`

### Message architecture
- `STRING CONCATENATION`
- `PSEUDO-PLURAL` such as `(s)`
- `SEMANTIC KEY COLLISION`
- `MISSING VARIABLE CONTEXT`
- `MISSING LOCALIZER NOTE`
- `HARD-CODED DATE/NUMBER/CURRENCY/UNIT`

### Interface transfer
- `FIXED-WIDTH DEPENDENCY`
- `POSITION/DIRECTION LOCK`
- `COLOR/ICON-ONLY SEMANTICS`
- `VISIBLE/ACCESSIBLE NAME DRIFT`

### Evidence limits
- `LOCALE EXPERT REVIEW NEEDED`
- `RUNTIME I18N TEST NEEDED`
- `HUMAN VALIDATION NEEDED`

The audit can identify structural localization debt. It cannot prove translation quality, comprehension or cultural appropriateness.

---

## 13. RELATED DOMAIN CHECK

### Type

Current Type work requires actual operational strings and rejects geometry-driven silent substitution.

Transfer:
- localized strings become real glyph/width/fallback test corpora;
- Type owns script/font/rendering support;
- Content owns semantic necessity and locale source strings.

Relationship: **DIRECT DEPENDENCY + FUTURE TRANSFER VALIDATION**.

### Color

Meaning must survive when visual encoding changes. Localization must not introduce color-only state names such as `choose the red option` as a required instruction.

Relationship: **REUSE**.

### Layout / Interaction

Interaction owns state/action/retry/recovery truth. Localization may reorder language but cannot alter that contract. Layout must support language expansion/recomposition rather than demand semantic truncation.

Relationship: **DIRECT DEPENDENCY**.

### Web

W3C directionality/language metadata and actual browser rendering belong to Web transfer validation. Content provides complete semantic message units and context; Web validates language/direction metadata, reflow and runtime accessibility.

Relationship: **FUTURE TRANSFER VALIDATION**.

### Existing Content

- CD001 supplies semantic fidelity;
- CD002 concept-before-designation;
- CD003 command contract;
- CD004 minimum-sufficient information;
- CD005 modality-neutral semantic identity;
- CD006 source provenance.

CD007 extension:

> **Preserve the semantic contract across locales; allow the linguistic realization to change.**

---

## 14. HANDOFFS TO OTHER SPECIALISTS

### Type

Future locale expansion must provide real translated/professional strings, not artificial alphabet samples alone. Script/fallback coverage decisions should follow product locale strategy.

### Layout / Interaction

Do not freeze component dimensions or reading-order assumptions around English. Preserve semantic/task order while allowing localized language to recompose.

### Web

Future integrated validation should include at least:
- longer localized strings;
- language metadata;
- an RTL transfer case;
- locale date/number formatting;
- visible/accessibility-name consistency after localization.

### Coordinator / project teams

For current products, English is the canonical source language. Localization readiness should be designed from the beginning even if additional locales are not shipped at v1.

---

## 15. Evidence boundary

CD007 establishes:
- authoritative i18n/l10n distinction;
- locale-sensitive plural/formatting requirements;
- source-English guidance for global audiences;
- full-message/localizer-context architecture;
- directionality/geometry risks;
- a reproducible localization-readiness audit;
- an English-first global product model.

CD007 does **not** establish:
- quality of any specific translation;
- which locales the products should launch in;
- human comprehension in English or any target locale;
- cultural appropriateness across markets;
- professional-term adoption in each locale;
- production framework implementation correctness.

Those require later locale, market, platform and human evidence.

---

## Current conclusion

`SOURCE`: W3C, Unicode CLDR, Apple and Microsoft all show that global product language requires more than translating English strings: sentence architecture, plural/format rules, context metadata, directionality and locale-sensitive systems matter.

`SYNTHESIS`: an English-first app should use natural, semantically explicit source English while keeping grammar, formatting and layout assumptions out of the product’s underlying content architecture.

`STUDIO JUDGMENT`: Design Studio’s Content curriculum is **English-first / global-by-design**. Specific non-English languages, including Korean, are later transfer cases chosen by product need, market risk or validation value—not mandatory primary curriculum targets.

Stage 1 remains **IN STUDY / PRACTICE — NOT PASSED**. The next step is an integrated Foundation capstone applying CD001–CD007 to one bounded professional workflow before a closure audit.
