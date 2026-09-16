# CD004 — Plain Language, Scanning, Information Order and Sufficiency

Status: **FOUNDATION — SOURCE STUDY + EVIDENCE REVIEW + ORIGINAL PRACTICE / NOT A PASS CLAIM**  
Date: 2026-09-16

## Research question

How should Content Design make interface language easier to find, understand and use without falling into the false rule that “shorter is always better” or deleting domain-critical meaning?

CD001 established semantic fidelity. CD002 established concept/terminology discipline. CD003 established command semantics. CD004 addresses the next Foundation layer: **how much information to include, in what order, and how to structure it so that users can find and act on necessary meaning.**

The target is not a style-guide checklist. It is a defensible method for deciding when plain language, front-loading, chunking, headings, short sentences and progressive disclosure help — and when aggressive simplification creates omission, ambiguity or semantic loss.

---

## 1. Sources

### SOURCE — ISO 24495-1:2023: plain language is broader than short words and sentences

ISO 24495-1:2023 is an international standard for plain-language principles and guidelines. ISO states that it applies to written text for general, technical and other contexts and is intended to help creators develop plain-language documents.

Official source:
- ISO 24495-1:2023 — Plain language — Part 1: Governing principles and guidelines  
  https://www.iso.org/standard/78907.html

The standard’s structure is important because plain language is not treated as mere vocabulary simplification. Its governing model centers on readers receiving relevant information, being able to find it, understand it and use it.

### SYNTHESIS

For Content Design, plain language should be treated as a **task-information system**, not a sentence-level aesthetic.

A string can contain short familiar words and still fail because:
- it omits necessary conditions;
- the key fact appears too late;
- headings do not reveal the topic;
- different concepts are collapsed;
- the action remains unclear;
- a user cannot determine what to do next.

Conversely, a longer message can be more usable when the extra words carry necessary state, condition or consequence information.

---

### SOURCE — GOV.UK: start with less, front-load important words, and fix the interface before explaining it

GOV.UK’s Service Manual advises interface writers to use user language, reduce unnecessary cognitive load, design for scanning, put important words first and remove unnecessary wording. It also says to start with less content and add help only when evidence shows that it is needed. If an interface requires substantial explanation, the interface itself may be the problem.

Source:
- GOV.UK Service Manual — Writing for user interfaces  
  https://www.gov.uk/service-manual/design/writing-for-user-interfaces

### SYNTHESIS

This is not equivalent to “delete everything possible.”

The stronger principle is:

> **Remove words that do not change understanding or action; preserve words that carry necessary distinctions, conditions, uncertainty, scope or consequence.**

This directly continues CD001 and CD003. A semantically necessary phrase cannot be classified as “fluff” merely because it increases character count.

---

### SOURCE — W3C Cognitive Accessibility guidance: clear wording and chunking can reduce processing burden

W3C supplemental cognitive-accessibility guidance recommends clear/common words, short blocks, one topic per paragraph, short descriptive headings and placing the purpose of a chunk near its beginning. It also recommends separating instructions into explicit steps and not relying on users to infer omitted steps.

Sources:
- W3C WAI — Use Clear Words  
  https://www.w3.org/WAI/WCAG2/supplemental/patterns/o3p01-clear-words/
- W3C WAI — Keep Text Succinct  
  https://www.w3.org/WAI/WCAG2/supplemental/patterns/o3p05-succinct-text/
- W3C WAI — Separate Each Instruction  
  https://www.w3.org/WAI/WCAG2/supplemental/patterns/o3p09-separated-instructions/
- W3C WAI — Use Clear Step-by-step Instructions  
  https://www.w3.org/WAI/WCAG2/supplemental/patterns/o4p07-step-instructions/

Important evidence boundary:
- this material is **supplemental guidance**, not a claim that every sentence must satisfy one universal word-count threshold;
- W3C itself notes that long sentences can sometimes be clearer and recommends usability testing where uncertain.

