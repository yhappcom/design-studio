# Study 015 — Directness, State, Modes, and Reversibility

Status: FOUNDATION STUDY / paired interaction exercise and critique included separately.

## Question

What makes an interaction feel directly connected to the user’s intention, and how should system state, modes, asynchronous work, and reversibility be designed so that control remains understandable?

## Scope

This study extends `research/007-interaction-agency-feedback-errors.md`.

Study 007 established agency, feedback, status, error prevention, and recovery. Study 015 goes deeper into the **action-to-state relationship**: how an intention becomes an input, how the system changes state, how that state is exposed, and how the user can reverse or leave the resulting condition.

This is an Interaction Specialist foundation module. It does not claim that direct manipulation is always superior to commands, forms, automation, or indirect workflows.

---

## SOURCE — direct manipulation was originally defined by more than pointing or dragging

Shneiderman’s 1983 account of direct manipulation identifies central characteristics including visible objects of interest, rapid/incremental/reversible operations, and replacing complex command syntax with manipulation of the represented objects.

Sources:
- https://www.cs.umd.edu/~ben/publications.html
- DOI: 10.1109/MC.1983.1654471

### SYNTHESIS

Direct manipulation is not synonymous with a gesture.

A draggable object can still be indirect if:

- the user cannot predict what the drag changes;
- the visible object is only a proxy for a hidden target;
- the result is delayed or silently rejected;
- the operation is hard to reverse;
- the final system state is not visible.

Conversely, a keyboard action can participate in a direct-feeling interaction if its mapping and result are clear, immediate, incremental, and reversible.

### STUDIO JUDGMENT

Evaluate **directness of the action-state loop**, not whether the control visually resembles physical manipulation.

---

## SOURCE — Hutchins, Hollan, and Norman separate directness into distance and engagement

Hutchins, Hollan, and Norman’s analysis of direct manipulation provides a cognitive account rather than treating direct manipulation as a visual style. Their framework distinguishes:

- **semantic distance** — the relationship between the user’s goals and the meaning available in the interface language;
- **articulatory distance** — the relationship between the physical/formal expression of an action or output and its meaning;
- **direct engagement** — interacting with a represented world in a way that minimizes the sense of an intervening interface.

The paper also connects continual representation of system state and rapid feedback with the user’s ability to evaluate the outcome of actions.

Sources:
- https://www.tandfonline.com/doi/abs/10.1207/s15327051hci0104_2
- DOI: 10.1207/s15327051hci0104_2

### SYNTHESIS — two different distances can fail independently

Example: changing the scheduled departure time of a flight record.

A control can have low articulatory distance but high semantic distance:

- dragging a clock hand is physically direct;
- but if the task concept is “block-off time in UTC on a specific date,” the analog clock metaphor may obscure timezone/date semantics.

A control can have low semantic distance but higher articulatory distance:

- typing `23:40` directly expresses the required domain value;
- but text entry requires more precise articulation than moving a slider.

Therefore “more graphical” does not automatically mean “more direct.”

### STUDIO JUDGMENT

Choose an interaction representation by asking separately:

1. Does the interface expose the **right domain concept**?
2. Does the physical/input form map clearly to that concept?
3. Is the resulting state continuously or promptly inspectable?

---

## SOURCE — mode errors depend strongly on how mode state is communicated and maintained

Sellen, Kurtenbach, and Buxton experimentally studied mode errors in a text-editing task. Both visual and kinesthetic feedback reduced mode errors in their experiments. The non-latching, user-maintained mode condition provided especially salient information about current mode state and reduced mode errors more effectively than the tested system-maintained mode condition.

Sources:
- https://www.microsoft.com/en-us/research/publication/the-prevention-of-mode-errors-through-sensory-feedback/
- https://www.tandfonline.com/doi/abs/10.1207/s15327051hci0702_1
- DOI: 10.1207/s15327051hci0702_1

### SYNTHESIS

The transferable result is **not** “use a foot pedal” or “all latched modes are bad.” The relevant design principle is that mode state must remain salient enough that the user’s next action is interpreted in the intended context.

Potential ways to increase mode salience in software include:

- persistent mode labels;
- changed control vocabulary while the mode is active;
- explicit entry and exit actions;
- constrained action sets;
- cursor/pointer or focus-context changes where appropriate;
- user-maintained temporary states for short operations;
- non-color-only state signals.

### STUDIO JUDGMENT

A mode is especially risky when:

- the same action produces materially different outcomes in different modes;
- mode entry is easy to miss;
- the mode persists after the user’s local goal is complete;
- leaving the mode is ambiguous;
- the current mode is shown only transiently or by weak decoration.

---

## SOURCE — complex interactive behavior benefits from explicit state modeling

Harel’s Statecharts extended conventional state-transition diagrams with hierarchical states, concurrency, and communication to describe complex reactive systems compactly.

Sources:
- https://www.sciencedirect.com/science/article/pii/0167642387900359
- https://weizmann.elsevierpure.com/en/publications/statecharts-a-visual-formalism-for-complex-systems/
- DOI: 10.1016/0167-6423(87)90035-9

### SYNTHESIS

Statecharts are a system-modeling formalism, not a UX rule. The transferable method is nevertheless highly useful for interaction design:

> Before styling a complex control, identify its meaningful user-facing states and legal transitions.

Examples:

- idle → editing → validating → saving → saved;
- idle → dragging → locally-updated → syncing → confirmed;
- normal → multi-select mode → selection-present → bulk-action pending → normal;
- active → delete-requested → undo-window → committed deletion.

The implementation may contain many more internal states. Interaction design needs a **user-facing state model** that exposes the distinctions necessary for prediction and recovery without exposing irrelevant engineering detail.

---

## SOURCE — reversible operations support control, but the target of undo must be predictable

