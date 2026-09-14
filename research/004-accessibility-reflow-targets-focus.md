# Study 004 — Accessibility Foundations: Reflow, Target Geometry, Focus, and Alternate Operation

Status: FOUNDATION STUDY / supports practice, not a completed gate.

## Question

How should accessibility constraints shape composition and interaction **before** visual polish rather than being treated as a late compliance pass?

## SOURCE — WCAG 2.2 Reflow

WCAG 2.2 Understanding SC 1.4.10 states that content should be presentable without loss of information or functionality and without two-dimensional scrolling at an equivalent width of 320 CSS pixels for vertically scrolling content, except where a two-dimensional layout is required for usage or meaning.

The guidance explicitly names data tables, maps, diagrams, video, games, and certain tool-manipulation interfaces as possible exceptions, while noting that content inside such layouts should still be made as usable as possible.

Source:
- https://www.w3.org/WAI/WCAG22/Understanding/reflow.html

### Studio synthesis

Responsive design is not “shrink the desktop canvas.”

When width or text scale changes, a professional composition should decide which relationships are:

- **semantic and must remain together**;
- **presentational and may stack/reorder**;
- **genuinely two-dimensional and may need controlled scrolling**.

A grid is therefore conditional infrastructure, not an immutable picture.

## SOURCE — target size is about activation error, not button aesthetics

WCAG 2.2 SC 2.5.8 defines a Level AA minimum target-size rule of 24×24 CSS pixels, with explicit exceptions including sufficient spacing, an equivalent control, inline links, user-agent controls, and essential presentations.

The Understanding document emphasizes the purpose: reducing accidental activation for people with limited dexterity or imprecise input, including touch, mouse, pen, or specialized input devices.

Source:
- https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html

### Studio synthesis

The visible mark and the interactive target are separate design layers.

A refined interface may use a visually small icon or thin text action while still providing a larger hit envelope. Conversely, a large-looking shadow/glow does not create a larger target unless the interactive geometry actually includes it.

## SOURCE — visible focus is structural information

WCAG 2.2 added Focus Not Obscured criteria and an enhanced Focus Appearance criterion. The W3C summary explains that keyboard focus must remain visible and, at the enhanced level, the indicator has explicit area and contrast requirements.

Source:
- https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/

### Studio synthesis

Focus is not an implementation artifact to hide for aesthetic cleanliness. It is a positional information channel.

A design system must allocate:

- physical space for the focus indicator;
- sufficient contrast against local surfaces;
- layering behavior so sticky headers, sheets, and overlays do not obscure focused elements;
- a predictable traversal path.

## SOURCE — dragging requires an alternative

WCAG 2.2 SC 2.5.7 requires functionality that uses dragging to also be achievable through a single-pointer alternative unless dragging is essential or controlled by the user agent.

Source:
- https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/

### Studio synthesis

Reorderable lists, sliders, canvases, timelines, and spatial controls must be designed as **interaction systems**, not gestures.

For example, a drag-to-reorder list may also provide:

- move up/down actions;
- keyboard reorder commands;
- explicit position menus;
- accessible increment/decrement controls.

The alternative should preserve the same semantic result even if the physical gesture differs.

## Relationship to platform guidance

Platform Human Interface Guidelines can provide stronger platform-specific targets or interaction conventions. WCAG should not be misread as the ideal design target merely because it defines minimum conformance thresholds.

Studio policy:

1. treat WCAG thresholds as floors for applicable web contexts;
2. use platform guidance and human-factor evidence for stronger defaults;
3. preserve the reason behind the rule when moving between web/native/desktop contexts;
4. document when a two-dimensional exception is genuinely essential rather than convenient for the existing design.

## Foundation checklist derived from the sources

For every interactive composition exercise:

### Reflow
- Can text and controls enlarge without clipping or semantic loss?
- Which areas genuinely require two-dimensional layout?
- Can supporting panels relocate or stack rather than force dual-axis scrolling?

### Targets
- Is the actual hit region known, not merely the visible mark?
- Are destructive and adjacent actions separated sufficiently?
- Is dense interaction still operable under tremor/imprecision assumptions?

### Focus
- Is focus visible in every state and layer?
- Can sticky surfaces obscure focused controls?
- Is the traversal order consistent with the visual/semantic order?

### Gesture alternatives
- If an action depends on drag, long-press, hover, or another high-precision gesture, is an equivalent lower-precision route available where required?

## Transfer to visual composition

Accessibility changes the composition itself:

- negative space may be functional target separation;
- hierarchy must survive larger type and reduced visible area;
- strong focus can coexist with premium visual restraint if it is designed as part of the system;
- compactness should come from information editing and alignment, not undersized hit regions;
- two-dimensional data should preserve meaning without turning every screen into a permanently zoomed-out table.

## Practice required before PASS

1. create one interface specimen with visible-control size separated from target size;
2. show the same information at wide and 320-equivalent narrow layouts;
3. demonstrate a data-table exception and how cell content remains readable;
4. show focus in normal, sticky-header, and overlay states;
5. show an alternative operation for a drag-reorder interaction;
6. critique failures and revise at least one state.

Until these are demonstrated, `Accessibility foundations` remains below PASS and `Interaction foundations` should not advance solely from reading.
