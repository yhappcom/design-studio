# C002 — Semantic Color Roles, Token Architecture, and State-System Resilience

Status: **SOURCE STUDY + PROJECT-READINESS SYNTHESIS / implementation and multi-project transfer validation pending**

## Why this study exists

The Color program already has evidence for luminance/contrast, colorimetry, perceptual spaces, gamut, ramp authoring, and browser/user color overrides. A remaining project-readiness gap is more operational:

> How should a real app or web product turn raw palette values into semantic color decisions that remain understandable across components, states, themes, accessibility settings, and platforms?

This study is not a universal token naming standard and does not prescribe one visual style for MintTap products. It establishes a decision model for separating **literal color values**, **semantic intent**, **component use**, and **environment/theme resolution**.

## RELATED DOMAIN CHECK

### Typography / Type
- Evidence checked: `progress/TYPE_STATUS.md`, `research/type/README.md`, `research/type/009-typography-as-information-architecture.md`, and the current Type→Web transfer direction in `T001`.
- Reusable finding: text roles, font metrics, fallback, size, weight, and rendering context affect whether a nominal foreground/background color pair is actually useful.
- Replication / challenge / transfer opportunity: semantic foreground roles should later be tested with real primary/secondary/numeric/status text rather than generic sample labels.
- Dependency or overlap: Type owns typography roles and rendering; Color owns the color-role contracts applied to those roles.

### Color
- Evidence checked: `008-color-luminance-contrast-hierarchy.md`, `013-perceptual-color-spaces-difference.md`, `016-color-gamut-wide-gamut-mapping.md`, `017-perceptual-ramp-authoring.md`, and `C001-web-color-user-override-resilience.md`.
- Reusable finding: luminance hierarchy precedes decorative hue hierarchy; palette regularity does not prove accessibility; authoring values and used/rendered values can diverge; color cannot be the only semantic carrier.
- Replication / challenge / transfer opportunity: C002 converts those findings into a reusable product color-system architecture.
- Dependency or overlap: direct extension of canonical Color evidence.

### Layout / Interaction
- Evidence checked: `progress/LAYOUT_STATUS.md`, `research/interaction/015-directness-state-modes-reversibility.md`, and current Layout density/state handoffs.
- Reusable finding: state semantics must be defined before styling; selected, pending, failed, committed, focused, and disabled-like conditions are behavioral distinctions, not merely tint variants.
- Replication / challenge / transfer opportunity: Color should test whether a semantic state remains distinguishable after hue removal or token substitution, while Interaction retains ownership of what that state means.
- Dependency or overlap: Interaction owns state/action semantics; Color owns visual encoding and color-system resilience.

### Web Design
- Evidence checked: `progress/WEB_STATUS.md`, `research/web/README.md`. No substantive `W###` study was available at this synchronization point.
- Reusable finding: Web Design will be the primary real-browser integration/validation partner for tokens, themes, native controls, CSS states, forced colors, and page/component application.
- Implementation/application validation opportunity: translate the architecture below into actual CSS/design-token output and test real component/page states in future `W###` work.
- Dependency or overlap: Color defines the semantic color architecture and acceptance criteria; Web validates browser implementation and returns failures/limitations.

### Other / cross-cutting / future specialist
- Evidence checked: DTCG 2025.10 stable Format/Color/Resolver reports, Apple semantic/adaptive color guidance, Android Material 3 color-role guidance, and WCAG 2.2 color/non-text/focus guidance.
- Reusable finding: multiple mature systems separate intended use from literal values, support context-dependent color resolution, and require state meaning to survive more than hue alone.
- Dependency or overlap: accessibility, localization, and design-system implementation remain cross-cutting.

### Overlap decision
- Reuse / deliberate repetition / extension / contradiction review / method comparison / transfer validation / project-specific study: **EXTENSION + METHOD COMPARISON + PROJECT-READINESS SYNTHESIS**.
- Why: DTCG, Apple, and Material all expose role-oriented color systems, but Design Studio needs a product-agnostic method rather than copying one platform vocabulary.

---

## SOURCE — stable design-token specifications distinguish base, alias, and component layers

Primary sources:

- Design Tokens Community Group, *Design Tokens Format Module 2025.10*: https://www.designtokens.org/TR/2025.10/format/
- DTCG, *Design Tokens Color Module 2025.10*: https://www.designtokens.org/TR/2025.10/color/
- DTCG, *Design Tokens Resolver Module 2025.10*: https://www.designtokens.org/TR/2025.10/resolver/

