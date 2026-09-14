# Study 008 — Color, Luminance, Contrast, and Hierarchy

Status: FOUNDATION STUDY / practice required before PASS.

## Question

How should color support hierarchy, state, brand, and accessibility without becoming the only carrier of meaning or a substitute for composition?

## SOURCE — WCAG separates text contrast, non-text contrast, and color dependence

WCAG treats several related problems separately:

- text contrast;
- non-text contrast for component boundaries and states;
- use of color as the sole means of conveying information;
- focus visibility.

Relevant W3C sources:

- https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html
- https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html
- https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html
- https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/

The important design lesson is that contrast is not one scalar applied to an entire interface. Text, boundaries, state changes, focus indicators, charts, and decoration have different semantic roles.

## SOURCE — platform guidance treats color as hierarchical and adaptive

Apple's current guidance describes color as part of hierarchy and branding, while warning against applying a brand color so broadly that it overwhelms content or dilutes emphasis. Apple also recommends testing legibility under increased contrast and other accessibility settings, and notes that custom fonts/colors create additional responsibility for adaptation.

Sources:

- https://developer.apple.com/design/human-interface-guidelines/branding
- https://developer.apple.com/design/human-interface-guidelines/dark-mode
- https://developer.apple.com/help/app-store-connect/manage-app-accessibility/sufficient-contrast-evaluation-criteria

### Studio consequence

A premium interface does not become premium by lowering contrast indiscriminately.

Low visual noise should come from:

- fewer competing accents;
- controlled luminance steps;
- strong primary information;
- restrained secondary information;
- structural spacing and alignment;
- semantic use of color.

It should **not** come from making every label faint.

## Luminance hierarchy before hue hierarchy

A grayscale test asks whether the composition still communicates:

1. primary information;
2. supporting information;
3. boundaries and grouping;
4. active/focused state;
5. disabled/de-emphasized state.

If the entire hierarchy disappears when hue is removed, the design is over-dependent on color.

### Working studio model

Use four conceptual luminance roles before adding chroma:

- **L0 environment** — deepest or quietest field;
- **L1 work surface** — principal content plane;
- **L2 structural/secondary information** — rules, labels, inactive structure;
- **L3 primary information / focus** — highest local perceptual priority.

This is a semantic model, not a frozen token set and not an instruction to use four literal grayscale values in every project.

## Simultaneous contrast and context dependence

The same nominal color can appear different against different surroundings. This matters in UI because:

- a secondary label that looks quiet on one surface may vanish on another;
- a divider may become visually loud when adjacent surfaces are too similar;
- saturated accents can appear brighter than their measured luminance suggests;
- dark-mode surfaces can create apparent contrast shifts as local adaptation changes.

Studio rule: **evaluate color in context, not as isolated swatches.**

A palette sheet alone cannot prove interface hierarchy.

## Contrast is necessary but not sufficient

Meeting a numerical contrast threshold does not prove good hierarchy, comfort, or readability.

Examples:

- many equally high-contrast items create visual noise;
- tiny text can remain hard to read even at technically sufficient contrast;
- excessive luminance contrast in large dark interfaces can increase glare or fatigue;
- a state change may meet contrast math but still be too subtle if its area is small or the user does not know where to look.

Therefore the studio separates:

1. **conformance floor** — measurable accessibility thresholds;
2. **perceptual hierarchy** — whether attention is ordered correctly;
3. **environmental comfort** — low light, high glare, OLED/brightness conditions;
4. **semantic redundancy** — color is not the only signal.

## High-glare and low-light are different stress tests

### High glare

Risks:

- low-contrast rules disappear;
- subtle surface distinctions collapse;
- dark UI may reflect surroundings and lose local separation;
- thin text loses edge definition.

### Low light

Risks:

- large bright areas feel aggressive;
- high-chroma accents can dominate disproportionately;
- pure white text on pure black can feel harsher than a controlled neutral system;
- glare halos and visual adaptation can reduce comfort.

A single screenshot at desktop brightness is not evidence for either condition.

## Brand color discipline

Brand color should have a job.

Possible jobs:

- selected navigation state;
- primary action;
- semantic status;
- content identity;
- rare editorial/brand moment.

Weak usage:

- every icon;
- every rule;
- every heading;
- decorative gradients that compete with data;
- color used merely because the palette contains it.

The more often an accent appears, the less power it has to indicate priority.

## Practice protocol

For one information set, build four variants:

A. hue-dependent hierarchy with weak grayscale performance;
B. luminance-first hierarchy in grayscale;
C. the same hierarchy under a low-light stress treatment;
D. the same hierarchy under a simulated high-glare/contrast-reduction treatment.

Then evaluate:

- what remains primary;
- which labels disappear first;
- whether focus/state survives without hue;
- whether separators are structural or decorative;
- whether brand color can be reduced without losing identity.

## Transfer to typography

Color and type hierarchy must cooperate.

Do not use low contrast to compensate for:

- wrong font size;
- wrong weight;
- unclear grouping;
- excessive labels;
- missing whitespace.

Do not use bold weight to compensate for color that is too weak to remain legible.

## PASS requirements

Before `Color / luminance / contrast` can reach PASS:

1. create a grayscale-first hierarchy exercise;
2. measure representative text and non-text contrast cases;
3. demonstrate a state that remains understandable without hue;
4. show low-light and high-glare stress variants;
5. critique at least one palette that is attractive in swatches but fails in context;
6. apply the method to two unrelated product contexts.
