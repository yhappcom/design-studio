# L006 Extension — Forced-Colors Layer Cues, Touch Implicit Capture, and Accessibility-Tree Ownership

Status: **PRACTICE + CRITIQUE / CONTROLLED CHROMIUM TRANSFER — forced-colors cue failure→revision, touch implicit-capture modal transition, and Chromium accessibility-tree ownership established; real OS high-contrast, screen-reader, Firefox/Safari, physical mobile and production-framework validation remain OPEN**

Owner: Layout, Spatial & Interaction Specialist  
Parent studies:
- `research/layout/L006-layer-ownership-cross-contract.md`
- `research/layout/L006-native-layer-primitives-transfer.md`
- `research/layout/L006-pointer-capture-touch-lost-invoker-transfer.md`

Reproducible artifacts:
- `research/layout/L006-forced-colors-touch-ax-specimen.html`
- `research/layout/L006-forced-colors-touch-ax-playwright.py`
- `research/layout/L006-forced-colors-touch-ax-results-summary.json`

## Question

L006 already established that one visually foreground surface can disagree with pointer, focus, data, gesture-capture and restoration ownership.

This extension asks three unresolved questions:

1. If forced-colors removes an authored elevation cue such as `box-shadow`, can interaction ownership remain correct while **visual layer ownership becomes structurally under-signaled**?
2. Does the explicit mouse pointer-capture failure reproduced earlier transfer to **touch implicit pointer capture**?
3. Does native modal/non-modal ownership transfer into Chromium's **accessibility tree**, even though actual screen-reader behavior remains untested?

The study deliberately separates those evidence layers. It does not treat a screenshot, pointer result, or AX tree as interchangeable proof.

---

## RELATED DOMAIN CHECK

### Typography / Type
- Evidence checked: `progress/TYPE_STATUS.md` through T007.
- Reusable finding: T007 demonstrates that technically valid source/build states can still produce malformed intermediate runtime output; exact delivered runtime state matters.
- Replication / challenge / transfer opportunity: future production overlay QA should pin the actual delivered font build/axis instance because text growth can move layer boundaries and fallback targets.
- Dependency or overlap: typography is held constant here; no Type conclusion is claimed.

### Color
- Evidence checked: `progress/COLOR_STATUS.md` through C009, especially C001 forced-color resilience and C007/C009 transfer boundaries.
- Reusable finding: authored color/elevation channels can be replaced while semantic/interaction contracts remain; Color should reinforce rather than define interaction meaning.
- Replication / challenge / transfer opportunity: independently transfer C001's channel-loss hypothesis into realistic L006 foreground/background layers.
- Dependency or overlap: Color owns the palette/contrast/system-color conclusions. Layout/Interaction owns whether the layer remains spatially/behaviorally coherent.

### Layout / Interaction
- Evidence checked: L001, L006, I001 and I003.
- Reusable finding: border/layer ownership is contextual; visual/pointer/focus/semantic/data/gesture ownership must be separated; I003 already proved color-channel loss can preserve or destroy state semantics depending on structural redundancy.
- Replication / challenge / transfer opportunity: add forced-colors layer-boundary evidence, touch implicit capture, and browser AX-tree evidence.
- Dependency or overlap: direct L006 extension.

### Web Design
- Evidence checked: `progress/WEB_STATUS.md`; `W001` remains next and no substantive W### evidence exists.
- Reusable finding: complete browser/page/framework integration remains Web-owned.
- Implementation/application validation opportunity: reproduce with real production overlays, framework portals, OS high contrast, screen readers, Safari/Firefox/mobile and delivered fonts.
- Dependency or overlap: this is controlled Chromium evidence, not Web PASS.

### Other / cross-cutting
- W3C CSS Color Adjustment Module Level 1, forced color palettes and `forced-color-adjust`: https://www.w3.org/TR/css-color-adjust-1/
- W3C Pointer Events Level 3 Recommendation, implicit pointer capture and release: https://www.w3.org/TR/pointerevents3/
- HTML Living Standard, modal dialogs and inert subtrees: https://html.spec.whatwg.org/multipage/interaction.html

