# W021 — Integrated runtime specimen static audit

Classification: **IMPLEMENTATION + CRITIQUE / PRE-EXECUTION**

## RELATED DOMAIN CHECK
- Type: current product/system typography is used; custom T021 A/B remains drawing-invalid.
- Color: C022 exact calculations show all bounded C021 text/state pairs above 7:1; contextual focus/non-text rendering remains a browser gate.
- Layout/Interaction: specimen implements one semantic task model with desktop/tablet/phone recomposition and outcome-unknown retry suppression.
- Content: typed operational literals use bidi isolation and the specimen contains expansion + RTL stress controls.

## Implemented specimen
`W021-integrated-runtime-specimen.html` is now an actual integrated artifact rather than a contract only. It contains:
- desktop three-region composition, tablet two-region recomposition, phone stacked composition;
- meaningful source order `nav → record list → record detail`;
- `role=status` + `aria-live=polite` state exposure;
- outcome-unknown state with blind `Save again` disabled until verification;
- 24px minimum native action boxes plus visible focus outline;
- C021 light/dark state aliases;
- forced-colors override using system colors;
- reduced-motion equivalence;
- pseudo-expansion stress;
- RTL wrapper stress with LTR isolated flight/airport literals;
- sticky edit action to make focus-obscuration a measurable runtime condition.

## Static critique
### KEEP
The specimen preserves the critical semantic distinction: outcome-unknown offers `Check record`; blind retry is unavailable. Responsive CSS changes region visibility/composition without changing the state/action contract. RTL changes direction but operational literals remain explicitly isolated LTR.

### OPEN / runtime required
Static inspection cannot prove:
1. actual tab sequence/focus visibility;
2. sticky focus obscuration geometry;
3. computed forced-colors behavior;
4. actual 200% browser zoom/reflow;
5. rendered pseudo-expansion overflow;
6. accessibility-tree/live-region behavior;
7. browser bidi rendering;
8. real route/history/network behavior.

### Known limitation
At tablet width the record list is hidden, so direct access to alternate records depends on navigation/task design not represented by this bounded specimen. This is acceptable for the current state-transfer proof but is **not** evidence that the full product information architecture is complete.

## Gate result
**W021 implementation exists; integrated browser execution remains OPEN.** This is a meaningful advance from execution contract to executable specimen, but no Chromium/cross-browser/AT PASS is claimed without a run.

## UX integration check
The end-to-end invariant is now executable: identify record → observe certainty → obtain safe action → verify → regain confirmed state. Color reinforces certainty; content names it; layout keeps state/action adjacent; responsive rules may recompose but not mutate it. Type remains a flexible current-product input.

## HANDOFFS TO OTHER SPECIALISTS
- Layout/Interaction: browser run must verify recomposition and sticky focus geometry.
- Color: browser run must verify computed focus/state behavior and forced colors.
- Content: browser run must verify expansion/bidi/status transfer.
- Type: no custom-font transfer until route comparison/drawing decision closes.