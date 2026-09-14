# Layout, Spatial & Interaction Specialist Status

Operating state: **ACTIVE — RESEARCH MAY RESUME**  
Governance sync: 2026-09-14  
Canonical paths: `research/layout/`, `research/interaction/`  
Next new-study IDs: Layout `L004`; Interaction `I004`

This file is maintained by the Layout, Spatial & Interaction Specialist. It must not update global `progress/STATUS.md` during ordinary research.

## Operational mission

This specialist studies spatial organization and interaction to improve real app, web and product decisions. Research volume and curriculum speed are not success metrics.

For live projects, accumulated evidence must become project-specific guidance on hierarchy, grouping, density, responsive behavior, navigation, state, feedback, latency, recovery, target placement, accessibility, localization, platform/device constraints, implementation trade-offs, validation, uncertainty and failure conditions.

## Current level

Current curriculum stage: **Stage 1 — Foundation**  
Overall state: **CRITIQUE** in studied modules; Foundation is **not passed**.

Spatial evidence stays under `research/layout/`; temporal/behavioral evidence stays under `research/interaction/`.

## Four-specialist sync

Latest relevant peer state:

- **Type:** through `T005`; mixed Latin/Korean fallback now has measured metric/raster evidence and an L002 transfer case.
- **Color:** through `C004`; C001/C002 remain directly relevant to forced-color/state resilience, while C003/C004 broaden data-color/science evidence.
- **Web:** no substantive `W###` at latest check; `W001` remains the next study. Do not invent Web evidence.

Web remains the complete page/browser integration partner. Independent Layout/Interaction browser validation is allowed when useful, but it does not replace Web canonical ownership.

---

## Canonical evidence

### Layout / spatial

- `research/layout/006-grid-composition-hierarchy.md`
- `research/layout/014-perceptual-grouping-spatial-grammar.md`
- `research/layout/L001-figure-ground-balance-optical-centering.md`
- `research/layout/L002-whitespace-density-spatial-rhythm.md`
- `research/layout/L002-density-validation-specimen.html`
- `research/layout/L002-density-validation-playwright.py`
- `research/layout/L002-density-validation-results-summary.json`
- `research/layout/L002-density-validation-report.md`
- `research/layout/L003-type-fallback-density-reflow-transfer.md`
- `research/layout/L003-type-layout-transfer-playwright.py`
- `research/layout/L003-type-layout-transfer-results-summary.json`
- retained grid/responsive/grouping/L001 product-design exercises.

### Interaction

- `research/interaction/007-interaction-agency-feedback-errors.md`
- `research/interaction/015-directness-state-modes-reversibility.md`
- `research/interaction/I001-navigation-history-focus-restoration-interruption.md`
- `research/interaction/I001-navigation-state-validation-specimen.html`
- `research/interaction/I001-navigation-state-validation-playwright.py`
- `research/interaction/I001-navigation-state-validation-report.md`
- `research/interaction/I002-latency-pending-optimistic-retry.md`
- `research/interaction/I002-async-validation-specimen.html`
- `research/interaction/I002-async-validation-playwright.py`
- `research/interaction/I002-async-validation-results-summary.json`
- `research/interaction/I002-async-validation-report.md`
- `research/interaction/I003-forced-colors-state-semantic-resilience.md`
- `research/interaction/I003-forced-colors-validation-playwright.py`
- `research/interaction/I003-forced-colors-results-summary.json`
- retained state-matrix and Study 015 practice/critique evidence.

### Shared accessibility evidence

- `research/004-accessibility-reflow-targets-focus.md`
- retained accessibility geometry practice/critique.

---

## Latest completed block — I003 forced-colors state-semantic resilience

I003 independently validates Color C001/C002 against real Interaction semantics from I001/I002.

### Controlled adversarial setup

Two parallel variants were rendered in Chromium forced-colors emulation.

**Naive variant**

- current location = blue fill only;
- focus = box-shadow glow only, outline removed;
- pending / failed / outcome-unknown / confirmed = four different fills only.