The DTCG 2025.10 reports are stable Community Group specifications intended for implementation, but they are explicitly **not W3C Standards and are not on the W3C Standards Track**.

The Color Module describes three useful token categories:

- **Base tokens** — lowest-level literal color values;
- **Alias tokens** — references that can express semantic relationships, such as a text or background role pointing to a base palette value;
- **Component tokens** — component-specific decisions that commonly reference aliases.

The Format Module also defines aliases/references as a way for multiple named tokens to resolve to the same underlying value without duplicating the literal value.

### SYNTHESIS

A product color system becomes easier to change, theme, audit, and explain when it separates:

`literal color → semantic role → component application`

rather than wiring components directly to literal swatches everywhere.

### STUDIO JUDGMENT

Design Studio should use this **layer separation as a method**, not copy DTCG example names mechanically.

Recommended conceptual architecture:

1. **Base / primitive** — actual palette coordinates and production encodings;
2. **Semantic / role** — what the color is doing in the product;
3. **Component** — only where a reusable component genuinely needs a local contract or exception;
4. **Context resolution** — light/dark/high-contrast/brand/product/platform variations where required.

A small product may not need a large component-token layer. Token count is not maturity.

---

## SOURCE — semantic names describe intended use rather than fixed appearance

Primary sources:

- Apple UIKit semantic UI colors: https://developer.apple.com/documentation/uikit/ui-element-colors
- Apple, *Supporting Dark Mode in your interface*: https://developer.apple.com/documentation/uikit/supporting-dark-mode-in-your-interface
- Android Developers, *Material Design 3 in Compose*: https://developer.android.com/develop/ui/compose/designsystems/material3
- Android Developers, *Migrate XML themes to Material 3 in Compose*: https://developer.android.com/develop/ui/compose/designsystems/migrate-xml-theme-to-compose

Apple explicitly describes semantic colors such as label colors by **intended use** rather than fixed color values and allows them to adapt across appearance settings. Android Material 3 similarly exposes role names such as `primary`, `onPrimary`, `surface`, `onSurface`, `error`, and `outline`, and its migration guidance explicitly recommends moving away from literal hex-oriented naming toward semantic roles.

### SYNTHESIS

A semantic token should remain conceptually stable when its literal value changes across light/dark themes, increased-contrast modes, platform conventions, or a brand refresh.

### STUDIO JUDGMENT

Prefer role names that answer **“what job does this color perform?”** over names that only answer **“what does it look like?”**.

Useful role dimensions can include:

- content: primary / secondary / muted;
- surface: canvas / raised / selected / inverse;
- boundary: standard / strong / focus;
- action: primary / secondary / destructive;
- status: informative / success / caution / critical;
- data: categorical / sequential / diverging roles when a dedicated data system is designed.

These are examples, not a required universal taxonomy.

A token called `blue500` can be useful as a base token. It is weak as the final meaning of a button, error message, selected row, or financial status.

---

## SOURCE — foreground/background roles should be treated as relationships, not isolated swatches

Material 3 explicitly defines `on-*` roles for content intended to sit on corresponding surfaces or containers and warns against arbitrary cross-pairing that creates poor contrast. Apple similarly provides adaptive foreground/background semantic colors and recommends using them according to their intended roles.

Primary sources:

- Android Developers, Material 3 `ColorScheme`: https://developer.android.com/reference/kotlin/androidx/compose/material3/ColorScheme
- Apple UIKit semantic UI colors: https://developer.apple.com/documentation/uikit/ui-element-colors

### SYNTHESIS

Color roles often operate as **pair contracts**:

- foreground on a specified surface;
- border against specified adjacent surfaces;
- focus indicator against both component and environment;
- status foreground on status container;
- inverse content on inverse surface.

A foreground token cannot be validated in isolation if it is only safe on one class of surfaces.

### STUDIO JUDGMENT

For important semantic tokens, record the intended pair or adjacency contract.

Example conceptual contracts:

- `content.primary` → approved on `surface.canvas`, `surface.raised`;
- `status.critical.content` → approved on `status.critical.surface` and/or defined neutral surfaces;
- `focus.indicator` → validated against the actual component edge and outer surface;
- `action.primary.content` → bound to the approved primary action surface.

This is safer than assuming “token X is accessible” without naming what it appears against.

---

## SOURCE — theme/context resolution is a separate dimension from semantic naming

