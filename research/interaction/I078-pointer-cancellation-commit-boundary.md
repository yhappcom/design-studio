# I078 — Pointer cancellation and reorder commit boundary

Status: PRACTICE / TRANSFER VALIDATION OPEN

## Question
After I077 establishes drag/non-drag semantic equivalence, can every pointer reorder path distinguish preview/press from committed mutation and let an accidental pointer action abort without corrupting transaction, focus, recovery, or projection truth?

## Source
WCAG 2.2 SC 2.5.2 Pointer Cancellation (Level A) requires single-pointer functionality to satisfy No Down-Event, Abort or Undo, Up Reversal, or Essential. W3C Understanding guidance prefers up-event activation for ordinary controls and explicitly treats drag-and-drop as a complex action where abort or undo becomes important. G210 gives drag cancellation patterns; G212 recommends native/up-event activation for ordinary controls. Flutter TapGestureRecognizer likewise distinguishes tap-up from tap-cancel: a sequence that loses the gesture arena after tap-down does not become a tap.

## Practice contract
For every reorder action record `semantic_object_id`, `pointer_id/type`, `interaction_path`, `phase`, `candidate_destination`, `commit_event`, `tx_id`, `projection_hash_before/after`, `focus_owner`, and `recovery_eligibility`.

Phases are semantic, not visual: `idle → pressed/preview → committed | cancelled`. A press/drag preview may expose affordance but must not create a committed reorder transaction. Ordinary Move controls should commit on platform activation/up-event unless an essential exception is demonstrated. Drag must support an abort/undo path consistent with SC 2.5.2.

## Scenario family
1. Move control: down inside → move outside → up outside = no committed mutation.
2. Move control: down/up inside = exactly one transaction.
3. Drag: pick up → return/release at origin or approved abort area = no net committed reorder, or an explicitly reversible transaction if that is the implementation contract.
4. Drag: valid drop = exactly one committed mutation.
5. Pointer cancel / gesture-arena loss = no accidental mutation.
6. Cancel after preview followed by keyboard or explicit single-pointer alternative = only the later resolved action mutates.
7. Repeat each with first/middle/last, boundary no-op, system group, Undo and Reset eligibility.

## Critique / acceptance
FAIL if pointer-down alone mutates an ordinary reorder control, cancelled preview changes the projection hash, cancellation creates misleading success/recovery content, a cancelled drag steals semantic focus, or drag/non-drag paths produce different committed object/destination truth.

This is non-human interaction evidence. Motor-error rate, perceived predictability, discoverability and representative-pilot usability remain OPEN.