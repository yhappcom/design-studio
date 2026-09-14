# C006 — Semantic Token Transfer Across Two Materially Different Product Contexts

Status: **PRACTICE + TRANSFER VALIDATION / two-context token graph, collision critique, and pair-matrix evidence complete; rendered, browser, CVD, human-task, and production-device validation pending**

## Why this study exists

C002 established a reusable color-system architecture:

`primitive/base → semantic role → optional component role → context resolution`

but it remained a project-readiness synthesis rather than a transfer proof.

The next question is practical:

> Does the semantic-role method produce useful but materially different color architectures when applied to products with different information semantics, interaction risks, and appearance strategies?

This study tests that question with two bounded product archetypes:

- **Context F — finance analytics / portfolio-tracking surface**, light appearance, dense numerical data, positive/negative values, chart/status semantics, and brand emphasis;
- **Context O — operational record/logbook surface**, dark appearance, dense records, strong current/action/focus requirements, and caution/critical operational states.

These are **transfer specimens**, not final MintTap or LogMate product color decisions. The purpose is to validate the method, identify semantic collisions, and show that one company does not need one frozen palette or one universal semantic mapping.

Reproducibility artifacts:

- `C006-semantic-token-transfer-two-contexts.py`
- `C006-semantic-token-transfer-results.json`

---

## RELATED DOMAIN CHECK

### Typography / Type
- Evidence checked: `progress/TYPE_STATUS.md`, T003/T004 renderer evidence, and Type handoffs to Color.
- Reusable finding: nominal foreground/background contrast is not the whole typography result; actual glyph size, coverage, weight, hinting, fallback, and numeric punctuation can change practical legibility.
- Replication / challenge / transfer opportunity: use T004 numerals/punctuation in future rendered versions of Context F and O instead of generic placeholder text.
- Dependency / overlap: current pair-matrix calculations are Color evidence only. Type rendering remains a later transfer requirement.

### Color
- Evidence checked: C001, C002, C003, Studies 008/013/016/017, and C005.
- Reusable finding: semantic roles should be separated from literals; pair contracts matter; hue cannot be the only semantic channel; gamut/production encoding remains a separate layer; numeric contrast does not prove total appearance quality.
- Replication / challenge / transfer opportunity: this study directly transfer-tests C002 in two different product semantics and intentionally creates/rejects collision-heavy architectures.
- Dependency / overlap: direct extension of C002.

### Layout / Interaction
- Evidence checked: `progress/LAYOUT_STATUS.md`, especially L002 and I001.
- Reusable finding: geometry/state semantics must remain explicit before Color encodes them; current location, focus, pending, error, success and selection should not be repaired by color alone.
- Replication / challenge / transfer opportunity: Context O uses the I001 distinction between state semantics and visual encoding; Context F preserves selection/action/status as separate jobs.
- Dependency / overlap: Interaction owns what a state means. Color owns the visual role assigned to that state.

### Web Design
- Evidence checked: `progress/WEB_STATUS.md`, `research/web/README.md`.
- Reusable finding: Web Design owns actual browser/page integration, CSS token application, forced-colors/system-color behavior, and browser/device validation.
- Implementation / application validation opportunity: both token graphs can later be represented in CSS/design-token form and tested in real page/component systems.
- Dependency / overlap: no substantive `W###` evidence exists yet; no browser PASS is claimed.

### Other / Cross-cutting / Future Specialist
- Evidence checked: the WCAG/DTCG/Apple/Material evidence already synthesized in C002.
- Reusable finding: color roles should describe intended job; important foreground/background/boundary relationships need explicit contracts; color alone must not carry critical distinctions.
- Dependency / overlap: CVD simulation, localization/cultural interpretation, environmental viewing, and human-task comprehension remain open.

### Overlap decision
- Reuse / replication / extension / contradiction review / method comparison / transfer validation / project-specific study: **TRANSFER VALIDATION + FAILURE ANALYSIS**.
- Why: C002 already contains the theory. C006 tests whether the same method produces different, coherent systems under different product semantics rather than becoming a disguised universal palette.