The DTCG Resolver Module 2025.10 defines modifiers and contexts for resolving token values under conditions such as light/dark themes. It also discusses orthogonality: when multiple context modifiers overwrite the same token, order can determine the result and increase complexity.

Apple supports semantic/adaptive colors that resolve differently across light/dark and increased-contrast environments.

### SYNTHESIS

Semantic role and environmental variant are different axes.

For example, `content.primary` can remain the same semantic role while its literal value changes under:

- light appearance;
- dark appearance;
- increased contrast;
- forced/user colors on the web;
- a different product brand or platform implementation.

### STUDIO JUDGMENT

Avoid names such as `darkModeBlueButtonText` when the underlying concept is actually `action.primary.content` under a dark-theme resolver.

Keep context dimensions as orthogonal as practical. If `theme`, `brand`, `accessibility`, and `platform` all independently overwrite the same token without a clear resolution model, the system becomes difficult to reason about and test.

---

## SOURCE — color consistency matters when color communicates status or interactivity

Primary source:

- Apple Human Interface Guidelines, *Color*: https://developer.apple.com/design/human-interface-guidelines/color
- Apple Human Interface Guidelines, *Branding*: https://developer.apple.com/design/human-interface-guidelines/branding

Apple recommends using color consistently when it communicates status or interactivity and warns that reusing an interaction/brand color for unrelated noninteractive styling can create confusion. Current branding guidance also recommends applying accent color judiciously rather than spreading it throughout the interface.

### SYNTHESIS

One literal hue should not be assigned incompatible semantic jobs merely because it is “the brand color.”

### STUDIO JUDGMENT

Treat **brand**, **action**, and **status** as separate semantic questions even if they occasionally resolve to related colors.

Examples of conflicts to detect:

- brand mint also used as “success,” making success indistinguishable from ordinary brand emphasis;
- primary action color also used for selected navigation and informational status, flattening hierarchy;
- red used for destructive action, loss, validation error, offline failure, and urgent alert without distinction of consequence or context;
- green/red finance semantics used with no sign, label, arrow, or value formatting.

A brand color can reinforce an action role, but the mapping must be intentional and reversible if the brand palette changes.

---

## SOURCE — semantic color cannot be the only state or information channel

Primary sources:

- WCAG 2.2 Understanding 1.4.1 Use of Color: https://www.w3.org/WAI/WCAG22/Understanding/use-of-color
- WCAG 2.2 Understanding 1.4.11 Non-text Contrast: https://www.w3.org/WAI/WCAG22/understanding/non-text-contrast.html
- WCAG 2.2 Understanding 2.4.13 Focus Appearance: https://www.w3.org/WAI/WCAG22/Understanding/focus-appearance
- Design Studio Interaction Study 015: `research/interaction/015-directness-state-modes-reversibility.md`

WCAG requires that color not be the sole visual means of conveying information/action/response/distinction. Required visual boundaries and indicators have their own contrast requirements, and focus indication has separate visibility/contrast considerations. Interaction Study 015 independently establishes that user-facing state should be modeled explicitly before styling.

### SYNTHESIS

A semantic token name such as `error`, `selected`, or `focus` does not make the implementation semantically robust.

### STUDIO JUDGMENT

Separate two classes that are often collapsed:

1. **domain/status semantics** — success, caution, critical, offline, synced, stale, profit/loss, etc.;
2. **interaction state** — hover, pressed, selected, focused, disabled, pending, committed, error-after-action, etc.

They may combine, but they are not interchangeable.

Example:

A destructive button can be:

- idle + destructive;
- hovered + destructive;
- focused + destructive;
- pressed + destructive;
- pending + destructive action;
- failed + destructive action result.

One red token cannot safely encode this entire state machine.

---

## SOURCE — color meaning can vary across locales and cultures

Primary source:

- Apple Human Interface Guidelines, *Inclusion*: https://developer.apple.com/design/human-interface-guidelines/inclusion

Apple explicitly notes that colors can carry different cultural meanings and recommends verifying that color communication remains appropriate in supported locales.

### SYNTHESIS

Semantic color conventions are partly platform/domain conventions and partly culturally learned. Familiarity in one market does not establish universality.

### STUDIO JUDGMENT

Do not define company-wide rules such as:

- success is always green;
- warning is always yellow;
- destructive is always red;
- positive finance is always green.

These may be strong candidates in many contexts, but the product domain, locale, existing conventions, and redundant cues must be checked.