Apple’s current Human Interface Guidelines describe undo and redo as ways to reverse actions and support safe exploration. The guidance also emphasizes helping people predict what undo/redo will affect and making the result apparent.

Source:
- https://developer.apple.com/design/human-interface-guidelines/undo-and-redo

### SYNTHESIS

Reversibility is not merely the presence of an Undo button.

A reversible interaction needs:

- a clearly identifiable committed action;
- a defined undo scope;
- a predictable target when multiple actions have occurred;
- a visible result of reversal;
- a policy for what happens after remote synchronization or another user/device changes the same object.

### STUDIO JUDGMENT

For risky but reversible operations, **perform + undo** can preserve flow better than repeated confirmation. For high-consequence or legally/financially binding actions, confirmation/review may still be necessary. The choice depends on consequence, reversibility, and recovery cost.

---

## SOURCE — accessibility standards constrain invisible or surprising state changes

WCAG 2.2 includes several relevant requirements for web interfaces:

- focus order must preserve meaning and operability when sequential navigation matters (2.4.3);
- receiving focus must not unexpectedly initiate a change of context (3.2.1);
- changing a setting must not unexpectedly change context unless the behavior is disclosed (3.2.2);
- error prevention for specified high-consequence submissions includes reversible, checked, or confirmed mechanisms (3.3.4);
- user-interface states/properties must be programmatically available where required by 4.1.2;
- status messages must be programmatically determinable without necessarily moving focus (4.1.3).

Source:
- https://www.w3.org/TR/WCAG22/

### SYNTHESIS

A state that exists only in pixels is incomplete.

For interactive state to be robust it may need to be available simultaneously through:

- visual presentation;
- programmatic state/role/value;
- keyboard/focus behavior;
- assistive-technology announcement when appropriate;
- stable interaction consequences.

This does not mean every state should be announced. The communication channel must match the state’s importance and interruption cost.

---

# Action-state coupling model

For every significant interaction, document the following sequence.

## 1. Intent

What is the user trying to change, choose, move, reveal, or commit?

## 2. Object

What visible/domain object does the action apply to?

## 3. Articulation

How is the intent expressed?

Examples: tap, click, drag, key command, text entry, voice, selection + action.

## 4. Transition

What state transition does the action request?

The transition must be defined before animation is specified.

## 5. Feedback

What evidence shows that the action was accepted, is pending, failed, or completed?

## 6. Commitment

Is the current result:

- preview only;
- local but not persisted;
- persisted locally;
- queued for synchronization;
- remotely confirmed;
- irreversible/externally committed?

## 7. Recovery

Can the user cancel, revert, undo, retry, edit, or restore?

## 8. Mode/context

Does the meaning of the next action depend on a persistent mode or context? If yes, how is that context made salient and how does it end?

---

# Interaction design consequences

## Directness is a loop, not a control type

A direct-feeling interaction has a short and intelligible loop:

**intent → articulation → visible transition → interpretable state → optional reversal**

A gesture alone does not satisfy this loop.

## Preview, pending, and committed are different states

Do not collapse them into one optimistic success appearance when the distinction affects user decisions.

Example: dragging an item into a new order may update the local layout immediately while remote synchronization is still pending. The user-facing model may legitimately show the new order immediately, but it must have a policy for synchronization failure and conflict.

## Animation is evidence of transition, not the state itself

If removing motion makes it impossible to know the current state, the design has encoded semantics only in animation. Reduced-motion alternatives and static end states must preserve meaning.

## Modes need explicit ownership and termination

For every mode, define:

- entry trigger;
- visible indication;
- actions whose meaning changes;
- exit trigger;
- whether the mode survives navigation/interruption;
- what happens to incomplete work on exit.

## Reversibility should be designed with the data lifecycle

Undo before persistence, undo after local persistence, and undo after remote side effects may require different mechanisms. “Undo” is therefore an interaction + data-contract question, not a button-level feature.

---

# Failure modes

- drag interaction that visually completes before the system accepts the change, with no pending state;
- optimistic success that silently rolls back after a network failure;
- a selection/edit mode indicated only by a small tint change;
- mode entry that changes the meaning of familiar controls without persistent indication;
- a cancel action that closes the UI but leaves partial changes committed;
- an Undo command whose target is ambiguous after several asynchronous actions;
- destructive operations made “safe” only by a confirmation dialog instead of also considering reversibility;
- loading indicators that do not distinguish “working,” “waiting for network,” and “blocked”; 
- keyboard and assistive-technology paths that enter a state the pointer path can leave, but have no equivalent exit;
- using animation as the only evidence that a state changed;
- direct manipulation used where precise textual/batch command entry better matches the domain concept.

---

# Practice gate for this study

Exercise 015 must model at least three flows and include all of the following across them:

1. one incremental direct-manipulation flow;
2. one asynchronous/pending transition;
3. one persistent or temporary mode;
4. one destructive or high-cost action with a defined recovery strategy;
5. explicit preview/local/persisted/confirmed distinctions where relevant;
6. keyboard/non-pointer alternatives;
7. a failure path;
8. an explicit KEEP / REWORK / REJECT critique.

This study adds foundation evidence but does **not** move `Interaction foundations` to PASS without an interactive prototype and real keyboard/status-message validation.

---

# OPEN

1. Study pointing/target-acquisition models and Fitts’ law separately; motor performance is not covered by this block.
2. Study response-time perception, latency masking, optimistic UI, and progress feedback using controlled empirical sources rather than folklore thresholds.
3. Study navigation/history as a state model, including back behavior, deep links, restoration, and interruption recovery.
4. Study gesture discoverability and expert shortcuts without conflating efficiency with learnability.
5. Validate state communication using keyboard and assistive technology in an actual interactive prototype.
