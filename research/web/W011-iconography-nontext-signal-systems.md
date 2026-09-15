# W011 — Iconography & Non-Text Signal Systems for Real Web Tasks

Status: **PRACTICE / CRITIQUE COMPLETE — Stage 2 explicit content gap closed; browser execution depth remains OPEN**  
Evidence intent: **SOURCE + SYNTHESIS + ORIGINAL COMPARATIVE PRACTICE + CRITIQUE + TRANSFER VALIDATION PLAN**  
Date: 2026-09-15

## PURPOSE

Close the explicit Stage 2 Web content gap identified by W010: direct Web-owned practice for iconography and non-text signals.

This is not an icon-style gallery. The unit of analysis is a realistic task surface containing navigation, search/filter, disclosure, async status, edit and destructive actions.

The study compares three complete signaling strategies for the same task surface and selects a direction using explicit criteria.

Human recognition/preference evidence is **DEFERRED TO LIVE APP/PRODUCT VALIDATION** and is not simulated.

---

## RELATED DOMAIN CHECK

### Type

Checked current Type status through T019 plus the newer T020 LogMate pre-implementation transfer commits visible on `main`.

Reusable finding: visible labels participate in layout geometry and can fail under enlargement/localization; compact technical surfaces should not solve geometry pressure by indiscriminately removing text. Exact font/platform transfer remains Type-owned.

### Color

Checked Color status through C015. Reused the established rule that hierarchy/state meaning must survive without hue and that forced/user-color behavior is distinct from authored palette intent.

Web implication: color may reinforce status or warning meaning, but cannot be the sole semantic carrier.

### Layout / Interaction

Checked Layout/Interaction status through L007/I006. Reused ownership separation: visible glyph, pointer target, focus owner, semantic owner and action owner are not automatically the same thing.

Web implication: an SVG is normally decorative inside a semantic `<button>` when the button owns the action/name; visible icon shape is not proof of behavior.

### Web

Checked W001–W010. W010 explicitly identified iconography/non-text signals as the only Stage 2 information/product-design requirement not directly baselined.

### Overlap classification

**TRANSFER VALIDATION + DIRECT WEB PRACTICE.** Peer accessibility/color/interaction findings are applied to a complete Web signaling problem; canonical peer ownership is not duplicated.

---

# 1. SOURCE BASELINE

## SOURCE — accessible naming

W3C ACT rule `Button has non-empty accessible name` maps button naming to WCAG 4.1.2 and requires each button in the accessibility tree to have a non-empty accessible name.

MDN's current `aria-label` guidance uses an icon-only SVG button as the canonical case for `aria-label`, but recommends visible text / `aria-labelledby` when an appropriate visible label exists. It also warns that important information should not be hidden only in an accessibility-only label.

**SYNTHESIS:** icon-only controls require a deliberate accessible-name contract; icon+visible-label controls should normally let the visible text supply the name rather than duplicate it with ARIA.

## SOURCE — SVG semantics

MDN documents SVG `<title>` as a short accessible description and notes that browsers usually expose it as a tooltip, while recommending reference to visible text when the graphic can be described by visible text.

**STUDIO JUDGMENT:** for an action button whose semantics belong to the button, prefer the button as the named semantic owner and mark the internal decorative SVG `aria-hidden="true"`; do not rely on SVG `<title>` as the primary control-label strategy.

## SOURCE — target geometry

WCAG 2.2 SC 2.5.8 defines a 24×24 CSS-pixel minimum pointer target at AA, subject to stated exceptions/spacing conditions.

**STUDIO JUDGMENT:** 24×24 is a conformance floor, not the default product target recommendation. Dense icon-only toolbars should normally preserve a larger hit area even when the glyph itself is visually smaller.

## SOURCE — forced colors

MDN documents `forced-colors` as a user-agent mode using a limited user-chosen palette. It notes that UA forcing is based on native element semantics rather than ARIA role simulation and that properties such as `box-shadow` may disappear. MDN also documents SVG `currentColor` as an indirect value usable by `fill` and `stroke`.

**SYNTHESIS:** native semantic controls + `currentColor` SVGs provide a robust default transfer path; authored hue, shadow, and decorative surface treatment must not be the only carrier of control/state meaning.

---

# 2. SIGNAL ROLE MATRIX

