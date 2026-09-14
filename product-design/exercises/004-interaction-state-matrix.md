# Exercise 004 — Interaction State Matrix

Status: PRACTICE / CRITIQUE INCLUDED

Research basis:
- `research/007-interaction-agency-feedback-errors.md`
- `research/004-accessibility-reflow-targets-focus.md`

## Objective

Design three small interaction systems without relying on visual polish to hide weak semantics.

Each flow must explicitly account for:

- discoverability;
- action/object mapping;
- immediate feedback;
- pending/system status;
- error prevention;
- error identification;
- recovery/undo;
- keyboard or non-gesture alternatives where relevant.

---

## Flow A — Save an edited record

### Initial state

Object: one editable record.

Visible actions:
- `Save`
- `Cancel`

State cues:
- changed fields are visibly edited;
- no fake `Saved` message before persistence succeeds.

### Activation

User activates `Save`.

### Pending state

Design response:
- primary action becomes temporarily non-repeatable;
- label/status communicates `Saving…` or equivalent;
- edited content remains visible;
- keyboard focus remains predictable;
- the interface does not navigate away solely to signal activity.

### Success

Design response:
- status changes to `Saved` or returns to stable saved state;
- focus does not jump to a transient message;
- the edited record remains inspectable;
- repeated saves are avoided if no new changes exist.

### Failure

Design response:
- entered values remain intact;
- message identifies that save failed;
- a concrete recovery path is available: `Retry`, `Save later`, or equivalent depending on product semantics;
- the failure is not represented by color alone.

### Critique

**KEEP**
- Separates pending from success.
- Preserves user work on failure.
- Feedback severity matches the event.

**REJECT**
- Toast saying `Saved` immediately on tap before persistence result.
- Clearing the form on failure.
- Generic alert with only `OK` and no recovery route.

---

## Flow B — Delete an item with meaningful consequence

### Initial state

Object: one stored item.

Visible primary task is *not* Delete. Delete sits in a secondary/destructive location with an explicit label.

### Prevention strategy

Before adding a confirmation dialog, ask:

1. Is deletion reversible?
2. Is accidental activation likely?
3. Is the consequence severe enough to justify interruption?

### Preferred reversible model

Activation:
- Delete removes the item from the active list.

Feedback:
- passive confirmation communicates `Deleted`.
- `Undo` remains available for a meaningful interval or until navigation/context change, if product architecture permits.

### Irreversible model

If deletion cannot be undone and consequence is significant:
- use confirmation that names the object/consequence;
- actions are explicit (`Delete` / `Cancel`), not ambiguous (`Yes` / `No`);
- destructive action is not preselected by keyboard focus unless platform convention and risk justify it.

### Critique

**KEEP**
- Recovery is preferred over routine confirmation when technically and semantically credible.
- Confirmation is proportional to consequence, not a ritual for every delete.

**REJECT**
- Trash icon with no label in a context where meaning is ambiguous.
- `Are you sure?` with no object or consequence.
- irreversible delete triggered by a swipe/gesture with no alternative or recovery.

---

## Flow C — Reorder a list

### Initial state

Rows expose order as a property of the collection.

### Pointer/touch route

- drag handle may support direct manipulation;
- the moved row provides continuous position feedback;
- insertion position is visible before drop.

### Alternative operation

The same semantic result is achievable without dragging through one or more of:

- `Move up` / `Move down`;
- keyboard commands;
- explicit destination/position menu.

### Completion feedback

- final order is immediately visible;
- screen-reader/assistive route communicates new position where implementation permits;
- if order persistence is asynchronous, pending/failure behavior is separate from drag completion.

### Failure state

If persistence fails:
- do not silently show an order that will later revert without explanation;
- either revert with an explicit message or retain local state with a clear unsaved/pending status, depending on product semantics.

### Critique

**KEEP**
- Gesture and semantic operation are separated.
- Visual drag feedback is not treated as persistence success.

**REJECT**
- drag-only control;
- invisible drop target;
- order changes without any confirmation of current position.

---

## Cross-flow action / destination / state classification

| Element | Category | Why |
| --- | --- | --- |
| Save | Action | commits a change |
| Cancel | Action / escape | abandons current edit context |
| Retry | Action | repeats failed operation |
| Settings | Destination | navigates to another context |
| Saved | State | describes system condition |
| Saving… | State | describes pending condition |
| Selected | State | describes current selection |
| Undo | Action | reverses previous action |

The exercise uses this classification to prevent visual hierarchy from conflating navigation, commands, and status.

## Failure-first review

### Visually clean but semantically weak candidate

Candidate:
- one minimal `Save` icon;
- no pending state;
- green check animation after tap;
- failure appears as a red border around the page.

Why it fails:
- icon may be recall-heavy;
- success is claimed before actual system confirmation;
- failure is color-dependent and does not identify the problem;
- no recovery route;
- status is transient and may be missed.

**Disposition: REJECT.**

## What this exercise proves

Practice evidence now exists for:

- action/state separation;
- pending/success/failure modeling;
- recovery before interruption;
- error preservation;
- destructive-action proportionality;
- drag alternatives;
- recognition/familiarity reasoning.

## What remains before PASS

- interactive prototype or implementation-level test;
- keyboard traversal evidence;
- assistive-technology/status-message evidence;
- a second unrelated product context;
- measured user or expert evaluation of discoverability;
- explicit navigation-model exercise beyond microflows.

Status implication: `Interaction foundations` may move to **PRACTICE**, not PASS.