### STUDIO JUDGMENT

The studio therefore adopts **chunking and sentence simplification as diagnostic defaults, not mechanical pass/fail rules**.

---

### SOURCE — ONS service guidance: front-loading supports task-oriented scanning

The UK Office for National Statistics service manual describes scanning patterns and recommends putting important information at the beginning of headings, sections, paragraphs and sentences so users can identify relevant information quickly.

Sources:
- ONS Service Manual — Plain language  
  https://service-manual.ons.gov.uk/content/writing-for-users/plain-language
- ONS Service Manual — How people read online  
  https://service-manual.ons.gov.uk/content/writing-for-users/how-people-read-online

### EVIDENCE LIMIT

Scanning-pattern descriptions are useful service-design guidance, but Content Design must not turn named patterns such as “F-pattern” into a universal behavioral law for every app, language, screen size or expert workflow.

Front-loading is retained as a **priority-order heuristic**:
- expose the object/task/status early;
- do not force the user through organizational preamble before the fact they came to find;
- validate real scan/find behavior with users when making performance claims.

---

### EVIDENCE — plain-language interventions can improve comprehension, but effects are context dependent

A 2024 randomized study comparing plain-language and standard versions of health recommendations found a substantial comprehension improvement for one recommendation but a much smaller, statistically non-significant difference for another. This is useful because it supports plain-language value while also demonstrating that the effect is not mechanically identical across content.

Source:
- Sayfi et al. — A multimethods randomized trial found that plain language versions improved adults understanding of health recommendations  
  https://pubmed.ncbi.nlm.nih.gov/38008266/

A randomized experiment on medication instructions likewise found that patient-centered revisions improved correct interpretation overall, but effects varied across individual instructions.

Source:
- Health IT Usability Focus Section: Adapting EHR-Based Medication Instructions to Comply with Plain Language Guidance—A Randomized Experiment  
  https://pmc.ncbi.nlm.nih.gov/articles/PMC5802303/

Another randomized study of clinical-trial explanations found that audience health-literacy level moderated which linguistic strategy produced better comprehension; plain language was not the best strategy for every subgroup and message condition.

Source:
- Linguistic Strategies for Improving Informed Consent in Clinical Trials Among Low Health Literacy Patients  
  https://pubmed.ncbi.nlm.nih.gov/27794035/

### SYNTHESIS

These studies are domain-specific health-communication evidence, not direct app-UI proof. Their reusable lesson is narrower:

> **Plain-language techniques can materially affect comprehension, but wording effects depend on audience, concept and context.**

This supports the studio rule that plain-language heuristics require later transfer validation rather than universal certainty.

---

### EVIDENCE — readability scores are not comprehension scores

Research on readability formulas shows that sentence length, word length and syllable count are incomplete proxies for comprehension. Different formulas can produce materially different grade estimates, and short-form content is particularly sensitive to preprocessing choices.

Sources:
- Leroy et al. — Moving Beyond Readability Metrics for Health-Related Text Simplification  
  https://pmc.ncbi.nlm.nih.gov/articles/PMC5044755/
- Reading grade level estimates of public health communication on social media vary due to text preprocessing  
  https://pmc.ncbi.nlm.nih.gov/articles/PMC12919665/
- Assessing readability formula differences with written health information materials  
  https://pubmed.ncbi.nlm.nih.gov/22835706/

### STUDIO JUDGMENT

A readability score may be used as a **lint signal**, but never as evidence that users understood the interface.

The studio rejects these substitutions:

`lower grade score = clearer`  
`shorter sentence = understood`  
`fewer syllables = familiar term`  
`plain-language checklist = validated comprehension`

A score can trigger review; it cannot close the human-evidence gate.

---

## 2. Foundation distinction — clarity, brevity and sufficiency are different variables

### STUDIO MODEL

For Content decisions, separate at least three questions:

1. **Clarity** — can the intended meaning be interpreted without unnecessary ambiguity?
2. **Brevity** — how much language is used?
3. **Sufficiency** — is enough information present to make the required decision or action safely?

These variables can move independently.

Examples:
- a two-word label can be brief but insufficient;
- a detailed warning can be sufficient but poorly ordered and therefore hard to use;
- a longer sentence can be clearer than several fragments if the causal relationship is important;
- a short common synonym can be less clear than a precise expert term for a specialist audience.

### Core rule

> **Optimize for the minimum sufficient content, not the minimum character count.**

“Minimum sufficient” means that removing another information unit would create a meaningful loss in task, state, scope, condition, consequence or recovery understanding.

---

## 3. Information order — front-load what changes the user’s next decision

### STUDIO JUDGMENT

Information should generally be ordered by **decision relevance**, not by the organization’s preferred explanation sequence.

A useful default order for transactional content is:

1. **what changed / what is required / what the current state is**;
2. **what the user can or must do**;
3. **critical condition, deadline, scope or consequence**;
4. **supporting explanation**;
5. **background or policy rationale**, if needed.

This is not a universal sentence template. Some legal, safety or domain contexts require a different order.

### Failure mode — organizational preamble

Weak:
> As part of our ongoing account security improvements, and in accordance with our updated authentication policy, we now require users with older credentials to...

The user’s task-relevant fact arrives late.

Stronger structure:
> **Reset your password before 30 September to keep signing in.**  
> We changed the password requirements for older accounts.

The second version front-loads action/deadline and moves rationale later.

This is a structured critique, not proof of user performance.

---

## 4. Scanning — write retrieval cues, not prose that requires complete reading

### SYNTHESIS

Task interfaces are often read selectively. Therefore Content should create **retrieval cues** that let a user identify whether a region contains the answer they need.

Useful cues include:
- descriptive headings that name the topic, state or decision;
- specific link/control labels;
- first sentence that states the section purpose;
- one conceptual topic per chunk;
- lists when items are genuinely parallel;
- visible conditions/deadlines near the relevant action;
- stable terminology from CD002.

### STUDIO JUDGMENT

A heading such as `Important information` carries little information scent because it says nothing about the subject.

A heading such as `When your imported records can be replaced` exposes the decision domain before the paragraph is read.

The studio therefore distinguishes:
- **attention label** — “Important”, “Note”, “Warning”;
- **topic label** — what the information is actually about.

An attention label may supplement a topic label, but should not routinely replace it.

---

## 5. Chunking — semantic grouping before arbitrary text splitting

### SOURCE synthesis

W3C guidance supports short logical chunks and one main topic per paragraph. Layout research in Design Studio also treats grouping, whitespace and density as meaning-bearing spatial structure.

### STUDIO JUDGMENT

Chunking is not “insert a line break every N words.”

A good chunk has:
- a coherent semantic purpose;
- an identifiable topic;
- a useful boundary from adjacent information;
- a sequence that matches task order or decision order.

### Bad chunking

One causal rule split into disconnected fragments can increase inference burden.

Example:
> Records may be replaced.  
> Only when IDs match.  
> Existing notes stay.  
> Unless you choose Replace all.

The fragments are short but the relationship among condition, consequence and exception is difficult to reconstruct.

### Better semantic grouping

> **Replace matching records**  
> If the record ID matches, you can replace the existing record. Its notes stay unless you choose **Replace all fields**.

This version is not automatically “proven clearer”; it preserves the relationships more explicitly for later human validation.

---

## 6. Necessary detail — progressive disclosure is not permission to hide prerequisites

### SYNTHESIS

GOV.UK advises starting with less and adding help when evidence shows it is needed. W3C guidance supports putting instructions before or next to the activity when users need them to complete the task.

### STUDIO JUDGMENT

Distinguish three information classes:

### A. Required-before-action
Information the user needs **before** deciding or acting.