---

# METHOD

For each context:

1. define the product's semantic color jobs before selecting final literals;
2. create an intentionally collision-heavy first mapping;
3. identify semantic ambiguity and future-maintenance risk;
4. revise to a role-separated token graph;
5. define explicit pair contracts;
6. calculate relative-luminance contrast for bounded text/boundary/focus cases;
7. identify what the numeric checks still do **not** prove;
8. compare the two contexts to see what transfers at the method level and what must remain product-specific.

The practice uses sRGB hex values as controlled implementation specimens. Hex values are not promoted to company standards.

---

# CONTEXT F — Finance Analytics / Portfolio Tracking

## Product color jobs

This context needs to distinguish at least:

- brand expression;
- primary action;
- selected/active row or filter;
- focus;
- positive/negative numerical movement;
- success/caution/critical/informational status;
- neutral content hierarchy;
- chart/data-series roles.

Finance makes semantic collision especially likely because brand, profit/loss, status and interaction colors can all compete for the same limited set of familiar hues.

## REJECTED first architecture — one teal/green family does everything

A naive system might map:

`brand → primary action → selected → success → positive P&L → focus`

into one teal/green family.

It might also map:

`negative P&L → destructive action → validation error → network failure → critical alert`

into one red family.

### Failure

This architecture is superficially consistent but semantically weak.

It creates questions the literal color cannot answer:

- Is green/teal telling the user that something is profitable, successful, selected, interactive, or merely branded?
- Is red showing financial loss, a destructive action, invalid input, or an urgent system failure?
- If the brand palette changes, should positive/negative financial semantics change too?
- If a row is selected and negative, which color owns the surface?
- If a destructive action receives focus, does one red state overwrite another?

### REJECT

Do not treat visual consistency as semantic consistency.

One hue may resolve several tokens to the same primitive temporarily, but those tokens should remain semantically separate when their jobs are not equivalent.

## Revised semantic graph

Conceptual mapping:

```text
base.brand.mint            #7CDDD3
base.action.blue           #155EEF
base.focus.blueStrong      #1D4ED8
base.success.green         #167A4B
base.caution.amber         #9A6700
base.critical.red          #B42318
base.info.blue             #175CD3
base.neutral.ink           #152028
base.neutral.secondary     #52616B
base.neutral.boundary      #7D8C97
base.neutral.canvas        #F7F9FA
base.neutral.surface       #FFFFFF
base.brand.selectedTint    #E7F8F6

brand.accent               → base.brand.mint
action.primary.surface     → base.action.blue
action.primary.content     → #FFFFFF
focus.indicator            → base.focus.blueStrong
surface.selected           → base.brand.selectedTint
content.primary            → base.neutral.ink
content.secondary          → base.neutral.secondary
boundary.strong            → base.neutral.boundary
status.success             → base.success.green
status.caution             → base.caution.amber
status.critical            → base.critical.red
status.info                → base.info.blue
```

### Important semantic separation

`data.positive` may currently resolve to the same green primitive as `status.success`, and `data.negative` may share a red primitive with a critical/destructive role, **but their semantic tokens remain separate**.

Reason:

- positive value is not the same concept as successful task completion;
- financial loss is not the same concept as destructive action or validation failure;
- future locale/domain/platform changes may require the mappings to diverge.

### Redundant encoding contract

Positive/negative financial meaning must not depend on green/red alone. Use sign, signed number formatting, arrow/direction where appropriate, labels, or chart position as redundant channels.

Selection should use structure in addition to color: row/container treatment, marker, border, typography, or position depending on the component.

Focus remains a separate interaction indicator.

---

## Context F pair matrix

Controlled numeric checks:

| Pair | Ratio | Bounded contract |
| --- | ---: | --- |
| `content.primary #152028` / `surface.canvas #F7F9FA` | 15.67:1 | text ≥ 4.5 |
| `content.secondary #52616B` / canvas | 6.06:1 | text ≥ 4.5 |
| `action.primary.content #FFFFFF` / `#155EEF` | 5.41:1 | text ≥ 4.5 |
| `content.primary` / `brand.accent #7CDDD3` | 10.35:1 | text ≥ 4.5 |
| `content.primary` / `surface.selected #E7F8F6` | 15.09:1 | text ≥ 4.5 |
| `focus.indicator #1D4ED8` / white surface | 6.70:1 | boundary ≥ 3 |
| focus / canvas | 6.35:1 | boundary ≥ 3 |
| `boundary.strong #7D8C97` / white | 3.46:1 | essential boundary ≥ 3 |
| strong boundary / canvas | 3.28:1 | essential boundary ≥ 3 |
| success / white | 5.36:1 | status text ≥ 4.5 |
| caution / white | 4.87:1 | status text ≥ 4.5 |
| critical / white | 6.57:1 | status text ≥ 4.5 |
| info / white | 5.99:1 | status text ≥ 4.5 |

All declared bounded numeric contracts pass in the controlled script.

### What this does not prove

- that all colors are optimally salient;
- that chart series remain distinguishable under CVD;
- that positive/negative interpretation is culturally or domain universally correct;
- that the selected row is clear in a real layout;
- that focus survives browser forced colors;
- that small numerals/legends work with the actual font;
- that the palette renders consistently on physical devices.

---

# CONTEXT O — Operational Record / Logbook

## Product color jobs

This context has different priorities:

- high-confidence content hierarchy on a dark working surface;
- active/current action emphasis;
- focus visibility;
- selected/current record distinction;
- success/caution/critical operational states;
- restrained brand/identity expression;
- strong legibility under dense data and potentially difficult viewing conditions.

This context is informed by the kind of operational constraints represented by the LogMate case study, but the values below are not declared LogMate product decisions. The LogMate case study explicitly warns against promoting its low-luminance appearance or any particular palette into universal Design Studio rules.

## REJECTED first architecture — accent color as universal importance

A naive dark product can easily make one pale-blue accent mean:

`brand → current row → primary action → focus → information → success → important number`

because the accent looks effective on dark surfaces.

### Failure

This produces attractive contrast while flattening semantics.

When every important thing is ice-blue:

- current location and actionable control compete;
- focus becomes indistinguishable from selected/current state;
- information status competes with primary action;
- success inherits brand meaning;
- the accent loses prioritization power through repetition.

### REJECT

High contrast does not justify assigning one accent to unrelated jobs.

## Revised semantic graph

```text
base.neutral.canvas        #0D1317
base.neutral.surface       #161D23
base.neutral.primary       #F2F4F5
base.neutral.secondary     #AAB4BC
base.neutral.boundary      #5E6D78
base.active.ice            #89B4C8
base.focus.iceBright       #C4E6F0
base.success.green         #6FAF88
base.caution.amber         #D7A44A
base.critical.red          #D9605D

surface.canvas             → base.neutral.canvas
surface.raised             → base.neutral.surface
content.primary            → base.neutral.primary
content.secondary          → base.neutral.secondary
boundary.strong            → base.neutral.boundary
action.active              → base.active.ice
action.onActive            → base.neutral.canvas
focus.indicator            → base.focus.iceBright
status.success             → base.success.green
status.caution             → base.caution.amber
status.critical            → base.critical.red
```

### Deliberate limited sharing

An operational product may deliberately let **active action** and some **selected/current structural accents** share the same cool accent family if geometry and state semantics remain distinct.

That is different from using the same token.

For example:

- primary action: filled active surface + dark content;
- selected/current record: neutral surface + accent rail/marker + structural state cue;
- focus: brighter outline/halo independent of selection;
- status: separate green/amber/red families plus icon/text/label.

This preserves visual family coherence without collapsing action, selection, focus and status into one semantic token.

---

## Context O pair matrix

