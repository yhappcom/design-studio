# C001 — Web Color Transfer: User Overrides, Forced Colors, and Semantic Resilience

Status: **SOURCE STUDY + PROJECT-READINESS SYNTHESIS / browser implementation validation pending**

## Why this study exists

The Color program already has strong foundations in luminance/contrast, colorimetry, perceptual spaces, gamut, and ramp authoring. A new Web Design Specialist is now part of Design Studio, so one immediate Color responsibility is to identify which color conclusions need transfer validation in actual web/browser conditions.

This study asks a practical product question:

> When a web product uses authored palettes, semantic colors, dark/light themes, focus states, and brand accents, what must remain true when the browser or user overrides those colors?

This is not a general Web Design study. It is a **Color-owned transfer study** about color-system resilience when browser/user preferences change the used colors.

## RELATED DOMAIN CHECK

### Typography / Type
- Evidence checked: `progress/TYPE_STATUS.md`, `research/type/README.md`, especially the requirement for realistic text roles, scaling, fallback, and rendered contexts.
- Reusable finding: contrast evaluation must use realistic text roles and rendered conditions rather than abstract swatches alone.
- Replication / challenge / transfer opportunity: Web forced-colors and theme testing should later include real text sizes/weights and fallback fonts, not placeholder typography.
- Dependency / overlap: Type owns typographic structure and rendering; Color owns foreground/background/system-color behavior.

### Color
- Evidence checked: `008-color-luminance-contrast-hierarchy.md`, `013-perceptual-color-spaces-difference.md`, `016-color-gamut-wide-gamut-mapping.md`, `017-perceptual-ramp-authoring.md`.
- Reusable finding: color must not be the sole carrier of meaning; authoring-space regularity does not prove accessibility or production behavior; final used colors can differ from source/authoring values.
- Replication / challenge / transfer opportunity: this study transfers those conclusions into browser user-override conditions.
- Dependency / overlap: direct extension of canonical Color evidence.

### Layout / Interaction
- Evidence checked: `progress/LAYOUT_STATUS.md`, `research/layout/README.md`, `research/interaction/README.md`.
- Reusable finding: state semantics, navigation, focus meaning, feedback, recovery, and spatial grouping cannot depend on Color alone.
- Replication / challenge / transfer opportunity: when forced colors remove fills, shadows, and authored state colors, Interaction evidence should determine whether the state still remains understandable.
- Dependency / overlap: Layout/Interaction owns state semantics and behavior; Color validates whether its visual encoding survives palette replacement.

### Web Design
- Evidence checked: `progress/WEB_STATUS.md`, `research/web/README.md`. No `W###` research exists yet at the time of this study.
- Reusable finding: Web Design explicitly owns real browser/device validation, themes, surfaces, states, browser-native behavior, and design-to-code fidelity.
- Implementation / application validation opportunity: Web should test the cases defined here in real browsers, native controls, forced-colors emulation, zoom/reflow, and actual page/component systems.
- Dependency / overlap: Color establishes the color-system requirements and failure conditions; Web validates the real implementation and reports browser-specific limitations back.

### Other / Cross-cutting / Future Specialist
- Evidence checked: W3C WCAG 2.2 color, non-text contrast, and focus guidance; CSS Color Adjustment Level 1; Media Queries Level 5; CSS Color Level 4.
- Reusable finding: accessibility preferences can deliberately replace author colors, and color-only semantics remain fragile even when nominal contrast is acceptable.
- Dependency / overlap: accessibility and human factors remain cross-cutting.

### Overlap decision
- Reuse / replication / extension / contradiction review / method comparison / transfer validation / project-specific study: **TRANSFER VALIDATION + EXTENSION**.
- Why: prior Color studies establish palette/contrast/gamut principles, but they do not yet prove survival under browser/user color overrides. The new Web Specialist creates a clear implementation-validation partner for this gap.

## SOURCE — browser color adjustment is an explicit part of CSS

Primary source:

- W3C CSS Color Adjustment Module Level 1: https://www.w3.org/TR/css-color-adjust-1/

The specification defines browser/user-agent behavior for preferred color schemes and forced color palettes. It explicitly separates:

- author support for light/dark schemes via `color-scheme`;
- user preference exposure via `prefers-color-scheme`;
- forced colors mode, where a limited user-chosen palette can replace author colors;
- `forced-color-adjust`, which controls whether an element participates in that forced palette.

The specification also states that browser-controlled UI such as form controls and scrollbars can respond to the used color scheme when the author declares supported schemes.

### SYNTHESIS

A production web color system does not fully control its own final pixels. The browser and user may legally and intentionally participate in color selection.

### STUDIO JUDGMENT

For web products, a color specification should distinguish at least:

1. **authoring value** — e.g. OkLCh source token;
2. **production encoded value** — e.g. sRGB/P3 CSS value;
3. **computed style** — the CSS-computed color;
4. **used/rendered behavior under user preference** — which may be changed by the user agent.

