# L006 Extension — Custom `aria-modal` Declaration Versus Actual Modality

Status: **PRACTICE + CRITIQUE / CONTROLLED CHROMIUM PORTAL TRANSFER — semantic-modal declaration vs inertness/hit/focus implementation mismatch reproduced and revised; actual screen-reader/framework/cross-browser evidence remains OPEN**

Owner: Layout, Spatial & Interaction Specialist  
Parent studies:
- `research/layout/L006-layer-ownership-cross-contract.md`
- `research/layout/L006-native-layer-primitives-transfer.md`
- `research/layout/L006-forced-colors-touch-ax-transfer.md`

Reproducible artifacts:
- `research/layout/L006-custom-aria-modal-inertness-specimen.html`
- `research/layout/L006-custom-aria-modal-inertness-playwright.py`
- `research/layout/L006-custom-aria-modal-inertness-results-summary.json`

## Question

Native `<dialog>.showModal()` establishes browser-level top-layer/inertness behavior. Many real web products instead render a custom portal with:

```html
<div role="dialog" aria-modal="true">…</div>
```

This experiment asks:

> What happens when a custom portal **declares** itself modal to accessibility semantics but does not implement actual background inertness, hit blocking, or keyboard containment?

The comparison holds the same visual portal/dialog structure and ARIA dialog declaration while changing only the operational modality contract.

---

## RELATED DOMAIN CHECK

### Typography / Type
- Evidence checked: `progress/TYPE_STATUS.md` through T007.
- Reusable finding: runtime validity cannot be inferred from source/build labels alone; T007 showed a file can build while a critical variation behavior is wrong.
- Transfer opportunity: the analogous L006 question is whether a component can carry a correct semantic label while runtime interaction remains wrong.
- Dependency or overlap: Type is not varied here.

### Color
- Evidence checked: `progress/COLOR_STATUS.md` through C009 plus C001/I003/L006 forced-colors transfer.
- Reusable finding: visual treatment cannot substitute for behavioral semantics; the same nominal semantic role may render differently under runtime conditions.
- Transfer opportunity: keep backdrop/visual dialog constant while testing actual modality.
- Dependency or overlap: Color is not used to repair the broken condition.

### Layout / Interaction
- Evidence checked: L006 custom/native/forced-colors extensions and I001 focus/restoration.
- Reusable finding: visual, pointer, focus, semantic/AT, data and restoration ownership are separate contracts.
- Transfer opportunity: directly test a semantic-modal declaration whose pointer/focus/background contracts are absent.
- Dependency or overlap: direct L006 extension.

### Web Design
- Evidence checked: `progress/WEB_STATUS.md`; no substantive W### evidence exists.
- Reusable finding: complete framework portal/focus-scope implementation validation remains Web-owned.
- Application opportunity: reproduce this matrix in production React/Flutter-Web/Vue/etc. portal/overlay managers and target AT/browser combinations.
- Dependency or overlap: controlled Chromium specimen only, not Web PASS.

### Other / cross-cutting
- WAI-ARIA APG Dialog (Modal) Pattern: https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/
- APG Modal Dialog Example: https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/examples/dialog/

APG requires the modal pattern to behave modally: background content is inert, Tab/Shift+Tab remain in the dialog, and focus is restored appropriately. APG explicitly warns that setting `aria-modal="true"` when application code does not actually prevent outside interaction can severely harm some assistive-technology users.

### Overlap decision
- **REALISTIC PORTAL TRANSFER + SEMANTIC/BEHAVIOR CONTRADICTION TEST**.
- Why: L006 already proved native and custom ownership contracts. This block isolates a frequent implementation failure: correct ARIA label/state without corresponding actual modality.

---

# SOURCE / SYNTHESIS BOUNDARY

## SOURCE

The APG modal dialog pattern states that:

- windows under an active modal dialog are inert;
- `Tab` and `Shift+Tab` do not move focus outside the dialog;
- the dialog container uses `role="dialog"` and `aria-modal="true"`;
- `aria-modal="true"` should only be used when application code prevents interaction outside the dialog and the UI visually obscures the underlying content.

## SYNTHESIS

`aria-modal="true"` is part of the semantic contract. It is not an implementation primitive that automatically creates pointer blocking, DOM inertness, or focus containment.

## STUDIO JUDGMENT

For custom portals, treat these as independent acceptance criteria:

`semantic modal declaration / underlay inertness / pointer blocking / focus containment / initial focus / dismissal / restoration`

A component is not approved merely because one criterion is present.

---

# CONTROLLED SPECIMEN

Both conditions use the same custom portal structure:

- visual backdrop;
- custom `div role="dialog"`;
- `aria-modal="true"`;
- `aria-labelledby` dialog title;
- Confirm / Cancel actions;
- initial focus on Confirm.

The page behind contains:

- a text input;
- the dialog opener;
- a destructive background action.

## Broken

The custom dialog has modal ARIA semantics but:

- the application subtree is not `inert`;
- backdrop uses `pointer-events:none`;
- no Tab/Shift+Tab containment is implemented.

## Revised

The ARIA declaration is unchanged, but:

- application underlay becomes `inert`;
- backdrop consumes outside pointer hits;
- forward and reverse Tab wrap between dialog controls;
- close restores focus to the opener.

