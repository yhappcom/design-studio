# CD001 — Language as Interface: User Need, State, Action and Consequence

Status: **FOUNDATION — SOURCE STUDY + ORIGINAL PRACTICE / NOT A PASS CLAIM**  
Date: 2026-09-16

## Research question

What must Content Design understand before it can responsibly optimize buttons, errors, onboarding, voice or tone?

This study tests a foundational proposition:

> Product language is part of the interface contract. A string is not successful merely because it is short, grammatical or pleasant; it must help the user understand the relevant object, state, available action and consequence without contradicting the actual product behavior.

The goal is to establish a base model for later Content Design research, not to create a universal copy formula.

## Why this comes first

The Design Studio mandate requires learning from fundamentals toward professional judgment rather than collecting pattern tips. Existing peer research already shows that system state, recovery, visual hierarchy and rendering are separate evidence domains. Content therefore needs a semantic foundation before studying surface patterns such as error-message templates or brand voice.

## Sources

### SOURCE — GOV.UK: content design starts with user need

GOV.UK publishing guidance describes good content design as helping people quickly find what they need to know or do and explicitly says content design starts with a user need and meeting it in the best way possible.

Source:
- GOV.UK — Understand content design  
  https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/plan-manage-content/understand-content-design/

Implication for this study: the unit of design is not the sentence in isolation. The relevant question is what the person needs to understand or accomplish.

### SOURCE — GOV.UK: interface writing should reduce unnecessary reading and use user language

The GOV.UK Service Manual advises using the same language as users, making transactional interfaces scannable, leading with important words, removing unnecessary words, using accessible link text and avoiding instructions that depend only on visual location/color/shape. It also states that if an interface needs excessive explanation, the interface itself may be the problem.

Source:
- GOV.UK Service Manual — Writing for user interfaces  
  https://www.gov.uk/service-manual/design/writing-for-user-interfaces

This is strong first-party service-design guidance, but individual wording rules remain context-specific rather than universal laws.

### SOURCE — Apple: writing is a design activity

Apple's WWDC session on interface writing explicitly frames UX writers/content designers as designing through the lens of language, including alerts, onboarding and accessibility descriptions. Apple's inclusion guidance also emphasizes direct, understandable and inclusive language and warns that tone can communicate unintended exclusion.

Sources:
- Apple WWDC22 — Writing for interfaces  
  https://developer.apple.com/videos/play/wwdc2022/10037/
- Apple Human Interface Guidelines — Inclusion  
  https://developer.apple.com/design/human-interface-guidelines/inclusion

This supports treating words as interface material rather than post-design decoration.

### SOURCE — Microsoft: wording affects usability and must expose next action clearly

Microsoft Windows writing guidance states that error wording, help content and button text can materially affect app usability. It recommends leading with important information, emphasizing action, using familiar language and providing a solution where possible. Microsoft also distinguishes voice from tone: voice is relatively stable while tone changes with context and the user's situation.

Sources:
- Microsoft Learn — Writing style for Windows apps  
  https://learn.microsoft.com/en-us/windows/apps/design/style/writing-style
- Microsoft Style Guide — Brand voice: Above all, simple and human  
  https://learn.microsoft.com/en-us/style-guide/brand-voice-above-all-simple-human
- Microsoft Style Guide — Describing interactions with the UI  
  https://learn.microsoft.com/en-us/style-guide/procedures-instructions/describing-interactions-with-ui

The input-neutral interaction-verb guidance is especially relevant to accessibility and cross-device instructions.

## What the sources agree on — and what they do not prove

### SYNTHESIS

Across GOV.UK, Apple and Microsoft, there is strong convergence on several principles:

1. start from what the user needs to understand or do;
2. treat interface language as part of product design;
3. prefer familiar, direct language over organization-internal or technical wording when the latter does not serve the user;
4. make important information and next actions easy to find;
5. remove unnecessary wording, but do not remove necessary meaning;
6. adapt tone to context rather than applying personality mechanically;
7. write accessibly and avoid instructions that assume one visual or input modality.