### Overlap decision
- **CROSS-DOMAIN TRANSFER VALIDATION + FAILURE REPRODUCTION + ACCESSIBILITY-TREE IMPLEMENTATION CHECK**.
- Why: each test closes a named L006 gap without inventing human or production evidence.

---

# SOURCE / SYNTHESIS BOUNDARY

## SOURCE — forced colors

CSS Color Adjustment Level 1 defines forced-colors as a user-preference mode that replaces author-chosen colors for affected properties. It specifically states that `box-shadow` and `text-shadow` compute to `none` when `forced-color-adjust:auto` applies. It also defines `forced-color-adjust:none` as an opt-out and cautions authors to use it only when they are themselves supporting the user's color/contrast needs.

## SOURCE — touch implicit capture

Pointer Events Level 3 states that direct-manipulation inputs such as touch or stylus SHOULD behave as though `setPointerCapture()` occurred immediately before `pointerdown` listeners run. Unless released, subsequent pointer events remain captured until the defined release conditions, including after `pointerup`/`pointercancel`.

## SOURCE — modal inertness / accessibility exposure

The HTML Living Standard defines nodes outside the topmost modal dialog as inert, and notes that inert nodes generally cannot be focused and are not exposed to accessibility APIs/assistive technologies.

## SYNTHESIS

Three separate ownership problems follow:

- a layer can keep correct **behavioral ownership** while its authored visual elevation channel disappears;
- a modal can establish new hit/focus availability while an already-active **touch capture stream** still belongs to the background;
- modal/non-modal differences should be visible not only in pointer/focus behavior but also in the browser's semantic accessibility representation.

## STUDIO JUDGMENT

L006's ownership vector remains:

`visual owner / pointer hit owner / active gesture-capture owner / keyboard-focus owner / semantic-AT owner / action-data owner / layer-stack position / restoration target`

No one channel substitutes for the others.

---

# CONTROLLED ENVIRONMENT

- Chromium `144.0.7559.96` on Linux;
- Playwright Python;
- CSS forced-colors emulation via Playwright/Chromium;
- native manual popover for the forced-colors overlap test;
- Chrome DevTools Protocol `Input.dispatchTouchEvent` for one bounded touch stream;
- native `<dialog>.showModal()`;
- Chrome DevTools Protocol `Accessibility.getFullAXTree` for browser accessibility-tree inspection.

Final matrix: **28 / 28 assertions PASS** after one measurement-control revision.

Important limits:

- forced-colors emulation is not a physical Windows High Contrast session;
- the AX tree is browser semantic evidence, not a screen-reader usability/announcement result;
- synthetic CDP touch is not physical iOS/Android browser evidence.

---

# A. FORCED-COLORS — VISUAL CUE LOSS WITHOUT OWNERSHIP LOSS

## Controlled variants

All three variants use the same foreground popover dimensions, placement, content and overlap action.

### `broken`

Visual separation relies on:

- white foreground surface over a white workspace;
- strong `box-shadow`;
- no structural outline/boundary.

### `revised`

Same surface and shadow, plus:

`outline: 3px solid CanvasText`

The outline uses a system color so the structural boundary remains compatible with the user's forced palette.

### `optout`

Same shadow-only design plus:

`forced-color-adjust: none`

This is included only as a diagnostic control. It is **not** the recommended default fix.

## Failure reproduced

Normal mode, broken variant:

- authored shadow is present.

Forced-colors, broken variant:

- computed `box-shadow` becomes `none`;
- popover background and page background both resolve to the same Canvas value in the controlled light emulation;
- no outline exists;
- after isolating the measurement area, the entire 3px strip immediately above the popover boundary contains **0 non-background pixels**.

Yet:

- `elementFromPoint()` at the overlapping foreground action still returns the foreground button;
- activation remains `foreground=1 / background=0`.

### Consequence

**Interaction ownership can remain correct while the authored visual ownership cue collapses.**

This is the reciprocal of the earlier L006 failure where pixels looked correct but ownership was wrong.

L006 now contains both directions:

- **same-looking foreground, wrong behavioral owner**;
- **correct behavioral owner, weakened/removed authored foreground cue**.

## Revision

