# CD003 — Action Labels, Command Grammar and Consequence Clarity

Status: **FOUNDATION — SOURCE STUDY + CROSS-DOMAIN TRANSFER + ORIGINAL PRACTICE / NOT A PASS CLAIM**  
Date: 2026-09-16

## Research question

What should an action label communicate, and when is a short generic label such as `Continue`, `OK`, `Save` or `Delete` insufficient because the action's object, persistence, commitment, uncertainty or consequence matters?

CD001 established an object → state → action → consequence diagnostic. CD002 added concept-first terminology discipline. CD003 applies both to **commands**: the language a person activates to make the product do something.

The goal is not to memorize verb-first button rules. It is to determine when a label is semantically complete enough for its actual interaction contract.

---

## 1. Sources

### SOURCE — Apple: buttons must communicate purpose and usually benefit from action-oriented labels

Apple's current Human Interface Guidelines state that a button should clearly communicate its purpose. For text buttons, Apple recommends a few words that succinctly describe what the button does and suggests beginning with a verb where useful. Apple's general writing guidance similarly recommends action-oriented labels and warns against cute/clever wording that obscures purpose.

Sources:
- Apple HIG — Buttons  
  https://developer.apple.com/design/human-interface-guidelines/buttons
- Apple HIG — Writing  
  https://developer.apple.com/design/human-interface-guidelines/writing

Apple also distinguishes destructive buttons as a semantic role and advises against making a destructive action the primary/default choice merely because it is likely.

Content consequence:
- the button label and the control's role are separate but coordinated signals;
- a strong visual role cannot repair an ambiguous or misleading action label.

### SOURCE — GOV.UK: label wording should reflect actual persistence and commitment

GOV.UK's Design System provides unusually useful semantic examples:
- `Continue` when the service does **not** save the user's information;
- `Save and continue` when it **does** save;
- `Save and come back later` when data is persisted and the user can leave;
- `Confirm and send` when submitting without additional legal agreement;
- `Accept and send` when submission includes legal acceptance.

Source:
- GOV.UK Design System — Button  
  https://design-system.service.gov.uk/components/button/

This is stronger than a stylistic “use verbs” rule because the wording changes when the underlying system contract changes.

GOV.UK also says warning-button context and text should make destructive consequence clear rather than relying only on red styling.

### SOURCE — Microsoft: command labels should describe the action, use enough text, and include the object when context does not make it obvious

Microsoft's command-button guidance recommends specific labels over generic ones, starting with an imperative verb, and adding a direct object when needed for understanding. Microsoft also notes that `Cancel` can remain conventional when its target is unambiguous, but may need clarification if several pending actions exist.

Sources:
- Microsoft Learn — Command Buttons in Windows 7 / UX Guide  
  https://learn.microsoft.com/en-us/windows/win32/uxguide/ctrl-command-buttons
- Microsoft Learn — Writing style for Windows apps  
  https://learn.microsoft.com/en-us/windows/apps/design/style/writing-style

Evidence role:
- historical/current Microsoft guidance is a platform precedent, not a universal grammatical law.

### SOURCE — W3C: labels and programmatic names participate in operability and predictability

W3C guidance requires controls to have names/purposes that can be programmatically determined, and WCAG 2.5.3 addresses alignment between visible labels and accessible names for speech-input and text-to-speech users.

Sources:
- W3C — Understanding 2.5.3 Label in Name  
  https://www.w3.org/WAI/WCAG22/Understanding/label-in-name.html
- W3C — G167 Using an adjacent button to label the purpose of a field  
  https://www.w3.org/WAI/WCAG22/Techniques/general/G167

Content consequence:
- a visible action label cannot be designed independently from the accessible name;
- hidden wording should not silently change the command's identity or force speech-input users to remember another phrase.

---

## 2. Cross-domain dependency — a label cannot outrun the interaction contract

### SOURCE REUSE — Interaction I002

`research/interaction/I002-latency-pending-optimistic-retry.md` distinguishes accepted, pending, progressing, confirmed, failed, canceled and outcome-unknown states and treats retry safety as an operation-semantics question rather than a visual-button question.

### SYNTHESIS

An action label describes what the user is **authorizing or initiating**, not necessarily what the system has already successfully completed.

Therefore:
- `Submit` can truthfully initiate a submission;
- after activation, the UI may move into `Submitting…`;
- only confirmed success supports a completed-state message such as `Submitted`;
- if outcome is unknown, Content must not silently relabel the situation as failure.

### STUDIO JUDGMENT

Separate these layers:

1. **Command** — what the user requests.
2. **Object/scope** — what the command affects.
3. **Immediate product behavior** — what happens on activation.
4. **Commitment/persistence** — whether data is saved, sent, published, deleted, charged, etc.
5. **Outcome state** — pending, confirmed, failed, unknown, canceled.
6. **Recoverability** — reversible, undoable, replaceable, permanent, externally committed.

A button label may not need to contain all six. The surrounding interface can carry part of the meaning. But the complete interaction must not misrepresent them.

---

## 3. Foundation model — command semantic load

CD003 introduces a provisional model for deciding how specific a command label must be.

### Low semantic load

Use a short conventional label when:
- the action is low-risk;
- the object is visually/contextually unambiguous;
- persistence or external commitment is absent or already obvious;
- the same term is stable across the product/platform.

Examples that may be sufficient in the right context:
- `Continue`
- `Back`
- `Cancel`
- `Share`

### Higher semantic load

Add object, persistence or consequence information when one or more are true:
- multiple possible objects exist;
- the command persists or transmits data;
- the action is destructive or hard to reverse;
- the action accepts a legal/financial commitment;
- the action creates external side effects;
- the difference between save/submit/publish/sync matters;
- the surrounding text may not be read before activation;
- the same generic verb could mean materially different things nearby.

Examples:
- `Save and continue`
- `Delete account`
- `Submit report`
- `Accept and send`
- `Remove member`

### Critical distinction

**Specificity should increase with consequence ambiguity, not with writer anxiety.**

Longer labels are not automatically safer. The added words must encode a real distinction.

---

## 4. Command grammar is semantic before grammatical

### 4.1 Verb-first is a useful default, not a universal law

Apple and Microsoft both support action-oriented labels. A verb-first phrase often exposes the command quickly.

But labels such as `Next`, `Back`, `Done`, `Cancel`, `Settings` or platform-standard symbols can remain appropriate when their function is conventional and unambiguous.

### 4.2 Add the object when the action alone is underspecified

`Delete` may be sufficient inside a clearly scoped one-record confirmation.

`Delete account` is safer when:
- multiple deletable objects exist;
- the surrounding context may be skipped;
- deletion scope is consequential.

### 4.3 Add persistence when it changes what the user is authorizing

The GOV.UK `Continue` vs `Save and continue` distinction is adopted as an important Content principle:

> If persistence changes, the label may need to change.

A product must not say `Save and continue` when it only stores state transiently or locally if the user could reasonably interpret that as durable save.

### 4.4 Add commitment when it changes the transaction

`Confirm and send` and `Accept and send` are not cosmetic variants. They indicate different acts.

The Content requirement is to identify whether the user is:
- reviewing;
- confirming facts;
- agreeing to terms;
- transmitting data;
- authorizing payment;
- publishing to others.

Do not merge these acts under `OK` if the distinction matters.

### 4.5 Do not promise a result that activation does not guarantee

If activation starts an asynchronous process, the command label should generally describe the request, not an already-completed outcome.

Potentially misleading:
- `Downloaded` on a button that merely starts generation;
- `Synced` before remote confirmation;
- `Paid` before payment confirmation.

More faithful command labels may be:
- `Create export`
- `Sync now`
- `Pay`

The subsequent state message owns completion evidence.

---

## 5. Generic labels — when they are valid and when they fail

### `Continue`

Valid when:
- the only semantic act is advancing;
- no hidden persistence/commitment distinction matters.

Fails when:
- activation also saves, sends, accepts or charges and that fact is not otherwise sufficiently clear.

### `OK`

Valid mainly when:
- conventional dismissal/acknowledgment is genuinely the entire action;
- no more specific command is required.

Fails when:
- it conceals a consequential operation;
- the dialog asks a question that could be answered more explicitly.

### `Save`

Valid when:
- the product actually persists the current object in the expected scope.

Fails when:
- it also publishes/submits externally;
- save location/scope is ambiguous;
- it only caches locally while the user expects remote durability.

### `Delete`

Valid when:
- object and scope are unmistakable.

Fails when:
- several objects or levels are present;
- deletion is permanent and the label/context does not expose scope;
- the actual behavior is archive/remove-from-view rather than delete.

### `Retry`

Valid only after Interaction establishes that retry is safe and meaningful.

Fails when:
- the original outcome is unknown and repeating could duplicate an external effect;
- the product should first verify status or present a different recovery path.

This is a direct Content→Interaction dependency.

---

## 6. Destructive actions — wording, context and visual role are independent safety layers

### SOURCE synthesis

Apple provides destructive roles/styles. GOV.UK explicitly warns not to rely on red alone and recommends making context and button text clear.

### STUDIO JUDGMENT