| Pair | Ratio | Bounded contract |
| --- | ---: | --- |
| `content.primary #F2F4F5` / canvas `#0D1317` | 16.95:1 | text ≥ 4.5 |
| primary / raised `#161D23` | 15.42:1 | text ≥ 4.5 |
| `content.secondary #AAB4BC` / canvas | 8.88:1 | text ≥ 4.5 |
| secondary / raised | 8.07:1 | text ≥ 4.5 |
| `action.onActive #0D1317` / `action.active #89B4C8` | 8.40:1 | text ≥ 4.5 |
| `focus.indicator #C4E6F0` / canvas | 14.18:1 | boundary ≥ 3 |
| focus / raised | 12.90:1 | boundary ≥ 3 |
| `boundary.strong #5E6D78` / canvas | 3.50:1 | essential boundary ≥ 3 |
| strong boundary / raised | 3.19:1 | essential boundary ≥ 3 |
| success / raised | 6.61:1 | status text ≥ 4.5 |
| caution / raised | 7.53:1 | status text ≥ 4.5 |
| critical / raised | 4.68:1 | status text ≥ 4.5 |

All declared bounded numeric contracts pass in the controlled script.

### What this does not prove

- glare/bright-cockpit readability;
- OLED black-smear/near-black behavior;
- physical-device dark appearance;
- actual focus geometry;
- whether the high focus contrast is visually too dominant;
- CVD/human status-recognition performance;
- actual Type rendering on compact numeric rows;
- whether the single-appearance strategy is right for a specific product.

---

# TRANSFER RESULT — What actually generalizes

## CONFIRMED method-level transfer

The following C002 ideas survive both contexts:

1. **semantic job inventory before palette assignment**;
2. **primitive values separate from semantic roles**;
3. **foreground/background/boundary pair contracts**;
4. **domain status separate from interaction state**;
5. **brand separate from status by default**;
6. **focus remains its own role**;
7. **color meaning needs redundant channels when important**;
8. **component tokens are added only when a real component needs local separation**;
9. **theme/environment resolution is a separate axis from semantic naming**;
10. **same literal value may back multiple semantic tokens without making the semantics equivalent**.

## NOT confirmed as universal

The following do **not** transfer as universal rules:

- one company-wide primary action hue;
- one company-wide success/positive hue;
- one global light or dark appearance;
- one fixed number of palette steps;
- one fixed token taxonomy depth;
- one rule that brand and action must always differ;
- one rule that selection and action may always share a family;
- one rule that finance positive/negative colors should be used in non-finance products.

This is the expected outcome. The same **method** should produce different systems when the product problem is different.

---

# FAILURE → REVISION SUMMARY

## Failure A — semantic overloading

Initial shortcut:

`one strong hue = everything important`

Revision:

separate brand, action, focus, selection, domain status and data meaning into different semantic roles even when some resolve to related primitives.

## Failure B — literal-first architecture

Initial shortcut:

create palette steps first, then assign jobs until all swatches are used.

Revision:

inventory semantic jobs first; palette values exist only to serve real jobs.

## Failure C — treating numeric contrast as final approval

Initial shortcut:

all measured pairs pass, therefore the system is good.

Revision:

numeric pair checks are only one gate. Human comprehension, salience, Type rendering, geometry, CVD, forced colors, device/environment and product semantics remain independent tests.

## Failure D — equating alias equality with semantic equality

Initial shortcut:

if `status.success` and `data.positive` currently point to the same green, merge them into one token.

Revision:

retain separate semantic roles when the jobs differ, even if their current primitive resolution matches. This keeps future product/domain/platform changes reversible.

---

# PROJECT READINESS TEST

## When should this knowledge be used?

Use this method when a product has repeated color decisions, multiple semantic states, brand color, data/status meaning, accessibility requirements, more than one component family, or multiple theme/platform contexts.

## When should it not be over-applied?

A tiny static surface with only neutral text and one simple action may not need a large token hierarchy. Token count is not maturity.

Do not create semantic roles for hypothetical future states with no product requirement.

## What project information is required first?

At minimum:

- core tasks and failure costs;
- primary information/data types;
- interaction states;
- domain status semantics;
- brand role;
- appearance/theme strategy;
- target platforms/devices;
- viewing environment;
- accessibility/localization requirements;
- whether charts/data visualization are involved.

