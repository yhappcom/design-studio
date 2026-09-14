# L006 Extension — Pointer Capture, Touch Ownership, Nested Dismissal, and Lost-Invoker Recovery

Status: **PRACTICE + CRITIQUE / HIGHER-FIDELITY CHROMIUM TRANSFER — pointer-capture failure→revision, touch hit ownership, nested dismissal order, and lost-invoker recovery established; Firefox/Safari/mobile-browser/AT/native-platform validation remain OPEN**

Owner: Layout, Spatial & Interaction Specialist  
Parent studies:
- `research/layout/L006-layer-ownership-cross-contract.md`
- `research/layout/L006-native-layer-primitives-transfer.md`

Reproducible artifacts:
- `research/layout/L006-pointer-capture-touch-lost-invoker-specimen.html`
- `research/layout/L006-pointer-capture-touch-lost-invoker-playwright.py`
- `research/layout/L006-pointer-capture-touch-lost-invoker-results.json`

## Question

L006 already established that visual ownership, hit-test ownership, keyboard ownership, semantic ownership, data ownership, and layer-stack position are separate contracts.

This extension asks four higher-fidelity questions:

1. What happens if a background gesture already owns **pointer capture** when a modal layer appears?
2. Does the foreground continue to own an overlapping coordinate under a real touch input source?
3. When a modal contains a nested popover, does dismissal occur topmost-first and restore focus coherently?
4. What happens when the element that invoked a dialog no longer exists when the dialog closes?

The goal is not to declare Chromium behavior universal. It is to expose failure classes that product overlay/gesture systems must explicitly validate.

---

## RELATED DOMAIN CHECK

### Typography / Type
- Evidence checked: `progress/TYPE_STATUS.md` through T006.
- Reusable finding: runtime output can differ from source/editor assumptions; L006 likewise treats visible overlay geometry as insufficient evidence of operational ownership.
- Replication / challenge / transfer opportunity: later use localized/long labels because text growth can move overlay bounds, drag regions, and fallback focus targets.
- Dependency or overlap: no Type construction/rendering claim is made here.

### Color
- Evidence checked: `progress/COLOR_STATUS.md` through C009, plus C001/C007/C009 handoffs.
- Reusable finding: visual appearance and operational semantics remain separate; Color cannot rescue incorrect hit/focus/gesture ownership.
- Replication / challenge / transfer opportunity: later repeat under forced-colors/high-contrast and reduced visual effects.
- Dependency or overlap: Color is held functionally constant; this study is about behavioral ownership.

### Layout / Interaction
- Evidence checked: L001, L006, I001, I002, I003.
- Reusable finding: layer ownership is a cross-contract; focus restoration is part of continuity; disappearance of a recovery target needs an explicit fallback.
- Replication / challenge / transfer opportunity: add active gesture/capture ownership and dismissal-stack behavior to the L006 model.
- Dependency or overlap: direct extension of L006 with Interaction coupling.

### Web Design
- Evidence checked: `progress/WEB_STATUS.md`; no substantive W### evidence exists.
- Reusable finding: production browser/framework overlay behavior remains Web-owned.
- Implementation/application validation opportunity: reproduce in production portals/overlay managers with Firefox/Safari/mobile browsers, pointer/touch input, real routing, and AT.
- Dependency or overlap: controlled Chromium evidence only; not Web PASS.

### Other / cross-cutting
- W3C Pointer Events Level 3 Recommendation (30 Jun 2026): https://www.w3.org/TR/pointerevents3/
- HTML Living Standard modal/inert behavior: https://html.spec.whatwg.org/multipage/interaction.html
- WAI-ARIA APG Modal Dialog Pattern: https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/

Relevant source constraints:
- pointer capture retargets subsequent pointer events to the capturing element until capture is released;
- implicit release is specified after `pointerup`/`pointercancel` and for other bounded cases, not simply because another layer becomes modal;
- `showModal()` makes outside document content inert;
- APG says that when an invoking element no longer exists, focus should move to another element that supports the logical workflow.

### Overlap decision
- **EXTENSION + FAILURE REPRODUCTION + NATIVE INPUT TRANSFER**.
- Why: L006 already established layer contracts. This block tests transition-time hazards that appear only when input/focus state already exists before or during layer changes.

---

# SOURCE / SYNTHESIS BOUNDARY

## SOURCE

Pointer Events Level 3 specifies that, while pointer capture is active, subsequent events for that pointer are targeted at the capturing element until capture is released. It also defines explicit and implicit release rules.