For a consequential destructive action, audit at least:
- **verb accuracy** — delete, remove, archive, clear, discard are not synonyms by default;
- **object scope** — what exactly is affected?;
- **persistence** — temporary, recoverable, undoable, permanent?;
- **external effect** — only local state or shared/server/financial state?;
- **confirmation necessity** — does the action need a distinct confirmation step?;
- **safe alternative** — cancel/undo/back/retain?;
- **non-color communication** — is severity understandable without red styling?;
- **accessible name** — does the programmatic command preserve visible identity?

Content does not decide alone whether confirmation is required; Interaction owns the behavioral pattern. Content ensures the language accurately represents the resulting contract.

---

## 7. RELATED DOMAIN CHECK

### Type

Evidence checked:
- `research/type/T017-logmate-operational-data-typography-semantic-geometry-transfer.md`;
- current `progress/TYPE_STATUS.md`.

Reusable finding:
- real product strings and role-specific text can alter width, hierarchy and operational alignment.

Content consequence:
- semantically necessary labels such as `Save and continue` or explicit destructive objects must not be shortened merely to preserve a preferred button width.

Relationship: **DIRECT REUSE / FUTURE RENDER TRANSFER**.

### Color

Evidence checked:
- current `progress/COLOR_STATUS.md`.

Reusable finding:
- semantic visual roles can reinforce state/action but do not replace meaning.

Content consequence:
- destructive severity must not rely on red alone; wording/context must survive forced-colors and alternate themes.

Relationship: **REUSE**.

### Layout / Interaction

Evidence checked:
- `research/interaction/I002-latency-pending-optimistic-retry.md`;
- CD001 reuse of I004 ambiguous outcomes;
- current `progress/LAYOUT_STATUS.md`.

Reusable findings:
- request, pending, confirmed, failed and unknown outcome are separate;
- retry safety is behavioral/domain logic;
- action consequence/reversibility belong to Interaction.

Content consequence:
- action labels may initiate a process but must not pre-announce an unconfirmed result;
- `Retry` is unavailable as a content choice until Interaction validates it as a safe action.

Relationship: **DIRECT DEPENDENCY + SEMANTIC TRANSFER**.

### Web Design

Evidence checked:
- current `progress/WEB_STATUS.md`;
- W016 native/custom-button runtime finding summarized there.

Reusable finding:
- role/name exposure and actual activation behavior are separate contracts.

Content consequence:
- a perfect label on a behaviorally broken custom button is not a complete interface solution;
- future transfer must verify visible label/accessibility name and actual browser behavior together.

Relationship: **FUTURE TRANSFER VALIDATION**.

### Existing Content

- CD001 supplies object/state/action/consequence.
- CD002 supplies concept/designation consistency.

CD003 extension:
- action labels are compact expressions of a command contract, not isolated verbs.

---

## 8. Original practice — four command contracts

This is a controlled synthetic exercise. It tests semantic fidelity, not human preference.

### Case A — advance without persistence

Product facts:
- entered data stays only in the current in-memory step;
- activation moves to the next screen;
- no save occurs.

Candidates:
- `Continue`
- `Save and continue`
- `Next`

Critique:
- `Save and continue` is **REJECTED** because it falsely asserts persistence.
- `Continue` and `Next` are both semantically viable; choice between them requires product-flow consistency and possibly user evidence.

Verdict:
- `Continue` **KEEP as semantic control**.

### Case B — durable draft save + advance

Product facts:
- activation persists the draft;
- the user can leave and resume later;
- activation also advances to the next step.

Candidates:
- `Continue`
- `Save and continue`
- `OK`

Critique:
- `Continue` omits a material persistence fact;
- `OK` names no command;
- `Save and continue` represents both durable persistence and navigation.

Verdict:
- `Save and continue` **KEEP as semantic control**.

This is not proof that the exact phrase is optimal for every audience or language.

### Case C — permanent record deletion

Product facts:
- one selected record is permanently deleted;
- no undo exists;
- the screen contains other records and an account-level menu.

Candidates:
- `Delete`
- `Delete record`
- `Confirm`

Critique:
- `Delete` may be interpretable but the object scope is consequential;
- `Confirm` hides the action entirely;
- `Delete record` preserves verb + object scope.

Verdict:
- `Delete record` **KEEP as semantic control**.
- `Confirm` **REJECT**.

Interaction still owns whether a confirmation step is required.

### Case D — asynchronous export generation

Product facts:
- activation starts server-side export creation;
- the file may take time;
- download becomes available only after successful generation;
- generation can fail.

Candidates:
- `Download`
- `Create export`
- `Export ready`

