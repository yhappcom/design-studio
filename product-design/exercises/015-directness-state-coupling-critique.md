# Exercise 015 Critique — Directness and Action-State Coupling

Status: CRITIQUE

Paired artifact: `product-design/exercises/015-directness-state-coupling-practice.md`

Research basis: `research/015-directness-state-modes-reversibility.md`

## Purpose

Evaluate whether the state models express user control, mode awareness, asynchronous commitment, and recovery before visual polish or animation is added.

This critique evaluates the **interaction specification**, not an implemented prototype. Timing, focus movement, screen-reader announcements, pointer feel, and actual synchronization behavior remain unvalidated.

---

# Flow A — Reorder a prioritized list

## KEEP

### Preview and commitment are separated

`Dragging` is a preview state, `LocalCommitted` is a local state change, and `Syncing`/`Confirmed` represent persistence progression. This avoids a common modeling error where visual placement and remote truth are treated as one event.

### Temporary mode is user-maintained

The drag state lasts only while the user actively manipulates the item and ends through drop or cancel. This reduces persistent mode ambiguity.

### Keyboard alternative preserves the same conceptual operation

The keyboard path still expresses “move this item to another position” rather than exposing a separate administrative command model.

## REWORK

### Define undo while synchronization is pending

The current model says undo is available after local commit but does not yet define the exact concurrency policy.

Questions to resolve in implementation:

- Does undo cancel a queued sync request or enqueue a compensating change?
- What if remote confirmation arrives after the user has already undone locally?
- What if another device changed the order concurrently?
- Which state is considered the last recoverable truth?

These are interaction/data-contract questions and must not be left to incidental implementation behavior.

### Define failure presentation without freezing the task

A sync failure may not justify blocking the entire list. The product needs a policy for whether the locally edited order remains usable while unsynced, whether it is marked as pending, and when conflict resolution becomes necessary.

## REJECT

- success visuals before the relevant commitment level is reached;
- silent rollback;
- making drag the only reorder path;
- removing the item from its prior position before a valid destination exists if that causes destructive-looking instability.

---

# Flow B — Multi-select mode and bulk deletion

## KEEP

### The mode has an explicit contract

The specification documents entry, altered item behavior, visible mode state, termination, focus implications, and destructive scope. This is stronger than merely changing toolbar appearance.

### Mode state is not color-only

Text/structure and changed action vocabulary are required, which reduces dependence on subtle visual detection.

### Destructive scope is tied to selected objects

The action operates on a visible selected set instead of presenting a generic “Delete?” question disconnected from the current context.

## REWORK

### Confirmation plus undo may be excessive in low-risk contexts

The exercise deliberately uses both to expose the mechanisms, but product design should not automatically stack every safety mechanism. The appropriate design depends on:

- number and recoverability of objects;
- cost of accidental deletion;
- whether deletion is local or externally consequential;
- whether undo can restore all metadata and relationships;
- user frequency and expert workflow cost.

### Exit behavior needs interruption cases

Define what happens when selection mode is interrupted by:

- app backgrounding;
- route/deep-link change;
- device rotation or adaptive-layout change;
- another device modifying selected records;
- timeout/session loss if relevant.

### Focus movement needs implementation proof

Changing the action area in selection mode can create keyboard and screen-reader focus discontinuity. Static state modeling is not enough to prove operability.

## REJECT

- tint-only mode indication;
- changing tap/click meaning without persistent evidence;
- selection persistence across navigation by accident rather than policy;
- destructive scope that is not available to assistive technology before commitment.

---

# Flow C — Rename a cloud document

## KEEP

### The exercise correctly separates semantic from articulatory directness

Typing a name is not physical mimicry, but it maps directly to the domain concept. This is useful evidence against treating graphical manipulation as inherently more direct.

### Draft preservation is explicit

Validation and remote errors preserve the entered value, reducing recovery cost and protecting user work.

### Conflict is modeled as a distinct state

A remote conflict is not collapsed into generic failure. This allows the recovery UI to explain what changed and what choices remain.

## REWORK

### Conflict semantics need a product-specific model

A file name conflict could mean several things:

- duplicate-name constraint;
- concurrent rename by another device/user;
- object version conflict;
- lost permission;
- remote object deletion.

Each has different recovery. `Conflict` is currently a useful umbrella state but not a sufficient production specification.

### Offline policy is missing

If rename can be queued offline, the commitment ladder becomes:

`draft → locally persisted → queued → remotely accepted/conflicted`.

The interface should expose only the distinctions that affect user decisions while still preserving enough state for recovery.

## REJECT

- closing the editor and silently discarding a valid unsaved draft;
- generic “Something went wrong” for a known conflict;
- displaying the new name as irrevocably saved when it is only locally pending;
- retry loops that repeatedly submit an impossible conflicting state.

---

# Cross-flow findings

## 1. Directness belongs to the whole loop

The strongest transferable principle is:

**intent → articulation → transition → state evidence → commitment → recovery**

A visually direct input can fail if later stages become opaque. A less graphical input can remain direct if it represents the domain concept clearly and the result is easy to evaluate.

## 2. User-facing state is not identical to implementation state

The product may internally contain dozens of network, cache, database, and animation states. The interaction model should expose the subset necessary for:

- prediction;
- meaningful action choice;
- error understanding;
- recovery.

Exposing every engineering state increases complexity; hiding every commitment distinction creates false certainty.

## 3. Preview, local state, pending state, and confirmed state must be consciously collapsed or separated

They do not always need four different visual treatments. The design decision is whether a distinction changes what the user should know or can safely do next.

## 4. Modes need stronger evidence than normal transient states

A mode changes the interpretation of future actions. Therefore it needs persistent evidence proportional to that semantic change and a predictable exit.

## 5. Undo is a state transition policy, not a decorative affordance

The design is incomplete until undo target, scope, persistence timing, conflict policy, and result feedback are specified.

## 6. Accessibility is part of the state model

If a state or transition exists visually but has no equivalent keyboard path, programmatic state, or appropriate status communication, it is not the same interaction for all users.

---

# KEEP / REWORK / REJECT summary

## KEEP

- explicit state models before motion styling;
- semantic/articulatory directness distinction;
- preview/local/remote commitment vocabulary;
- user-maintained temporary states where appropriate;
- explicit mode contracts;
- recovery designed alongside primary success flow;
- keyboard/non-pointer equivalence at the conceptual-operation level.

## REWORK

- concurrency and multi-device conflict policy;
- exact focus movement in dynamic modes;
- live-region/status-message behavior;
- undo behavior during pending remote operations;
- interruption/restoration behavior;
- product-specific thresholds for confirmation versus undo-only recovery.

## REJECT

- gesture = directness;
- animation = state;
- visual success = persistence success;
- color-only mode awareness;
- hidden commitment levels when they change user decisions;
- implementation state machine copied directly into the user-facing interface;
- universal use of confirmation dialogs for destructive actions.

---

# Gate result

**Result: advance `Interaction foundations` from PRACTICE to CRITIQUE, not PASS.**

Rationale:

- source study now covers agency/feedback/errors plus directness, semantic/articulatory distance, modes, reversibility, and explicit state modeling;
- original exercises now include action-state matrices and three state-modeled flows with failure/recovery paths;
- explicit critique and KEEP/REWORK/REJECT evidence exists.

Remaining before PASS:

1. implement at least one interactive navigation/state prototype;
2. keyboard-test every transition and exit path;
3. validate status/error communication with assistive technology;
4. test an asynchronous failure and recovery in a running environment;
5. transfer the method to another interaction domain after implementation evidence exists.