HTML defines modal-dialog blocking/inertness for nodes outside a topmost modal dialog.

APG defines a workflow fallback for dialog closure when the invoking element no longer exists.

## SYNTHESIS

A modal transition changes current interaction availability, but it does not automatically prove that every **already-active gesture stream** has been canceled.

## STUDIO JUDGMENT

Extend the L006 ownership vector to include:

`visual owner / pointer hit owner / active gesture-capture owner / keyboard-focus owner / semantic-AT owner / action-data owner / layer-stack position`

The new term matters because `pointer hit owner` and `active gesture-capture owner` can differ after a modal appears.

---

# CONTROLLED ENVIRONMENT

- Chromium `144.0.7559.96` on Linux;
- Playwright Python;
- desktop mouse pointer for explicit capture test;
- Playwright touch source (`has_touch=True`) for overlap hit/activation test;
- native `<dialog>.showModal()` and HTML `popover`;
- Firefox/Safari executables were not available in the current container and no result is inferred for them.

Final bounded automated matrix: **13 / 13 assertions PASS**.

---

# FAILURE → REVISION A — pointer capture survives modal transition

## Broken sequence

1. Background drag target receives `pointerdown`.
2. It calls `setPointerCapture(pointerId)`.
3. `gotpointercapture` is observed.
4. A modal dialog is opened while the mouse button remains down.
5. Pointer is moved over the visible modal action.
6. Pointer is released.

Observed after modal open:

- background drag target continues receiving `pointermove`;
- background target receives `pointerup` with capture still active;
- controlled underlying drag commit increments to `1`;
- `lostpointercapture` occurs only after the captured stream ends.

Therefore, in this Chromium run:

> **modal inertness did not cancel an already-captured pointer stream.**

This is stronger than the earlier L006 screenshot/hit-test failure. Even if new hit tests belong to the modal, an older captured stream can continue to deliver events to the background owner.

## Revised sequence

Before opening the modal:

1. product checks whether the background drag target owns capture;
2. explicitly releases capture;
3. marks/cancels the in-progress background gesture;
4. only then opens the modal.

Observed:

- `lostpointercapture` fires before modal interaction proceeds;
- no further background `pointermove`/`pointerup` is used to commit the drag;
- controlled background drag commit remains `0`.

### Project rule

When a modal or blocking task transition occurs during an active drag/resize/press-hold interaction, define a **gesture cancellation policy**. Do not assume `inert`, backdrop, or top-layer entry cancels an earlier captured pointer.

The policy may be:
- finish the current gesture before modal transition;
- explicitly cancel and release capture;
- delay the modal transition until the gesture resolves;
- or, where domain-safe, let the gesture finish and make that continuity explicit.

The correct choice is task-specific. Silent background mutation beneath a newly modal task is not acceptable by default.

---

# TOUCH TRANSFER — overlap ownership

A non-modal popover action was positioned at the exact screen coordinate of an underlying page action.

Using a real Playwright touch source:

- `elementFromPoint()` at the touched coordinate resolved to the popover action;
- touch activation incremented foreground count to `1`;
- underlying action remained `0`.

### Interpretation

The basic L006 overlap-ownership rule transferred from mouse hit-testing to this bounded Chromium touch input case.

### Limit

This is not physical mobile-browser proof and does not test scroll/pan competition, multi-touch, long press, stylus, implicit touch capture, or OS gesture arbitration.

---

# NESTED OVERLAY DISMISSAL STACK

Controlled stack:

`page → modal dialog → nested auto popover`

Observed:

1. both dialog and nested popover open;
2. first `Escape` closes the topmost popover while keeping dialog open;
3. second `Escape` closes the dialog;
4. focus returns to the original dialog-invoking button when that invoker remains present.

### Project rule

Dismissal is a **stack operation**, not a global “close overlay” action.

For every overlay stack define:
- current topmost layer;
- what one Escape/back/dismiss gesture closes;
- which lower layer remains active;
- where focus returns after each level closes;
- whether the state/data owned by the closed layer is preserved, committed, or discarded.

---

# LOST INVOKER — focus restoration failure and revision

## Broken case

The dialog is opened by a button. While dialog is open, the invoking button is removed from the DOM. Then the dialog closes.

Observed after a short settling delay:

- focus falls to `BODY`;
- it does **not** automatically move to the adjacent logical workflow control.

This is not treated as a browser defect. The invoker no longer exists, so the application must define the logical continuation.

## Revised case

A close-time fallback policy checks whether the original invoker still exists. If not, it moves focus to a declared logical workflow target.

