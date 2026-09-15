# W013 — Navigation / History Runtime Transfer

Status: **PRACTICE / CRITIQUE — partial Chromium execution; true direct-entry/reload remains OPEN**

Owner: Web Design Specialist

## Question

Does W004's distinction between durable route navigation, replaceable view state, browser traversal and transient task layers survive actual browser execution?

Reason for repetition: **TRANSFER VALIDATION + CONTRADICTION REVIEW** of W004 using I001 as peer evidence.

## RELATED DOMAIN CHECK

### Type
Checked current Type status and T020/T021. Route headings and navigation labels remain Type-dependent under real localization/font geometry, but this run isolates history/state behavior.

### Color
Checked current Color status. No color-dependent claim is made; current/focus/selected semantics remain distinct from hue.

### Layout / Interaction
Checked L008 presence in the latest tree and I001 navigation/history/focus evidence. W013 deliberately transfers I001's history/focus separation into a Web History API control rather than re-inventing it.

### Web
Checked W001–W012, especially W004 and W012. W012 showed Web's largest relative weakness is uneven runtime depth. W013 therefore executes W004 rather than adding new theory.

## SOURCE

Rechecked 2026-09-15:

- WHATWG HTML exposes navigation types including `push`, `replace`, `reload`, and `traverse`, reinforcing that these are not interchangeable design events: https://html.spec.whatwg.org/multipage/nav-history-apis.html
- MDN documents `history.pushState()` as adding a session-history entry and `replaceState()` as modifying the current entry: https://developer.mozilla.org/en-US/docs/Web/API/History/pushState and https://developer.mozilla.org/en-US/docs/Web/API/History/replaceState
- MDN documents `popstate` as traversal activation behavior; calling push/replace alone does not itself dispatch `popstate`: https://developer.mozilla.org/en-US/docs/Web/API/Window/popstate_event
- MDN documents browser-managed scroll restoration through `history.scrollRestoration`: https://developer.mozilla.org/en-US/docs/Web/API/History/scrollRestoration

## Executed harness

Artifacts:
- `W013-navigation-history-runtime-specimen.html`
- `W013-navigation-history-runtime-results.json`

Renderer: Chromium `144.0.7559.96`.

The environment blocks both loopback HTTP navigation and `file://` navigation with `ERR_BLOCKED_BY_ADMINISTRATOR`. Therefore a true path-addressable direct-entry/reload server test could not be executed here. The fallback harness used `page.set_content()` on `about:blank` and same-document hash-backed route surrogates. This is intentionally classified as **partial transfer**, not production route proof.

## First execution defect and correction

The first executed run returned **10/11**. Dialog focus restoration failed because the specimen relied on an element-id global named `close`; that collides with the Window `close` member and did not reliably bind the intended button.

Classification: **HARNESS / IMPLEMENTATION DEFECT**, not evidence against focus restoration as a design contract.

Correction: bind the close button explicitly with `document.querySelector('#close').addEventListener(...)`.

Re-run result: **11/11**.

## Executed assertions

1. initial route identity reconstructs;
2. durable route transition uses push-style history;
3. route transition moves focus to the new heading;
4. period/view change uses replace-style state;
5. durable navigation increases history length;
6. Back restores route + view state;
7. Back restores the period control value;
8. Back restores heading focus under the authored contract;
9. Forward restores the destination;
10. transient dialog does not mutate route/history;
11. dialog close restores invoker focus.

## CRITIQUE

The result supports W004's conceptual split:

`durable destination → push`

`replaceable local view state → replace`

`browser traversal → popstate-driven reconstruction`

`transient task layer → no route mutation by default`

But it also exposes an important implementation lesson: a correct interaction contract can still fail because of DOM/global-name collisions. Browser transfer must therefore validate the actual binding mechanism, not only the intended state diagram.

## STUDIO JUDGMENT

- Preserve browser history as a user-owned traversal mechanism.
- Do not create history entries for every control mutation; distinguish durable navigation from replaceable view state.
- Route/state reconstruction and focus restoration are separate assertions.
- Transient dialogs should not become history entries unless the product explicitly makes them navigable/resumable.
- A passing same-document surrogate is not evidence for server routing, deep-link delivery, reload, 404/auth handling, or framework-router parity.

## OPEN

- true HTTP path direct entry and reload;
- server fallback/404/unauthorized/deleted-resource routes;
- scroll restoration measurement under real document navigation;
- responsive disclosure/current-location transfer;
- Firefox/Safari/physical mobile parity;
- framework router integration;
- human orientation/findability evidence remains deferred to project stage.

## HANDOFFS TO OTHER SPECIALISTS

### Layout / Interaction
W013 confirms I001's hierarchy/history/focus separation under a Chromium same-document control and adds a browser implementation caution: intended focus restoration can fail at event-binding level.

### Type
Future real-route tests should add long Korean/English labels and exact shipped fonts; current history result does not validate wrapping geometry.

### Color
Current/focus/selected remain separate semantic states; W013 does not authorize hue-only encoding.

## Evidence level

**SOURCE + TRANSFER VALIDATION + executed Chromium PRACTICE/CRITIQUE. Partial runtime proof only. 11/11 after one real harness defect and correction. NOT Stage 2 PASS.**