Do not approve a web color system only from design-tool screenshots or token JSON.

## SOURCE — forced colors mode can replace many author colors and remove visual effects

CSS Color Adjustment Level 1 states that, in forced colors mode, user agents can force the used colors of properties including text, backgrounds, borders, outlines, SVG fill/stroke, accent colors, and related properties to system colors.

It also specifies important side effects, including removal of `box-shadow` and `text-shadow`, and replacement of many background images unless they are URL-based images.

### SYNTHESIS

A UI that uses a colored fill, shadow, glow, or decorative surface tint as the only evidence of state or boundary can lose that evidence under forced colors mode.

### STUDIO JUDGMENT

Semantic state must survive the removal or replacement of authored color channels.

Examples of risky patterns:

- selected tab distinguished only by a blue fill;
- validation error distinguished only by red border color;
- focus indicated only by a subtle glow;
- active card distinguished only by elevated shadow plus accent tint;
- positive/negative financial state conveyed only by green/red.

Color can reinforce these states, but geometry, text, iconography, border/outline structure, position, or other redundant cues must preserve the meaning when colors are substituted.

## SOURCE — `forced-color-adjust: none` is an exception, not a default strategy

CSS Color Adjustment Level 1 defines `forced-color-adjust: none` as an opt-out from automatic forced-color adjustment and states that authors should use it only when they are themselves adjusting the element to support the user's color/contrast needs and need to override the browser's default handling.

### SYNTHESIS

Opting out is a transfer of responsibility from the browser to the product.

### STUDIO JUDGMENT

MintTap web products should not globally disable forced-colors behavior to preserve brand appearance. Any opt-out must be local, justified, and validated as an accessibility requirement or true semantic necessity.

Good candidate for possible opt-out review:
- a visualization where the exact color relationships are themselves the content and an alternate accessible representation is provided.

Poor candidate:
- a branded button, logo-adjacent accent, decorative gradient, or ordinary selected state whose authors simply prefer the original palette.

## SOURCE — system colors expose user/browser palette roles

Primary source:

- W3C CSS Color Module Level 4, System Colors: https://www.w3.org/TR/css-color-4/

CSS defines semantic system-color keywords such as `Canvas`, `CanvasText`, `ButtonFace`, `ButtonText`, `Field`, `FieldText`, `Highlight`, `HighlightText`, `SelectedItem`, `SelectedItemText`, `AccentColor`, and `AccentColorText`.

The specification describes expected foreground/background pairings intended to remain legible, while warning that arbitrary pair combinations do not guarantee a useful contrast relationship.

### SYNTHESIS

System colors are semantic roles, not a replacement palette to sample once and freeze.

### STUDIO JUDGMENT

When author styling must integrate with forced-colors or browser-native controls, use semantic pairings rather than guessing literal fallback HEX values.

This matches the broader Color-program principle that **semantic role and literal color value are different layers**.

## SOURCE — forced colors does not simply mean “high contrast”

Primary source:

- W3C Media Queries Level 5: https://www.w3.org/TR/mediaqueries-5/

`forced-colors: active` means the user agent is enforcing a limited user-selected palette. The specification explicitly notes that this palette may represent more contrast, less contrast, or another arrangement. `prefers-contrast` is a separate preference signal.

### SYNTHESIS

Forced colors, dark mode, and contrast preference are three different state spaces.

### STUDIO JUDGMENT

Do not collapse these into one binary “accessibility/high-contrast theme.” Product tokens and QA plans should treat them separately:

- light/dark color scheme preference;
- forced palette substitution;
- contrast preference where exposed;
- normal authored palette.

## SOURCE — WCAG still requires non-color redundancy and state visibility

Primary sources:

- WCAG 2.2 Understanding SC 1.4.1 Use of Color
- WCAG 2.2 Understanding SC 1.4.11 Non-text Contrast
- WCAG 2.2 Understanding SC 2.4.7 Focus Visible
- WCAG 2.2 Understanding SC 2.4.13 Focus Appearance

WCAG states that color must not be the only visual means of conveying information, action, response, or distinction. Non-text controls and required state indicators must maintain sufficient contrast against adjacent colors, and visible keyboard focus remains required.

### SYNTHESIS

Color replacement modes do not create a new accessibility principle; they expose whether the existing design already depended too heavily on color.

### STUDIO JUDGMENT

Forced-colors testing should be treated as an adversarial test of semantic resilience, not merely as a browser compatibility checkbox.

## Product decision framework

### When to use this knowledge

Use it when a product includes any of the following:

- web application or website;
- semantic status colors;
- selected/active/focus states;
- dark/light themes;
- custom form controls;
- data visualization;
- brand-critical accents inside interactive UI;
- CSS wide-gamut or OkLCh-authored tokens;
- user-configurable appearance or accessibility settings.

### When not to over-apply it