---

# CONTROLLED RESULT

Chromium `144.0.7559.96`.

Final matrix: **14 / 14 assertions PASS**.

---

# FAILURE — DECLARED MODAL, OPERATIONALLY NON-MODAL

## 1. Chromium accessibility tree exposes the dialog as modal

Broken condition AX dialog node:

- role: `dialog`;
- name: `Confirm deletion`;
- property: `modal = true`.

So the ARIA declaration is not ignored.

## 2. But background remains exposed and focusable in the same AX tree

The broken tree also contains:

- `button — Background destructive action`, `focusable=true`;
- page textbox;
- dialog content.

This differs from the earlier native `showModal()` L006 test, where the page background disappeared from Chromium's exposed AX tree while the modal was active.

### Interpretation

In this Chromium implementation, `aria-modal="true"` on a custom `div` did **not** itself prune the underlay from the exposed AX tree.

This must not be generalized to screen-reader behavior across browsers. The important result is narrower:

> the semantic node says `modal=true`, while the background is still exposed/focusable and the DOM is not actually inert.

## 3. Keyboard actually escapes

Starting on `Confirm`:

Broken reverse sequence:

`Confirm → Background destructive action → Open custom dialog`

Starting on `Cancel` and pressing `Tab` leaves the dialog task and lands on `BODY` in this bounded run.

So the ARIA modal declaration did not create focus containment.

## 4. Pointer actually reaches obscured background

At a point visually under the backdrop but outside the dialog:

- `elementFromPoint()` resolves to `Background destructive action`;
- one click increments background destructive count to `1`.

The backdrop looks modal but owns no pointer input there.

### Failure classification

This is a **semantic/behavioral contradiction**:

- dialog semantics: modal;
- actual DOM background: not inert;
- keyboard: escapes;
- pointer: reaches background;
- destructive background action: activates.

---

# REVISION — ALIGN THE MODAL CONTRACT

The revised condition retains the same role/name/`aria-modal` declaration and visual dialog, while adding real modality behavior.

## Underlay inertness

`app.inert = true`

Observed:

- background destructive action and textbox disappear from the exposed Chromium AX tree;
- dialog remains exposed with `modal=true`.

## Keyboard containment

Reverse:

`Confirm → Cancel → Confirm`

Forward from `Cancel`:

`Cancel → Confirm`

## Pointer ownership

At the same outside-dialog coordinate:

- hit testing resolves to the backdrop rather than the hidden background button;
- background destructive count remains `0`.

## Restoration

After close:

- underlay inertness is removed;
- focus returns to `Open custom dialog`.

### Consequence

The revised portal aligns semantic, pointer, focus and restoration contracts instead of relying on ARIA to manufacture modality.

---

# PROJECT RULES

1. **ARIA describes the modal contract; it does not implement it.**
2. A custom `aria-modal="true"` dialog must still implement actual outside-interaction blocking.
3. Test both `Tab` and `Shift+Tab`; one direction is not enough.
4. Test pointer activation on visually obscured destructive background controls.
5. Inspect the browser accessibility representation, but do not call that screen-reader PASS.
6. Compare semantic state against actual interaction state; contradiction is worse than either channel being absent because different users can receive different truths.
7. Prefer native modal primitives when they fit the product because they establish more of the platform contract, while still validating focus/AT behavior on target browsers.
8. For framework portals, document which layer owns inertness, focus scope, pointer blocking, Escape, restoration and nested stack order.

---

# EVIDENCE LIMITS / OPEN

This does not establish:

- NVDA/JAWS/Narrator/VoiceOver/TalkBack behavior;
- Firefox/Safari AX mappings;
- actual React/Vue/Angular/framework portal behavior;
- native mobile accessibility;
- complex nested custom portals;
- routing/remount/lost-invoker cases beyond earlier L006 controls;
- physical touch and OS gesture interaction;
- human comprehension of modal layering.

No PASS promotion is justified.

---

# HANDOFFS TO OTHER SPECIALISTS

## Typography / Type
- Useful finding: a correct label/build state is not enough when runtime behavior differs; conceptually parallels T007's “build succeeded but critical behavior failed” evidence.
- Scope limit: no Type decision here.

## Color
- Useful finding: visual dimming/backdrop cannot establish actual modality; complements Color→Interaction separation from C001/C006/C007.
- Scope limit: no color threshold or palette recommendation.

## Layout / Interaction
- Useful finding: add `semantic declaration ↔ actual operational contract` consistency to L006 overlay review.
- Confirmation: extends visual/pointer/focus/AT ownership model with a direct ARIA-modal contradiction proof.
- Scope limit: actual AT remains OPEN.

## Web Design
- Useful finding: future W### framework overlay validation should deliberately test a portal that has correct ARIA but missing inert/focus/pointer implementation.
- Validation consequence: include this **14-assertion custom-modal matrix** alongside prior L006 matrices.
- Scope limit: no production framework tested here.

---

# Project-readiness conclusion

For a custom web modal, do not approve this state:

> “It has `role=dialog`, `aria-modal=true`, and looks dimmed.”

Approve only when the **declared semantic modality and the actual pointer/focus/background/restoration behavior describe the same interaction reality**.
