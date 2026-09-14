# L006 Validation — Native HTML Popover / Dialog Transfer

Status: **PRACTICE + CRITIQUE / NATIVE-BROWSER TRANSFER — Chromium top-layer/inertness/nested-overlay/focus-restoration evidence established; strict APG focus-loop, AT and cross-browser/device validation remain OPEN**

Owner: Layout, Spatial & Interaction Specialist  
Parent study: `research/layout/L006-layer-ownership-cross-contract.md`

Artifacts:

- `research/layout/L006-native-layer-primitives-specimen.html`
- `research/layout/L006-native-layer-primitives-playwright.py`
- `research/layout/L006-native-layer-primitives-results.json`

## Objective

Transfer the L006 ownership vector from a custom controlled overlay into actual browser primitives:

- HTML `popover`;
- `<dialog>.showModal()`;
- nested popover inside a modal dialog.

The question is not whether native primitives are universally preferable. The question is which parts of the ownership contract the browser establishes automatically and which still require product-level validation.

## Sources

- HTML Living Standard, popover: https://html.spec.whatwg.org/multipage/popover.html
- HTML Living Standard, inert/modal interaction: https://html.spec.whatwg.org/multipage/interaction.html
- HTML Living Standard, dialog: https://html.spec.whatwg.org/multipage/interactive-elements.html
- WAI-ARIA APG Modal Dialog Pattern: https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/

Relevant distinction:

- HTML `showModal()` places the dialog in the top layer and blocks the rest of the document by making outside nodes inert.
- APG recommends the stronger user-facing keyboard pattern in which Tab/Shift+Tab cycle within the dialog.
- These are related but not identical claims.

## Controlled Chromium result

Chromium `144.0.7559.96`.

Final automated matrix: **13 / 13 assertions PASS** for the bounded claims below.

### Native popover

Confirmed:

- `:popover-open` becomes true;
- the popover owns hit testing at a coordinate shared with an underlying background action;
- the foreground action fires while the background action does not;
- the rest of the page is not made inert merely because a non-modal popover is open.

This supports the L006 distinction:

> non-modal foreground ownership is local to its presented region; it does not imply global background inertness.

### Native modal dialog

Confirmed:

- `showModal()` opens a modal dialog and `:modal` matches;
- background pointer activation is blocked;
- keyboard traversal did not reach background page controls;
- a popover opened from inside the modal can itself occupy the topmost interactive layer;
- nested popover hit testing resolves to the nested action;
- closing the dialog restores focus to the invoking `Open dialog` button in this controlled case.

### Important focus nuance

The focus sequence contained transient states where `document.activeElement` was `<body>`.

Therefore:

- **background interactive controls were not reached**;
- but **strictly “activeElement always remains a descendant of the dialog” was false** in this Chromium/headless run.

This is consistent with the distinction between:
- HTML modal inertness/top-layer behavior;
- the APG recommended cyclic focus-containment interaction pattern.

Do not write:

> “Native `<dialog>` automatically proves the APG focus loop.”

Instead write:

> “`showModal()` establishes top-layer modality and document inertness; target-browser keyboard behavior still deserves explicit validation, and a product may choose an additional focus-scope policy when its UX/accessibility requirements demand the APG cycle.”

This is especially important because an assertion that only checks “background controls cannot receive focus” is weaker than an assertion that checks “focus always stays on an intended dialog descendant.”

## Nested overlay consequence

The nested popover inside the modal was:

- open in the popover showing state;
- topmost at its action coordinate;
- independently actionable;
- dismissed before the parent dialog was closed.

This establishes a useful future test requirement:

> Ownership must be modeled as a stack, not as one global foreground/background boolean.

Future production overlay managers should validate:
- which layer is currently topmost;
- which lower layer remains active but occluded;
- where focus should return when the topmost layer closes;
- whether dismissal order matches task semantics.

## Failure model refined from L006

L006 custom overlay proof showed:

`same pixels → opposite pointer/focus ownership`

Native transfer adds:

`native top layer / inertness ≠ complete product-level focus policy`

Therefore layer QA needs at least:

1. visual ownership;
2. hit-test ownership;
3. inertness/modal scope;
4. focus navigation behavior;
5. nested layer stack;
6. dismissal/focus restoration;
7. semantic/AT exposure.

## OPEN

- Firefox/Safari/mobile engines;
- screen readers and accessibility-tree inspection;
- browser chrome focus behavior outside headless testing;
- nested modal dialogs;
- popover light-dismiss/escape policies;
- lost invoker/unmounted trigger;
- scroll locking and visual viewport;
- touch/gesture/pointer capture;
- framework portal ownership;
- forced colors / reduced motion / reduced transparency;
- long/localized content and responsive sheet morphing.

## HANDOFFS

### Web Design
Reproduce this matrix with actual project components/frameworks. Native primitives reduce some ownership risk but do not eliminate the need for keyboard, restoration, nested overlay and AT validation.

### Color
Top-layer/inertness semantics must not depend on shadow/dimming surviving. C001/I003 forced-color resilience remains relevant.

### Type
Long/localized labels can change overlay size/placement and therefore overlap/hit regions. Later transfer should use T005-style strings.

### Layout / Interaction
Update the ownership vector to include **layer-stack position** and distinguish:
- inertness,
- strict focus-descendant containment,
- no-background-control reachability.

These are related but not interchangeable.