Under the same forced-colors emulation, the revised structural outline remains:

- width `3px`;
- style `solid`;
- system-color-resolved outline;
- every pixel in the isolated 3px top boundary strip differs from the page Canvas in this controlled run.

Foreground activation remains correct.

### Studio rule

For critical layer boundaries, prefer **structural cues that can resolve through system colors** rather than relying only on shadow/fill distinctions that forced-colors may remove or replace.

This does not mean every popover needs a permanent visible border in normal mode. It means the component needs an alternate robust boundary channel when the authored elevation channel is not available.

## Method challenge — `forced-color-adjust:none`

The opt-out control preserves the author shadow under Chromium forced-colors emulation.

That proves the opt-out mechanism works in this bounded test. It does **not** make it the preferred solution.

Reject the heuristic:

> "High contrast broke my shadow, so disable forced colors on the component."

Use `forced-color-adjust:none` only when the component itself supplies an appropriate user-compatible rendering and there is a concrete reason to override UA adjustment.

---

# B. TOUCH IMPLICIT POINTER CAPTURE — MODAL ENTRY DOES NOT CANCEL THE ACTIVE STREAM

## Baseline mechanism

The touch target uses `touch-action:none` so the bounded test can observe the scripted pointer stream without viewport pan/zoom arbitration.

A CDP touch sequence begins on the background drag target.

Observed immediately:

- `pointerType = touch`;
- `hasPointerCapture(pointerId) = true` during `pointerdown`;
- `gotpointercapture` follows on the next event.

This reproduces the Pointer Events Level 3 implicit-capture model.

## Broken modal transition

Sequence:

1. touch starts on background drag target;
2. implicit capture is confirmed;
3. modal dialog opens while the touch remains active;
4. the finger is moved to the visible modal region;
5. touch ends.

Observed:

- modal is open;
- background target still reports capture immediately after modal entry;
- subsequent `pointermove` remains targeted to the captured background;
- `pointerup` is delivered to the background with capture still active;
- controlled background drag commit becomes `1`;
- capture is then released.

### Consequence

The explicit mouse-capture result from the previous L006 extension **transfers to touch implicit capture in this Chromium test**.

Do not assume modal top-layer/inertness cancels a touch stream that already owns implicit capture.

## Revision

Before opening the modal:

- if the background target owns capture, call `releasePointerCapture(pointerId)`;
- cancel the domain gesture/data commit;
- then enter the modal state.

Observed:

- capture is no longer active immediately after the revised transition;
- the background does not receive a commit-producing `pointerup` path;
- controlled background commit remains `0`.

### Project rule

Modal/blocking transitions during touch drag/resize/press-hold need an explicit gesture policy:

- finish first;
- cancel/release first;
- defer modal entry;
- or intentionally allow completion when domain semantics make that safe.

The policy must be designed. It must not be an accidental by-product of layer visuals.

---

# C. CHROMIUM ACCESSIBILITY TREE — MODAL AND NON-MODAL SEMANTIC OWNERSHIP DIFFER

The study inspected Chromium's exposed accessibility tree, removing generic/static text nodes from the reporting view so the interactive/landmark structure is easier to compare.

## Baseline

Exposed tree includes:

- `button — Background action`;
- popover/dialog opener controls.

## Non-modal popover open

Exposed tree includes:

- background action remains exposed;
- `region — Quick tools`;
- `button — Popover action`.

### Interpretation

This matches the non-modal ownership contract:

> foreground owns its own presented region, but background remains semantically available.

## Modal dialog open

Exposed tree includes:

- `dialog — Confirm task`;
- dialog heading/actions.

The page-level `Background action` is **not present in the exposed tree** while the modal is active.

### Interpretation

This is Chromium accessibility-tree evidence consistent with HTML modal inertness.

It does not prove:

- exact screen-reader announcements;
- virtual-cursor behavior;
- rotor/landmark navigation behavior;
- Braille output;
- AT/browser interoperability.

Those remain OPEN.

## Nested popover inside modal

When a nested popover opens from inside the dialog:

- parent dialog remains exposed;
- `region — Nested tools` and its action become exposed;
- page background action remains absent.

