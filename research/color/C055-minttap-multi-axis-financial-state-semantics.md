# C055 — MintTap Multi-Axis Financial State Semantics

Status: **TRANSFER VALIDATION / PRODUCT SEMANTIC SYSTEM / RUNTIME OPEN**  
Date: 2026-09-17  
Stage relevance: Stage 3 systems practice

## Question

How should a financial product encode brand identity, outcome polarity, certainty/finality and data availability without collapsing them into one color meaning?

## SOURCE

MintTap 1.0.29 currently has a very small global color token surface (`brandMint`, `brandMintSoft`, `textPrimary`) while major screens define many local colors.

The localization layer already contains locale-sensitive market polarity behavior:

- default convention: positive green / negative red;
- Korean/Japanese convention: positive red / negative blue.

Therefore a single global assumption such as `green = good`, `red = bad`, or `mint = positive` is not a valid product-wide semantic contract.

Prior C054 established a contradiction case: a user may have high cumulative distributions while total economic performance is negative.

## SYNTHESIS

The product needs at least four independent semantic axes.

### Axis A — identity / emphasis

Examples:

- MintTap brand;
- selected product/navigation emphasis;
- neutral primary action.

Brand mint belongs here.

### Axis B — financial polarity

Examples:

- positive total performance;
- negative total performance;
- gain/loss rate.

Polarity may map to locale conventions and requires redundant non-color cues such as sign, direction and wording.

### Axis C — certainty / evidence state

Examples:

- actual/paid;
- estimated/projected;
- final issuer data;
- provisional calculation.

Estimated is not inherently good/bad and must not borrow polarity semantics.

### Axis D — availability / integrity

Examples:

- ready;
- partial;
- unavailable;
- failed/retry;
- action required.

Partial/unavailable describes evidence completeness, not investment outcome.

## Required contradiction matrix

A robust semantic system must represent combinations such as:

| Outcome | Certainty | Availability | Required interpretation |
| --- | --- | --- | --- |
| positive | actual | ready | positive confirmed outcome |
| negative | actual | ready | negative confirmed outcome |
| positive | estimated | ready | positive projected outcome |
| negative | estimated | ready | negative projected outcome |
| neutral | estimated | partial | estimate based on incomplete data |
| unknown | unknown | unavailable | no outcome inference allowed |

No single color token can encode the full matrix.

## PRACTICE — MintTap Product Lab

The isolated lab foundation now separates:

- `brand` / `brandContainer`;
- `positive` / `negative`;
- `estimated`;
- `partial`;
- `unavailable`;
- `warning` / `info`;
- surface and text hierarchy.

The high-income/negative-total-return scenario intentionally shows distribution values without converting the whole interface into a positive/success state.

This is product-source transfer evidence, not rendered-device evidence.

## CRITIQUE

The current lab palette is provisional. It has not yet established:

- WCAG contrast ratios for every foreground/background/state pair;
- forced-colors/high-contrast behavior;
- grayscale survival;
- color-vision deficiency robustness;
- light-theme behavior;
- locale-specific market convention implementation;
- OLED/direct-sunlight/device reproduction;
- chart series discrimination;
- physical-device observer evidence.

The next execution artifact must test semantic roles, not merely compare hex values.

## RELATED DOMAIN CHECK

### Type
Text/sign qualifiers are required redundant cues. C055 cannot rely on color-only state communication.

### Layout / Interaction
Status state must remain associated with the correct metric after stacking/reflow/filtering. Spatial proximity is part of semantic integrity.

### Web
Forced colors and browser/system overrides can replace authored colors. The meaning must survive those transformations.

### Content
`Estimated`, `Partial data`, `Unavailable`, `Final` and financial outcome labels verbalize state. Content must not collapse evidence state into generic success/error language.

### UX integration
The portfolio workflow must not visually celebrate income if total performance is negative. Primary hierarchy and color hierarchy must agree.

## HANDOFFS TO OTHER SPECIALISTS

### Layout / Interaction
Validate status association after large-text stack/reflow and dense-list recomposition.

### Web
W055 should include forced-colors/grayscale and exact artifact identity when browser execution becomes available.

### Content
CD061 should define exact language for evidence state and financial polarity combinations.

## Gate effect

C055 strengthens Stage 3 systems practice but does **not** establish Stage 3 PASS. Runtime, alternate-mode, cross-platform and human/observer evidence remain OPEN.
