# L006 — Layer Ownership as a Cross-Contract: Visual Boundary, Hit Testing, Focus, and Inertness

Status: **PRACTICE + CRITIQUE / REALISTIC L001 TRANSFER + INTERACTION COUPLING — controlled Chromium failure→revision proof established; human perceived-layering, AT, multi-browser/device and production-component validation remain OPEN**

Owner: Layout, Spatial & Interaction Specialist  
Canonical path: `research/layout/`

Reproducible artifacts:

- `research/layout/L006-layer-ownership-specimen.html`
- `research/layout/L006-layer-ownership-playwright.py`
- `research/layout/L006-layer-ownership-results-summary.json`

## Question

When an interface visually presents one surface as being above another, what additional contracts must agree with that visual ownership so the user does not interact with the wrong layer?

L006 transfers the abstract figure-ground/border-ownership work from L001 into realistic interface structures:

- non-modal popover;
- sticky controls overlapping scrollable content;
- modal sheet over an editor.

The experiment deliberately distinguishes **perceived/visual ownership** from **interaction ownership**. A screenshot can suggest that the foreground owns a region while hit testing or keyboard focus still belongs to the obscured background.

---

## RELATED DOMAIN CHECK

### Typography / Type
- Evidence checked: `progress/TYPE_STATUS.md` through T005.
- Reusable finding: rendered appearance and behavioral/semantic meaning are different evidence layers; text expansion can later alter layer geometry.
- Replication / challenge / transfer opportunity: localize popover/sheet controls and stress long labels after the ownership contract is stable.
- Dependency / overlap: no Type conclusion is claimed here.

### Color
- Evidence checked: Color through C007 plus Layout L005.
- Reusable finding: visual salience can change while geometry stays fixed; authored shadows/fills can be lost or redistributed under overrides.
- Replication / challenge / transfer opportunity: later test whether layer ownership remains clear under forced colors, dark theme and reduced visual effects.
- Dependency / overlap: L006 holds foreground/background pixels equal between broken and revised behavior pairs. Color is not used to rescue the revised version.

### Layout / Interaction
- Evidence checked:
  - L001 figure-ground/border ownership and its cue-isolation validation;
  - I001 focus/restoration/navigation;
  - I003 color-channel-independent state semantics.
- Reusable finding:
  - border ownership is contextual;
  - focus and pointer behavior are interaction state, not decoration;
  - visual and semantic structures should agree.
- Replication / challenge / transfer opportunity: test whether visually identical layers can have opposite hit/focus ownership.
- Dependency / overlap: spatial layering is primary; focus/hit/inertness are Interaction coupling requirements.

### Web Design
- Evidence checked: `progress/WEB_STATUS.md`; no substantive W### result exists at this checkpoint.
- Reusable finding: complete production browser/page integration remains Web-owned.
- Implementation/application validation opportunity: reproduce with actual `<dialog>`, `popover`, framework portals, sticky headers, production z-index/token systems and target browsers.
- Dependency / overlap: this controlled Chromium specimen is an independent Layout/Interaction validation, not Web PASS.

### Other / cross-cutting
- WAI-ARIA APG Modal Dialog Pattern: https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/
- HTML Living Standard `inert`: https://html.spec.whatwg.org/multipage/interaction.html#the-inert-attribute
- HTML Living Standard `popover`: https://html.spec.whatwg.org/multipage/popover.html

Relevant source constraints:
- a modal dialog makes underlying content unavailable for interaction and keeps keyboard focus inside the dialog;
- inert subtrees are removed from normal hit-testing/focus interaction;
- a shown HTML popover is rendered above other page content.

### Overlap decision
- **L001 REALISTIC TRANSFER + INTERACTION COUPLING + FAILURE REPRODUCTION**.
- Why: L001 established perceptual-boundary methodology. L006 asks whether the same intended foreground also owns input/focus where the surfaces overlap.

---

# SOURCE / SYNTHESIS BOUNDARY

## SOURCE