---

# Proposed MintTap Color-system method

This is a reusable method, not a frozen token schema.

## Step 1 — inventory semantic jobs before choosing final hues

Identify what the product actually needs to communicate:

- surfaces and depth/grouping roles;
- content hierarchy;
- action hierarchy;
- selection/focus/interaction states;
- domain statuses;
- destructive/high-consequence actions;
- charts/data states;
- brand moments;
- environmental/theme contexts.

Do not create a 10-step ramp first and then search for jobs for every swatch.

## Step 2 — define a base palette/ramp as implementation material

Use Color Studies 013/016/017 to choose authoring space, gamut target, ramps, and mapping policy.

Base palette values are **resources**, not semantics.

## Step 3 — bind semantic roles to base values

A semantic role should answer:

- what does it mean?
- where can it appear?
- what surfaces may it pair with?
- can it carry information or only emphasis?
- what redundant cue accompanies it when meaning is critical?

## Step 4 — define context resolution

For each relevant role, determine whether it varies under:

- light/dark appearance;
- increased/high contrast;
- browser forced colors/system colors;
- platform-specific semantic colors;
- brand/product variants;
- target gamut/device class.

Do not add a variant merely because tooling permits it.

## Step 5 — add component tokens only where they buy real separation

Component tokens are useful when:

- the same semantic role must map differently for a component for a justified reason;
- implementation ownership requires a stable local contract;
- the component has multiple meaningful states that cannot be expressed cleanly with global aliases.

Avoid creating component tokens for every visual property by default.

## Step 6 — validate pair matrices, not isolated swatches

For each important role, test:

- foreground/background contrast;
- adjacent boundary contrast;
- focused/unfocused distinction;
- state distinction with hue removed;
- theme/context variants;
- actual typography roles;
- real component geometry;
- target device/browser rendering.

## Step 7 — run semantic collision review

Ask whether the same color role is carrying too many unrelated meanings.

Typical collisions:

- brand = primary action = selected = success;
- critical = loss = destructive = offline = validation error;
- muted = disabled = secondary = placeholder = unavailable;
- accent = link = focus = active state = decoration.

Some overlap can be valid, but it must be deliberate and tested.

---

# Project Readiness Test

## When should this knowledge be used?

Use it when a product has more than a few repeated colors, multiple screens/components, semantic states, light/dark variants, brand colors, cross-platform delivery, or design-to-code handoff.

It becomes especially important for:

- finance/data products;
- dense professional tools;
- apps with error/success/pending states;
- web apps with user color overrides;
- products with multiple brands/themes;
- products expected to scale to a design system.

## When should it not be over-applied?

Do not build a large token taxonomy for a one-screen prototype that has no reuse or theme requirement.

Do not replace product thinking with token architecture. A beautifully normalized token tree cannot repair unclear state semantics, weak hierarchy, or wrong interaction design.

Do not force Material, Apple, or DTCG example names into every product.

## What project inputs are required?

- target platforms and environments;
- light/dark/high-contrast requirements;
- brand palette and brand-expression priority;
- user/task criticality;
- complete list of user-facing states and statuses;
- key surfaces/components;
- typography roles;
- accessibility target;
- localization markets;
- target gamut/device assumptions;
- implementation/design-token pipeline.

## What concrete decisions can this change?

- whether brand color should be an action color;
- which semantic roles need independent tokens;
- which roles can share a literal base value;
- whether a light/dark mode needs a new value or can reuse one;
- whether text/icon/border roles need separate foreground values;
- whether a component needs local tokens;
- whether a state needs a non-color cue;
- how theme/context resolution should be structured;
- which token pairs require automated contrast checks;
- which colors must be tested in real browsers/devices.

## Alternatives and trade-offs

### Direct primitive use
- Advantage: small and simple.
- Cost: semantics are embedded in components, making theme/brand changes and audits harder.
- Use when: tiny prototypes or intentionally narrow surfaces.

### Primitive → semantic
- Advantage: strong default for most products; values can change without changing meaning.
- Cost: requires role taxonomy discipline.
- Use when: repeated UI roles exist but component-specific abstraction is still modest.

### Primitive → semantic → component
- Advantage: supports mature multi-component systems and controlled exceptions.
- Cost: more indirection, documentation, and risk of token proliferation.
- Use when: component ownership/reuse and multiple state variants justify it.

## Failure modes

