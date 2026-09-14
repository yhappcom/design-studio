# I003 — State Semantics Under Color-Channel Loss: Forced Colors, Focus, Current Location, and Async Status

Status: **PRACTICE + CRITIQUE / COLOR→INTERACTION TRANSFER VALIDATION — controlled Chromium forced-colors evidence established; cross-browser/OS/AT/production validation remains OPEN**

Owner: Layout, Spatial & Interaction Specialist  
Canonical path: `research/interaction/`

Reproducible artifacts:

- `research/interaction/I003-forced-colors-validation-playwright.py`
- `research/interaction/I003-forced-colors-results-summary.json`

## Question

If authored fill, shadow, glow, and literal state colors are removed or replaced by the browser/user, do Interaction semantics such as **current location, focus, pending, failed, outcome unknown, and confirmed** remain understandable?

This study does not define a Color palette. It transfer-tests Color's C001/C002 requirements against Interaction-owned semantics from I001/I002.

---

## RELATED DOMAIN CHECK

### Typography / Type
- Evidence checked:
  - `progress/TYPE_STATUS.md` through T005.
- Reusable finding:
  - state labels and navigation labels are real semantic text roles and can later be stressed by fallback/localization/enlargement.
- Replication / challenge / transfer opportunity:
  - rerun robust state labels with Korean/English mixed strings and long localization.
- Dependency / overlap:
  - Type owns font/fallback/rendering behavior; I003 holds typography simple so color-channel loss is the principal variable.

### Color
- Evidence checked:
  - `research/color/C001-web-color-user-override-resilience.md`;
  - `research/color/C002-semantic-color-role-token-architecture.md`;
  - current Color status through C004.
- Reusable finding:
  - forced colors can replace authored fills/borders/colors and remove shadows;
  - state meaning should not depend on one literal color channel;
  - semantic role must precede literal token/component color assignment.
- Replication / challenge / transfer opportunity:
  - independently reproduce C001's browser failure hypothesis using real Interaction state examples.
- Dependency / overlap:
  - Color owns visual encoding and color-system resilience; Interaction owns what selected/current/focused/pending/failed/unknown/confirmed mean.

### Layout / Interaction
- Evidence checked:
  - `research/interaction/I001-navigation-history-focus-restoration-interruption.md`;
  - `research/interaction/I002-latency-pending-optimistic-retry.md`;
  - current `progress/LAYOUT_STATUS.md`.
- Reusable finding:
  - current location, focus and async states are semantic/behavioral distinctions before styling;
  - failed and outcome-unknown must not be collapsed;
  - focus must remain perceivable without stealing or losing focus.
- Replication / challenge / transfer opportunity:
  - remove color-dependent visual channels and test whether semantics survive.
- Dependency / overlap:
  - primary canonical ownership for this study remains Interaction.

### Web Design
- Evidence checked:
  - `progress/WEB_STATUS.md`;
  - `research/web/README.md`.
- Reusable finding:
  - Web owns production browser/page/component integration and device/browser validation.
- Implementation/application validation opportunity:
  - reproduce with production tokens/components, native/custom controls, actual Windows High Contrast/forced-color environments, target browsers, and AT.
- Dependency / overlap:
  - no substantive W### evidence existed at this checkpoint; I003 is an Interaction-owned independent browser transfer study, not Web canonical proof.

### Other / Cross-cutting / Future Specialist
- Evidence checked:
  - C001's underlying CSS Color Adjustment/WCAG evidence;
  - Chromium forced-colors emulation used in this study.
- Reusable finding:
  - user/browser color replacement is an adversarial test of whether semantics are encoded structurally.
- Dependency / overlap:
  - emulation is not identical to every OS/browser high-contrast environment.

### Overlap decision
- **INDEPENDENT VALIDATION + TRANSFER VALIDATION + ADVERSARIAL REVIEW**.
- Why:
  - C001 explicitly requested browser validation of selected/focus/state resilience. I003 uses real Interaction semantics rather than abstract color swatches.

---

# 1. Controlled specimen

The specimen contains two parallel implementations.

## Naive variant

- current navigation location indicated only by blue fill;
- focus indicated only by a box-shadow glow after explicitly removing the outline;
- four async states represented only by different background colors:
  - pending;
  - failed;
  - outcome unknown;
  - confirmed.

The empty state blocks include accessible names so the experiment specifically isolates **visual semantic collapse** rather than claiming AT behavior from color alone.

## Robust variant