Observed:

- focus lands on `Logical fallback focus`.

### Project rule

Every dismissible/transient layer that can delete, hide, replace, filter away, or navigate away from its invoker needs a **lost-invoker focus policy**.

Typical fallback candidates:
- newly created/updated item;
- nearest surviving item in the same collection;
- parent heading/region;
- stable toolbar action;
- next workflow step.

Do not hard-code “return to opener” as the only focus restoration rule.

---

# UPDATED L006 OWNERSHIP MODEL

For layered UI, document:

1. **Visual owner** — which surface appears foreground.
2. **Pointer hit owner** — which element receives a new hit at the overlap coordinate.
3. **Active gesture/capture owner** — which element owns an already-started pointer stream.
4. **Keyboard-focus owner** — where Tab/Shift+Tab and programmatic focus may go.
5. **Semantic/AT owner** — what is exposed as active/modal/available.
6. **Action/data owner** — which object receives mutations.
7. **Layer-stack position** — which overlay dismisses first and what remains beneath.
8. **Restoration target** — where focus/state returns when the layer closes, including when the invoker is gone.

A production overlay is not approved until the required subset of these contracts agrees with modality and task semantics.

---

# REUSABLE FAILURE MODES

1. **Captured-background commit** — modal appears but prior drag capture continues and commits under it.
2. **Touch-through** — touch coordinate visually belongs to foreground but underlying action activates.
3. **Stack flattening** — Escape closes the wrong layer or several layers at once.
4. **Lost-invoker body fallthrough** — opener disappears and dismissal drops focus to document/body.
5. **Restoration to stale object** — focus returns to an element that exists but no longer represents the relevant workflow state.
6. **Gesture/data mismatch** — gesture owner and data mutation owner diverge during layer transition.

---

# VALIDATION CHECKLIST FOR REAL PROJECTS

For drag/overlay/modal combinations test at least:

- modal opens before gesture begins;
- modal opens during captured drag;
- gesture ends exactly as modal opens;
- pointer cancel path;
- mouse and touch input;
- forward/reverse keyboard traversal;
- topmost-first Escape/back dismissal;
- invoker remains;
- invoker is removed;
- invoker is hidden/disabled/replaced;
- nested overlays;
- state/data commit or rollback at each transition.

High-risk destructive/financial/operational actions should explicitly test whether a background gesture can commit after foreground modality begins.

---

# EVIDENCE LIMITS / OPEN

Still OPEN:

- Firefox and Safari behavior;
- physical iOS/Android browsers;
- touch drag/implicit capture, stylus, multi-touch and OS gestures;
- screen-reader/AT announcement and virtual-cursor behavior;
- browser chrome interactions;
- framework portal/overlay-manager behavior;
- pointer capture in native mobile/desktop frameworks;
- forced-colors/high-contrast/reduced-transparency transfer;
- human comprehension of nested layer ownership;
- production localization/content stress.

No cross-browser or physical-device PASS is claimed.

---

# HANDOFFS TO OTHER SPECIALISTS

## Typography / Type
- Useful finding/context: localized text can cause an overlay/invoker to move, wrap, be replaced, or disappear; restoration policies should survive those geometry changes.
- Confirmation / transfer note: use T005/T006 production output when overlay geometry becomes project-specific.
- Scope limit: no Type-quality conclusion.

## Color
- Useful finding/context: modal/inert visual treatment does not cancel prior pointer capture; appearance cannot repair active-gesture ownership.
- Confirmation / transfer note: reinforces C001/I003 separation between authored appearance and actual operational state.
- Scope limit: no Color threshold or salience claim.

## Layout / Interaction
- Useful finding/context: add `active gesture/capture owner` and `restoration target` to the L006 ownership vector.
- Confirmation / transfer note: extends I001 focus restoration and L006 layer stack with transition-time input state.
- Scope limit: Chromium-only implementation proof.

## Web Design
- Useful finding/context: production overlay managers must explicitly test modal entry during active pointer capture, topmost-first dismissal, touch overlap, and lost invokers.
- Validation consequence: native `dialog`/popover support does not eliminate application-level gesture cancellation/restoration policy.
- Scope limit: Firefox/Safari/mobile/AT/framework transfer remains open.

---

# Project-readiness conclusion

For real projects, the question is no longer only:

> “Which layer owns this pixel now?”

Also ask:

> “Which object already owns the active input stream, and what must happen to that stream when modality changes?”

That distinction prevents a class of hidden background mutations that visual, hit-test, and inertness QA alone can miss.