| Role | User question | Default representation | Icon-only threshold | State contract |
| --- | --- | --- | --- | --- |
| navigation | Where will this take me? | text label; icon may reinforce | only highly conventional, repeatedly used compact nav with explicit name | current destination must not rely on hue alone |
| action | What will happen now? | icon + verb for consequential/less-familiar actions | familiar repetitive actions under severe density pressure | disabled/pending/pressed behavior belongs to control, not SVG |
| disclosure | Is more content/options hidden here? | conventional chevron + relationship/state | acceptable when context makes target unambiguous | expanded/collapsed state must be programmatic (`aria-expanded`) |
| status | What is true now? | status word + optional symbol | icon-only only for redundant, noncritical secondary display | status meaning survives hue removal |
| warning | What risk needs attention? | explicit warning text + symbol | reject for consequential warning | severity/action cannot be encoded only by shape/color |
| destructive action | What irreversible/high-cost action is available? | visible verb where practical; icon may reinforce | only in repeated object-row contexts with strong surrounding identity and accessible name | confirmation/recovery policy independent of trash glyph |
| data marker | What category/value does this mark? | symbol + legend/label | only when legend/adjacent value establishes meaning | not interactive unless explicitly modeled as a control |

Core distinction:

`signal shape != semantic owner != action owner != state owner`.

---

# 3. FIXED TASK SURFACE

A portfolio/logbook-like Web workspace is used only as a generic real-task substrate:

- primary navigation;
- search;
- filter toggle;
- table/list rows;
- row disclosure;
- save/sync status;
- edit action;
- delete action;
- warning state.

The information and actions are held constant across all three directions.

---

# 4. THREE COMPLETE DIRECTIONS

## Direction A — Text-first explicit controls

Examples:

- `Search`, `Filter`, `Edit`, `Delete`, `More details`;
- `Saved`, `Syncing`, `Sync failed` as status text;
- icons used sparingly as decoration/reinforcement.

### KEEP

- highest explicitness for unfamiliar/consequential tasks;
- strongest localization/translatability semantics;
- visible label and accessible name naturally converge;
- resilient when icon styling or color disappears.

### REWORK

- toolbar width pressure at narrow widths;
- repeated row actions can become visually noisy;
- long translations may force recomposition.

### REJECT WHEN

- the surface is extremely repetitive/dense and the text repetition materially harms scan/available data width.

---

## Direction B — Icon + label semantic pair

Examples:

- magnifier + `Search`;
- funnel + `Filter`;
- pencil + `Edit`;
- trash + `Delete`;
- chevron + row label/context;
- status symbol + `Saved`/`Syncing`/`Failed`.

The semantic control owns the accessible name through visible text. Internal SVG is decorative (`aria-hidden=true`) unless the graphic itself is independent content.

### KEEP

- supports recognition without making symbol interpretation mandatory;
- visible text remains available for unfamiliar/consequential actions;
- icon can support scan speed and state grouping;
- `currentColor` allows icon to follow text/system color in forced-color transfer.

### REWORK

- responsive layout must decide which pairs wrap, move, or become menu items;
- icon and text cannot be allowed to become competing names;
- icon family must preserve role distinction rather than visual sameness.

### REJECT WHEN

- decorative icons add clutter but no task differentiation;
- every label receives an icon merely for visual consistency.

---

## Direction C — Compact icon-only toolbar

Examples:

- magnifier, funnel, pencil, trash, kebab, chevron with no visible labels;
- every interactive icon button has an explicit accessible name;
- tooltip/help is supplemental, not the only semantic mechanism;
- target box remains at least 24×24 CSS px under the WCAG floor, with a larger product default preferred.

### KEEP

- can preserve horizontal space in highly repetitive expert workflows;
- useful for conventional disclosure/overflow actions and some repeated row controls.

### REWORK

- requires explicit accessible naming for every control;
- requires strong focus, target and tooltip/help behavior;
- localization pressure moves from visible label geometry to accessible-name/help content but does not disappear;
- unfamiliar symbols remain recall/learning costs.

### REJECT WHEN

- warning, status, destructive consequence, or unfamiliar domain action would become symbol-only;
- the design assumes `title`/hover is sufficient;
- touch or keyboard use is treated as secondary;
- color/shape alone carries selected/current/error meaning.

---

# 5. SELECTION CRITERIA

Weighted qualitative criteria for the fixed task surface:

| Criterion | Weight | A text-first | B icon+label | C icon-only |
| --- | ---: | ---: | ---: | ---: |
| semantic explicitness | 5 | 5 | 5 | 2 |
| dense-space efficiency | 4 | 2 | 3 | 5 |
| accessibility naming alignment | 5 | 5 | 5 | 3 |
| localization/enlargement resilience | 4 | 3 | 3 | 4* |
| forced-color/state resilience | 4 | 5 | 5 | 3 |
| unfamiliar/consequential action safety | 5 | 5 | 5 | 2 |
| scan differentiation | 3 | 3 | 5 | 4 |

`*` Icon-only saves visible label width but does not remove localization/semantic obligations; accessible names and supplemental help still require correct language.

## SELECTED DIRECTION — B with bounded C exceptions