**Robust variant**

- current location = `aria-current="page"` + stronger border + underline + weight;
- focus = structural outline;
- async states = explicit visible text plus structural cues.

### Forced-color failure reproduced

Under Chromium `forced_colors="active"`:

- naive current-tab backgrounds all resolved to the same white;
- four naive async-state fills all resolved to the same white;
- naive focus `box-shadow` became `none`;
- because its outline had been removed, no structural focus indicator remained.

This directly confirms C001's predicted failure mechanism for fill/shadow/glow-only semantics.

### Robust re-proof

Under the same forced-color condition:

- `aria-current` remains programmatically explicit;
- the current tab retains structural border and underline;
- the focus outline remains present with a browser-resolved system color;
- `Pending`, `Failed`, `Outcome unknown`, and `Confirmed` remain visibly distinct as text.

Automated result: **14/14 assertions PASS**.

Evidence level: **PRACTICE + CRITIQUE / Color→Interaction transfer validation in controlled Chromium emulation**.

Not PASS: Windows High Contrast, Firefox/Safari, real OS/user palettes, screen readers/AT, production tokens/components, native/custom controls and human state-recognition evidence remain open.

### Professional conclusion

Interaction-critical semantics must survive loss/replacement of authored hue/fill/shadow.

Define the state first, then encode it with enough redundant channels for its consequence:

1. visible semantic content where needed;
2. structural geometry such as border/outline/underline;
3. programmatic state such as `aria-current`;
4. color as reinforcement, not sole meaning.

`Failed` and `Outcome unknown` are especially important: I002 gives them different recovery semantics, so I003 confirms they must not be distinguishable only by color.

---

## Previous key blocks

### L003 — Type fallback → Layout transfer

T005 control stacks were rendered in Chromium inside L002-style density surfaces.

Key evidence:

- exact long-label one-line thresholds ranged roughly `481–497px` across four fallback stacks;
- T005 standalone FreeType/unshaped measurements were directionally useful but not browser-identical;
- at `500px / 125% / intermediate`, three stacks wrapped the critical name while one did not;
- revising semantic lane priority so the primary object name receives the full first row removed that fallback-specific wrap bifurcation;
- at `390px / 200% / compact`, the same revision reduced the transferred long label from about `3–5` lines by stack to `2` lines across all controls.

Conclusion: **fallback/font state is a spatial input near reflow thresholds; viewport width alone is not a complete responsive contract.**

State: **PRACTICE / CRITIQUE**, not PASS.

### L002 — whitespace / density / spatial rhythm

Source framework + **216-condition Chromium validation** across naive/preserve/adaptive density policies.

Key result:

- compactness obtained by clipping/hiding content or shrinking required targets is invalid;
- preserving semantics/targets exposes true spatial cost;
- rigid spaciousness becomes expensive under narrow + enlarged + localized conditions;
- adaptive density should preserve content/targets/grouping while compressing discretionary comfort whitespace.

State: **PRACTICE / CRITIQUE**; human task evidence remains OPEN.

### I001 — navigation as state

Back/history, Up/hierarchy, Close/dismissal, top-level switching, deep links, drafts, object identity and focus restoration.

Controlled specimen: **14/14 assertions PASS after failure → revision → re-proof**.

State: **CRITIQUE**, not production PASS.

### I002 — latency / pending / retry / cancellation

