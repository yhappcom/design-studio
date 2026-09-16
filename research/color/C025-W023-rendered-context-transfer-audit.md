# C025 — W023 rendered-context color transfer audit

Classification: **TRANSFER VALIDATION + CALCULATION CHECK + CONTRADICTION REVIEW**

## Purpose
Consume actual W023 Chromium computed evidence instead of expanding palette theory.

## RELATED DOMAIN CHECK
- Type T022: character ambiguity remains non-color.
- Layout L015: focus/adjoining surfaces are contextual geometry, not token-only facts.
- Interaction I010: certainty state is behavioral truth; Color only encodes it.
- Web W023: supplies actual dark/forced-colors computed values.
- Content CD029: textual state identity must survive hue loss.
- UX: visual salience calculations are not human noticeability evidence.

## SOURCE baseline
WCAG 2.2 remains the current W3C conformance baseline used by this studio. SC 2.4.11 requires focused components not be entirely obscured by author-created content; SC 1.4.11 governs non-text contrast, while 2.4.13 Focus Appearance is AAA. W3C Technique C40 also cautions against relying on box-shadow alone in forced-colors contexts and describes outline-based two-color focus as one sufficient technique, not a mandatory implementation.

## W023 evidence consumed
Dark phone execution returned:
- canvas/background `rgb(16,20,24)`;
- dark button background `rgb(37,43,49)` from the authored rule;
- focus outline `rgb(140,200,255)`.

Forced-colors execution returned unknown-state:
- text `rgb(0,0,0)`;
- background `rgb(255,255,255)`;
- border `rgb(0,0,0)`.

## Independent contrast calculation
Using WCAG 2.x sRGB relative-luminance math:
- dark focus outline `140,200,255` vs root background `16,20,24`: **10.41:1**;
- same outline vs dark button background `37,43,49`: **8.05:1**;
- forced-colors black vs white: **21:1**.

These calculations establish strong contrast for the measured color pairs. They do not prove every pixel of every focus indicator/component context, because actual adjacency/overlap geometry can vary.

## Semantic collision result
Forced colors deliberately collapses confirmed/failure/unknown/offline authored hues to system text/background. The specimen still retains textual state identity and border structure. This is the intended resilience model: **state truth survives color loss**. Color is reinforcement, not sole semantics.

## Gate interpretation
C024's blanket statement that browser transfer was missing is now partially outdated. Chromium dark + forced-colors transfer exists for the W021 bounded specimen. Remaining Stage 3 gaps are:
1. component-by-component contextual non-text/focus geometry beyond the sampled controls;
2. all semantic states rendered, not only unknown plus transition-confirmed text;
3. cross-browser/platform forced-colors/high-contrast behavior;
4. calibrated/physical display and observer evidence;
5. human salience/recognition evidence.

P3 remains deferred; W023 provides no reason to widen gamut before these sRGB transfer gaps close.

## HANDOFFS TO OTHER SPECIALISTS
- Web: preserve outline-based focus resilience; do not interpret the calculations as global conformance.
- Layout: provide exact adjacency/overlap geometry for future contextual component matrices.
- Content: textual state identity is proven structurally necessary under forced-color hue collapse.
- Interaction: semantic state distinctions remain independent of color.

## Verdict
**C025 PARTIAL TRANSFER PASS for measured Chromium dark/forced-colors contexts. Stage 3 remains PRACTICE.**