# C020 — Multi-surface Semantic Token System

Classification: **SYSTEMS PRACTICE + CROSS-DOMAIN TRANSFER CONTRACT**

## RELATED DOMAIN CHECK
- Type T021 is drawing-invalid; this system assumes current product text rendering and does not use hue to repair character ambiguity.
- Layout/Interaction L011 defines one truth-state contract across phone, tablet/EFB and desktop/web.
- Web W019 closes Stage 2 but browser theme/forced-color transfer remains a later executable gate.
- Content CD019 defines structured lifecycle/message truth; Color maps to that truth and does not redefine it.
- UX remains cross-cutting; color is a redundant signal, not the only carrier.

## Fixed substrate
Professional record workflow: `lookup → inspect → compare → correct → confirm/recover` across phone, tablet/EFB and desktop/web.

Truth states: neutral, informational, edited, pending, confirmed, known failure, outcome-unknown, offline/stale, conflict, disabled, selected/focus.

## Token graph
`meaning → semantic role → interaction state → theme mode → output/gamut mapping → surface instance`

Canonical semantic roles are independent of component names:
- `surface.base`, `surface.raised`, `surface.sunken`
- `text.primary`, `text.secondary`, `text.disabled`
- `border.default`, `border.strong`
- `state.info`, `state.pending`, `state.success`, `state.warning`, `state.critical`, `state.unknown`, `state.offline`, `state.conflict`
- `action.primary`, `action.destructive`, `focus.indicator`, `selection.indicator`

Component tokens may alias these roles but may not invent new lifecycle meaning.

## Three-surface invariants
Phone, tablet/EFB and desktop/web MUST preserve the semantic role and non-color carrier for the same truth state. They MAY vary surface area, density, emphasis distribution and data-visualization quantity.

| State | Color role | Required non-color carrier | Cross-surface invariant |
| --- | --- | --- | --- |
| pending | state.pending | explicit status text/progress semantics | action not represented as complete |
| confirmed | state.success | confirmation text/icon semantics | completion certainty unchanged |
| known failure | state.critical | failure + safe recovery action | retry only when Interaction says safe |
| outcome unknown | state.unknown | verification instruction | never collapse into known failure |
| offline/stale | state.offline | stale/offline label + freshness context | recency uncertainty retained |
| conflict | state.conflict | resolution-required message/action | no automatic winner implied |
| focus | focus.indicator | focus geometry/outline | survives hue removal/forced colors |

## Theme architecture
Light and dark are separately authored mappings from the same semantic roles. Dark mode is not an RGB inversion. Pair contracts are role-based: foreground/background pair identity is preserved even when concrete values differ.

The initial production baseline remains sRGB. A wide-gamut candidate may enhance brand/data expression only when:
1. semantic identity is unchanged;
2. an explicit sRGB fallback exists;
3. clipping/fallback does not merge status or data categories;
4. the wide-gamut value is not required for accessibility.

No wide-gamut value is promoted in C020 because actual browser/device reproduction has not yet been transferred.

## Status palette vs data palette
Status colors are reserved for lifecycle/action meaning. Data-series colors use a separate namespace (`data.series.*`, `data.sequential.*`, `data.diverging.*`). A chart series must not inherit `state.critical` merely because both appear red-like. Selection of data marks requires a redundant mark/stroke/label mechanism so status semantics remain unambiguous.

## Forced-colors / high-contrast survival
C011 evidence is reused: semantic meaning must survive user-agent color remapping. C020 therefore requires text/state semantics, system-color-compatible focus geometry and no color-only selection or warning. Exact browser transfer belongs to Web.

## Three-form-factor stress conclusions
1. Phone compression may reduce simultaneous status detail but may not remove consequence/recovery truth.
2. Tablet/EFB may expose comparison panes concurrently; status roles remain identical to phone.
3. Desktop/web may add dense tables and data visualization; data palette must remain separate from lifecycle state palette.
4. Color cannot be used to compensate for Type T021 ambiguity or shortened Content strings.

## Gate result
**C020 SYSTEM ARCHITECTURE: PASS FOR STATIC CONTRACT / Stage 3 remains PRACTICE.**

Passed: semantic graph, three-surface invariant mapping, theme/output separation, status/data namespace separation, adverse-color survival contract.

Open: concrete light/dark value authorship and pair matrix, bounded P3 candidate, actual CSS forced-colors transfer, calibrated physical display, CVD/low-vision observer evidence, human salience/task evidence.

## HANDOFFS TO OTHER SPECIALISTS
- Layout/Interaction: consume the state/non-color carrier matrix in L012/I007.
- Web: implement role aliases rather than component-specific meaning; later test light/dark/forced-colors.
- Content: verbal state identity is mandatory when hue is unavailable.
- Type: color does not repair glyph identity.

## Evidence boundary
This is a system architecture and cross-domain contract, not physical-display, human-perception, browser-parity or WCAG-conformance proof.