The WAI-ARIA APG modal dialog pattern specifies that content below a modal dialog is inert and that Tab/Shift+Tab remain inside the dialog.

The HTML Living Standard defines inert subtrees as non-interactive for hit testing/focus and defines modal top-layer behavior. The Popover section defines shown popovers as rendered over other page content.

## SYNTHESIS

A visual layer hierarchy does not by itself create the correct interaction hierarchy.

## STUDIO JUDGMENT

For any overlaying component, explicitly define an **ownership vector**:

`visual owner / pointer owner / keyboard-focus owner / semantic-AT owner / action-data owner`

These owners do not always need to be globally identical, but any difference must be intentional.

Examples:

- non-modal popover: foreground owns its own overlap region; background outside the popover may remain interactive;
- sticky toolbar/header: foreground owns the pixels it covers; scroll content outside that region remains active;
- modal sheet/dialog: foreground owns the active task while the underlay becomes inert.

---

# CONTROLLED EXPERIMENT

## Pair design

Three UI structures each have a **broken** and **revised** version:

1. popover;
2. sticky header/controls;
3. modal sheet.

For every pair:

- dimensions are identical;
- foreground surface, border and shadow are identical;
- underlying workspace is identical;
- foreground/background controls are deliberately placed at the same screen coordinate;
- broken vs revised **pixels are identical** before focus/click interaction.

Only behavioral ownership differs.

### Broken condition

- foreground visuals remain present;
- foreground layer uses `pointer-events:none`, so hit testing falls through;
- modal underlay is not inert;
- modal keyboard traversal is not contained.

### Revised condition

- pixels are unchanged;
- foreground receives pointer interaction in its visible region;
- modal underlay is inert;
- modal forward and reverse focus traversal remain in the foreground task.

---

# FAILURE → REVISION

## Failure 1 — visual popover, background action fires

At the screen coordinate occupied by the visible foreground `Open details` action:

Broken:
- `elementFromPoint` resolves to the background `Delete record` action;
- one click produces `background = 1`, `foreground = 0`.

Revised:
- the same visible pixels resolve to the foreground action;
- one click produces `background = 0`, `foreground = 1`.

### Consequence

A surface can be visually unambiguous yet behaviorally owned by the wrong object.

Do not treat `z-index`, shadow or border as proof that the foreground actually owns the interaction.

---

## Failure 2 — sticky layer visually covers a row but click reaches the row

Broken:
- the visible sticky `Filter` control is above the row;
- the same coordinate activates the underlying row action.

Revised:
- the sticky control owns the covered coordinate.

### Consequence

Sticky headers/toolbars create real occlusion. Covered content should not remain accidentally actionable through the covering layer.

This does **not** mean the entire scroll area becomes inert. Ownership is local to the covered region.

---

## Failure 3 — modal sheet looks modal but background remains active

Broken:
- the dimming backdrop and sheet are visually present;
- clicking at the visible `Confirm` coordinate activates the obscured background commit action;
- starting on the sheet and pressing `Shift+Tab` moves focus to the background input, then the background action.

Observed broken reverse sequence:

`foreground Confirm → background input → background Commit`

Revised:
- the same foreground/background pixels are preserved;
- foreground receives the click;
- background subtree is inert;
- `Shift+Tab` and `Tab` remain within `Confirm / Cancel`.

Observed revised sequence:

`Confirm ↔ Cancel` only.

### Consequence

A dimmed background is not equivalent to modal behavior.

Modal ownership needs:
- visual separation;
- hit-test exclusion of the underlay;
- keyboard containment;
- semantic modal/inert treatment;
- explicit close/restoration policy.

---

# CONTROLLED RESULT

Chromium `144.0.7559.96`.

Automated assertions: **15 / 15 PASS** after revision.

Pixel controls:
- popover workspace diff: `0`;
- popover layer diff: `0`;
- sticky workspace diff: `0`;
- sticky layer diff: `0`;
- sheet workspace diff: `0`;
- sheet layer diff: `0`.