- current navigation exposes `aria-current="page"` and also uses persistent structural cues: stronger border, font weight and underline;
- focus uses an actual outline rather than a shadow-only glow;
- async states use explicit visible text (`Pending`, `Failed`, `Outcome unknown`, `Confirmed`) plus non-color structural cues.

This is a controlled research specimen, not a universal component design.

---

# 2. Browser environment

- Chromium `144.0.7559.96` on Debian;
- Playwright `forced_colors="active"` media emulation;
- headless browser;
- no production design system or application framework.

Scope warning:

> Chromium forced-colors emulation is implementation evidence for this engine/environment, not proof of Windows High Contrast, Firefox/Safari parity, OS-specific system colors, or assistive-technology output.

---

# 3. Baseline normal-color condition

Before forced colors:

- naive navigation uses visibly different background fills for current vs non-current tabs;
- naive pending/failed/unknown/confirmed blocks have four distinct authored fills;
- naive focus has a visible `box-shadow` glow;
- robust structural cues are also present.

This confirms the naive specimen appears distinguishable in its intended authored palette before the adversarial condition is applied.

---

# 4. Forced-colors failure

After enabling Chromium forced colors:

## F1 — selected/current fill collapses

Naive navigation backgrounds resolve to the same white used color across all three tabs.

The authored blue selected fill therefore no longer visually distinguishes the current location.

## F2 — async state fills collapse

The four naive state backgrounds that were distinct in normal rendering all resolve to the same white used color.

Pending, failed, outcome-unknown and confirmed therefore become visually identical when color was the only visible state channel.

## F3 — box-shadow focus disappears

The naive focus glow is present in normal rendering but computed as `none` under forced colors.

Because the specimen intentionally removed its outline, the control has no remaining authored structural focus indication in this forced-color condition.

### TRANSFER VALIDATION

These failures directly confirm C001's hypothesis that fill/shadow/glow-only state encoding is fragile under browser/user color replacement.

---

# 5. Robust re-proof

The robust variant preserves non-color/state semantics under the same forced-color emulation.

## Current location

The current `Records` navigation item retains:

- `aria-current="page"`;
- stronger structural border width;
- underline;
- stronger text weight.

The browser may replace literal colors, but the structural distinction remains.

## Focus

The robust control retains a visible structural outline under forced colors. The literal outline color is browser-resolved, but the outline's existence and geometry remain.

## Async state

The four I002-derived semantic states retain explicit visible text:

- `Pending`;
- `Failed`;
- `Outcome unknown`;
- `Confirmed`.

Even when their authored fills no longer provide differentiation, the states do not collapse into one meaning.

---

# 6. Automated assertions

The final Playwright harness passes **14/14 assertions** covering:

1. forced-colors media query is actually active;
2. naive current fill is distinct in normal mode;
3. naive current fill collapses under forced colors;
4. naive async fills are distinct normally;
5. naive async fills collapse under forced colors;
6. naive focus glow exists normally;
7. naive focus glow is removed in forced colors;
8. naive focus has no fallback structural outline;
9. robust current item exposes `aria-current`;
10. robust current item retains stronger structural border;
11. robust current item retains underline;
12. robust focus outline survives;
13. robust async states retain explicit visible labels;
14. robust async labels remain semantically distinct without authored fill.

The fact that the naive assertions deliberately pass when failure is reproduced is important: this harness is proving the **failure mechanism and the revised resilience contract**, not pretending the naive design succeeds.

---

# 7. Interaction design consequences

## State semantics first, color second

For interaction-critical states, define the semantic distinction before assigning color.

Examples:

- current vs available destination;
- focused vs not focused;
- pending vs failed;
- failed vs outcome unknown;
- confirmed vs merely optimistic/local.

Color may reinforce the state but should not create the state definition.

## Structural redundancy should match importance

Useful non-color channels include:

- visible text/state labels;
- border/outline presence or thickness;
- underline;
- shape/iconography with textual support where needed;
- position/grouping;
- programmatic state such as `aria-current`;
- focus semantics and logical DOM behavior.

Do not add redundant decoration mechanically. Use enough channels that the state remains perceivable when one channel is removed.

## Failed and outcome-unknown require distinct semantics

I002 established that these states can demand different recovery paths. I003 adds that they must also remain visually/semantically distinguishable when authored warning colors are replaced.

A product should not rely on “red vs purple” or similar palette distinctions to communicate whether retry is safe.

## Focus effects must survive effect removal

A glow or shadow can reinforce focus but should not be the only focus geometry in environments where such effects may be removed.