1. **Palette-first taxonomy** — every swatch gets a token despite no semantic job.
2. **Literal-name lock-in** — component code depends on `blue500`, making later theme/brand changes semantically unsafe.
3. **Semantic collision** — one accent color carries brand, action, selection, success, and decoration simultaneously.
4. **Role without pair contract** — `text.secondary` is declared “accessible” without specifying surfaces.
5. **Theme duplication** — entire token trees copied for light/dark with no stable semantic layer.
6. **Context explosion** — theme, brand, platform, and accessibility modifiers overwrite the same roles unpredictably.
7. **Component-token explosion** — every component receives bespoke colors and the semantic layer stops constraining anything.
8. **Color-only state** — `selected/error/success` exists only as hue.
9. **Status/state conflation** — domain status and interaction state share one token vocabulary and become ambiguous.
10. **Platform-copying** — Material/Apple role names are adopted without checking whether the product has the same semantics.
11. **Token-as-proof fallacy** — a semantic name is treated as evidence of sufficient contrast or comprehension.

## How should the result be validated?

Minimum project validation should include:

1. token graph review: primitive → semantic → component dependencies;
2. pair/adjacency contrast matrix for representative roles;
3. grayscale or hue-removal semantic check;
4. light/dark/increased-contrast variants where supported;
5. forced-colors/system-colors validation for web products;
6. real text roles from Type;
7. real state flows from Interaction;
8. representative phone/tablet/desktop/browser/device rendering;
9. locale/cultural review when semantic hues matter;
10. failure-state and destructive-action scenarios;
11. gamut/fallback validation when using P3/OkLCh/high-chroma sources;
12. automated checks where the implementation pipeline can support them, followed by visual/contextual review.

---

## OPEN

- No complete MintTap product has yet been rebuilt using this architecture and measured against a previous direct-primitive implementation.
- Real browser/component validation awaits Web Design `W###` work.
- Dynamic/platform-generated color schemes require a separate study; this note does not approve dynamic color as a default product strategy.
- Data visualization needs its own categorical/sequential/diverging color-system study rather than reusing UI semantic tokens indiscriminately.
- Disabled/unavailable/read-only semantics need product-specific interaction analysis; this study does not assign one universal opacity or contrast rule.
- Automated token contrast auditing needs a production-tooling exercise.
- Cultural/localization implications need product-market evidence beyond general platform guidance.

## HANDOFFS TO OTHER SPECIALISTS

### Typography / Type
- Useful finding/context: semantic foreground roles must be validated with actual text roles, sizes, weights, numerals, fallback fonts, and scaling conditions.
- Canonical section: `foreground/background roles should be treated as relationships` and `Step 6 — validate pair matrices`.
- Confirmation / contradiction / transfer note: extends Type's real-rendering requirement into explicit color pair contracts.
- Scope limit: Color does not decide typographic hierarchy or font metrics.

### Color
- Useful finding/context: establish `base → semantic → optional component → context resolution` as a reusable architecture, with pair contracts and collision review.
- Canonical section: `Proposed MintTap Color-system method`.
- Confirmation / contradiction / transfer note: operationalizes Studies 008/013/016/017 and C001 for real product systems.
- Scope limit: not a frozen token naming scheme and not PASS without implementation/project evidence.

### Layout / Interaction
- Useful finding/context: interaction state and domain/status semantics should be separated before Color assigns visual roles; a single hue must not encode the whole state machine.
- Canonical section: `semantic color cannot be the only state or information channel`.
- Confirmation / contradiction / transfer note: confirms Interaction Study 015 and turns it into a Color validation contract.
- Scope limit: Color does not define state transitions, navigation, recovery, or mode behavior.

### Web Design
- Useful finding/context: token architecture to implement and challenge in real page/component systems, including theme modifiers, semantic aliases, forced-color resilience, and pair contracts.
- Web application / validation consequence: future W### work can test whether role names remain coherent across actual CSS, native controls, browser states, long content, and forced/user color conditions.
- Confirmation / contradiction / transfer note: C002 supplies a Color→Web implementation contract; no browser confirmation is claimed here.
- Scope limit: final CSS architecture, framework integration, browser support, and complete page design remain Web-owned evidence.

## Status implication

C002 closes a conceptual/project-method gap between palette science and real design-system use. It does **not** advance the Color program to PASS. The highest-value next evidence is now implementation/project transfer: actual token resolution, contrast matrices, real browser/device rendering, and semantic-state testing in representative products.