Do not redesign native mobile-only color systems around CSS forced-colors behavior. The transferable principle is user/system override resilience, but the specific mechanism is web-platform specific.

Do not force every brand color into system colors during normal rendering. System colors are for browser/user preference integration, not a universal visual style.

### Project information required before advising

- platform/browser support targets;
- whether the surface is content, control, data visualization, or brand decoration;
- semantic meaning of each state;
- light/dark/theme requirements;
- whether native controls are preserved or custom styled;
- whether exact color itself carries domain meaning;
- accessibility target and user population;
- target devices/displays;
- implementation framework and CSS architecture.

### Concrete decisions this can change

- whether a state needs a non-color cue;
- whether a custom control should remain native or be restyled;
- whether brand color should be removed from an interactive role;
- whether `color-scheme` should be declared;
- whether a component should opt out of forced colors;
- whether CSS system colors should be used for a special fallback state;
- whether wide-gamut values are appropriate for semantic roles;
- what browser/device QA matrix is required.

### Failure modes

1. **Brand lock-in:** forced-colors disabled to preserve aesthetics, reducing user control.
2. **State collapse:** selected/invalid/active states become indistinguishable after palette substitution.
3. **Shadow dependency:** boundary or focus disappears because shadows are removed.
4. **Literal fallback error:** author hardcodes a fallback HEX pair that conflicts with the user's palette.
5. **Computed-vs-used confusion:** automated inspection sees an author color in computed style while the rendered used color differs.
6. **Theme conflation:** forced colors, dark mode, and contrast preference are treated as one mode.
7. **Wide-gamut distraction:** P3/OkLCh sophistication is prioritized while semantic resilience remains weak.

## Proposed Color → Web validation matrix

The Web Design Specialist can validate the following without taking over Color's canonical conclusions:

| Case | Color question | Web validation |
| --- | --- | --- |
| light/dark theme | does semantic hierarchy survive both schemes? | real page + native controls + scrollbars + system theme |
| forced colors | do states remain understandable after palette replacement? | browser/emulation + keyboard path + native/custom controls |
| focus | does focus remain visible without glow/shadow dependence? | actual keyboard traversal in browser |
| P3/OkLCh | what is the actual CSS/rendering/fallback behavior? | browser implementation comparison on sRGB/P3-capable devices |
| semantic error/success | is hue only reinforcing, not carrying, meaning? | forms/tables/dashboard states under forced colors |
| system colors | are foreground/background roles paired correctly? | live CSS component checks |
| native controls | does author theme integrate with UA rendering? | form controls across light/dark/forced modes |

## OPEN

- This study establishes specification-level behavior, not current cross-browser implementation parity.
- No real browser forced-colors session has been executed in the Color specialist's environment.
- No actual P3-capable vs sRGB-limited device comparison has been completed.
- No complete web page has yet been transfer-tested because Web Design has not published its first `W###` study.
- `prefers-contrast` behavior and browser support need implementation-level validation before becoming a production assumption.
- Data visualization under forced colors requires a dedicated study and alternate-representation strategy.

## HANDOFFS TO OTHER SPECIALISTS

### Typography / Type
- Useful finding/context: web color overrides can change text/background colors while Type still controls hierarchy, density, rendering, and fallback.
- Canonical section: `SOURCE — browser color adjustment is an explicit part of CSS` and the project decision framework.
- Confirmation / contradiction / transfer note: confirms the need to validate Type roles in rendered browser states rather than isolated screenshots.
- Scope limit: Color does not define font metrics, line breaking, or fallback behavior.

### Color
- Useful finding/context: semantic role must remain distinct from literal token value; user-agent overrides are a production color-management condition for web products.
- Canonical section: entire C001 study.
- Confirmation / contradiction / transfer note: extends Studies 008/016/017 into user/browser override conditions.
- Scope limit: actual browser parity is still OPEN.

### Layout / Interaction
- Useful finding/context: state meaning must survive removal/replacement of fill, shadow, hue, and some decorative channels.
- Canonical section: `SOURCE — forced colors mode can replace many author colors and remove visual effects`.
- Confirmation / contradiction / transfer note: confirms Interaction's ownership of state semantics; Color should reinforce rather than define state meaning alone.
- Scope limit: this study does not specify navigation models, focus order, or recovery behavior.

### Web Design
- Useful finding/context: concrete browser validation matrix for themes, forced colors, system colors, focus, P3/OkLCh, native controls, and semantic states.
- Web application / validation consequence: W### work should include live page/component tests in actual browsers and return implementation differences to Color.
- Confirmation / contradiction / transfer note: specification-level transfer target established; no real-browser confirmation claimed yet.
- Scope limit: browser-specific support, framework behavior, and final page architecture remain Web-owned evidence.

## Status implication

C001 adds a web-transfer bridge to the Color program. It does **not** advance the overall Color domain to PASS. The next evidence step is implementation validation with the Web Design Specialist plus physical/device testing already open in `progress/COLOR_STATUS.md`.