Examples:
- irreversible consequence;
- required format when the system cannot accept alternatives;
- deadline;
- eligibility constraint;
- known cost or external commitment;
- safety-critical prerequisite.

Do not hide this behind optional help merely to reduce visual density.

### B. Helpful-at-point-of-need
Information useful only when a user hesitates or encounters a less common case.

Examples:
- examples of accepted formats;
- definitions of uncommon terms;
- edge-case explanation;
- why a value is requested.

This is a strong candidate for progressive disclosure.

### C. Background/explanatory
Information that does not change immediate action.

Examples:
- policy history;
- implementation rationale;
- organizational process explanation.

This should usually be secondary to the task path.

### Consequence

The content question is not “Can this be hidden?” but:

> **At what point must this information become available for the user to make the next correct decision?**

---

## 7. Expert-domain plain language — preserve precision, remove unnecessary decoding

CD002 established that specialist vocabulary may be correct when it is genuinely audience-native.

CD004 adds an important refinement:

> **Plain language for experts does not mean replacing every technical term with a general-language synonym. It means reducing unnecessary linguistic and structural difficulty around the concepts the audience actually needs.**

For a professional interface:
- keep a domain term when it is precise, conventional and task-critical;
- do not surround it with bureaucratic or implementation jargon;
- define or contextualize terms whose familiarity is uncertain;
- avoid changing a precise term merely to reduce syllable count;
- keep concept boundaries stable across screens.

### Example

If a specialist audience genuinely uses `duplicate`, replacing it with `same thing` can reduce precision.

Plain-language improvement may instead be:

Weak:
> The system has performed duplicate candidate identification processing on the imported dataset.

Stronger:
> **3 possible duplicates need review.**

The improvement comes from information order, active task relevance and removal of implementation language — not from eliminating the domain concept `duplicate`.

---

## 8. RELATED DOMAIN CHECK

### Typography / Type

Evidence checked:
- current `progress/TYPE_STATUS.md`;
- `research/type/T017-logmate-operational-data-typography-semantic-geometry-transfer.md`.

Reusable finding:
- actual operational strings, identifiers, numerals, punctuation and mixed-language content materially affect rendering and geometry;
- text should not be shortened solely to rescue preferred layout geometry.

Content consequence:
- CD004’s “minimum sufficient” wording must become real Type stress content;
- necessary headings/help/warnings can expose width and wrapping problems that Type/Layout must solve rather than Content silently deleting meaning.

Relationship: **DIRECT REUSE + FUTURE TRANSFER VALIDATION**.

### Color

Evidence checked:
- current `progress/COLOR_STATUS.md`.

Reusable finding:
- salience and semantic color roles can help users locate information, but meaning must survive alternate/forced-color contexts.

Content consequence:
- front-loaded wording and descriptive labels must carry meaning independently of visual highlight color.

Relationship: **REUSE; no contradiction**.

### Layout / Interaction

Evidence checked:
- current `progress/LAYOUT_STATUS.md`;
- prior Layout evidence on whitespace/density/rhythm and semantic grouping;
- `research/interaction/I002-latency-pending-optimistic-retry.md` for state/action consequence.

Reusable findings:
- grouping and density are spatial contracts, not decoration;
- state/action/recovery semantics determine which information is necessary before action.

Content consequence:
- Content owns semantic chunk boundaries and information priority; Layout owns spatial realization;
- Content cannot use progressive disclosure to hide a prerequisite that Interaction says is needed before the action.

Relationship: **CROSS-DOMAIN DEPENDENCY**.

### Web Design

Evidence checked:
- current `progress/WEB_STATUS.md` through W017;
- `research/web/W017-icon-signal-chromium-transfer.md`.

Reusable finding:
- W017 preserved visible labels at enlarged text and kept consequential status textual rather than icon-only.

Content consequence:
- succinctness must not be achieved by deleting labels at narrow widths or enlarged text;
- later Web transfer should test CD004 content under responsive reflow, zoom, localization and real component constraints.

