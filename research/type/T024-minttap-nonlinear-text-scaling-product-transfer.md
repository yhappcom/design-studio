# T024 — MintTap Nonlinear Text Scaling Product Transfer

Status: **TRANSFER VALIDATION / PRODUCT SOURCE + OFFICIAL PLATFORM GUIDANCE / RUNTIME OPEN**  
Date: 2026-09-17  
Stage relevance: Stage 2 practice; **does not alter T021 drawing gate**

## Question

How should a dense financial Flutter product preserve typographic hierarchy when system text scaling is large or nonlinear, without hiding layout defects by globally suppressing user scaling?

## SOURCE

### Flutter platform guidance

Flutter's accessibility guidance states that Android and iOS system font settings are respected by Flutter text widgets and that layouts should leave enough room for increased font sizes. Flutter recommends testing small-screen layouts with the largest accessibility font setting.

Source:
- https://docs.flutter.dev/ui/accessibility/ui-design-and-styling

Android 14 introduced nonlinear font scaling up to 200%. Flutter documents that custom UI should migrate from scalar `textScaleFactor` assumptions to `TextScaler`, and recommends testing at the maximum 200% setting.

Source:
- https://docs.flutter.dev/release/breaking-changes/android-14-nonlinear-text-scaling-migration
- https://docs.flutter.dev/release/breaking-changes/deprecate-textscalefactor

### MintTap product source

MintTap 1.0.29 contains:

- a compact-iOS global text-scaling clamp in the application builder;
- very small shared typography roles, including 9–14 px classes;
- dense financial rows with fixed-width numeric slots and many localized labels;
- eleven language variants in the custom string system;
- high-value financial strings combining sign, currency, amount, rate, estimate/finality and date context.

The Product Lab branch deliberately removes the global compact-iOS clamp from the isolated lab entrypoint and uses responsive stack/reflow decisions instead.

## SYNTHESIS

### 1. Scaling is a composition input, not only a font-size input

With nonlinear scaling, an interface cannot safely derive every surrounding dimension from one scalar multiplier. A financial row that is stable at 1.0 may need a different composition at high scaling:

`Ticker | amount | signed rate`

can become:

`Ticker`
`amount`
`signed rate`

without changing the semantic order.

### 2. Global text suppression can hide the wrong failure

A product-level clamp may reduce visible clipping while preserving an underlying dependency on small type, fixed widths and dense horizontal packing. For Product Lab validation, the preferred method is:

`natural platform scaling → observe failure → recompose/wrap/stack/disclose → retest`

rather than:

`observe pressure → globally cap scaling → declare geometry stable`.

### 3. Financial hierarchy must survive enlargement

The following roles should remain distinguishable when enlarged:

1. primary portfolio/position value;
2. total economic outcome;
3. section title;
4. metric value;
5. label/body;
6. supporting status/provenance.

Hierarchy cannot depend solely on a large spread in absolute font sizes because nonlinear scaling changes those relationships. Weight, spacing, grouping, placement and content order must reinforce the hierarchy.

### 4. Long financial strings are a Type × Content stress corpus

Required strings include:

- `-₩123,456,789 (-12.34%)`;
- `$123,456.78`;
- `Net estimated distributions`;
- `Estimated ROC share`;
- `USD → KRW exchange rate`;
- long portfolio names;
- localized status qualifiers such as Actual / Estimated / Partial / Unavailable.

These should be tested as complete semantic strings. Content must not be shortened merely to make a preferred geometry pass.

## PRACTICE — MintTap isolated Product Lab

The Product Lab foundation now:

- does not apply the production compact-iOS global scale clamp;
- uses `MediaQuery.textScalerOf(context).scale(...)` as a pressure signal rather than a universal scalar geometry formula;
- stacks paired metrics under narrow or enlarged-text conditions;
- stacks holding rows and key/value rows under pressure;
- keeps explicit state labels when space is constrained.

This is source-level implementation evidence only until a Flutter-capable environment renders it.

## CRITIQUE

The lab currently uses fixed authored font sizes for semantic roles. That is acceptable for a bounded prototype but does not establish an optimal production type scale.

Risks still open:

- actual iOS Dynamic Type categories;
- Android nonlinear scaling behavior on the product's supported Flutter version;
- numeral fallback/raster quality across locales/platforms;
- line-break quality in Korean/Japanese/Arabic-like long strings;
- VoiceOver/TalkBack reading order;
- chart labels and data-table density;
- whether 200% stress causes excessive task length or hidden controls.

## Gate relationship

T024 is **not** permission to bypass the custom-type drawing sequence.

- T021 drawing repair remains prerequisite for custom glyph promotion.
- spacing remains closed until drawing evidence passes;
- kerning remains closed until spacing evidence passes;
- mature fallback remains the product-safe choice where the custom face is not ready.

Product scaling evidence and glyph drawing evidence are separate gates.

## RELATED DOMAIN CHECK

### Type
T022/T023 financial-string corpus and product string gate are reused. T024 extends them into nonlinear scaling and recomposition.

### Color
State labels must remain understandable without relying on color. Enlarged text may alter colored surface mass, so semantic color hierarchy must be rechecked after reflow.

### Layout / Interaction
Layout owns the actual stack/reflow breakpoint and target geometry. Type supplies string/render pressure and hierarchy requirements.

### Web
Browser zoom and Flutter web semantics are a separate transfer surface. Mobile text scaling PASS does not imply browser zoom/reflow PASS.

### Content
Necessary qualifiers must remain available. Content shortening is not a substitute for layout resilience.

## HANDOFFS TO OTHER SPECIALISTS

### Layout / Interaction
Use the same financial stress strings and large-text conditions when validating L046/I042 workflow recomposition.

### Web
Record text-scaling/zoom method in the W055 artifact identity; do not label a proportional lab scale as field/browser evidence.

### Content
CD061 should preserve terminology qualifiers through enlarged-text states and localization.

## Evidence level

`SOURCE → PRODUCT SOURCE AUDIT → TRANSFER IMPLEMENTATION → RUNTIME OPEN → DEVICE/AT/HUMAN OPEN`

No Stage 2 PASS is claimed from T024.
