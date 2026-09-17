# L046 — Whole-Product Hierarchy & Recomposition Transfer

Status: **TRANSFER VALIDATION / PRODUCT SYSTEMS PRACTICE / RUNTIME OPEN**  
Date: 2026-09-17

## Question

When a mature-but-dense app has accumulated many valid features, how should layout practice move from local screen polishing to a coherent whole-product hierarchy that survives localization, large text and specialist data density?

## SOURCE

MintTap 1.0.29 contains very large screen-local implementations for Home, Stock Detail, Transaction Entry, Settings and History. The prior whole-app audit found that the dominant issue is not information deficit but information hierarchy and compactness.

The Product Lab source now covers one synthetic end-to-end surface spanning:

`Start → Portfolio → Holding → Add Transaction → Insights/ROC/Tax → Settings`.

Flutter accessibility guidance requires layouts to accommodate large system fonts, and WCAG 2.2 retains the reflow requirement inherited from WCAG 2.1 for web content.

Sources:
- https://docs.flutter.dev/ui/accessibility/ui-design-and-styling
- https://www.w3.org/WAI/WCAG22/Understanding/reflow.html

## SYNTHESIS

### 1. Product hierarchy precedes component polish

A component can be well spaced yet still participate in a poor product hierarchy. The meaningful layout unit for MintTap is not a card; it is a user question and its dependent evidence.

For portfolio understanding:

`scope/context → current value → total outcome → income/recovery → holdings explanation → trend → specialist ROC/tax`

This ordering prevents equal-card layouts from implying that all metrics answer the same question.

### 2. Semantic dependency defines adjacency

The following relationships deserve stronger proximity than decorative consistency:

- total performance ↔ invested basis;
- distribution amount ↔ gross/net/estimate qualifier;
- recovery/payback ↔ invested capital;
- status qualifier ↔ affected value;
- holding identity ↔ amount ↔ rate;
- save consequence ↔ primary save action.

An ad, secondary destination or unrelated control should not interrupt these pairs/groups.

### 3. Recomposition is preferable to shrink-to-fit

At narrow widths or enlarged text, horizontal financial comparison rows may transform into vertically stacked blocks while preserving semantic order.

Acceptable:

`MSTY | ₩45,200,000 | +12.4%`

→

`MSTY`
`₩45,200,000`
`+12.4%`

Not preferred:

- shrinking all text;
- clipping the label;
- removing the signed rate;
- forcing two-dimensional scrolling for ordinary reading.

### 4. Whole-app shared roles reduce spatial drift

Product-level roles should include:

- page introduction;
- primary answer block;
- metric pair/group;
- task action;
- destination action;
- state/context control;
- status notice;
- protected value block;
- monetization boundary;
- specialist detail block.

The exact Flutter components can vary, but the spatial role should remain recognizable across screens.

## PRACTICE — MintTap Product Lab

The lab now shares:

- common page and section spacing;
- semantic surface hierarchy;
- responsive metric pairs;
- responsive holding/key-value rows;
- explicit protected-value/ad-boundary regions;
- one synthetic scenario model across six workflow surfaces.

The lab deliberately removes the need for owner review at each local iteration; specialist critique occurs before owner review of the coherent candidate.

## CRITIQUE

Still unvalidated:

- actual Flutter rendering at phone/tablet sizes;
- 200% nonlinear text behavior;
- long Korean/Japanese and other localized strings;
- RTL transfer;
- keyboard/focus order on web/desktop;
- actual ad SDK reserved geometry;
- scroll-depth/task-length consequences;
- physical-device ergonomics;
- human scan/comprehension evidence.

The Product Lab journey switcher is an internal validation control, not a proposed production navigation architecture.

## RELATED DOMAIN CHECK

### Type
T024 supplies text-pressure conditions. Layout must recompose instead of forcing smaller typography.

### Color
C055 supplies independent semantic axes. Layout must keep state badges/cues attached to the correct value after reflow.

### Interaction
I042 owns task continuity, action/state/destination distinction and owner-review timing.

### Web
W055 owns runtime/browser artifact evidence and reflow/semantics transfer.

### Content
CD061 supplies the financial concept ledger and required qualifiers that layout must accommodate.

## HANDOFFS TO OTHER SPECIALISTS

### Interaction
Use the same product job map so state transitions preserve spatial/context continuity.

### Web
Validate the same reading/grouping order at narrow viewport, zoom and browser accessibility tree levels.

### Content
Do not shorten concept labels merely to protect a row layout; report layout pressure back for recomposition.

## Gate effect

L046 adds product-level systems transfer evidence. Stage 3 remains PRACTICE / NOT PASSED until executable artifact evidence and the remaining platform/human gaps are addressed.