Relationship: **DIRECT HANDOFF RECEIVED + FUTURE TRANSFER VALIDATION**.

### Existing Content

- CD001 prevents brevity from overriding semantic truth.
- CD002 prevents simplification from collapsing concepts.
- CD003 prevents short action labels from hiding persistence/consequence.

CD004 extends these into information quantity and order.

---

## 9. Original practice — three versions of the same professional workflow message

### Controlled product facts

Assume a professional data-import workflow with these fixed facts:
- 124 records were parsed;
- 3 records are possible duplicates;
- duplicate records will **not** be imported until reviewed;
- the other 121 records can be imported now;
- reviewing duplicates is optional before importing the 121 non-duplicates;
- no existing records are modified by importing the 121 new records.

The task is to tell the user what happened and what they can do next.

### Candidate A — compressed

> **124 records found. Review duplicates or continue.**

Critique:
- brief;
- hides the fact that there are exactly 3 duplicates;
- `continue` is ambiguous about what will happen;
- does not clarify whether duplicates will also import;
- fails CD003 command specificity and CD004 sufficiency.

Verdict: **REJECT**.

### Candidate B — complete but poorly ordered

> The import parser identified 124 records in total and, because 3 of those records may correspond to records that already exist, those 3 will be withheld from the import pending review while the remaining 121 records can be imported without changing existing records.

Critique:
- semantically richer;
- internal term `parser` is unnecessary for the user task;
- one long sentence carries count, condition, consequence and next action;
- the key choice is difficult to locate;
- information is sufficient but not findable enough.

Verdict: **REWORK**.

### Candidate C — minimum sufficient structure

> **121 new records are ready to import.**  
> **3 possible duplicates need review.** They will not be imported until you review them. Importing the 121 new records will not change your existing records.  
> Actions: **Import 121 records** / **Review 3 duplicates**

Critique:
- front-loads the immediately actionable result;
- preserves duplicate count and withholding behavior;
- exposes the non-modification consequence;
- action labels name scope;
- longer than Candidate A but with materially more decision-relevant information;
- human comprehension and action-selection performance remain untested.

Verdict: **KEEP AS SEMANTIC/INFORMATION-ORDER CONTROL**, not final proven copy.

### Practice conclusion

This exercise separates three failure classes:
- A: **brevity-induced omission**;
- B: **sufficient content with poor information order**;
- C: **structured minimum-sufficient candidate**.

The studio therefore rejects “shortest wins” as a Content criterion.

---

## 10. Reproducible non-human audit — information sufficiency v0.1

For a consequential interface block, record the known product facts first, then evaluate the content using these checks.

### Semantic checks

- `MISSING OBJECT` — user cannot tell what entity/process the message concerns.
- `MISSING STATE` — current state is omitted or materially vague.
- `MISSING ACTION` — next available/required action is not identifiable.
- `MISSING CONSEQUENCE` — a material result/risk is absent.
- `MISSING CONDITION` — a rule applies only under a condition that is not exposed.
- `MISSING SCOPE` — count/object/range affected by the action is unclear.

### Information-order checks

- `LATE TASK FACT` — critical fact appears after background/rationale.
- `GENERIC HEADING` — heading signals importance but not topic.
- `MULTI-TOPIC CHUNK` — unrelated decisions are combined.
- `FRAGMENTED RELATIONSHIP` — condition/consequence/exception is split so aggressively that the relationship becomes implicit.

### Plain-language checks

- `INTERNAL JARGON` — implementation/organizational term has no user-task value.
- `UNEXPLAINED UNCOMMON TERM` — familiarity is uncertain and no definition/context is available.
- `FALSE SIMPLIFICATION` — a precise concept is replaced with a familiar but semantically weaker term.
- `REDUNDANT PREFACE` — words delay the task fact without changing meaning.

### Validation flags