---

# 8. Project decision protocol

For any interactive color/state system, list critical states first:

1. current location;
2. focus;
3. selected/checked;
4. pending/busy;
5. failed;
6. outcome unknown;
7. confirmed/success;
8. disabled/unavailable where relevant.

For each state, document:

- semantic meaning;
- interaction consequence;
- visual channels;
- programmatic state;
- what remains if authored fill/hue/shadow is removed;
- what recovery/action is allowed.

Then adversarially test:

- forced colors / high-contrast environment when relevant;
- grayscale/hue removal when useful;
- keyboard focus traversal;
- theme substitution;
- actual production components and browser-native controls.

---

# 9. Failure modes

Rework when:

- current navigation is only a colored fill;
- focus is only a glow/shadow;
- error vs unknown vs success is only hue;
- forced-color support is "fixed" by globally opting out of browser adjustment;
- a token system has semantic names but the component still exposes no non-color cue;
- visual state remains visible but programmatic state is absent;
- programmatic state exists but sighted users lose all visible differentiation after color replacement;
- Color is asked to compensate for an Interaction state model that never distinguished failed from unknown in the first place.

---

# 10. Evidence level and OPEN

Established:

- actual Chromium forced-colors emulation;
- computed-style evidence of fill convergence and shadow removal;
- controlled naive failure;
- robust structural/textual re-proof;
- 14 automated assertions.

Still OPEN:

1. Windows High Contrast on physical/virtual Windows;
2. Firefox and other browser engines;
3. Safari/macOS/iOS equivalent user-color/accessibility environments;
4. screen-reader announcement and AT behavior;
5. production design tokens/components;
6. native/custom form controls;
7. actual C002 token resolver implementation;
8. dark/light/contrast-preference combinations;
9. human state-recognition performance;
10. data visualization/forced-colors alternate representations.

No PASS promotion is claimed.

---

## Project Readiness Test

### When should this knowledge be applied?
- any web/app surface where color encodes interaction state, current location, focus, failure, uncertainty, pending or success.

### When should it not be over-applied?
- do not force heavy labels/borders onto every decorative color difference; prioritize semantically consequential states.

### What concrete decisions can change?
- whether a selected state needs a structural cue;
- whether focus uses outline vs shadow-only treatment;
- whether async status requires explicit text;
- whether failed and outcome-unknown need separate content/action patterns;
- whether browser forced-color adjustment can remain enabled;
- which states become mandatory QA cases.

### How should it be validated?
- production components;
- target OS/browser accessibility modes;
- keyboard and AT;
- real tokens/themes;
- representative users/tasks when state recognition is consequential.

---

## HANDOFFS TO OTHER SPECIALISTS

### Typography / Type
- Useful finding/context:
  - explicit state labels become the surviving semantic channel when color fills collapse.
- Canonical section:
  - robust async-state re-proof.
- Confirmation / contradiction / transfer note:
  - future Type validation should ensure localized/fallback/enlarged status labels remain legible and do not create new layout failures.
- Scope limit:
  - I003 does not define typography roles or font selection.

### Color
- Useful finding/context:
  - C001's predicted fill/shadow failure is independently reproduced in Chromium with real Interaction semantics.
- Canonical section:
  - Sections 4–6.
- Confirmation / contradiction / transfer note:
  - **CONFIRMATION + IMPLEMENTATION-LIMITED TRANSFER**: authored tab/state fills converged and box-shadow focus disappeared under Chromium forced colors; structural/text cues survived.
- Scope limit:
  - this is not cross-browser, OS, physical display or Color-system PASS.

### Layout / Interaction
- Useful finding/context:
  - current location, focus, pending, failed, unknown and confirmed must remain distinguishable without authored hue/fill/shadow.
- Canonical section:
  - Sections 5–8.
- Confirmation / contradiction / transfer note:
  - extends I001/I002 by adversarially removing a visual channel rather than changing the state model.
- Scope limit:
  - human recognition and AT remain open.

### Web Design
- Useful finding/context:
  - a reproducible forced-colors Interaction matrix is available for production transfer.
- Web application / validation consequence:
  - reproduce with real design tokens/components, system/native controls, target browsers, Windows High Contrast/forced colors and AT; test any `forced-color-adjust` exceptions explicitly.
- Confirmation / contradiction / transfer note:
  - current result is controlled Chromium emulation, not W### evidence.
- Scope limit:
  - Web page/system integration remains Web-owned.