Use **icon + visible label as the default for actionable toolbar controls**, with bounded icon-only exceptions for:

- conventional disclosure/overflow controls;
- highly repetitive row actions where surrounding object context is stable;
- compact modes where an equivalent labeled route remains available or the symbol is demonstrably conventional.

Use **text-first** for consequential warnings/status explanations and when icon addition has no differentiation value.

This is deliberately not a single global icon policy. Signal role and task consequence determine the representation.

---

# 6. IMPLEMENTATION CONTRACT

## Named control owner

Preferred labeled control:

```html
<button type="button">
  <svg aria-hidden="true" focusable="false" ...></svg>
  <span>Edit</span>
</button>
```

Preferred icon-only exception:

```html
<button type="button" aria-label="More actions">
  <svg aria-hidden="true" focusable="false" ...></svg>
</button>
```

Disclosure:

```html
<button type="button" aria-expanded="false" aria-controls="row-details-42">
  <svg aria-hidden="true" focusable="false" ...></svg>
  <span>Details</span>
</button>
```

## Color contract

- SVG action icons use `fill: currentColor` or `stroke: currentColor` where appropriate;
- state/warning meaning includes text, native semantics, or another non-color carrier;
- do not depend on shadow alone for control boundary in forced colors;
- avoid `forced-color-adjust:none` unless preserving authored color is essential and separately justified.

## Geometry contract

- semantic target box, not glyph path bounds, defines pointer target;
- WCAG 2.2 AA floor: 24×24 CSS px unless an explicit exception applies;
- product default should remain larger where density permits;
- text enlargement/localization triggers recomposition, not silent label deletion.

## Tooltip contract

Tooltip/help is **supplemental**. It may explain an icon-only control but must not be the sole accessible name or sole path to understanding a consequential action.

---

# 7. NON-HUMAN VALIDATION MATRIX

A later executable browser harness should assert at minimum:

1. every semantic button has a non-empty accessible name;
2. visible-label controls do not receive conflicting duplicate ARIA names;
3. decorative SVGs are removed from the semantic naming path;
4. disclosure exposes `aria-expanded` and controls the intended region;
5. icon-only targets remain >=24×24 CSS px or document the applicable exception;
6. 200% text enlargement preserves labeled-control access by wrapping/recomposition/menu transfer rather than clipping/removal;
7. long localized labels do not overlap adjacent targets;
8. keyboard focus remains visible for all controls;
9. forced-colors transfer preserves control boundaries and status/warning semantics;
10. icon SVGs using `currentColor` follow the effective control text/system color;
11. hover-only tooltip is not required to operate or name a control;
12. selected/current/error/pending state is not communicated by hue alone.

## OPEN

This run did not execute a new browser harness. W010 already identified Web's broader runtime-depth imbalance, and W011 closes the **content/practice gap**, not that execution-depth gap.

Next Web priority should therefore be an integrated executable browser transfer rather than another broad theory topic.

---

# 8. PROJECT-READINESS RULES

Use icon-only when:

- the symbol is conventional in the actual task context;
- repetition/density pressure is real;
- the semantic control has an explicit accessible name;
- focus/touch/keyboard geometry is preserved;
- loss of visible text does not hide consequential meaning.

Do not use icon-only when:

- domain meaning is unfamiliar or culturally unstable;
- warning/status/consequence requires explanation;
- the design is merely chasing visual minimalism;
- hover/title is assumed to solve naming;
- forced colors or color loss would erase the distinction.

Required project inputs:

- task frequency and consequence;
- user expertise/context;
- viewport/density constraints;
- localization corpus;
- state model;
- input methods;
- accessibility requirements;
- icon convention evidence.

---

## HANDOFFS TO OTHER SPECIALISTS

### Type

Confirms Type's geometry concern: removing labels is not a legitimate default response to enlargement/localization pressure. Exact font/fallback metrics remain Type-owned.

### Color

Confirms Color's semantic resilience rule in a Web signaling context: hue may reinforce status, but status/warning/action meaning requires a non-color carrier.

### Layout / Interaction

Transfers L006 ownership separation into icon controls: SVG visual owner and semantic/action/focus owner can differ. Target geometry belongs to the semantic control, not glyph bounds.

### Web

The explicit Stage 2 iconography/non-text-signal content gap is now directly practiced and critiqued. The next imbalance is reproducible execution of already-authored W003–W008/W011 contracts.

---

## EVIDENCE LEVEL

**SOURCE + SYNTHESIS + ORIGINAL THREE-DIRECTION PRACTICE + KEEP/REWORK/REJECT CRITIQUE + CROSS-SPECIALIST TRANSFER.**

No human, AT, Firefox/Safari, physical-device, or new browser-runtime PASS is claimed.