- `READABILITY SIGNAL ONLY` — automated score may prompt review but cannot justify comprehension claims.
- `AUDIENCE EVIDENCE NEEDED` — terminology/amount/order depends on actual audience knowledge.
- `HUMAN FINDABILITY TEST NEEDED` — claim concerns whether users can locate information.
- `HUMAN COMPREHENSION TEST NEEDED` — claim concerns understanding.
- `TASK PERFORMANCE TEST NEEDED` — claim concerns successful action/error/time.
- `LOCALIZATION REVIEW NEEDED` — information order or compactness may change materially across languages.

### What this audit can establish

It can identify contradictions, omissions, late-priority facts, terminology problems and structural weaknesses against known product facts.

### What it cannot establish

It cannot prove:
- reading speed;
- scan pattern;
- comprehension;
- preference;
- trust;
- task success;
- accessibility outcomes for actual users;
- cross-language equivalence.

---

## 11. Foundation principles after CD004

The Content Foundation now provisionally adopts these rules:

1. **Plain language is task-oriented information design, not a synonym for short text.**
2. **Semantic fidelity and sufficiency precede brevity optimization.**
3. **Front-load the information that changes the user’s next decision.**
4. **Chunk by semantic purpose, not arbitrary word count.**
5. **Descriptive headings should expose topic, not merely importance.**
6. **Do not hide required-before-action information behind optional disclosure.**
7. **For expert audiences, preserve precise domain-native terminology when justified; simplify the surrounding language and structure.**
8. **Readability formulas are diagnostics, not comprehension evidence.**
9. **Plain-language effects are context- and audience-dependent and require transfer/human validation for performance claims.**
10. **Minimum sufficient content is a stronger target than minimum character count.**

---

## 12. HANDOFFS TO OTHER SPECIALISTS

### Type

CD004 supplies realistic long/short content controls that should be used in later rendering stress. If a semantically necessary condition, heading or warning causes wrap pressure, Type should test it rather than assume Content should delete it.

### Layout / Interaction

Content now distinguishes required-before-action vs point-of-need vs background information. Layout/Interaction can use this classification to determine spatial priority and disclosure timing without transferring semantic ownership.

### Web Design

W017’s decision to preserve visible text under enlargement is confirmed from the Content side. A later browser transfer should test CD004 controls under narrow width, 200%+ text/zoom, localization and dynamic state changes.

### Color

Visual emphasis may support findability but must not replace topic/state wording; no content block should require authored hue to identify its meaning.

---

## 13. OPEN questions after CD004

1. Which human methods best separate **findability**, **comprehension**, **recall** and **task actionability** for short interface content?
2. How should information-order heuristics change in Korean, where grammatical and discourse structure differs from English?
3. Which expert-domain abbreviations should be expanded, retained or paired with definitions for pilots, investors and other specialist audiences?
4. How should progressive disclosure be tested when the cost of missing information is asymmetric?
5. How should Content and Layout coordinate density reduction without moving required information below the point of action?
6. Can a reproducible content-lint pipeline detect terminology drift, missing state/action/consequence and generic headings without pretending to measure understanding?

These remain Foundation/next-stage research questions.

## Current conclusion

`SOURCE`: ISO, GOV.UK and W3C treat plain language as audience/task-oriented communication involving relevance, findability, understandability, structure and usability — not merely short words.

`EVIDENCE`: controlled health-communication studies show that language simplification can improve comprehension in some contexts but that effects vary by content and audience.

`SYNTHESIS`: brevity, clarity and sufficiency are separate variables; a Content system should minimize unnecessary language while preserving all decision-relevant meaning.

`STUDIO JUDGMENT`: **minimum sufficient content + decision-relevant information order** becomes the current Foundation model.

`OPEN`: Korean transfer, expert-domain transfer and human findability/comprehension/task-performance evidence remain unresolved.

Stage 1 remains **IN STUDY / PRACTICE — NOT PASSED**.