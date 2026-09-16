# C027 — Focus, Overlay and Semantic-State Survival

Evidence type: SOURCE / SYNTHESIS / TRANSFER VALIDATION / OPEN

## RELATED DOMAIN CHECK
C026 established six-state authored contrast and forced-color structural survival. L017/I012 own geometry/state truth; W024 is the browser integration surface; CD031 owns wording; T022 is unrelated to color repair.

## Standards baseline
WCAG 2.2 is the studio baseline. W3C SC 2.4.11 (AA) requires a keyboard-focused component not be entirely hidden by author-created content. SC 2.4.12 (AAA) requires no part to be hidden. SC 2.4.13 Focus Appearance is AAA and defines focus-indicator area/contrast requirements. Sources: https://www.w3.org/TR/WCAG22/ and https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum .

## System implication
Color conformance cannot be audited as isolated foreground/background pairs when sticky headers, sticky action bars, dialogs, toasts or other authored layers can overlap focus. The relevant matrix is `(state surface × focused control × adjacent/overlapping layer × theme × forced-colors mode)`. A passing text pair does not establish focus visibility or semantic-state survival.

## Practice matrix
For the W024 six-state surface, the next executable browser run must sample every focusable recovery action under: light, dark, forced colors; sticky top/bottom layers; transient non-modal notification; narrow viewport; and zoomed/reflowed composition. Record whether semantic identity survives when authored hue disappears and whether the focus indicator remains visually distinguishable from both its component and adjacent/overlapping surfaces.

## Critique
C026's >7:1 authored text pairs are useful but insufficient evidence for interactive accessibility. The next Color bottleneck is adjacency/occlusion, not further palette expansion or P3 work.

## Current result
**C027 SPECIFICATION PASS / EXECUTION OPEN.** No cross-browser, physical-display, CVD/low-vision observer or human salience claim is made.

## HANDOFFS TO OTHER SPECIALISTS
Layout/Interaction supplies actual overlay geometry and focus order. Web executes browser/runtime matrices. Content must keep state names/actions understandable without color. UX integration must treat focus visibility and recovery discoverability as one end-to-end risk, while human discoverability remains OPEN.