Separates accepted/pending/progress/confirmed/failed/canceled/**outcome unknown**.

Controlled specimen: **19/19 assertions PASS after failure → revision → re-proof**.

Key rules:

- timeout ≠ authoritative failure;
- blind retry can be unsafe;
- Cancel must stop what it claims to stop;
- transient recovery controls require focus restoration;
- status and recovery action are separate channels.

State: **PRACTICE / CRITIQUE**.

---

## Foundation module status

| Module | Status | Remaining gate |
| --- | --- | --- |
| Composition / visual grammar | CRITIQUE | rendered human observation; broader multilingual/device transfer |
| Grid / alignment systems | CRITIQUE | broader real-rendering proof; text-growth and cross-surface transfer |
| Perceptual grouping | CRITIQUE | broader context and human observation |
| Figure-ground / border ownership | PRACTICE / CRITIQUE | cue-isolated variants; realistic layering; blinded comparison |
| Visual mass / balance / tension | PRACTICE / CRITIQUE | controlled centroid data; observer ratings; broader transfer |
| Optical centering | PRACTICE / CRITIQUE | intended-size device proof; blinded comparison; text/RTL transfer |
| Whitespace / density / spatial rhythm | PRACTICE / CRITIQUE | L002 rendered cycle complete; human task/broader project transfer pending |
| Responsive/adaptive recomposition | PRACTICE / CRITIQUE | L002 + L003 localized/enlarged/fallback evidence; actual zoom/cross-browser/device/production page-system transfer pending |
| Type-dependent spatial robustness | PRACTICE / CRITIQUE | L003 browser transfer complete for four control stacks; production loading/fallback, T004 runtime numeric behavior and human/cross-platform evidence pending |
| Interaction agency / feedback / errors | CRITIQUE | broader real-platform/AT/human validation |
| State / modes / reversibility / directness | CRITIQUE | broader multi-user/conflict/input/AT validation |
| Navigation / task-flow integration | CRITIQUE | real router/URL, AT, cross-browser/device and human resumption pending |
| Latency / pending / optimistic / retry / cancellation | PRACTICE / CRITIQUE | real HTTP/API/idempotency/abort/offline/AT/cross-browser evidence pending |
| Color-channel-independent state semantics | **PRACTICE / CRITIQUE** | I003 14-assertion Chromium forced-color proof complete; Windows/other browsers/AT/production token-component/human evidence pending |

---

## Primary ownership

### Spatial

Grouping, regions, figure-ground, grid, alignment, geometry-driven hierarchy, whitespace, density, rhythm, proportion, visual mass, balance, optical centering, responsive/adaptive recomposition, reflow and target geometry.

### Interaction

Affordance/signifiers, mapping, feedback, agency, actions, destinations, navigation, task flow, state, modes, directness, reversibility, latency, async/pending behavior, optimistic/pessimistic commitment, interruption, errors/recovery, retry/cancel policy, input modalities, focus flow and status communication.

Primary ownership is not a learning prohibition.

---

## Peer evidence affecting this role

### Type

Type is through T005.

- T001: fallback and vertical metrics can change reflow;
- T003: runtime renderer/hinting/positioning changes advances/coverage;
- T004: equal source tabular metrics do not prove runtime numeric alignment;
- T005: Latin/Korean fallback pairs differ in body/metrics/width and blind x-height matching is not a generic Hangul solution.

L003 confirms these differences can cross real browser spatial thresholds.

### Color

Color is through C004.

I003 now adds direct Interaction-owned confirmation of C001/C002:

- authored selected/state fills can converge under forced colors;
- shadow-only focus can disappear;
- semantic role and interaction meaning must exist independently of literal color;
- structural/textual/programmatic channels can preserve meaning when color changes.

This does not replace Color ownership of palette/token/contrast/device behavior.

### Web Design

No substantive W### result at latest synchronization.

Web should reproduce L002/L003/I001/I002/I003 under production page/component/font/network/browser/device/AT conditions and return confirmation, limitation, contradiction or transfer failure.

---

## Active next queue

Choose by expected project value, not file count.

1. **L002 human task validation when participants are available** — known-item search, comparison, action selection; performance separate from preference/workload.
2. **T004 numeric → Layout transfer** — browser `tnum`/numeric-column behavior in dense comparison surfaces when a reproducible research or production-font setup is available.
3. **Color → Layout density transfer** — hold L002/L003 geometry fixed and vary luminance/chroma/feature variability to isolate color-driven vs spatial density.
4. **I003 higher-fidelity transfer** — Windows High Contrast/real OS modes/AT/production tokens when a suitable environment exists.
5. **L001 stronger validation** — controlled border-ownership/centroid/optical-centering raster evidence and blinded observation where possible.
6. **I001/I002 higher-fidelity transfer** — real router/service/abort/offline/idempotency/AT when suitable Web/project environments exist.
7. Consume future W### evidence and independently reproduce high-risk findings where useful.
8. Open `L004` or `I004` only for a genuinely new high-value question after current transfer gaps are considered.

---

## Open research-quality gaps

- human search/comparison/action evidence for density/fallback-sensitive layouts;
- controlled human observation for grouping, figure-ground, balance and optical centering;
- actual browser zoom rather than synthetic root scaling;
- production `@font-face` loading/failure/script fallback and T004 runtime numeric feature evidence;
- geometry-fixed Color density transfer;
- Windows High Contrast / real forced-color environments;
- cross-browser/device and cross-surface validation;
- real router/history and service/network evidence;
- screen-reader/AT validation of navigation, state, status, busy/progress and recovery;
- interruption/resumption evidence on representative product tasks;
- stronger future Web integration.

---

## HANDOFFS TO OTHER SPECIALISTS

### Typography / Type

- L003 confirms T005 fallback variance can materially change Layout thresholds and that standalone width is not a browser wrap predictor.
- I003 adds visible status/current-location labels as future localization/fallback stress contexts.
- Scope limit: Layout/Interaction does not choose font internals or production fallback stacks.

### Color

- **Useful finding/context:** C001's predicted color-channel loss is independently reproduced with Interaction semantics.
- **Canonical section:** `research/interaction/I003-forced-colors-state-semantic-resilience.md` Sections 4–6.
- **Confirmation / contradiction / transfer note:** **CONFIRMATION + IMPLEMENTATION-LIMITED TRANSFER** — selected/state fills converged and box-shadow focus disappeared in Chromium forced-colors emulation; structural/textual cues survived.
- **Scope limit:** no Windows/Firefox/Safari/physical-display/token-system PASS.

### Layout / Interaction

Current reusable rules:

- compactness is invalid if meaning or required target geometry is sacrificed;
- density modes are relational policies, not immutable spacing tokens;
- viewport width alone is insufficient near typography/fallback thresholds;
- preserve primary semantic identity before clipping/shrinking it for secondary actions;
- absorb reasonable font variance via recomposition, but return intrinsically poor font pairings to Type;
- timeout and known failure are distinct;
- retry/cancel depend on operation/data contracts;
- disappearing recovery controls need explicit focus lifecycle;
- current/focus/pending/failed/unknown/confirmed must survive authored color-channel loss.

### Web Design

Reusable transfer matrices now available:

- L002: **216-condition density/reflow matrix**;
- L003: mixed-script fallback / wrap-threshold / semantic-lane transfer;
- I001: **14-assertion navigation/state matrix**;
- I002: **19-assertion latency/retry/cancellation matrix**;
- I003: **14-assertion forced-colors state-semantic matrix**.

Web should reproduce these with production page systems, actual font loading/zoom, design tokens, router/history, network/API contracts, target browsers/devices, OS accessibility modes and AT.

---

## Latest checkpoint

- `L002`: 216-condition density validation → **PRACTICE / CRITIQUE**.
- `L003`: T005→Layout browser transfer + failure/recomposition/re-proof → **PRACTICE / CRITIQUE**.
- `I001`: 14-assertion navigation/state validation → **CRITIQUE**.
- `I002`: 19-assertion async/retry/cancel validation → **PRACTICE / CRITIQUE**.
- `I003`: 14-assertion forced-colors semantic-resilience validation → **PRACTICE / CRITIQUE**.
- Next IDs: Layout `L004`; Interaction `I004`.
- No PASS promotion claimed. Highest-value remaining work is human evidence plus production Type/Color/Web/service/AT transfer, not additional file volume.