### EVIDENCE LIMIT

Agreement among platform/service style guides does **not** prove:

- a specific wording will improve task completion;
- shorter wording is always more comprehensible;
- conversational wording is always more trusted;
- one platform's tone is appropriate for another product/domain;
- professional users prefer simplified domain terminology in every case;
- a readability score predicts interface comprehension;
- a static expert critique equals user research.

Human outcome claims remain OPEN until tested with appropriate users/tasks.

## Foundation model — semantic contract before style

### STUDIO JUDGMENT

Before optimizing tone or brevity, analyze a user-facing message through four semantic questions:

1. **Object** — What thing/process is this about?
2. **State** — What is actually known to be true now?
3. **Action** — What can the user actually do now?
4. **Consequence** — What will that action change or risk?

Not every string must literally contain all four elements. The model is a diagnostic, not a sentence template.

A button may need only an action label because the object and consequence are already obvious from surrounding context. A destructive confirmation may need explicit object + consequence because ambiguity cost is high. A pending or ambiguous network outcome may require careful state wording before any retry action is offered.

### Why this matters

A polished sentence can still be wrong if it asserts a state the system does not know. Conversely, a technically precise sentence can still fail if it uses internal terminology the user cannot map to their goal.

Therefore Content quality has at least two distinct gates:

- **semantic fidelity** — wording matches the real product state/action/consequence contract;
- **human comprehensibility** — intended users understand it as intended.

The first can often be checked against product behavior and peer-domain evidence without users. The second ultimately requires human evidence when the claim concerns real comprehension or task performance.

## RELATED DOMAIN CHECK

### Typography / Type

Evidence checked:
- `research/type/009-typography-as-information-architecture.md`
- `research/type/T017-logmate-operational-data-typography-semantic-geometry-transfer.md`

Reusable finding:
- information roles and operational strings have typographic consequences; content length, numerals, punctuation and script mix affect layout/rendering.

Content consequence:
- Content must not assume wording is independent of rendering, but semantic wording remains Content ownership while font/metric/rendering decisions remain Type ownership.

### Color

Evidence checked:
- `research/color/C002-semantic-color-role-token-architecture.md`
- `research/color/C006-semantic-token-transfer-two-contexts.md`

Reusable finding:
- semantic state meaning should remain stable even if visual color strategy changes.

Content consequence:
- wording should refer to the state itself, not rely on color-specific descriptions such as “the red item” when state identity must survive alternate themes/forced colors.

### Layout / Interaction

Evidence checked:
- `research/interaction/007-interaction-agency-feedback-errors.md`
- `research/interaction/I002-latency-pending-optimistic-retry.md`
- `research/interaction/I004-ambiguous-outcome-idempotency-transfer.md`

Reusable finding:
- pending, failed and ambiguous outcomes are different interaction states; retry can create risk when outcome or idempotency is uncertain.

Content consequence:
- Content must not collapse these states into a generic “failed” message merely because that is shorter.

Relationship: **DIRECT REUSE + SEMANTIC TRANSFER**.

### Web Design

Evidence checked:
- `research/web/W006-complete-task-surfaces-state-recovery-contracts.md`
- `research/web/W015-integrated-task-state-recovery-validation.md`
- `research/web/W016-native-custom-button-chromium-transfer.md`

Reusable finding:
- actual browser/control behavior and state/recovery implementation can confirm or falsify assumptions made in static copy/design.

Content consequence:
- future Content patterns should be transfer-tested in actual web components, long/localized strings, keyboard/focus contexts and real failure states.

### Overlap decision

This study does not duplicate Interaction's state model. It **reuses** Interaction's canonical behavioral distinctions and asks the new Content-specific question: how must language preserve those distinctions?

## Original practice — ambiguous operation outcome

### Controlled product facts