## What concrete decisions can change?

- whether brand color should be used for primary action;
- whether positive/negative data shares status colors;
- how selected/current/focus differ;
- whether action/state tokens share primitives but remain separate aliases;
- which foreground/background pairs are legally/operationally allowed;
- whether a dark or light context needs different semantic resolutions;
- whether component-specific tokens are justified.

## Trade-offs

More semantic separation improves auditability and future adaptability but increases naming/system complexity.

More literal reuse can create visual coherence but may increase semantic collision.

More distinct colors can improve semantic separation but can increase visual density and reduce brand/accent power.

## Failure modes

- brand/action/success collision;
- data status and interaction state collision;
- focus hidden inside selection;
- literal token names leaking into component semantics;
- pair contracts valid in one theme but not another;
- inaccessible or misleading status under hue loss/CVD;
- too many strong colors increasing perceived visual density;
- component overrides bypassing the semantic layer;
- platform/forced-color substitution breaking meaning.

## Validation plan

Next evidence should include:

1. render both contexts with realistic Type roles;
2. run grayscale and CVD-oriented critique;
3. hold geometry constant while reducing/increasing chroma to evaluate visual-density transfer with L002-like conditions;
4. test selected/current/focus/status combinations rather than isolated swatches;
5. test light/dark/context resolution in actual component surfaces;
6. when Web evidence exists, validate CSS tokens, forced colors, system colors and browser rendering;
7. later validate on physical devices and representative viewing environments.

---

# HANDOFFS TO OTHER SPECIALISTS

### Typography / Type
- Useful finding/context: both contexts now provide explicit primary/secondary/numeric/status foreground roles and bounded surfaces for real glyph-rendering transfer.
- Canonical section: Context F/O pair matrices and validation plan.
- Confirmation / contradiction / transfer note: C006 does not change T003/T004 findings; it supplies realistic color environments in which those findings can be transfer-tested.
- Scope limit: Color does not determine font metrics, hinting, numeral design, or fallback strategy.

### Color
- Useful finding/context: C002's semantic architecture survives two materially different contexts, but the actual mappings differ substantially.
- Canonical section: Transfer Result and Failure→Revision Summary.
- Confirmation / contradiction / transfer note: confirms method transfer; rejects any inference that C002 defines a universal palette or one fixed company-wide token mapping.
- Scope limit: no rendered/human/device PASS.

### Layout / Interaction
- Useful finding/context: focus, selection/current, action and domain status remain separate roles. Color should not redefine their semantics.
- Canonical section: both revised semantic graphs.
- Confirmation / contradiction / transfer note: consistent with I001 state-first logic and L002's request for Color transfer with geometry held constant.
- Scope limit: no new state machine or layout decision is asserted by Color.

### Web Design
- Useful finding/context: two explicit semantic graphs and pair contracts are ready for future implementation validation.
- Canonical section: Context F/O graphs and pair matrices.
- Web application / validation consequence: represent roles as CSS/design tokens; test theme resolution, forced colors, system colors, focus, native/custom controls, and browser rendering without collapsing semantic aliases.
- Confirmation / contradiction / transfer note: Web should return browser/framework limitations rather than silently changing semantic meaning.
- Scope limit: no substantive W### evidence exists yet.

---

# OPEN

- rendered light/dark specimen for both contexts;
- realistic Type transfer using T004/T005 evidence;
- CVD/grayscale critique with redundant cues;
- L002-style fixed-geometry salience/density experiment;
- selected + focused + status combination stress cases;
- browser forced-colors/system-color implementation;
- physical-device/environmental validation;
- real project transfer before any product-specific recommendation;
- human comprehension/performance evidence.

## Status implication

C002 semantic color/token architecture advances from **IN STUDY / PROJECT-READINESS SYNTHESIS** to **PRACTICE / TRANSFER VALIDATION**.

This does not justify PASS. The next high-value Color block is a fixed-geometry salience/density transfer or rendered/CVD practice using the two-context architecture above.