Therefore the behavioral differences were established without changing the paired visual rendering.

This is particularly important:

> **The screenshot cannot tell whether the visible foreground owns the input.**

Visual QA alone is insufficient for layered interactive components.

---

# PROJECT DIAGNOSTIC MODEL

When reviewing a popover, dropdown, sheet, modal, sticky header, floating toolbar or drag target, ask separately:

### 1. Visual ownership
- Which object appears above/inside/in front?
- Which contours, occlusion, enclosure and elevation cues support that claim?

### 2. Pointer ownership
- What does hit testing return inside the foreground's visible region?
- Can a covered destructive/background control still activate?

### 3. Keyboard ownership
- Is the layer modal or non-modal?
- If modal, can both Tab **and Shift+Tab** escape?
- If non-modal, what keyboard route intentionally returns to the background?

### 4. Semantic / assistive-technology ownership
- Is the modal/non-modal relationship represented semantically?
- Are inert/hidden/unavailable regions actually unavailable to AT where required?
- Is focus placed and restored according to task structure?

### 5. Data/action ownership
- Which object receives the mutation?
- Can an action visually presented inside a foreground layer accidentally mutate the background object?

---

# REUSABLE RULES

1. **Visual ownership is necessary but not sufficient.**
2. **A screenshot cannot validate layer interaction ownership.**
3. **Non-modal and modal ownership are different contracts.**
4. **Occluded background controls must not activate through an opaque foreground.**
5. **Modal testing must include reverse traversal (`Shift+Tab`), not only forward Tab.**
6. **Dimming does not create inertness.**
7. **Do not solve a behavioral ownership bug by adding more shadow/border.**
8. **Do not make the entire page inert for a non-modal popover merely because it is visually elevated.**
9. **Layer design should record ownership across visual, pointer, keyboard, semantic and data channels.**

---

# EVIDENCE LIMITS / OPEN

This study does not establish:

- human judgments of which layer appears foreground;
- screen-reader behavior;
- cross-browser/platform equality;
- native mobile layering;
- production framework portal behavior;
- touch/gesture capture;
- pointer capture during drag;
- nested overlays;
- focus restoration after dismissal;
- system forced-colors/reduced-transparency transfer;
- actual HTML `popover`/native `<dialog>` implementation quality.

The present custom DOM specimen isolates the ownership contract. Production implementation remains a later Web/platform transfer.

---

# HANDOFFS TO OTHER SPECIALISTS

## Typography / Type
- Useful finding/context: layer ownership testing should later include long/localized labels because wrapping can change overlap and hit regions.
- Confirmation / transfer note: no Type conclusion; use L003/T005 conditions in production transfer.
- Scope limit: typography held constant here.

## Color
- Useful finding/context: broken and revised ownership pairs are pixel-identical, proving that Color/elevation treatment cannot establish behavioral ownership by itself.
- Confirmation / transfer note: complements C001/I003 and C007/L005; appearance and operational semantics remain distinct.
- Scope limit: no color-salience/perception threshold.

## Layout / Interaction
- Useful finding/context: L001 contextual boundary ownership now has a realistic interaction coupling rule.
- Canonical consequence: record visual/pointer/keyboard/semantic/data ownership explicitly for layered components.
- Confirmation / transfer note: extends I001 focus-state work and L001 border-ownership work.
- Scope limit: human figure-ground perception remains unmeasured.

## Web Design
- Useful finding/context: transfer the 15-assertion matrix to native `<dialog>`, `popover`, portal/overlay systems, sticky page chrome and framework focus managers.
- Validation consequence: pixel/screenshot tests alone cannot approve an overlay.
- Scope limit: Chromium custom-DOM proof only.

---

# Project-readiness conclusion

For real projects, do not ask only:

> “Does this look like a popover/modal?”

Ask:

> “Does the object that visually owns this region also own pointer, focus, semantics and mutation to the degree required by its modality?”

That is the actionable transfer from L001 figure-ground theory into interactive product layering.
