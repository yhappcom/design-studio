# Study 007 — Interaction Foundations: Agency, Familiarity, Feedback, Status, and Error Recovery

Status: FOUNDATION STUDY / paired scenario exercise included separately.

## Question

What makes an interaction feel understandable and trustworthy before visual styling is applied?

## SOURCE — agency, familiarity, and feedback

Apple's 2026 Design Principles emphasize three relevant ideas:

- **Agency:** help people accomplish goals, keep them informed, and make recovery from mistakes easy.
- **Familiarity:** build on concepts and interaction patterns people already understand, and apply behavior consistently.
- **Feedback:** provide clear signals about availability, change, success, failure, warnings, and next steps.

Sources:
- https://developer.apple.com/design/human-interface-guidelines/design-principles
- https://developer.apple.com/design/human-interface-guidelines/feedback

### Studio synthesis

An interface is easier to learn when four layers agree:

1. **perceived possibility** — the person can tell what can be acted on;
2. **mapping** — the action appears connected to the object/result it affects;
3. **feedback** — the system visibly communicates what happened;
4. **recovery** — mistakes are reversible or correctable without disproportionate cost.

A visually attractive control that fails one of these layers is not a successful interaction.

## SOURCE — structure and navigation should answer location and next action

Apple's navigation guidance and design teaching emphasize that people should be able to understand where they are, what they can do, and where they can go next. Familiar navigation structures can reduce unnecessary learning while still allowing a product to retain personality.

Sources:
- https://developer.apple.com/design/human-interface-guidelines/navigation-and-search
- https://developer.apple.com/videos/play/wwdc2022/10001/
- https://developer.apple.com/tutorials/develop-in-swift/organize-your-features

### Studio consequence

Navigation novelty carries a burden of proof.

A custom navigation treatment is acceptable only if:

- destinations remain recognizable;
- current location is legible;
- back/escape behavior remains predictable;
- discoverability is not materially worse than a familiar control without compensating value.

Personality may alter presentation. It should not silently alter the user's mental model of destination/action/state.

## SOURCE — status changes must be perceivable without stealing focus

WCAG's Status Messages criterion addresses changes that need to be communicated without forcing keyboard focus onto the message. Its intent is to make important content changes perceivable to assistive technology users without unnecessary interruption.

Source:
- https://www.w3.org/WAI/WCAG21/Understanding/status-messages

### Studio synthesis

A professional feedback system should distinguish:

- **passive status** — saved, synced, results updated;
- **action success/failure** — a task completed or failed;
- **warning** — a meaningful risk before commitment;
- **blocking error** — the task cannot continue;
- **destructive confirmation** — only when consequence and reversibility justify interruption.

Not every state deserves a modal alert.

## SOURCE — error design should help avoidance and correction

WCAG Input Assistance states the goal directly: help users avoid and correct mistakes. Related success criteria require descriptive error identification and, when known, useful correction suggestions.

Sources:
- https://www.w3.org/WAI/WCAG22/Understanding/input-assistance
- https://www.w3.org/WAI/WCAG22/Understanding/error-identification
- https://www.w3.org/WAI/WCAG22/Understanding/error-suggestion.html

WCAG 2.2 also adds Redundant Entry guidance to reduce repeated input burden in the same process.

Source:
- https://www.w3.org/WAI/WCAG22/Understanding/redundant-entry.html

### Studio synthesis — error hierarchy

Prefer, in order where appropriate:

1. **prevent** the error through constraints, clear labels, defaults, and input design;
2. **detect early** when feedback is reliable and non-disruptive;
3. **identify precisely** what is wrong;
4. **suggest a correction** when the system knows one;
5. **preserve entered work**;
6. **support undo/reversal** when possible.

A confirmation dialog is not a substitute for good prevention and recovery.

## Recognition vs recall

The studio uses the following operational distinction:

- **recognition-heavy interaction:** visible options, familiar placement, persistent context, labeled actions;
- **recall-heavy interaction:** hidden gestures, unlabeled icons with uncommon meaning, command syntax, remembering values or prior steps.

Recall is not always wrong — expert workflows may justify it — but hidden knowledge should be chosen deliberately and paired with discoverable paths when the audience is broader.

This principle is consistent with Apple's familiarity guidance and WCAG's effort-reduction direction, including redundant-entry and consistent-help requirements.

## Action / destination / state separation

Three categories should not be visually conflated:

### Action
Changes something now: Save, Delete, Add, Retry.

### Destination
Moves to another place/context: Settings, Search, Detail, Log.

### State
Describes or toggles current condition: On/Off, Selected, Synced, Draft.

The same visual component may sometimes implement more than one category, but the semantic distinction remains useful for hierarchy and feedback design.

## Interaction foundation audit

For any proposed control or flow, ask:

### Discoverability
- What tells the user this can be acted on?
- Is the visible cue familiar enough for the audience?

### Mapping
- Is it clear what object/result this action affects?
- Are destructive actions spatially or semantically separated from benign actions?

### Feedback
- What changes immediately after activation?
- Is success/failure communicated at the right level of interruption?

### Status
- Can the user tell whether work is saved, pending, unavailable, selected, or in progress?

### Recovery
- Can the user undo, retry, edit, or return?
- Is entered work preserved after an error?

### Accessibility
- Does the same interaction work with keyboard/assistive technology?
- Does feedback remain available without color or transient animation alone?

## Common failure modes

- icon-only novelty that requires memorization;
- a button whose label describes a destination but behaves as a destructive action;
- optimistic success visuals before the operation is actually complete;
- errors shown only by red borders;
- generic "Something went wrong" messages with no recovery path;
- modal alerts for routine passive status;
- irreversible destructive actions without undo/confirmation proportional to risk;
- asking for the same information again because the implementation is stateless;
- hidden gestures as the only operation route.

## Practice gate

Before `Interaction foundations` can PASS:

1. map at least three microflows from action → system state → feedback → recovery;
2. include one destructive action;
3. include one asynchronous/pending state;
4. include one form validation/error case;
5. distinguish action, destination, and state controls;
6. provide keyboard/non-gesture alternatives where relevant;
7. critique at least one flow that is visually clean but semantically weak;
8. apply the method in a second product context.

The accompanying Exercise 004 begins this practice; the domain remains below PASS.