Assume a network operation with the following facts:

- the user initiated an upload;
- the client lost confirmation before learning the final server outcome;
- the system cannot truthfully say whether the upload completed;
- repeating the operation could be harmful if the operation is not safely deduplicated;
- the product can show the user a list of existing uploads before another attempt.

This scenario deliberately reuses Interaction's ambiguous-outcome/idempotency distinction.

### Candidate A

**Upload failed. Try again.**

Critique:
- concise;
- clear action;
- but **REJECT** because “failed” asserts a state the system does not know;
- retry may expose the user to duplicate effect risk.

This is a semantic-fidelity failure even before any human comprehension testing.

### Candidate B

**We couldn't confirm whether the upload completed. Check your uploads before trying again.**

Critique:
- accurately communicates uncertainty;
- gives a safer next step;
- consequence is implicit rather than explicit;
- longer than A, but the extra information carries necessary state meaning.

Verdict: **KEEP as current semantic baseline**, not as a proven final UX string.

### Candidate C

**Upload status unknown. View uploads.**

Critique:
- compact and action-oriented;
- “status unknown” may sound system-centric or technical;
- “View uploads” is clear if that destination exists;
- may work for expert users, but comprehensibility is untested.

Verdict: **REWORK / candidate for later audience-specific comparison**.

### Practice conclusion

The exercise falsifies one common shortcut: **shortest is not automatically clearest or safest**.

Candidate A is shortest but semantically wrong. Candidate B is longer but more faithful to the actual interaction contract. Whether B or a refined C performs better for real users is OPEN and requires human evidence.

## Initial reusable method

For an important interface string:

1. write down the actual product facts without UI wording;
2. identify object, state, available action and consequence;
3. mark unknown/ambiguous facts explicitly;
4. draft at least two materially different wording strategies when the decision is consequential;
5. reject any draft that contradicts the product contract before testing style;
6. then critique clarity, information order, terminology, accessibility, length and tone;
7. identify which remaining claims require human testing;
8. transfer-test final candidates in the real component/platform when implementation can change meaning or discoverability.

This method is provisional and should be challenged in later studies.

## HANDOFFS TO OTHER SPECIALISTS

### Layout / Interaction

Content independently confirms the practical importance of preserving Interaction's distinctions among failure, pending and ambiguous outcome. A copy layer that collapses them can undo correct state modeling.

### Web Design

Future transfer validation should test semantic candidates in actual components and recovery flows rather than as isolated text snippets.

### Type

Longer but semantically necessary state messages create real wrapping/density/localization stress and should be used as Type/Layout test content rather than replaced solely to preserve a preferred geometry.

### Color

State wording should remain understandable when color encoding changes or is unavailable; avoid visual-only references.

## OPEN questions after CD001

1. How should user language and professional-domain terminology be reconciled when expert users rely on precise jargon?
2. How should terminology consistency be modeled across navigation, fields, table columns, notifications and help content?
3. How much state uncertainty should be exposed before language becomes cognitively burdensome?
4. Which evidence best supports front-loading and scan behavior for transactional interfaces beyond practitioner guidance?
5. What methods can validate content structure reproducibly before human studies without pretending to measure comprehension?
6. How should Korean/English linguistic differences change information order, action-label design and localization strategy?

These questions motivate the next Foundation studies rather than Stage 2 pattern work.

## Current conclusion

`SOURCE`: first-party guidance consistently treats interface language as a design concern grounded in user needs, clarity, action and accessibility.

`SYNTHESIS`: Content Design must operate on the product contract, not on isolated strings.

`STUDIO JUDGMENT`: object → state → action → consequence is adopted as an initial diagnostic model, subject to later revision.

`OPEN`: real comprehension/task-performance effects, Korean-language transfer, terminology systems and human validation remain unproven.

Stage 1 remains **IN STUDY / PRACTICE**. CD001 does not justify a Foundation PASS.