This reinforces L006's ownership-stack model at the semantic-tree layer.

## Modal close

After the nested layer and dialog close:

- page background action becomes exposed again.

### Project rule

For layered components, browser accessibility-tree QA should compare at least:

- baseline;
- non-modal foreground open;
- modal foreground open;
- nested foreground open;
- dismissal/restoration.

Do not infer screen-reader quality from tree membership alone, but do not skip the semantic ownership layer either.

---

# MEASUREMENT FAILURE → REVISION

The first integrated forced-colors run produced **27/28 assertions**, because the top-boundary screenshot strip contained unrelated pixels from surrounding page content.

That failed the isolation contract, not the product behavior.

Revision:

- move the popover to a blank region of the viewport;
- constrain nearby workspace text away from the measurement strip;
- rerun the exact matrix.

Final result:

**28/28 assertions PASS.**

### Method consequence

A screenshot metric is invalid if the sampled region contains uncontrolled neighboring content. Measurement geometry deserves the same isolation discipline as the UI geometry being studied.

---

# UPDATED L006 PROJECT CHECKLIST

For a layered component, review:

1. **Visual owner** — does the foreground remain distinguishable when shadows/fills/colors are replaced?
2. **Pointer hit owner** — what would a new hit test target now?
3. **Active gesture-capture owner** — who owns a pointer stream that began before the layer transition?
4. **Keyboard-focus owner** — where do Tab and Shift+Tab move?
5. **Semantic/AT owner** — what remains exposed in the browser accessibility representation, and later in actual AT?
6. **Action/data owner** — which object receives mutations?
7. **Layer-stack position** — what is topmost and what does one dismiss action remove?
8. **Restoration target** — where does focus/state return, including lost-invoker cases?
9. **User-override resilience** — does forced/high-contrast mode remove the only spatial/elevation cue?

---

# EVIDENCE LIMITS / OPEN

Still not established:

- actual Windows High Contrast rather than Chromium emulation;
- Firefox forced-colors behavior;
- Safari/macOS/iOS accessibility behavior;
- NVDA, JAWS, Narrator, VoiceOver or TalkBack behavior;
- physical touch drag/scroll competition;
- implicit capture under Safari/iOS and Android browsers;
- stylus, multi-touch and OS gesture arbitration;
- framework portal/focus-scope/overlay manager behavior;
- production content/localization/variable-font axis states;
- human judgments of foreground/layer comprehension.

No PASS promotion is justified.

---

# HANDOFFS TO OTHER SPECIALISTS

## Typography / Type
- Useful finding/context: overlay boundaries and fallback/restoration targets must be retested with actual delivered font builds/axis instances; T007 shows runtime intermediates can depart materially from endpoint assumptions.
- Confirmation / transfer note: Type held constant here.
- Scope limit: no font recommendation.

## Color
- Useful finding/context: C001's forced-color warning transfers directly to layer elevation. Shadow-only elevation disappeared while interaction ownership remained correct.
- Confirmation / transfer note: **CONFIRMATION + REALISTIC LAYER TRANSFER** of forced-color channel loss.
- Scope limit: Layout does not define palette/system-color policy beyond requiring a structurally robust boundary channel.

## Layout / Interaction
- Useful finding/context: extend L006 review with forced-color resilience, touch implicit-capture transition policy, and semantic-tree ownership.
- Confirmation / transfer note: touch implicit capture confirms the previous explicit mouse capture failure class with a different input mechanism.
- Scope limit: screen-reader and physical-mobile behavior still open.

## Web Design
- Useful finding/context: future W### overlay integration should inherit this 28-assertion matrix in addition to prior L006 matrices.
- Validation consequence: test actual OS high contrast, actual AT, framework portals/focus scopes, mobile browsers and delivered fonts.
- Scope limit: Chromium lab evidence only.

---

# Project-readiness conclusion

A robust overlay is not merely a component that still *works* when colors change, nor one that merely *looks elevated* in the default theme.

It must keep the intended relationship aligned across:

> **visual boundary + new-hit ownership + active-gesture ownership + focus + semantic exposure + data mutation + stack/dismissal + restoration**

under the user and platform conditions that matter to the project.