Critique:
- `Export ready` falsely describes a completed state before activation;
- `Download` may be misleading because no downloadable file yet exists;
- `Create export` accurately names the initiated action.

Verdict:
- `Create export` **KEEP as current semantic control**.
- after confirmation, the resulting action may become `Download export`.

### Practice result

The four cases show that label validity changes when persistence, object scope or temporal state changes even if the visual component remains the same.

The common rule is not “always use longer labels.” It is:

> Encode the smallest amount of language that preserves the distinctions the user is actually authorizing.

---

## 9. Reproducible non-human command audit — version 0.1

For each consequential action, record:

| Field | Question |
| --- | --- |
| command | What is the user asking the system to do? |
| object | What object/scope is affected? |
| persistence | Is anything saved, transmitted, published, charged, deleted or otherwise committed? |
| temporal status | Does activation complete immediately or start pending work? |
| reversibility | Can the action be canceled, undone, restored or retried safely? |
| label | What visible phrase represents the command? |
| accessible name | Does it preserve the same command identity? |
| context dependency | Which meaning is supplied by surrounding UI rather than the label? |
| semantic risk | What incorrect outcome might a user infer? |
| validation | Is semantic review enough, or is user testing needed? |

### Automatic/expert-checkable failure classes

- `FALSE PERSISTENCE` — label says save/submit/publish when the product does not perform that act.
- `FALSE COMPLETION` — label describes a completed outcome before it is confirmed.
- `OBJECT AMBIGUITY` — action affects multiple possible scopes but label/context does not distinguish them.
- `CONSEQUENCE HIDING` — generic command hides a material legal/financial/destructive act.
- `UNSAFE RETRY LANGUAGE` — retry offered before Interaction verifies retry safety.
- `TERM COLLISION` — same action word represents materially different commands in the same task context.
- `ACCESSIBLE-NAME DRIFT` — visible and programmatic names imply different commands.
- `HUMAN VALIDATION NEEDED` — multiple semantically valid candidates remain and comprehension/efficiency cannot be established from product facts alone.

### Evidence boundary

This audit can reject semantically false labels. It cannot determine which of several truthful labels users understand fastest or prefer most.

---

## 10. HANDOFFS TO OTHER SPECIALISTS

### Interaction

CD003 reinforces that command wording must follow the actual persistence, temporal, recovery and consequence contract. If Content cannot truthfully name an action because behavior is ambiguous, the dependency belongs back to Interaction/product logic.

### Web

A later browser transfer should verify command labels together with:
- correct native/custom control semantics;
- focus/keyboard activation;
- visible/accessibility-name consistency;
- pending/disabled/busy states;
- double-submission behavior where consequential.

### Type

Use final semantic labels, not placeholder `OK`/`Save`, when testing component width, localization and text scaling. Geometry should adapt to necessary wording.

### Color

Destructive/warning visual treatment must reinforce rather than carry the entire consequence signal.

---

## 11. OPEN questions after CD003

1. When does surrounding context make a generic action label sufficiently specific?
2. Which empirical methods best compare truthful command labels without reducing testing to preference polling?
3. How should Korean action labels handle verb-final grammar and object omission relative to English verb-first conventions?
4. When should `Cancel`, `Back`, `Close`, `Discard` and `Exit` be modeled as distinct product actions?
5. How should actions be named when one activation performs multiple commits or crosses local/remote boundaries?
6. How should voice interfaces and command discoverability alter action-label design?
7. What content architecture best supports one semantic command across compact mobile, desktop menu, notification and accessibility surfaces?

---

## Current conclusion

`SOURCE`:
- Apple, GOV.UK and Microsoft converge on labels that communicate action purpose clearly;
- GOV.UK provides concrete evidence that label wording should change with persistence and commitment semantics;
- W3C constrains the relationship between visible labels and accessible names;
- Interaction evidence distinguishes command initiation from pending/confirmed/unknown outcomes.

`SYNTHESIS`:
- an action label is a compact representation of a command contract, not merely a verb.

`STUDIO JUDGMENT`:
- choose the shortest label that preserves the distinctions the user is actually authorizing;
- increase specificity when object, persistence, commitment, destructive scope or outcome uncertainty materially changes the action;
- never let Content invent retry safety or completion certainty that the Interaction contract does not provide.

`OPEN`:
- truthful alternatives still require appropriate human evidence for claims about comprehension, speed, confidence or preference;
- Korean command-language transfer remains unvalidated.

Stage 1 remains **IN STUDY / PRACTICE — NOT PASSED**.

Next recommended study: **CD004 — plain language, scanning, information order and sufficiency trade-offs**.